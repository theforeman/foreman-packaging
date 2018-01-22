#!/usr/bin/env ruby

require 'optparse'

options = {}

OptionParser.new do |opts|
  opts.banner = "Usage: merge_tag_release.rb [options]"

  opts.on("-c", "--commit [COMMIT]", "SHA hash of the commit to be cherry-picked") do |commit|
    options[:commit] = commit
  end

  opts.on("-b", "--branches [BRANCHES]", "Branches to merge commit to, separated by commas. e.g: '1.16-stable, 1.15-stable' ") do |branches|
    options[:branches] = branches
  end

  opts.on("-p", "--project [PROJECT]", "Name of the project e.g: rubygem-foreman_discovery") do |project|
    options[:project] = project
  end
end.parse!

raise OptionParser::MissingArgument, "--branches" if options[:branches].nil?
raise OptionParser::MissingArgument, "--project" if options[:project].nil?
raise OptionParser::MissingArgument, "--commit" if options[:commit].nil?
CORE_PROJECTS = %q(foreman foreman-selinux foreman-proxy foreman-installer)

branches = options[:branches].split(',').map!(&:strip)

branches.each do |branch|
  `git checkout rpm/#{branch}`
  `git cherry-pick #{options[:commit]}`
  # Cherry-pick commit to branch
  Dir.chdir(options[:project])
  system('tito tag --keep-version --accept-auto-changelog')
  `git push origin rpm/#{branch}`
  `git push origin rpm/#{branch} --tags`
  `git push upstream rpm/#{branch}`
  `git push upstream rpm/#{branch} --tags`
  # Release on the releasers for the branch you're in. e.g: koji-foreman-1.15
  # Plugins are automatically detected.
  branch = 'nightly' if branch == 'develop'
  releaser = if CORE_PROJECTS.include? options[:project]
               "koji-foreman-#{branch}"
             else
               "koji-foreman-plugins-#{branch}"
             end
  `ruby release_package.rb -p #{options[:project]} -r #{releaser}`
  Dir.chdir('../')
  exit
end
