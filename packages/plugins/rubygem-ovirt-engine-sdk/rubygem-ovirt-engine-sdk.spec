# template: default
%global gem_name ovirt-engine-sdk
%global gem_require_name ovirtsdk4

Name: rubygem-%{gem_name}
Version: 4.6.0
Release: 2%{?dist}
Summary: oVirt SDK
License: Apache-2.0
URL: https://ovirt.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.5
BuildRequires: ruby-devel >= 2.5
BuildRequires: rubygems-devel
BuildRequires: (rubygem(json) >= 1 with rubygem(json) < 3)
# Compiler is required for build of gem binary extension.
# https://fedoraproject.org/wiki/Packaging:C_and_C++#BuildRequires_and_Requires
BuildRequires: gcc
# end specfile generated dependencies

BuildRequires: libcurl-devel
BuildRequires: libxml2-devel

%description
Ruby SDK for the oVirt Engine API.


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
%exclude %{gem_instdir}/.yardopts
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGES.adoc
%doc %{gem_instdir}/README.adoc

%changelog
* Tue Aug 12 2025 Evgeni Golov - 4.6.0-2
- Rebuild for plugins

* Sun Feb 04 2024 Foreman Packaging Automation <packaging@theforeman.org> - 4.6.0-1
- Update to 4.6.0

* Tue Jul 26 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 4.4.1-1
- Update to 4.4.1

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 4.4.0-2
- Rebuild against rh-ruby27

* Wed Dec 23 2020 Evgeni Golov 4.4.0-1
- Update to 4.4.0-1

* Mon Apr 20 2020 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 4.3.0-1
- Update to 4.3.0-1

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 4.2.3-4
- Bump to release for EL8

* Wed Sep 12 2018 Bryan Kearney <bryan.kearney@gmail.com> - 4.2.3-3
- Use ASL 2.0 instead of Apache 2.0 or Apache-2.0

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 4.2.3-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Wed Apr 04 2018 Ivan Necas <inecas@redhat.com> 4.2.3-1
- new package
