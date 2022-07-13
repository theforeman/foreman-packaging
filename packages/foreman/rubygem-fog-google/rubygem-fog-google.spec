# template: default
%global gem_name fog-google

Name: rubygem-%{gem_name}
Version: 1.18.0
Release: 1%{?dist}
Summary: Module for the 'fog' gem to support Google
License: MIT
URL: https://github.com/fog/fog-google
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.0
BuildRequires: ruby >= 2.0
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
This library can be used as a module for `fog` or as standalone provider to
use the Google Cloud in applications.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

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
%exclude %{gem_instdir}/.codecov.yml
%exclude %{gem_instdir}/.editorconfig
%exclude %{gem_instdir}/.fog.example
%exclude %{gem_instdir}/.github
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.hound.yml
%exclude %{gem_instdir}/.rubocop.yml
%exclude %{gem_instdir}/.ruby-gemset
%exclude %{gem_instdir}/fog-google.gemspec
%license %{gem_instdir}/LICENSE.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/CONTRIBUTORS.md
%doc %{gem_instdir}/MIGRATING.md
%doc %{gem_instdir}/SECURITY.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/examples
%{gem_instdir}/tasks
%{gem_instdir}/test

%changelog
* Wed Jul 13 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.18.0-1
- Update to 1.18.0

* Thu May 19 2022 Evgeni Golov 1.15.0-1
- Update to 1.15.0

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
