%global release 1
%global prereleasesource develop
%global prerelease %{?prereleasesource}

Name:       foreman-installer
Epoch:      1
Version:    3.16.0
Release:    %{?prerelease:0.}%{release}%{?prerelease:.}%{?prerelease}%{?nightly}%{?dist}
Summary:    Puppet-based installer for The Foreman
Group:      Applications/System
License:    GPLv3+ and ASL 2.0
URL:        https://theforeman.org
Source0:    https://downloads.theforeman.org/%{name}/%{name}-%{version}%{?prerelease:-}%{?prerelease}.tar.bz2

BuildArch:  noarch

Requires:   curl
Requires:   hostname
Requires:   puppet-agent >= 7.0.0
Requires:   rubygem(kafo) >= 7.6.0
Requires:   rubygem(kafo) < 8.0.0
Requires:   ruby(release)

BuildRequires: asciidoc
BuildRequires: puppet-agent >= 7.0.0
BuildRequires: rubygem(rake)
BuildRequires: rubygem(kafo) >= 7.6.0
BuildRequires: rubygem(kafo) < 8.0.0
BuildRequires: puppet-agent-puppet-strings >= 1.2.0
BuildRequires: puppet-agent-puppet-strings < 5

%description
Complete installer for The Foreman life-cycle management system based on Puppet.

%package katello
Summary: Katello installer bits
Group: Applications/System
Provides: katello-installer-base < 3.11.0-1
Obsoletes: katello-installer-base < 3.11.0-1

Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: openssl
Requires: katello-certs-tools
Requires: which

# both katello and foreman-proxy-content scenarios require this
# it also makes the package lock feature available on the first run
Requires: foreman-maintain

%description katello
Various scenarios and tools for the Katello ecosystem

%prep
%setup -q -n %{name}-%{version}%{?prerelease:-}%{?prerelease}

%build
rake build \
  VERSION=%{version} \
  LOCALSTATEDIR=%{_localstatedir} \
  PREFIX=%{_prefix} \
  SBINDIR=%{_sbindir} \
  SYSCONFDIR=%{_sysconfdir} \
  --trace

%install
rake install \
  PREFIX=%{buildroot}%{_prefix} \
  LOCALSTATEDIR=%{buildroot}%{_localstatedir} \
  SBINDIR=%{buildroot}%{_sbindir} \
  SYSCONFDIR=%{buildroot}%{_sysconfdir} \
  --trace

%post
foreman-installer --scenario foreman --migrations-only > /dev/null

%post katello
foreman-installer --scenario foreman-proxy-content --migrations-only > /dev/null
foreman-installer --scenario katello --migrations-only > /dev/null

%files
%defattr(-,root,root,-)
%doc README.*
%license LICENSE
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/custom-hiera.yaml
%dir %{_sysconfdir}/%{name}/scenarios.d
%{_sysconfdir}/%{name}/scenarios.d/foreman.migrations
%config(noreplace) %attr(600, root, root) %{_sysconfdir}/%{name}/scenarios.d/foreman.yaml
%config(noreplace) %attr(600, root, root) %{_sysconfdir}/%{name}/scenarios.d/foreman-answers.yaml
%config(noreplace) %{_sysconfdir}/%{name}/scenarios.d/foreman-migrations-applied
%{_sbindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man8

# katello files
%exclude %{_datadir}/%{name}/config/foreman-proxy-content*
%exclude %{_datadir}/%{name}/config/katello*
%exclude %{_datadir}/%{name}/katello-certs
%exclude %{_datadir}/%{name}/parser_cache/foreman-proxy-certs.yaml
%exclude %{_datadir}/%{name}/parser_cache/foreman-proxy-content.yaml
%exclude %{_datadir}/%{name}/parser_cache/katello.yaml

%files katello
# common
%{_sbindir}/katello-certs-check

# foreman-proxy-content scenario
%{_datadir}/%{name}/config/foreman-proxy-content*
%{_datadir}/%{name}/parser_cache/foreman-proxy-content.yaml
%{_sysconfdir}/%{name}/scenarios.d/foreman-proxy-content.migrations
%config(noreplace) %attr(600, root, root) %{_sysconfdir}/%{name}/scenarios.d/foreman-proxy-content.yaml
%config(noreplace) %attr(600, root, root) %{_sysconfdir}/%{name}/scenarios.d/foreman-proxy-content-answers.yaml
%config(noreplace) %{_sysconfdir}/%{name}/scenarios.d/foreman-proxy-content-migrations-applied

# katello scenario
%{_datadir}/%{name}/config/katello*
%{_datadir}/%{name}/parser_cache/katello.yaml
%{_sysconfdir}/%{name}/scenarios.d/katello.migrations
%config(noreplace) %attr(600, root, root) %{_sysconfdir}/%{name}/scenarios.d/katello.yaml
%config(noreplace) %attr(600, root, root) %{_sysconfdir}/%{name}/scenarios.d/katello-answers.yaml
%config(noreplace) %{_sysconfdir}/%{name}/scenarios.d/katello-migrations-applied

# foreman-proxy-certs-generate
%{_datadir}/%{name}/katello-certs
%{_datadir}/%{name}/parser_cache/foreman-proxy-certs.yaml
%{_sbindir}/foreman-proxy-certs-generate

%changelog
* Mon May 19 2025 Ondřej Gajdušek <ogajduse@redhat.com> - 1:3.16.0-0.1.develop
- Bump version to 3.16-develop

* Tue Feb 18 2025 Patrick Creech <pcreech@redhat.com> - 1:3.15.0-0.1.develop
- Bump version to 3.15-develop

* Wed Nov 06 2024 Patrick Creech <pcreech@redhat.com> - 1:3.14.0-0.1.develop
- Bump version to 3.14-develop

* Thu Oct 24 2024 Evgeni Golov - 1:3.13.0-0.2.develop
- Require kafo >= 7.6

* Tue Aug 20 2024 Patrick Creech <pcreech@redhat.com> - 1:3.13.0-0.1.develop
- Bump version to 3.13-develop

* Thu Jul 18 2024 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1:3.12.0-0.2.develop
- katello: depend on foreman-maintain

* Wed May 22 2024 Zach Huntington-Meath <zhunting@redhat.com> - 1:3.12.0-0.1.develop
- Bump version to 3.12-develop

* Tue Feb 20 2024 Patrick Creech <pcreech@redhat.com> - 1:3.11.0-0.1.develop
- Bump version to 3.11-develop

* Thu Jan 11 2024 Patrick Creech <pcreech@redhat.com> - 1:3.10.0-0.4.develop
- Remove pretrans segment

* Wed Nov 29 2023 Zach Huntington-Meath <zhunting@redhat.com> - 1:3.10.0-0.3.develop
- Bump version to 3.10-develop

* Wed Nov 15 2023 Evgeni Golov - 1:3.9.0-0.3.develop
- Require kafo >= 7.3.0

* Mon Oct 02 2023 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1:3.9.0-0.2.develop
- Require at least Kafo 7.2 to show failed resources

* Wed Aug 23 2023 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1:3.9.0-0.1.develop
- Bump version to 3.9-develop

* Tue May 23 2023 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1:3.8.0-0.1.develop
- Bump version to 3.8-develop

* Fri May 05 2023 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1:3.7.0-0.4.develop
- Widen allowed dependencies

* Thu May 04 2023 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1:3.7.0-0.3.develop
- Drop SCL macros
- Bump Puppet minimum version to 7.0.0

* Tue Mar 21 2023 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1:3.7.0-0.2.develop
- Correct Puppet version lower bound

* Wed Feb 22 2023 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1:3.7.0-0.1.develop
- Bump version to 3.7-develop

* Tue Nov 08 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1:3.6.0-0.1.develop
- Bump version to 3.6-develop

* Wed Aug 10 2022 Patrick Creech <pcreech@redhat.com> - 1:3.5.0-0.1.develop
- Bump version to 3.5-develop

* Thu Aug 04 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1:3.4.0-0.3.develop
- Drop katello subdirectory from files

* Thu Jun 02 2022 Evgeni Golov - 1:3.4.0-0.2.develop
- bump kafo dependency for UTF-8 fix

* Tue May 10 2022 Odilon Sousa <osousa@redhat.com> - 1:3.4.0-0.1.develop
- Bump version to 3.4-develop

* Thu Feb 17 2022 Evgeni Golov - 1:3.3.0-0.2.develop
- require hostname explicitly

* Fri Feb 11 2022 Zach Huntington-Meath <zhunting@redhat.com> - 1:3.3.0-0.1.develop
- Bump version to 3.3-develop

* Fri Nov 12 2021 Odilon Sousa <osousa@redhat.com> - 1:3.2.0-0.1.develop
- Bump version to 3.2-develop

* Thu Aug 05 2021 Patrick Creech <pcreech@redhat.com> - 1:3.1.0-0.1.develop
- Bump version to 3.1-develop

* Thu Jul 22 2021 Tomer Brisker <tbrisker@gmail.com> - 1:3.0.0-0.1.develop
- Bump version to 3.0-develop

* Wed May 19 2021 Eric D. Helms <ericdhelms@gmail.com> - 1:2.6.0-0.3.develop
- Bump puppet-agent requires to 6.15.0

* Mon May 10 2021 Eric D. Helms <ericdhelms@gmail.com> - 1:2.6.0-0.2.develop
- Use Kafo 6.4+

* Tue May 04 2021 Zach Huntington-Meath <zhunting@redhat.com> - 1:2.6.0-0.1.develop
- Bump version to 2.6-develop

* Wed Apr 07 2021 Eric D. Helms <ericdhelms@gmail.com> - 1:2.5.0-0.4.develop
- Do not fail if rhel macro is undefined

* Fri Mar 05 2021 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1:2.5.0-0.3.develop
- Require Puppet with DNF module support (#32003)

* Mon Feb 15 2021 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1:2.5.0-0.2.develop
- Drop puppet/selinux workaround

* Tue Feb 02 2021 Evgeni Golov - 1:2.5.0-0.1.develop
- Bump version to 2.5-develop

* Mon Nov 02 2020 Patrick Creech <pcreech@redhat.com> - 1:2.4.0-0.1.develop
- Bump version to 2.4-develop

* Wed Oct 28 2020 Eric D. Helms <ericdhelms@gmail.com> - 1:2.3.0-0.3.develop
- Require kafo 6.0.0 or greater

* Wed Aug 26 2020 William Bradford Clark <wclark@redhat.com> - 1:2.3.0-0.2.develop
- Require kafo 5.1

* Tue Aug 11 2020 Eric D. Helms <ericdhelms@gmail.com> - 1:2.3.0-0.1.develop
- Bump version to 2.3-develop

* Fri Aug 07 2020 Eric D. Helms <ericdhelms@gmail.com> - 1:2.2.0-0.6.develop
- Require kafo 5.Y

* Tue Jul 28 2020 Eric D. Helms <ericdhelms@gmail.com> - 1:2.2.0-0.5.develop
- Drop requires on selinux packages, allow installer code to handle

* Thu Jul 02 2020 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1:2.2.0-0.4.develop
- Drop foreman-maintain dependency

* Wed May 13 2020 Eric D. Helms <ericdhelms@gmail.com> - 1:2.2.0-0.3.develop
- Bump version to 2.2-develop

* Wed Apr 08 2020 Eric D. Helms <ericdhelms@gmail.com> - 1:2.1.0-0.3.develop
- Build for EL8

* Wed Apr 01 2020 Eric D. Helms <ericdhelms@gmail.com> - 1:2.1.0-0.2.develop
- Build foreman-installer for SCL

* Thu Feb 13 2020 Tomer Brisker <tbrisker@gmail.com> - 1:2.1.0-0.1.develop
- Bump version to 2.1-develop

* Mon Jan 13 2020 Eric D. Helms <ericdhelms@gmail.com> - 1:2.0.0-0.2.develop
- Add requires on foreman-maintain

* Mon Jan 06 2020 Tomer Brisker <tbrisker@gmail.com> - 1:2.0.0-0.1.develop
- Bump version to 2.0-develop

* Mon Nov 18 2019 Evgeni Golov - 1:1.25.0-0.2.develop
- Unify prerelease macro handling

* Wed Oct 30 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1:1.25.0-0.1.develop
- Bump version to 1.25-develop

* Fri Oct 18 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1:1.24.0-0.4.develop
- Update package dependencies

* Thu Sep 12 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1:1.24.0-0.3.develop
- Add which as a dependency since it's used in a hook

* Fri Aug 23 2019 Evgeni Golov - 1:1.24.0-0.2.develop
- don't move katello migrations when they point to a symlink

* Tue Jul 30 2019 Evgeni Golov - 1:1.24.0-0.1.develop
- Bump version to 1.24-develop

* Tue May 21 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1:1.23.0-0.2.develop
- Require at least Puppet 5.5.10 (#26844)

* Tue Apr 23 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1:1.23.0-0.1.develop
- Bump version to 1.23-develop

* Fri Mar 08 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1:1.22.0-0.3.develop
- Update to Kafo 3 (#26282)
- Require Puppet >= 5.5.8 (#26339)
- Require puppet-agent-puppet-strings >= 1.2.0

* Fri Feb 22 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1:1.22.0-0.2.develop
- Remove katello-service dependency (#26111)

* Wed Jan 16 2019 Evgeni Golov <evgeni@golov.de> - 1:1.22.0-0.1.develop
- Bump to 1.22

* Wed Dec 12 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1:1.21.0-0.3.develop
- Add Katello installer subpackage

* Wed Oct 24 2018 Adam Price <komidore64@gmail.com> - 1:1.21.0-0.2.develop
- add nightly macro

* Wed Oct 17 2018 Eric D. Helms <ericdhelms@gmail.com> - 1:1.21.0-0.1.develop
- Bump version to 1.21 and reset release

* Wed Jul 25 2018 Eric D. Helms <ericdhelms@gmail.com> - 1:1.20.0-0.1.develop
- Add prerelease macro

* Tue Jul 17 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1:1.20.0-0.develop
- Bump version to 1.20-develop

* Thu May 31 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1:1.19.0-0.develop
- Bump version to 1.19-develop

* Mon Aug 28 2017 Daniel Lobato Garcia <me@daniellobato.me> - 1.17.0-0.develop
- Bump version to 1.17-develop

* Wed Mar 29 2017 Eric D Helms <ericdhelms@gmail.com> - 1.16.0-0.develop
- Bump version to 1.16-develop

* Tue Dec 06 2016 Dominic Cleal <dominic@cleal.org> - 1.15.0-0.develop
- Bump version to 1.15-develop

* Wed Sep 07 2016 Dominic Cleal <dominic@cleal.org> - 1.14.0-0.develop
- Bump version to 1.14-develop

* Tue May 31 2016 Dominic Cleal <dominic@cleal.org> - 1.13.0-0.develop
- Bump version to 1.13-develop

* Fri Feb 19 2016 Dominic Cleal <dominic@cleal.org> - 1.12.0-0.develop
- Bump version to 1.12-develop

* Wed Oct 07 2015 Dominic Cleal <dcleal@redhat.com> - 1.11.0-0.develop
- Bump version to 1.11-develop

* Fri Jun 26 2015 Dominic Cleal <dcleal@redhat.com> - 1.10.0-0.develop
- Bump version to 1.10-develop

* Tue Mar 03 2015 Dominic Cleal <dcleal@redhat.com> - 1.9.0-0.develop
- Bump version to 1.9-develop

* Tue Oct 28 2014 Dominic Cleal <dcleal@redhat.com> - 1.8.0-0.develop
- Bump version to 1.8-develop

* Mon Aug 11 2014 Dominic Cleal <dcleal@redhat.com> - 1.7.0-0.develop
- Bump version to 1.7-develop

* Wed Apr 16 2014 Dominic Cleal <dcleal@redhat.com> - 1.6.0-0.develop
- Bump to version 1.6-develop

* Thu Jan 16 2014 Dominic Cleal <dcleal@redhat.com> - 1.5.0-0.develop
- Bump to version 1.5-develop

* Thu Nov 21 2013 Dominic Cleal <dcleal@redhat.com> - 1.4.0-0.develop
- Bump and change versioning scheme (#3712)

* Fri Nov 08 2013 Marek Hulan <mhulan[@]redhat.com> - 1.3.9999-4
- upgrade to kafo 0.3.0

* Thu Sep 12 2013 Marek Hulan <mhulan[@]redhat.com> - 1.3.9999-3
- set config flag on configuration files

* Thu Sep 12 2013 Marek Hulan <mhulan[@]redhat.com> - 1.3.9999-2
- config files packaging fix

* Wed Sep 11 2013 Lukas Zapletal <lzap+rpm[@]redhat.com> - 1.3.9999-1
- bump to version 1.3-develop

* Mon Jul 22 2013 Marek Hulan <mhulan[@]redhat.com> - 1.2.9999-3
- new files structure for a installer based on kafo

* Mon Jul 22 2013 Lukas Zapletal <lzap+rpm[@]redhat.com> - 1.2.9999-2
- adding foreman_api as a dependency

* Thu May 23 2013 Lukas Zapletal <lzap+rpm[@]redhat.com> - 1.2.9999-1
- initial version
