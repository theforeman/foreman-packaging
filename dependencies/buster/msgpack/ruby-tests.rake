require 'gem2deb/rake/spectask'

Gem2Deb::Rake::RSpecTask.new do |spec|
  spec.pattern = './spec/*_spec,./spec/cruby/*_spec.rb'
end
