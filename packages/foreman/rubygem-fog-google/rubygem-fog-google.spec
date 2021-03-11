# Generated from fog-google-1.8.2.gem by gem2rpm -*- rpm-spec -*-
# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name fog-google

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.11.0
Release: 2%{?dist}
Summary: Module for the 'fog' gem to support Google
Group: Development/Languages
License: MIT
URL: https://github.com/fog/fog-google
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby >= 2.0
Requires: %{?scl_prefix_ruby}ruby < 3
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(fog-core) <= 2.1.0
Requires: %{?scl_prefix}rubygem(fog-json) >= 1.2
Requires: %{?scl_prefix}rubygem(fog-json) < 2
Requires: %{?scl_prefix}rubygem(fog-xml) >= 0.1.0
Requires: %{?scl_prefix}rubygem(fog-xml) < 0.2
Requires: %{?scl_prefix}rubygem(google-api-client) >= 0.32
Requires: %{?scl_prefix}rubygem(google-api-client) < 0.34
Requires: %{?scl_prefix}rubygem(google-cloud-env) >= 1.2
Requires: %{?scl_prefix}rubygem(google-cloud-env) < 2
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby >= 2.0
BuildRequires: %{?scl_prefix_ruby}ruby < 3
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

%description
This library can be used as a module for `fog` or as standalone provider to
use the Google Cloud in applications.


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}.

%prep
%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} - << \EOF}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:EOF}

%build
# Create the gem as gem install only works on a gem file
%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%{?scl:EOF}

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%{?scl:scl enable %{scl} - << \EOF}
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.codecov.yml
%exclude %{gem_instdir}/.editorconfig
%exclude %{gem_instdir}/.fog.example
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.hound.yml
%exclude %{gem_instdir}/.rubocop.yml
%exclude %{gem_instdir}/.ruby-gemset
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/LICENSE.md
%{gem_libdir}
%{gem_instdir}/tasks
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/CONTRIBUTORS.md
%doc %{gem_instdir}/SECURITY.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/examples
%{gem_instdir}/fog-google.gemspec
%{gem_instdir}/test
%{gem_instdir}/ci
%doc %{gem_instdir}/MIGRATING.md

%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.11.0-2
- Rebuild against rh-ruby27

* Thu Oct 08 2020 Ondřej Ezr <oezr@redhat.com> 1.11.0-1
- Update to 1.11.0

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.8.2-2
- Bump to release for EL8


* Tue Mar 12 2019 kgaikwad <kavitagaikwad103@gmail.com> 1.8.2-1
- Update to 1.8.2

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.1.0-4
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.1.0-3
- More rebuilds for Rails 5.1 (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 0.1.0-2
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Oct 06 2015 Dominic Cleal <dcleal@redhat.com> 0.1.0-1
- Update fog-google to 0.1.0 (elobatocs@gmail.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 0.0.7-2
- Converted to tfm SCL (dcleal@redhat.com)

* Tue Jul 07 2015 Dominic Cleal <dcleal@redhat.com> 0.0.7-1
- Update fog-google to 0.0.7 (dcleal@redhat.com)

* Mon May 11 2015 Dominic Cleal <dcleal@redhat.com> 0.0.5-1
- new package built with tito
