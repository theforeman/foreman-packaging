# template: foreman_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}
%{!?_root_sbindir:%global _root_sbindir %{_sbindir}}
%{!?_root_sysconfdir:%global _root_sysconfdir %{_sysconfdir}}

%global gem_name foreman_remote_execution
%global plugin_name remote_execution
%global foreman_min_version 1.24.0

Summary:    Plugin that brings remote execution capabilities to Foreman
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    4.1.0
Release:    2%{?foremandist}%{?dist}
Group:      Applications/Systems
License:    GPLv3
URL:        https://github.com/theforeman/foreman_remote_execution
Source0:    https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires: systemd

# start specfile generated dependencies
Requires: foreman >= %{foreman_min_version}
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(deface)
Requires: %{?scl_prefix}rubygem(dynflow) >= 1.0.2
Requires: %{?scl_prefix}rubygem(dynflow) < 2.0.0
Requires: %{?scl_prefix}rubygem(foreman_remote_execution_core)
Requires: %{?scl_prefix}rubygem(foreman-tasks) >= 0.15.1
BuildRequires: foreman-assets >= %{foreman_min_version}
BuildRequires: foreman-plugin >= %{foreman_min_version}
BuildRequires: %{?scl_prefix}rubygem(deface)
BuildRequires: %{?scl_prefix}rubygem(dynflow) >= 1.0.2
BuildRequires: %{?scl_prefix}rubygem(dynflow) < 2.0.0
BuildRequires: %{?scl_prefix}rubygem(foreman_remote_execution_core)
BuildRequires: %{?scl_prefix}rubygem(foreman-tasks) >= 0.15.1
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

# start package.json devDependencies BuildRequires
BuildRequires: %{?scl_prefix}npm(@babel/core) >= 7.7.0
BuildRequires: %{?scl_prefix}npm(@babel/core) < 8.0.0
BuildRequires: %{?scl_prefix}npm(@theforeman/builder) >= 4.2.1
BuildRequires: %{?scl_prefix}npm(@theforeman/builder) < 5.0.0
# end package.json devDependencies BuildRequires

# start package.json dependencies BuildRequires
# end package.json dependencies BuildRequires

%description
A plugin bringing remote execution to the Foreman, completing the config
management functionality with remote management functionality.

%package cockpit
BuildArch:  noarch
Requires: cockpit
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Requires(post): systemd-units
Requires(preun): systemd-units
Summary:    Cockpit integration using remote execution connection

%description cockpit
This package contains files related to Cockpit, mainly foreman-cockpit service
and corresponding configuration files.

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

%foreman_bundlerd_file
%foreman_precompile_plugin -a -s

mkdir -p %{buildroot}%{_root_sbindir}
ln -sv %{gem_instdir}/extra/cockpit/foreman-cockpit-session %{buildroot}%{_root_sbindir}/foreman-cockpit-session
install -Dp -m0644 %{buildroot}%{gem_instdir}/extra/cockpit/foreman-cockpit.service %{buildroot}%{_unitdir}/foreman-cockpit.service
install -Dp -m0644 %{buildroot}%{gem_instdir}/extra/cockpit/cockpit.conf.example %{buildroot}%{_root_sysconfdir}/foreman/cockpit/cockpit.conf
install -Dp -m0644 %{buildroot}%{gem_instdir}/extra/cockpit/settings.yml.example %{buildroot}%{_root_sysconfdir}/foreman/cockpit/foreman-cockpit-session.yml

%post cockpit
%systemd_post foreman-cockpit.service

%preun cockpit
%systemd_preun foreman-cockpit.service

%postun cockpit
%systemd_postun_with_restart foreman-cockpit.service

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/package.json
%exclude %{gem_instdir}/webpack
%{gem_instdir}/app
%{gem_instdir}/config
%{gem_instdir}/db
%{gem_instdir}/extra
%{gem_libdir}
%{gem_instdir}/locale
%{gem_spec}
%{foreman_bundlerd_plugin}
%{foreman_apipie_cache_foreman}
%{foreman_apipie_cache_plugin}
%{foreman_assets_plugin}
%{foreman_webpack_plugin}
%{foreman_webpack_foreman}
%license %{gem_instdir}/LICENSE
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/foreman_remote_execution.gemspec
%{gem_instdir}/test

%files cockpit
%{_root_sbindir}/foreman-cockpit-session
%config(noreplace) %{_root_sysconfdir}/foreman/cockpit/cockpit.conf
%config(noreplace) %{_root_sysconfdir}/foreman/cockpit/foreman-cockpit-session.yml
%{_unitdir}/foreman-cockpit.service

%changelog
* Thu Nov 12 2020 Evgeni Golov 4.1.0-2
- Let cockpit subpackage depend on exact version of the main package

* Tue Sep 01 2020 Adam Ruzicka <aruzicka@redhat.com> 4.1.0-1
- Update to 4.1.0

* Thu Aug 13 2020 Adam Ruzicka <aruzicka@redhat.com> 4.0.0-1
- Update to 4.0.0

* Thu Aug 13 2020 Adam Ruzicka <aruzicka@redhat.com> 3.3.6-1
- Update to 3.3.6

* Mon Aug 03 2020 Adam Ruzicka <aruzicka@redhat.com> 3.3.5-1
- Update to 3.3.5

* Mon Jul 20 2020 Adam Ruzicka <aruzicka@redhat.com> 3.3.4-1
- Update to 3.3.4

* Tue Jul 14 2020 Adam Ruzicka <aruzicka@redhat.com> 3.3.3-1
- Update to 3.3.3

* Tue Jun 23 2020 Adam Ruzicka <aruzicka@redhat.com> 3.3.2-1
- Update to 3.3.2

* Wed Jun 10 2020 Adam Ruzicka <aruzicka@redhat.com> 3.3.1-1
- Update to 3.3.1

* Mon Jun 1 2020 Adam Ruzicka <aruzicka@redhat.com> 3.3.0-1
- Update to 3.3.0

* Thu May 14 2020 Adam Ruzicka <aruzicka@redhat.com> 3.2.1-1
- Update to 3.2.1

* Thu May 07 2020 Adam Ruzicka <aruzicka@redhat.com> 3.2.0-1
- Update to 3.2.0

* Mon Apr 20 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.1.0-2
- Exclude the debug folder for remote execution

* Thu Apr 09 2020 Adam Ruzicka <aruzicka@redhat.com> 3.1.0-1
- Update to 3.1.0

* Tue Jan 28 2020 Tomer Brisker <tbrisker@gmail.com> - 3.0.3-2
- rebuild for webpack change

* Wed Jan 22 2020 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 3.0.3-1
- Update to 3.0.3
- Update spec to closer match the foreman_plugin template

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
