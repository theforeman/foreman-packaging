%if "%{?scl}" == "ruby193"
    %global scl_prefix %{scl}-
    %global scl_ruby /usr/bin/ruby193-ruby
%else
    %global scl_ruby /usr/bin/ruby
%endif

# set and uncomment all three to set alpha tag
#global alphatag RC2
#global dotalphatag .%{alphatag}
#global dashalphatag -%{alphatag}

Name:       foreman-installer
Epoch:      1
Version:    1.7.0
Release:    1%{?dotalphatag}%{?dist}
Summary:    Puppet-based installer for The Foreman
Group:      Applications/System
License:    GPLv3+ and ASL 2.0
URL:        http://theforeman.org
Source0:    http://downloads.theforeman.org/%{name}/%{name}-%{version}%{?dashalphatag}.tar.bz2

BuildArch:  noarch

Requires:   curl
Requires:   %{?scl_prefix}puppet >= 2.7.0
Requires:   %{?scl_prefix}rubygem-kafo >= 0.6.5
Requires:   %{?scl_prefix}rubygem-apipie-bindings >= 0.0.6
Requires:   foreman-selinux

%if "%{?scl}" == "ruby193" || (0%{?rhel} == 6 && "%{?scl}" == "")
Requires:   %{?scl_prefix}ruby(abi)
%else
Requires:   %{?scl_prefix}ruby(release)
%endif
Requires:   %{?scl_prefix}rubygem-highline

BuildRequires: asciidoc
BuildRequires: rubygem(rake)
BuildRequires: %{?scl_prefix}puppet >= 2.7.0
BuildRequires: %{?scl_prefix}rubygem-kafo

%description
Complete installer for The Foreman life-cycle management system based on Puppet.

%prep
%setup -q -n %{name}-%{version}%{?dashalphatag}

%build
#replace shebangs for SCL
%if %{?scl:1}%{!?scl:0}
  sed -ri '1sX(/usr/bin/ruby|/usr/bin/env ruby)X%{scl_ruby}X' bin/foreman-installer
%endif
rake build \
  VERSION=%{version} \
  PREFIX=%{_prefix} \
  SBINDIR=%{_sbindir} \
  SYSCONFDIR=%{_sysconfdir} \
  --trace

%install
rake install \
  PREFIX=%{buildroot}%{_prefix} \
  SBINDIR=%{buildroot}%{_sbindir} \
  SYSCONFDIR=%{buildroot}%{_sysconfdir} \
  --trace

%files
%defattr(-,root,root,-)
%doc README.* LICENSE
%config %attr(600, root, root) %{_sysconfdir}/foreman/%{name}.yaml
%config(noreplace) %attr(600, root, root) %{_sysconfdir}/foreman/%{name}-answers.yaml
%{_sbindir}/foreman-installer
%{_datadir}/%{name}
%{_mandir}/man8

%changelog
* Tue Dec 02 2014 Dominic Cleal <dcleal@redhat.com> 1.7.0-1
- Release 1.7.0

* Tue Nov 25 2014 Dominic Cleal <dcleal@redhat.com> 1.7.0-0.2.RC2
- Release 1.7.0-RC2

* Tue Nov 11 2014 Dominic Cleal <dcleal@redhat.com> 1.7.0-0.1.RC1
- Release 1.7.0-RC1

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
