# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name ovirt-engine-sdk
%global gem_require_name ovirtsdk4

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 4.4.0
Release: 2%{?dist}
Summary: oVirt SDK
Group: Development/Languages
License: ASL 2.0
URL: http://ovirt.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby >= 2.5
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}rubygem(json) >= 1
Requires: %{?scl_prefix_ruby}rubygem(json) < 3
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby-devel >= 2.5
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygem(json) >= 1
BuildRequires: %{?scl_prefix_ruby}rubygem(json) < 3
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

BuildRequires: libcurl-devel
BuildRequires: libxml2-devel

%description
Ruby SDK for the oVirt Engine API.


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

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/

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
%exclude %{gem_instdir}/ext
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
