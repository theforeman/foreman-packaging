#!/usr/bin/env ruby

require 'optparse'
require 'json'

def package_name(npm_module_name)
  "nodejs-#{npm_module_name}"
end

def package_dir(npm_module_name)
  "packages/foreman/#{package_name(npm_module_name)}"
end

def package_exist?(npm_module_name)
  File.directory?(package_dir(npm_module_name))
end

def current_version(npm_module_name)
  if package_exist?(npm_module_name)
    spec_file = "#{package_dir(npm_module_name)}/#{package_name(npm_module_name)}.spec"
    version_line = File.readlines(spec_file).grep(/^\W*Version:.*/).first
    version_line.gsub(/^\W*Version:\W*/, '').strip
  end
end

def bundle_strategy(npm_module_name)
  if !package_exist?(npm_module_name)
    @options[:defauilt_strategy]
  else
    dir = package_dir(npm_module_name)
    zipped_dependencies = Dir["#{dir}/*.tgz"]
    if zipped_dependencies.length > 1
      'bundle'
    else
      'single'
    end
  end
end

def detect_action(npm_module_name, details)
  if package_exist?(npm_module_name)
    if details['version'] == current_version(npm_module_name)
      :skip
    else
      :update
    end
  else
    :add
  end
end

def add_package_cmd(npm_module_name, module_details)
  strategy = bundle_strategy(npm_module_name)
  cmd = ''
  if @options[:git_packager]
    cmd += 'RPM_PACKAGER="$(git config user.name) <$(git config user.email)>" '
  end
  cmd += "./add_npm_package.sh #{npm_module_name} #{module_details['version']} #{strategy}"
  cmd
end

STRATEGIES = ['single', 'bundle', '']

@options = {}
opts = OptionParser.new do |opts|
  opts.banner = [
    "Usage: #{__FILE__} [options]",
    "",
    "Updates npm packages based on json output of npm list.",
    "Make sure you generate the input json file without development and optional dependencies:",
    "    npm list --production --no-optional --json",
    "",
    ""
  ].join("\n")

  opts.separator('Options:')
  opts.on('--package-list FILE', 'Path to a json file with output of npm list (required)') do |val|
    if !File.exist?(val)
      puts "File #{val} doesn't exist."
      exit 1
    end
    @options[:package_list_file] = val
  end

  opts.on('--only NPM_MODULES', 'Comma separated list of npm modules to update, others are skipped') do |val|
    @options[:only] = val.split(',')
  end

  opts.on('--except NPM_MODULES', 'Comma separated list of npm modules to be excluded from updating') do |val|
    @options[:except] = val.split(',')
  end

  available_strategies = STRATEGIES.map{|s| "'#{s}'" }.join(', ')
  opts.on('--default-strategy STRATEGY', "Default npm2rpm strategy for new packages, must be one of: #{available_strategies}") do |val|
    if !STRATEGIES.include?(val)
      opts.abort("Invalid default strategy, must be one of: #{available_strategies}")
    end
    @options[:defauilt_strategy] = val
  end

  opts.on('--dryrun', 'Only print what packages need to be added or updated') do |val|
    @options[:dryrun] = true
  end

  opts.on('--git-packager', 'Use packager info from git') do |val|
    @options[:git_packager] = true
  end

  opts.on('-h', '--help', 'Print help') do
    puts opts
    exit
  end

  opts.parse!
end
opts.abort("Received unsupported arguments: #{ARGV}") if ARGV.length > 0
opts.abort("Option --package-list is required") unless @options[:package_list_file]

failed_packages = []
counts = {
  :add => 0,
  :update => 0,
  :skip => 0,
  :fail => 0,
}

npm_list = JSON.parse(File.read(@options[:package_list_file]))
npm_list['dependencies'].each do |npm_module_name, details|
  next if @options[:only] && !@options[:only].include?(npm_module_name)
  next if @options[:except] && @options[:except].include?(npm_module_name)

  puts
  action = detect_action(npm_module_name, details)

  case action
  when :skip
    puts "Skipping package #{npm_module_name}, already at version #{details['version']} ..."
  when :update
    puts "Updating package #{npm_module_name} to version #{details['version']} ..."
  when :add
    puts "Adding new package #{npm_module_name} in version #{details['version']} ..."
  end

  if @options[:dryrun]
    puts add_package_cmd(npm_module_name, details)
  elsif action != :skip
    result = system(add_package_cmd(npm_module_name, details))
    if !result
      failed_packages << npm_module_name
      action = :fail
    end
  end

  counts[action] += 1
end

puts
if failed_packages.length > 0
  puts "Following packages failed:"
  puts "  " + failed_packages.join("\n  ")
  puts
end

puts "#{counts[:add]} packages added"
puts "#{counts[:update]} packages updated"
puts "#{counts[:update]} packages skipped"
puts "#{counts[:fail]} packages failed"
