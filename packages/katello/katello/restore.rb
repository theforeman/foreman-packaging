require 'rubygems/package'
require 'socket'
require 'optparse'
require 'fileutils'
require 'date'
require_relative "helper.rb"

module KatelloUtilities
  class Restore
    include ::KatelloUtilities::Helper

    def initialize(foreman_proxy_content, program, accepted_scenarios=nil)
      @standard_backup_files = ['config_files.tar.gz', 'pulp_data.tar*']
      @online_backup_files = ['mongo_dump', 'candlepin.dump', 'foreman.dump', 'pg_globals.dump']
      @offline_backup_files = ['mongo_data.tar.gz', 'pgsql_data.tar.gz']
      @foreman_proxy_content_backup_files = ['mongo_data.tar.gz']
      @foreman_proxy_content_online_backup_files = ['mongo_dump']
      @foreman_proxy_content = foreman_proxy_content
      @accepted_scenarios = accepted_scenarios
      @program = program

      @confirmed = false
      @is_foreman_proxy_content = !foreman_rpm_installed?
      @skip_register = false

      setup_opt_parser
    end

    def setup_opt_parser
      @optparse = OptionParser.new do |opts|
        opts.banner = "Usage: #{@program}-restore /path/to/dir [options]\n eg: $ #{@program}-restore /tmp/backup/#{@program}-backup-20171002150106"

        opts.on("-y", "--assumeyes", "Answer yes for all questions") do
          @confirmed = true
        end
      end
      @optparse
    end

    def parse_options
      begin @optparse.parse! ARGV
        if ARGV.length == 0
          @optparse.abort("**** ERROR: Please specify the backup directory to restore ****")
        elsif ARGV.length != 1
          puts @optparse
          exit(-1)
        end

        @dir = ARGV.pop.dup
        unless File.directory?(@dir)
          @optparse.abort("Backup directory does not exist: #{@dir}")
        end
      end
    end

    def set_file_security
      puts "Setting file security"
      run_cmd("restorecon -Rn /")
      puts "Done.\n"
    end

    def reset_katello
      puts "Resetting Katello"
      run_cmd("tar --selinux --overwrite --listed-incremental=/dev/null -xzf config_files.tar.gz -C /")
      installer = "yes | foreman-installer -v --reset"
      if @is_foreman_proxy_content
        installer << " --scenario #{@foreman_proxy_content} --foreman-proxy-register-in-foreman false"
      else
        installer << " --scenario #{@program}"
      end

      # always disable system checks to avoid unnecessary errors. The installer should have
      # already ran since this is to be run on an existing system and installer checks would
      # have already been skipped
      installer << " --disable-system-checks" if disable_system_check_option?
      puts installer
      installer_output = run_cmd(installer, [0,6])
      puts installer_output

      puts "Done.\n"
    end

    def restore_psql_dumps
      puts "Restoring postgres dump files"
      run_cmd("katello-service start --only postgresql")
      run_cmd("runuser - postgres -c 'dropdb foreman'")
      run_cmd("runuser - postgres -c 'dropdb candlepin'")
      run_cmd("runuser - postgres -c 'psql -f #{File.join(@dir, "pg_globals.dump")} postgres 2>/dev/null'")
      run_cmd("runuser - postgres -c 'pg_restore -C -d postgres #{File.join(@dir, "foreman.dump")}'")
      run_cmd("runuser - postgres -c 'pg_restore -C -d postgres #{File.join(@dir, "candlepin.dump")}'")
      run_cmd("katello-service stop --only postgresql")
      puts "Done."
    end

    def migrate_pulp
      puts "Migrating pulp databases"
      necessary_services = "rh-mongodb34-mongod,qpidd"
      pulp_services = "pulp,celerybeat,pulp_workers,pulp_resource_manager"
      run_cmd("katello-service start --only #{necessary_services}")
      run_cmd("katello-service stop --only #{pulp_services}")
      run_cmd("su - apache -s /bin/bash -c pulp-manage-db")
      puts "Done."
    end

    def restore_mongo_dump
      puts "Restoring mongo dump"
      run_cmd("katello-service start --only rh-mongodb34-mongod")
      run_cmd("echo 'db.dropDatabase();' | mongo pulp_database")
      run_cmd("mongorestore --host localhost mongo_dump/pulp_database/")
      run_cmd("katello-service stop --only rh-mongodb34-mongod")
      puts "Done."
    end

    def valid_logical_backup
      base_files_present =  @mongo_dump_exists && @mongo_data_exists
      if @is_foreman_proxy_content
        base_files_present
      else
        base_files_present && @pgsql_data_exists && @candlepin_dump_exists && @foreman_dump_exists
      end
    end

    def valid_online_backup
      @candlepin_dump_exists && @foreman_dump_exists && @mongo_dump_exists && @pg_globals_exist &&
      !(@mongo_data_exists || @pgsql_data_exists)
    end

    def valid_fpc_online_backup
      @mongo_dump_exists &&
      !(@mongo_data_exists || @pgsql_data_exists || @candlepin_dump_exists || @foreman_dump_exists)
    end

    def valid_standard_backup
      @mongo_data_exists && @pgsql_data_exists &&
      !(@candlepin_dump_exists || @foreman_dump_exists || @mongo_dump_exists)
    end

    def valid_fpc_standard_backup
      @mongo_data_exists &&
      !(@pgsql_data_exists || @candlepin_dump_exists || @foreman_dump_exists || @mongo_dump_exists)
    end

    def restore_databases
      puts "Logical backup detected, using the standard backup files to restore" if valid_logical_backup
      if @pulp_data_exists
        puts "Restoring Pulp data"

        tar_command = "tar --selinux --overwrite --listed-incremental=/dev/null "

        if File.exist?('pulp_data.part0002')
          split_tar_script = default_split_tar_script
          tar_command += "-M --new-volume-script=#{split_tar_script} "
        end

        tar_command += "-xf pulp_data.tar -C /"

        run_cmd(tar_command)
      end
      if @mongo_data_exists
        run_cmd("tar --selinux --overwrite --listed-incremental=/dev/null -xzf mongo_data.tar.gz -C /")
      end
      if @pgsql_data_exists
        run_cmd("tar --selinux --overwrite --listed-incremental=/dev/null -xzf pgsql_data.tar.gz -C /")
      end
      if !@mongo_data_exists && !@pgsql_data_exists && !valid_logical_backup
        if @foreman_dump_exists && @candlepin_dump_exists
          restore_psql_dumps
        end
        if @mongo_dump_exists
          restore_mongo_dump
        end
      end
      migrate_pulp
      puts "Done.\n"
    end

    def restore
      FileUtils.chown(nil, 'postgres', @dir) unless @is_foreman_proxy_content
      Dir.chdir(@dir)

      set_file_security
      reset_katello

      puts "Stopping Katello services"
      run_cmd("katello-service stop")
      puts "Done.\n"

      restore_databases

      puts "Ensuring all Katello processes are started"
      run_cmd("katello-service start")
      run_cmd("systemctl daemon-reload") unless @is_foreman_proxy_content
      puts "Done.\n"
    end

    def display_backup_options
      puts "---- The given directory does not contain the required files or has too many files"
      puts "---- All backup directories contain: #{@standard_backup_files.join(", ")}"
      if @is_foreman_proxy_content
        puts "---- A #{@foreman_proxy_content.gsub(/-/, " ")} backup directory contains: #{@foreman_proxy_content_backup_files.join(", ")}"
        puts "---- A #{@foreman_proxy_content.gsub(/-/, " ")} backup directory contains: #{@foreman_proxy_content_online_backup_files.join(", ")}"
      else
        puts "---- An online backup directory contains: #{@online_backup_files.join(", ")}"
        puts "---- An offline backup directory contains: #{@offline_backup_files.join(", ")}"
      end
      puts "---- A logical backup directory contains: #{@online_backup_files.join(", ")}, #{@offline_backup_files.join(", ")}"
      puts "---- *pulp_data.tar is optional"
      puts "---- Please choose a valid backup directory"
      puts @optparse
      exit(-1)
    end

    def tarball_file_list(tarball)
      # accepts tar.gz files only
      file_list = []
      File.open(tarball, "rb") do |file|
        ::Zlib::GzipReader.wrap(file) do |gz|
          ::Gem::Package::TarReader.new(gz) do |tar|
            tar.each { |entry| file_list << entry.full_name }
          end
        end
      end
      file_list
    end

    def hostname_check
      # make sure that the system hostname is the same as the backup
      config_tarball = File.join(@dir, 'config_files.tar.gz')
      config_files = tarball_file_list(config_tarball)

      # Incremental backups sometimes don't include httpd.conf. Since a "base" backup is restored before an incremental, we can
      # assume that the hostname is checked during the base backup restore
      if config_files.include?("etc/httpd/conf/httpd.conf")
        backup_hostname = run_cmd("tar zxf #{config_tarball} etc/httpd/conf/httpd.conf --to-stdout | grep ServerName | awk {'print $2'} | tr -d '\"'").chomp
        hostname = Socket.gethostname.chomp
        backup_hostname == hostname
      else
        true
      end
    end

    def backup_valid?
      @mongo_data_exists = File.exist?(File.join(@dir, 'mongo_data.tar.gz'))
      @pgsql_data_exists = File.exist?(File.join(@dir, 'pgsql_data.tar.gz'))
      @pulp_data_exists = File.exist?(File.join(@dir, 'pulp_data.tar'))
      @foreman_dump_exists = File.exist?(File.join(@dir, 'foreman.dump'))
      @candlepin_dump_exists = File.exist?(File.join(@dir, 'candlepin.dump'))
      @mongo_dump_exists = Dir.exists?(File.join(@dir, 'mongo_dump'))
      @config_exists = File.exist?(File.join(@dir, 'config_files.tar.gz'))
      @pg_globals_exist = File.exist?(File.join(@dir, 'pg_globals.dump'))

      unless @config_exists
        puts "Cannot find the required config_files.tar.gz file in #{@dir}"
        exit(-1)
      end

      unless hostname_check
        puts "The hostname in the backup does not match the hostname of the system"
        exit(-1)
      end

      return true if valid_logical_backup

      if @is_foreman_proxy_content
        unless valid_fpc_standard_backup || valid_fpc_online_backup
          display_backup_options
        end
      else
        unless valid_standard_backup || valid_online_backup
          display_backup_options
        end
      end
      true
    end

    def confirm
      puts "WARNING: This script will drop and restore your database."
      puts "Your existing installation will be replaced with the backup database."
      puts "Once this operation is complete there is no going back.\n"
      print "Are you sure(Y/N)? "
      response = gets.chomp
      if /[Y]/i.match(response)
        puts "Starting restore from #{@dir}: #{Time.now}"
        restore
        puts "Done with restore: #{Time.now}"
      else
        puts "**** cancelled ****"
      end
    end

    def run
      parse_options
      if backup_valid?
        @confirmed ? restore : confirm
      else
        display_backup_options
      end
    end
  end
end
