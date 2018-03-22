# explicitly define, as we build on top of an scl, not inside with scl_package
%{?scl:%global scl_prefix %{scl}-}

%global homedir %{_datarootdir}/%{name}
%global confdir common

Name:       katello
Version:    3.7.0
Release:    3.nightly%{?dist}
Summary:    A package for managing application life-cycle for Linux systems
BuildArch:  noarch

Group:      Applications/Internet
License:    GPLv2
URL:        https://theforeman.org/plugins/katello
Source0:    katello-service.8.asciidoc
Source1:    katello-debug.sh
Source2:    katello-remove
Source3:    katello-remove-orphans
Source4:    katello-service
Source5:    service-wait
Source6:    katello-restore
Source7:    katello-backup
Source8:    katello-service-bash_completion.sh
Source9:    qpid-core-dump
Source10:   katello-clean-empty-puppet-environments
Source11:   katello-change-hostname
Source12:   katello-repository-publish-check
Source13:   katello-change-hostname.8.asciidoc
Source14:   restore.rb
Source15:   backup.rb
Source16:   hostname-change.rb
Source17:   helper.rb

BuildRequires: asciidoc
BuildRequires: util-linux

Requires: %{name}-common = %{version}-%{release}

%if 0%{?rhel} == 6
Requires: redhat-logos >= 60.0.14
%endif
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
Requires: python-gofer-qpid
Requires: qpid-cpp-server-linearstore
Requires: qpid-cpp-client-devel
Requires: qpid-dispatch-router
Requires: createrepo >= 0.9.9-18%{?dist}
Requires: squid
Requires: mod_xsendfile

Requires(post): candlepin >= 2.0
Requires: candlepin-selinux >= 2.0
Requires: java-openjdk >= 1:1.7.0
Requires: java-openjdk < 1:1.8.0.45
Requires: /usr/bin/psql
Requires: /usr/bin/pg_dump
Requires: /usr/bin/pg_dumpall

Obsoletes: mongodb

%description
Provides a package for managing application life-cycle for Linux systems.

%prep

%build
#man pages
a2x -d manpage -f manpage %{SOURCE0}
a2x -d manpage -f manpage %{SOURCE13}
gzip -f9 %{_sourcedir}/katello-service.8
gzip -f9 %{_sourcedir}/katello-change-hostname.8

%install
mkdir -p %{buildroot}/%{_mandir}/man8

#copy cron scripts to be scheduled
install -d -m0755 %{buildroot}%{_sysconfdir}/cron.weekly
install -d -m0755 %{buildroot}%{_sysconfdir}/cron.daily
install -m 755 %{SOURCE3} %{buildroot}%{_sysconfdir}/cron.weekly/katello-remove-orphans
install -m 755 %{SOURCE10} %{buildroot}%{_sysconfdir}/cron.weekly/katello-clean-empty-puppet-environments
install -m 755 %{SOURCE12} %{buildroot}%{_sysconfdir}/cron.daily/katello-repository-publish-check

# symlink script libraries
mkdir -p %{buildroot}%{_datarootdir}/katello
install -m 644 %{SOURCE14} %{buildroot}%{_datarootdir}/katello/restore.rb
install -m 644 %{SOURCE15} %{buildroot}%{_datarootdir}/katello/backup.rb
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
install -Dp -m0755 %{SOURCE5} %{buildroot}%{_sbindir}/service-wait
install -Dp -m0755 %{SOURCE2} %{buildroot}%{_sbindir}/katello-remove
install -Dp -m0755 %{SOURCE1} %{buildroot}/usr/share/foreman/script/foreman-debug.d/katello-debug.sh

# install tab completion scripts
install -d %{buildroot}/etc/bash_completion.d
install -m 644 %{SOURCE8} %{buildroot}/etc/bash_completion.d/katello-service

# install man page
install -m 644 %{_sourcedir}/katello-service.8.gz %{buildroot}/%{_mandir}/man8
install -m 644 %{_sourcedir}/katello-change-hostname.8.gz %{buildroot}/%{_mandir}/man8

%clean
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
%{_datarootdir}/katello/restore.rb
%{_datarootdir}/katello/backup.rb
%{_datarootdir}/katello/hostname-change.rb
%{_datarootdir}/katello/helper.rb
%config(missingok) %{_sysconfdir}/cron.weekly/katello-clean-empty-puppet-environments
%config(missingok) %{_sysconfdir}/cron.weekly/katello-remove-orphans
%config(missingok) %{_sysconfdir}/cron.daily/katello-repository-publish-check

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
Requires: foreman-installer-%{name}
Requires: rubygem-highline
Obsoletes: katello-capsule

%description -n foreman-proxy-content
Provides a federation of katello services

%files -n foreman-proxy-content
%config(missingok) %{_sysconfdir}/cron.weekly/katello-clean-empty-puppet-environments
%{_sbindir}/katello-backup
%{_sbindir}/katello-restore
%{_sbindir}/katello-change-hostname
%{_sbindir}/katello-remove
%{_datarootdir}/katello/restore.rb
%{_datarootdir}/katello/backup.rb
%{_datarootdir}/katello/hostname-change.rb
%{_datarootdir}/katello/helper.rb

# ------ Service ----------------
%package service
Summary: Katello Service utilities
Group: Applications/System

# service-wait dependency
Requires:       curl
Requires:       ruby
Requires:       /usr/sbin/ss
Requires:       /bin/systemctl

%description service
Useful utilities for managing Katello services

%files service
%{_sbindir}/service-wait
%{_sbindir}/katello-service
%{_mandir}/man8/katello-service.8*
%{_sysconfdir}/bash_completion.d/katello-service

%changelog
* Tue Jan 16 2018 Eric D. Helms <ericdhelms@gmail.com> 3.7.0-1.nightly
- new package built with tito

