#!/usr/bin/env ruby
require 'nokogiri'

def print_usage
  usage = <<-USAGE
add_to_comps - adds packagereqs for a package to a comps xml file

Usage ./add_to_comps.rb comps-file package-name

Examples:
  ./add_to_comps.rb comps/comps-foreman-el8.xml nodejs-example

Return codes:

  0 - successfully added
  1 - package is already present
  2 - wrong arguments
USAGE
  puts usage
end

def find_packagereq(comps, package_name)
  comps.xpath('//packagelist/packagereq').select { |s| s.text == package_name }
end

# Gets subset of packagereqs that are not -docs nor comments
def get_packagereqs(packagelist)
  relevant = []
  packagelist.children.each do |packagereq|
    # Break as soon as you find a comment which means start
    # of -doc packages
    break if packagereq.class == Nokogiri::XML::Comment
    relevant << packagereq
    packagereq.unlink
  end
  relevant
end

def prepend_packagereqs(packagelist, packagereqs)
  packagereqs.each do |packagereq|
    if packagelist.children.empty?
      packagelist.add_child(packagereq)
    else
      packagelist.children.before(packagereq)
    end
  end
end

if ARGV.length != 2
  print_usage
  exit(2)
end

comps = Nokogiri::XML(File.open(ARGV[0])) { |config| config.noblanks }
exit(1) unless find_packagereq(comps, ARGV[1]) == []
packagelist = comps.xpath("//packagelist").first
new_packagereq = Nokogiri::XML(
  "<packagereq type='default'>#{ARGV[1]}</packagereq>"
).children.first
packagereqs = get_packagereqs(packagelist)
packagereqs << new_packagereq
packagereqs.sort! { |x,y| y.text <=> x.text }
prepend_packagereqs(packagelist, packagereqs)

File.write(ARGV[0], comps.to_xml)
exit 0
