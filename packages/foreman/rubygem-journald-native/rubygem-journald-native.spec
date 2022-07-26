# template: default
%global gem_name journald-native
%global gem_require_name journald/native

Name: rubygem-%{gem_name}
Version: 1.0.12
Release: 1%{?dist}
Summary: systemd-journal logging native lib wrapper
License: LGPLv2+
URL: https://github.com/theforeman/journald-native
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 1.9.3
BuildRequires: ruby-devel >= 1.9.3
BuildRequires: rubygems-devel
# Compiler is required for build of gem binary extension.
# https://fedoraproject.org/wiki/Packaging:C_and_C++#BuildRequires_and_Requires
BuildRequires: gcc
# end specfile generated dependencies

BuildRequires: systemd-devel

%description
systemd-journal logging native lib wrapper.


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

mkdir -p %{buildroot}%{gem_extdir_mri}/
cp -a .%{gem_extdir_mri}/{*.so,gem.build_complete} %{buildroot}%{gem_extdir_mri}/

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
%license %{gem_instdir}/COPYING.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
* Tue Jul 26 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.0.12-1
- Update to 1.0.12

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.0.11-4
- Rebuild against rh-ruby27

* Wed Apr 15 2020 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.0.11-3
- Add check section to test native library

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.0.11-2
- Bump to release for EL8

* Fri Oct 12 2018 Lukas Zapletal <lzap+rpm@redhat.com> 1.0.11-1
- Bump version to the latest upstream version

* Thu Sep 13 2018 Bryan Kearney <bryan.kearney@gmail.com> - 1.0.10-3
- Use LGPLv2 for versions 2 and 2.1 of the license

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.0.10-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Tue Apr 03 2018 Lukas Zapletal <lzap+rpm@redhat.com> 1.0.10-1
- new upstream release (contains relative load patch)
- dropped relative loading patch

* Thu Mar 29 2018 Lukas Zapletal <lzap+rpm@redhat.com> 1.0.9-2
- added relative loading patch

* Tue Feb 20 2018 Daniel Lobato Garcia <me@daniellobato.me> 1.0.9-1
- new package built with tito

