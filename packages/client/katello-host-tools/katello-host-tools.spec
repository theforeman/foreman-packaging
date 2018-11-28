%global dnf_install (0%{?rhel} > 7) || (0%{?fedora} > 26)
%global yum_install ((0%{?rhel} <= 7) && (0%{?rhel} >= 5)) || ((0%{?fedora} < 27) && (0%{?fedora} > 0))
%global zypper_install (0%{?suse_version} > 0)

%global build_tracer (0%{?suse_version} == 0)

%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

%global build_agent (0%{?suse_version} == 0)
%global legacy_agent (0%{?rhel} == 5) || (0%{?rhel} == 6)

%if 0%{?suse_version}
%define dist suse%{?suse_version}
%endif

Name: katello-host-tools
Version: 3.4.0
Release: 1%{?dist}
Summary: A set of commands and yum plugins that support a Katello host
Group:   Development/Languages
License: LGPLv2
URL:     https://github.com/Katello/katello-agent
Source0: https://codeload.github.com/Katello/katello-host-tools/tar.gz/%{version}#/%{name}-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%if 0%{?suse_version} && 0%{?suse_version} < 1200
ExclusiveArch: x86_64
%else
BuildArch: noarch
%endif

Requires: subscription-manager >= 1.23
Requires: %{name}-fact-plugin

%if 0%{?fedora} > 18 || 0%{?rhel} > 6
%if %{dnf_install}
Requires: python3-subscription-manager-rhsm
%else
Requires: python-rhsm
%endif
Requires: crontabs
%endif

%if 0%{?rhel} == 5
Requires: python-simplejson
%endif

%if 0%{?sles_version}
BuildRequires: python-devel >= 2.6
%else
%if %{dnf_install}
BuildRequires: python3-devel
%else
BuildRequires: %{?suse_version:python-devel >= 2.6} %{!?suse_version:python2-devel}
%endif
%endif

BuildRequires: python-setuptools
BuildRequires: rpm-python

%description
A set of commands and yum plugins that support a Katello host including faster package profile uploading and bound repository reporting.  This is required for errata and package applicability reporting.

%if %{build_agent}
%package -n katello-agent
BuildArch:  noarch
Summary:    The Katello Agent
Group:      Development/Languages

Conflicts: pulp-consumer-client

%if %{legacy_agent}
Requires: gofer >= 2.11.5
Requires: gofer < 2.12
Requires: python-pulp-agent-lib >= 2.6
Requires: pulp-rpm-handlers >= 2.6
%else
Requires: gofer >= 2.12.1
Obsoletes: python-pulp-agent-lib < 3.0
Obsoletes: pulp-rpm-handlers < 3.0
Obsoletes: python-pulp-rpm-common < 2.16.4
%endif

%if %{dnf_install}
Requires: python3-gofer-proton
%else
Requires: python-gofer-proton >= 2.5
%endif

Requires: subscription-manager
Requires: katello-host-tools = %{version}-%{release}

%if 0%{?rhel} == 6
Requires: yum-plugin-security
%endif

%if 0%{?rhel} == 5
Requires: yum-security
%endif

%description -n katello-agent
Provides plugin for gofer, which allows communicating with Katello server
and execute scheduled actions.
%endif

%package fact-plugin
BuildArch:  noarch
Summary:    Adds an fqdn fact plugin for subscription-manager
Group:      Development/Languages

Requires:   subscription-manager
Obsoletes:  katello-agent-fact-plugin <= 3.0.0

%description fact-plugin
A subscription-manager plugin to add an additional fact 'network.fqdn' if not present

%if %{build_tracer}
%package tracer
BuildArch:  noarch
Summary:    Adds Tracer functionality to a client managed by katello-host-tools
Group:      Development/Languages

Requires: katello-host-tools
%if %{dnf_install}
Requires: python3-tracer
%else
Requires: python2-tracer >= 0.6.12
%endif

%description tracer
Adds Tracer functionality to a client managed by katello-host-tools
%endif #build tracer

%prep
%setup -q

%build
pushd src
%{__python} setup.py build
popd

%install
rm -rf %{buildroot}

%if %{dnf_install}
%global katello_libdir %{python3_sitelib}/katello
%endif

%if %{yum_install}
%global katello_libdir %{python_sitelib}/katello
%global plugins_dir %{_usr}/lib/yum-plugins
%global plugins_confdir %{_sysconfdir}/yum/pluginconf.d
%endif

%if %{zypper_install}
%global katello_libdir %{python_sitelib}/katello
%global plugins_dir %{_usr}/lib/zypp/plugins/commit/
# Deploy yum plugin config to control reports
%global plugins_confdir %{_sysconfdir}/yum/pluginconf.d
%endif

mkdir -p %{buildroot}%{katello_libdir}
mkdir -p %{buildroot}%{plugins_dir}

cp src/katello/*.py %{buildroot}%{katello_libdir}/

%if %{build_agent}
mkdir -p %{buildroot}%{_sysconfdir}/gofer/plugins
cp etc/gofer/plugins/katello.conf %{buildroot}%{_sysconfdir}/gofer/plugins
cp -R src/katello/agent %{buildroot}%{katello_libdir}/

%if %{legacy_agent}
mv %{buildroot}%{katello_libdir}/agent/goferd/legacy_plugin.py %{buildroot}%{katello_libdir}/agent/goferd/plugin.py
rm -rf %{buildroot}%{katello_libdir}/agent/pulp
%else
rm %{buildroot}%{katello_libdir}/agent/pulp/test.py
rm %{buildroot}%{katello_libdir}/agent/goferd/legacy_plugin.py
%endif
%endif

%if %{yum_install} || %{zypper_install}
mkdir -p %{buildroot}%{plugins_confdir}
cp etc/yum/pluginconf.d/*.conf %{buildroot}%{plugins_confdir}/
%endif

%if %{yum_install}
cp src/yum-plugins/*.py %{buildroot}%{plugins_dir}/
%endif

%if %{zypper_install}
cp src/zypper_plugins/*.py %{buildroot}%{plugins_dir}/
rm %{buildroot}%{plugins_dir}/__init__.py
%endif

# executables
%if %{yum_install} || %{zypper_install}
mkdir -p %{buildroot}%{_sbindir}
cp bin/* %{buildroot}%{_sbindir}/
%endif

#clean up tracer if its not being built
%if %{build_tracer}
#do nothing
%else
rm %{buildroot}%{katello_libdir}/tracer.py
rm %{buildroot}%{_sbindir}/katello-tracer-upload
%if %{yum_install} || %{zypper_install}
rm %{buildroot}%{plugins_confdir}/tracer_upload.conf
%endif
%endif


# RHSM plugin
mkdir -p %{buildroot}%{_sysconfdir}/rhsm/pluginconf.d/
mkdir -p %{buildroot}%{_datadir}/rhsm-plugins/
cp etc/rhsm/pluginconf.d/fqdn.FactsPlugin.conf %{buildroot}%{_sysconfdir}/rhsm/pluginconf.d/fqdn.FactsPlugin.conf
cp src/rhsm-plugins/fqdn.py %{buildroot}%{_datadir}/rhsm-plugins/fqdn.py

# cache directory
mkdir -p %{buildroot}%{_localstatedir}/cache/katello-agent/

%if 0%{?fedora} > 18 || 0%{?rhel} > 6
# crontab
mkdir -p %{buildroot}%{_sysconfdir}/cron.d/
cp extra/katello-agent-send.cron %{buildroot}%{_sysconfdir}/cron.d/%{name}
%endif

%clean
rm -rf %{buildroot}

%if %{build_agent}
%post -n katello-agent
%if %{dnf_install}
sed 's/bin\/python/bin\/python3/' /etc/sysconfig/goferd -i
%endif

%if 0%{?fedora} > 18 || 0%{?rhel} > 6
  systemctl enable goferd
  /bin/systemctl start goferd > /dev/null 2>&1 || :
%else
  chkconfig goferd on
  /sbin/service goferd start > /dev/null 2>&1 || :
%endif

touch /tmp/katello-agent-restart
exit 0
%endif

%posttrans
katello-package-upload 2> /dev/null
katello-enabled-repos-upload 2> /dev/null
exit 0

%if %{build_agent}
%postun -n katello-agent
touch /tmp/katello-agent-restart
exit 0

%files -n katello-agent
%defattr(-,root,root,-)
%config %{_sysconfdir}/gofer/plugins/katello.conf
%{katello_libdir}/agent/__init__.py*
%{katello_libdir}/agent/goferd/plugin.*
%{katello_libdir}/agent/goferd/__init__.py*

%if %{legacy_agent}
%else
%{katello_libdir}/agent/pulp/__init__.py*
%{katello_libdir}/agent/pulp/dispatcher.py*
%{katello_libdir}/agent/pulp/handler.py*
%{katello_libdir}/agent/pulp/libdnf.py*
%{katello_libdir}/agent/pulp/libyum.py*
%{katello_libdir}/agent/pulp/report.py*

%if %{dnf_install}
%{katello_libdir}/agent/goferd/__pycache__/__init__.*
%{katello_libdir}/agent/goferd/__pycache__/plugin.*
%{katello_libdir}/agent/__pycache__/__init__.*
%{katello_libdir}/agent/pulp/__pycache__/__init__.*
%{katello_libdir}/agent/pulp/__pycache__/dispatcher.*
%{katello_libdir}/agent/pulp/__pycache__/handler.*
%{katello_libdir}/agent/pulp/__pycache__/libdnf.*
%{katello_libdir}/agent/pulp/__pycache__/libyum.*
%{katello_libdir}/agent/pulp/__pycache__/report.*
%endif

%endif
%endif

%files
%defattr(-,root,root,-)
%doc LICENSE
%dir %{_localstatedir}/cache/katello-agent/

%if %{yum_install} || %{zypper_install}
%config(noreplace) %{plugins_confdir}/package_upload.conf
%config(noreplace) %{plugins_confdir}/enabled_repos_upload.conf
%endif

%dir %{katello_libdir}/
%{katello_libdir}/constants.py*
%{katello_libdir}/enabled_report.py*
%{katello_libdir}/packages.py*
%{katello_libdir}/repos.py*
%{katello_libdir}/uep.py*
%{katello_libdir}/utils.py*
%{katello_libdir}/__init__.py*

%if %{yum_install} || %{zypper_install}
%{plugins_dir}/enabled_repos_upload.py*
%{plugins_dir}/package_upload.py*
%endif

%if %{dnf_install}
%{katello_libdir}/__pycache__/constants.*
%{katello_libdir}/__pycache__/enabled_report.*
%{katello_libdir}/__pycache__/packages.*
%{katello_libdir}/__pycache__/repos.*
%{katello_libdir}/__pycache__/uep.*
%{katello_libdir}/__pycache__/utils.*
%{katello_libdir}/__pycache__/__init__.*
%else
%attr(750, root, root) %{_sbindir}/katello-package-upload
%attr(750, root, root) %{_sbindir}/katello-enabled-repos-upload
%endif

%if %{zypper_install}
%dir %{_usr}/lib/zypp/
%dir %{_usr}/lib/zypp/plugins/
%dir %{_usr}/lib/zypp/plugins/commit/
%endif

%if 0%{?fedora} > 18 || 0%{?rhel} > 6
%config(noreplace) %attr(0644, root, root) %{_sysconfdir}/cron.d/%{name}
%endif

%files fact-plugin
%defattr(-,root,root,-)
%dir %{_sysconfdir}/rhsm/
%dir %{_sysconfdir}/rhsm/pluginconf.d/
%config %{_sysconfdir}/rhsm/pluginconf.d/fqdn.FactsPlugin.conf
%dir %{_datadir}/rhsm-plugins/
%{_datadir}/rhsm-plugins/fqdn.*

%if %{build_tracer}
%files tracer
%defattr(-,root,root,-)
%if %{yum_install} || %{zypper_install}
%{plugins_dir}/tracer_upload.py*
%{plugins_confdir}/tracer_upload.conf
%endif
%{katello_libdir}/tracer.py*

%if %{dnf_install}
%{katello_libdir}/__pycache__/tracer.*
%else
%attr(750, root, root) %{_sbindir}/katello-tracer-upload
%endif
%endif #build_tracer

%changelog
* Wed Nov 28 2018 John Mitsch <jomitsch@redhat.com> - 3.4.0-1
- Update katello-host-tools to 3.4.0 and specify subscription-manager version

* Mon Nov 12 2018 Jonathon Turel <jturel@gmail.com> - 3.3.6-2
- Fix katello-agent upgrades from old versions

* Wed Oct 17 2018 Justin Sherrill <jlsherrill@gmail.com> - 3.3.6-1
- 3.3.6 release

* Fri Sep 21 2018 Patrick Creech <pcreech@redhat.com> - 3.3.5-3
- Decrease Obsolete version for python-pulp-rpm-common

* Tue Sep 18 2018 Eric D. Helms <ericdhelms@gmail.com> - 3.3.5-2
- Obsolete python-pulp-rpm-common on EL7

* Wed Aug 29 2018 Jonathon Turel <jturel@gmail.com> - 3.3.5-1
- Fixes #24500 - prevent exceptions through registerCommand
- Remove old makefile syntax from readme
- Add a readme, makefile help, other small fixes

* Mon Jul 23 2018 Jonathon Turel <jturel@gmail.com> - 3.3.4-1
- Fixes #24353 - handle update all packages

* Fri Jul 20 2018 Jonathon Turel <jturel@gmail.com> - 3.3.3-1
- Fixes #24270: Handle server errors

* Tue Jul 17 2018 Jonathon Turel <jturel@gmail.com> - 3.3.2-2
- Fix obsoletes

* Fri Jul 13 2018 Jonathon Turel <jturel@gmail.com> - 3.3.2-1
- Fixes #24214 - fill in vars on repo URLs (cduryee@redhat.com)

* Thu Jun 28 2018 Jonathon Turel <jturel@gmail.com> - 3.3.1-1
- fixes #24081 - Fix errata install of extra packages.
- fixes #24006 - support plugin reload when queue not found.

* Fri May 25 2018 Jonathon Turel <jturel@gmail.com> - 3.3.0-1
- Fixes #23459 - Restore legacy goferd plugin
- Remove yum plugin dep, dead code, fix lint
- Further containerize the tests
- Fixes #23405 - Tracer executable throws error

* Thu May 10 2018 Justin Sherrill <jsherrill@gmail.com> 3.2.1-4
- suse build fixes

* Mon Apr 30 2018 Justin Sherrill <jlsherrill@gmail.com> 3.2.1-3
- Backporting format issue with enabled-repos

* Thu Apr 19 2018 Eric D. Helms <ericdhelms@gmail.com> - 3.2.1-2
- rebuilt

* Wed Mar 21 2018 Justin Sherrill <jsherril@redhat.com> 3.2.0-1
- Version bump 3.2.0 (jturel@redhat.com)
- Fixes #22889 - Zypper client tooling (paji@redhat.com)
- Fixes #22852 - Python3 support for Facts plugin (jturel@redhat.com)
- Fixes #22330 - Always run cron after reboot (seanokeeffe797@gmail.com)
- Fixes #22852 - Python3 support for Facts plugin (jturel@redhat.com)
- Refs #22623 - Support DNF (jturel@redhat.com)

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
