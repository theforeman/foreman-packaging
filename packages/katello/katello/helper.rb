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
      if File.exist?('/var/lib/foreman-installer/scenarios.d')
        '/var/lib/foreman-installer/scenarios.d'
      else
        '/etc/foreman-installer/scenarios.d'
      end
    end

    def hammer_root_config_path
      '/root/.hammer/cli.modules.d'
    end

    def hammer_config_path
      '/etc/hammer/cli.modules.d'
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

    def load_scenario_data(scenario)
      YAML.load_file(File.join(scenarios_path, "#{scenario}.yaml"))
    end

    def load_scenario_answers(scenario)
      data = load_scenario_data(scenario)
      unless data && data[:answer_file]
        fail_with_message("Could not determine answers file location for scenario '#{scenario}'")
      end
      YAML.load_file(data[:answer_file])
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
