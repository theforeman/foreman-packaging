# explicitly define, as we build on top of an scl, not inside with scl_package
%{?scl:%global scl_prefix %{scl}-}

%global homedir %{_datarootdir}/%{name}
%global confdir common
#%%global prever .rc2

Name:       katello
Version:    3.7.1
Release:    1%{?prever}%{?dist}
Summary:    A package for managing application life-cycle for Linux systems
BuildArch:  noarch

Group:      Applications/Internet
License:    GPLv2
URL:        https://theforeman.org/plugins/katello
Source0:    katello-service.8.asciidoc
Source1:    katello-debug.sh
Source2:    katello-remove
Source4:    katello-service
Source6:    katello-restore
Source7:    katello-backup
Source8:    katello-service-bash_completion.sh
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

#Pulp Requirements
Requires: pulp-katello
Requires: pulp-docker-plugins
Requires: pulp-puppet-plugins
Requires: pulp-rpm-plugins
Requires: pulp-puppet-tools
Requires: pulp-selinux
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

Requires(post): candlepin >= 2.0
Requires: rubygem-foreman_maintain >= 0.2.2
Requires: candlepin-selinux >= 2.0
Requires: java-openjdk >= 1:1.7.0
Requires: java-openjdk < 1:1.8.0.45
Requires: /usr/bin/psql
Requires: /usr/bin/pg_dump
Requires: /usr/bin/pg_dumpall

%description
Provides a package for managing application life-cycle for Linux systems.

%prep

%build
#man pages
mkdir -p ./manpages
cp %{SOURCE0} ./manpages
cp %{SOURCE13} ./manpages
pushd ./manpages
a2x -d manpage -f manpage katello-service.8.asciidoc
a2x -d manpage -f manpage katello-change-hostname.8.asciidoc
gzip -f9 katello-service.8
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
install -Dp -m0755 %{SOURCE4} %{buildroot}%{_sbindir}/katello-service
install -Dp -m0755 %{SOURCE2} %{buildroot}%{_sbindir}/katello-remove
install -Dp -m0755 %{SOURCE1} %{buildroot}/usr/share/foreman/script/foreman-debug.d/katello-debug.sh

# install tab completion scripts
install -d %{buildroot}/etc/bash_completion.d
install -m 644 %{SOURCE8} %{buildroot}/etc/bash_completion.d/katello-service

# install man page
install -m 644 ./manpages/katello-service.8.gz %{buildroot}/%{_mandir}/man8
install -m 644 ./manpages/katello-change-hostname.8.gz %{buildroot}/%{_mandir}/man8

%clean
%{__rm} -rf ./manpages
%{__rm} -rf %{buildroot}

%files

# ------ Common ------------------

%package common
BuildArch:  noarch
Summary:    Common runtime components of %{name}

Requires:       %{?scl_prefix}rubygem-katello
Requires:       %{?scl_prefix}rubygem-hammer_cli
Requires:       %{?scl_prefix}rubygem-hammer_cli_foreman
Requires:       %{?scl_prefix}rubygem-hammer_cli_katello
Requires:       rubygem-highline
Requires:       %{name}-debug
Requires:       %{name}-service

%description common
Common runtime components of %{name}

%files common
%{_sbindir}/katello-remove
%{_sbindir}/katello-backup
%{_sbindir}/katello-restore
%{_sbindir}/qpid-core-dump
%{_sbindir}/katello-change-hostname
%{_mandir}/man8/katello-change-hostname.8*
%{_datarootdir}/katello/hostname-change.rb
%{_datarootdir}/katello/helper.rb
%config(missingok) %{_sysconfdir}/cron.d/katello

# ------ Debug ----------------
%package debug
Summary: Katello Debug utilities
Group: Applications/System
Requires: bash
Requires: mktemp
Requires: foreman-debug
Requires: findutils
Requires: coreutils
Requires: qpid-tools
Requires: /bin/ps
Requires: rh-mongodb34
Requires: %{?scl_prefix}rubygem-hammer_cli_katello
Requires: %{name}-service

%description debug
Useful utilities for debug info collecting

%files debug
%{_datadir}/foreman/script/foreman-debug.d/katello-debug.sh

%package -n foreman-proxy-content
Summary: Provides a federation of katello services
BuildArch: noarch
Requires: findutils
Requires: rh-mongodb34
Requires: foreman-installer-%{name}
Requires: rubygem-highline
Requires: rubygem-foreman_maintain >= 0.2.2
Obsoletes: katello-capsule

%description -n foreman-proxy-content
Provides a federation of katello services

%files -n foreman-proxy-content
%config(missingok) %{_sysconfdir}/cron.d/katello
%{_sbindir}/katello-backup
%{_sbindir}/katello-restore
%{_sbindir}/katello-change-hostname
%{_sbindir}/katello-remove
%{_datarootdir}/katello/hostname-change.rb
%{_datarootdir}/katello/helper.rb

# ------ Service ----------------
%package service
Summary: Katello Service utilities
Group: Applications/System
Requires: ruby
Requires: /bin/systemctl

%description service
Useful utilities for managing Katello services

%files service
%{_sbindir}/katello-service
%{_mandir}/man8/katello-service.8*
%{_sysconfdir}/bash_completion.d/katello-service

%changelog
* Wed Oct 10 2018 Jonathon Turel <jturel@gmail.com> 3.7.1-1
- Rev for 3.7.1 GA

* Wed Jul 25 2018 Jonathon Turel <jturel@gmail.com> - 3.7.0-4
- Obsolete the python-gofer-qpid obsolete

* Wed Jul 25 2018 Jonathon Turel <jturel@gmail.com> - 3.7.0-3
- Obsolete python-gofer-qpid

* Tue Jul 24 2018 Jonathon Turel <jturel@gmail.com> 3.7.0-2
- remove python-gofer-qpid dep

* Tue Jul 24 2018 Jonathon Turel <jturel@gmail.com> 3.7.0-1
- Rev for 3.7 GA

* Mon Jul 16 2018 Jonathon Turel <jturel@gmail.com> 3.7.0-1.rc2
- Rev for 3.7 RC2

* Wed Jun 20 2018 Chris Roberts <chrobert@redhat> - 3.7.0-3.rc1
- Reverted rh-mongodb34-syspaths due to MongoDB 2.6 dependency error

* Wed Jun 13 2018 Chris Roberts <chrobert@redhat> - 3.7.0-2.rc1
- Added rh-mongodb34-syspaths to deps to bypass scl enable bash

* Mon Jun 11 2018 Jonathon Turel <jturel@gmail.com> 3.7.0-1.rc1
- Rev for 3.7 RC1

* Wed May 23 2018 John Mitsch <jomitsch@redhat.com> - 3.7.0-5.nightly
- Remove katello-backup and katello-restore and require foreman-maintain

* Fri May 11 2018 Chris Roberts <chrobert@redhat.com> - 3.7.0-4.nightly
- removed el6 references and service-wait

* Thu Apr 19 2018 Eric D. Helms <ericdhelms@gmail.com> - 3.7.0-3.nightly
- rebuilt

* Tue Jan 16 2018 Eric D. Helms <ericdhelms@gmail.com> 3.7.0-1.nightly
- new package built with tito
