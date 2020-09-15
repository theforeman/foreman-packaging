# explicitly define, as we build on top of an scl, not inside with scl_package
%{?scl:%global scl_prefix %{scl}-}

%global homedir %{_datarootdir}/%{name}
%global confdir common
%global release 1

Name:       katello
Version:    3.16.0
Release:    %{?prerelease:0.}%{release}%{?prerelease}%{?dist}
Summary:    A package for managing application life-cycle for Linux systems
BuildArch:  noarch

Group:      Applications/Internet
License:    GPLv2
URL:        https://theforeman.org/plugins/katello
Source1:    katello-debug.sh
Source6:    katello-restore
Source7:    katello-backup
Source9:    qpid-core-dump
Source11:   katello-change-hostname
Source13:   katello-change-hostname.8.asciidoc
Source16:   hostname-change.rb
Source17:   helper.rb
Source18:   katello.cron

BuildRequires: asciidoc
BuildRequires: util-linux

Requires: %{name}-common = %{version}-%{release}

Requires: foreman-installer-%{name}

Requires: %{?scl_prefix}rubygem-katello
Requires: %{?scl_prefix}rubygem-hammer_cli
Requires: %{?scl_prefix}rubygem-hammer_cli_foreman
Requires: %{?scl_prefix}rubygem-hammer_cli_katello

#Pulp Requirements
%if 0%{?rhel} == 7
Requires: pulp-katello
Requires: pulp-docker-plugins
Requires: pulp-puppet-plugins
Requires: pulp-rpm-plugins
Requires: pulp-puppet-tools
Requires: pulp-server
Requires: python-pulp-streamer
Requires: rh-mongodb34
Requires: cyrus-sasl-plain
Requires: python-crane
Requires: qpid-cpp-server-linearstore
Requires: qpid-cpp-client-devel
Requires: qpid-dispatch-router
Requires: createrepo >= 0.9.9-18%{?dist}
Requires: squid
Requires: mod_xsendfile
%endif

Requires: candlepin >= 2.0
Requires: candlepin-selinux >= 2.0
Requires: rubygem-foreman_maintain >= 0.2.2

%description
Provides a package for managing application life-cycle for Linux systems.

%prep

%build
#man pages
mkdir -p ./manpages
cp %{SOURCE13} ./manpages
pushd ./manpages
a2x -d manpage -f manpage katello-change-hostname.8.asciidoc
gzip -f9 katello-change-hostname.8
popd

%install
mkdir -p %{buildroot}/%{_mandir}/man8

#copy cron scripts to be scheduled
install -d -m0755 %{buildroot}%{_sysconfdir}/cron.d
install -m 644 %{SOURCE18} %{buildroot}%{_sysconfdir}/cron.d/katello

# symlink script libraries
mkdir -p %{buildroot}%{_datarootdir}/katello
install -m 644 %{SOURCE16} %{buildroot}%{_datarootdir}/katello/hostname-change.rb
install -m 644 %{SOURCE17} %{buildroot}%{_datarootdir}/katello/helper.rb

# install important scripts
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sbindir}
install -Dp -m0755 %{SOURCE11} %{buildroot}%{_sbindir}/katello-change-hostname
install -Dp -m0755 %{SOURCE9} %{buildroot}%{_sbindir}/qpid-core-dump
install -Dp -m0755 %{SOURCE7} %{buildroot}%{_sbindir}/katello-backup
install -Dp -m0755 %{SOURCE6} %{buildroot}%{_sbindir}/katello-restore
install -Dp -m0755 %{SOURCE1} %{buildroot}/usr/share/foreman/script/foreman-debug.d/katello-debug.sh

# install tab completion scripts
install -d %{buildroot}/etc/bash_completion.d

# install man page
install -m 644 ./manpages/katello-change-hostname.8.gz %{buildroot}/%{_mandir}/man8

%clean
%{__rm} -rf ./manpages
%{__rm} -rf %{buildroot}

%files
%config(missingok) %{_sysconfdir}/cron.d/katello

# ------ Common ------------------

%package common
BuildArch:  noarch
Summary:    Common runtime components of %{name}

Requires:       rubygem-highline
Requires:       %{name}-debug

#Pulp Requirements
%if 0%{?rhel} == 7
Requires: pulp-selinux
%endif

%description common
Common runtime components of %{name}

%files common
%{_sbindir}/katello-backup
%{_sbindir}/katello-restore
%if 0%{?rhel} == 7
%{_sbindir}/qpid-core-dump
%else
%exclude %{_sbindir}/qpid-core-dump
%endif
%{_sbindir}/katello-change-hostname
%{_mandir}/man8/katello-change-hostname.8*
%{_datarootdir}/katello/hostname-change.rb
%{_datarootdir}/katello/helper.rb

# ------ Debug ----------------
%package debug
Summary: Katello Debug utilities
Group: Applications/System
Requires: bash
Requires: mktemp
Requires: foreman-debug
Requires: findutils
Requires: coreutils
Requires: /bin/ps
%if 0%{?rhel} == 7
Requires: qpid-tools
Requires: rh-mongodb34
%endif

%description debug
Useful utilities for debug info collecting

%files debug
%{_datadir}/foreman/script/foreman-debug.d/katello-debug.sh

%package -n foreman-proxy-content
Summary: Provides a federation of katello services
BuildArch: noarch
Requires: findutils
%if 0%{?rhel} == 7
Requires: rh-mongodb34
%endif
Requires: foreman-installer-%{name}
Requires: rubygem-foreman_maintain >= 0.2.2
Requires: %{name}-common = %{version}-%{release}
Obsoletes: katello-capsule

%description -n foreman-proxy-content
Provides a federation of katello services

%files -n foreman-proxy-content
# the files section is empty, but without it no RPM will be generated

%changelog
* Mon Aug 10 2020 Eric D. Helms <ericdhelms@gmail.com> - 3.16.0-1
- Release katello 3.16.0

* Fri Jul 31 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.16.0-0.4.rc5.1
- Release katello 3.16.0

* Tue Jul 21 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.16.0-0.4.rc5
- Release katello 3.16.0

* Tue Jul 14 2020 Eric D. Helms <ericdhelms@gmail.com> - 3.16.0-0.4.rc4.1
- Release katello 3.16.0

* Mon Jul 06 2020 Patrick Creech <pcreech@redhat.com> - 3.16.0-0.4.rc4
- Release katello 3.16.0

* Wed Jun 17 2020 Justin Sherrill <jsherril@redhat.com> 3.16.0-0.4.rc3
- move pulp-selinux requirement to katello-common for smart proxies

* Tue Jun 16 2020 Evgeni Golov - 3.16.0-0.3.rc3
- Release katello 3.16.0

* Tue Jun 02 2020 Eric D. Helms <ericdhelms@gmail.com> - 3.16.0-0.3.rc2
- Release katello 3.16.0

* Wed May 20 2020 Evgeni Golov - 3.16.0-0.3.rc1
- Release katello 3.16.0

* Mon Apr 20 2020 Eric D. Helms <ericdhelms@gmail.com> - 3.16.0-0.3.master
- Only require mongo and pulp on EL7

* Tue Mar 10 2020 Jonathon Turel <jturel@gmail.com> 3.16.0-0.2.master
- Bump release for satellite-change-hostname supporting DNS updates

* Tue Feb 11 2020 James Jeffers <jjeffers@redhat.com> 3.16.0-0.1.master
- Bump to 3.16.0

* Wed Jan 29 2020 Samir Jha <sjha4@ncsu.edu> 3.15.0-0.5.master
- Rename pulp_service_files

* Mon Jan 20 2020 Samir Jha <sjha4@ncsu.edu> - 3.15.0-0.4.master
- Add pulp3 debug info to katello-debug

* Mon Nov 18 2019 Evgeni Golov - 3.15.0-0.3.master
- Unify prerelease macro handling

* Mon Nov 04 2019 Chris Roberts <chrobert@redhat.com> 3.15.0-0.2.master
- Remove CSR reference from hostname-change

* Fri Nov 01 2019 Jonathon Turel <jturel@gmail.com> - 3.15.0-0.1.master
- Bump to 3.15.0

* Tue Oct 29 2019 Eric D. Helms <ericdhelms@gmail.com> - 3.14.0-0.5.master
- Drop katello-service subpackage in favor of foreman-maintain

* Mon Oct 28 2019 Eric D. Helms <ericdhelms@gmail.com> - 3.14.0-0.4.master
- Drop psql requirement on -debug and let foreman-debug handle

* Tue Sep 03 2019 Eric D. Helms <ericdhelms@gmail.com> - 3.14.0-0.3.master
- Drop katello-remove

* Tue Aug 13 2019 Lukas Zapletal <lzap+rpm@redhat.com> - 3.14.0-0.2.master
- Updated katello-debug.sh

* Wed Aug 07 2019 Evgeni Golov - 3.14.0-0.1.master
- Bump version to 3.14

* Sun Jul 21 2019 Jonathon Turel <jturel@gmail.com> 3.13.0-0.4.master
- katello-change-hostname: clean puppet certs
- katello-change-hostname: s/foreman-proxy-content-certs-tar/certs-tar-file/

* Fri Jun 07 2019 Lukas Zapletal <lzap+rpm@redhat.com> 3.13.0-0.3.master
- BZ#1710625 - updated qpidd debug paths

* Tue May 07 2019 Evgeni Golov - 3.13.0-0.2.master
- delete new candlepin keystore paths in katello-change-hostname

* Tue Apr 23 2019 Evgeni Golov <evgeni@golov.de> - 3.13.0-0.1.master
- Bump version to 3.13-master

* Mon Jan 28 2019 Evgeni Golov - 3.12.0-0.3.master
- Refs #25576 - add an empty files section to make foreman-proxy-content build

* Fri Jan 25 2019 Evgeni Golov - 3.12.0-0.2.master
- Refs #25576 - drop the Puppet cleanup cron, this is done inside Pulp now

* Wed Jan 16 2019 Eric D. Helms <ericdhelms@gmail.com> - 3.12.0-0.1.master
- Bump version to 3.12

* Fri Nov 30 2018 Eric D. Helms <ericdhelms@gmail.com> - 3.11.0-1
- Bump version to 3.11

* Mon Nov 19 2018 Evgeni Golov - 3.10.0-6
- Move rubygem-katello and rubygem-hammer* requires to katello

* Tue Nov 13 2018 Evgeni Golov - 3.10.0-5
- Drop rubygem-highline from foreman-proxy-content requires

* Mon Nov 12 2018 Evgeni Golov - 3.10.0-4
- Make katello-common truly common and move specific files to katello itself.
  This allows foreman-proxy-content to depend on k-common.

* Tue Oct 23 2018 sokeeffe <sokeeffe@redhat.com> - 3.10.0-3
- Split out Katello and Smart Proxy Cron

* Mon Oct 22 2018 Chris Roberts <chrobert@redhat.com> - 3.10.0-2
- Change katello-remove to support wildcards and cleanup

* Thu Oct 18 2018 Eric D. Helms <ericdhelms@gmail.com> - 3.10.0-1
- Bump version to 3.10

* Wed Oct 10 2018 Eric D. Helms <ericdhelms@gmail.com> - 3.9.0-11
- Cleanup spec requires

* Tue Oct 09 2018 Eric D. Helms <ericdhelms@gmail.com> - 3.9.0-10
- Drop java requirement

* Tue Sep 11 2018 Eric D. Helms <ericdhelms@gmail.com> - 3.9.0-9
- Drop hammer requirement from katello-debug

* Mon Sep 03 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 3.9.0-8
- Use foreman-maintain instead of katello-service in debug

* Sun Sep 02 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 3.9.0-7
- Use foreman-maintain instead of katello-service in debug

* Mon Jul 30 2018 John Mitsch <jomitsch@redhat.com> - 3.9.0-6
- k-c-h Check hostname is not current hostname

* Wed Jul 25 2018 Jonathon Turel <jturel@gmail.com> - 3.9.0-5
- Obsolete the python-gofer-qpid obsolete

* Wed Jul 25 2018 Jonathon Turel <jturel@gmail.com> - 3.9.0-4
- Obsolete python-gofer-qpid

* Tue Jul 24 2018 Eric D. Helms <ericdhelms@gmail.com> - 3.9.0-3
- Add prerelease macro support

* Thu Jul 19 2018 Chris Roberts <chrobert@redhat.com> - 3.9.0-2.nightly
- Updated katello-debug to remove qpid resource mgr command

* Wed Jul 18 2018 Eric D. Helms <ericdhelms@gmail.com> 3.9.0-1.nightly
- Bump to 3.9

* Wed Jun 27 2018 Eric D. Helms <ericdhelms@gmail.com> - 3.8.0-4.nightly
- rebuilt

* Wed Jun 20 2018 Chris Roberts <chrobert@redhat.com> - 3.8.0-3.nightly
- Reverted rh-mongodb34-syspaths due to MongoDB 2.6 dependency error

* Mon Jun 04 2018 John Mitsch <jomitsch@redhat.com> - 3.8.0-2.nightly
- Redirect katello-service to foreman-maintain

* Sun Jun 03 2018 Chris Roberts <chrobert@redhat.com> - 3.7.0-6.nightly
- Added rh-mongodb34-syspaths to deps to bypass scl enable bash

* Wed May 23 2018 John Mitsch <jomitsch@redhat.com> - 3.7.0-5.nightly
- Remove katello-backup and katello-restore and require foreman-maintain

* Fri May 11 2018 Chris Roberts <chrobert@redhat.com> - 3.7.0-4.nightly
- removed el6 references and service-wait

* Thu Apr 19 2018 Eric D. Helms <ericdhelms@gmail.com> - 3.7.0-3.nightly
- rebuilt

* Tue Jan 16 2018 Eric D. Helms <ericdhelms@gmail.com> 3.7.0-1.nightly
- new package built with tito
