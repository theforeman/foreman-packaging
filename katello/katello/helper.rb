require 'pathname'
require_relative 'db_config'

module KatelloUtilities
  module Helper
    def last_scenario_config
      Pathname.new("/etc/foreman-installer/scenarios.d/last_scenario.yaml").realpath.to_s
    end

    def last_scenario
      File.basename(last_scenario_config).split(".")[0]
    end

    def accepted_scenarios
      @accepted_scenarios || ["katello", "foreman-proxy-content"]
    end

    def error_message
      "This utility can't run on a non-katello system."
    end

    def foreman_rpm_installed?
      system("rpm -q foreman > /dev/null")
    end

    def load_scenario_answers(scenario)
      YAML.load_file("/etc/foreman-installer/scenarios.d/#{scenario}-answers.yaml")
    end

    def disable_system_check_option?
      katello_installer_version = run_cmd("rpm -q --queryformat '%{RPMTAG_VERSION}' katello-installer-base")
      Gem::Version.new(katello_installer_version) >= Gem::Version.new("3.2.0")
    end

    def fail_with_message(message, opt_parser=nil)
      STDOUT.puts message
      puts opt_parser if opt_parser
      exit(false)
    end

    def run_cmd(command, exit_codes=[0], message=nil)
      result = `#{command}`
      unless exit_codes.include?($?.exitstatus)
        STDOUT.puts result
        STDOUT.puts message if message
        failed_command = "Failed '#{command}' with exit code #{$?.exitstatus}"
        if self.respond_to? :cleanup
          STDOUT.puts failed_command
          cleanup($?.exitstatus)
        end
        fail_with_message(failed_command)
      end
      result
    end

    def timestamp
      DateTime.now.strftime('%Y%m%d%H%M%S')
    end

    def db_config
      @katello_db_config ||= KatelloUtilities::DBConfig.new(last_scenario_config)
    end
  end
end
