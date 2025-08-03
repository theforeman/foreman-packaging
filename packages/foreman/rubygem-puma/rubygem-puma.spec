# template: default
%global gem_name puma
%global gem_require_name %{gem_name}

Name: rubygem-%{gem_name}
Version: 6.6.1
Release: 1%{?dist}
Summary: Puma is a simple, fast, threaded, and highly parallel HTTP 1.1 server for Ruby/Rack applications
License: BSD-3-Clause
URL: https://puma.io
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.4
BuildRequires: ruby-devel >= 2.4
BuildRequires: rubygems-devel
BuildRequires: (rubygem(nio4r) >= 2.0 with rubygem(nio4r) < 3)
# Compiler is required for build of gem binary extension.
# https://fedoraproject.org/wiki/Packaging:C_and_C++#BuildRequires_and_Requires
BuildRequires: gcc
# end specfile generated dependencies

BuildRequires: openssl-devel

%description
Puma is a simple, fast, threaded, and highly parallel HTTP 1.1 server for
Ruby/Rack applications. Puma is intended for use in both development and
production environments. It's great for highly parallel Ruby implementations
such as Rubinius and JRuby as well as as providing process worker support to
support CRuby well.


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

mkdir -p %{buildroot}%{gem_extdir_mri}/%{gem_name}
cp -a .%{gem_extdir_mri}/gem.build_complete %{buildroot}%{gem_extdir_mri}/
cp -a .%{gem_extdir_mri}/%{gem_name}/*.so %{buildroot}%{gem_extdir_mri}/%{gem_name}

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

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
%{_bindir}/puma
%{_bindir}/pumactl
%{gem_extdir_mri}
%license %{gem_instdir}/LICENSE
%{gem_instdir}/bin
%{gem_libdir}
%{gem_instdir}/tools
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/History.md
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/docs

%changelog
* Sun Aug 03 2025 Foreman Packaging Automation <packaging@theforeman.org> - 6.6.1-1
- Update to 6.6.1

* Wed Jan 29 2025 Foreman Packaging Automation <packaging@theforeman.org> - 6.6.0-1
- Update to 6.6.0

* Sun Nov 24 2024 Foreman Packaging Automation <packaging@theforeman.org> - 6.5.0-1
- Update to 6.5.0

* Fri Sep 20 2024 Foreman Packaging Automation <packaging@theforeman.org> - 6.4.3-1
- Update to 6.4.3

* Tue May 07 2024 Ian Ballou <ianballou67@gmail.com> - 6.4.2-2
- Add patch for chunking bug

* Tue Jan 09 2024 Foreman Packaging Automation <packaging@theforeman.org> - 6.4.2-1
- Update to 6.4.2

* Wed Jan 03 2024 Foreman Packaging Automation <packaging@theforeman.org> 6.4.1-1
- Update to 6.4.1

* Sun Sep 24 2023 Foreman Packaging Automation <packaging@theforeman.org> 6.4.0-1
- Update to 6.4.0

* Sat Aug 19 2023 Foreman Packaging Automation <packaging@theforeman.org> 6.3.1-1
- Update to 6.3.1

* Sun Jun 04 2023 Foreman Packaging Automation <packaging@theforeman.org> 6.3.0-1
- Update to 6.3.0

* Thu May 04 2023 Evgeni Golov 6.2.2-1
- Update to 6.2.2-1

* Sun Aug 28 2022 Foreman Packaging Automation <packaging@theforeman.org> 5.6.5-1
- Update to 5.6.5

* Wed May 18 2022 Eric D. Helms <ericdhelms@gmail.com> - 5.6.4-1
- Release rubygem-puma 5.6.4

* Fri Mar 18 2022 Eric D. Helms <ericdhelms@gmail.com> - 5.6.2-1
- Release rubygem-puma 5.6.2

* Thu Dec 02 2021 Evgeni Golov 5.5.2-1
- Update to 5.5.2

* Thu Sep 23 2021 Evgeni Golov 5.5.0-1
- Update to 5.5.0

* Wed May 26 2021 Eric D. Helms <ericdhelms@gmail.com> - 5.3.2-1
- Release 5.3.2

* Mon May 10 2021 Evgeni Golov 5.3.0-1
- Update to 5.3.0

* Mon Apr 05 2021 Eric D. Helms <ericdhelms@gmail.com> - 5.1.1-2
- Rebuild for Ruby 2.7

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
