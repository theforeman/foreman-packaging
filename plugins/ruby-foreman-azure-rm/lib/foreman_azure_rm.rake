# frozen_string_literal: true

# Tests
namespace :test do
  desc 'Test foreman_azure_rm'
  Rake::TestTask.new(:foreman_azure_rm) do |t|
    test_dir = File.join(File.dirname(__FILE__), '..', 'test')
    t.libs << ['test', test_dir]
    t.pattern = "#{test_dir}/**/*_test.rb"
    t.verbose = true
    t.warning = false
  end
end
