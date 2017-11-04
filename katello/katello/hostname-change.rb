require "socket"
require "optparse"
require "rubygems"
require "yaml"
require "shellwords"
require "json"
require "uri"
require_relative "helper.rb"

module KatelloUtilities
  class HostnameChange
    include ::KatelloUtilities::Helper

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

    def yesno
      begin
        system("stty raw -echo")
        str = STDIN.getc
      ensure
        system("stty -raw echo")
      end
      if str.chr.downcase == "y"
        return true
      elsif str.chr.downcase == "n"
        return false
      else
        puts "Invalid Character. Try again: [y/n]"
        self.yesno
      end
    end

    def check_for_certs_tar
      STDOUT.puts "Checking for certs tarball"
      if @options[:certs_tar]
        if File.file?(@options[:certs_tar])
          true
        else
          self.fail_with_message("#{@options[:certs_tar]} does not exist! Please check the file path and try again")
        end
      else
        self.fail_with_message("You must specify --certs-tar argument when on a #{@proxy}." \
                               " These can be generated on the #{@default_program} server using " \
                               "#{@proxy.downcase.gsub(" ", "-")}-certs-generate and copied to this machine.")
      end
    end

    def get_fpc_answers
      register_in_foreman = false
      certs_tar = @options[:certs_tar]
      " --foreman-proxy-register-in-foreman #{register_in_foreman} --foreman-proxy-content-certs-tar #{certs_tar}"
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

      STDOUT.puts "\nChecking hostname validity"
      # This regex is an approximation of a hostname, it will handle most invalid hostnames and typos.
      # Taken from https://www.safaribooksonline.com/library/view/regular-expressions-cookbook/9781449327453/ch08s15.html
      hostname_regex = /^([a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,}$/
      unless hostname_regex === @new_hostname
        self.fail_with_message("#{@new_hostname} is not a valid fully qualified domain name, please use a valid FQDN and try again. " \
                          "No changes have been made to your system.");
      end

      unless @foreman_proxy_content
        STDOUT.puts "\nChecking overall health of server"
        self.run_cmd("hammer ping", [0], "There is a problem with the server, please check 'hammer ping'")
        STDOUT.puts "\nChecking credentials"
        self.hammer_cmd("capsule list", [0], "There is a problem with the credentials, please retry")
      end

      if @options[:confirm]
        response = true
      else
        STDOUT.print(self.warning_message)
        response = self.yesno
      end

      unless response
        self.fail_with_message("Hostname change aborted, no changes have been made to your system")
      end
    end

    def successful_hostname_change_message
    # the following multi-line string isn't indented because the indents are taken literally.
    successful_message = %(
  If you want to use custom certificates, re-run the #{@options[:program]}-installer with custom certificate options.

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
      STDOUT.puts "**** Hostname change complete! **** \nIMPORTANT:"
      if @foreman_proxy_content
        STDOUT.print "You will have to update the Name and URL of the Smart Proxy in #{@options[:program].capitalize} to the new hostname.\n"
      else
        STDOUT.print successful_message
      end
      STDOUT.print ""
      exit(true)
    end

    def warning_message
      STDOUT.print("***WARNING*** This script will modify your system. " \
                   "You will need to re-register any #{@options[:program]} clients registered to this system after script completion.")
      unless @foreman_proxy_content
        STDOUT.print(" #{ @plural_proxy } will have to be re-registered and reinstalled. If you are using custom certificates, you " \
                     "will have to run the #{@options[:program]}-installer again with custom certificate options after this script completes.")
      end
      STDOUT.print(" Have you taken the necessary precautions (backups, snapshots, etc...) and want to proceed with " \
                   "changing your hostname? \n [y/n]:")
    end

    def hammer_cmd(cmd, exit_codes=[0], message=nil)
      run_cmd("hammer -u #{@options[:username].shellescape} -p #{@options[:password].shellescape} #{cmd}", exit_codes, message)
    end

    def get_default_proxy_id
      output = hammer_cmd("--output json capsule info --name #{@old_hostname}",
                          [0], "Couldn't find default #{@proxy} id")
      proxy = JSON.parse(output)
      proxy["Id"]
    end

    def setup_opt_parser
      @opt_parser = OptionParser.new do |opt|
        opt.banner = "usage: #{@command_prefix}-change-hostname hostname [options]"
        opt.separator  ""
        opt.separator  "example:"
        opt.separator  "#{@command_prefix}-change-hostname foo.example.com -u admin -p changeme"
        opt.separator  ""
        opt.separator  "options"

        opt.on("-u","--username username","admin username (required)") do |username|
          @options[:username] = username
        end

        opt.on("-p","--password password","admin password (required)") do |password|
          @options[:password] = password
        end

        opt.on("-g","--program program","name of the program you are modifying (defaults to #{@default_program})") do |program|
          @options[:program] = program
        end

        opt.on("-s","--scenario scenario","name of the scenario you are modifying (defaults to #{@last_scenario})") do |scenario|
          @options[:scenario] = scenario
        end

        opt.on("-y", "--assumeyes", "answer yes for all questions") do |confirm|
          @options[:confirm] = confirm
        end

        if @foreman_proxy_content
          opt.on("-c",
                 "--certs-tar certs_tar",
                 "the path to the certs tar generated on the #{@default_program} server with the new hostname (required for #{@plural_proxy})") do |certs_tar|
            @options[:certs_tar] = certs_tar
          end
        end

        opt.on("-h","--help","help") do
          puts @opt_parser
          exit
        end
      end
      @opt_parser.parse!
    end

    def run
      raise 'Must run as root' unless Process.uid == 0

      self.precheck

      if @foreman_proxy_content
        self.check_for_certs_tar
        fpc_installer_args = self.get_fpc_answers
      end

      # Get the hostname from your system
      @old_hostname = self.get_hostname

      scenario_answers = load_scenario_answers(@options[:scenario])

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

      STDOUT.puts "stopping services"
      self.run_cmd("katello-service stop")

      public_dir = "/var/www/html/pub"
      public_backup_dir = "#{public_dir}/#{@old_hostname}-#{self.timestamp}.backup"
      STDOUT.puts "deleting old certs"

      self.run_cmd("rm -rf /etc/pki/katello-certs-tools{,.bak}")
      self.run_cmd("rm -rf #{scenario_answers["foreman_proxy"]["ssl_cert"]}")
      self.run_cmd("rm -rf #{scenario_answers["foreman_proxy"]["ssl_key"]}")
      self.run_cmd("rm -rf #{scenario_answers["foreman_proxy"]["foreman_ssl_cert"]}")
      self.run_cmd("rm -rf #{scenario_answers["foreman_proxy"]["foreman_ssl_key"]}")
      self.run_cmd("rm -rf /etc/pki/katello/nssdb")
      self.run_cmd("mkdir #{public_backup_dir}")
      self.run_cmd("mv #{public_dir}/*.rpm #{public_backup_dir}")

      unless @foreman_proxy_content
        self.run_cmd("rm -rf /etc/candlepin/certs/amqp{,.bak}")
        self.run_cmd("rm -f /etc/tomcat/keystore")
        self.run_cmd("rm -rf /etc/foreman/old-certs")
        self.run_cmd("rm -f /etc/pki/katello/keystore")
        self.run_cmd("rm -rf #{scenario_answers["foreman"]["client_ssl_cert"]}")
        self.run_cmd("rm -rf #{scenario_answers["foreman"]["client_ssl_key"]}")
      end

      STDOUT.puts "backed up #{public_dir} to #{public_backup_dir}"
      STDOUT.puts "updating hostname in /etc/hosts"
      self.run_cmd("sed -i -e 's/#{@old_hostname}/#{@new_hostname}/g' /etc/hosts")

      STDOUT.puts "updating hostname in foreman installer scenarios"
      self.run_cmd("sed -i -e 's/#{@old_hostname}/#{@new_hostname}/g' /etc/foreman-installer/scenarios.d/*.yaml")

      STDOUT.puts "removing last_scenario.yml file"
      self.run_cmd("rm -rf /etc/foreman-installer/scenarios.d/last_scenario.yaml")

      STDOUT.puts "re-running the installer"

      installer = "#{@options[:program]}-installer --scenario #{@options[:scenario]} -v"
      if @foreman_proxy_content
        installer << fpc_installer_args
      else
        installer << " --certs-regenerate=true --foreman-proxy-register-in-foreman true"
      end
      # always disable system checks to avoid unnecessary errors. The installer should have
      # already ran since this is to be run on an existing system and installer checks would
      # have already been skipped
      installer << " --disable-system-checks" if disable_system_check_option?

      STDOUT.puts installer
      installer_output = self.run_cmd("#{installer}")
      installer_success = $?.success?
      STDOUT.puts installer_output

      STDOUT.puts "Restarting puppet services"
      self.run_cmd("/sbin/service puppet restart")
      self.run_cmd("katello-service restart --only puppetserver")

      if installer_success
        self.successful_hostname_change_message
      else
        self.fail_with_message("Something went wrong with the #{@options[:scenario].capitalize} installer! Please check the above output and the corresponding logs")
      end
    end
  end
end
