# template: default
%global gem_name nio4r
%global gem_require_name nio

Name: rubygem-%{gem_name}
Version: 2.7.4
Release: 1%{?dist}
Summary: New IO for Ruby
License: MIT
URL: https://github.com/socketry/nio4r
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.6
BuildRequires: ruby-devel >= 2.6
BuildRequires: rubygems-devel
# Compiler is required for build of gem binary extension.
# https://fedoraproject.org/wiki/Packaging:C_and_C++#BuildRequires_and_Requires
BuildRequires: gcc
# end specfile generated dependencies

%description
Cross-platform asynchronous I/O primitives for scalable network clients and
servers. Inspired by the Java NIO API, but simplified for ease-of-use.


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
%{gem_extdir_mri}
%{gem_libdir}
%license %{gem_instdir}/license.md
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/changes.md
%doc %{gem_instdir}/readme.md

%changelog
* Wed Oct 30 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.7.4-1
- Update to 2.7.4

* Sun May 12 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.7.3-1
- Update to 2.7.3

* Sun Mar 24 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.7.1-1
- Update to 2.7.1

* Sun Dec 17 2023 Foreman Packaging Automation <packaging@theforeman.org> 2.7.0-1
- Update to 2.7.0

* Sun Apr 09 2023 Foreman Packaging Automation <packaging@theforeman.org> 2.5.9-1
- Update to 2.5.9

* Tue Jul 26 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.5.8-1
- Update to 2.5.8

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 2.5.4-2
- Rebuild against rh-ruby27

* Fri Sep 25 2020 Eric D. Helms <ericdhelms@gmail.com> - 2.5.4-1
- Release rubygem-nio4r 2.5.4

* Thu Sep 17 2020 Patrick Creech <pcreech@redhat.com> - 2.5.2-2
- Use '-fno-strict-aliasing' due to "warning: dereferencing type-punned pointer will break strict-aliasing rules"

* Mon Apr 13 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.5.2-1
- Release rubygem-nio4r 2.5.2

* Fri Mar 27 2020 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.3.1-5
- Add check section to test native library

* Mon Mar 02 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.3.1-4
- Update all rails packages for el8

* Mon Jan 27 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.3.1-3
- Update spec to include Obsoletes of rails-packaging version

* Thu Dec 19 2019 Zach Huntington-Meath <zhunting@redhat.com> 2.3.1-2
- Bump for moving over to foreman-packaging

* Thu Jul 26 2018 Eric D. Helms <ericdhelms@gmail.com> - 2.3.1-1
- Initial package
