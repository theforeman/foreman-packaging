require 'yaml'

module KatelloUtilities
  class DBConfig
    attr_reader :foreman, :candlepin
    INSTALLER_CONFIG = '/etc/foreman-installer/scenarios.d/last_scenario.yaml'

    def initialize(scenario = INSTALLER_CONFIG)
      config = YAML.load(File.read(scenario))
      answers = YAML.load(File.read(config[:answer_file]))
      @foreman = {
          :username => answers['foreman']['db_username'],
          :password => answers['foreman']['db_password'],
          :database => answers['foreman']['db_database'] || 'foreman',
          :host => answers['foreman']['db_host'] || 'localhost',
          :port => answers['foreman']['db_port'] || '5432'
      }
      @candlepin = {
          :username => answers['katello']['candlepin_db_user'],
          :password => answers['katello']['candlepin_db_password'],
          :database => answers['katello']['candlepin_db_name'] || 'candlepin',
          :host => answers['katello']['candlepin_db_host'] || 'localhost',
          :port => answers['katello']['candlepin_db_port'] || '5432',
      }
    end

    def remote_db?(config)
      !['localhost', '127.0.0.1', `hostname`.strip].include? config[:host]
    end

    def any_local_db?
      !remote_db?(foreman) || !remote_db?(candlepin)
    end

    def any_remote_db?
      remote_db?(foreman) || remote_db?(candlepin)
    end

    def pg_command_base(config, command, args)
      "PGPASSWORD='#{config[:password]}' #{command} -U #{config[:username]} -h #{config[:host]} -p #{config[:port]} #{args}"
    end

    def pg_command(config, command, args)
      pg_command_base(config, command, "-d #{config[:database]} #{args}")
    end

    def pg_dump_command(config, dump_file)
      pg_command_base(config, 'pg_dump', "-Fc #{config[:database]} > #{dump_file}")
    end

    def pg_sql_statement(config, statement)
      pg_command(config, 'psql', '-t -c "' + statement + '"')
    end

    # WARNING: deletes all the data from a dabase. No warnings. No confirmations.
    def empty_database!(config)
      generate_delete_statements = pg_sql_statement(config, %q(
        select string_agg('drop table if exists \"' || tablename || '\" cascade;', '')
        from pg_tables
        where schemaname = 'public';
      ))
      delete_statements = `#{generate_delete_statements}`
      system(pg_sql_statement(config, delete_statements)) if delete_statements
    end
  end
end
