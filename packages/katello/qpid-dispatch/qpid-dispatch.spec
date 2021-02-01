# Define pkgdocdir for releases that don't define it already
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

# determine whether to install systemd or sysvinit scripts
%if 0%{?fedora} || 0%{?rhel} >= 7

%global _use_sysvinit 0
%global _use_systemd 1

%else

%global _use_sysvinit 1
%global _use_systemd 0

%endif

%global proton_minimum_version 0.31.0
%global libwebsockets_minimum_version 2.4.2

%undefine __brp_mangle_shebangs

Name:          qpid-dispatch
Version:       1.14.0
Release:       1%{?dist}
Summary:       Dispatch router for Qpid
License:       ASL 2.0
URL:           http://qpid.apache.org/
Source0:       http://www.apache.org/dist/qpid/dispatch/%{version}/qpid-dispatch-%{version}.tar.gz

Source2:       licenses.xml
Source3:       qpid-dispatch-console-%{version}.tar.gz
Source4:       config.json

%global _pkglicensedir %{_licensedir}/%{name}-%{version}
%{!?_licensedir:%global license %doc}
%{!?_licensedir:%global _pkglicensedir %{_pkgdocdir}}

%if 0%{?rhel} && 0%{?rhel} >= 7
ExcludeArch: i686
%endif

%if 0%{?rhel} && 0%{?rhel} <= 6
Source1:       docs-%{version}-1.tar.gz
%endif

#Patch3:        dispatch.patch
Patch4:        console-listener.patch

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: cmake
BuildRequires: qpid-proton-c-devel >= %{proton_minimum_version}
BuildRequires: python3-devel
BuildRequires: cmake
BuildRequires: python3-qpid-proton >= %{proton_minimum_version}
BuildRequires: openssl-devel
BuildRequires: libwebsockets-devel >= %{libwebsockets_minimum_version}

# Missing dependency on RHEL 6: asciidoc >= 8.6.8
# asciidoc-8.4.5-4.1.el6 does not work for man pages
%if 0%{?fedora} || (0%{?rhel} && 0%{?rhel} >= 7)
BuildRequires: asciidoc >= 8.6.8
BuildRequires: systemd
%endif


%description
A lightweight message router, written in C and built on Qpid Proton, that provides flexible and scalable interconnect between AMQP endpoints or between endpoints and brokers.


%package router
Summary:  The Qpid Dispatch Router executable
Obsoletes: libqpid-dispatch
Obsoletes: libqpid-dispatch-devel
Requires:  qpid-proton-c%{?_isa} >= %{proton_minimum_version}
Requires:  python3
Requires:  python3-qpid-proton >= %{proton_minimum_version}
%if %{_use_systemd}
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
%endif
Requires: libwebsockets >= %{libwebsockets_minimum_version}

%description router
%{summary}.


%files router
%license %{_pkglicensedir}/LICENSE
%license %{_pkglicensedir}/licenses.xml
%{_sbindir}/qdrouterd
%config(noreplace) %{_sysconfdir}/qpid-dispatch/qdrouterd.conf
%config(noreplace) %{_sysconfdir}/sasl2/qdrouterd.conf
%{_exec_prefix}/lib/qpid-dispatch
%{python3_sitelib}/qpid_dispatch_site.py*
%{python3_sitelib}/qpid_dispatch
%{python3_sitelib}/qpid_dispatch-*.egg-info
%{python3_sitelib}/__pycache__/*

%if %{_use_systemd}

%{_unitdir}/qdrouterd.service

%else

%{_initrddir}/qdrouterd
%attr(755,qdrouterd,qdrouterd) %dir %{_localstatedir}/run/qpid-dispatch

%endif

%{_mandir}/man5/qdrouterd.conf.5*
%{_mandir}/man8/qdrouterd.8*

%pre router
getent group qdrouterd >/dev/null || groupadd -r qdrouterd
getent passwd qdrouterd >/dev/null || \
  useradd -r -M -g qdrouterd -d %{_localstatedir}/lib/qdrouterd -s /sbin/nologin \
    -c "Owner of Qdrouterd Daemons" qdrouterd
exit 0


%if %{_use_systemd}

%post router
/sbin/ldconfig
%systemd_post qdrouterd.service

%preun router
%systemd_preun qdrouterd.service

%postun router
/sbin/ldconfig
%systemd_postun_with_restart qdrouterd.service

%endif

%if %{_use_sysvinit}

%post router
/sbin/ldconfig
/sbin/chkconfig --add qdrouterd

%preun router
if [ $1 -eq 0 ]; then
    /sbin/service qdrouterd stop >/dev/null 2>&1
    /sbin/chkconfig --del qdrouterd
fi

%postun router
/sbin/ldconfig
if [ "$1" -ge "1" ]; then
    /sbin/service qdrouterd condrestart >/dev/null 2>&1
fi

%endif


%package docs
Summary:   Documentation for the Qpid Dispatch router
BuildArch: noarch
Obsoletes:  qpid-dispatch-router-docs

%description docs
%{summary}.


%files docs
%doc %{_pkgdocdir}
%license %{_pkglicensedir}/LICENSE
%license %{_pkglicensedir}/licenses.xml


%package console
Summary: Web console for Qpid Dispatch Router
BuildArch: noarch
Requires: qpid-dispatch-router

%description console
%{summary}.

%files console
%{_datarootdir}/qpid-dispatch/console


%package tools
Summary: Tools for the Qpid Dispatch router
BuildArch: noarch
Requires: python3-qpid-proton >= %{proton_minimum_version}


%description tools
%{summary}.


%files tools
%{_bindir}/qdstat
%{_bindir}/qdmanage

%{_mandir}/man8/qdstat.8*
%{_mandir}/man8/qdmanage.8*


%prep
%setup -q

#%patch3 -p1
%patch4 -p1

mkdir pre_built
cd pre_built
tar xvzpf %{SOURCE3} -C .
cp %{SOURCE4} console/
%if 0%{?rhel} && 0%{?rhel} <= 6
tar xvzpf %{SOURCE1} -C .
%endif

%build
export DOCS=ON
%if 0%{?rhel} && 0%{?rhel} <= 6
export DOCS=OFF
%endif
%cmake -DDOC_INSTALL_DIR=%{?_pkgdocdir} \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DUSE_SETUP_PY=0 \
       -DQD_DOC_INSTALL_DIR=%{_pkgdocdir} \
       "-DBUILD_DOCS=$DOCS" \
       -DCMAKE_SKIP_RPATH:BOOL=OFF \
       -DUSE_LIBWEBSOCKETS=ON \
       -DCONSOLE_INSTALL=OFF \
      "-DCMAKE_C_FLAGS=$CMAKE_CXX_FLAGS $CFLAGS -Wno-error=deprecated-declarations" \
       .

# to fix multilib install, force (any) known date to generated file
touch -r %{SOURCE4} %{_builddir}/qpid-dispatch-%{version}/python/qpid_dispatch_site.py

make doc


%install
%make_install

%if %{_use_systemd}

install -dm 755 %{buildroot}%{_unitdir}
install -pm 644 %{_builddir}/qpid-dispatch-%{version}/etc/fedora/qdrouterd.service \
                %{buildroot}%{_unitdir}

%else

install -dm 755 %{buildroot}%{_initrddir}
install -pm 755 %{_builddir}/qpid-dispatch-%{version}/etc/fedora/qdrouterd \
                %{buildroot}%{_initrddir}

%endif

%if 0%{?rhel} && 0%{?rhel} <= 6
install -dm 755 %{buildroot}%{_mandir}/man5
install -dm 755 %{buildroot}%{_mandir}/man8
install -pm 644 %{_builddir}/qpid-dispatch-%{version}/pre_built/man/man5/* %{buildroot}%{_mandir}/man5/
install -pm 644 %{_builddir}/qpid-dispatch-%{version}/pre_built/man/man8/* %{buildroot}%{_mandir}/man8/
cp -a           %{_builddir}/qpid-dispatch-%{version}/pre_built/doc/qpid-dispatch-%{version}/*  \
                %{buildroot}%{_pkgdocdir}/
%endif

install -dm 755 %{buildroot}/var/run/qpid-dispatch

%if 0%{?rhel} && 0%{?rhel} <= 6
install -pm 644 %{SOURCE2} %{buildroot}%{_pkgdocdir}
%else
install -dm 755 %{buildroot}%{_pkglicensedir}
install -pm 644 %{SOURCE2} %{buildroot}%{_pkglicensedir}
install -pm 644 %{buildroot}%{_pkgdocdir}/LICENSE %{buildroot}%{_pkglicensedir}
rm -f %{buildroot}%{_pkgdocdir}/LICENSE
%endif

install -dm 755 %{buildroot}/%{_datarootdir}/qpid-dispatch/console
cp -a %{_builddir}/qpid-dispatch-%{version}/pre_built/console/* %{buildroot}/%{_datarootdir}/qpid-dispatch/console/

rm -f  %{buildroot}/%{_includedir}/qpid/dispatch.h
rm -fr %{buildroot}/%{_includedir}/qpid/dispatch

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%changelog
* Wed Sep 16 2020 Irina Boverman <iboverma@redhat.com> - 1.14.0-1
- Rebased to 1.14.0

* Thu May 14 2020 Irina Boverman <iboverma@redhat.com> - 1.12.0-1
- Rebased to 1.12.0
