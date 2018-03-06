Name: katello-host-tools
Version: 3.1.0
Release: 3%{?dist}
Summary: A set of commands and yum plugins that support a Katello host
Group:   Development/Languages
License: LGPLv2
URL:     https://github.com/Katello/katello-agent
Source0: https://codeload.github.com/Katello/katello-agent/tar.gz/%{version}#/%{name}-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

Requires: subscription-manager
Requires: %{name}-fact-plugin

%if 0%{?fedora} > 18 || 0%{?rhel} > 6
Requires: python-rhsm
Requires: crontabs
%endif

%if 0%{?rhel} == 5
Requires: python-simplejson
%endif

%if 0%{?sles_version}
BuildRequires: python-devel >= 2.6
%else
BuildRequires: python2-devel
%endif
BuildRequires: python-setuptools
BuildRequires: rpm-python

%description
A set of commands and yum plugins that support a Katello host including faster package profile uploading and bound repository reporting.  This is required for errata and package applicability reporting.

%package -n katello-agent
BuildArch:  noarch
Summary:    The Katello Agent
Group:      Development/Languages

Conflicts: pulp-consumer-client

%if 0%{?rhel} == 5
Requires: gofer >= 2.5
%else
Requires: gofer >= 2.7.6
%endif

Requires: python-gofer-proton >= 2.5
Requires: python-pulp-agent-lib >= 2.6
Requires: pulp-rpm-handlers >= 2.6
Requires: subscription-manager
Requires: katello-host-tools

%if 0%{?rhel} == 6
Requires: yum-plugin-security
%endif

%if 0%{?rhel} == 5
Requires: yum-security
%endif

%description -n katello-agent
Provides plugin for gofer, which allows communicating with Katello server
and execute scheduled actions.

%package fact-plugin
BuildArch:  noarch
Summary:    Adds an fqdn fact plugin for subscription-manager
Group:      Development/Languages

Requires:   subscription-manager
Obsoletes:  katello-agent-fact-plugin <= 3.0.0

%description fact-plugin
A subscription-manager plugin to add an additional fact 'network.fqdn' if not present

%package tracer
BuildArch:  noarch
Summary:    Adds Tracer functionality to a client managed by katello-host-tools
Group:      Development/Languages

Requires: katello-host-tools
Requires: python2-tracer >= 0.6.12

%description tracer
Adds Tracer functionality to a client managed by katello-host-tools

%prep
%setup -q -n katello-host-tools-%{version}

%build
pushd src
%{__python} setup.py build
popd

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_sysconfdir}/gofer/plugins
mkdir -p %{buildroot}/%{_prefix}/lib/gofer/plugins

cp etc/gofer/plugins/katelloplugin.conf %{buildroot}/%{_sysconfdir}/gofer/plugins
cp src/katello/agent/katelloplugin.py %{buildroot}/%{_prefix}/lib/gofer/plugins

mkdir -p %{buildroot}/%{_prefix}/lib/yum-plugins
cp src/yum-plugins/package_upload.py %{buildroot}/%{_prefix}/lib/yum-plugins
cp src/yum-plugins/enabled_repos_upload.py %{buildroot}/%{_prefix}/lib/yum-plugins

mkdir -p %{buildroot}/%{_sysconfdir}/yum/pluginconf.d/
cp etc/yum/pluginconf.d/package_upload.conf %{buildroot}/%{_sysconfdir}/yum/pluginconf.d/package_upload.conf
cp etc/yum/pluginconf.d/enabled_repos_upload.conf %{buildroot}/%{_sysconfdir}/yum/pluginconf.d/enabled_repos_upload.conf

mkdir -p %{buildroot}%{_sbindir}
cp bin/katello-package-upload %{buildroot}%{_sbindir}/katello-package-upload
cp bin/katello-enabled-repos-upload %{buildroot}%{_sbindir}/katello-enabled-repos-upload

mkdir -p %{buildroot}%{_sysconfdir}/rhsm/pluginconf.d/
mkdir -p %{buildroot}%{_datadir}/rhsm-plugins/
cp etc/rhsm/pluginconf.d/fqdn.FactsPlugin.conf %{buildroot}%{_sysconfdir}/rhsm/pluginconf.d/fqdn.FactsPlugin.conf
cp src/rhsm-plugins/fqdn.py %{buildroot}%{_datadir}/rhsm-plugins/fqdn.py

# cache directory
mkdir -p %{buildroot}/var/cache/katello-agent/

cp src/yum-plugins/tracer_upload.py %{buildroot}/%{_prefix}/lib/yum-plugins
cp etc/yum/pluginconf.d/tracer_upload.conf %{buildroot}/%{_sysconfdir}/yum/pluginconf.d/tracer_upload.conf
cp bin/katello-tracer-upload %{buildroot}%{_sbindir}/katello-tracer-upload

%if 0%{?fedora} > 18 || 0%{?rhel} > 6
# crontab
mkdir -p %{buildroot}%{_sysconfdir}/cron.d/
cp extra/katello-agent-send.cron %{buildroot}%{_sysconfdir}/cron.d/%{name}
%endif

%clean
rm -rf %{buildroot}

%post -n katello-agent
%if 0%{?fedora} > 18 || 0%{?rhel} > 6
  systemctl enable goferd
  /bin/systemctl start goferd > /dev/null 2>&1 || :
%else
  chkconfig goferd on
  /sbin/service goferd start > /dev/null 2>&1 || :
%endif

touch /tmp/katello-agent-restart
exit 0

%posttrans
katello-package-upload 2> /dev/null
katello-enabled-repos-upload 2> /dev/null
exit 0

%postun -n katello-agent
touch /tmp/katello-agent-restart
exit 0

%files -n katello-agent
%defattr(-,root,root,-)
%config %{_sysconfdir}/gofer/plugins/katelloplugin.conf
%{_prefix}/lib/gofer/plugins/katelloplugin.*

%doc LICENSE

%files
%defattr(-,root,root,-)
%config %{_sysconfdir}/yum/pluginconf.d/package_upload.conf
%config %{_sysconfdir}/yum/pluginconf.d/enabled_repos_upload.conf
/var/cache/katello-agent/
%attr(750, root, root) %{_sbindir}/katello-package-upload
%attr(750, root, root) %{_sbindir}/katello-enabled-repos-upload
%{_prefix}/lib/yum-plugins/package_upload.py*
%{_prefix}/lib/yum-plugins/enabled_repos_upload.py*

%if 0%{?fedora} > 18 || 0%{?rhel} > 6
%config(noreplace) %attr(0644, root, root) %{_sysconfdir}/cron.d/%{name}
%endif

%files fact-plugin
%config %{_sysconfdir}/rhsm/pluginconf.d/fqdn.FactsPlugin.conf
%{_datadir}/rhsm-plugins/fqdn.*

%files tracer
%{_sysconfdir}/yum/pluginconf.d/tracer_upload.conf
%attr(750, root, root) %{_sbindir}/katello-tracer-upload
%{_prefix}/lib/yum-plugins/tracer_upload.py*

%changelog
* Tue Mar 6 2018 Jonathon Turel <jturel@redhat.com> 3.1.0-3
- Fix directory used by setup macro

* Wed Jan 10 2018 Eric D. Helms <ericdhelms@gmail.com> 3.1.0-2
- new package built with tito

* Thu Sep 28 2017 Justin Sherrill <jsherril@redhat.com> 3.1.0-1
- katello-host-tools 3.1.0 (jsherril@redhat.com)

* Mon Aug 28 2017 Eric D. Helms <ericdhelms@gmail.com> 3.0.2-1
- Release katello-host-tools 3.0.2 (ericdhelms@gmail.com)

* Thu Jul 27 2017 Evgeni Golov <egolov@redhat.com> - 3.0.1-1
- use Python2.4 compatible syntax in enabled_repos_upload

* Thu Jun 29 2017 Justin Sherrill <jsherril@redhat.com> 3.0.0-3
- rename base package to katello-host-tools
* Wed Jun 14 2017 Eric D. Helms <ericdhelms@gmail.com> 3.0.0-2
- Make /var/cache/katello-agent available on all OS (ericdhelms@gmail.com)

* Wed Jun 14 2017 Eric D. Helms <ericdhelms@gmail.com> 3.0.0-1
- update katello-agent to include new plugin (jsherril@redhat.com)

* Wed May 24 2017 Justin Sherrill <jsherril@redhat.com> 2.9.1-2
- Fixes #19256 - allow older goferd on el5 (jsherril@redhat.com)
- Fixes #19038 - Start goferd on install (ericdhelms@gmail.com)

* Wed Jan 25 2017 Justin Sherrill <jsherril@redhat.com> 2.9.1-1
- Refs #18174 - Run katello-tracer-upload after reboot
  (seanokeeffe797@gmail.com)

* Mon Jan 23 2017 Justin Sherrill <jsherril@redhat.com> 2.9.0-1
- Fixes #18187 - restarting goferd while being updated by RPM
  (zhunting@redhat.com)

* Fri Jan 20 2017 Justin Sherrill <jsherril@redhat.com> 2.8.0-4
- Fixes #18173 - Dont run katello-tracer-upload during install
  (seanokeeffe797@gmail.com)

* Thu Jan 19 2017 Eric D Helms <ericdhelms@gmail.com> 2.8.0-3
- Fixes #18012 - depend on newer gofer (cduryee@redhat.com)

* Thu Dec 29 2016 Justin Sherrill <jsherril@redhat.com> 2.8.0-2
- fixing tracer version requirement (jsherril@redhat.com)

* Wed Dec 21 2016 Justin Sherrill <jsherril@redhat.com> 2.8.0-1
- Refs #17230 - added tracer support (seanokeeffe797@gmail.com)

* Tue Sep 27 2016 Justin Sherrill <jsherril@redhat.com> 2.7.0-1
- Refs #16134 - add new subpackage for sub-man plugin (jsherril@redhat.com)

* Fri Sep 16 2016 Justin Sherrill <jsherril@redhat.com> 2.6.0-4
- Fixes #16524 - use yum-security for el5 (jsherril@redhat.com)

* Thu Jul 28 2016 Eric D Helms <ericdhelms@gmail.com> 2.6.0-2
- fixes #15366 - add yum-plugin-security dep to rhel5/6 packages (#234)
  (komidore64@gmail.com)

* Wed Jun 22 2016 Justin Sherrill <jsherril@redhat.com> 2.6.0-1
- building katello-agent 2.6.0 (jsherril@redhat.com)

* Mon May 16 2016 Justin Sherrill <jsherril@redhat.com> 2.5.0-3
- Added basic SLES compatibility Tested against SLES 11 SP3
  (darinlively@gmail.com)

* Thu May 12 2016 Darin Lively <darinlively@gmail.com> 2.5.0-3
- Added basic SLES build compatibility

* Thu May 12 2016 Eric D Helms <ericdhelms@gmail.com> 2.5.0-2
- fixes #15012 - run katello-package-upload in %%posttrans (#219)
  (stephen@bitbin.de)

* Thu Mar 17 2016 Eric D Helms <ericdhelms@gmail.com> 2.5.0-1
- Refs #13589 - replace gofer plugin config file (jsherril@redhat.com)
- fixes #14054 - ensure katello-agent service errors don't show during install
  (stbenjam@redhat.com)

* Thu Aug 13 2015 Eric D. Helms <ericdhelms@gmail.com> 2.4.0-3
- Fixes #11083: Prevent katello-agent from being installed with pulp-consumer-
  client (ericdhelms@gmail.com)

* Wed Jul 29 2015 Eric D. Helms <ericdhelms@gmail.com> 2.4.0-2
- new package built with tito

* Mon Jul 06 2015 Stephen Benjamin <stbenjam@redhat.com> 2.4.0-1
- Version buimp to 2.4.0 (stbenjam@redhat.com)
- Fixes #10670 - preffer the katello-default-ca.pem as the client ca cert
  (inecas@redhat.com)
- refs #10224 - adding fedora to releasers (jsherril@redhat.com)
- Adding el5 releaser. (ericdhelms@gmail.com)

* Tue Feb 24 2015 Eric D. Helms <ericdhelms@gmail.com> 2.3.0-1
-

* Tue Feb 24 2015 Eric D. Helms <ericdhelms@gmail.com> 2.2.0-2
- Bumping release to 2.2.0-2 (ericdhelms@gmail.com)
- Using port: 5647 for dispatch router. (jortel@redhat.com)
- registration fixes. (jortel@redhat.com)
- Using proton; consumer registration validated. (jortel@redhat.com)
- gofer 2.x compat. (jortel@redhat.com)
- refs #9403 - get rhsm certificate from rhsm configration
  (stbenjam@redhat.com)
- fixes #9403 - use correct certificate location (stbenjam@redhat.com)

* Tue Feb 24 2015 Eric D. Helms <ericdhelms@gmail.com>
- Using port: 5647 for dispatch router. (jortel@redhat.com)
- registration fixes. (jortel@redhat.com)
- Using proton; consumer registration validated. (jortel@redhat.com)
- gofer 2.x compat. (jortel@redhat.com)
- refs #9403 - get rhsm certificate from rhsm configration
  (stbenjam@redhat.com)
- fixes #9403 - use correct certificate location (stbenjam@redhat.com)

* Tue Feb 24 2015 Eric D. Helms <ericdhelms@gmail.com>
- Using port: 5647 for dispatch router. (jortel@redhat.com)
- registration fixes. (jortel@redhat.com)
- Using proton; consumer registration validated. (jortel@redhat.com)
- gofer 2.x compat. (jortel@redhat.com)
- refs #9403 - get rhsm certificate from rhsm configration
  (stbenjam@redhat.com)
- fixes #9403 - use correct certificate location (stbenjam@redhat.com)

* Fri Dec 19 2014 David Davis <daviddavis@redhat.com> 2.2.0-1
- fixes #7815 - fixing katello-agent for older subscription-managers
  (jsherril@redhat.com)

* Fri Oct 10 2014 Justin Sherrill <jsherril@redhat.com> 2.1.2-1
- fixes #7815 - fixing package upload feature with new sub-man
  (jsherril@redhat.com)

* Wed Sep 24 2014 Eric D. Helms <ericdhelms@gmail.com> 2.1.1-1
- Fixes #7553: Update ConsumerIdentity location. (ericdhelms@gmail.com)

* Fri Sep 12 2014 Justin Sherrill <jsherril@redhat.com> 2.1.0-1
- bumping version to 2.1 (jsherril@redhat.com)

* Fri Sep 12 2014 Justin Sherrill <jsherril@redhat.com> 2.0.0-1
- bumping version to 2.0 (jsherril@redhat.com)
- refs #7330 / BZ 1136393 - %%postun - only restart goferd when it is running
  (bbuckingham@redhat.com)
- fixes #7330 / BZ 1136393 - katello-agent - update %%postun to support systemd
  (bbuckingham@redhat.com)
- refs #5271 - update for el7 builds (jsherril@redhat.com)
- fixes #6103 - updating package profile after every yum action
  (jsherril@redhat.com)
- fixes #5095 - starting goferd by default (jsherril@redhat.com)

* Tue May 20 2014 Justin Sherrill <jsherril@redhat.com> 1.5.3-1
  (jlsherrill@gmail.com)
- Fix agent requirements for pulp 2.4; catch and report errors sending the
  enabled report. (jortel@redhat.com)

* Fri May 16 2014 Justin Sherrill <jsherril@redhat.com> 1.5.2-1
- Ensure EnabledReport filters by basename. (jortel@redhat.com)
- agent requires gofer >= 1.0.10. (jortel@redhat.com)
- add unit tests. (jortel@redhat.com)
- Refit agent to work with gofer 1.0+ and pulp 2.4+. (jortel@redhat.com)

* Fri Oct 11 2013 Partha Aji <paji@redhat.com> 1.5.1-1
- Bumping package versions for 1.5 (paji@redhat.com)

* Fri Oct 11 2013 Partha Aji <paji@redhat.com> 1.4.5-1
- Implement conduit for pulp 2.3 compat (jortel@redhat.com)
- Autobuild f19 packages (paji@redhat.com)

* Wed Jul 31 2013 Partha Aji <paji@redhat.com> 1.4.4-1
- add katello-nightly-fedora19 to tito.props (msuchy@redhat.com)

* Thu Jun 06 2013 Miroslav Suchý <msuchy@redhat.com> 1.4.3-1
- 893596 - sending up baseurl of repos from katello-agent (jsherril@redhat.com)

* Sat Apr 27 2013 Mike McCune <mmccune@redhat.com> 1.4.2-1
- adding rel-eng directory for new location (mmccune@redhat.com)

* Fri Apr 12 2013 Justin Sherrill <jsherril@redhat.com> 1.4.1-1
- version bump to 1.4 (jsherril@redhat.com)

* Fri Apr 12 2013 Justin Sherrill <jsherril@redhat.com> 1.3.2-1
- remove old changelog entries (msuchy@redhat.com)
- 872528 - restart gofer after katello-agent upgrade (msuchy@redhat.com)

* Mon Jan 07 2013 Justin Sherrill <jsherril@redhat.com> 1.3.1-1
- Refit agent for pulp v2. (jortel@redhat.com)

* Fri Oct 12 2012 Lukas Zapletal <lzap+git@redhat.com> 1.1.3-1
-

* Fri Aug 24 2012 Miroslav Suchý <msuchy@redhat.com> 1.1.2-1
- 845643 - consistently use rpm macros (msuchy@redhat.com)

* Thu Aug 23 2012 Mike McCune <mmccune@redhat.com> 1.1.1-1
- buildroot and %%clean section is not needed (msuchy@redhat.com)
- Bumping package versions for 1.1. (msuchy@redhat.com)

* Tue Jul 31 2012 Miroslav Suchý <msuchy@redhat.com> 1.0.6-1
- update copyright years (msuchy@redhat.com)
- point Source0 to fedorahosted.org where tar.gz are stored (msuchy@redhat.com)

* Fri Jul 27 2012 Lukas Zapletal <lzap+git@redhat.com> 1.0.5-1
- macro python_sitelib is not used anywhere, removing
- provide more descriptive description
- put plugins into correct location
- build root is not used since el6 (inclusive)
- point URL to our wiki
- %%defattr is not needed since rpm 4.4

* Wed Jun 27 2012 Lukas Zapletal <lzap+git@redhat.com> 1.0.4-1
- 828533 - changing to proper QPIDD SSL port
