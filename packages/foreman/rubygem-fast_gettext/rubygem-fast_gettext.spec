%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name fast_gettext

Summary: A simple, fast, memory-efficient and threadsafe implementation of GetText
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.4.1
Release: 5%{?dist}
Group: Development/Languages
# fast_gettext is MIT. However the files in lib/vendor directory
# are GPLv2+ or Ruby licensed.
# https://github.com/grosser/fast_gettext/issues/50
License: MIT and (GPLv2+ or Ruby)
URL: https://github.com/grosser/fast_gettext
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}rubygems
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
A simple, fast, memory-efficient and threadsafe implementation of GetText

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

# SCL-enable shebang lines
find %{buildroot}%{gem_libdir} -type f -exec \
  sed -i -e 's"^#! /usr/bin/ruby"#!%{?scl:%_scl_root}/usr/bin/ruby"' {} +

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/Readme.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_instdir}/CHANGELOG
%doc %{gem_docdir}

%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.4.1-5
- Rebuild against rh-ruby27

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.4.1-4
- Bump to release for EL8

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.4.1-3
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.4.1-2
- More rebuilds for Rails 5.1 (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Wed Jul 12 2017 Eric D. Helms <ericdhelms@gmail.com> 1.4.1-1
- Update fast_gettext to 1.4.1 (tbrisker@gmail.com)

* Tue May 31 2016 Dominic Cleal <dominic@cleal.org> 1.1.0-1
- Update fast_gettext to 1.1.0 (dominic@cleal.org)

* Tue Apr 12 2016 Dominic Cleal <dominic@cleal.org> 1.0.0-1
- Update fast_gettext to 1.0.0 (dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 0.9.2-3
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 0.9.2-2
- Fix checks against scl name, optimise rhel/empty SCL conditional
  (dcleal@redhat.com)
- Converted to tfm SCL (dcleal@redhat.com)

* Mon Jan 12 2015 Dominic Cleal <dcleal@redhat.com> 0.9.2-1
- Update fast_gettext to 0.9.2 (dcleal@redhat.com)

* Thu Jan 08 2015 Dominic Cleal <dcleal@redhat.com> 0.9.1-1
- Update fast_gettext to 0.9.1 (dcleal@redhat.com)

* Mon Nov 24 2014 Dominic Cleal <dcleal@redhat.com> 0.8.1-1
- Update fast_gettext to 0.8.1 (dcleal@redhat.com)

* Thu May 29 2014 Dominic Cleal <dcleal@redhat.com> 0.8.0-15
- Modernise and update for EL7 (dcleal@redhat.com)

* Wed Mar 19 2014 Jason Montleon <jmontleo@redhat.com> 0.8.0-14
- remove unnecessary Require for rubygems-devel. Only needed as a BuildRequire
  (jmontleo@redhat.com)

* Tue Mar 18 2014 Jason Montleon <jmontleo@redhat.com> 0.8.0-13
- fix fedora 19 builds, add rubygems-devel dependency (jmontleo@redhat.com)

* Mon Mar 17 2014 Jason Montleon <jmontleo@redhat.com> 0.8.0-7
- update build dependencies (jmontleo@redhat.com)

* Mon Mar 17 2014 Jason Montleon <jmontleo@redhat.com> 0.8.0-6
- update build dependencies (jmontleo@redhat.com)

* Mon Mar 17 2014 Jason Montleon <jmontleo@redhat.com> 0.8.0-5
- update build dependencies (jmontleo@redhat.com)

* Mon Mar 17 2014 Jason Montleon <jmontleo@redhat.com> 0.8.0-4
-

* Mon Dec 02 2013 Jason Montleon <jmontleo@redhat.com> 0.8.0-3
- Temporary file permission fix for string.rb (lzap+git@redhat.com)
- SCL-enable shebang lines (dcleal@redhat.com)

* Tue Sep 17 2013 Jason Montleon <jmontleo@redhat.com> 0.8.0-2
- update rubygem-fast_gettext to 0.8.0 for Foreman 1.3 (jmontleo@redhat.com)

* Thu Sep 12 2013 Lukas Zapletal <lzap+git@redhat.com> 0.8.0-2
- Revert "update rubygems to include wrapper BuildRequires and Requires"
  (jmontleo@redhat.com)
- update rubygems to include wrapper BuildRequires and Requires
  (jmontleo@redhat.com)

* Fri Aug 30 2013 Lukas Zapletal <lzap+rpm[@]redhat.com> - 0.8.0-1
- update to 0.8.0 (multi-domain support)
- renamed spec name to comply with standards
- new SPEC content derived from F19 (0.7.1-1) and spec2scl

* Mon Aug 19 2013 Vít Ondruch <vondruch@redhat.com> - 0.7.1-1
- Update to fast_gettext 0.7.1.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 07 2013 Vít Ondruch <vondruch@redhat.com> - 0.7.0-1
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0
- Update to fast_gettext 0.7.0.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Feb 02 2012 Vít Ondruch <vondruch@redhat.com> - 0.6.1-3
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 17 2011 Vít Ondruch <vondruch@redhat.com> - 0.6.1-1
- Update to fast_gettext 6.1.

* Mon Aug 01 2011 Vít Ondruch <vondruch@redhat.com> - 0.5.13-1
- Initial package
