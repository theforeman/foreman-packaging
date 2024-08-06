require "socket"
require "optparse"
require "rubygems"
require "yaml"
require "shellwords"
require "json"
require "uri"
require "fileutils"
require "highline/import"
require "tempfile"
require "resolv"
require_relative "helper.rb"

module KatelloUtilities
  class HostnameChange
    include ::KatelloUtilities::Helper

    def initialize(init_options)
      @last_scenario = self.last_scenario

      @proxy = init_options.fetch(:proxy)
      @plural_proxy = init_options.fetch(:plural_proxy)
      @proxy_hyphenated = init_options.fetch(:proxy_hyphenated)
      @command_prefix = init_options.fetch(:command_prefix)
      @accepted_scenarios = init_options.fetch(:accepted_scenarios, nil)

      @default_program = self.get_default_program

      @options = {}
      @options[:program] = init_options.fetch(:program, @default_program)
      @options[:scenario] = init_options.fetch(:scenario, @last_scenario)
      @scenario_answers = load_scenario_answers(@options[:scenario])
      @foreman_proxy_content = @options[:scenario] == @proxy_hyphenated

      setup_opt_parser
    end

    def get_default_program
      case @last_scenario
      when "katello"
        return "foreman"
      when @proxy_hyphenated
        return "foreman"
      else
        return @last_scenario
      end
    end

    def get_hostname
      Socket.gethostname.chomp
    end

    def check_for_certs_tar
      STDOUT.puts "Checking for certs tarball"
      if @options[:certs_tar]
        fail_if_file_not_found([@options[:certs_tar]])
      else
        self.fail_with_message("You must specify --certs-tar argument when on a #{@proxy}." \
                               " These can be generated on the #{@default_program} server using " \
                               "#{@proxy.downcase.gsub(" ", "-")}-certs-generate and copied to this machine.")
      end
    end

    def get_fpc_answers
      register_in_foreman = false
      certs_tar = @options[:certs_tar]
      " --foreman-proxy-register-in-foreman #{register_in_foreman} --certs-tar-file #{certs_tar}"
    end

    def precheck
      unless @options[:username] && @options[:password]
        self.fail_with_message("Username and/or Password options are missing!", @opt_parser)
      end

      if ARGV[0] && ARGV.count >= 1
        @new_hostname = ARGV[0]
      else
        self.fail_with_message("Please specify a hostname.", @opt_parser)
      end

      if @old_hostname == @new_hostname
        self.fail_with_message("The hostname specified must be different from the current hostname. If you have changed the hostname" \
                              " with another utility, please change it back to the original hostname before running this tool.")
      end

      STDOUT.puts "\nChecking hostname validity"
      # This regex is an approximation of a hostname, it will handle most invalid hostnames and typos.
      # Taken from https://www.safaribooksonline.com/library/view/regular-expressions-cookbook/9781449327453/ch08s15.html
      hostname_regex = /^([a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,}$/
      unless hostname_regex === @new_hostname
        self.fail_with_message("#{@new_hostname} is not a valid fully qualified domain name. Please use a valid FQDN and try again. " \
                          "No changes have been made to your system.");
      end

      unless @foreman_proxy_content
        STDOUT.puts "\nChecking overall health of server"
        self.run_cmd("hammer ping", [0], "There is a problem with the server; please check 'hammer ping'")
        STDOUT.puts "\nChecking credentials"
        self.hammer_cmd("capsule list", [0], "There is a problem with the credentials; please retry")
      end

      if should_update_dns?
        begin
          STDOUT.puts "\nAssembling data for DNS update"
          @answers_dns_values = answers_dns_values
          @assembled_nsupdate_command = assembled_nsupdate_command(@answers_dns_values)
        rescue StandardError => e # could not reach the DNS server, or something broke while assembling the data
          STDOUT.puts e
          fail_with_message("Error querying local DNS server for #{@old_hostname}. Make sure the 'named' service is running, or re-run with the --skip-dns option.")
        end

        @answers_dns_values.each do |field, v|
          next unless v.nil?
          fail_with_message """
    Error gathering DNS data: couldn't find value for '#{field}'
    Make sure #{scenarios_path}/#{@options[:scenario]}-answers.yaml
    has not been modified, or re-run with the --skip-dns option.
"""
        end

      end

      return if @options[:confirm]
      questions = []
      questions << dns_skip_warning if @options[:skip_dns]
      questions << warning
      questions.each do |q|
        STDOUT.puts
        STDOUT.puts q[:message]
        unless agree(q[:question])
          self.fail_with_message("Hostname change aborted; no changes have been made to your system")
        end
      end
      STDOUT.puts "Precheck passed"
    end

    def next_steps_message
      if @foreman_proxy_content
        "You will have to update the Name and URL of the Smart Proxy in #{@options[:program].capitalize} to the new hostname.\n"
      else
        # the following multi-line string isn't indented because the indents are taken literally.
%(
  You will have to install the new bootstrap rpm and reregister all clients and #{@plural_proxy} with subscription-manager
  (update organization and environment arguments appropriately):

  set -o pipefail && curl -sS "http://#{@new_hostname}/unattended/public/foreman-ca-refresh" | bash
  subscription-manager register --org="Default_Organization" --environment="Library" --force

  Then reattach subscriptions to the client(s) and run:

  subscription-manager refresh
  yum repolist


  On all #{@plural_proxy}, you will need to re-run the #{@options[:program]}-installer with this command:

  #{@options[:program]}-installer --foreman-proxy-foreman-base-url https://#{@new_hostname} \\
                                  --foreman-proxy-trusted-hosts #{@new_hostname}

  If Puppet is enabled on the #{@proxy}, add the following to the installer command:

                                  --puppet-server-foreman-url https://#{@new_hostname}

  Short hostnames have not been updated, please update those manually.\n
)
      end
    end

    def warning
      msg = <<-HEREDOC
***WARNING*** This script will modify your system.
You will need to re-register any #{@options[:program]} clients registered to this system after script completion.
      HEREDOC
      unless @foreman_proxy_content
        msg << "#{@plural_proxy} will have to be re-registered and reinstalled. If you are using custom certificates,\n" \
                     "you will have to run the #{@options[:program]}-installer again with custom certificate options after this script completes.\n"
      end
      msg << " Have you taken the necessary precautions (backups, snapshots, etc...)?\n"
      {
        message: msg,
        question: 'Proceed with changing your hostname? [y/n]'
      }
    end

    def dns_skip_warning
      msg = <<-HEREDOC
***WARNING*** Since the --skip-dns option was specified, nsupdate will NOT be run and
DNS records will NOT be created for #{@new_hostname}. You will need to do the following manually:

- Remove the A and NS records for #{@old_hostname}
- Update the SOA record for #{@new_hostname}
- Create new A and NS records for #{@new_hostname}

If not done, all hosts will lose connection to #{@options[:scenario]} and discovery may not work.
      HEREDOC
      {
        message: msg,
        question: 'Proceed without updating DNS? [y/n]'
      }
    end

    def hammer_cmd(cmd, exit_codes=[0], message=nil)
      run_cmd("LANG=en_US.UTF-8 hammer -u #{@options[:username].shellescape} -p #{@options[:password].shellescape} #{cmd}", exit_codes, message)
    end

    def curl_cmd(method, url, exit_codes=[0], message=nil)
      run_cmd("curl --silent --user #{@options[:username].shellescape}:#{@options[:password].shellescape} --request #{method} https://#{@old_hostname}/#{url}", exit_codes, message)
    end

    def get_default_proxy_id
      output = hammer_cmd("--output json capsule info --name #{@old_hostname}",
                          [0], "Couldn't find default #{@proxy} id")
      proxy = JSON.parse(output)
      proxy["Id"]
    end

    def using_custom_certs?(scenario_answers)
      scenario_answers["certs"]["server_cert"] &&
      scenario_answers["certs"]["server_key"]
    end

    def delete_puppet_certs
      return unless @scenario_answers['puppet'].is_a?(Hash)

      puppet_ssldir = @scenario_answers['puppet']['ssldir']

      run_cmd("rm -rf '#{puppet_ssldir}'")
    end

    def all_custom_cert_options_present?
      @options[:custom_cert] && @options[:custom_key]
    end

    def custom_certs_check(scenario_answers)
      if all_custom_cert_options_present?
        if FileUtils.compare_file(scenario_answers["foreman"]["server_ssl_ca"],
                                  scenario_answers["foreman"]["server_ssl_chain"])
          fail_with_message("This system is set up with custom certificates, but those certificates " \
                            "are using the same CA as the default #{@default_program} CA. " \
                            "Please fix this and re-run #{@default_program}-change-hostname.")
        end
      else
        fail_with_message("You are currently using custom certificates but not all custom " \
                          "certificate arguments are present. To change the hostname, " \
                          "you need to provide certificates with the new hostname. Please " \
                          "review the custom certificate arguments required with --help.")
      end
    end

    def setup_opt_parser
      @opt_parser = OptionParser.new do |opt|
        opt.banner = "usage: #{@command_prefix}-change-hostname hostname [options]"
        opt.separator  ""
        opt.separator  "example:"
        opt.separator  "#{@command_prefix}-change-hostname newhost.example.com -u admin -p changeme"
        opt.separator  ""
        opt.separator  "options"

        opt.on("-u","--username username","admin username (required)") do |username|
          @options[:username] = username
        end

        opt.on("-p","--password password","admin password (required)") do |password|
          @options[:password] = password
        end

        opt.on("-y", "--assumeyes", "answer yes for all questions") do |confirm|
          @options[:confirm] = confirm
        end

        opt.on("--skip-dns", "skip updating DNS records even if they are managed by #{@options[:scenario]}") do |skip_dns|
          @options[:skip_dns] = skip_dns
        end

        if @foreman_proxy_content
          opt.on("-c",
                 "--certs-tar certs_tar",
                 "the path to the certs tar generated on the #{@default_program} server with the new hostname (required for #{@plural_proxy})") do |certs_tar|
            @options[:certs_tar] = File.expand_path(certs_tar)
          end
        else
          if using_custom_certs?(@scenario_answers)
            opt.on("-c","--custom-cert CERT","If you are using custom certificates, please provide a server cert with the new hostname") do |custom_cert|
              @options[:custom_cert] = File.expand_path(custom_cert)
            end

            opt.on("-k","--custom-key KEY","If you are using custom certificates, please provide a server key with the new hostname") do |custom_key|
              @options[:custom_key] = File.expand_path(custom_key)
            end
          end
        end

        opt.on("-h","--help","help") do
          puts @opt_parser
          exit
        end
      end
      begin
        @opt_parser.parse!
      rescue OptionParser::InvalidOption => error
        self.fail_with_message("#{error}", @opt_parser)
        exit
      end
    end

    def dns_managed?
      @scenario_answers['foreman_proxy'].is_a?(Hash) &&
        @scenario_answers['foreman_proxy']['dns'] &&
        @scenario_answers['foreman_proxy']['dns_managed'] &&
        @scenario_answers['foreman_proxy']['dns_provider'] == 'nsupdate'
    end

    def should_update_dns?
      dns_managed? && !@options[:skip_dns]
    end

    def answers_dns_values
      {
        nameserver_ip: @scenario_answers['foreman_proxy']['dns_server'],
        zone: @scenario_answers['foreman_proxy']['dns_zone'],
        key_file: @scenario_answers['foreman_proxy']['keyfile'],
        reverse_zones: [@scenario_answers['foreman_proxy']['dns_reverse']].flatten.compact
      }
    end

    def nsupdate_command(dns_entries, key_file)
      "echo -e \"#{dns_entries}\" | nsupdate -l -k #{key_file}"
    end

    def update_zone(zone, resolver)
      commands = []

      soa = resolver.getresource(zone, Resolv::DNS::Resource::IN::SOA)
      commands << "update add #{zone} #{soa.ttl} SOA #{@new_hostname}. #{soa.rname} #{soa.serial + 1} #{soa.refresh} #{soa.retry} #{soa.expire} #{soa.minimum}"

      commands << "update add #{zone}. 3600 IN NS #{@new_hostname}."
      commands << "update delete #{zone}. IN NS #{@old_hostname}"

      return commands if zone.end_with?('arpa') # don't modify A records for reverse zones

      begin
        a_record = resolver.getresource(@old_hostname, Resolv::DNS::Resource::IN::A)
        commands << "update delete #{@old_hostname} A"
        commands << "update add #{@new_hostname} #{a_record.ttl} A #{a_record.address}"
      rescue Resolv::ResolvError => e
        # This is fine
      end

      begin
        aaaa_record = resolver.getresource(@old_hostname, Resolv::DNS::Resource::IN::AAAA)
        commands << "update delete #{@old_hostname} AAAA"
        commands << "update add #{@new_hostname} #{aaaa_record.ttl} AAAA #{aaaa_record.address}"
      rescue Resolv::ResolvError => e
        # This is fine
      end

      commands
    end

    def assembled_nsupdate_command(d)
      resolver = Resolv::DNS.new(nameserver: [d[:nameserver_ip]], search: [], ndots: 1)
      commands = ["local #{d[:nameserver_ip]}", "zone #{d[:zone]}"]
      commands += update_zone(d[:zone], resolver)
      commands << "send\n"
      d[:reverse_zones].each do |zone|
        commands << "zone #{zone}"
        commands += update_zone(zone, resolver)
        commands << "send\n"
      end
      commands.join("\n")
    end

    def update_dns_records
      STDOUT.puts 'updating DNS records with nsupdate:'
      # Use nsupdate to update DNS records
      # Update SOA record to new hostname; add new A and NS records; delete old A and NS records.
      # Multi-line strings are not indented because Ruby 2.0 doesn't support <<~ heredocs

      run_cmd('rndc thaw')
      STDOUT.puts @assembled_nsupdate_command
      run_cmd nsupdate_command(@assembled_nsupdate_command, @answers_dns_values[:key_file])
      STDOUT.puts 'updating dynamic zone files...'
      run_cmd('rndc freeze')
      run_cmd('rndc thaw')
      STDOUT.puts 'DNS records updated'
    end

    def restore_last_scenario_yaml
      STDOUT.puts 'restoring last_scenario.yaml'
      if File.exist?(last_scenario_yaml)
        run_cmd("cp #{@temp_last_scenario_yaml.path} #{last_scenario_yaml}")
      else
        # if the installer failed early the last_scenario symlink won't exist
        scenario_path = "#{scenarios_path}/#{@options[:scenario]}.yaml"
        run_cmd("cp #{@temp_last_scenario_yaml.path} #{scenario_path}")
        File.symlink(scenario_path, last_scenario_yaml)
      end
    end

    def run
      raise 'Must run as root' unless Process.uid == 0

      if using_custom_certs?(@scenario_answers)
        custom_certs_check(@scenario_answers)
      end

      if using_custom_certs?(@scenario_answers) && !@foreman_proxy_content
        STDOUT.puts "\nChecking custom certificates"
        fail_if_file_not_found([@options[:custom_cert], @options[:custom_key]])
        run_cmd("katello-certs-check -c #{@options[:custom_cert]} -k #{@options[:custom_key]} " \
                "-b #{@scenario_answers["certs"]["server_ca_cert"]}")
      end

      if @foreman_proxy_content
        self.check_for_certs_tar
        fpc_installer_args = self.get_fpc_answers
      end

      # Get the hostname from your system
      @old_hostname = self.get_hostname

      self.precheck

      if should_update_dns?
        update_dns_records
      end

      STDOUT.puts "updating hostname in /etc/hostname"
      self.run_cmd("sed -i -e 's/#{@old_hostname}/#{@new_hostname}/Ig' /etc/hostname")
      STDOUT.puts "setting hostname"
      self.run_cmd("hostnamectl set-hostname #{@new_hostname}")

      # override environment variable (won't be updated until bash login)
      ENV['HOSTNAME'] = @new_hostname

      STDOUT.puts "checking if hostname was changed"
      if self.get_hostname != @new_hostname
        self.fail_with_message("The new hostname was not changed successfully, exiting script")
      end

      unless @foreman_proxy_content
        STDOUT.puts "\nUpdating default #{@proxy}"
        proxy_id = self.get_default_proxy_id
        self.curl_cmd('DELETE', "/api/v2/instance_hosts/#{@old_hostname}")
        self.curl_cmd('DELETE', "/api/v2/smart_proxies/#{proxy_id}/hosts/#{@old_hostname}")
        # Incorrect error message is piped to /dev/null, can be removed when http://projects.theforeman.org/issues/18186 is fixed
        # For the same reason, we accept exit code 65 here.
        self.hammer_cmd("capsule update --id #{proxy_id} --url https://#{@new_hostname}:9090 --new-name #{@new_hostname} 2> /dev/null", [0, 65])

        STDOUT.puts "Updating installation media paths"
        old_media = JSON.parse(hammer_cmd("--output json medium list --search 'path ~ //#{@old_hostname}/'"))
        old_media.each do |medium|
          new_path = URI.parse(medium['Path'])
          new_path.host = @new_hostname
          new_path = new_path.to_s
          hammer_cmd("medium update --id #{medium['Id']} --path #{new_path}")
        end
      end

      STDOUT.puts "stopping services"
      self.run_cmd("foreman-maintain service stop")

      public_dir = "/var/www/html/pub"
      public_backup_dir = "#{public_dir}/#{@old_hostname}-#{self.timestamp}.backup"

      STDOUT.puts "deleting old certs"
      self.run_cmd("rm -rf /etc/pki/katello-certs-tools{,.bak}")
      self.run_cmd("rm -rf #{@scenario_answers["foreman_proxy"]["ssl_cert"]}")
      self.run_cmd("rm -rf #{@scenario_answers["foreman_proxy"]["ssl_key"]}")
      self.run_cmd("rm -rf #{@scenario_answers["foreman_proxy"]["foreman_ssl_cert"]}")
      self.run_cmd("rm -rf #{@scenario_answers["foreman_proxy"]["foreman_ssl_key"]}")
      self.run_cmd("rm -rf /etc/pki/katello/nssdb")
      self.run_cmd("mkdir #{public_backup_dir}")
      self.run_cmd("mv #{public_dir}/*.rpm #{public_backup_dir}")

      unless @foreman_proxy_content
        self.run_cmd("rm -rf /etc/candlepin/certs/amqp{,.bak}")
        self.run_cmd("rm -f /etc/candlepin/certs/candlepin-ca.crt /etc/candlepin/certs/candlepin-ca.key")
        self.run_cmd("rm -f /etc/candlepin/certs/keystore")
        self.run_cmd("rm -f /etc/candlepin/certs/truststore")
        self.run_cmd("rm -f /etc/tomcat/keystore")
        self.run_cmd("rm -f /etc/tomcat/truststore")
        self.run_cmd("rm -rf /etc/foreman/old-certs")
        self.run_cmd("rm -f /etc/pki/katello/keystore")
        self.run_cmd("rm -f /etc/pki/katello/truststore")
        self.run_cmd("rm -rf #{@scenario_answers["foreman"]["client_ssl_cert"]}")
        self.run_cmd("rm -rf #{@scenario_answers["foreman"]["client_ssl_key"]}")
      end

      delete_puppet_certs

      STDOUT.puts "backed up #{public_dir} to #{public_backup_dir}"
      STDOUT.puts "updating hostname in /etc/hosts"
      self.run_cmd("sed -i -e 's/#{@old_hostname}/#{@new_hostname}/Ig' /etc/hosts")

      STDOUT.puts "updating hostname in foreman installer scenarios"
      self.run_cmd("sed -i -e 's/#{@old_hostname}/#{@new_hostname}/Ig' #{scenarios_path}/*.yaml")

      if File.exist?(hammer_root_config_path) or File.exist?(hammer_config_path)
        STDOUT.puts "updating hostname in hammer configuration"
        [hammer_root_config_path, hammer_config_path].each do |config_dir|
          Dir[File.join(config_dir, "*.yml")].each do |config_file|
            self.run_cmd("sed -i.bak -e 's/#{@old_hostname}/#{@new_hostname}/Ig' #{config_file}")
          end
        end
      end

      if File.exist?(last_scenario_yaml)
        STDOUT.puts 'backing up last_scenario.yaml'
        @temp_last_scenario_yaml = Tempfile.new('last_scenario')
        begin
          @temp_last_scenario_yaml << File.read(last_scenario_yaml)
        ensure
          @temp_last_scenario_yaml.close
        end

        STDOUT.puts 'removing last_scenario.yaml'
        File.unlink(last_scenario_yaml)
      end

      STDOUT.puts "re-running the installer"

      installer = default_installer
      if @foreman_proxy_content
        installer << fpc_installer_args
      else
        if using_custom_certs?(@scenario_answers)
          # The CA must be the same one used for the original certs
          installer << " --certs-server-ca-cert #{@scenario_answers["certs"]["server_ca_cert"]}"
          installer << " --certs-server-cert #{@options[:custom_cert]}"
          installer << " --certs-server-key #{@options[:custom_key]}"
        end
        installer << " --certs-regenerate=true --foreman-proxy-register-in-foreman true"
      end

      STDOUT.puts installer
      run_cmd(installer, [0], installer_failure_message) do |result, success|
        if @temp_last_scenario_yaml && @temp_last_scenario_yaml.path
          unless success
            restore_last_scenario_yaml
          end
          STDOUT.puts 'cleaning up temporary files'
          @temp_last_scenario_yaml.unlink
        end

        if success
          STDOUT.puts result
          puppet_services = ['puppet', 'puppetserver'].select do |service|
            system("systemctl is-active #{service} --quiet")
          end
          if puppet_services.any?
            STDOUT.puts 'Restarting puppet services'
            run_cmd("/bin/systemctl try-restart #{puppet_services.join(' ')}")
          end

          STDOUT.puts "**** Hostname change complete! ****".green
          STDOUT.puts "IMPORTANT:"
          STDOUT.print next_steps_message
          STDOUT.print ""
          exit(true)
        end
      end
    end

    private

    def installer_failure_message
      resolve_text = """
  Once the issue is resolved you may complete the hostname change by running: '#{default_installer}'
  and completing the following steps:\n#{next_steps_message}
"""

"""
  Something went wrong with the #{@options[:scenario].capitalize} installer.
  Please check the above output and the corresponding logs.
  #{resolve_text.gray}
"""
    end

    def default_installer
      "#{@options[:program]}-installer --scenario #{@options[:scenario]}"
    end
  end
end
