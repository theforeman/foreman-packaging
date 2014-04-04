inc = $:.map { |d| "-I#{d}" }.join(' ')
p inc
ENV['json'] = 'pure'
puts "Pure version of the tests"
system("#{ENV['RUBY_TEST_BIN']} #{inc} tests/test_*.rb") or raise
ENV['json'] = 'ext'
puts "Ext version of the tests"
system("#{ENV['RUBY_TEST_BIN']} #{inc} tests/test_*.rb") or raise
