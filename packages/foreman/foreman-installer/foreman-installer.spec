# set and uncomment all three to set alpha tag
#global alphatag RC1
#global dotalphatag .%{alphatag}
#global dashalphatag -%{alphatag}

Name:       foreman-installer
Epoch:      1
Version:    1.18.0
Release:    0.develop%{?dotalphatag}%{?dist}
Summary:    Puppet-based installer for The Foreman
Group:      Applications/System
License:    GPLv3+ and ASL 2.0
URL:        http://theforeman.org
Source0:    http://downloads.theforeman.org/%{name}/%{name}-%{version}%{?dashalphatag}.tar.bz2

BuildArch:  noarch

Requires:   curl
Requires:   %{?scl_prefix}puppet-agent >= 1.9.0
Requires:   %{?scl_prefix}rubygem-kafo >= 1.0.5
Requires:   foreman-selinux
Requires:   %{?scl_prefix_ruby}ruby(release)
Requires:   %{?scl_prefix}rubygem-highline

BuildRequires: asciidoc
BuildRequires: rubygem(rake)
BuildRequires: %{?scl_prefix}puppet-agent >= 1.9.0
BuildRequires: %{?scl_prefix}rubygem-kafo >= 1.0.5
BuildRequires: puppet-agent-puppet-strings >= 0.99
BuildRequires: puppet-agent-puppet-strings < 2
BuildRequires: puppet-agent-rgen

%description
Complete installer for The Foreman life-cycle management system based on Puppet.

%prep
%setup -q -n %{name}-%{version}%{?dashalphatag}

%build
#replace shebangs for SCL
%if %{?scl:1}%{!?scl:0}
  sed -ri '1sX(/usr/bin/ruby|/usr/bin/env ruby)X/usr/bin/%{?scl:%{scl_prefix}}rubyX' bin/foreman-installer
%endif
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

%files
%defattr(-,root,root,-)
%doc README.* LICENSE
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/custom-hiera.yaml
%dir %{_sysconfdir}/%{name}/scenarios.d
%{_sysconfdir}/%{name}/scenarios.d/foreman.migrations
%config %attr(600, root, root) %{_sysconfdir}/%{name}/scenarios.d/foreman.yaml
%config(noreplace) %attr(600, root, root) %{_sysconfdir}/%{name}/scenarios.d/foreman-answers.yaml
%config(noreplace) %{_sysconfdir}/%{name}/scenarios.d/foreman-migrations-applied
%{_sbindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man8

%changelog
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
