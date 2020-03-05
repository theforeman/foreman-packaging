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
require "ostruct"
require_relative "helper.rb"

module KatelloUtilities
  class HostnameChange
    include ::KatelloUtilities::Helper

    attr_accessor :temp_last_scenario_yaml

    def initialize(init_options)
      @default_program = self.get_default_program
      @proxy = init_options.fetch(:proxy)
      @plural_proxy = init_options.fetch(:plural_proxy)
      @proxy_hyphenated = init_options.fetch(:proxy_hyphenated)
      @command_prefix = init_options.fetch(:command_prefix)
      @accepted_scenarios = init_options.fetch(:accepted_scenarios, nil)
      @last_scenario = self.last_scenario

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
          @new_dns_values = new_dns_values
        rescue StandardError => e # could not reach the DNS server, or something broke while assembling the data
          STDOUT.puts e
          fail_with_message("Error querying local DNS server for #{@old_hostname}. Make sure the 'named' service is running, or re-run with the --skip-dns option.")
        end

        %w[dns_server zone soa_admin_domain key_file old_fqdn new_fqdn ip new_serial reverse_soa_records].each do |field|
          next if @new_dns_values[field]

          fail_with_message """
    Error gathering DNS data: couldn't find value for '#{field}'.
    Make sure /etc/foreman-installer/scenarios.d/#{@options[:scenario]}-answers.yaml
    'foreman-proxy' section has values for dns_zone, dns_reverse, and keyfile.
    Make sure A and SOA records are present for #{@old_hostname}.
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

  yum remove -y katello-ca-consumer*
  rpm -Uvh http://#{@new_hostname}/pub/katello-ca-consumer-latest.noarch.rpm
  subscription-manager register --org="Default_Organization" --environment="Library" --force

  Then reattach subscriptions to the client(s) and run:

  subscription-manager refresh
  yum repolist


  On all #{@plural_proxy}, you will need to re-run the #{@options[:program]}-installer with this command:

  #{@options[:program]}-installer --foreman-proxy-content-parent-fqdn #{@new_hostname} \\
                                  --foreman-proxy-foreman-base-url  https://#{@new_hostname} \\
                                  --foreman-proxy-trusted-hosts #{@new_hostname}

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
      @opt_parser.parse!
    end

    def dns_managed?
      @scenario_answers['foreman_proxy']['dns'] &&
        @scenario_answers['foreman_proxy']['dns_managed'] &&
        @scenario_answers['foreman_proxy']['dns_provider'] == 'nsupdate'
    end

    def should_update_dns?
      dns_managed? && !@options[:skip_dns]
    end

    def query_dns_server(fqdn, zone, nameserver_ip)
      query_dns = Resolv::DNS.new(nameserver: [nameserver_ip], search: [], ndots: 1)
      a_record = query_dns.getresource(fqdn, Resolv::DNS::Resource::IN::A)
      ip = a_record.address.to_s if a_record
      soa_record = query_dns.getresource(zone, Resolv::DNS::Resource::IN::SOA)
      serial = soa_record.serial if soa_record
      {
        ip: ip,
        serial: serial
      }
    end

    def new_dns_values
      new_vals = OpenStruct.new

      new_vals.dns_server = @scenario_answers['foreman_proxy']['dns_server']
      new_vals.zone = @scenario_answers['foreman_proxy']['dns_zone']
      new_vals.soa_admin_domain = "root.#{new_vals.zone}"
      new_vals.key_file = @scenario_answers['foreman_proxy']['keyfile']
      new_vals.old_fqdn = @old_hostname
      new_vals.new_fqdn = @new_hostname

      new_vals.reverse_zones = [@scenario_answers['foreman_proxy']['dns_reverse']].flatten
      ip_serial_data = query_dns_server(@old_hostname, new_vals.zone, new_vals.dns_server)
      new_vals.ip = ip_serial_data[:ip]
      serial = ip_serial_data[:serial]
      new_vals.new_serial = serial + 1

      new_vals.reverse_soa_records = new_vals.reverse_zones.map do |reverse_zone|
        reverse_serial = query_dns_server(@old_hostname, reverse_zone, new_vals.dns_server)[:serial]
        {
          reverse_zone: reverse_zone,
          new_reverse_serial: reverse_serial + 1
        }
      end
      run_cmd('rndc thaw')

      new_vals
    end

    def nsupdate_command(dns_entries, key_file)
      "echo -e \"#{dns_entries}\" | nsupdate -l -k #{key_file}"
    end

    def update_zone(zone, nameserver_ip)
      resolver = Resolv::DNS.new(nameserver: [nameserver_ip], search: [], ndots: 1)
      commands = []

      soa = resolver.getresource(zone, Resolv::DNS::Resource::IN::SOA)
      # if soa.mname.to_s == @old_hostname
        commands << "update add #{zone} #{soa.ttl} SOA #{@new_hostname}. #{soa.rname} #{soa.serial + 1} #{soa.refresh} #{soa.retry} #{soa.expire} #{soa.minimum}"
      # end

      nameservers = resolver.getresources(zone, Resolv::DNS::Resource::IN::NS)
      # if nameservers.any? { |ns| ns.name.to_s == @old_hostname }
        # TODO: replace the correct nameserver
        commands << "update add #{zone}. 3600 IN NS #{@new_hostname}."
        commands << "update delete #{zone}. IN NS #{@old_hostname}"
      # end

      return commands if zone.include?('arpa')
      begin
        a_record = resolver.getresource(@old_hostname, Resolv::DNS::Resource::IN::A)
        commands << "update delete #{@old_hostname} A"
        commands << "update add #{@new_hostname} #{a_record.ttl} A #{a_record.address}"
      rescue Resolv::ResolvError
        # This is fine
      end

      begin
        aaaa_record = resolver.getresource(@old_hostname, Resolv::DNS::Resource::IN::AAAA)
        commands << "update delete #{@old_hostname} AAAA"
        commands << "update add #{@new_hostname} #{aaaa_record.ttl} A #{aaaa_record.address}"
      rescue Resolv::ResolvError
        # This is fine
      end

      commands
    end

    def forward_dns_command(d)
      <<-HEREDOC
local #{d.dns_server}
zone #{d.zone}
update add #{d.zone} 10800 SOA #{d.new_fqdn} #{d.soa_admin_domain}. #{d.new_serial} 86400 3600 604800 3600
update add #{d.zone}. 3600 IN NS #{d.new_fqdn}.
update delete #{d.zone}. IN NS #{d.old_fqdn}
update delete #{d.old_fqdn} A
update add #{d.new_fqdn} 86400 A #{d.ip}
send
      HEREDOC
    end

    def assembled_nsupdate_command(d)
      commands = ["local #{d.dns_server}", "zone #{d.zone}"]
      commands += update_zone(d.zone, d.dns_server)
      commands << "send\n"
      d.reverse_zones.each do |zone|
        commands << "zone #{zone}"
        commands += update_zone(zone, d.dns_server)
        commands << "send\n"
      end
      STDOUT.puts(commands.join("\n"))
      commands.join("\n")
    end

    def reverse_dns_command(d)
      result = "local #{d.dns_server}\n"
      d.reverse_soa_records.each do |soa|
        reverse_zone = soa[:reverse_zone]
        new_reverse_serial = soa[:new_reverse_serial]
        result += "zone #{reverse_zone}\n"
        result += <<-HEREDOC
update add #{reverse_zone} 10800 SOA #{d.new_fqdn} root.#{reverse_zone}. #{new_reverse_serial} 86400 3600 604800 3600
update add #{reverse_zone} 3600 IN NS #{d.new_fqdn}
update delete #{reverse_zone} IN NS #{d.old_fqdn}
        HEREDOC
      end
      result += "send\n"
      result
    end

    def update_dns_records(d)
      STDOUT.puts 'updating DNS records:'
      # Use nsupdate to update DNS records
      # Update SOA record to new hostname; add new A and NS records; delete old A and NS records.
      # Multi-line strings are not indented because Ruby 2.0 doesn't support <<~ heredocs

      # STDOUT.puts 'forward...'
      run_cmd nsupdate_command(assembled_nsupdate_command(d), d.key_file)
      # run_cmd nsupdate_command(forward_dns_command(d), d.key_file)
      STDOUT.puts 'updating dynamic zone files...'
      run_cmd('rndc freeze')
      run_cmd('rndc thaw')
      STDOUT.puts 'DNS records updated'
    end

    def restore_last_scenario_yaml
      STDOUT.puts 'restoring last_scenario.yaml'
      if File.exist?(last_scenario_yaml)
        run_cmd("cp #{temp_last_scenario_yaml.path} #{last_scenario_yaml}")
      else
        # if the installer failed early the last_scenario symlink won't exist
        scenario_path = "#{scenarios_path}/#{@options[:scenario]}.yaml"
        run_cmd("cp #{temp_last_scenario_yaml.path} #{scenario_path}")
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
        update_dns_records(@new_dns_values)
      end

      STDOUT.puts "updating hostname in /etc/hostname"
      self.run_cmd("sed -i -e 's/#{@old_hostname}/#{@new_hostname}/g' /etc/hostname")
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

      STDOUT.puts "removing old cert rpms"
      cert_packages = [
        "apache",
        "foreman-client",
        "foreman-proxy",
        "foreman-proxy-client",
        "puppet-client",
        "qpid-broker",
        "qpid-client-cert",
        "qpid-router-client",
        "qpid-router-server",
        "tomcat"
      ]
      cert_rpms = cert_packages.map { |pkg| "#{@old_hostname}-#{pkg}*" }.join(' ')
      self.run_cmd("yum remove -y #{cert_rpms}")

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
        self.run_cmd("rm -f /etc/tomcat/keystore")
        self.run_cmd("rm -rf /etc/foreman/old-certs")
        self.run_cmd("rm -f /etc/pki/katello/keystore")
        self.run_cmd("rm -rf #{@scenario_answers["foreman"]["client_ssl_cert"]}")
        self.run_cmd("rm -rf #{@scenario_answers["foreman"]["client_ssl_key"]}")
      end

      delete_puppet_certs

      STDOUT.puts "backed up #{public_dir} to #{public_backup_dir}"
      STDOUT.puts "updating hostname in /etc/hosts"
      self.run_cmd("sed -i -e 's/#{@old_hostname}/#{@new_hostname}/g' /etc/hosts")

      STDOUT.puts "updating hostname in foreman installer scenarios"
      self.run_cmd("sed -i -e 's/#{@old_hostname}/#{@new_hostname}/g' #{scenarios_path}/*.yaml")

      STDOUT.puts "updating hostname in hammer configuration"
      self.run_cmd("sed -i.bak -e 's/#{@old_hostname}/#{@new_hostname}/g' #{hammer_root_config_path}/*.yml")
      self.run_cmd("sed -i.bak -e 's/#{@old_hostname}/#{@new_hostname}/g' #{hammer_config_path}/*.yml")

      if File.exist?(last_scenario_yaml)
        STDOUT.puts 'backing up last_scenario.yaml'
        temp_last_scenario_yaml = Tempfile.new('last_scenario')
        begin
          temp_last_scenario_yaml << File.read(last_scenario_yaml)
        ensure
          temp_last_scenario_yaml.close
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
        if temp_last_scenario_yaml && temp_last_scenario_yaml.path
          unless success
            restore_last_scenario_yaml
          end
          STDOUT.puts 'cleaning up temporary files'
          temp_last_scenario_yaml.unlink
        end

        if success
          STDOUT.puts result
          STDOUT.puts 'Restarting puppet services'
          run_cmd('/bin/systemctl try-restart puppet')
          run_cmd('foreman-maintain service restart --only puppetserver')

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
      # always disable system checks to avoid unnecessary errors. The installer should have
      # already ran since this is to be run on an existing system and installer checks would
      # have already been skipped
      "#{@options[:program]}-installer --scenario #{@options[:scenario]} -v --disable-system-checks"
    end
  end
end
