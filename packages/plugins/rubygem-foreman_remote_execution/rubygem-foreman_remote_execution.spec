# template: foreman_plugin
%global gem_name foreman_remote_execution
%global plugin_name remote_execution
%global foreman_min_version 3.15

Name: rubygem-%{gem_name}
Version: 16.0.4
Release: 2%{?foremandist}%{?dist}
Summary: A plugin bringing remote execution to the Foreman, completing the config management functionality with remote management functionality
License: GPLv3
URL: https://github.com/theforeman/foreman_remote_execution
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: foreman >= %{foreman_min_version}
BuildRequires: foreman-assets >= %{foreman_min_version}
BuildRequires: foreman-plugin >= %{foreman_min_version}
Requires: ruby >= 2.7
Requires: ruby < 4
BuildRequires: ruby >= 2.7
BuildRequires: ruby < 4
BuildRequires: rubygems-devel
BuildRequires: rubygem(deface)
BuildRequires: (rubygem(dynflow) >= 1.0.2 with rubygem(dynflow) < 2.0.0)
BuildRequires: rubygem(foreman-tasks) >= 8.3.0
BuildArch: noarch
Provides: foreman-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

# start package.json devDependencies BuildRequires
BuildRequires: (npm(@babel/core) >= 7.7.0 with npm(@babel/core) < 8.0.0)
BuildRequires: npm(@theforeman/builder) >= 15.0.1
BuildRequires: (npm(graphql) >= 15.5.0 with npm(graphql) < 16.0.0)
BuildRequires: (npm(graphql-tag) >= 2.11.0 with npm(graphql-tag) < 3.0.0)
# end package.json devDependencies BuildRequires

# start package.json dependencies BuildRequires
# end package.json dependencies BuildRequires

%description
A plugin bringing remote execution to the Foreman, completing the config
management functionality with remote management functionality.

%package cockpit
BuildArch: noarch
Requires: cockpit
Requires: %{name} = %{version}-%{release}
Requires(post): systemd-units
Requires(preun): systemd-units
Summary: Cockpit integration using remote execution connection

%description cockpit
This package contains files related to Cockpit, mainly foreman-cockpit service
and corresponding configuration files.

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

%foreman_bundlerd_file
%foreman_precompile_plugin -s

mkdir -p %{buildroot}%{_sbindir}
install -Dp -m0755 %{buildroot}%{gem_instdir}/extra/cockpit/foreman-cockpit-session %{buildroot}%{_sbindir}/foreman-cockpit-session
install -Dp -m0644 %{buildroot}%{gem_instdir}/extra/cockpit/foreman-cockpit.service %{buildroot}%{_unitdir}/foreman-cockpit.service
install -Dp -m0644 %{buildroot}%{gem_instdir}/extra/cockpit/cockpit.conf.example %{buildroot}%{_sysconfdir}/foreman/cockpit/cockpit.conf
install -Dp -m0644 %{buildroot}%{gem_instdir}/extra/cockpit/settings.yml.example %{buildroot}%{_sysconfdir}/foreman/cockpit/foreman-cockpit-session.yml

%post cockpit
%systemd_post foreman-cockpit.service

%preun cockpit
%systemd_preun foreman-cockpit.service

%postun cockpit
%systemd_postun_with_restart foreman-cockpit.service

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE
%{gem_instdir}/app
%{gem_instdir}/config
%{gem_instdir}/db
%exclude %{gem_instdir}/jsconfig.json
%{gem_libdir}
%{gem_instdir}/locale
%exclude %{gem_instdir}/package.json
%exclude %{gem_instdir}/webpack
%exclude %{gem_cache}
%{gem_spec}
%{foreman_bundlerd_plugin}
%{foreman_assets_plugin}
%{foreman_assets_foreman}
%{foreman_webpack_plugin}
%{foreman_webpack_foreman}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%files cockpit
%{_sbindir}/foreman-cockpit-session
%config(noreplace) %{_sysconfdir}/foreman/cockpit/cockpit.conf
%config(noreplace) %{_sysconfdir}/foreman/cockpit/foreman-cockpit-session.yml
%{_unitdir}/foreman-cockpit.service
%exclude %{gem_instdir}/extra/cockpit

%posttrans
%{foreman_plugin_log}

%changelog
* Tue Jul 15 2025 Evgeni Golov - 16.0.4-2
- Rebuild for removal of theforeman/vendor

* Thu Jun 26 2025 Foreman Packaging Automation <packaging@theforeman.org> - 16.0.4-1
- Update to 16.0.4

* Wed May 14 2025 Foreman Packaging Automation <packaging@theforeman.org> - 16.0.3-1
- Update to 16.0.3

* Sun Apr 13 2025 Foreman Packaging Automation <packaging@theforeman.org> - 16.0.2-1
- Update to 16.0.2

* Wed Mar 26 2025 Foreman Packaging Automation <packaging@theforeman.org> - 16.0.1-1
- Update to 16.0.1

* Wed Mar 05 2025 Foreman Packaging Automation <packaging@theforeman.org> - 15.0.2-1
- Update to 15.0.2

* Wed Feb 19 2025 Foreman Packaging Automation <packaging@theforeman.org> - 15.0.1-1
- Update to 15.0.1

* Wed Jan 29 2025 Foreman Packaging Automation <packaging@theforeman.org> - 15.0.0-1
- Update to 15.0.0

* Wed Dec 18 2024 Adam Ruzicka <aruzicka@redhat.com> - 14.1.4-1
- Update to 14.1.4

* Tue Dec 03 2024 Foreman Packaging Automation <packaging@theforeman.org> - 14.1.3-1
- Update to 14.1.3

* Wed Nov 27 2024 Foreman Packaging Automation <packaging@theforeman.org> - 14.1.2-1
- Update to 14.1.2

* Tue Nov 12 2024 Adam Ruzicka <aruzicka@redhat.com> - 14.1.1-1
- Update to 14.1.1

* Wed Nov 06 2024 aruzicka - 14.1.0-1
- Release rubygem-foreman_remote_execution 14.1.0

* Wed Oct 30 2024 Foreman Packaging Automation <packaging@theforeman.org> - 14.0.2-1
- Update to 14.0.2

* Wed Sep 11 2024 Foreman Packaging Automation <packaging@theforeman.org> - 14.0.0-1
- Update to 14.0.0

* Wed Aug 28 2024 Foreman Packaging Automation <packaging@theforeman.org> - 13.2.5-1
- Update to 13.2.5

* Thu Aug 01 2024 Leos Stejskal <lstejska@redhat.com> - 13.2.4-1
- Update to 13.2.4

* Thu Jul 18 2024 Foreman Packaging Automation <packaging@theforeman.org> - 13.2.3-1
- Update to 13.2.3

* Wed Jul 10 2024 Adam Ruzicka <aruzicka@redhat.com> - 13.2.2-1
- Update to 13.2.2

* Thu Jun 20 2024 Adam Ruzicka <aruzicka@redhat.com> - 13.2.1-1
- Update to 13.2.1

* Thu May 30 2024 Adam Ruzicka <aruzicka@redhat.com> - 13.2.0-1
- Update to 13.2.0

* Thu May 23 2024 Adam Ruzicka <aruzicka@redhat.com> - 13.1.1-1
- Update to 13.1.1

* Thu May 16 2024 Adam Ruzicka <aruzicka@redhat.com> - 13.1.0-1
- Release rubygem-foreman_remote_execution 13.1.0

* Tue May 07 2024 Evgeni Golov - 13.0.0-2
- Rebuild for Webpack asset compression

* Tue Mar 12 2024 Adam Ruzicka <aruzicka@redhat.com> - 13.0.0-1
- Update to 13.0.0

* Thu Feb 08 2024 Evgeni Golov - 12.0.5-3
- Move all cockpit related files to cockpit package

* Fri Jan 26 2024 Evgeni Golov - 12.0.5-2
- Rebuild for Webpack 5

* Tue Jan 23 2024 Adam Ruzicka <aruzicka@redhat.com> - 12.0.5-1
- Update to 12.0.5

* Thu Jan 18 2024 Adam Ruzicka <aruzicka@redhat.com> - 12.0.4-1
- Update to 12.0.4

* Thu Jan 04 2024 Adam Ruzicka <aruzicka@redhat.com> 12.0.2-1
- Update to 12.0.2

* Fri Dec 01 2023 Adam Ruzicka <aruzicka@redhat.com> 12.0.0-1
- Update to 12.0.0

* Tue Nov 14 2023 Adam Ruzicka <aruzicka@redhat.com> 11.1.1-1
- Update to 11.1.1

* Sun Oct 29 2023 Foreman Packaging Automation <packaging@theforeman.org> 11.1.0-1
- Update to 11.1.0

* Tue Aug 29 2023 Adam Ruzicka <aruzicka@redhat.com> 11.0.0-1
- Update to 11.0.0

* Wed Aug 16 2023 Adam Ruzicka <aruzicka@redhat.com> 10.0.6-1
- Update to 10.0.6

* Wed Aug 02 2023 Adam Ruzicka <aruzicka@redhat.com> 10.0.5-1
- Update to 10.0.5

* Wed Jul 19 2023 Foreman Packaging Automation <packaging@theforeman.org> 10.0.4-1
- Update to 10.0.4

* Thu Jun 22 2023 Foreman Packaging Automation <packaging@theforeman.org> 10.0.3-1
- Update to 10.0.3

* Mon May 22 2023 Foreman Packaging Automation <packaging@theforeman.org> 10.0.1-1
- Update to 10.0.1

* Thu May 04 2023 Evgeni Golov 9.1.0-2
- regenerate RPM spec from latest template

* Fri Mar 10 2023 Foreman Packaging Automation <packaging@theforeman.org> 9.1.0-1
- Update to 9.1.0

* Sun Jan 01 2023 Foreman Packaging Automation <packaging@theforeman.org> 9.0.1-1
- Update to 9.0.1

* Sun Dec 04 2022 Foreman Packaging Automation <packaging@theforeman.org> 8.1.1-1
- Update to 8.1.1

* Thu Nov 10 2022 Adam Ruzicka <aruzicka@redhat.com> 8.1.0-1
- Update to 8.1.0

* Fri Sep 09 2022 Adam Ruzicka <aruzicka@redhat.com> 8.0.0-2
- Bump dependency on Foreman to >=3.4.0

* Sun Aug 28 2022 Foreman Packaging Automation <packaging@theforeman.org> 8.0.0-1
- Update to 8.0.0

* Wed Aug 24 2022 Evgeni Golov - 7.1.0-2
- Refs #35409 - Include legacy assets in foreman_remote_execution

* Mon Jun 13 2022 Adam Ruzicka <aruzicka@redhat.com> 7.1.0-1
- Update to 7.1.0

* Mon May 16 2022 Adam Ruzicka <aruzicka@redhat.com> 7.0.0-1
- Update to 7.0.0

* Mon May 09 2022 Evgeni Golov - 6.2.0-3
- log plugin installation in posttrans

* Fri Apr 22 2022 Eric D. Helms <ericdhelms@gmail.com> - 6.2.0-2
- Stop generaing apipie cache

* Tue Apr 19 2022 Adam Ruzicka <aruzicka@redhat.com> 6.2.0-1
- Update to 6.2.0

* Thu Mar 31 2022 Adam Ruzicka <aruzicka@redhat.com> 6.1.0-1
- Update to 6.1.0

* Thu Feb 17 2022 Adam Ruzicka <aruzicka@redhat.com> 6.0.0-1
- Update to 6.0.0

* Tue Dec 14 2021 Adam Ruzicka <aruzicka@redhat.com> 5.1.0-1
- Update to 5.1.0

* Fri Dec 03 2021 Adam Ruzicka <aruzicka@redhat.com> 5.0.1-1
- Update to 5.0.1

* Tue Nov 16 2021 Adam Ruzicka <aruzicka@redhat.com> 5.0.0-1
- Update to 5.0.0

* Tue Sep 14 2021 Adam Ruzicka <aruzicka@redhat.com> 4.8.0-1
- Update to 4.8.0

* Tue Aug 03 2021 Adam Ruzicka <aruzicka@redhat.com> 4.7.0-1
- Update to 4.7.0

* Mon Jun 07 2021 Adam Ruzicka <aruzicka@redhat.com> 4.6.0-1
- Update to 4.6.0

* Mon May 31 2021 Adam Ruzicka <aruzicka@redhat.com> 4.5.0-1
- Update to 4.5.0

* Mon May 10 2021 Adam Ruzicka <aruzicka@redhat.com> 4.4.0-1
- Update to 4.4.0

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 4.3.0-2
- Rebuild plugins for Ruby 2.7

* Mon Mar 22 2021 Adam Ruzicka <aruzicka@redhat.com> 4.3.0-1
- Update to 4.3.0

* Wed Jan 13 2021 Adam Ruzicka <aruzicka@redhat.com> 4.2.2-1
- Update to 4.2.2

* Thu Nov 26 2020 Adam Ruzicka <aruzicka@redhat.com> 4.2.1-1
- Update to 4.2.1

* Tue Nov 17 2020 Adam Ruzicka <aruzicka@redhat.com> 4.2.0-1
- Update to 4.2.0

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
