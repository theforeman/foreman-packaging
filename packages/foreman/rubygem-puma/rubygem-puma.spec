# Generated from puma-3.11.4.gem by gem2rpm -*- rpm-spec -*-
# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name puma
%global gem_require_name %{gem_name}

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 5.1.1
Release: 2%{?dist}
Summary: Puma is a simple, fast, threaded, and highly concurrent HTTP 1.1 server for Ruby/Rack applications
Group: Development/Languages
License: BSD-3-Clause
URL: https://puma.io
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0: rdoc-issue-14617-workaround.patch

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby >= 2.2
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(nio4r) >= 2.0
Requires: %{?scl_prefix}rubygem(nio4r) < 3
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby-devel >= 2.2
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix}rubygem(nio4r) >= 2.0
BuildRequires: %{?scl_prefix}rubygem(nio4r) < 3
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

# Puma 5.1.0 includes systemd support so the plugin is no longer needed
Obsoletes: %{?scl_prefix}rubygem-puma-plugin-systemd < 0.1.5-2

BuildRequires: openssl-devel

%description
Puma is a simple, fast, threaded, and highly concurrent HTTP 1.1 server for
Ruby/Rack applications. Puma is intended for use in both development and
production environments. It's great for highly concurrent Ruby implementations
such as Rubinius and JRuby as well as as providing process worker support to
support CRuby well.


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

%autosetup -p1 -D -T -n  %{gem_name}-%{version}

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

mkdir -p %{buildroot}%{gem_extdir_mri}/puma
cp -a .%{gem_extdir_mri}/gem.build_complete %{buildroot}%{gem_extdir_mri}/
cp -a .%{gem_extdir_mri}/puma/*.so %{buildroot}%{gem_extdir_mri}/puma

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

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
%{_bindir}/puma
%{_bindir}/pumactl
%{gem_extdir_mri}
%license %{gem_instdir}/LICENSE
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/History.md
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/docs
%doc %{gem_instdir}/tools

%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 5.1.1-2
- Rebuild against rh-ruby27

* Thu Jan 07 2021 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 5.1.1-1
- Update to 5.1.1

* Thu Oct 15 2020 Eric D. Helms <ericdhelms@gmail.com> - 4.3.6-1
- Release rubygem-puma 4.3.6

* Thu May 28 2020 Eric D. Helms <ericdhelms@gmail.com> - 4.3.5-1
- Update to 4.3.5

* Thu Apr 16 2020 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 4.3.3-4
- Add check section to test native library

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 4.3.3-3
- Bump to release for EL8

* Wed Apr 01 2020 Eric D. Helms <ericdhelms@gmail.com> - 4.3.3-2
- Build puma with SSL support

* Tue Mar 17 2020 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 4.3.3-1
- Update to 4.3.3

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 3.11.4-3
- Rebuild for Rails 5.2 and Ruby 2.5

* Sat Jun 02 2018 Eric D. Helms <ericdhelms@gmail.com> 3.11.4-2
- Update rubygem-puma spec and rebuild

* Mon Apr 30 2018 Eric D. Helms <ericdhelms@gmail.com> 3.11.4-1
- Add rubygem-puma generated by gem2rpm using the scl template
