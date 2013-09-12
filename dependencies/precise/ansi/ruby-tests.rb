# FIXME
# there's a spec/ or a test/ directory in the upstream source, but
# no test suite was defined in the Gem specification. It would be
# a good idea to define it here so the package gets tested at build time.
# Examples:
# $: << 'lib' << '.'
# Dir['{spec,test}/**/*.rb'].each { |f| require f }
#
# require 'test/ts_foo.rb'
#
# require 'rbconfig'
# ruby = File.join(RbConfig::CONFIG['bindir'], RbConfig::CONFIG['ruby_install_name'])
# exec("#{ruby} -I. test/runtests.rb")
