#!/usr/bin/env ruby

require 'optparse'
require 'time'

options = {:message => []}

author_name = ENV['GIT_AUTHOR_NAME'] || `git config --get user.name`.chomp
author_email = ENV['DEBEMAIL'] || ENV['EMAIL'] || ENV['GIT_AUTHOR_EMAIL'] || `git config --get user.email`.chomp
options[:author] = "#{author_name} <#{author_email}>" if !author_name.nil? && !author_email.nil?

VERSION_REGEX = %r{\((?<version>.*)-(?<release>.*)\)}

OptionParser.new do |opts|
  opts.banner = "Usage: changelog.rb -v [VERSION] [options] paths ..."

  opts.on("-a", "--author [AUTHOR]", String, "Author name and e-mail address") do |a|
    options[:author] = a
  end

  opts.on("-m", "--message [MESSAGE]", String, "Changelog message(s)") do |m|
    options[:message] << m
  end

  opts.on("-v", "--version [VERSION]", String, "Package version number") do |v|
    options[:version] = v
  end
end.parse!

raise "missing author" if options[:author].nil?
raise "missing changelog file(s)" if ARGV.empty?
ARGV.each { |f| raise "cannot find file #{f}" unless File.readable? f }

options[:message] << "#{options[:version]} released" if options[:message].empty?

ARGV.each do |path|
  control = File.read(File.join(File.dirname(path), 'control'))
  project = $1 if control =~ /Source:\s*(.+)/

  version = options.fetch(:version, nil)

  unless version
    match = File.read(path).split("\n")[0].match(VERSION_REGEX)
    current_version = match[:version]
    current_release = match[:release]

    version = "#{current_version}-#{current_release.to_i + 1}"
  end

  logs = File.read(path)
  entry = "#{project} (#{version}) stable; urgency=low\n\n"
  options[:message].each { |m| entry += "  * #{m}\n" }
  entry += "\n -- #{options[:author]}  #{Time.now.rfc2822}\n\n"
  File.open(path, 'w') { |f| f.write(entry + logs) }
end
