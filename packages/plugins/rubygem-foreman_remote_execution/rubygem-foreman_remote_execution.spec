# This package contains macros that provide functionality relating to
# Software Collections. These macros are not used in default
# Fedora builds, and should not be blindly copied or enabled.
# Specifically, the "scl" macro must not be defined in official Fedora
# builds. For more information, see:
# http://docs.fedoraproject.org/en-US/Fedora_Contributor_Documentation
# /1/html/Software_Collections_Guide/index.html

%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_remote_execution
%global foreman_min_version 1.24.0

Summary:    Plugin that brings remote execution capabilities to Foreman
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    2.0.6
Release:    1%{?foremandist}%{?dist}
Group:      Applications/System
License:    GPLv3
URL:        https://github.com/theforeman/foreman_remote_execution
Source0:    https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires:   foreman >= 1.24.0

BuildRequires: systemd

# start specfile generated dependencies
BuildArch: noarch
Requires: foreman >= %{foreman_min_version}
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(deface)
Requires: %{?scl_prefix}rubygem(dynflow) >= 1.0.1
Requires: %{?scl_prefix}rubygem(dynflow) < 2.0.0
Requires: %{?scl_prefix}rubygem(foreman_remote_execution_core)
Requires: %{?scl_prefix}rubygem(foreman-tasks) >= 0.15.1
Requires: %{?scl_prefix}rubygem(foreman-tasks) < 1.0.0
BuildRequires: foreman-assets >= %{foreman_min_version}
BuildRequires: foreman-plugin >= %{foreman_min_version}
BuildRequires: %{?scl_prefix}rubygem(deface)
BuildRequires: %{?scl_prefix}rubygem(dynflow) >= 1.0.1
BuildRequires: %{?scl_prefix}rubygem(dynflow) < 2.0.0
BuildRequires: %{?scl_prefix}rubygem(foreman_remote_execution_core)
BuildRequires: %{?scl_prefix}rubygem(foreman-tasks) >= 0.15.1
BuildRequires: %{?scl_prefix}rubygem(foreman-tasks) < 1.0.0
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

# start package.json devDependencies BuildRequires
BuildRequires: %{?scl_prefix}npm(babel-plugin-lodash) >= 3.3.2
BuildRequires: %{?scl_prefix}npm(babel-plugin-lodash) < 4.0.0
BuildRequires: %{?scl_prefix}npm(babel-plugin-transform-class-properties) >= 6.24.1
BuildRequires: %{?scl_prefix}npm(babel-plugin-transform-class-properties) < 7.0.0
BuildRequires: %{?scl_prefix}npm(babel-plugin-transform-object-assign) >= 6.22.0
BuildRequires: %{?scl_prefix}npm(babel-plugin-transform-object-assign) < 7.0.0
BuildRequires: %{?scl_prefix}npm(babel-plugin-transform-object-rest-spread) >= 6.26.0
BuildRequires: %{?scl_prefix}npm(babel-plugin-transform-object-rest-spread) < 7.0.0
BuildRequires: %{?scl_prefix}npm(babel-preset-env) >= 1.6.0
BuildRequires: %{?scl_prefix}npm(babel-preset-env) < 2.0.0
BuildRequires: %{?scl_prefix}npm(babel-preset-react) >= 6.24.1
BuildRequires: %{?scl_prefix}npm(babel-preset-react) < 7.0.0
# end package.json devDependencies BuildRequires

# start package.json dependencies BuildRequires
BuildRequires: %{?scl_prefix}npm(@theforeman/vendor) >= 1.4.0
BuildRequires: %{?scl_prefix}npm(@theforeman/vendor) < 2.0.0
# end package.json dependencies BuildRequires

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-remote_execution
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
A plugin bringing remote execution to the Foreman, completing the config
management functionality with remote management functionality

%package cockpit
BuildArch:  noarch
Requires:   cockpit
Requires(post): systemd-units
Requires(preun): systemd-units
Summary:    Cockpit integration using remote execution connection

%description cockpit
This package contains files related to Cockpit, mainly foreman-cockpit service
and corresponding configuration files.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
mkdir -p %{buildroot}%{_root_sbindir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/
rm %{buildroot}%{gem_instdir}/.babelrc

%{foreman_bundlerd_file}
%foreman_precompile_plugin -a -s

ln -sv %{gem_instdir}/extra/cockpit/foreman-cockpit-session %{buildroot}%{_root_sbindir}/foreman-cockpit-session
install -Dp -m0644 %{buildroot}%{gem_instdir}/extra/cockpit/foreman-cockpit.service %{buildroot}%{_unitdir}/foreman-cockpit.service
install -Dp -m0644 %{buildroot}%{gem_instdir}/extra/cockpit/cockpit.conf.example %{buildroot}%{_root_sysconfdir}/foreman/cockpit/cockpit.conf
install -Dp -m0644 %{buildroot}%{gem_instdir}/extra/cockpit/settings.yml.example %{buildroot}%{_root_sysconfdir}/foreman/cockpit/foreman-cockpit-session.yml

%posttrans
%{foreman_db_migrate}
%{foreman_db_seed}
%{foreman_apipie_cache}
%{foreman_restart}
exit 0

%post cockpit
%systemd_post foreman-cockpit.service

%preun cockpit
%systemd_preun foreman-cockpit.service

%postun cockpit
%systemd_postun_with_restart foreman-cockpit.service

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/%{gem_name}.gemspec
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/package.json
%exclude %{gem_instdir}/webpack
%{gem_instdir}/app
%{gem_instdir}/config
%{gem_instdir}/db
%{gem_instdir}/extra
%{gem_instdir}/locale
%{gem_instdir}/lib
%{gem_instdir}/public
%{gem_spec}
%{foreman_bundlerd_plugin}
%{foreman_apipie_cache_foreman}
%{foreman_apipie_cache_plugin}
%{foreman_assets_plugin}
%{foreman_webpack_plugin}
%{foreman_webpack_foreman}
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/LICENSE
%exclude %{gem_cache}
%exclude %{gem_instdir}/test

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%files cockpit
%{_root_sbindir}/foreman-cockpit-session
%config(noreplace) %{_root_sysconfdir}/foreman/cockpit/cockpit.conf
%config(noreplace) %{_root_sysconfdir}/foreman/cockpit/foreman-cockpit-session.yml
%{_unitdir}/foreman-cockpit.service

%changelog
* Thu Dec 19 2019 Marek Hulan <mhulan@redhat.com> 2.0.6-1
- Update to 2.0.6

* Fri Nov 29 2019 Adam Ruzicka <aruzicka@redhat.com> 2.0.4-1
- Update to 2.0.4

* Thu Nov 21 2019 Adam Ruzicka <aruzicka@redhat.com> 2.0.3-1
- Update to 2.0.3

* Tue Oct 29 2019 Lukas Zapletal <lzap+rpm@redhat.com> 2.0.2-1
- Update to 2.0.2

* Tue Oct 22 2019 Eric D. Helms <ericdhelms@gmail.com> - 1.8.4-2
- Rebuild for SCL nodejs

* Tue Aug 20 2019 Adam Ruzicka <aruzicka@redhat.com> 1.8.4-1
- Update to 1.8.4

* Sun Aug 18 2019 Ivan Nečas <inecas@redhat.com> 1.8.3-1
- Update to 1.8.3

* Tue Jul 16 2019 Adam Ruzicka <aruzicka@redhat.com> 1.8.2-1
- Update to 1.8.2

* Tue May 21 2019 Ivan Nečas <inecas@redhat.com> 1.8.0-1
- Update to 1.8.0

* Thu May 16 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.7.0-18
- Rebuild rubygem-foreman_remote_execution for webpack

* Wed May 15 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.7.0-17
- Rebuild rubygem-foreman_remote_execution for webpack

* Thu May 09 2019 Marek Hulan - 1.7.0-16
- Rebuild REX for webpack

* Mon May 06 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.7.0-15
- Rebuild rubygem-foreman_remote_execution for webpack

* Thu May 02 2019 Marek Hulan - 1.7.0-14
- Rebuild REX for webpack

* Tue Apr 30 2019 Evgeni Golov - 1.7.0-13
- Rebuild REX for webpack

* Fri Apr 12 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.7.0-12
- Rebuild rubygem-foreman_remote_execution for webpack

* Thu Apr 04 2019 Marek Hulan - 1.7.0-11
- Rebuild REX for webpack

* Thu Mar 28 2019 Evgeni Golov - 1.7.0-10
- Rebuild REX for webpack

* Tue Mar 26 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.7.0-9
- Rebuild rubygem-foreman_remote_execution for webpack

* Mon Mar 11 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.7.0-8
- Rebuild rubygem-foreman_remote_execution for webpack

* Mon Feb 25 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.7.0-7
- Rebuild rubygem-foreman_remote_execution for webpack

* Tue Feb 19 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.7.0-6
- Rebuild rubygem-foreman_remote_execution for webpack

* Tue Feb 12 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.7.0-5
- Rebuild rubygem-foreman_remote_execution for webpack

* Mon Jan 28 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.7.0-4
- Rebuild rubygem-foreman_remote_execution for webpack

* Thu Jan 24 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.7.0-3
- Rebuild rubygem-foreman_remote_execution for webpack

* Fri Jan 18 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.7.0-2
- Rebuild for webpack

* Mon Jan 14 2019 Ivan Nečas <inecas@redhat.com> 1.7.0-1
- Update to 1.7.0

* Wed Jan 09 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.6.7-3
- Rebuild for webpack

* Tue Jan 08 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.6.7-2
- Rebuild for webpack

* Wed Dec 12 2018 Ivan Nečas <inecas@redhat.com> 1.6.7-1
- Update to 1.6.7

* Thu Dec 06 2018 Adam Ruzicka <aruzicka@redhat.com> 1.6.6-1
- Update to 1.6.6

* Wed Nov 28 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.6.5-3
- Rebuild for changed Foreman's vendor.js

* Mon Nov 26 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.6.5-2
- Rebuild for new vendor.js in Foreman

* Thu Nov 22 2018 Ivan Nečas <inecas@redhat.com> 1.6.5-1
- Update to 1.6.5

* Wed Oct 31 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.6.4-2
- Stop removing JS source maps

* Tue Oct 09 2018 Ivan Nečas <inecas@redhat.com> 1.6.4-1
- Update to 1.6.4

* Wed Sep 12 2018 Ivan Nečas <inecas@redhat.com> 1.6.3-1
- Update to 1.6.3

* Mon Sep 10 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.6.1-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Tue Aug 14 2018 Adam Ruzicka <aruzicka@redhat.com> 1.6.1-1
- Update to 1.6.1

* Tue Aug 14 2018 Adam Ruzicka <aruzicka@redhat.com> 1.5.5-1
- Update to 1.5.5

* Thu Jul 12 2018 Ivan Nečas <inecas@redhat.com> 1.5.4-1
- Update to 1.5.4

* Wed Jun 27 2018 Ondrej Prazak <oprazak@redhat.com> 1.5.3-2
- Plugin rebuild

* Thu Jun 14 2018 Ivan Nečas <inecas@redhat.com> 1.5.3-1
- Update to 1.5.3

* Wed May 16 2018 Ivan Nečas <inecas@redhat.com> 1.5.2-1
- Update to 1.5.2

* Thu Apr 19 2018 Daniel Lobato Garcia <me@daniellobato.me> 1.5.1-1
- Update to 1.5.1

* Thu Apr 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.5.0-1
- Update to 1.5.0

* Wed Mar 14 2018 Adam Ruzicka <aruzicka@redhat.com> 1.4.6-1
- Update foreman_remote_execution to 1.4.6 (aruzicka@redhat.com.com)

* Fri Feb 02 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.4.5-1
- Update foreman_remote_execution to 1.4.5 (mhulan@redhat.com)

* Mon Jan 22 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.4.2-1
- drop doc directory (aruzicka@redhat.com)
- Update rubygem-foreman_remote_execution to 1.4.2 (aruzicka@redhat.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Wed Jul 26 2017 Eric D. Helms <ericdhelms@gmail.com> 1.3.3-1
- Bump foreman_remote_execution to 1.3.3 (inecas@redhat.com)

* Mon Jul 17 2017 Eric D. Helms <ericdhelms@gmail.com> 1.3.2-1
- Update foreman_remote_execution to 1.3.2 (inecas@redhat.com)

* Wed May 31 2017 Dominic Cleal <dominic@cleal.org> 1.3.1-1
- Update foreman_remote_execution to 1.3.1 (inecas@redhat.com)

* Tue Apr 11 2017 Dominic Cleal <dominic@cleal.org> 1.3.0-1
- Update foreman_remote_execution to 1.3.0 (aruzicka@redhat.com)

* Fri Jan 27 2017 Dominic Cleal <dominic@cleal.org> 1.2.2-1
- Update foreman_remote_execution to 1.2.2 (inecas@redhat.com)

* Tue Sep 20 2016 Dominic Cleal <dominic@cleal.org> 1.2.1-1
- Update foreman_remote_execution to 1.2.1 (inecas@redhat.com)

* Tue Aug 23 2016 Dominic Cleal <dominic@cleal.org> 1.1.0-1
- Update foreman_remote_execution to 1.1.0 (inecas@redhat.com)

* Tue Jul 19 2016 Dominic Cleal <dominic@cleal.org> 1.0.0-1
- Release foreman_remote_execution 1.0 (stephen@redhat.com)

* Wed May 04 2016 Dominic Cleal <dominic@cleal.org> 0.3.2-2
- Use gem_install macro (dominic@cleal.org)

* Thu Apr 28 2016 Dominic Cleal <dominic@cleal.org> 0.3.2-1
- Release foreman_remote_execution 0.3.2 (RPM) (stephen@redhat.com)

* Wed Feb 17 2016 Dominic Cleal <dominic@cleal.org> 0.3.0-1
- Release foreman_remote_execution 0.3.0 (stbenjam@redhat.com)

* Fri Feb 12 2016 Dominic Cleal <dcleal@redhat.com> 0.2.3-1
- Release foreman_remote_execution 0.2.3 (stbenjam@redhat.com)

* Mon Jan 25 2016 Dominic Cleal <dcleal@redhat.com> 0.2.2-1
- Release foreman_remote_execution 0.2.2 (stbenjam@redhat.com)

* Mon Jan 25 2016 Dominic Cleal <dcleal@redhat.com> 0.2.1-1
- Release foreman_remote_execution 0.2.1 (stbenjam@redhat.com)
- Update dependencies to ror SCL (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Fri Nov 13 2015 Dominic Cleal <dcleal@redhat.com> 0.1.1-1
- Update foreman_remote_execution to 0.1.1 (stbenjam@redhat.com)

* Mon Oct 12 2015 Dominic Cleal <dcleal@redhat.com> 0.0.10-1
- Update foreman_remote_execution to 0.0.10 (inecas@redhat.com)

* Tue Oct 06 2015 Dominic Cleal <dcleal@redhat.com> 0.0.7-1
- Release foreman_remote_execution 0.0.7 (stbenjam@redhat.com)

* Mon Sep 14 2015 Dominic Cleal <dcleal@redhat.com> 0.0.6-1
- Release foreman_remote_execution 0.0.6 (stbenjam@redhat.com)

* Wed Sep 02 2015 Dominic Cleal <dcleal@redhat.com> 0.0.5-1
- Release Remote Execution Plugins 0.0.5 (stbenjam@redhat.com)

* Thu Aug 27 2015 Dominic Cleal <dcleal@redhat.com> 0.0.4-1
- Release foreman_remote_execution 0.0.4 (stbenjam@redhat.com)

* Thu Aug 27 2015 Dominic Cleal <dcleal@redhat.com> 0.0.3-2
- Converted to tfm SCL (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 0.0.3-1
- Release foreman_remote_execution 0.0.3 (stbenjam@redhat.com)

* Tue Aug 18 2015 Stephen Benjamin <stephen@redhat.com> 0.0.2-1
- Initial release of 0.0.2
