# explicitly define, as we build on top of an scl, not inside with scl_package
%{?scl:%global scl_prefix %{scl}-}

%global homedir %{_datarootdir}/%{name}
%global confdir common

Name:       katello
Version:    3.4.0
Release:    1.nightly%{?dist}
Summary:    A package for managing application life-cycle for Linux systems
BuildArch:  noarch

Group:      Applications/Internet
License:    GPLv2
URL:        http://www.katello.org
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
Requires: mongodb >= 2.4
Requires: mongodb-server >= 2.4
Requires: cyrus-sasl-plain
Requires: python-crane
Requires: python-gofer-qpid
Requires: qpid-cpp-server-linearstore
Requires: qpid-cpp-client-devel
Requires: qpid-dispatch-router
Requires: createrepo >= 0.9.9-18%{?dist}
Requires: squid
Requires: mod_xsendfile

Requires(post): candlepin
Requires: candlepin-selinux
Requires: java-openjdk >= 1:1.7.0
Requires: java-openjdk < 1:1.8.0.45
Requires: lsof
Requires: postgresql
Requires: postgresql-server

%description
Provides a package for managing application life-cycle for Linux systems.

%prep

%build
#man pages
a2x -d manpage -f manpage %{SOURCE0}
gzip -f9 %{_sourcedir}/katello-service.8

%install
mkdir -p %{buildroot}/%{_mandir}/man8

#copy cron scripts to be scheduled
install -d -m0755 %{buildroot}%{_sysconfdir}/cron.weekly
install -m 755 %{SOURCE3} %{buildroot}%{_sysconfdir}/cron.weekly/katello-remove-orphans
install -m 755 %{SOURCE10} %{buildroot}%{_sysconfdir}/cron.weekly/katello-clean-empty-puppet-environments

# install important scripts
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sbindir}
install -Dp -m0755 %{SOURCE11} %{buildroot}%{_bindir}/katello-change-hostname
install -Dp -m0755 %{SOURCE9} %{buildroot}%{_bindir}/qpid-core-dump
install -Dp -m0755 %{SOURCE7} %{buildroot}%{_bindir}/katello-backup
install -Dp -m0755 %{SOURCE6} %{buildroot}%{_bindir}/katello-restore
install -Dp -m0755 %{SOURCE4} %{buildroot}%{_bindir}/katello-service
install -Dp -m0755 %{SOURCE5} %{buildroot}%{_sbindir}/service-wait
install -Dp -m0755 %{SOURCE2} %{buildroot}%{_bindir}/katello-remove
install -Dp -m0755 %{SOURCE1} %{buildroot}/usr/share/foreman/script/foreman-debug.d/katello-debug.sh

# install tab completion scripts
install -d %{buildroot}/etc/bash_completion.d
install -m 644 %{SOURCE8} %{buildroot}/etc/bash_completion.d/katello-service

# install man page
install -m 644 %{_sourcedir}/katello-service.8.gz %{buildroot}/%{_mandir}/man8

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
Requires:       %{?scl_prefix}rubygem-hammer_cli_import
Requires:       %{name}-debug
Requires:       %{name}-service

%description common
Common runtime components of %{name}

%files common
%{_bindir}/katello-remove
%{_bindir}/katello-backup
%{_bindir}/katello-restore
%{_bindir}/qpid-core-dump
%{_bindir}/katello-change-hostname
%config(missingok) %{_sysconfdir}/cron.weekly/katello-clean-empty-puppet-environments
%config(missingok) %{_sysconfdir}/cron.weekly/katello-remove-orphans

# ------ Debug ----------------
%package debug
Summary: Katello Debug utilities
Group: Applications/System
Requires: foreman-debug

%description debug
Useful utilities for debug info collecting

%files debug
%{_datadir}/foreman/script/foreman-debug.d/katello-debug.sh

%package -n foreman-proxy-content
Summary: Provides a federation of katello services
BuildArch: noarch
Requires: findutils
Requires: foreman-installer-%{name}
Obsoletes: katello-capsule

%description -n foreman-proxy-content
Provides a federation of katello services

%files -n foreman-proxy-content
%config(missingok) %{_sysconfdir}/cron.weekly/katello-clean-empty-puppet-environments

# ------ Service ----------------
%package service
Summary: Katello Service utilities
Group: Applications/System

# service-wait dependency
Requires:       wget
Requires:       curl
Requires:       ruby

%description service
Useful utilities for managing Katello services

%files service
%{_sbindir}/service-wait
%{_bindir}/katello-service
%{_mandir}/man8/katello-service.8*
%{_sysconfdir}/bash_completion.d/katello-service

%changelog
* Wed Dec 14 2016 Eric D Helms <ericdhelms@gmail.com> 3.3.0-2.nightly
- refs #17567 - enable use of katello-remove for Foreman proxies (#324)
  (cfouant@redhat.com)
- fixes #17621 - python-semantic_version rpm name (cfouant@redhat.com)
- Fixes #17114 - foreman-debug counts size instead lines (#297)
  (pmoravec@redhat.com)
- fixes #17174 - fixes restore failure if missing pulp database
  (cfouant@redhat.com)
- Fixes #17047 - Redirect cron to /dev/null (#311) (chrobert@redhat.com)
- Fixes #16927 - Dir.exist? isnt available on el6 (ruby 1.8)
  (seanokeeffe797@gmail.com)
- fixes #16825 - verifies valid backup exists before attempting to restore
  (#303) (cfouant@redhat.com)
- Fixes #16251 - Add katello-service disable/enable options
  (seanokeeffe797@gmail.com)
- fixes #16746 - creates subdirectory for backups (#299) (cfouant@redhat.com)
- fixes #16795 - fixes katello-restore syntax failure (#301)
  (cfouant@redhat.com)
- fixes #16732 - gzips archive after services turned back on (#298)
  (cfouant@redhat.com)
- Fixes #16586 - restart gofer with katello-service (#291)
  (chrobert@redhat.com)
- refs #16523 - fix error in find command (#285) (stephen@bitbin.de)
- fixes #16523 - support puppet 4 environments in clean up script (#284)
  (stephen@bitbin.de)
- Katello version bump to 3.3.0 (jomitsch@redhat.com)

* Wed Sep 07 2016 Eric D Helms <ericdhelms@gmail.com> 3.2.0-2.nightly
- fixes #16373 - include rex services in katello-service (#275)
  (stephen@bitbin.de)
- Fixes #16028 - Ignoring proxy when pinging services (#267)
  (daviddavis@users.noreply.github.com)
- Refs #15845 - add installer dep to katello-capsule (jsherril@redhat.com)
- Fixes #15823 - Do not send mail on cron error (#257) (chrobert@redhat.com)
- Fixes #15845 - add cronjob to clean puppet envs (jsherril@redhat.com)
- fixes #15454 - Changes online pulp backup to fully online backup (#240)
  (cfouant@redhat.com)
- Fixes #15484 - Handle pulp_streamer and squid in katello-service
  (daviddavis@redhat.com)
- bumping pkgs for nightly 3.2 (jsherril@redhat.com)
- fixes #14858 - removes gutterball (#213) (cfouant@redhat.com)
- Fixes #15146 - service-wait now correctly handles tomcat (#229)
  (parthaa@gmail.com)
- Fixes #14125 - Updating katello-remove cleanup (#189) (chrobert@redhat.com)
- Have katello-backup report on times (#204) (jcpunk@gmail.com)
- Fixes #15051 - Update katello-remove with help message (#221)
  (chrobert@redhat.com)
- Fix error with Katello-restore script `pulp_data' (narbutas.tadas@gmail.com)
- Fix error with Katello-restore script `pulp_data' (narbutas.tadas@gmail.com)

* Thu May 12 2016 Eric D Helms <ericdhelms@gmail.com> 3.1.0-3.nightly
- fixes #15010 - fix katello-service man page (#218) (stephen@bitbin.de)
- Fixes #14881 - Add in /etc/qpid-dispatch/qdrouterd.conf for files which are
  collected (#215) (bryan.kearney@gmail.com)
- fixes #14784 - fix katello-backup syntax error (narbutas.tadas@gmail.com)
- Fixes #14605 - clean temp files after foreman-debug (#202) (lzap@redhat.com)
- Fixes #14608 - avoid collection of squid with sosreport (#203)
  (lzap@redhat.com)
- Fixes #13363 - Adding additional qpid debug statements to foreman-debug
  (mmccune@redhat.com)
- fixes #14161 - adds online backup for pulp database, BZ170292
  (cfouant@redhat.com)
- fixes #13121 - Allows for incremental backups, BZ1254413 (cfouant@redhat.com)

* Fri Mar 18 2016 Eric D Helms <ericdhelms@gmail.com> 3.1.0-2.nightly
- fixes #13300 - allows backing up without pulp (cfouant@redhat.com)
- Fixes #14105 - fixes backup/restore after moving to foreman-installer,
  BZ1316567 (cfouant@redhat.com)
- Fixes #13199 - Remove pulp-nodes-parent as a requirement
  (jomitsch@redhat.com)
- fixes #13907 - adds squid logs to katello-debug (cfouant@redhat.com)

* Tue Feb 23 2016 Eric D Helms <ericdhelms@gmail.com> 3.1.0-1.nightly
- Bump master to 3.1.0 (ericdhelms@gmail.com)
- Fixes #10163 - Converted katello installer into scenario based installer
  (martin.bacovsky@gmail.com)
- Cleanup requires across katello and installer (ericdhelms@gmail.com)
- Fixes #13450 - Adding packages for lazy sync (paji@redhat.com)

* Thu Feb 04 2016 Justin Sherrill <jsherril@redhat.com> 2.5.0-4.nightly
- drop requirement of candlepin-tomcat (jsherril@redhat.com)

* Thu Jan 21 2016 Eric D Helms <ericdhelms@gmail.com> 2.5.0-3.nightly
- Remove bootdisk and discovery since they aren't Rails 4 compatible
  (ericdhelms@gmail.com)
- Fixes #12792 Katello backup missing puppet certs (seanokeeffe797@gmail.com)
- Refs #10291 - Remove elasticsearch from completion script
  (seanokeeffe797@gmail.com)
- Fixes #12782 Updating katello-backup (chrobert@redhat.com)

* Wed Dec 09 2015 Eric D. Helms <ericdhelms@gmail.com> 2.5.0-2.nightly
- Fixes #12741: Move pulp/candlepin requires to metapackage
  (ericdhelms@gmail.com)
- Fixes #12678 - Add qpid-stat -q/-u to foreman-debug (pmoravec@redhat.com)
- do not compress pulp data -- RPMs are already compressed (egolov@redhat.com)

* Thu Nov 19 2015 Eric D. Helms <ericdhelms@gmail.com> 2.5.0-1.nightly
- Fixes #10291 - removes elasticsearch (cfouant@redhat.com)
- Added bash completion support for katello-service
  (stack@localhost.localdomain)
- updating nightly to 2.5 (jsherril@redhat.com)
- fixes #11826 - update katello-service man page (stbenjam@redhat.com)
- Fixes #12181 - Restart katello services in right order (aruzicka@redhat.com)
- Fixes #12137 - Stops katello services in right order (aruzicka@redhat.com)
- fixes #11568 - adds help scripts to recovery methods (cfouant@redhat.com)

* Thu Sep 03 2015 Eric D. Helms <ericdhelms@gmail.com> 2.4.0-6.nightly
- fixes #11648 - katello-service : add --only option (bbuckingham@redhat.com)
- fixes #11648 - katello-service: update to start/stop postgresql
  (bbuckingham@redhat.com)

* Tue Sep 01 2015 Eric D. Helms <ericdhelms@gmail.com> 2.4.0-5.nightly
- Stop building katello-sam RPM (ericdhelms@gmail.com)

* Fri Aug 28 2015 Eric D. Helms <ericdhelms@gmail.com> 2.4.0-4.nightly
- Update katello for TFM (ericdhelms@gmail.com)
- fixes #11353 - make wait_for_url more reliable (stbenjam@redhat.com)
- fixes #11249 - return `katello list` command (stbenjam@redhat.com)
- fixes #10960 - Adds backup and restore scripts, BZ1233443
  (cfouant@redhat.com)

* Mon Aug 03 2015 Eric D. Helms <ericdhelms@gmail.com> 2.4.0-3.nightly
- Update katello dependency on hammer_cli_sam to SCL version
  (ericdhelms@gmail.com)

* Fri Jul 31 2015 Eric D. Helms <ericdhelms@gmail.com> 2.4.0-2.nightly
- Update katello requirements for SCL'd hammer packages. (ericdhelms@gmail.com)
- fixes #11261 - wait a little after starting httpd (stbenjam@redhat.com)

* Wed Jul 29 2015 Eric D. Helms <ericdhelms@gmail.com> 2.4.0-1.nightly
- new package built with tito

* Tue Feb 24 2015 Eric D. Helms <ericdhelms@gmail.com> 2.3.0-1
- Update katello to 2.3.0 (ericdhelms@gmail.com)
- Fixed #9530 - installer logs are collected again by debug script
  (lzap+git@redhat.com)
- katello-remove typo 'permanetly' -> 'permanently' (elobatocs@gmail.com)
- Merge pull request #4970 from lzap/debug-capsule-split-8710
  (jlsherrill@gmail.com)
- Refs #8710 - created katello-debug sub-package (lzap+git@redhat.com)
- Refs #9200: Discovery does not work with Foreman 1.8 currently.
  (ericdhelms@gmail.com)
- Merge pull request #4923 from mccun934/20150109-1447 (mmccune@gmail.com)
- refs 8213 - split out katello package into modular sub-packages
  (mmccune@redhat.com)
- Fixes #9079 - Add /var/lib/mongodb to the foreman-debug collection
  (bkearney@redhat.com)
- Fixes #8858: Collect candlepin logs on RHEL7 (bkearney@redhat.com)

* Fri Dec 19 2014 David Davis <daviddavis@redhat.com> 2.2.0-1
- Automatic commit of package [rubygem-katello] minor release [2.2.0-1].
  (daviddavis@redhat.com)
- Fixes #6543 - updt index on cp event bz1115602 (inecas@redhat.com)

* Fri Sep 12 2014 Justin Sherrill <jsherril@redhat.com> 2.1.0-1
- bumping to katello version to 2.1 (jsherril@redhat.com)

* Fri Sep 12 2014 Justin Sherrill <jsherril@redhat.com> 2.0.0-0
- fixes #7084 - add rubygem-hammer_cli_import dep (jmontleo@redhat.com)
- Fixes #6297 - delayed jobs is dead, long live foreman-tasks
  (inecas@redhat.com)
- Fixes #7071/BZ1125391: add installer and pulp configs to katello-debug.
  (walden@redhat.com)
- Fixes #6967: Add the correct location of mongo, and collect all log files
  (bkearney@redhat.com)
- Fixes #6682 : Add a warning message if the user tries to run katello-debug.sh
  directly (bkearney@redhat.com)
- Fixes #5805: Update qpidd.conf location and grab Pulp messages in debug.
  (ericdhelms@gmail.com)
- Fixes #6245 : Add mongo and postgres logs to katello debug
  (bkearney@redhat.com)
- Fixes 6048: The spec file was not building due to the new katello-debug
  changes (bkearney@redhat.com)
- Fixes 6041: Convert katello-debug to be an extension of foreman-debug
  (bkearney@redhat.com)
- fixes #5862 - adding pulp 2.4 services to katello-service
  (jsherril@redhat.com)
- Merge pull request #3980 from iNecas/reposets-rework (inecas@redhat.com)
- Fixes #5164 - fix rpm builds (inecas@redhat.com)
- Fixes #4826 - rework reposets to not create repositories on repo set enable
  (inecas@redhat.com)
- Merge pull request #3975 from mccun934/20140409-2045 (mmccune@gmail.com)
- fixes #5164 - adding katello_remove.sh script (mmccune@redhat.com)
- fixes #4991 - adding a few foreman plugins to the default installation
  (jsherril@redhat.com)
- Fixes #4690 - Updating directory in katello deployed scripts
  (daviddavis@redhat.com)
- fixes #4744 - updating copyright to 2014 (jsherril@redhat.com)
- Merge remote-tracking branch 'origin/master' into dynflow (inecas@redhat.com)
- rename hammer_cli package for katelli support (jmontleo@redhat.com)
- Merge pull request #3609 from mccun934/requires-update9 (mmccune@gmail.com)
- remove foreman and thumbslug services now that they are no longer used
  (mmccune@redhat.com)
- Update katello-jobs to include dynflow executor (inecas@redhat.com)
- adding CLI requires so installs of katello pull in the CLI
  (mmccune@redhat.com)
- Merge pull request #3592 from mccun934/specfile-fixes3 (mmccune@gmail.com)
- remove unused calls to the defunct 'katello' service (mmccune@redhat.com)
- adding requires on the rubygem (mmccune@redhat.com)
- Spec: Removing node-installer requires and adding back katello-installer
  requires to katello RPM. (ericdhelms@gmail.com)
- removing old files from katello spec file (jsherril@redhat.com)
- removing katello's service calls and uneeded cruft

* Sat Jan 11 2014 Justin Sherrill <jsherril@redhat.com> 1.5.0-14
- adding util-linux to requires and removing f18 builds (jsherril@redhat.com)

* Sat Jan 11 2014 Justin Sherrill <jsherril@redhat.com> 1.5.0-13
- fixing requires placement in katello spec file (jsherril@redhat.com)

* Sat Jan 11 2014 Justin Sherrill <jsherril@redhat.com> 1.5.0-12
- new package built with tito

* Fri Jan 10 2014 Mike McCune <mmccune@redhat.com> 1.5.0-11
- resurrect the old katello specfile for non-ruby configs and scripts
  (mmccune@redhat.com)

* Fri Jan 10 2014 Mike McCune <mmccune@redhat.com> 1.5.0-10
- initial revision of resurrected katello package
