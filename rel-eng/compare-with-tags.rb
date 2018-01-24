#!/usr/bin/env ruby
#
# Compares tito.props with koji and prints out differences in Github markup for
# review and cleanup.
#

require 'configparser'

cfg = ConfigParser.new('tito.props')
cfg.each do |entry|
  tag = entry.first
  scl = entry.last['scl']
  next unless tag =~ /^foreman/
  comp_pkgs = entry.last['whitelist'].split
  comp_pkgs.map!{ |x| (scl && x =~ /^rubygem-/) ? "#{scl}-#{x}" : x }
  koji_pkgs = []
  `koji list-pkgs --tag=#{tag} --quiet`.each_line do |line|
    koji_pkgs << line.split.first
  end
  missing_pkgs = comp_pkgs - koji_pkgs
  extra_pkgs = koji_pkgs - comp_pkgs

  if missing_pkgs.any?
    puts "\n# Packages missing in tag #{tag}"
    missing_pkgs.sort.each { |x| puts " * [x] #{x}" }
    puts "```shell"
    missing_pkgs.sort.each { |x| puts "koji add-pkg --owner=kojiadm #{tag} #{x}" }
    puts "```"
  end

  if extra_pkgs.any?
    puts "\n# Packages not expected in #{tag}"
    extra_pkgs.sort.each { |x| puts " * [x] #{x}" }
    puts "```shell"
    extra_pkgs.sort.each { |x| puts "koji remove-pkg #{tag} #{x}" }
    puts "```"
  end
end
