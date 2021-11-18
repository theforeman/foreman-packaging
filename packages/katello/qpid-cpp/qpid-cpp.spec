# Define pkgdocdir for releases that don't define it already
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

# We ship a .pc file but don't need to depend on pkg-config
%global __requires_exclude pkg-config
%global __provides_exclude_from ^(%{python2_sitearch}/.*\\.so|%{_libdir}/.libqmf*)$
%global proton_min_ver 0.31.0

Name:          qpid-cpp
Version:       1.39.0
Release:       7%{?dist}
Summary:       Libraries for Qpid C++ client applications
License:       ASL 2.0
URL:           http://qpid.apache.org

Source0:       http://www.apache.org/dist/qpid/cpp/%{version}/%{name}-%{version}.tar.gz
Patch0:        amq.patch
Source1:       licenses.xml

%global _pkglicensedir %{_licensedir}/%{name}-%{version}
%{!?_licensedir:%global license %doc}
%{!?_licensedir:%global _pkglicensedir %{_pkgdocdir}}

ExcludeArch:   ppc s390
BuildRequires: boost-devel
BuildRequires: boost-filesystem
BuildRequires: boost-program-options
BuildRequires: cmake
BuildRequires: cyrus-sasl
BuildRequires: cyrus-sasl-devel
BuildRequires: cyrus-sasl-lib
BuildRequires: doxygen
BuildRequires: gcc-c++
BuildRequires: libaio-devel
BuildRequires: libdb-cxx-devel
%ifnarch s390 s390x
BuildRequires: libibverbs-devel
BuildRequires: librdmacm-devel
%endif
BuildRequires: libuuid-devel
BuildRequires: make
BuildRequires: nspr-devel
BuildRequires: nss-devel
BuildRequires: pkgconfig
BuildRequires: python2
BuildRequires: python2-devel
BuildRequires: python2-setuptools
BuildRequires: qpid-proton-c-devel >= %{proton_min_ver}
BuildRequires: ruby
BuildRequires: ruby-devel
BuildRequires: swig

%description

Run-time libraries for AMQP client applications developed using Qpid
C++. Clients exchange messages with an AMQP message broker using
the AMQP protocol.


%package client
Summary:   Libraries for Qpid C++ client applications
Obsoletes: %{name}-client-ssl

Requires:  boost-filesystem
Requires:  boost-program-options
Requires:  boost-system
Requires:  qpid-proton-c%{?_isa} >= %{proton_min_ver}

%if (0%{?rhel} && 0%{?rhel} < 7)
Requires:  initscripts
Requires(post):/sbin/chkconfig
Requires(preun):/sbin/chkconfig
Requires(preun):/sbin/service
Requires(postun):/sbin/service
%endif

%description client
Run-time libraries for AMQP client applications developed using Qpid
C++. Clients exchange messages with an AMQP message broker using
the AMQP protocol.

%files client
%defattr(-,root,root,-)
%license %{_pkglicensedir}/LICENSE.txt
%license %{_pkglicensedir}/licenses.xml
%doc NOTICE.txt
%doc README.md
%doc INSTALL.txt
%{_libdir}/libqpidcommon.so.*
%{_libdir}/libqpidclient.so.*
%{_libdir}/libqpidtypes.so.*
%{_libdir}/libqpidmessaging.so.*
%dir %{_libdir}/qpid
%ifnarch s390 s390x
%dir %{_libdir}/qpid/client
%exclude %{_libdir}/qpid/client/rdmaconnector.so*
%endif
%dir %{_sysconfdir}/qpid
%config(noreplace) %{_sysconfdir}/qpid/qpidc.conf

%post client -p /sbin/ldconfig

%postun client -p /sbin/ldconfig


%package client-devel
Summary:   Header files, documentation and testing tools for developing Qpid C++ clients
Requires:  %{name}-client = %{version}-%{release}
Requires:  boost-devel
Requires:  boost-filesystem
Requires:  boost-program-options
Requires:  libuuid-devel
Requires:  python2

%description client-devel
Libraries and header files for developing AMQP clients in C++ using Qpid.
Qpid implements the AMQP messaging specification.

%files client-devel
%defattr(-,root,root,-)
%dir %{_includedir}/qpid
%{_includedir}/qpid/*.h
%{_includedir}/qpid/qpid.i
%{_includedir}/qpid/swig_perl_typemaps.i
%{_includedir}/qpid/swig_python_typemaps.i
%{_includedir}/qpid/swig_ruby_typemaps.i
%{_includedir}/qpid/client
%{_includedir}/qpid/framing
%{_includedir}/qpid/sys
%{_includedir}/qpid/messaging
%{_includedir}/qpid/types
%{_libdir}/libqpidcommon.so
%{_libdir}/libqpidclient.so
%{_libdir}/libqpidtypes.so
%{_libdir}/libqpidmessaging.so
%{_libdir}/pkgconfig/qpid.pc
%{_libdir}/cmake/Qpid/QpidConfig.cmake
%{_libdir}/cmake/Qpid/QpidConfigVersion.cmake
%{_datadir}/qpid/examples/README.txt
%{_datadir}/qpid/examples/messaging
%defattr(755,root,root,-)
%{_libexecdir}/qpid/tests/qpid-perftest
%{_libexecdir}/qpid/tests/qpid-topic-listener
%{_libexecdir}/qpid/tests/qpid-topic-publisher
%{_libexecdir}/qpid/tests/qpid-latency-test
%{_libexecdir}/qpid/tests/qpid-client-test
%{_libexecdir}/qpid/tests/qpid-txtest
%{_libexecdir}/qpid/tests/qpid-ping
%{_libexecdir}/qpid/tests/qpid-txtest2
%{_libexecdir}/qpid/tests/receiver
%{_libexecdir}/qpid/tests/sender
%{_bindir}/qpid-send
%{_bindir}/qpid-receive

%post client-devel -p /sbin/ldconfig

%postun client-devel -p /sbin/ldconfig


%package client-docs
Summary:   AMQP client development documentation
BuildArch: noarch
Obsoletes: %{name}-client-devel-docs

%description client-docs
This package includes the AMQP clients development documentation in HTML
format for easy browsing.

%files client-docs
%defattr(-,root,root,-)
%doc %{_pkgdocdir}
%license %{_pkglicensedir}/LICENSE.txt
%license %{_pkglicensedir}/licenses.xml


%package server
Summary:   An AMQP message broker daemon
Requires:  %{name}-client = %{version}-%{release}
Requires:  cyrus-sasl
Requires:  qpid-proton-c%{?_isa} >= %{proton_min_ver}
%if 0%{?rhel} && 0%{?rhel} >= 7
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
%endif
Obsoletes: %{name}-server-ssl
Obsoletes: %{name}-server-devel

%description server
A message broker daemon that receives stores and routes messages using
the open AMQP messaging protocol.

%files server
%defattr(-,root,root,-)
%{_libdir}/libqpidbroker.so*
%{_sbindir}/qpidd
%if 0%{?rhel} && 0%{?rhel} >= 7
%{_unitdir}/qpidd.service
%else
%{_initrddir}/qpidd
%endif
%config(noreplace) %{_sysconfdir}/qpid/qpidd.conf
%config(noreplace) %{_sysconfdir}/sasl2/qpidd.conf
%dir %{_libdir}/qpid/daemon
%{_libdir}/qpid/daemon/amqp.so
%attr(755, qpidd, qpidd) %dir %{_localstatedir}/lib/qpidd
%attr(755, qpidd, qpidd) %dir %{_localstatedir}/run/qpidd
%doc %{_mandir}/man1/*

%pre server
# Only needed for Fedora & Epel builds
rm -fr /var/run/qpidd
#
getent group qpidd >/dev/null || groupadd -r qpidd
getent passwd qpidd >/dev/null || \
  useradd -r -M -g qpidd -d %{_localstatedir}/lib/qpidd -s /sbin/nologin \
    -c "Owner of Qpidd Daemons" qpidd
exit 0

%post server
%if (0%{?rhel} && 0%{?rhel} < 7)
# This adds the proper /etc/rc*.d links for the script
/sbin/chkconfig --add qpidd
/sbin/ldconfig
%else
%systemd_post qpidd.service
%endif

%preun server
%if (0%{?rhel} && 0%{?rhel} < 7)
# Check that this is actual deinstallation, not just removing for upgrade.
if [ $1 = 0 ]; then
  /sbin/service qpidd stop >/dev/null 2>&1 || :
  /sbin/chkconfig --del qpidd
fi
%else
%systemd_preun qpidd.service
%endif

%postun server
%if (0%{?rhel} && 0%{?rhel} < 7)
if [ "$1" -ge "1" ]; then
  /sbin/service qpidd condrestart >/dev/null 2>&1 || :
fi
%else
%systemd_postun_with_restart qpidd.service
%endif
/sbin/ldconfig


%package server-ha
Summary: Provides extensions to the AMQP message broker to provide high availability
Requires: %{name}-server = %{version}-%{release}
Requires: %{name}-client = %{version}-%{release}
Obsoletes: %{name}-server-cluster

%if 0%{?rhel} && 0%{?rhel} >= 7
# for systemd
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units
%endif

%description server-ha
%{summary}.

%files server-ha
%defattr(-,root,root,-)
%if 0%{?rhel} && 0%{?rhel} >= 7
%{_unitdir}/qpidd-primary.service
%else
%{_initrddir}/qpidd-primary
%endif
%{_libdir}/qpid/daemon/ha.so

%post server-ha
%if 0%{?rhel} && 0%{?rhel} >= 7
%systemd_post qpidd-primary.service
%else
/sbin/chkconfig --add qpidd-primary
%endif
/sbin/ldconfig

%preun server-ha
%if 0%{?rhel} && 0%{?rhel} >= 7
%systemd_preun qpidd-primary.service
%else
if [ $1 = 0 ]; then
  /sbin/service qpidd-primary stop > /dev/null 2>&1 || :
  /sbin/chkconfig --del qpidd-primary
fi
%endif

%postun server-ha
%if 0%{?rhel} && 0%{?rhel} >= 7
%systemd_postun_with_restart qpidd-primary.service
%else
if [ $1 -ge 1 ]; then
  /sbin/service qpidd-primary condrestart >/dev/null 2>&1 || :
fi
%endif
/sbin/ldconfig


%ifnarch s390 s390x
%package client-rdma
Summary:  RDMA Protocol support (including Infiniband) for Qpid clients
Requires: %{name}-client = %{version}-%{release}

%description client-rdma
A client plugin and support library to support RDMA protocols (including
Infiniband) as the transport for Qpid messaging.

%files client-rdma
%defattr(-,root,root,-)
%{_libdir}/librdmawrap.so*
%{_libdir}/qpid/client/rdmaconnector.so*
%config(noreplace) %{_sysconfdir}/qpid/qpidc.conf

%post client-rdma -p /sbin/ldconfig

%postun client-rdma -p /sbin/ldconfig


%package server-rdma
Summary:   RDMA Protocol support (including Infiniband) for the Qpid daemon
Requires: %{name}-server = %{version}-%{release}
Requires: %{name}-client = %{version}-%{release}
Requires: %{name}-client-rdma = %{version}-%{release}

%description server-rdma
A Qpid daemon plugin to support RDMA protocols (including Infiniband) as the
transport for AMQP messaging.

%files server-rdma
%defattr(-,root,root,-)
%{_libdir}/qpid/daemon/rdma.so

%post server-rdma -p /sbin/ldconfig

%postun server-rdma -p /sbin/ldconfig
%endif


%package server-linearstore
Summary: Red Hat persistence extension to the Qpid messaging sytem
Requires: %{name}-server = %{version}-%{release}
Requires: %{name}-client = %{version}-%{release}
Requires: libdb
Requires: libaio
Obsoletes: %{name}-server-store
Conflicts: %{name}-server-store

%description server-linearstore
Red Hat persistence extension to the Qpid AMQP broker: persistent message
storage using a libaio-based asynchronous journal.

%files server-linearstore
%defattr(-,root,root,-)
%{_libdir}/qpid/daemon/linearstore.so
%{_libdir}/liblinearstoreutils.so

%post server-linearstore -p /sbin/ldconfig
%postun server-linearstore -p /sbin/ldconfig


%package -n qpid-tools
Summary:  Management and diagostic tools for Apache Qpid
BuildArch: noarch

Requires:  python2-qpid
Requires:  python2-qpid-qmf = %{version}-%{release}

%description -n qpid-tools
Management and diagnostic tools for Apache Qpid brokers and clients.

%files -n qpid-tools
%{_bindir}/qpid-config
%{_bindir}/qpid-ha
%{_bindir}/qpid-printevents
%{_bindir}/qpid-queue-stats
%{_bindir}/qpid-route
%{_bindir}/qpid-stat
%{_bindir}/qpid-tool
%{python2_sitelib}/qpidtoollibs
%{_libexecdir}/qpid-qls-analyze
%dir %{_datadir}/qpid-tools
%dir %{_datadir}/qpid-tools/python
%{_datadir}/qpid-tools/python/qlslibs
%{python2_sitelib}/qpid_tools-*.egg-info


%package -n qpid-qmf
Summary: The QPID Management Framework
Requires:  qpid-cpp-client%{?_isa} = %{version}-%{release}

%description -n qpid-qmf
The Qpid Management Framework is a general-purpose management bus built on Qpid
messaging. It takes advantage of the scalability, security, and rich
capabilities of Qpid to provide flexible and easy-to-use manageability to a
large set of applications.

%files -n qpid-qmf
%{_libdir}/libqmf2.so.*

%post -n qpid-qmf -p /sbin/ldconfig

%postun -n qpid-qmf -p /sbin/ldconfig


%package -n qpid-qmf-devel
Summary:   Header files and tools for developing QMF extensions
Requires:  qpid-qmf%{?_isa} = %{version}-%{release}
Requires:  qpid-cpp-client-devel%{?_isa} = %{version}-%{release}

%description -n qpid-qmf-devel
Header files and code-generation tools needed for developers of QMF-managed
components.

%files -n qpid-qmf-devel
%{_includedir}/qmf
%{_libdir}/libqmf2.so
%{_bindir}/qmf-gen
%{python2_sitelib}/qmfgen
%{_libdir}/pkgconfig/qmf2.pc

%post -n qpid-qmf-devel -p /sbin/ldconfig

%postun -n qpid-qmf-devel -p /sbin/ldconfig


%package -n python2-qpid-qmf
Summary:   The QPID Management Framework bindings for python
Requires:  qpid-qmf%{?_isa} = %{version}-%{release}
Requires:  %{name}-client%{?_isa} = %{version}-%{release}

%description -n python2-qpid-qmf
An extensible management framework layered on QPID messaging, bindings
for python.

%files -n python2-qpid-qmf
%{python2_sitelib}/qmf

%post -n python2-qpid-qmf -p /sbin/ldconfig

%postun -n python2-qpid-qmf -p /sbin/ldconfig


%prep
%setup -q -n qpid-cpp-%{version}

%patch0 -p1

%build

export RHEL_ALLOW_PYTHON2_FOR_BUILD=1

CXX11FLAG="-std=c++11"

%if (0%{?rhel} && 0%{?rhel} <= 6)
CXX11FLAG="-w -std=c++0x"
%endif

export ADDFLAGS=""
%cmake -DDOC_INSTALL_DIR:PATH=%{_pkgdocdir} \
       -DBUILD_LEGACYSTORE=false \
       -DBUILD_LINEARSTORE=true \
       -DBUILD_BINDING_RUBY=false \
       "-DCMAKE_CXX_FLAGS=$CXXFLAGS $CXX11FLAG $ADDFLAGS" \
       .
make %{?_smp_mflags}
make docs-user-api

%install
export RHEL_ALLOW_PYTHON2_FOR_BUILD=1
rm -rf %{buildroot}

pushd management/python
%{__python2} setup.py install \
    --install-purelib %{python2_sitelib} \
    --root %{buildroot}
popd

chmod +x %{buildroot}/%{python2_sitelib}/qpidtoollibs/disp.py
mkdir -p -m0755 %{buildroot}/%{_bindir}
mkdir -p -m0755 %{buildroot}/%{_unitdir}

%make_install

# enable auth by default
echo "auth=yes" >> %{buildroot}/etc/qpid/qpidd.conf

# change tp python2
sed -i.original 's/!\/usr\/bin\/env python/!\/usr\/bin\/env python2/' %{buildroot}%{_libexecdir}/qpid-qls-analyze
sed -i.original 's/!\/usr\/bin\/env python/!\/usr\/bin\/env python2/' %{buildroot}%{python2_sitelib}/qpidtoollibs/disp.py
sed -i.original 's/!\/usr\/bin\/env python/!\/usr\/bin\/env python2/' %{buildroot}%{_bindir}/qmf-gen
rm -f %{buildroot}%{_libexecdir}/qpid-qls-analyze.original
rm -f %{buildroot}%{python2_sitelib}/qpidtoollibs/disp.py.original
rm -f %{buildroot}%{_bindir}/qmf-gen.original

# install systemd files
mkdir -p %{buildroot}/%{_unitdir}
install -pm 644 %{_builddir}/qpid-cpp-%{version}/etc/fedora/qpidd.service \
    %{buildroot}/%{_unitdir}
install -pm 644 %{_builddir}/qpid-cpp-%{version}/etc/fedora/qpidd-primary.service \
    %{buildroot}/%{_unitdir}

install -d -m0755 %{buildroot}%{_localstatedir}/lib/qpidd
install -d -m0755 %{buildroot}%_libdir/qpid
install -d -m0755 %{buildroot}/var/run/qpidd

rm -f %{buildroot}/%{_initrddir}/qpidd*
rm -f %{buildroot}/%{_libdir}/qpid/daemon/store.so*

install -dm 755 %{buildroot}%{_pkglicensedir}
install -pm 644 %{SOURCE1} %{buildroot}%{_pkglicensedir}
install -pm 644 %{buildroot}%{_pkgdocdir}/LICENSE.txt %{buildroot}%{_pkglicensedir}
rm -f %{buildroot}%{_pkgdocdir}/LICENSE.txt

# clean up leftover ruby files
rm -rf %{buildroot}/usr/local/%{_lib}/ruby/site_ruby

# clean up rhel build
rm -f  %{buildroot}/%{python2_sitearch}/_qpid_messaging.so
rm -f  %{buildroot}/%{python2_sitearch}/qpid_messaging.py*
# These bits will be build if perl-devel package is installed
rm -fr %{buildroot}%_libdir/perl5
# Remove windows files
rm -fr %{buildroot}/%{_bindir}/*.bat

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%changelog
* Fri Mar 19 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.39.0-7
- Do not build qpid_messaging Ruby binding

* Tue Oct 20 2020 Mike Cressman <mcressma@redhat.com> - 1.39.0-6
- add client fixes that are missing from RHEL-8 (which is based on 1.39.0)
  - Bug 1618908 - client memory leak when attaching to an unreachable broker address
  - Bug 1663609 - fix CLOSE_WAIT leak in qpid-cpp-client when trying to reconnect over unreliable network
  - Bug 1687401/1663609 - close socket before calling socketClosed callback (fix sporadic crash)
  - Bug 1857205,QPID-8453 - fix boundary test between map8 and map32 encodings for AMQP 1.0 messages

* Mon May  4 2020 Irina Boverman <iboverma@redhat.com> - 1.39.0-5
- Rebuilt against qpid-proton 0.31.0

* Thu Aug 15 2019 Irina Boverman <iboverma@redhat.com> - 1.39.0-4
- Rebuilt against qpid-proton 0.29.0
- Added fix for QPID-8320 (Fix-for-empty-journal-file-leak-when-linea)

* Wed May  8 2019 Irina Boverman <iboverma@redhat.com> - 1.39.0-3
- Rebuilt against qpid-proton 0.28.0

* Thu Feb  7 2019 Irina Boverman <iboverma@redhat.com> - 1.39.0-2
- Rebuilt against qpid-proton 0.27.0

* Fri Nov 16 2018 Irina Boverman <iboverma@redhat.com> - 1.39.0-1
- Rebased to 1.39.0
- Initial build for RHEL 8

* Mon Oct  8 2018 Irina Boverman <iboverma@redhat.com> - 1.36.0-18
- Rebuilt against qpid-proton 0.26.0

* Thu Sep 13 2018 Irina Boverman <iboverma@redhat.com> - 1.36.0-17
- Rebuilt against qpid-proton 0.25.0
- Updated patch to sync with qpid-cpp-1.36.0-20

* Mon Jul  2 2018 Irina Boverman <iboverma@redhat.com> - 1.36.0-16
- Rebuilt against qpid-proton 0.24.0

* Wed Jun  6 2018 Irina Boverman <iboverma@redhat.com> - 1.36.0-15
- Rebuilt against qpid-proton 0.23.0

* Mon Apr  2 2018 Irina Boverman <iboverma@redhat.com> - 1.36.0-14
- Rebuilt against qpid-proton 0.22.0

* Mon Mar  5 2018 Irina Boverman <iboverma@redhat.com> - 1.36.0-13
- Rebuilt against qpid-proton 0.21.0

* Tue Jan 30 2018 Irina Boverman <iboverma@redhat.com> - 1.36.0-12
- Rebuilt against qpid-proton 0.20.0

* Mon Oct  2 2017 Irina Boverman <iboverma@redhat.com> - 1.36.0-11
- QPID-7895 - fix another race condition in flush timer

* Wed Sep 27 2017 Irina Boverman <iboverma@redhat.com> - 1.36.0-10
- Added licenses.xml file
- Changed location of license files to use %license for RHEL 7
- Added QPID-7929 fix

* Fri Sep 15 2017 Irina Boverman <iboverma@redhat.com> - 1.36.0-9
- Rebased to 1.36.0 (patches match 1.36.0-9 for mrg)
- Rebuilt against qpid-proton 0.18.0 snapshot/commit c6d086

* Mon Jan  9 2017 Irina Boverman <iboverma@redhat.com> - 1.35.0-4
- Removed perl5 files (when perl-devel package is installed), per
  ENTMQCL-460

* Fri Dec  9 2016 Irina Boverman <iboverma@redhat.com> - 1.35.0-1
- Consolidated changes for other distribution
- Removed qpid-cpp-server-devel
- Renamed qpid-cpp-client-devel-docs to qpid-cpp-client-docs
