load 'Rakefile'

gemspec = "ruby-libvirt-#{PKG_VERSION}.gemspec"

task :gemspec => gemspec
file gemspec do |t|
  File.open(t.name, 'w') { |f| f.write(SPEC.to_ruby) }
end
