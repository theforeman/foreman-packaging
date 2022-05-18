# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name nokogiri
%global gem_require_name %{gem_name}

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.13.6
Release: 2%{?dist}
Summary: Nokogiri (鋸) makes it easy and painless to work with XML and HTML from Ruby
Group: Development/Languages
License: MIT
URL: https://nokogiri.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# On EL8 rubygem-racc is bundled into ruby-libs package and
# auto-generated dependencies will break dependency resolution
Autoreq: 0

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby >= 2.6.0
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(mini_portile2) >= 2.8.0
Requires: %{?scl_prefix}rubygem(mini_portile2) < 2.9
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby-devel >= 2.6.0
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix}rubygem(mini_portile2) >= 2.8.0
BuildRequires: %{?scl_prefix}rubygem(mini_portile2) < 2.9
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies
BuildRequires: libxml2-devel
BuildRequires: libxslt-devel

%if 0%{?rhel} >= 8
Requires: bundled(rubygem-racc) >= 1.4
Requires: bundled(rubygem-racc) < 2
BuildRequires: bundled(rubygem-racc) >= 1.4
BuildRequires: bundled(rubygem-racc) < 2
%else
Requires: %{?scl_prefix}rubygem(racc) >= 1.4
Requires: %{?scl_prefix}rubygem(racc) < 2
BuildRequires: %{?scl_prefix}rubygem(racc) >= 1.4
BuildRequires: %{?scl_prefix}rubygem(racc) < 2
%endif

%description
Nokogiri (鋸) makes it easy and painless to work with XML and HTML from Ruby.
It provides a
sensible, easy-to-understand API for reading, writing, modifying, and querying
documents. It is
fast and standards-compliant by relying on native parsers like libxml2 (C) and
xerces (Java).


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

mkdir -p %{buildroot}%{gem_extdir_mri}/%{gem_name}
cp -a .%{gem_extdir_mri}/gem.build_complete %{buildroot}%{gem_extdir_mri}/
cp -a .%{gem_extdir_mri}/%{gem_name}/*.so %{buildroot}%{gem_extdir_mri}/%{gem_name}/

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
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
%{_bindir}/nokogiri
%exclude %{gem_instdir}/ext
%{gem_extdir_mri}
%license %{gem_instdir}/LICENSE-DEPENDENCIES.md
%license %{gem_instdir}/LICENSE.md
%{gem_instdir}/bin
%{gem_instdir}/dependencies.yml
%{gem_instdir}/gumbo-parser
%{gem_libdir}
%{gem_instdir}/patches
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md

%changelog
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
