$: << 'spec' << '.'
Dir['{spec}/**/*.rb'].each { |f| require f }
