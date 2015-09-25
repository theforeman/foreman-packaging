#!/usr/bin/env ruby

require 'optparse'

options = {:message => []}

OptionParser.new do |opts|
  opts.banner = "Usage: update_package.rb -n [NAME] -v [VERSION] [options]"

  opts.on("-m", "--message [MESSAGE]", String, "Changelog message(s)") do |m|
    options[:message] << m
  end

  opts.on("-n", "--name [NAME]", String, "Package or gem name, or a part thereof") do |n|
    options[:name] = n
  end

  opts.on("-v", "--version [VERSION]", String, "Package version number") do |v|
    options[:version] = v
  end
end.parse!

raise "missing --name" if options[:name].nil?
raise "missing --version" if options[:version].nil?

# Try and find operating directories, prefer an exact match
def find_directories(name)
  dirs = if File.exist?("plugins/#{name}")
           Dir["plugins/#{name}"]
         else
           Dir["plugins/*#{name}*"]
         end

  if dirs.size > 1
    raise "Ambiguous name given, multiple packages match: #{dirs.inspect}"
  elsif dirs.empty?
    # dependencies will have multiple directories, one per OS
    dirs = Dir["dependencies/*/#{name}"]
    if dirs.empty?
      dirs = Dir["dependencies/*/*#{name}*"]
      if dirs.empty?
        raise "Cannot find a package with the name #{name}"
      end
    end
  end

  dirs
end

# updates a bundler.d/Gemfile entry
def update_bundlerd(pwd, opts)
  Dir[File.join(pwd, '**', '*.rb')].each do |rb|
    updated = false
    original = File.read(rb)
    File.open(rb, 'w') do |f|
      original.each_line do |line|
        if line =~ /^gem\s+/ && !updated
          line.gsub! /(["'])[\d\.]+["']\s*$/, "\\1#{opts[:version]}\\1"
          updated = true
        end
        f.puts(line)
      end
    end
    break if updated
  end
end

# updates a gem.list file
def update_gemlist(pwd, opts)
  Dir[File.join(pwd, '**', 'gem.list')].each do |rb|
    updated = false
    original = File.read(rb)
    File.open(rb, 'w') do |f|
      original.each_line do |line|
        if line =~ /^GEMS=/ && !updated
          line.gsub! /-[\d\.]+\.gem/, "-#{opts[:version]}.gem"
          updated = true
        end
        f.puts(line)
      end
    end
  end
end

def update_changelog(pwd, opts)
  changelog = File.expand_path('../changelog.rb', __FILE__)
  args = ['-v', opts[:version]]
  opts[:message].each { |m| args += ['-m', m] }
  args += Dir[File.join(pwd, '**', 'changelog')].to_a
  system(changelog, *args)
end

find_directories(options[:name]).each do |pwd|
  update_bundlerd(pwd, options)
  update_gemlist(pwd, options)
  update_changelog(pwd, options)
end
