module KatelloUtilities
  module Helper
    def last_scenario
      if File.exist?(last_scenario_yaml)
        File.basename(File.readlink(last_scenario_yaml)).split(".")[0]
      else
        'katello'
      end
    end

    def scenarios_path
      '/etc/foreman-installer/scenarios.d'
    end

    def last_scenario_yaml
      "#{scenarios_path}/last_scenario.yaml"
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
      STDOUT.puts message.red
      puts opt_parser if opt_parser
      exit(false)
    end

    def fail_if_file_not_found(files)
      files.reject! { |file| File.exist?(file) }
      if files.any?
        multiple_files = files.count > 1
        fail_with_message("Error: #{multiple_files ? "Files" : "File"} #{files.join(", ")} " \
                          "#{multiple_files ? "do" : "does"} not exist! Please check the file path and try again.")
      end
    end

    def run_cmd(command, exit_codes=[0], message=nil, &block)
      result = `#{command}`
      exit_code = $?.exitstatus
      success = $?.success?

      yield(result, success) if block_given?

      unless exit_codes.include?(exit_code)
        STDOUT.puts result
        STDOUT.puts message.red if message
        failed_command = "Failed '#{command}' with exit code #{exit_code}"
        if self.respond_to? :cleanup
          STDOUT.puts failed_command
          cleanup(exit_code)
        end
        fail_with_message(failed_command)
      end

      result
    end

    def timestamp
      DateTime.now.strftime('%Y%m%d%H%M%S')
    end

    class ::String
      def red
        colorize(31)
      end

      def green
        colorize(32)
      end

      def gray
        colorize(37)
      end

      private

      def colorize(color_code)
        "\e[#{color_code}m#{self}\e[0m"
      end
    end
  end
end
