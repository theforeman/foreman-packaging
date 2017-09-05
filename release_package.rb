#!/usr/bin/env ruby

require 'optparse'

options = {
  :jenkins_job_id => 'lastSuccessfulBuild'
}

OptionParser.new do |opts|
  opts.banner = "Usage: release_package.rb [options]"

  opts.on("-p", "--project [PROJECT]", "Project to build an RPM for") do |project|
    options[:project] = project
  end

  opts.on("-r", "--releaser REQUIRED", "Tito releaser to release for") do |releaser|
    options[:releaser] = releaser
  end

  opts.on("--jenkins-job [JENKINS_JOB]", "Name of Jenkins job to pull source file from") do |job|
    options[:jenkins_job] = job
  end

  opts.on("--jenkins-job-id [JENKINS_JOB_ID]", "ID of Jenkins job to pull source from (default: lastSuccessfulBuild") do |id|
    options[:jenkins_job_id] = id unless id.nil?
  end

  opts.on("--source_dir [SOURCE DIR]", "Directory which contains the source of the package being built (you can create it with gem unpack)") do |source_dir|
    options[:source_dir] = source_dir unless source_dir.nil?
  end
end.parse!

raise OptionParser::MissingArgument, "--project" if options[:project].nil?
raise OptionParser::MissingArgument, "--releaser" if options[:releaser].nil?

def log(msg)
  puts
  puts "== #{msg} =="
end

log("Initializing git annex")
puts `git-annex init`

log("Setting up source")
if options[:project] == 'rubygem-katello' || options[:project] == 'katello-installer'
  `./setup_sources.sh #{options[:project]} --relaxed`
else
  `./setup_sources.sh #{options[:project]}`
end

Dir.mkdir("rel-eng/build") if !File.exist?('rel-eng/build')

args = ["-o #{Dir.pwd}/rel-eng/build/"]

if (jenkins_job = options[:jenkins_job])
  args.push("--arg jenkins_job=#{jenkins_job}")

  if (jenkins_job_id = options[:jenkins_job_id])
    args.push("--arg jenkins_job_id=#{jenkins_job_id}")
  end
elsif (source_dir = options[:source_dir])
  args.push("--arg source_dir=#{source_dir}")
else
  puts options[:project]
  `git-annex get #{options[:project]}/*.gem`
  `gem unpack #{options[:project]}/*.gem --target .`
  # Assumes there is only going to be one gem in each project.
  # The output of 'gem unpack' is put in a directory with the same name as
  # the gem.
  source = Dir.glob(File.join(options[:project], "*.gem")).first.split('.gem')[0]
  source = File.basename(source)
  `mv #{source} source`
  `gem spec #{options[:project]}/*.gem --ruby > #{options[:project]}/source/#{source}.gemspec`
  args.push("--arg source_dir=./source")
end

output = ''
Dir.chdir(options[:project]) do
  log("Running tito release for #{options[:project]} using #{options[:releaser]}")
  puts "tito release #{args.join(' ')} #{options[:releaser]}"
  output = `tito release #{args.join(' ')} #{options[:releaser]}`
  puts output
end

if output.include?('ERROR')
  puts output
  exit 1
end

if output.include?('Traceback')
  puts output
  exit 1
end

release_tasks = output.
                  split("\n").
                  select { |line| line.start_with?("Task info:") }.
                  collect { |line| line.scan(/\d+/) }.
                  flatten
release_count = release_tasks.length

if !release_tasks.empty?
  release_tasks = release_tasks.join(' ')
  log("Watching koji tasks #{release_tasks}")
  response = `koji -c ~/.koji/config watch-task #{release_tasks}`
end

if $? == 0
  puts response
  exit 0
else
  build_exists_count = response.count("Build already exists") if response

  if build_exists_count == release_count
    exit 0
  else
    puts response
    exit 1
  end
end
