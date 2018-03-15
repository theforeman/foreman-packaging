#!/usr/bin/env ruby
#
# Compares tito.props with koji and prints out differences in Github markup for
# review and cleanup.
#

require 'configparser'

cfg = ConfigParser.new(File.join(__dir__, 'tito.props'))
cfg.each do |tag, entry|
  next unless entry.has_key?('whitelist')
  comp_pkgs = entry['whitelist'].split
  if entry['scl']
    comp_pkgs.map!{ |x| x =~ /^rubygem-/ ? "#{entry['scl']}-#{x}" : x }
  end
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
    puts "koji add-pkg --owner=kojiadm #{tag} #{missing_pkgs.sort.join(" ")}"
    puts "```"
  end

  if extra_pkgs.any?
    puts "\n# Packages not expected in #{tag}"
    extra_pkgs.sort.each { |x| puts " * [x] #{x}" }
    puts "```shell"
    puts "koji remove-pkg #{tag} #{extra_pkgs.sort.join(" ")}"
    puts "```"
  end
end
