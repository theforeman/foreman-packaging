require 'rspec/core/rake_task'
RSpec::Core::RakeTask.new(:spec) do |spec|
  spec.pattern = 'spec/**/*_spec.rb'
#  spec.spec_opts = ['--options', 'spec/spec.opts']
end

task :default => :spec
