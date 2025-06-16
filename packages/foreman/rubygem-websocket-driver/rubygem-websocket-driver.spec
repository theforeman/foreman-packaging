# template: default
%global gem_name websocket-driver
%global gem_require_name websocket/driver

Name: rubygem-%{gem_name}
Version: 0.8.0
Release: 1%{?dist}
Summary: WebSocket protocol handler with pluggable I/O
License: Apache-2.0
URL: https://github.com/faye/websocket-driver-ruby
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby
BuildRequires: ruby-devel
BuildRequires: rubygems-devel
BuildRequires: rubygem(websocket-extensions) >= 0.1.0
# Compiler is required for build of gem binary extension.
# https://fedoraproject.org/wiki/Packaging:C_and_C++#BuildRequires_and_Requires
BuildRequires: gcc
# end specfile generated dependencies
Requires: (rubygem(base64) or ruby-default-gems < 3.4)
BuildRequires: (rubygem(base64) or ruby-default-gems < 3.4)

%description
WebSocket protocol handler with pluggable I/O.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

%gemspec_remove_dep -g base64

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

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/

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
%exclude %{gem_instdir}/ext
%{gem_extdir_mri}
%license %{gem_instdir}/LICENSE.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
* Mon Jun 16 2025 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 0.8.0-1
- Update to 0.8.0

* Wed Jan 08 2025 Foreman Packaging Automation <packaging@theforeman.org> - 0.7.7-1
- Update to 0.7.7

* Sun Aug 20 2023 Foreman Packaging Automation <packaging@theforeman.org> 0.7.6-1
- Update to 0.7.6

* Wed Jul 06 2022 Foreman Packaging Automation <packaging@theforeman.org> 0.7.5-1
- Update to 0.7.5

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.7.1-2
- Rebuild against rh-ruby27

* Mon Apr 13 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.7.1-1
- Release rubygem-websocket-driver 0.7.1

* Fri Mar 27 2020 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 0.7.0-5
- Add check section to test native library

* Tue Mar 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.7.0-4
- Bump packages to build for el8

* Mon Jan 27 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.7.0-3
- Update spec to include Obsoletes of rails-packaging version

* Thu Dec 19 2019 Zach Huntington-Meath <zhunting@redhat.com> 0.7.0-2
- Bump for moving over to foreman-packaging

* Mon Aug 06 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.7.0-1
- Initial package
