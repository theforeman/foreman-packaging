# template: foreman_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_openscap
%global plugin_name openscap
%global foreman_min_version 1.17.0

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.9.3
Release: 1%{?foremandist}%{?dist}
Summary: Foreman plug-in for displaying OpenSCAP audit reports
Group: Applications/Systems
License: GPLv3
URL: https://github.com/theforeman/foreman_openscap
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: scap-security-guide
# start generated dependencies
Requires: foreman >= %{foreman_min_version}
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(deface) < 2.0
BuildRequires: foreman-assets >= %{foreman_min_version}
BuildRequires: foreman-plugin >= %{foreman_min_version}
BuildRequires: %{?scl_prefix}rubygem(deface) < 2.0
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-%{plugin_name}
# end generated dependencies
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}
Obsoletes: %{?scl_prefix}rubygem(scaptimony) < 0.3.2-3

%description
Foreman plug-in for managing security compliance reports.


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
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

%foreman_bundlerd_file
%foreman_precompile_plugin -a -s

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_instdir}/app
%{gem_instdir}/config
%{gem_instdir}/db
%{gem_libdir}
%{gem_instdir}/locale
%exclude %{gem_cache}
%{gem_spec}
%{foreman_bundlerd_plugin}
%{foreman_apipie_cache_foreman}
%{foreman_apipie_cache_plugin}
%{foreman_assets_plugin}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/test

%posttrans
%{foreman_db_migrate}
%{foreman_db_seed}
%{foreman_apipie_cache}
%{foreman_restart}
exit 0

%changelog
* Tue Jun 12 2018 Eric D. Helms <ericdhelms@gmail.com> 0.9.3-1
- Update foreman_openscap to 0.9.3 (mhulan@redhat.com)

* Thu May 31 2018 Marek Hulan <mhulan@redhat.com> 0.9.3-1
- Update to 0.9.3

* Mon May 28 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 0.9.2-2
- Regenerate spec file based on the current template

* Thu Jan 11 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.9.0-1
- Update foreman_openscap to 0.9.0 (mhulan@redhat.com)

* Thu Jan 04 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.8.4-1
- Updates foreman_openscap to 0.8.4 (mhulan@redhat.com)

* Fri Oct 27 2017 Daniel Lobato Garcia <me@daniellobato.me> 0.8.3-2
- Precompile assets for foreman_openscap in nightlies
  (xprazak2@users.noreply.github.com)

* Tue Oct 24 2017 Daniel Lobato Garcia <me@daniellobato.me> 0.8.3-1
- Update foreman_openscap to 0.8.3 (ares@users.noreply.github.com)

* Wed Sep 27 2017 Daniel Lobato Garcia <me@daniellobato.me> 0.8.2-1
- Update foreman_openscap to 0.8.2 (ares@users.noreply.github.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

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
