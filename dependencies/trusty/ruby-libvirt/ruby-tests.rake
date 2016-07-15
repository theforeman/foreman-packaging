topdir = File.dirname(File.dirname(__FILE__))
ENV['XDG_RUNTIME_DIR'] = topdir
ENV['XDG_CONFIG_HOME'] = topdir
ENV['LIBVIRT_DEFAULT_URI'] = 'test:///default'
ENV['RUBY_LIBVIRT_TEST_URI'] = 'test:///default'

require 'gem2deb/rake/testtask'
Gem2Deb::Rake::TestTask.new do |t|
  t.test_files = [ 'tests/test_nodedevice.rb',
                   'tests/test_open.rb',
                   'tests/test_stream.rb' ]
end
