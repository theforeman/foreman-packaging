%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name journald-native
%global gem_require_name journald/native

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.0.11
Release: 4%{?dist}
Summary: systemd-journal logging native lib wrapper
Group: Development/Languages
License: LGPLv2
URL: https://github.com/sandfoxme/journald-native
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby >= 1.9.2
Requires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby-devel >= 1.9.2
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: systemd-devel
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
systemd-journal logging native lib wrapper.


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

mkdir -p %{buildroot}%{gem_extdir_mri}
%if 0%{?scl:1}
  cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/
%else
  # for some reason, this file is not created by the build process on EL8
  touch .%{gem_instdir}/ext/journald_native/gem.build_complete
  cp -a .%{gem_instdir}/ext/journald_native/{gem.build_complete,journald_native.so} %{buildroot}%{gem_extdir_mri}/
%endif

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

%check
%{?scl:scl enable %{scl} - << \EOF}
# Ideally, this would be something like this:
# GEM_PATH="%{buildroot}%{gem_dir}:$GEM_PATH" ruby -e "require '%{gem_name}'"
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
%{gem_extdir_mri}
%exclude %{gem_instdir}/CHANGELOG.md
%exclude %{gem_instdir}/gems.rb
%exclude %{gem_instdir}/journald-native.gemspec
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile

%changelog
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

