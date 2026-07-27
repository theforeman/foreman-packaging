# template: default
%global gem_name sqlite3
%global gem_require_name %{gem_name}

Name: rubygem-%{gem_name}
Version: 1.7.3
Release: 2%{?dist}
Summary: This module allows Ruby programs to interface with the SQLite3 database engine (http://www.sqlite.org)
License: BSD-3-Clause
URL: https://github.com/sparklemotion/sqlite3-ruby
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.7.0
BuildRequires: ruby-devel >= 2.7.0
BuildRequires: rubygems-devel
# Compiler is required for build of gem binary extension.
# https://fedoraproject.org/wiki/Packaging:C_and_C++#BuildRequires_and_Requires
BuildRequires: gcc
# end specfile generated dependencies
BuildRequires: sqlite-devel

%description
This module allows Ruby programs to interface with the SQLite3
database engine (http://www.sqlite.org).  You must have the
SQLite engine installed in order to build this module.
Note that this module is only compatible with SQLite 3.6.16 or newer.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

# Remove bundled SQLite right away.
rm -rf ports
%gemspec_remove_file "ports/archives/sqlite-autoconf-3450200.tar.gz"

# This is not really runtime dependency, neither it is needed by official
# prebuild platform specific packages.
%gemspec_remove_dep -g mini_portile2 "~> 2.8.0"

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# Build against system SQLite3.
CONFIGURE_ARGS="--enable-system-libraries"

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}/%{gem_name}
cp -a .%{gem_extdir_mri}/gem.build_complete %{buildroot}%{gem_extdir_mri}/
cp -a .%{gem_extdir_mri}/%{gem_name}/*.so %{buildroot}%{gem_extdir_mri}/%{gem_name}

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

%check
# Ideally, this would be something like this:
# GEM_PATH="%{buildroot}%{gem_dir}:$GEM_PATH" ruby -e "require '%{gem_require_name}'"
# But that fails to find native extensions on EL8, so we fake the structure that ruby expects
mkdir gem_ext_test
cp -a %{buildroot}%{gem_dir} gem_ext_test/
mkdir -p gem_ext_test/gems/extensions/%{_arch}-%{_target_os}/$(ruby -r rbconfig -e 'print RbConfig::CONFIG["ruby_version"]')/
cp -a %{buildroot}%{gem_extdir_mri} gem_ext_test/gems/extensions/%{_arch}-%{_target_os}/$(ruby -r rbconfig -e 'print RbConfig::CONFIG["ruby_version"]')/
GEM_PATH="./gem_ext_test/gems:$GEM_PATH" ruby -e "require '%{gem_require_name}'"
rm -rf gem_ext_test

%files
%dir %{gem_instdir}
%{gem_extdir_mri}
%exclude %{gem_instdir}/.gemtest
%license %{gem_instdir}/LICENSE
# This does not apply because it does not bundle the SQLite3
# library.
%exclude %license %{gem_instdir}/LICENSE-DEPENDENCIES
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/API_CHANGES.md
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/ChangeLog.cvs
%doc %{gem_instdir}/FAQ.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/INSTALLATION.md
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/dependencies.yml
%{gem_instdir}/test

%changelog
* Mon Jul 27 2026 Zach Huntington-Meath <zhunting@redhat.com> - 1.7.3-2
- rebuilt

* Fri Dec 19 2025 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.7.3-1
- Update to 1.7.3

* Mon Dec 18 2023 Evgeni Golov 1.4.4-1
- Update to 1.4.4

* Thu May 05 2022 Evgeni Golov 1.4.2-1
- Update to 1.4.2

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.3.13-7
- Rebuild against rh-ruby27

* Fri Mar 27 2020 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.3.13-6
- Add check section to test native library

* Tue Mar 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.3.13-5
- Bump packages to build for el8

* Mon Jan 27 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.3.13-4
- Update spec to include Obsoletes of rails-packaging version

* Tue Jan 21 2020 Zach Huntington-Meath <zhunting@redhat.com> 1.3.13-3
- Bump to move the .so file to the proper place

* Thu Dec 19 2019 Zach Huntington-Meath <zhunting@redhat.com> 1.3.13-2
- Bump for moving over to foreman-packaging

* Tue Aug 14 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.3.13-1
- Initial package
