require 'optparse'
require 'fileutils'
require 'date'
require 'yaml'
require 'find'
require 'json'
require 'highline/import'
require_relative "helper.rb"

module KatelloUtilities
  class Backup
    include ::KatelloUtilities::Helper

    def initialize(foreman_proxy_content, foreman_proxy, program, accepted_scenarios=nil)
      @excluded="--exclude goferd,foreman-proxy,squid,smart_proxy_dynflow_core,qdrouterd,qpidd"
      @databases = ['pulp', 'pgsql', 'mongodb']

      @options = {}
      @dir = nil
      @databases = @databases.dup
      @accepted_scenarios = accepted_scenarios
      @last_scenario = self.last_scenario
      @services_online = true

      # keep as variables for easy backporting
      @foreman_proxy_content = foreman_proxy_content
      @foreman_proxy = foreman_proxy
      @program = program

      setup_opt_parser
    end

    # do not use run_cmd() inside this method, to avoid a recursive loop
    # as run_cmd() calls cleanup, and they will infinitely trigger one another
    # rather, use system() call provided by ruby
    def cleanup(exitstatus=-1)
      puts "Cleaning up backup folder and starting any stopped services... "
      FileUtils.cd("/")
      FileUtils.rm_rf @dir unless @options[:no_subdir]
      if @options[:snapshot]
        @databases.each do |database|
          mount_location = File.join(@mountdir, database)
          system("umount #{mount_location}") if File.readlines('/proc/mounts').grep(/#{database}--snap/).any?
          snapshot_location = get_snapshot_location(database)
          system("lvremove #{snapshot_location} -f") unless snapshot_location.empty?
        end
      end
      `katello-service start #{@excluded}` unless @services_online
      puts "Done."
      exit(exitstatus)
    end

    def start_services
      run_cmd("katello-service start #{@excluded}") unless @services_online
      @services_online = true
    end

    def stop_services
      run_cmd("katello-service stop #{@excluded}") if @services_online
      @services_online = false
    end

    def specified_features
      @options[:features] || []
    end

    def feature_included?(feature)
      specified_features.include?(feature) || specified_features.include?("all")
    end

    def configure_configs
      base_configs = [
        "/etc/foreman-proxy",
        "/etc/httpd",
        "/etc/foreman-installer",
        "/etc/pki/katello",
        "/etc/pki/katello-certs-tools",
        "/etc/pki/pulp",
        "/etc/pulp",
        "/etc/puppet",
        "/etc/qpid",
        "/etc/qpid-dispatch",
        "/root/ssl-build",
        "/var/www/html/pub",
        "/etc/squid",
        "/etc/puppetlabs",
        '/opt/puppetlabs/puppet/cache/foreman_cache_data',
        '/opt/puppetlabs/puppet/ssl/',
        '/var/lib/puppet/foreman_cache_data',
        '/var/lib/puppet/ssl',
        '/usr/share/foreman-proxy/.ssh/'
      ]

      scenario_answers = load_scenario_answers(@last_scenario)

      katello_configs = [
        "/etc/candlepin",
        "/etc/foreman",
        "/etc/hammer",
        "/etc/sysconfig/tomcat*",
        "/etc/tomcat*",
        "/var/lib/candlepin",
        scenario_answers["certs"]["server_cert"],
        scenario_answers["certs"]["server_key"],
        scenario_answers["certs"]["server_cert_req"],
        scenario_answers["certs"]["server_ca_cert"]
      ]

      if @is_foreman_proxy_content
        fpc_certs_tar = run_cmd("cat /etc/foreman-installer/scenarios.d/#{@foreman_proxy_content}-answers.yaml | grep certs_tar | awk '{print $2}'").chomp
        unless File.exist?(fpc_certs_tar)
          puts "#{@foreman_proxy} certs tar file is not present on the system in path #{fpc_certs_tar} please move the file back to that location or generate a new one on the main server."
          cleanup
        end
        backup_configs = base_configs.push(fpc_certs_tar)
      else
        backup_configs = base_configs + katello_configs
      end

      feature_configs = []
      feature_configs.push("/var/lib/tftpboot") if feature_included?("tftp")
      feature_configs += ["/var/named/", "/etc/named*"] if feature_included?("dns")
      feature_configs += ["/var/lib/dhcpd", "/etc/dhcp"] if feature_included?("dhcp")
      feature_configs.push("/usr/share/xml/scap") if feature_included?("openscap")

      backup_configs + feature_configs
    end

    def confirm
      unless agree("WARNING: This script will stop your services. Do you want to proceed(y/n)? ")
        puts "**** cancelled ****"
        FileUtils.rm_rf @dir
        exit(-1)
      end
    end

    def warning
      unless agree("*** WARNING: The online backup flag is intended for making a copy of the data\n" \
                   "*** for debugging purposes only. The backup routine can not ensure 100% consistency while the\n" \
                   "*** backup is taking place as there is a chance there may be data mismatch between\n" \
                   "*** Mongo and Postgres databases while the services are live. If you wish to utilize the --online-backup\n" \
                   "*** flag for production use you need to ensure that there are no modifications occurring during\n" \
                   "*** your backup run.\n\nDo you want to proceed(y/n)? ")
        puts "**** cancelled ****"
        FileUtils.rm_rf @dir
        exit(-1)
      end
    end

    def create_directories(directory)
      @dir = File.join directory, "#{@program}-backup-" + self.timestamp unless @options[:no_subdir]
      puts "Creating backup folder #{@dir}"
      FileUtils.mkdir_p @dir
      FileUtils.chown_R nil, 'postgres', @dir if @databases.include? "pgsql"
      FileUtils.chmod_R 0770, @dir
    end

    def snapshot_backup
      @mountdir = @options[:snapshot_mount] || "/var/snap"
      @snapsize = @options[:snapshot_size] || "2G"
      FileUtils.mkdir_p @mountdir
      confirm unless @options[:confirm]
      validate_logical_volume unless @options[:confirm]
      stop_services
      create_and_mount_snapshots
      start_services
      backup_and_destroy_snapshots
    end

    def validate_logical_volume
      backup_lv = get_lv_info(@dir)
      shared_lv = @databases.select {|database| get_lv_info(database) == backup_lv}
      if shared_lv.any?
        unless agree("*** WARNING: The chosen backup location is mounted on the same logical volume as the #{shared_lv.join(', ')} location\n" \
                     "*** It is highly suggested to backup to a different logical volume than the #{shared_lv.join(', ')} database.\n" \
                     "*** If you would like to continue, the snapshot size will be required to be at least the size of the actual #{shared_lv.join(', ')} database.\n" \
                     "*** You can skip this confirmation with the '-y' flag. Do you want to proceed(y/n)? ")
          puts "**** cancelled ****"
          cleanup
	end
      end
    end

    def create_and_mount_snapshots
      @databases.each do |database|
        puts "Creating #{database} snapshot"
        lv_info = get_lv_info(database)
        run_cmd("lvcreate -n#{database}-snap -L#{@snapsize} -s #{lv_info[0]}")
        mount_location = File.join(@mountdir, database)
        FileUtils.mkdir_p mount_location
        puts "Mounting #{database} snapshot on #{mount_location}"
        options = lv_info[1] == 'xfs' ? "-onouuid,ro" : "-oro"
        run_cmd("mount #{get_snapshot_location(database)} #{mount_location} #{options}")
      end
    end

    def get_snapshot_location(database)
      run_cmd("lvs --noheadings -o lv_path -S lv_name=#{database}-snap").strip
    end

    def get_lv_info(database)
      target = database
      target = File.join(database, 'data') if target == 'pgsql'
      target = File.join('/var/lib', target) if @databases.include? database
      run_cmd("findmnt -n --target #{target} -o SOURCE,FSTYPE").split
    end

    def get_base_directory(database)
      target = ""
      case database
      when 'pulp'
        target = '0005_puppet_module_name_change.txt'
      when 'pgsql'
        target = 'postgresql.conf'
      when 'mongodb'
        target = 'mongod.lock'
      end

      result = nil
      Find.find(File.join(@mountdir, database)) do |path|
        result = File.dirname(path) if File.basename(path) == target
      end
      result
    end

    def backup_and_destroy_snapshots
      @databases.each do |database|
        basedir = get_base_directory(database)
        puts "Backing up #{database} from #{basedir}"
        offline_backup(database, basedir)

        puts "Unmounting #{database} snapshot"
        run_cmd("umount #{File.join(@mountdir, database)}")

        snapshot_location = get_snapshot_location(database)
        puts "Removing snapshot #{snapshot_location}"
        run_cmd("lvremove #{snapshot_location} -f")
      end
    end

    def online_backup(database)
      case database
      when 'pulp'
        FileUtils.cd '/var/lib/pulp' do
          puts "Backing up Pulp data... "
          matching = false
          until matching
            checksum1 = run_cmd("find . -printf '%T@\n' | md5sum")
            create_pulp_data_tar
            checksum2 = run_cmd("find . -printf '%T@\n' | md5sum")
            matching = (checksum1 == checksum2)
          end
        end
        puts "Done."
      when 'pgsql'
        puts "Backing up postgres online schema... "
        run_cmd("runuser - postgres -c 'pg_dumpall -g > #{File.join(@dir, 'pg_globals.dump')}'")
        run_cmd("runuser - postgres -c 'pg_dump -Fc foreman > #{File.join(@dir, 'foreman.dump')}'")
        run_cmd("runuser - postgres -c 'pg_dump -Fc candlepin > #{File.join(@dir, 'candlepin.dump')}'")
        puts "Done."
      when 'mongodb'
        puts "Backing up mongo online schema... "
        run_cmd("mongodump --host localhost --out #{File.join(@dir, 'mongo_dump')}")
        puts "Done."
      end
    end

    def offline_backup(database, dir_path = nil)
      case database
      when 'pulp'
        dir_path ||= '/var/lib/pulp'
        FileUtils.cd dir_path do
          puts "Backing up Pulp data... "
          create_pulp_data_tar
          puts "Done."
        end
      when 'mongodb'
        dir_path ||= '/var/lib/mongodb'
        FileUtils.cd dir_path do
          puts "Backing up mongo db... "
          run_cmd("tar --selinux --create --file=#{File.join(@dir, 'mongo_data.tar')} --listed-incremental=#{File.join(@dir, '.mongo.snar')} --exclude=mongod.lock --transform 's,^,var/lib/mongodb/,S' -S *")
          puts "Done."
        end
      when 'pgsql'
        dir_path ||= '/var/lib/pgsql/data'
        FileUtils.cd dir_path do
          puts "Backing up postgres db..."
          run_cmd("tar --selinux --create --file=#{File.join(@dir, 'pgsql_data.tar')} --listed-incremental=#{File.join(@dir, '.postgres.snar')} --transform 's,^,var/lib/pgsql/data/,S' -S *")
          puts "Done."
        end
      end
    end

    def compress_files
      psql = spawn('gzip', 'pgsql_data.tar', '-f') if @databases.include? "pgsql"
      mongo = spawn('gzip', 'mongo_data.tar', '-f')
      Process.wait(psql) if @databases.include? "pgsql"
      Process.wait(mongo)
    end

    def plugin_list
      if @is_foreman_proxy_content
        JSON.parse(run_cmd("curl -k https://$(hostname):9090/features"))
      else
        plugins = []
        plugin_list = run_cmd("foreman-rake plugin:list | grep 'Foreman plugin: '", [0,1]).lines
        plugin_list.each do |line|
          plugin = line.split
          plugins << "#{plugin[2].chop}-#{plugin[3].chop}"
        end
        plugins
      end
    end

    def generate_metadata
      puts "Generating metadata ... "
      os_version = run_cmd("cat /etc/redhat-release").chomp
      plugins = plugin_list
      rpms = run_cmd("rpm -qa").split("\n")
      system_facts = {os_version: os_version, plugin_list: plugins, rpms: rpms}
      File.open('metadata.yml', 'w') do |metadata_file|
        metadata_file.puts system_facts.to_yaml
      end
      puts "Done."
    end

    def create_pulp_data_tar
      run_cmd("tar --selinux --create --file=#{File.join(@dir, 'pulp_data.tar')} --exclude=var/lib/pulp/katello-export --listed-incremental=#{File.join(@dir, '.pulp.snar')} --transform 's,^,var/lib/pulp/,S' -S *")
    end

    def backup_config_files
      puts "Backing up config files... "
      flags = "--exclude=\"/var/www/html/pub/isos*\" --exclude=\"/var/www/html/pub/exports*\" --selinux --create --gzip"
      flags += " --file=#{File.join(@dir, 'config_files.tar.gz')} --listed-incremental=#{File.join(@dir, '.config.snar')}"
      tar_command = "tar #{flags} #{configure_configs.join(' ')} 2>/dev/null"
      run_cmd(tar_command, [0,2])
      puts "Done."
    end

    def validate_directory
      return true unless @databases.include? "pgsql"
      unless system("sudo -u postgres test -w #{@dir}")
        puts "****cancelled****"
        puts "Postgres user needs write access to the backup directory"
        puts "Please select a directory, such as /tmp or /var/tmp which allows Postgres write access"
        FileUtils.rm_rf @dir unless @options[:no_subdir]
      end
    end

    def setup_opt_parser
      @optparse = OptionParser.new do |opts|
        opts.banner = "Usage: #{@program}-backup /path/to/dir [options]\n eg: $ #{@program}-backup /tmp/#{@program}-backup"

        opts.on("--skip-pulp-content", "Create backup without Pulp content for debugging only") do |config_only|
          @options[:config_only] = config_only
          @databases.delete 'pulp'
        end

        opts.on("--incremental PREVIOUS_BACKUP_DIR", String, "Backup changes since previous backup") do |dir_path|
          opts.abort("Please specify the previous backup directory.") unless dir_path
          if File.directory?(dir_path)
            @options[:incremental] = dir_path
          else
            opts.abort("Previous backup directory does not exist: #{dir_path}")
          end
        end

        opts.on("--online-backup", "Keep services online during backup") do |online|
          @options[:online] = online
        end

        opts.on("--logical-db-backup", "Also dump full database schema during offline backup") do |logical|
          @options[:logical_backup] = logical
        end

        opts.on("--snapshot", "Use snapshots of the databases to create backup") do |snapshot|
          @options[:snapshot] = snapshot
        end

        opts.on("--snapshot-mount-dir SNAPSHOT_MOUNT_LOCATION", String, "Override default directory (/var/snap/) where the snapshots will be mounted") do |mount_dir|
          @options[:snapshot_mount] = mount_dir
        end

        opts.on("--snapshot-size SNAPSHOT_BLOCK_DEVICE_SIZE", String, "Override default block size (2G)") do |size|
          @options[:snapshot_size] = size
        end

        opts.on("--features FEATURES", Array, "#{@foreman_proxy.capitalize} features to include in the backup, please specify a list with commas. " \
                "Valid features are tftp, dns, dhcp, openscap, and all.") do |features|
          @options[:features] = features.map { |f| f.to_s.downcase }
        end

        opts.on("--preserve-directory", "Do not create a time-stamped subdirectory") do |no_subdir|
          @options[:no_subdir] = no_subdir
        end

        opts.on("-y", "--assumeyes", "Bypass interaction by answering yes") do |confirm|
          @options[:confirm] = confirm
        end
      end
      @optparse
    end

    def parse_options
      begin @optparse.parse! ARGV
        if ARGV.length == 0
          @optparse.abort("**** ERROR: Please specify an export directory ****")
        elsif ARGV.length != 1
          puts @optparse
          exit(-1)
        end

        @dir = File.expand_path(ARGV[0].dup)
      rescue OptionParser::ParseError => e
        puts e
        puts @optparse
        exit -1
      end
    end

    def run
      parse_options

      if @dir.nil?
        puts "**** ERROR: Please specify an export directory ****"
        puts @optparse
        exit(-1)
      end

      puts "Starting backup: #{Time.now}"
      @is_foreman_proxy_content = !foreman_rpm_installed?
      @databases.delete 'pgsql' if @is_foreman_proxy_content
      create_directories(@dir.dup)
      validate_directory

      Dir.chdir(@dir) do
        generate_metadata
        if @options[:incremental]
          FileUtils.cp Dir.glob(File.join(@options[:incremental], '.*.snar')), @dir
        elsif @options[:no_subdir]
          FileUtils.rm Dir.glob(File.join(@dir, '.*.snar'))
        end
        backup_config_files

        if @options[:logical_backup]
          @databases.each do |database|
            online_backup(database)
          end
        end

        if @options[:snapshot]
          snapshot_backup
          compress_files
        elsif @options[:online]
          warning unless @options[:confirm]
          @databases.each do |database|
            online_backup(database)
          end
        else
          confirm unless @options[:confirm]
          stop_services
          @databases.each do |database|
            offline_backup(database)
          end
          start_services
          compress_files
        end
      end

      puts "Done with backup: #{Time.now}"
      puts "**** BACKUP Complete, contents can be found in: #{@dir} ****"
    end
  end
end
