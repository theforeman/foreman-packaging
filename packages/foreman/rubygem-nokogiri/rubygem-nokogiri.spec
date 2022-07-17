# template: default
%global gem_name nokogiri
%global gem_require_name %{gem_name}

Name: rubygem-%{gem_name}
Version: 1.13.7
Release: 1%{?dist}
Summary: Nokogiri (鋸) makes it easy and painless to work with XML and HTML from Ruby
License: MIT
URL: https://nokogiri.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# On EL8 rubygem-racc is bundled into ruby-libs package and
# auto-generated dependencies will break dependency resolution
Autoreq: 0

# start specfile generated dependencies
Requires: ruby >= 2.6.0
BuildRequires: ruby-devel >= 2.6.0
BuildRequires: rubygems-devel
BuildRequires: rubygem(mini_portile2) >= 2.8.0
BuildRequires: rubygem(mini_portile2) < 2.9
# Compiler is required for build of gem binary extension.
# https://fedoraproject.org/wiki/Packaging:C_and_C++#BuildRequires_and_Requires
BuildRequires: gcc
# end specfile generated dependencies
BuildRequires: libxml2-devel
BuildRequires: libxslt-devel

Requires: bundled(rubygem-racc) >= 1.4
Requires: bundled(rubygem-racc) < 2
BuildRequires: bundled(rubygem-racc) >= 1.4
BuildRequires: bundled(rubygem-racc) < 2

%description
Nokogiri (鋸) makes it easy and painless to work with XML and HTML from Ruby.
It provides a
sensible, easy-to-understand API for reading, writing, modifying, and querying
documents. It is
fast and standards-compliant by relying on native parsers like libxml2 (C) and
xerces (Java).


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
%{_bindir}/nokogiri
%{gem_extdir_mri}
%license %{gem_instdir}/LICENSE-DEPENDENCIES.md
%license %{gem_instdir}/LICENSE.md
%{gem_instdir}/bin
%{gem_instdir}/dependencies.yml
%{gem_instdir}/gumbo-parser
%{gem_libdir}
%{gem_instdir}/patches
%exclude %{gem_instdir}/ports
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md

%changelog
* Sun Jul 17 2022 Foreman Packaging Automation <packaging@theforeman.org> 1.13.7-1
- Update to 1.13.7

* Wed May 18 2022 Eric D. Helms <ericdhelms@gmail.com> - 1.13.6-2
- Add back disable of Autoreq

* Fri May 13 2022 Eric D. Helms <ericdhelms@gmail.com> - 1.13.6-1
- Release rubygem-nokogiri 1.13.6

* Thu May 27 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.11.3-2
- Do not generate auto requires due to rubygem-racc

* Fri Apr 30 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.11.3-1
- Release 1.11.3

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.10.9-2
- Rebuild against rh-ruby27

* Thu Apr 30 2020 Zach Huntington-Meath <zhunting@redhat.com> 1.10.9-1
- Update to 1.10.9

* Thu Apr 16 2020 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.8.4-8
- Add check section to test native library

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.8.4-7
- Bump release to build for el8

* Tue Jan 21 2020 Zach Huntington-Meath <zhunting@redhat.com> 1.8.4-6
- Bump to Obsolete the ror_52 version of Nokogiri

* Tue Jan 21 2020 Zach Huntington-Meath <zhunting@redhat.com> 1.8.4-5
- Bump to fix issue with nokogiri.so placement

* Mon Jan 20 2020 Zach Huntington-Meath <zhunting@redhat.com> 1.8.4-4
- Bump to fix issue with nokogiri.so placement

* Thu Dec 19 2019 Zach Huntington-Meath <zhunting@redhat.com> 1.8.4-3
- Bump for moving over to foreman-packaging

* Thu Aug 09 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.8.4-2
- Add missing gem_docdir

* Mon Aug 06 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.8.4-1
- Initial package
