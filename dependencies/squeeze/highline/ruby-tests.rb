if defined? Encoding
  Encoding.default_external = Encoding::UTF_8
end

$: << 'lib' << 'test' << '.'
Dir['{spec,test}/**/{test,tc}_*.rb'].each { |f| require f }
