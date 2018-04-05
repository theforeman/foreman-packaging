# This package contains macros that provide functionality relating to
# Software Collections. These macros are not used in default
# Fedora builds, and should not be blindly copied or enabled.
# Specifically, the "scl" macro must not be defined in official Fedora
# builds. For more information, see:
# http://docs.fedoraproject.org/en-US/Fedora_Contributor_Documentation/1/html/Software_Collections_Guide/index.html

%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_openscap

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.8.6
Release: 1%{?foremandist}%{?dist}
Summary: Foreman plug-in for displaying OpenSCAP audit reports
Group: Applications/System
License: GPLv3
URL: https://github.com/OpenSCAP/foreman_openscap
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: foreman >= 1.16.0

Requires: scap-security-guide
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(deface) < 2.0
Obsoletes: %{?scl_prefix}rubygem(scaptimony) < 0.3.2-3

BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems
BuildRequires: foreman-assets >= 1.7.0
BuildRequires: foreman-plugin >= 1.8.0
BuildRequires: %{?scl_prefix}rubygem(deface) < 2.0

BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-openscap
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Foreman plug-in for managing security compliance reports.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%{?scl:scl enable %{scl} "}
gem unpack %{SOURCE0}
%{?scl:"}

%setup -q -D -T -n  %{gem_name}-%{version}
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{foreman_bundlerd_dir}

%foreman_bundlerd_file
%foreman_precompile_plugin -a -s

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_instdir}/app
%{gem_instdir}/db
%{gem_instdir}/config
%{gem_instdir}/locale
%foreman_apipie_cache_plugin
%foreman_apipie_cache_foreman
%foreman_assets_plugin

%exclude %{gem_cache}
%{gem_spec}
%{foreman_bundlerd_plugin}
%doc %{gem_instdir}/LICENSE

%exclude %{gem_instdir}/test

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.md

%posttrans
# We need to run the db:migrate (because of SCAPtimony) after the install transaction
%foreman_db_migrate
%foreman_db_seed
%foreman_apipie_cache
%foreman_restart
exit 0

%changelog
* Thu Apr 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.8.6-1
- Update foreman_openscap to 0.8.6 (mhulan@redhat.com)

* Fri Oct 27 2017 Daniel Lobato Garcia <me@daniellobato.me> 0.8.3-2
- Precompile assets for foreman_openscap in nightlies
  (xprazak2@users.noreply.github.com)

* Tue Oct 24 2017 Daniel Lobato Garcia <me@daniellobato.me> 0.8.3-1
- Update foreman_openscap to 0.8.3 (ares@users.noreply.github.com)

* Wed Sep 27 2017 Daniel Lobato Garcia <me@daniellobato.me> 0.8.2-1
- Update foreman_openscap to 0.8.2 (ares@users.noreply.github.com)

* Wed Sep 13 2017 Daniel Lobato Garcia <me@daniellobato.me> 0.8.1-1
- Update foreman_openscap to 0.8.1 (ares@users.noreply.github.com)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Wed Jun 28 2017 Eric D. Helms <ericdhelms@gmail.com> 0.8.0-1
- Update foreman_openscap to 0.8.0 (mhulan@redhat.com)

* Fri Jun 23 2017 Eric D. Helms <ericdhelms@gmail.com> 0.7.3-1
- Update foreman_openscap to 0.7.3 (mhulan@redhat.com)

* Wed May 31 2017 Dominic Cleal <dominic@cleal.org> 0.7.2-1
- Update foreman_openscap to 0.7.2 (mhulan@redhat.com)

* Wed Apr 05 2017 Dominic Cleal <dominic@cleal.org> 0.7.1-1
- Update foreman_openscap to 0.7.1 (mhulan@redhat.com)

* Thu Mar 30 2017 Dominic Cleal <dominic@cleal.org> 0.7.0-1
- Update foreman_openscap to 0.7.0 (mhulan@redhat.com)

* Fri Mar 24 2017 Dominic Cleal <dominic@cleal.org> 0.6.6-1
- Update foreman_openscap to 0.6.6 (mhulan@redhat.com)

* Wed Mar 15 2017 Dominic Cleal <dominic@cleal.org> 0.6.5-1
- Update foreman_openscap to 0.6.5 (mhulan@redhat.com)

* Tue Feb 21 2017 Dominic Cleal <dominic@cleal.org> 0.6.4-1
- Update foreman_openscap to 0.6.4 (mhulan@redhat.com)

* Wed Oct 19 2016 Dominic Cleal <dominic@cleal.org> 0.6.3-1
- Update foreman openscap to 0.6.3 (oprazak@redhat.com)

* Wed Sep 21 2016 Dominic Cleal <dominic@cleal.org> 0.6.2-1
- Update foreman_openscap to 0.6.2 (ares@users.noreply.github.com)

* Wed Sep 07 2016 Dominic Cleal <dominic@cleal.org> 0.6.1-1
- Update foreman_openscap to 0.6.1 (mhulan@redhat.com)

* Fri Sep 02 2016 Dominic Cleal <dominic@cleal.org> 0.6.0-1
- Update foreman_openscap to 0.6.0 (oprazak@redhat.com)
- Modernise spec file (dominic@cleal.org)

* Thu Jun 02 2016 Dominic Cleal <dominic@cleal.org> 0.5.4-1
- Version bump foreman_openscap 0.5.4 (shlomi@ben-hanna.com)

* Thu Jan 28 2016 Dominic Cleal <dcleal@redhat.com> 0.5.3-1
- foreman_openscap 0.5.3 (shlomi@ben-hanna.com)

* Thu Dec 24 2015 Dominic Cleal <dcleal@redhat.com> 0.5.2-2
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Thu Dec 10 2015 Dominic Cleal <dcleal@redhat.com> 0.5.2-1
- foreman_openscap version 0.5.2 (shlomi@ben-hanna.com)

* Mon Nov 02 2015 Dominic Cleal <dcleal@redhat.com> 0.5.0-1
- foreman_openscap 0.5.0 (shlomi@ben-hanna.com)
- Remove Scaptimony (shlomi@ben-hanna.com)

* Thu Aug 27 2015 Dominic Cleal <dcleal@redhat.com> 0.4.3-2
- Converted to tfm SCL (dcleal@redhat.com)

* Thu Aug 20 2015 Dominic Cleal <dcleal@redhat.com> 0.4.3-1
- Release foreman_openscap 0.4.3 (shlomi@ben-hanna.com)

* Fri Aug 14 2015 Dominic Cleal <dcleal@redhat.com> 0.4.2-1
- foreman_openscap 0.4.2 (shlomi@ben-hanna.com)
- Better branched builds with Foreman version macro (dcleal@redhat.com)

* Tue May 12 2015 Dominic Cleal <dcleal@redhat.com> 0.4.1-1
- foreman_openscap 0.4.1 (shlomi@ben-hanna.com)

* Wed Mar 25 2015 Šimon Lukašík <slukasik@redhat.com> - 0.4.0-1
- new upstream release

* Thu Mar 19 2015 Šimon Lukašík <slukasik@redhat.com> - 0.3.3-1
- new upstream release

* Mon Mar 02 2015 Šimon Lukašík <slukasik@redhat.com> - 0.3.2-1
- new upstream release
- fix FTBFS, missing foreman-plugins dep for build macros (dcleal@redhat.com)

* Thu Feb 12 2015 Šimon Lukašík <slukasik@redhat.com> - 0.3.1-1
- new upstream release

* Wed Jan 28 2015 Šimon Lukašík <slukasik@redhat.com> - 0.3.0-1
- new upstream release

* Fri Jan 23 2015 Marek Hulán <mhulan@redhat.com> - 0.2.1-1
- new upstream release

* Thu Dec 04 2014 Šimon Lukašík <slukasik@redhat.com> - 0.2.0-1
- new upstream release

* Thu Oct 23 2014 Šimon Lukašík <slukasik@redhat.com> - 0.1.0-1
- rebuilt

* Mon Jul 28 2014 Šimon Lukašík <slukasik@redhat.com> - 0.0.1-1
- Initial package
