
# Determine supported
%if 0%{?fedora} || 0%{?rhel} >= 6
%define with_tools 1
%endif
%if 0%{?fedora} || 0%{?rhel} >= 7
%define with_systemd 1
%endif
%if 0%{?fedora} || 0%{?rhel} <= 7
%define with_python2 1
%endif
%if 0%{?fedora} || 0%{?rhel} >= 8
%define with_python3 1
%endif
%if 0%{?fedora}
%define p2n 2
%endif


Name: gofer
Version: 2.12.5
Release: 3%{?dist}
Summary: A lightweight, extensible python agent
Group:   Development/Languages
License: LGPLv2
URL: https://github.com/jortel/gofer
Source0: https://github.com/jortel/gofer/archive/%{name}-%{version}-1.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
%if 0%{?with_python2}
Requires: python%{?p2n}-%{name} = %{version}
%else
Requires: python3-%{name} = %{version}
%endif
%if 0%{?with_systemd}
BuildRequires: systemd
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
%endif
%description
Gofer provides an extensible, light weight, universal python agent.
The gofer core agent is a python daemon (service) that provides
infrastructure for exposing a remote API and for running Recurring
Actions. The APIs contributed by plug-ins are accessible by Remote
Method Invocation (RMI). The transport for RMI is AMQP using an
AMQP message broker. Actions are also provided by plug-ins and are
executed at the specified interval.

%prep
%setup -q -n %{name}-%{name}-%{version}-1

%build
pushd src
rm ./gofer/devel/test.py
%if !0%{?with_tools}
rm -rf ./gofer/tools/
%endif
%if 0%{?with_python2}
%if 0%{?p2n}
%{py2_build}
%else
%{py_build}
%endif
%endif
%if 0%{?with_python3}
%{py3_build}
%endif
popd
pushd docs/man/man1
gzip *
popd

%install
rm -rf %{buildroot}
pushd src
%if 0%{?with_python2}
%if 0%{?p2n}
%{py2_install}
%else
%{py_install}
%endif
%endif
%if 0%{?with_python3}
%{py3_install}
%endif
popd

mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/%{_sysconfdir}/%{name}
mkdir -p %{buildroot}/%{_sysconfdir}/%{name}/plugins
mkdir -p %{buildroot}/%{_sysconfdir}/%{name}/conf.d
mkdir -p %{buildroot}/%{_sysconfdir}/init.d
mkdir -p %{buildroot}/%{_sysconfdir}/sysconfig
mkdir -p %{buildroot}/%{_unitdir}
mkdir -p %{buildroot}/%{_usr}/lib/%{name}/plugins
mkdir -p %{buildroot}/%{_usr}/share/%{name}/plugins
mkdir -p %{buildroot}/%{_mandir}/man1

cp bin/* %{buildroot}/usr/bin
cp etc/%{name}/*.conf %{buildroot}/%{_sysconfdir}/%{name}
cp etc/sysconfig/%{name}d %{buildroot}/%{_sysconfdir}/sysconfig
cp docs/man/man1/* %{buildroot}/%{_mandir}/man1

cp plugins/demo.conf %{buildroot}/%{_sysconfdir}/%{name}/plugins
cp plugins/demo.py %{buildroot}/%{_usr}/share/%{name}/plugins

%if 0%{?with_systemd}
cp usr/lib/systemd/system/* %{buildroot}/%{_unitdir}
%else
cp etc/init.d/%{name}d %{buildroot}/%{_sysconfdir}/init.d
%endif

%if 0%{?with_python2}
rm -rf %{buildroot}/%{python2_sitelib}/%{name}*.egg-info
%endif
%if 0%{?with_python3}
rm -rf %{buildroot}/%{python3_sitelib}/%{name}*.egg-info
%endif

%if !0%{?with_python2}
sed -i '1 s/python/python3/' %{buildroot}/usr/bin/%{name}
sed -i '1 s/python/python3/' %{buildroot}/usr/bin/%{name}d
%endif
%if !0%{?with_tools}
rm %{buildroot}/usr/bin/%{name}
rm %{buildroot}/%{_mandir}/man1/gofer.*
%endif

%files
%defattr(-,root,root,-)
%dir %{_sysconfdir}/%{name}/
%dir %{_sysconfdir}/%{name}/conf.d/
%dir %{_sysconfdir}/%{name}/plugins/
%dir %{_usr}/lib/%{name}/plugins/
%dir %{_usr}/share/%{name}/plugins/
%{_bindir}/%{name}d
%if 0%{?with_systemd}
%attr(644,root,root) %{_unitdir}/%{name}d.service
%else
%attr(755,root,root) %{_sysconfdir}/init.d/%{name}d
%endif
%attr(644,root,root) %{_sysconfdir}/sysconfig/%{name}d
%config(noreplace) %{_sysconfdir}/%{name}/agent.conf
%config(noreplace) %{_sysconfdir}/%{name}/plugins/demo.conf
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}d
%{_usr}/share/%{name}/plugins/demo.*
%doc LICENSE
%doc %{_mandir}/man1/goferd.*

%post
%if 0%{?with_systemd}
%systemd_post %{name}d.service
%else
chkconfig --add %{name}d
%endif

%preun
%if 0%{?with_systemd}
%systemd_preun %{name}d.service
%else
if [ $1 = 0 ] ; then
   /sbin/service %{name}d stop >/dev/null 2>&1
   /sbin/chkconfig --del %{name}d
fi
%endif

%postun
%if 0%{?with_systemd}
%systemd_postun_with_restart %{name}d.service
%endif


# --- tools ------------------------------------------------------------------
%if 0%{?with_tools}

%package -n %{name}-tools
Summary: Gofer tools
Group: Development/Languages
%if 0%{?with_python2}
Requires: python%{?p2n}-%{name} = %{version}
%else
Requires: python3-%{name} = %{version}
%endif

%description -n%{name}-tools
Provides the gofer tools.

%files -n %{name}-tools
%defattr(-,root,root,-)
%{_bindir}/%{name}
%doc LICENSE
%doc %{_mandir}/man1/gofer.*

%endif


# --- python lib -------------------------------------------------------------

%if 0%{?with_python2}

%package -n python%{?p2n}-%{name}
Summary: Gofer python lib modules
Group: Development/Languages
BuildRequires: python%{?p2n}-devel
BuildRequires: python%{?p2n}-setuptools
Requires: python%{?p2n}-six
Requires: pam
%if 0%{?rhel} == 5
Requires: python%{?p2n}-ctypes
Requires: python%{?p2n}-simplejson
Requires: python%{?p2n}-hashlib
Requires: python%{?p2n}-uuid
%endif

%if 0%{?p2n}
%{?python_provide:%python_provide python2-%{name}}
%endif

%description -n python%{?p2n}-%{name}
Provides gofer python common modules.

%files -n python%{?p2n}-%{name}
%defattr(-,root,root,-)
%{python2_sitelib}/%{name}/*.py*
%{python2_sitelib}/%{name}/compat/
%{python2_sitelib}/%{name}/agent/
%{python2_sitelib}/%{name}/rmi/
%{python2_sitelib}/%{name}/tools/
%{python2_sitelib}/%{name}/devel/
%dir %{python2_sitelib}/%{name}/messaging/
%dir %{python2_sitelib}/%{name}/messaging/adapter
%{python2_sitelib}/%{name}/messaging/*.py*
%{python2_sitelib}/%{name}/messaging/adapter/*.py*
%doc LICENSE

%endif

# ---

%if 0%{?with_python3}

%package -n python3-%{name}
Summary: Gofer python lib modules
Group: Development/Languages
BuildRequires: python3-devel
BuildRequires: python3-setuptools
Requires: python3-six
Requires: pam

%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
Provides gofer python common modules.

%files -n python3-%{name}
%defattr(-,root,root,-)
%{python3_sitelib}/%{name}/*.py
%{python3_sitelib}/%{name}/__pycache__/
%{python3_sitelib}/%{name}/compat/
%{python3_sitelib}/%{name}/agent/
%{python3_sitelib}/%{name}/rmi/
%{python3_sitelib}/%{name}/tools/
%{python3_sitelib}/%{name}/devel/
%dir %{python3_sitelib}/%{name}/messaging/
%dir %{python3_sitelib}/%{name}/messaging/adapter
%{python3_sitelib}/%{name}/messaging/*.py
%{python3_sitelib}/%{name}/messaging/__pycache__/
%{python3_sitelib}/%{name}/messaging/adapter/*.py
%{python3_sitelib}/%{name}/messaging/adapter/__pycache__/
%doc LICENSE

%endif


# --- python-qpid messaging adapter ------------------------------------------

%if 0%{?with_python2}

%package -n python%{?p2n}-%{name}-qpid
Summary: Gofer Qpid messaging adapter python package
Group: Development/Languages
BuildRequires: python%{?p2n}-devel
Requires: python%{?p2n}-%{name} = %{version}
Requires: python%{?p2n}-qpid >= 0.18
%if 0%{?rhel} == 5
Requires: python%{?p2n}-ssl
%endif

%if 0%{?p2n}
%{?python_provide:%python_provide python2-%{name}-qpid}
%endif

%description -n python%{?p2n}-%{name}-qpid
Provides the gofer qpid messaging adapter package.

%files -n python%{?p2n}-%{name}-qpid
%{python2_sitelib}/%{name}/messaging/adapter/qpid
%doc LICENSE

%endif

# ---

%if 0%{?with_python3}

%package -n python3-%{name}-qpid
Summary: Gofer Qpid messaging adapter python package
Group: Development/Languages
BuildRequires: python3-devel
Requires: python3-%{name} = %{version}
Requires: python3-qpid >= 0.18

%{?python_provide:%python_provide python3-%{name}-qpid}

%description -n python3-%{name}-qpid
Provides the gofer qpid messaging adapter package.

%files -n python3-%{name}-qpid
%{python3_sitelib}/%{name}/messaging/adapter/qpid
%doc LICENSE

%endif


# --- python-qpid-proton messaging adapter -----------------------------------

%if 0%{?with_python2}

%package -n python%{?p2n}-%{name}-proton
Summary: Gofer Qpid proton messaging adapter python package
Group: Development/Languages
BuildRequires: python%{?p2n}-devel
Requires: python%{?p2n}-%{name} = %{version}
Requires: python%{?p2n}-qpid-proton >= 0.9-5

%if 0%{?p2n}
%{?python_provide:%python_provide python2-%{name}-proton}
%endif

%description -n python%{?p2n}-%{name}-proton
Provides the gofer qpid proton messaging adapter package.

%files -n python%{?p2n}-%{name}-proton
%{python2_sitelib}/%{name}/messaging/adapter/proton
%doc LICENSE

%endif

# ---

%if 0%{?with_python3}

%package -n python3-%{name}-proton
Summary: Gofer Qpid proton messaging adapter python package
Group: Development/Languages
BuildRequires: python3-devel
Requires: python3-%{name} = %{version}
Requires: python3-qpid-proton >= 0.9-5

%{?python_provide:%python_provide python3-%{name}-proton}

%description -n python3-%{name}-proton
Provides the gofer qpid proton messaging adapter package.

%files -n python3-%{name}-proton
%{python3_sitelib}/%{name}/messaging/adapter/proton
%doc LICENSE

%endif


# --- python-amqp messaging adapter ------------------------------------------

%if 0%{?with_python2}

%package -n python%{?p2n}-%{name}-amqp
Summary: Gofer amqp messaging adapter python package
Group: Development/Languages
BuildRequires: python%{?p2n}-devel
Requires: python%{?p2n}-%{name} = %{version}
Requires: python%{?p2n}-amqp >= 2.1.4

%if 0%{?p2n}
%{?python_provide:%python_provide python2-%{name}-amqp}
%endif

%description -n python%{?p2n}-%{name}-amqp
Provides the gofer amqp messaging adapter package.

%files -n python%{?p2n}-%{name}-amqp
%{python2_sitelib}/%{name}/messaging/adapter/amqp
%doc LICENSE

%endif

# ---

%if 0%{?with_python3}

%package -n python3-%{name}-amqp
Summary: Gofer amqp messaging adapter python package
Group: Development/Languages
BuildRequires: python3-devel
Requires: python3-%{name} = %{version}
Requires: python3-amqp >= 2.1.4

%{?python_provide:%python_provide python3-%{name}-amqp}

%description -n python3-%{name}-amqp
Provides the gofer amqp messaging adapter package.

%files -n python3-%{name}-amqp
%{python3_sitelib}/%{name}/messaging/adapter/amqp
%doc LICENSE

%endif


# --- changelog --------------------------------------------------------------


%changelog
* Wed Mar 06 2019 Evgeni Golov - 2.12.5-3
- Make gofer depend on the correct pythonX-gofer library.

* Wed Jan 30 2019 Evgeni Golov - 2.12.5-2
- Don't build Python2 libs on EL8.

* Tue Oct 02 2018 Jeff Ortel <jortel@redhat.com> 2.12.5-1
- Consumer read call no_route instead of repair on node not-found.
  (jortel@redhat.com)

* Tue Oct 02 2018 Jeff Ortel <jortel@redhat.com> 2.12.4-1
- Consumer read: log node-not-found at debug instead of error.
  (jortel@redhat.com)

* Mon Oct 01 2018 Jeff Ortel <jortel@redhat.com> 2.12.3-1
- bz:1417345, consumer log node-not-found at debug instead of error.
  (jortel@redhat.com)

* Tue Sep 18 2018 Jeff Ortel <jortel@redhat.com> 2.12.2-1
- Adapter reliability logging at WARN instead of ERROR. (jortel@redhat.com)
- Update logging documentation; Clean removed from spec. (jortel@redhat.com)

* Thu Jun 21 2018 Jeff Ortel <jortel@redhat.com> 2.12.1-1
- Reload plugin on no-route caused by missing queue. (jortel@redhat.com)

* Wed May 23 2018 Jeff Ortel <jortel@redhat.com> 2.12.0-1
- Fix buildrequires: python3-setuptools. (jortel@redhat.com)

* Tue May 22 2018 Jeff Ortel <jortel@redhat.com> 2.12.0-0
- python-future not available in el6/el7. (jortel@redhat.com)
- Fixed exception propagation of builtin exceptions when raised by different python versions (2/3).
- Fixed raising ValidationError when non-validation related exceptions are caught.
- Z-bit added to version: 2.12.0

* Tue May 08 2018 Jeff Ortel <jortel@redhat.com> 2.12-0
- Add support for python3; Drop support for python<2.7. (jortel@redhat.com)

* Tue Apr 24 2018 Jeff Ortel <jortel@redhat.com> 2.11.4-3
- Fixed dist in spec. (jortel@redhat.com)

* Thu Apr 12 2018 Jeff Ortel <jortel@redhat.com> 2.11.4-2
- packaging: with_systemd and with_tools; devel not packaged.
  (jortel@redhat.com)

* Wed Apr 11 2018 Jeff Ortel <jortel@redhat.com> 2.11.4-1
- Apply upstream patch. (jortel@redhat.com)

* Wed Apr 11 2018 Jeff Ortel <jortel@redhat.com> 2.11.3-1
- Fix amqp handling of: Basic.return: (312) NO_ROUTE. (jortel@redhat.com)

* Wed Apr 11 2018 Jeff Ortel <jortel@redhat.com> 2.11.2-1
- Compat with python-amqp 2.1.4. (jortel@redhat.com)

* Wed Jan 03 2018 Jeff Ortel <jortel@redhat.com> 2.11.1-1
- Add interpreter exit handler to abort threads. (jortel@redhat.com)
- Fix unit test. (jortel@redhat.com)
- Testing environment fixes. 1. Working directory in user home. 2. Auth testing
  using user=gofer instead of jortel. 3. Comment out auth testing in server.
  (jortel@redhat.com)
- Fix proton no ssl-validation to use anonymous-peer. (jortel@redhat.com)
- support root logger in agent configuration. (jortel@redhat.com)
- add dist containing sources (jortel@redhat.com)
- update url to github. (jortel@redhat.com)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.11.0-3
- Python 2 binary package renamed to python2-gofer
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Apr 07 2017 Jeff Ortel <jortel@redhat.com> 2.11.0-1
- Bumped for semantic versioning.
* Fri Apr 07 2017 Jeff Ortel <jortel@redhat.com> 2.10.1-1
- Detect broken pipe instead of TIOCSCTTY. (jortel@redhat.com)
- plugin unload should do hard shutdown. (jortel@redhat.com)
- Bumped setup.py to: 2.10 (jortel@redhat.com)

* Fri Jan 20 2017 Jeff Ortel <jortel@redhat.com> 2.10.0-1
- Add 2.10 release notes. (jortel@redhat.com)
- Support soft plugin shutdown. (jortel@redhat.com)

* Fri Jul 08 2016 Jeff Ortel <jortel@redhat.com> 2.9.2-1
- Use mp module instead of multiprocessing. (jortel@redhat.com)

* Mon Jun 27 2016 Jeff Ortel <jortel@redhat.com> 2.9.1-1
- Fix IOError errno=EAGAIN on EL5. (jortel@redhat.com)
- python 2.4 compat. (jortel@redhat.com)
- 2.9 release notes. (jortel@redhat.com)

* Fri Jun 17 2016 Jeff Ortel <jortel@redhat.com> 2.9.0-1
- Added direct and fork decorators. (jortel@redhat.com)
- Metrics enhancements. (jortel@redhat.com)

* Fri May 27 2016 Jeff Ortel <jortel@redhat.com> 2.8.1-1
- 1340262 - Fix unwanted dependency on agent in lib (jortel@redhat.com)

* Thu May 19 2016 Jeff Ortel <jortel@redhat.com> 2.8.0-1
- Support RMI invocation models. (jortel@redhat.com)
- Use LSB common pidfile kill functions to stop (rgeorge@liveramp.com)

* Wed Apr 13 2016 Jeff Ortel <jortel@redhat.com> 2.7.6-1
- Fix proton reliable send. Reported on 1323726. (jortel@redhat.com)

* Mon Feb 29 2016 Jeff Ortel <jortel@redhat.com> 2.7.5-1
- Load pam libs on demand. (jortel@redhat.com)

* Tue Feb 16 2016 Jeff Ortel <jortel@redhat.com> 2.7.4-2
- Relax proton requirement. (jortel@redhat.com)
* Fri Feb 05 2016 Jeff Ortel <jortel@redhat.com> 2.7.4-1
- Require proton 0.9-13. (jortel@redhat.com)
- Support latency plugin descriptor property. (jortel@redhat.com)
- Fix memory leak in Pending.journal. (jortel@redhat.com)
- Connections closed after each request. (jortel@redhat.com)
* Tue Jan 26 2016 Jeff Ortel <jortel@redhat.com> 2.7.3-1
- Thread resources such as connections released between RMI requests.
  (jortel@redhat.com)
* Mon Jan 25 2016 Jeff Ortel <jortel@redhat.com> 2.7.2-1
- Fix rpmlint complaint: E: incorrect-fsf-address in deplist.py (jortel@redhat.com)

* Mon Jan 11 2016 Jeff Ortel <jortel@redhat.com> 2.7.1-1
- Reference plugins relocated and not packaged. (jortel@redhat.com)
- Support runtime plugin load/unload/reload.  (jortel@redhat.com)
- Add manager. (jortel@redhat.com)
- Add gofer CLI for management and RMI. (jortel@redhat.com)
- Renamed builtin plugin to demo plugin. (jortel@redhat.com)
- Fix -f option passed to goferd. (jortel@redhat.com)
- Resend logic removed from proton reliability. (jortel@redhat.com)
- Added a ton of unit tests. (jortel@redhat.com)
- Run goferd optimized by default (sean.myers@redhat.com)
- Add additional logging in adapter reliability. (jortel@redhat.com)
- Improved handling of malformed AMQP messages. (jortel@redhat.com)
- In agent.rmi, add transactions; discard request for plugins without URL
  configured. (jortel@redhat.com)
- Support proton heartbeats; requires proton >= 0.9-5. (jortel@redhat.com)
- Persistent canceled tracking. (jortel@redhat.com)
- Authorization deprectated. (jortel@redhat.com)
- Using utf8() instead of: str(). (jortel@redhat.com)
* Mon Mar 09 2015 Jeff Ortel <jortel@redhat.com> 2.6.0-1
- Support one-time actions. (jortel@redhat.com)
- Support authenticator in the plugin descriptor. (jortel@redhat.com)
- Support plugin monitoring. (jortel@redhat.com)
- Support dynamic plugin loading, reloading, unloading.
- Support services in system plugin. (jortel@redhat.com)
- Support forwarding/accepting. (jortel@redhat.com)
- Support comprehensive broker connection clean up.
- Requires: python-ssl only on RHEL 5. (jortel@redhat.com)
- 1198797 - Fixed recursion in adapter reliability logic. (jortel@redhat.com)
- Fix not-authenticated error message. (jortel@redhat.com)
- Fix systemd unit permissions. (jortel@redhat.com)
- Window deprecated (jortel@redhat.com)

* Fri Feb 20 2015 Jeff Ortel <jortel@redhat.com> 2.5.3-1
- Broker renamed: Connector. (jortel@redhat.com)
- Plugin not-found logged and discarded. (jortel@redhat.com)

* Fri Feb 20 2015 Jeff Ortel <jortel@redhat.com> 2.5.2-1
- proton 0.9-1.20150219 compat; proton.reactors renamed: proton.reactor.
  (jortel@redhat.com)
- 1192563 - validate SSL file paths. (jortel@redhat.com)

* Thu Feb 12 2015 Jeff Ortel <jortel@redhat.com> 2.5.1-1
- Fix virtual hosts. (jortel@redhat.com)
- Using LinkDetached in proton.reliable. (jortel@redhat.com)
- Better recognition of when SSL is to be used. (jortel@redhat.com)
- Sender supports durable option. (jortel@redhat.com)
* Tue Feb 10 2015 Jeff Ortel <jortel@redhat.com> 2.5.0-1
- AdapterNotFound raised when explicit adapter not found. (jortel@redhat.com)
- NotFound raised amqp node not found. (jortel@redhat.com)
- Add url to Queue/Exchange constructor. (jortel@redhat.com)
- Renamed: route to: address. (jortel@redhat.com)
- Support amqp 1.0; add proton messaging adapter. (jortel@redhat.com)
- Support auto-delete queue expiration. (jortel@redhat.com)
- python-gofer-qpid no longer requires python-qpid-qmf. (jortel@redhat.com)
- Add 2.5 release notes. (jortel@redhat.com)
* Fri Jan 09 2015 Jeff Ortel <jortel@redhat.com> 2.4.0-1
- Better thread pool worker selection. (jortel@redhat.com)
- Fix builtin.Admin.help(). (jortel@redhat.com)
- Add description to InvalidDocument. (jortel@redhat.com)
- Fix TTL. (jortel@redhat.com)
- amqplib adapter removed; heartbeat enabled on qpid connection
  (jortel@redhat.com)
- support configurable broker model management. (jortel@redhat.com)

* Tue Jan 06 2015 Jeff Ortel <jortel@redhat.com> 2.3.0-1
- QPID adapter using QMF. (jortel@redhat.com)
- amqp adapter using epoll. (jortel@redhat.com)
- Support custom exchanges. (jortel@redhat.com)
* Thu Dec 18 2014 Jeff Ortel <jortel@redhat.com> 2.1.0-1
- Fix plugin loading from python path. (jortel@redhat.com)
- Improved adapter model. (jortel@redhat.com)
- Improved builtin plugin. (jortel@redhat.com)
- Get rid of broadcast policy. (jortel@redhat.com)
- Domains added. (jortel@redhat.com)
- The messaging section no longer supported in agent.conf. (jortel@redhat.com)
- Update pmon to retry on notification exception. (jortel@redhat.com)
- Get rid of adapter descriptors. (jortel@redhat.com)
- ModelError raised for all model operations. (jortel@redhat.com)
- Plugin class properties. (jortel@redhat.com)
- Improved test coverage.
* Mon Nov 24 2014 Jeff Ortel <jortel@redhat.com> 2.0.0-1
- The transport concept has been revised and renamed to messaging adapters.
- The transport parameter and configuation deprecated.
- The URL updated to specify the messaging adapter.
- Messaging adapters have descriptors and are loaded much like plugins.
- Better unit test coverage.
- Performance improvements and bug fixes.

* Thu Nov 20 2014 Jeff Ortel <jortel@redhat.com> 1.4.1-1
- Remove ruby lib. (jortel@redhat.com)
- Remove broken ruby dependency. (jortel@redhat.com)

* Mon Nov 03 2014 Jeff Ortel <jortel@redhat.com> 1.4.0-1
- Add reply timestamp. (jortel@redhat.com)
- Fix synchronous policy using durable queue.
  (jortel@redhat.com)
- Add python-amqp transport. (jortel@redhat.com)

* Fri Aug 15 2014 Jeff Ortel <jortel@redhat.com> 1.3.1-1
- 1129828 - split stack traces into separate log records. (jortel@redhat.com)
- Added python-ctypes dependency. (jortel@redhat.com)
- PyPAM replaced with ctypes implementation. (jortel@redhat.com)
- Refactor: add transport Loader; transports loaded and cached when Transport
  is instantiated instead of package import. (jortel@redhat.com)
- Support passing url=None in broker meta-class. (jortel@redhat.com)
* Mon Jun 16 2014 Jeff Ortel <jortel@redhat.com> 1.3.0-1
- Update man page to reference github. (jortel@redhat.com)
- Replace --console option with --foreground and use in systemd unit.
  (jortel@redhat.com)
- systemd support. (jortel@redhat.com)

* Mon Jun 09 2014 Jeff Ortel <jortel@redhat.com> 1.2.1-1
- 1107244 - python 2.4 compat issues. (jortel@redhat.com)
* Thu May 29 2014 Jeff Ortel <jortel@redhat.com> 1.2.0-1
- Add authenticator param to ReplyConsumer constructor. (jortel@redhat.com)
- python 2.4 compat. (jortel@redhat.com)

* Wed May 28 2014 Jeff Ortel <jortel@redhat.com> 1.1.0-1
- Pass original document during auth validation instead of destination uuid.
  (jortel@redhat.com)
- Better support for associating an authenticator with a consumer.
  (jortel@redhat.com)

* Tue May 20 2014 Jeff Ortel <jortel@redhat.com> 1.0.13-1
- Fix setting logging levels in agent.conf. (jortel@redhat.com)
- In the amqplib transport, message durable=True. (jortel@redhat.com)

* Wed May 14 2014 Jeff Ortel <jortel@redhat.com> 1.0.12-1
- 1097732 - broker configured during attach. (jortel@redhat.com)
- Support loading plugins from the PYTHON path. (jortel@redhat.com)
- Support custom plugin naming. (jortel@redhat.com)

* Tue May 06 2014 Jeff Ortel <jortel@redhat.com> 1.0.10-1
- Condition Requires: and import of simplejson. (jortel@redhat.com)
* Fri May 02 2014 Jeff Ortel <jortel@redhat.com> 1.0.9-1
- Fix url syntax for userid:password; get vhost from url path component.
  (jortel@redhat.com)

* Thu May 01 2014 Jeff Ortel <jortel@redhat.com> 1.0.8-1
- Inject inbound_url to support reply when plugin is not found.
  (jortel@redhat.com)
- Pass and store transport by name (instead of object). (jortel@redhat.com)
- Set transport package based on actual packaged. (jortel@redhat.com)
- Declare agent (target) queue in RMI policy send. (jortel@redhat.com)
- Create queues in the consumer instead of the reader. (jortel@redhat.com)

* Tue Apr 22 2014 Jeff Ortel <jortel@redhat.com> 1.0.7-1
- Support extends= in plugin descriptors.  Defines another plugin to extend.
  (jortel@redhat.com)

* Thu Apr 17 2014 Jeff Ortel <jortel@redhat.com> 1.0.6-1
- Inject inbound transport name on request receipt and used to reply when
  unable to route to a plugin. (jortel@redhat.com)
- Trash plugin implements get_url() and get_transport(). (jortel@redhat.com)
- Log when plugin not found and request is trashed. (jortel@redhat.com)
- PathMonitor initialized to prevent initial notification. (jortel@redhat.com)
- Add @initializer decorator and plugin support. (jortel@redhat.com)
- Fix pending message leak when uuid not matched to a plugin.
  (jortel@redhat.com)
* Mon Mar 31 2014 Jeff Ortel <jortel@redhat.com> 1.0.5-1
- Log to syslog instead of /var/log/gofer/. (jortel@redhat.com)
- Support userid/password in the broker url. (jortel@redhat.com)
- Remove librabbitmq transport. (jortel@redhat.com)
- Add support for skipping SSL validation. (jortel@redhat.com)
- Use qpid builtin SSL transport. (jortel@redhat.com)
* Wed Mar 12 2014 Jeff Ortel <jortel@redhat.com> 1.0.4-1
- Improved import between plugins. (jortel@redhat.com)

* Tue Mar 11 2014 Jeff Ortel <jortel@redhat.com> 1.0.3-1
- make queue non-exclusive by default. (jortel@redhat.com)

* Mon Mar 10 2014 Jeff Ortel <jortel@redhat.com> 1.0.2-1
- Log consumed messages. (jortel@redhat.com)

* Mon Mar 10 2014 Jeff Ortel <jortel@redhat.com> 1.0.1-1
- Improved agent logging. (jortel@redhat.com)

* Mon Mar 10 2014 Jeff Ortel <jortel@redhat.com> 1.0.0-1
- Detach before attach and make detach idempotent. (jortel@redhat.com)
- Explicit manual plugin attach; get rid of plugin monitor thread.
  (jortel@redhat.com)
- Support virtual_host and host_validation configuration options.
  (jortel@redhat.com)
- Support userid and password configuration options. (jortel@redhat.com)
- Change envelope/document and Envelope/Document. (jortel@redhat.com)
- Support pluggable message authentication. (jortel@redhat.com)
- Send 'accepted' status when RMI request is added to the pending queue.
  (jortel@redhat.com)
- Send 'rejected' status report when message validation failed.
  (jortel@redhat.com)
- Direct routing by uuid; no more blending of plugin APIs. (jortel@redhat.com)
- Move Admin class from builtin plugin to internal. (jortel@redhat.com)
- Improved pending queue. (jortel@redhat.com)
- Improved thread pool. (jortel@redhat.com)
- Purge unused filter in configuration. (jortel@redhat.com)
- Discontinue support for configuration directives. (jortel@redhat.com)
- Purge mocks in favor of python mock. (jortel@redhat.com)
- Support multiple transports (amqplib, rabbmitmq, python-qpid).
- Discontinue support for deprectated watchdog. (jortel@redhat.com)
- Simplified RMI timeout.  No longer supporting timeout for RMI completion.
  (jortel@redhat.com)
* Tue Jan 14 2014 Jeff Ortel <jortel@redhat.com> 1.0.0-0.1
- default asynchronous timeout to None. (jortel@redhat.com)
  add 'send' as required by transports. (jortel@redhat.com)
- watchdog removed; timeout flows revised. watchdog removed; add 'accepted'
  status; add 'wait' option; redefine timeout option as single integer
  pertaining to the accepted. (jortel@redhat.com)
- Add 'match' criteria operator. (jortel@redhat.com)
- Support plugable transports. (jortel@redhat.com)
* Mon Sep 30 2013 Jeff Ortel <jortel@redhat.com> 0.77-1
- Reduce logging do DEBUG on frequent messaging and RMI processing events.
  (jortel@redhat.com)
* Wed Mar 06 2013 Jeff Ortel <jortel@redhat.com> 0.76-1
- Add support for cancelling RMI; thread pool rewrite; RMI class restructure.
  (jortel@redhat.com)

* Wed Nov 07 2012 Jeff Ortel <jortel@redhat.com> 0.75-1
- policy timeout enhancements. (jortel@redhat.com)
- Fix threadpool leak; change plugin to use simplex pool. (jortel@redhat.com)
- Move threadpool test to unit/ (jortel@redhat.com)
- Add simplex/duplex option to ThreadPool. Fixes memory leak. (jortel@redhat.com)

* Wed Oct 03 2012 Jeff Ortel <jortel@redhat.com> 0.74-1
- Make watchdog journal object configurable; watchdog singleton by URL only.
  (jortel@redhat.com)

* Thu Sep 13 2012 Jeff Ortel <jortel@redhat.com> 0.73-1
- Progress reporting enhancements. (jortel@redhat.com)
- Add for debugging w/o running as root. (jortel@redhat.com)
* Mon Aug 20 2012 Jeff Ortel <jortel@redhat.com> 0.72-1
- Add unit tests: watchdog test. (jortel@redhat.com)
- Add man page for goferd. (jortel@redhat.com)
- Replace BlackList with python set. (jortel@redhat.com)
- Add progress reporting; watchdog enhancements. (jortel@redhat.com)
- remove f15 and add f18 to tito releaser. (jortel@redhat.com)

* Tue Jul 31 2012 Jeff Ortel <jortel@redhat.com> 0.71-1
- Port ruby-gofer to rubygem-qpid. (jortel@redhat.com)
- Make /usr/share/gofer/plugins the primary plugin location. Based on fedora
  packaging guidelines referencing FHS standards. (jortel@redhat.com)
- Discontinue {_libdir} macro for plugins. (jortel@redhat.com)
* Tue Jun 12 2012 Jeff Ortel <jortel@redhat.com> 0.70-1
- Refit mocks for reparent of Envelope & Options to (object).
  (jortel@redhat.com)

* Fri Jun 08 2012 Jeff Ortel <jortel@redhat.com> 0.69-1
- 829767 - fix simplejons 2.2+ issue (fedora 17). Envelope/Options rebased on
  object rather than dict. (jortel@redhat.com)
- Add whiteboard. (jortel@redhat.com)
- Fixed 'Undefined variable (s) in XBindings.__bindings(). (jortel@redhat.com)

* Thu Apr 26 2012 Jeff Ortel <jortel@redhat.com> 0.68-1
- Refit watchdog plugin; set journal location; skip directories in journal dir.
  (jortel@redhat.com)
- Make the watchdog journal directory configurable. (jortel@redhat.com)
- Add Broker.touch() and rename Topic.binding(). (jortel@redhat.com)
- Better support for durable topic subscription.  Queue bindings to specified
  exchanges. (jortel@redhat.com)
* Fri Mar 16 2012 Jeff Ortel <jortel@redhat.com> 0.67-1
- Add (trace) attribute to propagated exceptions. (jortel@redhat.com)
- Add traceback info to propagated exceptions as: Exception.trace.
  (jortel@redhat.com)
- Add support for __getitem__ in container and stub. (jortel@redhat.com)
- Refactor to crypto (delegate) interface. (jortel@redhat.com)
- Support multiple security decorators. (jortel@redhat.com)
- perf: asynchronous ack(); tcp_nodelay. (jortel@redhat.com)
- Rename 'delayed/trigger' policy property to match option. (jortel@redhat.com)
- Rename 'delayed' option to: 'trigger'. (jortel@redhat.com)
- option 'delayed' implies asynchronous RMI. (jortel@redhat.com)
- fix for tito compat. (jortel@redhat.com)
- bridge: clean debug prints; make gateway a thread. (jortel@redhat.com)
- Add tcp bridge (experimental). (jortel@redhat.com)
- Add support for delayed trigger asynchronous RMI. (jortel@redhat.com)
- Add fedora releaser. (jortel@redhat.com)
- support setting producer uuid; HMAC enhancements. (jortel@redhat.com)
- rel-eng: rename redhat releaser. (jortel@redhat.com)

* Tue Feb 21 2012 Jeff Ortel <jortel@redhat.com> 0.66-1
- Add DistGit releaser. (jortel@redhat.com)
- Add deps: python-iniparse; python-hashlib (rhel5). (jortel@redhat.com)

* Fri Feb 03 2012 Jeff Ortel <jortel@redhat.com> 0.65-1
- Initial add of hmac classes; add synchronized decorator. (jortel@redhat.com)
- python 2.4 compat for __import__(). (jortel@redhat.com)
- Enhanced monitoring, use sha256 in addition to mtime. (jortel@redhat.com)
- Add support for dynamic plugin URL in addition to UUID. (jortel@redhat.com)

* Mon Jan 09 2012 Jeff Ortel <jortel@redhat.com> 0.64-1
- Enhanced package (plugin) API. (jortel@redhat.com)
* Wed Nov 30 2011 Jeff Ortel <jortel@redhat.com> 0.63-1
- Mitigate systemd issues on F15. (jortel@redhat.com)

* Wed Nov 30 2011 Jeff Ortel <jortel@redhat.com> 0.62-1
- plugin: package; extra monkey business with yum optparser to support
  INTERACTIVE yum plugins. (jortel@redhat.com)

* Wed Nov 23 2011 Jeff Ortel <jortel@redhat.com> 0.61-1
- mocks: add support for mock constructors. (jortel@redhat.com)
- plugin: package; Fix problem of yum interactive plugins accessing contributed
  options. (jortel@redhat.com)

* Fri Nov 18 2011 Jeff Ortel <jortel@redhat.com> 0.60-1
- plugin: package; revise API for constructors; add Yum wrapper class.
  (jortel@redhat.com)
- Support remote class constructor arguments. (jortel@redhat.com)

* Wed Nov 16 2011 Jeff Ortel <jortel@redhat.com> 0.59-1
- plugin: package; Initialize yum plugins. (jortel@redhat.com)

* Wed Nov 16 2011 Jeff Ortel <jortel@redhat.com> 0.58-1
- Add 'apply' flag on Pacakge.update(); handle obsoletes; better return info.
  (jortel@redhat.com)
- Test commit for SSH key changed. (jortel@redhat.com)
- Better handling of corrupted files in pending store. (jortel@redhat.com)
- Fix bug in non-eager plugin loading. (jortel@redhat.com)

* Thu Nov 10 2011 Jeff Ortel <jortel@redhat.com> 0.57-1
- Impl plugin: System, rename shutdown() to: halt(); add cancel().
  (jortel@redhat.com)

* Thu Nov 10 2011 Jeff Ortel <jortel@redhat.com> 0.56-1
- Impl plugin: Package.update(). (jortel@redhat.com)
- Impl plugin: system.shutdown() & reboot(). (jortel@redhat.com)

* Thu Nov 10 2011 Jeff Ortel <jortel@redhat.com> 0.55-1
- change to 'importkeys' semantics; add importkeys to group installs.
  (jortel@redhat.com)
- Restrict Plugin.export() to class|function; split test agent & plugin.
  (jortel@redhat.com)
- Add tools. (jortel@redhat.com)

* Thu Oct 27 2011 Jeff Ortel <jortel@redhat.com> 0.54-1
- Refactor pmon, separate threading. (jortel@redhat.com)

* Thu Oct 27 2011 Jeff Ortel <jortel@redhat.com> 0.53-1
- Remove testing code in pmon.py left in by mistake. (jortel@redhat.com)

* Thu Oct 27 2011 Jeff Ortel <jortel@redhat.com> 0.52-1
- Add pmon utility. (jortel@redhat.com)

* Fri Oct 21 2011 Jeff Ortel <jortel@redhat.com> 0.51-1
- Better semantics: replace Plugin.__getitem__() w/ Plugin.export().
  (jortel@redhat.com)
- Optional plugins disabled by default. (jortel@redhat.com)
- Provide for plugin inheritance.   - add [loader].eager property   - switched
  to model where disabled plugins loaded but not started to support sharing.
  - add support for plugin load order specified by [main].requires.   - actions
  stored on plugins. (jortel@redhat.com)
- Add the package plugin. (jortel@redhat.com)
- Change system plugin to use subprocess. (jortel@redhat.com)

* Fri Sep 30 2011 Jeff Ortel <jortel@redhat.com> 0.50-1
- Fix epydocs. (jortel@redhat.com)

* Tue Sep 27 2011 Jeff Ortel <jortel@redhat.com> 0.49-3
- Discontinue 'pam' option and just go with user=, password=.
  (jortel@redhat.com)

* Tue Sep 27 2011 Jeff Ortel <jortel@redhat.com> 0.49-2
- mitigate rpmlint perms error on /var/log/gofer. (jortel@redhat.com)

* Tue Sep 27 2011 Jeff Ortel <jortel@redhat.com> 0.49-1
- Reader inject subject into the envelope like Consumer. (jortel@redhat.com)
- Make installed plugins, enabled. (jortel@redhat.com)
- Fix default PAM service. (jortel@redhat.com)
- Fix virt plugin; add libvirt dep. (jortel@redhat.com)
- Organize spec by pacakge/subpackage. (jortel@redhat.com)
- set facl on journal/watchdog. (jortel@redhat.com)
- Add authentication/authorization unit tests. (jortel@redhat.com)
- Finer grained auth exceptions. (jortel@redhat.com)
- package plugins; split shell into system plugin. (jortel@redhat.com)
- Split watchdog and thread objects for better performance. (jortel@redhat.com)
- Create watchdog journal directory on-demand. (jortel@redhat.com)
- Add PyPAM dep; change perms /var/log/gofer/ to 700. (jortel@redhat.com)
- Make default PAM service configurable. (jortel@redhat.com)
- Add PAM authentication and decorators; change Shell.run() to run as
  authenticated user. (jortel@redhat.com)
- FHS guidelines, move the journal back to /var/lib/gofer/journal. See: http://
  www.pathname.com/fhs/pub/fhs-2.3.html#USRSHAREARCHITECTUREINDEPENDENTDATA
  (jortel@redhat.com)

* Tue Sep 13 2011 Jeff Ortel <jortel@redhat.com> 0.48-3
- Fix tito tagging problem. (jortel@redhat.com)

* Tue Sep 13 2011 Jeff Ortel <jortel@redhat.com> 0.48-2
- bump to release: 2. (jortel@redhat.com)
- Move journal to /usr/share; hunt for plugins in path: /usr/lib/gofer/plugins,
  /usr/lib64/gofer/plugins, /opt/gofer/plugins. (jortel@redhat.com)

* Fri Sep 09 2011 Jeff Ortel <jortel@redhat.com> 0.48-1
- Use rpm _var macro; use global instead of define rpm macro; fix perms on
  agent.conf. (jortel@redhat.com)
- Fix builtin.Admin.help(). (jortel@redhat.com)

* Tue Aug 23 2011 Jeff Ortel <jortel@redhat.com> 0.47-1
- Fix macros in changelog. (jortel@redhat.com)
- Fix cp etc/xx replaced with macro my mistake in build section of spec.
  (jortel@redhat.com)
- upload spec file. (jortel@redhat.com)

* Mon Aug 22 2011 Jeff Ortel <jortel@redhat.com> 0.46-1
- Fix duplicate ruby files. (jortel@redhat.com)
- Add /var/log/gofer to %%files. (jortel@redhat.com)
- Fix rpmlink complaints. (jortel@redhat.com)
- Point Source0: at fedorahosted. (jortel@redhat.com)
- Fix rpmlint complaints. (jortel@redhat.com)
- Add LICENSE and reference in %%doc. (jortel@redhat.com)

* Fri Aug 12 2011 Jeff Ortel <jortel@redhat.com> 0.45-1
- ruby: align with python impl. (jortel@redhat.com)
- Rework dispatcher flow. Move most of the RMI modules to a new (rmi) package.
  Dispatch everything to the PendingQueue which has been greatly optimized. Fix
  ThreadPool worker allocation. Add scheduler to process PendingQueue and queue
  messages to appropriate plugin's thread pool. Add TTL processing throughout
  the dispatch flow. Commit individual messages grabbed off the PendingQueue.
  (jortel@redhat.com)

* Wed Aug 03 2011 Jeff Ortel <jortel@redhat.com> 0.44-1
- Fix RHEL (python 2.4) macro. (jortel@redhat.com)
- Add watchdog plugin. (jortel@redhat.com)
- Add journal & watchdog. (jortel@redhat.com)

* Fri Jul 22 2011 Jeff Ortel <jortel@redhat.com> 0.43-1
- Propigate json exception of return and raised exception values back to
  caller. (jortel@redhat.com)
- Fix topic queue leak that causes: Enqueue capacity threshold exceeded on
  queue. (jortel@redhat.com)
- Add atexit hook to close endpoints. (jortel@redhat.com)
- Fix epydocs. (jortel@redhat.com)

* Wed Jun 22 2011 Jeff Ortel <jortel@redhat.com> 0.42-1
- Simplified thread pool. (jortel@redhat.com)

* Thu Jun 16 2011 Jeff Ortel <jortel@redhat.com> 0.41-1
- python-qpid 0.10 API compat. Specifically on EL6, the Transport.__init__()
  constructor/factory gets called with (con, host, port) instead of (host,
  port) in < 0.10. The 0.10 in F14 still called with (host, port).
  (jortel@redhat.com)

* Thu Jun 16 2011 Jeff Ortel <jortel@redhat.com> 0.40-1
- License as: LGPLv2. (jortel@redhat.com)

* Tue Jun 14 2011 Jeff Ortel <jortel@redhat.com> 0.39-1
- Increase logging in policy. (jortel@redhat.com)
- Add session pool & fix receiver leak in policy. (jortel@redhat.com)
- Testing: enhanced thread pool testing. (jortel@redhat.com)

* Fri May 27 2011 Jeff Ortel <jortel@redhat.com> 0.38-1
- Skip comments when processing config macros. (jortel@redhat.com)
- Queue exceptions caught in the threadpool. (jortel@redhat.com)

* Fri May 13 2011 Jeff Ortel <jortel@redhat.com> 0.37-1
- Fix broker singleton lookup. (jortel@redhat.com)
- Mock call object enhancements. (jortel@redhat.com)

* Mon May 09 2011 Jeff Ortel <jortel@redhat.com> 0.36-1
- Stop receiver thread before closing session. (jortel@redhat.com)
* Tue May 03 2011 Jeff Ortel <jortel@redhat.com> 0.35-1
- Additional concurrency protection; move qpid receiver to ReceiverThread.
  (jortel@redhat.com)
- python 2.4 compat: Queue. (jortel@redhat.com)

* Mon May 02 2011 Jeff Ortel <jortel@redhat.com> 0.34-1
- More robust (receiver) management. (jortel@redhat.com)
- Support getting a list of all mock agent (proxies). (jortel@redhat.com)
- proxy.Agent deprecated. (jortel@redhat.com)
- close() called by __del__() can have AttributeError when consumer never
  started. (jortel@redhat.com)
- Provide means to detect number of proxies. (jortel@redhat.com)
- Singleton enhancements. (jortel@redhat.com)
- Move url translated into producer to proxy.Agent. (jortel@redhat.com)
- add mock.reset(). (jortel@redhat.com)
- Revised and simplified mocks. (jortel@redhat.com)

* Wed Apr 20 2011 Jeff Ortel <jortel@redhat.com> 0.33-1
- Mock history enhancements. (jortel@redhat.com)
- support 'threads' in agent.conf. (jortel@redhat.com)

* Wed Apr 13 2011 Jeff Ortel <jortel@redhat.com> 0.32-1
- Add messaging.theads (cfg) property. (jortel@redhat.com)
- Add support for concurrent RMI dispatching. (jortel@redhat.com)

* Mon Apr 11 2011 Jeff Ortel <jortel@redhat.com> 0.31-1
- Default timeout in specific policies. (jortel@redhat.com)
- Manage invocation policy in stub instead of agent proxy. This provides for
  timeout, async and other flags to be passed in stub constructor.
  (jortel@redhat.com)

* Mon Apr 11 2011 Jeff Ortel <jortel@redhat.com> 0.30-1
- Fix @import of whole sections on machines w/ old versions of iniparse.
  (jortel@redhat.com)

* Wed Apr 06 2011 Jeff Ortel <jortel@redhat.com> 0.29-1
- Refactor mocks; fix NotPermitted. (jortel@redhat.com)
- Mock enhancements. (jortel@redhat.com)
- Fix lockfile. (jortel@redhat.com)
- Stop logging shared secret at INFO. (jortel@redhat.com)

* Wed Mar 30 2011 Jeff Ortel <jortel@redhat.com> 0.28-1
- plugin descriptor & qpid error handling. (jortel@redhat.com)

* Mon Mar 28 2011 Jeff Ortel <jortel@redhat.com> 0.27-1
- Change to yappi profiler. (jortel@redhat.com)
- factor Reader.__fetch() and catch/log fetch exceptions. (jortel@redhat.com)
- Add missing import sleep(). (jortel@redhat.com)

* Thu Mar 24 2011 Jeff Ortel <jortel@redhat.com> 0.26-1
- close sender, huge performance gain. (jortel@redhat.com)
- Add stub Factory. (jortel@redhat.com)

* Tue Mar 22 2011 Jeff Ortel <jortel@redhat.com> 0.25-1
- Use {el5} macro. (jortel@redhat.com)
- Reduce log clutter. (jortel@redhat.com)

* Fri Mar 18 2011 Jeff Ortel <jortel@redhat.com> 0.24-1
- Update secret in options epydoc; fix options override in stub().
  (jortel@redhat.com)
- Add code profiling option. (jortel@redhat.com)
- Add mutex to Broker. (jortel@redhat.com)

* Fri Mar 11 2011 Jeff Ortel <jortel@redhat.com> 0.23-1
- Change receiver READY message to debug. (jortel@redhat.com)

* Fri Mar 11 2011 Jeff Ortel <jortel@redhat.com> 0.22-1
- Change message send/recv to DEBUG. (jortel@redhat.com)

* Fri Mar 11 2011 Jeff Ortel <jortel@redhat.com> 0.21-1
- URL not defined in builtin & main configurations. (jortel@redhat.com)
- Test action every 36 hours. (jortel@redhat.com)
- Start plugin monitor only when URL defined. (jortel@redhat.com)
- Make references to properties on undefined sections safe. (jortel@redhat.com)

* Wed Feb 16 2011 Jeff Ortel <jortel@redhat.com> 0.20-1
- shared in remote decorator may be callable. (jortel@redhat.com)
- Update @remote to support (shared,secret). shared = (0|1): indicates method
  may be shared with other plugins   and called via other uuid's. secret =
  (None, str): A shared secret that must be presented by   the caller and
  included in the RMI request for authentication. The defaults (shared=1,
  secret=None). (jortel@redhat.com)

* Thu Feb 10 2011 Jeff Ortel <jortel@redhat.com> 0.19-1
- ruby: ruby & c++ API expect ttl as miliseconds. (jortel@redhat.com)
- ruby: make non-durable queues auto_delete; make all queues exclusive.
  (jortel@redhat.com)

* Wed Feb 09 2011 Jeff Ortel <jortel@redhat.com> 0.18-1
- Make sure plugins directory exists. (jortel@redhat.com)
- Make file paths portable; fix usage. (jortel@redhat.com)

* Wed Feb 02 2011 Jeff Ortel <jortel@redhat.com> 0.17-1
- Add Obsoletes: gofer-lib. (jortel@redhat.com)
- ruby: Move url/producer options handling to Container. (jortel@redhat.com)
- ruby: replace (puts) with logging. (jortel@redhat.com)

* Tue Feb 01 2011 Jeff Ortel <jortel@redhat.com> 0.16-1
- Fix build requires. (jortel@redhat.com)

* Mon Jan 31 2011 Jeff Ortel <jortel@redhat.com> 0.15-1
- ruby: symbolize JSON key names; Fix proxy constructor. (jortel@redhat.com)
- Add timeout support using Timeout since ruby-qpid does not support
  Queue.get() w/ timeout arg. (jortel@redhat.com)
- Replace stub() method w/ StubFactory(). (jortel@redhat.com)
- Add keyword (options) to Stub pseudo constructor. Supports Eg: dog =
  agent.Dog(window=mywin, any=100). Update async test to use ctag = XYZ.
  (jortel@redhat.com)
- Fix & simplify inherited messaging properties. Name ReplyConsumer properly.
  (jortel@redhat.com)
- Add ruby packaging. (jortel@redhat.com)
- Make messaging completely centric. * Add [messaging] section to plugin
  descriptor. * Remove messaging.enabled property. * Refactor plugin monitor
  thread to be 1 thread/plugin. * Clean up decorated /Remote/ functions when
  plugin fails to load. (jortel@redhat.com)
- Add ruby (client) API bindings. (jortel@redhat.com)

* Thu Jan 20 2011 Jeff Ortel <jortel@redhat.com> 0.14-1
- Fix conditional for pkgs required on RHEL. (jortel@redhat.com)

* Wed Jan 12 2011 Jeff Ortel <jortel@redhat.com> 0.13-1
- Make Broker a smart singleton. (jortel@redhat.com)
- py 2.4 compat: replace @singleton class decorator with __metaclass__
  Singleton. (jortel@redhat.com)
- Log dispatch exceptions. (jortel@redhat.com)

* Wed Jan 05 2011 Jeff Ortel <jortel@redhat.com> 0.12-1
- Adjust sleep times & correct log messages. (jortel@redhat.com)
- Make logging (level) configurable. (jortel@redhat.com)
- Remove @identity decorator. (jortel@redhat.com)

* Tue Jan 04 2011 Jeff Ortel <jortel@redhat.com> 0.11-1
- Quiet logged Endpoint.close() not checking for already closed.
  (jortel@redhat.com)
- Replace builtin variables with macros (format=%%{macro}). (jortel@redhat.com)
- make Config a singleton; Make PluginDescriptor a 'Base' config.
  (jortel@redhat.com)
- Add support for @import directive. (jortel@redhat.com)
- The server test needs to use the correct uuid. (jortel@redhat.com)

* Wed Dec 15 2010 Jeff Ortel <jortel@redhat.com> 0.10-1
- session.stop() not supported in python-qpid 0.7. (jortel@redhat.com)
- Remove unused catch. (jortel@redhat.com)
- Make worker threads daemons. (jortel@redhat.com)

* Mon Dec 13 2010 Jeff Ortel <jortel@redhat.com> 0.9-1
- Set AMQP message TTL=timeout for synchronous RMI. (jortel@redhat.com)

* Thu Dec 09 2010 Jeff Ortel <jortel@redhat.com> 0.8-1
- Fix RHEL requires. (jortel@redhat.com)
- Enable module (level) access to plugin descriptor (conf). (jortel@redhat.com)

* Wed Dec 08 2010 Jeff Ortel <jortel@redhat.com> 0.7-1
- Support timeout as tuple. (jortel@redhat.com)
- Enhanced exception propagation. (jortel@redhat.com)
- Fix testings. (jortel@redhat.com)

* Fri Dec 03 2010 Jeff Ortel <jortel@redhat.com> 0.6-1
- Reverse presidence of uuid: plugin descriptor now overrides @identity
  function/method. (jortel@redhat.com)

* Thu Dec 02 2010 Jeff Ortel <jortel@redhat.com> 0.5-1
- python 2.4 (& RHEL 5) compatibility. (jortel@redhat.com)

* Thu Dec 02 2010 Jeff Ortel <jortel@redhat.com> 0.4-1
- Modify builtin (generated) uuid to be persistent. (jortel@redhat.com)
- Use hostname for 'builtin' plugin's uuid. Use the hostname unless it is non-
  unique such as 'localhost' or 'localhost.localdomain'. (jortel@redhat.com)

* Thu Dec 02 2010 Jeff Ortel <jortel@redhat.com> 0.3-1
- Set 'builtin' plugin back to uuid=123. (jortel@redhat.com)
- Re-specify exclusive queue subscription; filter plugin descriptors by ext.
  (jortel@redhat.com)
- Add support for each plugin to specify a messaging consumer (uuid).
  (jortel@redhat.com)
- Rename builtin AgentAdmin to just Admin. (jortel@redhat.com)
- Replace class decorators for python 2.4 compat. (jortel@redhat.com)
- Fix cvs tags. (jortel@redhat.com)
- Automatic commit of package [gofer] release [0.2-1]. (jortel@redhat.com)
- Add brew build informaton. (jortel@redhat.com)

* Fri Nov 19 2010 Jeff Ortel <jortel@redhat.com> 0.2-1
- Add brew build informaton. (jortel@redhat.com)
- Fix test. (jortel@redhat.com)

* Mon Nov 08 2010 Jeff Ortel <jortel@redhat.com> 0.1-1
- new package built with tito

* Thu Sep 30 2010 Jeff Ortel <jortel@redhat.com> 0.1-1
- 0.1
