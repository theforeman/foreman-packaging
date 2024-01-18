%global dnf_install (0%{?rhel} > 7) || (0%{?fedora} > 26)
%global yum_install ((0%{?rhel} <= 7) && (0%{?rhel} >= 5)) || ((0%{?fedora} < 27) && (0%{?fedora} > 0))
%global zypper_install (0%{?suse_version} > 0)
%global build_tracer 0%{?rhel} >= 7 || 0%{?fedora} || 0%{?suse_version}

%global build_agent 0
%global legacy_agent 0

%if 0%{?suse_version}
%define dist suse%{?suse_version}
%endif

%if %{dnf_install}
%global python_libdir %{python3_sitelib}
%global plugins_dir %{python3_sitelib}/dnf-plugins
%global plugins_confdir %{_sysconfdir}/dnf/plugins
%endif

%if %{yum_install}
%if 0%{?rhel} == 6
%global python_libdir %{python_sitelib}
%else
%global python_libdir %{python2_sitelib}
%endif
%global plugins_dir %{_usr}/lib/yum-plugins
%global plugins_confdir %{_sysconfdir}/yum/pluginconf.d
%endif

%if %{zypper_install}
%global python_libdir %{python_sitelib}
%global plugins_dir %{_usr}/lib/zypp/plugins/commit/
# Deploy yum plugin config to control reports
%global plugins_confdir %{_sysconfdir}/yum/pluginconf.d
%endif

%global katello_libdir %{python_libdir}/katello

Name: katello-host-tools
Version: 4.2.3
Release: 5%{?dist}
Summary: A set of commands and yum plugins that support a Katello host
Group:   Development/Languages
%if 0%{?suse_version}
License: LGPL-2.0
%else
License: LGPLv2
%endif
URL:     https://github.com/Katello/katello-agent
Source0: https://codeload.github.com/Katello/katello-host-tools/tar.gz/%{version}#/%{name}-%{version}.tar.gz

%if 0%{?suse_version} && 0%{?suse_version} < 1200
# this needs to be BuildArch for Suse but
# keeping it as ExclusiveArch to avoid lint errors
ExclusiveArch: x86_64
%else
BuildArch: noarch
%endif

Requires: subscription-manager
Obsoletes: %{name}-fact-plugin < %{version}-%{release}

%if %{dnf_install} || 0%{?suse_version} >= 1500
Requires: python3-subscription-manager-rhsm
%else
Requires: python-rhsm
%endif

%if 0%{?suse_version}
%if 0%{?suse_version} >= 1500
BuildRequires: python3-devel
Requires: python3-zypp-plugin
%else
BuildRequires: python-devel >= 2.6
Requires: python2-zypp-plugin
%endif
%else
%if %{dnf_install}
BuildRequires: python3-devel
%else
BuildRequires: python2-devel
%endif
%endif

%if %{dnf_install} || 0%{?suse_version} >= 1500
BuildRequires: python3-setuptools
%else
BuildRequires: python-setuptools
%endif

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
Requires: dnf >= 4.0.9
Requires: python3-libdnf
%else
Requires: python-gofer-proton >= 2.5
%endif

Requires: subscription-manager
Requires: %{name} = %{version}-%{release}

%if 0%{?rhel} == 6
Requires: yum-plugin-security
%endif

%description -n katello-agent
Provides plugin for gofer, which allows communicating with Katello server
and execute scheduled actions.
%endif

%if %{build_tracer}
%package tracer
BuildArch:  noarch
Summary:    Adds Tracer functionality to a client managed by katello-host-tools
Group:      Development/Languages
Requires: %{name} = %{version}-%{release}
%if 0%{?suse_version}
Requires: cronie
%else
Requires: crontabs
%endif
%if %{dnf_install}
Requires: python3-tracer
%else
%if 0%{?suse_version} == 0
Requires: python2-tracer >= 0.6.12
%endif
%endif

%description tracer
Adds Tracer functionality to a client managed by katello-host-tools
%endif

%prep
%setup -q

%build
# Remove apt bits
rm -r src/apt_plugins
rm src/katello/deb_tracer.py

%if !%{dnf_install}
rm -r src/dnf_plugins
%else
# 'Hack' for the fact that dnf recognizes plugins in 'dnf-plugins'
# can be removed when we update to a release that contains https://github.com/Katello/katello-host-tools/pull/145
mv src/dnf_plugins src/dnf-plugins
%endif

%if !%{yum_install}
rm -r src/yum-plugins
%endif

%if !%{zypper_install}
rm -r src/zypper_plugins
rm src/katello/zypper_tracer.py
%endif

%if %{build_tracer}
%if %{dnf_install}
# On DNF installs a small shell wrapper for "dnf katello-tracer-upload" is used
sed -i '/katello-tracer-upload=katello.scripts:tracer_upload/d' src/setup.py
%endif
%else
rm src/katello/tracer.py
sed -i '/katello-tracer-upload=katello.scripts:tracer_upload/d' src/setup.py
rm etc/yum/pluginconf.d/tracer_upload.conf
%endif

%if %{build_agent}
%if %{legacy_agent}
mv src/katello/agent/goferd/legacy_plugin.py src/katello/agent/goferd/plugin.py
rm -r src/katello/agent/pulp
%else
rm src/katello/agent/goferd/legacy_plugin.py
# This should be in test/ instead of src/
rm src/katello/agent/pulp/test.py
%endif
%else
rm -r src/katello/agent
%endif

pushd src
%if %{dnf_install} || 0%{?suse_version} >= 1500
%py3_build
%else
%if 0%{?rhel} == 6
%{__python} setup.py build
%else
%py_build
%endif
%endif
popd

%install
rm -rf %{buildroot}

pushd src
%if %{dnf_install} || 0%{?suse_version} >= 1500
%py3_install
%else
%if 0%{?rhel} == 6
%{__python} setup.py install --root %{buildroot}
%else
%py_install
%endif
%endif
popd

mkdir -p %{buildroot}%{_sbindir}
mv %{buildroot}%{_bindir}/* %{buildroot}%{_sbindir}/

%if %{build_agent}
mkdir -p %{buildroot}%{_sysconfdir}/gofer/plugins
cp etc/gofer/plugins/katello.conf %{buildroot}%{_sysconfdir}/gofer/plugins

# cache directory
mkdir -p %{buildroot}%{_localstatedir}/cache/katello-agent/
%endif

%if %{dnf_install} || %{yum_install} || %{zypper_install}
mkdir -p %{buildroot}%{plugins_confdir}
%if %{dnf_install}
cp etc/yum/pluginconf.d/tracer_upload.conf %{buildroot}%{plugins_confdir}/
%else
cp etc/yum/pluginconf.d/*.conf %{buildroot}%{plugins_confdir}/
%endif
%endif

%if %{yum_install}
mkdir -p %{buildroot}%{plugins_dir}
cp src/yum-plugins/*.py %{buildroot}%{plugins_dir}/
%endif

%if %{zypper_install}
mkdir -p %{buildroot}%{plugins_dir}
cp src/zypper_plugins/*.py %{buildroot}%{plugins_dir}/
rm %{buildroot}%{plugins_dir}/__init__.py
%endif

%if %{build_tracer}
# executables
mkdir -p %{buildroot}%{_sbindir}
%if %{dnf_install}
cp extra/katello-tracer-upload-dnf %{buildroot}%{_sbindir}/katello-tracer-upload
%endif

# crontab
mkdir -p %{buildroot}%{_sysconfdir}/cron.d/
cp extra/katello-tracer-upload.cron %{buildroot}%{_sysconfdir}/cron.d/katello-tracer-upload
%endif

%clean
rm -rf %{buildroot}

%if %{build_agent}
%post -n katello-agent
%if %{dnf_install}
sed 's/bin\/python$/bin\/python3/' /etc/sysconfig/goferd -i
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

%if %{yum_install} || %{zypper_install}
%posttrans
katello-package-upload 2> /dev/null
katello-enabled-repos-upload 2> /dev/null
exit 0
%endif

%if %{build_agent}
%postun -n katello-agent
touch /tmp/katello-agent-restart
exit 0

%files -n katello-agent
%defattr(-,root,root,-)
%config %{_sysconfdir}/gofer/plugins/katello.conf
%{katello_libdir}/agent/
%dir %{_localstatedir}/cache/katello-agent/
%endif

%files
%defattr(-,root,root,-)
%if 0%{?rhel} == 6
%doc LICENSE
%else
%license LICENSE
%endif

%{katello_libdir}
%{python_libdir}/katello_host_tools-*.egg-info
%exclude %{katello_libdir}/contrib

%if %{build_agent}
%exclude %{katello_libdir}/agent
%endif

%if %{build_tracer}
# TODO pycached unavailable on SuSE - what to do with cache files?
%if %{zypper_install}
%exclude %{katello_libdir}/tracer.py
%else
%if %{yum_install}
%exclude %{katello_libdir}/tracer.py*
%else
%pycached %exclude %{katello_libdir}/tracer.py
%endif
%endif

%if %{dnf_install}
%pycached %exclude %{plugins_dir}/__init__.py
%else
%exclude %{plugins_dir}
%endif
%endif

%if %{yum_install} || %{zypper_install}
%attr(750, root, root) %{_sbindir}/katello-package-upload
%attr(750, root, root) %{_sbindir}/katello-enabled-repos-upload
%else
%exclude %{_sbindir}/katello-package-upload
%exclude %{_sbindir}/katello-enabled-repos-upload
%endif

%if %{zypper_install}
%dir %{_sysconfdir}/yum
%dir %{plugins_confdir}
%exclude %{python_libdir}/zypper_plugins
%endif

%if %{yum_install}
%{plugins_dir}
%exclude %{python_libdir}/yum-plugins
%endif

%if %{yum_install} || %{zypper_install}
%config(noreplace) %{plugins_confdir}/package_upload.conf
%config(noreplace) %{plugins_confdir}/enabled_repos_upload.conf
%endif

%if %{build_tracer}
%files tracer
%defattr(-,root,root,-)
%if %{zypper_install}
%{katello_libdir}/tracer.py
%dir %{_usr}/lib/zypp
%dir %{_usr}/lib/zypp/plugins
%dir %{plugins_dir}
%{plugins_dir}/tracer_upload.py
%else
%if %{yum_install}
%{katello_libdir}/tracer.py*
%{plugins_dir}/tracer_upload.py*
%else
%pycached %{katello_libdir}/tracer.py
%pycached %{plugins_dir}/tracer_upload.py
%endif
%endif
%{plugins_confdir}/tracer_upload.conf
%config(noreplace) %attr(0644, root, root) %{_sysconfdir}/cron.d/katello-tracer-upload
%attr(750, root, root) %{_sbindir}/katello-tracer-upload
%endif


%changelog
* Thu Jan 18 2024 Evgeni Golov - 4.2.3-5
- Don't install package and repository upload on DNF installs

* Wed Sep 13 2023 Eric D. Helms <ericdhelms@gmail.com> - 4.2.3-4
- Stop building katello-agent

* Thu Apr 20 2023 Patrick Creech <pcreech@redhat.com> - 4.2.3-3
- Fix dnf-plugin location for tracer

* Tue Mar 28 2023 Patrick Creech <pcreech@redhat.com> - 4.2.3-2
- Fix building on el6
- Build agent for el9

* Fri Mar 17 2023 Patrick Creech <pcreech@redhat.com> - 4.2.3-1
- Release 4.2.3

* Tue May 24 2022 Eric D. Helms <ericdhelms@gmail.com> - 3.5.7-5
- Stop building katello-host-tools-fact-plugin

* Thu Apr 14 2022 Bernhard Suttner - 3.5.7-4
- Improve regular expression for python2/python3 interop

* Wed Feb 09 2022 Patrick Creech <pcreech@redhat.com> - 3.5.7-3
- Fixup python macros to be more compliant with recent changes

* Mon Oct 25 2021 Bernhard Suttner - 3.5.7-2
- Build for SLES 15 with python3

* Fri Oct 15 2021 Bernhard Suttner - 3.5.7-1
- Update to 3.5.7
- Add cron job for tracer upload to tracer package and
  use this cron job for sles, too.

* Wed Sep 22 2021 Jonathon Turel <jturel@gmail.com> 3.5.6-1
- Update to 3.5.6

* Mon May 31 2021 Bernhard Suttner - 3.5.5-2
- Use suse_version instead of sles_version to make
  sure python2-zypp-plugin is a requirement

* Thu Apr 29 2021 Justin Sherrill <jsherril@redhat.com> 3.5.5-1
* update to 3.5.5

* Fri Feb 05 2021 Eric D. Helms <ericdhelms@gmail.com> - 3.5.4-3
- Build katello-agent for EL8

* Mon Dec 07 2020 Evgeni Golov - 3.5.4-2
- remove EL5 bits that aren't longer needed

* Wed May 27 2020 Jonathon Turel - 3.5.4-1
- Release 3.5.4

* Fri Mar 27 2020 Bernhard Suttner - 3.5.3-3
- SLES requires python2-zypp-plugin

* Mon Mar 23 2020 Jonathon Turel - 3.5.3-2
- require matching katello-host-tools version in subpackages

* Mon Feb 17 2020 Jonathon Turel - 3.5.3-1
- Release 3.5.3

* Tue Jan 14 2020 Evgeni Golov - 3.5.2-2
- Rebuild for EL8 client repository

* Mon Jan 13 2020 Jonathon Turel - 3.5.2-1
- Release 3.5.2

* Thu Aug 1 2019 Jonathon Turel - 3.5.1-2
- Updates from SLES builds

* Fri Jun 21 2019 Jonathon Turel - 3.5.1-1
- Fixes #26920 - Install errata via libdnf
- Fixes #26375 - zypper plugin for tracer upload

* Thu May 23 2019 Garret Rumohr - 3.5.0-4
- Fixes #26837 - Corrects string replacement in /etc/sysconfig/goferd by RPM script

* Thu May 23 2019 Evgeni Golov - 3.5.0-3
- don't build the tracer plugin on RHEL < 7

* Tue Apr 23 2019 Evgeni Golov - 3.5.0-2
- Don't ship fact-plugin on modern Fedora and EL

* Thu Mar 28 2019 Justin Sherrill - 3.5.0-1
- Update to 3.5.0, drop support for agent on f27 and f28
- Install katello-tracer-upload wrapper on DNF platforms

* Wed Jan 30 2019 Evgeni Golov - 3.4.2-2
- Explicitly build using Python3 on Python3 distibutions

* Mon Jan 14 2019 Jonathon Turel <jturel@gmail.com> - 3.4.2-1
- Fixes #25725 - disable plugins if we have subman profiles

* Tue Dec 11 2018 Jonathon Turel <jturel@gmail.com> - 3.4.1-1
- Restore DNF tracer plugin

* Mon Dec 3 2018 Jonathon Turel <jturel@gmail.com> - 3.4.0-3
- Don't specify subman minimum version for now

* Mon Dec 3 2018 Jonathon Turel <jturel@gmail.com> - 3.4.0-2
- Downgrade subscription-manager dependency until it's in centos7 repos

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
