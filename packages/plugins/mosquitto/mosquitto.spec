%global with_tests 0
%bcond_with websockets

Name:           mosquitto
Version:        2.0.19
Release:        1%{?dist}
Summary:        Open Source MQTT v5/v3.1.x Broker

License:        EPL-2.0
URL:            http://mosquitto.org/
Source0:        http://mosquitto.org/files/source/%{name}-%{version}.tar.gz

BuildRequires:  c-ares-devel
BuildRequires:  cjson-devel
BuildRequires:  gcc-c++
BuildRequires:  libuuid-devel
%if %{with websockets}
BuildRequires:  libwebsockets-devel
%endif
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  systemd-devel
%if 0%{?rhel} == 7
BuildRequires:  tcp_wrappers-libs
%endif
%if 0%{?with_tests}
BuildRequires:  CUnit-devel
%endif
#BuildRequires:  uthash-devel
Provides: bundled(uthash)

Requires(pre):    shadow-utils
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

%description
Mosquitto is an open source message broker that implements the MQ Telemetry
Transport protocol version 3.1 and 3.1.1 MQTT provides a lightweight method
of carrying out messaging using a publish/subscribe model. This makes it
suitable for "machine to machine" messaging such as with low power sensors
or mobile devices such as phones, embedded computers or micro-controllers
like the Arduino.

%package devel
Requires:     %{name}%{?_isa} = %{version}-%{release}
Summary:      Development files for %{name}

%description devel
Development headers and libraries for %{name}.

%prep
%autosetup -p1
# Set the install prefix to /usr
sed -i "s|prefix?=/usr/local|prefix?=/usr|" config.mk
# Don't strip binaries on install: rpmbuild will take care of it
sed -i "s|(INSTALL) -s|(INSTALL)|g" lib/Makefile src/Makefile client/Makefile

%build
%if 0%{?rhel} == 7
export CFLAGS="%{optflags} -std=gnu99"
%else
export CFLAGS="%{optflags}"
%endif
export LDFLAGS="%{optflags} %{__global_ldflags} -Wl,--as-needed"
make all %{?_smp_mflags} WITH_WEBSOCKETS=%{?with_websockets:yes}%{!?with_websockets:no} WITH_SYSTEMD=yes WITH_SRV=yes

%install
%if "%{_lib}" == "lib64"
export LIB_SUFFIX=64
%endif
%make_install

mkdir -p %{buildroot}%{_unitdir}
install -p -m 0644 service/systemd/%{name}.service.notify %{buildroot}%{_unitdir}/%{name}.service
mv %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf.example %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf

%if 0%{?with_tests}
%check
make test
%endif

%pre
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || \
    useradd -r -g %{name} -d %{_sysconfdir}/%{name} -s /sbin/nologin \
    -c "Mosquitto Broker" %{name}
exit 0

%post
%systemd_post %{name}.service
/sbin/ldconfig

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service
/sbin/ldconfig

%files
%license LICENSE.txt
%doc ChangeLog.txt CONTRIBUTING.md README.md
%{_bindir}/%{name}*
%{_sbindir}/%{name}
%{_libdir}/libmosquitto*.so.1
%{_libdir}/mosquitto_dynamic_security.so
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%config %{_sysconfdir}/%{name}/*.example
%{_unitdir}/%{name}.service
%{_mandir}/man*/%{name}*
%{_mandir}/man7/mqtt.7.*

%files devel
%{_includedir}/mosquitto*.h
%{_includedir}/mqtt*.h
%{_libdir}/libmosquitto*.so
%{_libdir}/pkgconfig/libmosquitto*.pc
%{_mandir}/man3/libmosquitto.3.*

%changelog
* Mon Oct 14 2024 Eric D. Helms <ericdhelms@gmail.com> - 2.0.19-1
- Build 2.0.19

* Thu Sep 07 2023 Eric D. Helms <ericdhelms@gmail.com> - 2.0.17-1
- Release 2.0.17

* Mon Nov 22 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 2.0.14-1
- Update to 2.0.14

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 2.0.12-2
- Rebuilt with OpenSSL 3.0.0

* Wed Aug 25 2021 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.12-1
- Update to latest upstream release 2.0.12
- Fixes CVE-2021-34434 (closes rhbz#1999865)

* Wed Aug 25 2021 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.11-3
- Rebuilt

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 10 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 2.0.11-1
- Update to 2.0.11

* Mon Apr 05 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 2.0.10-1
- Update to 2.0.10

* Mon Mar 08 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 2.0.8-1
- Update to 2.0.8

* Tue Mar 02 2021 Zbigniew JÄ™drzejewski-Szmek <zbyszek@in.waw.pl> - 2.0.7-2
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Sun Feb 07 2021 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.7-1
- Update to latest upstream release 2.0.7

* Sat Jan 30 2021 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.6-1
- Update to latest upstream release 2.0.6

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 12 2021 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.5-2
- Remove duplicate BR

* Mon Jan 11 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 2.0.5-1
- Update to 2.0.5

* Thu Dec 24 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 2.0.4-1
- Update to 2.0.4

* Fri Dec 18 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 2.0.3-1
- Update to new upstream release 2.0.3
- Enable DNS SRV record support
- Ship plugin in main package
- More explicit globs for files
- Conditionalise tests

* Wed Dec 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.2-1
- Update to new upstream release 2.0.2

* Fri Dec 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.0-1
- Update license
- Update to new upstream version 2.0.0

* Wed Dec 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.6.12-5
- Rebuilt

* Thu Oct 29 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.6.12-4
- Rebuilt

* Mon Oct 12 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.6.12-3
- Rebuilt

* Mon Sep 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.6.12-2
- Rebuilt

* Thu Aug 20 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.6.12-1
- Update to new upstream version 1.6.12

* Tue Aug 11 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.6.11-1
- Update to new upstream version 1.6.11

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 15 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.6.10-3
- Rebuilt

* Mon Jun 22 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.6.10-2
- Rebuilt

* Wed May 27 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 1.6.10-1
- Update to 1.6.10

* Sun May 24 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.6.9-5
- Rebuilt

* Mon May 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.6.9-4
- Rebuilt

* Fri May 01 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.6.9-3
- Rebuilt

* Tue Mar 24 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.6.9-2
- Fix build failure

* Sat Feb 29 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.6.9-1
- Update to new upstream version 1.6.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.6.8-2
- Rebuild for libwebsockets

* Tue Dec  3 2019 Peter Robinson <pbrobinson@fedoraproject.org> 1.6.8-1
- 1.6.8 release

* Wed Sep 25 2019 Peter Robinson <pbrobinson@fedoraproject.org> 1.6.7-1
- 1.6.7 release

* Tue Sep 24 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.6.6-1
- Update to new upstream version 1.6.6

* Sat Sep 14 2019 Peter Robinson <pbrobinson@fedoraproject.org> 1.6.5-1
- 1.6.5 release

* Mon Sep  2 2019 Peter Robinson <pbrobinson@fedoraproject.org> 1.6.4-2
- Rebuild for libwebsockets 3.2

* Fri Aug  2 2019 Peter Robinson <pbrobinson@fedoraproject.org> 1.6.4-1
- 1.6.4 release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.6.3-1
- Update to new upstream version 1.6.3

* Tue Apr 30 2019 Peter Robinson <pbrobinson@fedoraproject.org> 1.6.2-1
- 1.6.2 release

* Sat Apr 27 2019 Peter Robinson <pbrobinson@fedoraproject.org> 1.6.1-1
- 1.6.1 release

* Thu Apr 18 2019 Peter Robinson <pbrobinson@fedoraproject.org> 1.6.0-1
- Major new 1.6.0 release
- Support for MQTT 5

* Wed Mar  6 2019 Peter Robinson <pbrobinson@fedoraproject.org> 1.5.8-1
- New upstream version 1.5.8

* Sat Feb 16 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.5.7-1
- Update to new upstream version 1.5.7

* Sat Feb  9 2019 Peter Robinson <pbrobinson@fedoraproject.org> 1.5.6-1
- 1.5.6 release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan  7 2019 Peter Robinson <pbrobinson@fedoraproject.org> 1.5.5-2
- Rebuild for libwebsockets 3.x

* Tue Dec 18 2018 Fabian Affolter <mail@fabian-affolter.ch> - 1.5.5-1
- Update to new upstream version 1.5.5 (rhbz#1660413, rhbz#1660414)

* Fri Nov 09 2018 Fabian Affolter <mail@fabian-affolter.ch> - 1.5.4-2
- Update to new upstream version 1.5.4

* Sun Oct 14 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.5.3-1
- 1.5.3 release

* Thu Sep 20 2018 Fabian Affolter <mail@fabian-affolter.ch> - 1.5.2-2
- Use WITH_BUNDLED_DEPS=no

* Thu Sep 20 2018 Fabian Affolter <mail@fabian-affolter.ch> - 1.5.2-1
- Update to new upstream version 1.5.2

* Mon Aug 20 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.5.1-1
- 1.5.1 release

* Fri Jul 20 2018 John W. Linville <linville@redhat.com> - 1.5-5
- Add previously unnecessary BuildRequires for gcc-c++

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat May 26 2018 Rich Mattes <richmattes@gmail.com> - 1.5-3
- Add network-online.target and documentation to unitfile

* Sat May 26 2018 Rich Mattes <richmattes@gmail.com> - 1.5-2
- Use upstream systemd service and enable systemd notification support
  (rhbz#1410654)

* Sun May 20 2018 Fabian Affolter <mail@fabian-affolter.ch> - 1.5-2
- Update to new upstream version 1.5 (rhbz#1580115)

* Sat May 05 2018 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.15-2
- Update systemd unit file (rhbz#1564733)

* Tue Mar 06 2018 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.15-1
- Fix CVE-2017-7651 (rhbz#1551755, rhbz#1551754)
- Fix CVE-2017-7652 (rhbz#1551743, rhbz#1551745)
- Update to new upstream version 1.4.15

* Fri Feb 16 2018 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.14-7
- Rebuild for libwebsockets

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct 21 2017 Kevin Fenzi <kevin@scrye.com> - 1.4.14-5
- Rebuild again for libwebsockets

* Tue Aug 22 2017 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.14-4
- Rebuild for libwebsockets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 12 2017 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.14-1
- Update to new upstream version 1.4.14

* Sat Jul 01 2017 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.13-1
- Fix CVE-2017-9868 (rhbz#1464946)
- Update to new upstream version 1.4.13

* Sun Jun 18 2017 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.12-2
- Rebuild for libwebsockets

* Tue May 30 2017 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.12-1
- Fix CVE-2017-7650 (rhbz#1456507)
- Update to new upstream version 1.4.12

* Thu May 18 2017 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.11-2
- Rebuild for libwebsockets

* Thu Mar 02 2017 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.11-1
- Update to new upstream version 1.4.11

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 29 2016 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.10-2
- Rebuild for libwebsockets (rhbz#1406779)

* Fri Nov 18 2016 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.10-1
- Update to new upstream version 1.4.10

* Mon Aug 08 2016 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.9-3
- Rebuild

* Fri Jul 01 2016 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.9-2
- Fix configuration example

* Fri Jul 01 2016 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.9-1
- Use sample configuration (rhbz#1272342)
- Update to new upstream version 1.4.9

* Sun May 08 2016 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.8-2
- Enable websockets support (rhbz#1197678)

* Wed Mar 09 2016 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.8-1
- Update to new upstream version 1.4.8

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 24 2016 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.7-1
- Update to new upstream version 1.4.7

* Fri Nov 27 2015 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.5-1
- Update to new upstream version 1.4.5

* Wed Oct 07 2015 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.4-1
- Update to new upstream version 1.4.4

* Thu Sep 03 2015 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.3-1
- Update to new upstream version 1.4.3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 10 2015 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.2-1
- Update to new upstream version 1.4.2

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.4-2
- Rebuilt for GCC 5 C++11 ABI change

* Wed Feb 25 2015 Fabian Affolter <mail@fabian-affolter.ch> - 1.4-1
- Update BRs
- Python subpackage is replaced by python-paho-mqtt
- Update to new upstream version 1.4

* Thu Oct 16 2014 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.5-1
- Update to new upstream version 1.3.5

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Aug 12 2014 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.4-1
- Update to new upstream version 1.3.4

* Mon Aug 11 2014 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.3-1
- Update to new upstream version 1.3.3

* Mon Jul 14 2014 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.2-1
- Update to new upstream version 1.3.2 (rhbz#1119238)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 06 2014 Rich Mattes <richmattes@gmail.com> - 1.3.1-1
- Update to latest upstream release 1.3.1

* Sat Mar 22 2014 Fabian Affolter <mail@fabian-affolter.ch> - 1.3-1
- Update to latest upstream release 1.3

* Sat Dec 21 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.3-2
- Add install section to service file

* Sat Dec 21 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.3-1
- Update to latest upstream release 1.2.3

* Mon Oct 28 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.2-1
- Update to latest upstream release 1.2.2

* Sat Sep 21 2013 Fabian Affolter <mail@fabian-affolter.ch> - 1.2.1-1
- Update to latest upstream release 1.2.1

* Wed Aug 14 2013 Rich Mattes <richmattes@gmail.com> - 1.2-1
- Update to release 1.2

* Sat Aug 10 2013 Rich Mattes <richmattes@gmail.com> - 1.1.3-3
- Switch to Makefiles from CMake scripts
- Add User=mosquitto to systemd unit

* Tue Jul 23 2013 Rich Mattes <richmattes@gmail.com> - 1.1.3-2
- Unbundle uthash
- Add as-needed to ldflags to avoid spurious links

* Wed May 1 2013 Rich Mattes <richmattes@gmail.com> - 1.1.3-1
- Initial package
