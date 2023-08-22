# template: default
%global gem_name netbox-client-ruby

Name: rubygem-%{gem_name}
Version: 0.6.0
Release: 1%{?dist}
Summary: A read/write client for Netbox v2
License: MIT
URL: https://github.com/ninech/netbox-client-ruby
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.6.0
BuildRequires: ruby >= 2.6.0
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
A read/write client for Netbox v2.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

# openssl is bundled with ruby
%gemspec_remove_dep -g openssl

# Allow faraday 1.x
# https://github.com/ninech/netbox-client-ruby/pull/58
%gemspec_remove_dep -g faraday ["~> 0.11", ">= 0.11.0"]
%gemspec_add_dep -g faraday [">= 0.11.0", "< 2"]
%gemspec_remove_dep -g faraday_middleware ["~> 0.11"]
%gemspec_add_dep -g faraday_middleware [">= 0.11", "< 2"]

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.github
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/Dockerfile
%license %{gem_instdir}/LICENSE.txt
%exclude %{gem_instdir}/VERSION
%exclude %{gem_instdir}/bin
%exclude %{gem_instdir}/dump.sql
%{gem_libdir}
%exclude %{gem_instdir}/netbox-client-ruby_rsa
%exclude %{gem_instdir}/netbox-client-ruby_rsa.pub
%exclude %{gem_instdir}/netbox.env
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%exclude %{gem_instdir}/.dockerignore
%exclude %{gem_instdir}/.rspec
%exclude %{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/docker-compose.test.yml
%exclude %{gem_instdir}/docker-compose.yml
%exclude %{gem_instdir}/docker
%exclude %{gem_instdir}/netbox-client-ruby.gemspec

%changelog
* Tue Aug 22 2023 Dirk Goetz <dirk.goetz@netways.de> 0.6.0-1
- Update to 0.6.0

* Thu Jul 14 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 0.5.6-3
- Regenerate spec
- Correctly allow faraday 1.x
- Exclude more unrelated files

* Thu Jul 07 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 0.5.6-2
- Allow rubygem-faraday 1.x
- Use gemspec_remove_dep macro instead of a patch to drop openssl

* Tue May 31 2022 Dirk Goetz <dirk.goetz@netways.de> 0.5.6-1
- Add rubygem-netbox-client-ruby generated by gem2rpm using the scl template
