%global proton_datadir %{_datadir}/proton
%global gem_name qpid_proton

# per https://fedoraproject.org/wiki/Packaging:AutoProvidesAndRequiresFiltering#Preventing_files.2Fdirectories_from_being_scanned_for_deps_.28pre-scan_filtering.29
%global __provides_exclude_from ^%{proton_datadir}/examples/.*$
%global __requires_exclude_from ^%{proton_datadir}/examples/.*$

%undefine __brp_mangle_shebangs

Name:           qpid-proton
Version:        0.37.0
Release:        1%{?dist}
Summary:        A high performance, lightweight messaging library
License:        ASL 2.0
URL:            http://qpid.apache.org/proton/

Source0:        https://apache.osuosl.org/qpid/proton/%{version}/%{name}-%{version}.tar.gz
Patch0:         proton.patch

Source1:        licenses.xml

%global proton_licensedir %{_licensedir}/proton

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  swig
BuildRequires:  pkgconfig
BuildRequires:  doxygen
#BuildRequires:  python3-sphinx
BuildRequires:  libuuid-devel
BuildRequires:  openssl-devel
BuildRequires:  python3-devel
BuildRequires:  glibc-headers
BuildRequires:  cyrus-sasl-devel
BuildRequires:  jsoncpp-devel
BuildRequires:  python3-setuptools
BuildRequires:  ruby-devel
BuildRequires:  rubygems-devel

%description
Proton is a high performance, lightweight messaging library. It can be used in
the widest range of messaging applications including brokers, client libraries,
routers, bridges, proxies, and more. Proton is based on the AMQP 1.0 messaging
standard. Using Proton it is trivial to integrate with the AMQP 1.0 ecosystem
from any platform, environment, or language.


%package c
Group:     System Environment/Libraries
Summary:   C libraries for Qpid Proton
Requires:  cyrus-sasl-lib
Obsoletes: qpid-proton

%description c
%{summary}.

%files c
%dir %{proton_datadir}
%license %{proton_licensedir}/LICENSE.txt
%license %{proton_licensedir}/licenses.xml
%doc %{proton_datadir}/README*
%{_libdir}/libqpid-proton.so.*
%{_libdir}/libqpid-proton-core.so.*
%{_libdir}/libqpid-proton-proactor.so.*

%post c -p /sbin/ldconfig

%postun c -p /sbin/ldconfig


%package   cpp
Group:     System Environment/Libraries
Summary:   C++ libraries for Qpid Proton
Requires:  qpid-proton-c%{?_isa} = %{version}-%{release}
#Requires:  jsoncpp
%description cpp
%{summary}.

%files cpp
%defattr(-,root,root,-)
%dir %{proton_datadir}
%doc %{proton_datadir}/README*
%{_libdir}/libqpid-proton-cpp.so.*

%post cpp -p /sbin/ldconfig

%postun cpp -p /sbin/ldconfig


%package c-devel
Group:     Development/System
Requires:  qpid-proton-c%{?_isa} = %{version}-%{release}
Summary:   Development libraries for writing messaging apps with Qpid Proton
Obsoletes: qpid-proton-devel

%description c-devel
%{summary}.

%files c-devel
%{_includedir}/proton
%exclude %{_includedir}/proton/*.hpp
%exclude %{_includedir}/proton/**/*.hpp
%{_libdir}/libqpid-proton.so
%{_libdir}/libqpid-proton-core.so
%{_libdir}/libqpid-proton-proactor.so
%{_libdir}/pkgconfig/libqpid-proton.pc
%{_libdir}/pkgconfig/libqpid-proton-core.pc
%{_libdir}/pkgconfig/libqpid-proton-proactor.pc
%{_libdir}/cmake/Proton


%package cpp-devel
Group:     Development/System
Requires:  qpid-proton-cpp%{?_isa} = %{version}-%{release}
Requires:  qpid-proton-c-devel%{?_isa} = %{version}-%{release}
Summary:   Development libraries for writing messaging apps with Qpid Proton

%description cpp-devel
%{summary}.

%files cpp-devel
%{_includedir}/proton/*.hpp
%{_includedir}/proton/**/*.hpp
%{_libdir}/pkgconfig/libqpid-proton-cpp.pc
%{_libdir}/libqpid-proton-cpp.so
%{_libdir}/cmake/ProtonCpp


%package c-docs
Summary:   Documentation for the C development libraries for Qpid Proton
BuildArch: noarch
Obsoletes: qpid-proton-c-devel-doc
Obsoletes: qpid-proton-c-devel-docs

%description c-docs
%{summary}.

%files c-docs
%license %{proton_licensedir}/LICENSE.txt
%doc %{proton_datadir}/docs/api-c
%doc %{proton_datadir}/examples/README.md
%doc %{proton_datadir}/examples/c/ssl-certs
%doc %{proton_datadir}/examples/c/*.c
%doc %{proton_datadir}/examples/c/*.h
%doc %{proton_datadir}/examples/c/README.dox
%doc %{proton_datadir}/examples/c/CMakeLists.txt


%package   cpp-docs
Summary:   Documentation for the C++ development libraries for Qpid Proton
BuildArch: noarch
Obsoletes: qpid-proton-cpp-devel-doc
Obsoletes: qpid-proton-cpp-devel-docs

%description cpp-docs
%{summary}.

%files cpp-docs
%license %{proton_licensedir}/LICENSE.txt
%{proton_datadir}/docs/api-cpp
%doc %{proton_datadir}/examples/cpp/*.cpp
%doc %{proton_datadir}/examples/cpp/*.hpp
%doc %{proton_datadir}/examples/cpp/README.dox
%doc %{proton_datadir}/examples/cpp/CMakeLists.txt
%doc %{proton_datadir}/examples/cpp/ssl-certs
%doc %{proton_datadir}/examples/cpp/tutorial.dox

%package -n python3-qpid-proton
Summary:  Python language bindings for the Qpid Proton messaging framework
%{?python_provide:%python_provide python3-qpid-proton}
Requires: qpid-proton-c%{?_isa} = %{version}-%{release}
Requires: python3

%description -n python3-qpid-proton
%{summary}.

%files -n python3-qpid-proton
%{python3_sitearch}/__pycache__/*
%{python3_sitearch}/*.so
%{python3_sitearch}/*.py*
%{python3_sitearch}/*.egg-info
%{python3_sitearch}/proton


%package -n python-qpid-proton-docs
Summary:   Documentation for the Python language bindings for Qpid Proton
BuildArch: noarch
Obsoletes:  python-qpid-proton-doc

%description -n python-qpid-proton-docs
%{summary}.

%files -n python-qpid-proton-docs
%license %{proton_licensedir}/LICENSE.txt
%doc %{proton_datadir}/examples/python

%package tests
Group:     Documentation
Summary:   Qpid Proton Tests
BuildArch: noarch

%description tests
%{summary}.

%files tests
%defattr(-,root,root,-)
%doc %{proton_datadir}/tests
%exclude %{proton_datadir}/tests/py/*.pyo
%exclude %{proton_datadir}/tests/py/*.pyc


%package -n rubygem-%{gem_name}
Group:   System Environment/Libraries
Summary: Ruby language bindings for the Qpid Proton messaging framework
Obsoletes:  rubygem-%{gem_name}-doc

%description -n rubygem-%{gem_name}
Proton is a high performance, lightweight messaging library. It can be used in
the widest range of messaging applications including brokers, client libraries,
routers, bridges, proxies, and more. Proton is based on the AMQP 1.0 messaging
standard.

%files -n rubygem-%{gem_name}
%dir %{gem_instdir}
%{gem_libdir}
%{gem_extdir_mri}
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/examples
%doc %{gem_instdir}/tests


%prep
%setup -q -n %{name}-%{version}
%patch0 -p1


%build

python_includes=$(ls -d /usr/include/python3.6*)
python_lib=$(ls /usr/**/libpython3.6*.so)

mkdir build; cd build

%cmake \
    -DSYSINSTALL_BINDINGS=ON \
    -DCMAKE_SKIP_RPATH:BOOL=OFF \
    "-DPYTHON_EXECUTABLE=%{__python3}" \
    "-DPYTHON_INCLUDE_DIR=$python_includes" \
    "-DPYTHON_LIBRARY=$python_lib" \
    ..
make all docs %{?_smp_mflags}
(cd python/dist; %py3_build)

%install
rm -rf %{buildroot}

cd build
%make_install
(cd python/dist; %py3_install)

chmod +x %{buildroot}%{python3_sitearch}/_cproton.so

install -dm 755 %{buildroot}%{proton_licensedir}
install -pm 644 %{SOURCE1} %{buildroot}%{proton_licensedir}
install -pm 644 %{buildroot}%{proton_datadir}/LICENSE.txt %{buildroot}%{proton_licensedir}
rm -f %{buildroot}%{proton_datadir}/LICENSE.txt

cd ruby/gem/
mkdir -p %{buildroot}%{gem_instdir}
install -dm 755 %{buildroot}%{gem_dir}/specifications
mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a %{buildroot}%{ruby_vendorarchdir}/cproton.so %{buildroot}%{gem_extdir_mri}/
touch %{buildroot}%{gem_extdir_mri}/gem.build_complete
chmod 644 %{buildroot}%{gem_extdir_mri}/gem.build_complete
cp -a examples tests lib %{buildroot}%{gem_instdir}/
install -pm 644 %{gem_name}.gemspec %{buildroot}%{gem_spec}

# clean up files that are not shipped
rm -rf %{buildroot}%{_exec_prefix}/bindings
rm -rf %{buildroot}%{_libdir}/java
rm -rf %{buildroot}%{_libdir}/libproton-jni.so
rm -rf %{buildroot}%{_datarootdir}/java
rm -rf %{buildroot}%{_libdir}/proton.cmake
rm -rf %{buildroot}%{_libdir}/php
rm -rf %{buildroot}%{_libdir}/ruby
rm -rf %{buildroot}%{_datarootdir}/php
rm -rf %{buildroot}%{_datarootdir}/ruby
rm -rf %{buildroot}%{_sysconfdir}/php.d
rm -fr %{buildroot}%{proton_datadir}/examples/CMakeFiles
rm -f  %{buildroot}%{proton_datadir}/examples/Makefile
rm -f  %{buildroot}%{proton_datadir}/examples/*.cmake
rm -fr %{buildroot}%{proton_datadir}/examples/c/CMakeFiles
rm -f  %{buildroot}%{proton_datadir}/examples/c/*.cmake
rm -f  %{buildroot}%{proton_datadir}/examples/c/Makefile
rm -f  %{buildroot}%{proton_datadir}/examples/c/Makefile.pkgconfig
rm -f  %{buildroot}%{proton_datadir}/examples/c/broker
rm -f  %{buildroot}%{proton_datadir}/examples/c/direct
rm -f  %{buildroot}%{proton_datadir}/examples/c/receive
rm -f  %{buildroot}%{proton_datadir}/examples/c/send
rm -f  %{buildroot}%{proton_datadir}/examples/c/send-abort
rm -f  %{buildroot}%{proton_datadir}/examples/c/send-ssl
rm -fr %{buildroot}%{proton_datadir}/examples/cpp/CMakeFiles
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/*.cmake
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/Makefile
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/Makefile.pkgconfig
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/broker
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/client
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/connection_options
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/direct_recv
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/direct_send
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/encode_decode
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/flow_control
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/helloworld
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/helloworld_direct
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/queue_browser
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/scheduled_send_03
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/scheduled_send
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/selected_recv
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/server
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/server_direct
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/service_bus
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/simple_connect
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/simple_recv
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/simple_send
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/ssl
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/ssl_client_cert
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/message_properties
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/multithreaded_client
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/multithreaded_client_flow_control
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/reconnect_client
rm -f  %{buildroot}%{proton_datadir}/examples/cpp/colour_send
rm -fr %{buildroot}%{proton_datadir}/examples/engine/java
rm -fr %{buildroot}%{proton_datadir}/examples/go
rm -fr %{buildroot}%{proton_datadir}/examples/java
rm -fr %{buildroot}%{proton_datadir}/examples/javascript
rm -fr %{buildroot}%{proton_datadir}/examples/ruby
rm -fr %{buildroot}%{proton_datadir}/examples/perl
rm -fr %{buildroot}%{proton_datadir}/examples/php
rm -f  %{buildroot}%{proton_datadir}/CMakeLists.txt

%check

%changelog
* Wed May 11 2022 Eric D. Helms <ericdhelms@gmail.com> - 0.37.0-1
- Rebase to 0.37

* Mon Mar 21 2022 Eric D. Helms <ericdhelms@gmail.com> - 0.36.0-1
- Release qpid-proton 0.36.0

* Wed Oct 20 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.35.0-1
- Build 0.35

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.32.0-3
- Rebuild for Ruby 2.7

* Fri Oct  2 2020 Irina Boverman <iboverma@redhat.com> - 0.32.0-2
- Added temp fix to allow building c/cpp examples

* Thu Sep 24 2020 Irina Boverman <iboverma@redhat.com> - 0.32.0-1
- Rebased to 0.32.0

* Thu Jul 30 2020 Irina Boverman <iboverma@redhat.com> - 0.31.0-3
- Added rubygem-qpid_proton subpackage

* Mon Jun  1 2020 Irina Boverman <iboverma@redhat.com> - 0.31.0-2
- Corrected cmake for c/cpp examples
- Resolved PROTON-2228

* Thu May 14 2020 Irina Boverman <iboverma@redhat.com> - 0.31.0-1
- Rebased to 0.31.0

* Fri Mar 20 2020 Irina Boverman <iboverma@redhat.com> - 0.30.0-2
- Rebased to 0.30.0
- Replaced epydoc with python3-sphinx

* Wed Sep 18 2019 Irina Boverman <iboverma@redhat.com> - 0.29.0-1
- Resolved PROTON-2092
- Rebased to 0.29.0 rc1 upstream
- Removed jsoncpp BuildRequires and Requires for now, there is no jsoncpp in EPEL 8

* Tue May  7 2019 Irina Boverman <iboverma@redhat.com> - 0.28.0-1
- Rebased to 0.28.0 rc1 upstream

* Tue Apr  9 2019 Irina Boverman <iboverma@redhat.com> - 0.27.0-4
- Added another patch to resolve ENTMQCL-1294

* Mon Apr  1 2019 Irina Boverman <iboverma@redhat.com> - 0.27.0-3
- Resolved: ENTMQCL-1294

* Tue Feb 26 2019 Irina Boverman <iboverma@redhat.com> - 0.27.0-2
- Resolved: ENTMQCL-753, ENTMQCL-1200

* Wed Feb  6 2019 Irina Boverman <iboverma@redhat.com> - 0.27.0-1
- Rebased to 0.27.0

* Thu Dec 20 2018 Irina Boverman <iboverma@redhat.com> - 0.26.0-3
- Added patch to resolve ENTMQCL-1121

* Mon Nov 12 2018 Irina Boverman <iboverma@redhat.com> - 0.26.0-2
- Added jsoncpp BuildRequires and Requires

* Mon Oct 22 2018 Irina Boverman <iboverma@redhat.com> - 0.26.0-1
- Rebased to 0.26.0

* Tue Sep 11 2018 Irina Boverman <iboverma@redhat.com> - 0.25.0-1
- Rebased to 0.25.0

* Wed Jul 18 2018 Irina Boverman <iboverma@redhat.com> - 0.24.0-2
- Resolved PROTON-1896/ENTMQCL-755

* Mon Jul  2 2018 Irina Boverman <iboverma@redhat.com> - 0.24.0-1
- Rebased to 0.24.0

* Tue Jun  5 2018 Irina Boverman <iboverma@redhat.com> - 0.23.0-1
- Rebased to 0.23.0

* Mon Apr  2 2018 Irina Boverman <iboverma@redhat.com> - 0.22.0-2
- Updated licenses.xml file

* Mon Apr  2 2018 Irina Boverman <iboverma@redhat.com> - 0.22.0-1
- Rebased to 0.22.0

* Mon Mar  5 2018 Irina Boverman <iboverma@redhat.com> - 0.21.0-1
- Rebased to 0.21.0

* Wed Jan 31 2018 Irina Boverman <iboverma@redhat.com> - 0.20.0-2
- Removed ruby files

* Mon Jan 29 2018 Irina Boverman <iboverma@redhat.com> - 0.20.0-1
- Rebased to 0.20.0

* Tue Jan 16 2018 Irina Boverman <iboverma@redhat.com> - 0.18.1-2
- Added fix for ENTMQCL-587
- Removed fix for ENTMQCL-602

* Mon Jan  8 2018 Irina Boverman <iboverma@redhat.com> - 0.18.1-1
- Rebased to 0.18.1
- Added fixes for ENTMQCL-589 and ENTMQCL-602

* Tue Nov 28 2017 Irina Boverman <iboverma@redhat.com> - 0.18.0-6
- Added fix for PROTON-1700

* Wed Nov  8 2017 Irina Boverman <iboverma@redhat.com> - 0.18.0-5
- Added fixes for PROTON-1678 and PROTON-1681

* Wed Oct 18 2017 Irina Boverman <iboverma@redhat.com> - 0.18.0-4
- Rebased to 0.18.0 rc1

* Mon Oct  2 2017 Irina Boverman <iboverma@redhat.com> - 0.18.0-3
- Added PROTON-1607 FIX

* Mon Oct  2 2017 Irina Boverman <iboverma@redhat.com> - 0.18.0-2
- Rebased to 0.18.0-beta upstream

* Wed Sep 13 2017 Irina Boverman <iboverma@redhat.com> - 0.18.0-1
- Rebased to 0.18.0 snapshot/commit c6d086

* Wed Aug 23 2017 Mike Cressman <mcressma@redhat.com> - 0.16.0-7
- Resolved: PROTON-1536, PROTON-1394/BZ-1318015, PROTON-1534/BZ-1319165

* Tue Aug 22 2017 Irina Boverman <iboverma@redhat.com> - 0.16.0-6
- Resolved: ENTMQCL-514, ENTMQCL-515, PROTON-1539

* Thu Mar  9 2017 Irina Boverman <iboverma@redhat.com> - 0.16.0-3
- Resolved: ENTMQCL-443, ENTMQCL-448

* Wed Mar  1 2017 Irina Boverman <iboverma@redhat.com> - 0.16.0-2
- Resolved: ENTMQCL-428, ENTMQCL-457, ENTMQCL-459, ENTMQCL-468, ENTMQCL-475

* Thu Dec  8 2016 Irina Boverman <iboverma@redhat.com> - 0.16.0-1
- Rebased to 0.16.0-rc1
- Renamed sub-packages qpid-proton-c-devel-docs/qpid-proton-cpp-devel-docs
  to qpid-proton-c-docs/qpid-proton-cpp-docs
- Removed binary and derived files from qpid-proton-cpp-docs package

* Mon Aug 29 2016 Irina Boverman <iboverma@redhat.com> - 0.14.0-1
- Rebased to 0.14.0

* Wed Jun 22 2016 Irina Boverman <iboverma@redhat.com> - 0.13.0-5
- Restored cyrus-sasl-devel dependency for non-Fedora builds

* Fri Jun 17 2016 Irina Boverman <iboverma@redhat.com> - 0.13.0-4
- Replaced "Provides" with "Obsoletes"

* Wed Jun 15 2016 Irina Boverman <iboverma@redhat.com> - 0.13.0-2
- Rebased to 0.13.0 GA version
- Changed *doc to *docs, moved examples to *docs
- Resolved ENTMQCL-367

* Tue May 17 2016 Irina Boverman <iboverma@redhat.com> - 0.13.0-1
- Rebased to 0.13.0 Beta

* Wed Mar 23 2016 Irina Boverman <iboverma@redhat.com> - 0.12.1-1
- Rebased to 0.12.1

* Thu Feb 25 2016 Irina Boverman <iboverma@redhat.com> - 0.12.0-1
- Rebased to 0.12.0
- Added python3 installation

* Thu Jan 21 2016 Irina Boverman <iboverma@redhat.com> - 0.11.1-1
- Rebased to 0.11.1

* Thu Dec  3 2015 Irina Boverman <iboverma@redhat.com> - 0.11.0-1
- Rebased to 0.11.0

* Thu Sep  3 2015 Irina Boverman <iboverma@redhat.com> - 0.10-2
- Added dependency on cyrus-sasl-devel and cyrus-sasl-lib
- Added 0001-PROTON-974-Accept-a-single-symbol-in-SASL-mechs-fram.patch

* Mon Aug 17 2015 Irina Boverman <iboverma@redhat.com> - 0.10-1
- Rebased to 0.10 proton release

* Wed Jun  3 2015 Irina Boverman <iboverma@redhat.com> - 0.9-4
- Added PROTON-858-fix-deletion-of-entries-from-map-to-.patch

* Thu May  7 2015 Irina Boverman <iboverma@redhat.com> - 0.9-3
- Rebased to 0.9.1 upstream

* Tue Mar 31 2015 Irina Boverman <iboverma@redhat.com> - 0.9-2
- Rebased to final 0.9 upstream

* Tue Mar  3 2015 Irina Boverman <iboverma@redhat.com> - 0.9-1.20150223
- Revised spec file to exclude generated and binary files from
  examples/c/messender directory

* Mon Feb 23 2015 Irina Boverman <iboverma@redhat.com> - 0.9-1.20150223
- Rebased to upstream snapshot 92d0499

* Thu Feb 19 2015 Irina Boverman <iboverma@redhat.com> - 0.9-1.20150219
- Removed perl examples

* Wed Feb 18 2015 Irina Boverman <iboverma@redhat.com> - 0.9-1.20150218.1
- Rebased to upstream snapshot ae49e3a

* Fri Nov  7 2014 Irina Boverman <iboverma@redhat.com> - 0.7-5
- Resolved: 1153769

* Thu Sep  4 2014 Irina Boverman <iboverma@redhat.com> - 0.7-4
- Resolved: 1126074

* Fri Aug  1 2014 Irina Boverman <iboverma@redhat.com> - 0.7-3
- Resolved: 1109320

* Thu May 29 2014 Irina Boverman <iboverma@redhat.com> - 0.7-2
- Add Visual-Studio-2008 patch

* Thu May  1 2014 Irina Boverman <iboverma@redhat.com> - 0.7-1
- Rebase to 0.7

* Fri Apr  4 2014 Irina Boverman <iboverma@redhat.com> - 0.6-2
- Added a patch to resolve bz 1077384

* Thu Dec 19 2013 Irina Boverman <iboverma@redhat.com> - 0.6-1
- Rebasing to 0.6-rc3

* Fri Nov 15 2013 Irina Boverman <iboverma@redhat.com> - 0.5-9
- Additional fixes for 1023639

* Wed Nov  6 2013 Irina Boverman <iboverma@redhat.com> - 0.5-8
- Resolved 1023639

* Thu Sep 26 2013 Irina Boverman <iboverma@redhat.com> - 0.5-6
- Added changes required to fix bz 995554

* Mon Sep 23 2013 Irina Boverman <iboverma@redhat.com> - 0.5-5
- Changed spec file to remove additional items

* Thu Sep 19 2013 Irina Boverman <iboverma@redhat.com> - 0.5-4
- Changed python-qpid-proton-doc sub-package to noarch

* Tue Sep 17 2013 Irina Boverman <iboverma@redhat.com> - 0.5-3
- Added qpid-proton-c-devel-doc/noarch package to resolve bz 1005058

* Wed Aug 28 2013 Irina Boverman <iboverma@redhat.com> - 0.5-2
- Built from mrg-messaging-3-rhel-6 branch

* Wed Aug 28 2013 Irina Boverman <iboverma@redhat.com> - 0.5-1
- Revised to Qpid Proton 0.5 version
- Resolves bz: 1002290

* Wed Apr 10 2013 Irina Boverman <iboverma@redhat.com> - 0.4-2.2
- Initial packaging of the Qpid Proton for a product.

* Fri Apr  5 2013 Darryl L. Pierce <dpierce@redhat.com> - 0.4-2.2
- Added Obsoletes and Provides for packages whose names changed.
- Resolves: BZ#948784

* Mon Apr  1 2013 Darryl L. Pierce <dpierce@redhat.com> - 0.4-2.1
- Fixed the dependencies for qpid-proton-devel and python-qpid-proton.

* Thu Mar 28 2013 Darryl L. Pierce <dpierce@redhat.com> - 0.4-2
- Moved all C libraries to the new qpid-proton-c subpackage.

* Wed Mar 13 2013 Darryl L. Pierce <dpierce@redhat.com> - 0.4-1
- Rebased on Proton 0.4.
- On EL6 BR pulls in Cmake 2.8 on PPC/PPC64.

* Thu Feb 21 2013 Darryl L. Pierce <dpierce@redhat.com> - 0.3-4
- Fixes copying nested data.
- PROTON-246, PROTON-230

* Mon Jan 28 2013 Darryl L. Pierce <dpierce@redhat.com> - 0.3-3
- Fixes build failure on non-x86 platforms.
- Resolves: BZ#901526

* Fri Jan 25 2013 Darryl L. Pierce <dpierce@redhat.com> - 0.3-2
- Fixes build failure on non-x86 platforms.
- Resolves: BZ#901526

* Wed Jan 16 2013 Darryl L. Pierce <dpierce@redhat.com> - 0.3-1
- Rebased on Proton 0.3.

* Fri Dec 28 2012 Darryl L. Pierce <dpierce@redhat.com> - 0.2-2.4
- Moved ownership of the docs dir to the docs package.

* Wed Dec 19 2012 Darryl L. Pierce <dpierce@redhat.com> - 0.2-2.3
- Fixed package dependencies, adding the release macro.

* Mon Dec 17 2012 Darryl L. Pierce <dpierce@redhat.com> - 0.2-2.2
- Fixed subpackage dependencies on main package.
- Removed accidental ownership of /usr/include.

* Thu Dec 13 2012 Darryl L. Pierce <dpierce@redhat.com> - 0.2-2.1
- Remove BR for ruby-devel.
- Removed redundant package name from summary.
- Removed debugging artifacts from specfile.
- Moved unversioned library to the -devel package.
- Added dependency on main package to -devel.
- Fixed directory ownerships.

* Fri Nov 30 2012 Darryl L. Pierce <dpierce@redhat.com> - 0.2-2
- Removed BR on help2man.
- Added patch for generated manpage.

* Mon Nov  5 2012 Darryl L. Pierce <dpierce@redhat.com> - 0.2-1
- Initial packaging of the Qpid Proton.
