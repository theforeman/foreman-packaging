# -*- encoding: utf-8 -*-

Gem::Specification.new do |s|
  s.name = %q{foreman_scap_client}
  s.version = "0.4.0"

  s.required_rubygems_version = Gem::Requirement.new(">= 0") if s.respond_to? :required_rubygems_version=
  s.authors = ["Marek Hulan", "\305\240imon Luka\305\241\303\255k", "Shlomi Zadok"]
  s.date = %q{2017-02-20}
  s.default_executable = %q{foreman_scap_client}
  s.description = %q{Client script that runs openscap scan and uploads the result to foreman proxy}
  s.email = ["mhulan@redhat.com", "slukasik@redhat.com", "szadok@redhat.com"]
  s.executables = ["foreman_scap_client"]
  s.files = ["LICENSE", "README.md", "bin/foreman_scap_client", "config/config.yaml.example", "lib/foreman_scap_client.rb", "lib/foreman_scap_client/client.rb", "lib/foreman_scap_client/version.rb"]
  s.homepage = %q{https://github.com/openscap/foreman_scap_client}
  s.require_paths = ["lib"]
  s.requirements = ["/usr/bin/bzip2"]
  s.rubygems_version = %q{1.3.7}
  s.summary = %q{Client script that runs openscap scan and uploads the result to foreman proxy}

  if s.respond_to? :specification_version then
    current_version = Gem::Specification::CURRENT_SPECIFICATION_VERSION
    s.specification_version = 4

    s.add_development_dependency(%q<bundler>, ["~> 1.7"])
    s.add_development_dependency(%q<rake>, ["~> 10.0"])
  else
    s.add_dependency(%q<bundler>, ["~> 1.7"])
    s.add_dependency(%q<rake>, ["~> 10.0"])
  end
end
