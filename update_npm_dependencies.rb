#!/usr/bin/env ruby

require 'optparse'
require 'json'

STRATEGIES = ['single', 'bundle', '']

PROJECT_PACKAGE_PATHS = {
  'foreman' => ['foreman'],
  'plugins' => ['plugins', 'foreman'],
  'katello' => ['katello', 'plugins', 'foreman'],
}


def package_name(npm_module_name)
  "nodejs-#{npm_module_name}"
end

def package_dir(npm_module_name, project)
  "packages/#{project}/#{package_name(npm_module_name)}"
end

def find_package_project(npm_module_name)
  PROJECT_PACKAGE_PATHS[@options[:project]].find do |project|
    File.directory?(package_dir(npm_module_name, project))
  end
end

def package_exist?(npm_module_name)
  !!find_package_project(npm_module_name)
end

def current_version(npm_module_name)
  project = find_package_project(npm_module_name)
  if project
    spec_file = "#{package_dir(npm_module_name, project)}/#{package_name(npm_module_name)}.spec"
    version_line = File.readlines(spec_file).grep(/^\W*Version:.*/).first
    version_line.gsub(/^\W*Version:\W*/, '').strip
  end
end

def bundle_strategy(npm_module_name)
  project = find_package_project(npm_module_name)
  if project
    dir = package_dir(npm_module_name, project)
    zipped_dependencies = Dir["#{dir}/*.tgz"]
    if zipped_dependencies.length > 1
      'bundle'
    else
      'single'
    end
  else
    @options[:default_strategy]
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
  project = find_package_project(npm_module_name) || @options[:project]
  cmd = ''
  if @options[:git_packager]
    cmd += 'RPM_PACKAGER="$(git config user.name) <$(git config user.email)>" '
  end
  cmd += "./add_npm_package.sh #{npm_module_name} #{module_details['version']} '#{strategy}' #{project}"
  cmd
end

def action_description(action, npm_module_name, module_details)
  case action
  when :skip
    "skip   #{npm_module_name} (#{module_details['version']})"
  when :update
    "update #{npm_module_name} (#{current_version(npm_module_name)} -> #{module_details['version']})"
  when :add
    "add    #{npm_module_name} (#{module_details['version']})"
  end
end

def format_list(lines)
  "  " + lines.join("\n  ")
end


@options = {
  :project => 'foreman'
}
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

  available_projects = PROJECT_PACKAGE_PATHS.keys.map{|s| "'#{s}'" }.join(', ')
  opts.on('--project NAME', "Base directory were the specs will be created, must be one of #{available_projects}, default is: '#{@options[:project]}'") do |val|
    if !PROJECT_PACKAGE_PATHS.keys.include?(val)
      opts.abort("Invalid project, must be one of: #{available_projects}")
    end
    @options[:project] = val
  end

  available_strategies = STRATEGIES.map{|s| "'#{s}'" }.join(', ')
  opts.on('--default-strategy STRATEGY', "Default npm2rpm strategy for new packages, must be one of: #{available_strategies}") do |val|
    if !STRATEGIES.include?(val)
      opts.abort("Invalid default strategy, must be one of: #{available_strategies}")
    end
    @options[:default_strategy] = val
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

packages = {
  :succeeded => [],
  :failed => []
}
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
  desc = action_description(action, npm_module_name, details)

  case action
  when :skip
    puts "Skipping package #{npm_module_name}, already at version #{details['version']} ..."
  when :update
    puts "Updating package #{npm_module_name} to version #{details['version']} ..."
  when :add
    puts "Adding new package #{npm_module_name} in version #{details['version']} ..."
  end

  status = :succeeded
  if action != :skip
    if @options[:dryrun]
      puts add_package_cmd(npm_module_name, details)
    else
      result = system(add_package_cmd(npm_module_name, details))
      if !result
        action = :fail
        status = :failed
      end
    end
  end

  packages[status] << desc
  counts[action] += 1
end

puts
puts "Package changes:"
puts format_list(packages[:succeeded])
puts
if packages[:failed].length > 0
  puts "Following packages failed:"
  puts format_list(packages[:failed])
  puts
end

puts "Stats:"
puts "  #{counts[:add]} packages added"
puts "  #{counts[:update]} packages updated"
puts "  #{counts[:update]} packages skipped"
puts "  #{counts[:fail]} packages failed"
