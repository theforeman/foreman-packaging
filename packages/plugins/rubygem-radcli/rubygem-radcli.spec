# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name radcli
%global gem_require_name %{gem_name}

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.0.0
Release: 4%{?dist}
Summary: A Ruby interface for the adcli library
Group: Development/Languages
License: Artistic-2.0
URL: https://github.com/martencassel/radcli
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires: %{?scl_prefix}rubygem(rake-compiler)
BuildRequires: krb5-devel
BuildRequires: openldap-devel
BuildRequires: cyrus-sasl-devel

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby-devel
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

%description
The radcli library provides a Ruby interface for performing actions on
a Active Directory domain using the realmd/adcli tool library.


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
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%if 0%{?scl:1}
mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/gem.build_complete %{buildroot}%{gem_extdir_mri}/
cp -a .%{gem_instdir}/ext/%{gem_name}/*.so %{buildroot}%{gem_extdir_mri}/
%else
mkdir -p %{buildroot}%{gem_extdir_mri}/lib
cp -a %{buildroot}%{gem_instdir}/lib/radcli.so %{buildroot}%{gem_extdir_mri}/lib/
%endif

# rake-compiler isn't needed on the system itself
sed -i '/rake-compiler/ s/runtime/development/' %{buildroot}/%{gem_spec}

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

%check
%{?scl:scl enable %{scl} - << \EOF}
# Ideally, this would be something like this:
# GEM_PATH="%{buildroot}%{gem_dir}:$GEM_PATH" ruby -e "require '%{gem_require_name}'"
# But that fails to find native extensions on EL8, so we fake the structure that ruby expects
mkdir gem_ext_test
cp -a %{buildroot}%{gem_dir} gem_ext_test/
mkdir -p gem_ext_test/gems/extensions/%{_arch}-%{_target_os}/$(ruby -r rbconfig -e 'print RbConfig::CONFIG["ruby_version"]')/
cp -a %{buildroot}%{gem_extdir_mri} gem_ext_test/gems/extensions/%{_arch}-%{_target_os}/$(ruby -r rbconfig -e 'print RbConfig::CONFIG["ruby_version"]')/
GEM_PATH="./gem_ext_test/gems:$GEM_PATH" ruby -e "require '%{gem_require_name}'"
rm -rf gem_ext_test
%{?scl:EOF}

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_instdir}/MANIFEST
%{gem_instdir}/build_adcli.sh
%{gem_instdir}/scripts
%exclude %{gem_cache}
%{gem_spec}
%exclude %{gem_instdir}/radcli.gemspec
%{gem_extdir_mri}
%if 0%{!?scl:1}
%{gem_libdir}
%endif

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/CHANGES
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
* Fri Mar 27 2020 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.0.0-4
- Add check section to test native library
- Fix building of native library

* Tue Jan 07 2020 Eric D. Helms <ericdhelms@gmail.com> - 1.0.0-3
- Build for SCL

* Tue Sep 17 2019 Eric D. Helms <ericdhelms@gmail.com> 1.0.0-2
- Update to support building for SCL

* Tue Jan 02 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.0.0-1
- new package built with tito

