# template: default
%global gem_name radcli
%global gem_require_name %{gem_name}

Name: rubygem-%{gem_name}
Version: 1.1.0
Release: 1%{?dist}
Summary: A Ruby interface for the adcli library
License: Artistic-2.0
URL: https://github.com/martencassel/radcli
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby
BuildRequires: ruby-devel
BuildRequires: rubygems-devel
BuildRequires: rubygem(rake-compiler)
# Compiler is required for build of gem binary extension.
# https://fedoraproject.org/wiki/Packaging:C_and_C++#BuildRequires_and_Requires
BuildRequires: gcc
# end specfile generated dependencies
BuildRequires: krb5-devel
BuildRequires: openldap-devel
BuildRequires: cyrus-sasl-devel

%description
The radcli library provides a Ruby interface for performing actions on
a Active Directory domain using the realmd/adcli tool library.


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

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/gem.build_complete %{buildroot}%{gem_extdir_mri}/
cp -a .%{gem_instdir}/ext/%{gem_name}/*.so %{buildroot}%{gem_extdir_mri}/

# rake-compiler isn't needed on the system itself
sed -i '/rake-compiler/ s/runtime/development/' %{buildroot}/%{gem_spec}

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
%exclude %{gem_instdir}/.devcontainer
%doc %{gem_instdir}/CHANGES
%license %{gem_instdir}/LICENSE
%exclude %{gem_instdir}/MANIFEST
%exclude %{gem_instdir}/build_adcli.sh
%exclude %{gem_instdir}/install.sh
%{gem_instdir}/scripts
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/radcli.gemspec
%{gem_instdir}/test

%changelog
* Wed Jul 24 2024 Evgeni Golov - 1.1.0-1
- Update to 1.1.0

* Fri Jan 05 2024 Evgeni Golov - 1.0.0-6
- Explicitly BuildRequire gcc

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.0.0-5
- Rebuild for Ruby 2.7

* Fri Mar 27 2020 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.0.0-4
- Add check section to test native library
- Fix building of native library

* Tue Jan 07 2020 Eric D. Helms <ericdhelms@gmail.com> - 1.0.0-3
- Build for SCL

* Tue Sep 17 2019 Eric D. Helms <ericdhelms@gmail.com> 1.0.0-2
- Update to support building for SCL

* Tue Jan 02 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.0.0-1
- new package built with tito

