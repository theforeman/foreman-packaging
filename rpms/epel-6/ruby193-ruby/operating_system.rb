module Gem
  class << self

    ##
    # Returns a string representing that part or the directory tree that is
    # common to all specified directories.

    def common_path(dirs)
      paths = dirs.collect {|dir| dir.split(File::SEPARATOR)}
      uncommon_idx = paths.transpose.each_with_index.find {|dirnames, idx| dirnames.uniq.length > 1}.last
      paths[0][0 ... uncommon_idx].join(File::SEPARATOR)
    end
    private :common_path

    ##
    # Default gems locations allowed on FHS system (/usr, /usr/share).
    # The locations are derived from directories specified during build
    # configuration.

    def default_locations
      @default_locations ||= {
        :system => common_path([ConfigMap[:vendorlibdir], ConfigMap[:vendorarchdir]]),
        :local => common_path([ConfigMap[:sitelibdir], ConfigMap[:sitearchdir]])
      }
    end

    ##
    # For each location provides set of directories for binaries (:bin_dir)
    # platform independent (:gem_dir) and dependent (:ext_dir) files.

    def default_dirs
      @default_dirs ||= Hash[default_locations.collect do |destination, path|
        [destination, {
          :bin_dir => File.join(path, ConfigMap[:bindir].split(File::SEPARATOR).last),
          :gem_dir => File.join(path, ConfigMap[:datadir].split(File::SEPARATOR).last, 'gems'),
          :ext_dir => File.join(path, ConfigMap[:libdir].split(File::SEPARATOR).last, 'gems')
        }]
      end]
    end

    ##
    # RubyGems default overrides.

    def default_dir
      if Process.uid == 0
        Gem.default_dirs[:local][:gem_dir]
      else
        Gem.user_dir
      end
    end

    def default_path
      path = default_dirs.collect {|location, paths| paths[:gem_dir]}
      path.unshift Gem.user_dir if File.exist? Gem.user_home
    end

    def default_bindir
      if Process.uid == 0
        Gem.default_dirs[:local][:bin_dir]
      else
        File.join [Dir.home, 'bin']
      end
    end

    def default_ext_dir_for base_dir
      dirs = Gem.default_dirs.detect {|location, paths| paths[:gem_dir] == base_dir}
      dirs && File.join(dirs.last[:ext_dir], 'exts')
    end
  end
end
