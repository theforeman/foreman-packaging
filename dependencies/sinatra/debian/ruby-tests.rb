$: << 'lib' << 'test' << '.'
Dir['test/**/*_test.rb'].each { |f| require f }
