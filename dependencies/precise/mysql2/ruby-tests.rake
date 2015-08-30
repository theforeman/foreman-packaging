require 'rspec/core/rake_task'

RSpec::Core::RakeTask.new(:spec) do |spec|
  spec.pattern      = './spec/mysql2/**/*_spec.rb'
end

task :default => :spec
