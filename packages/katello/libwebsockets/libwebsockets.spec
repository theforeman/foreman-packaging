Name:           libwebsockets
Version:        2.4.2
Release:        2%{?dist}
Summary:        A lightweight C library for Websockets

# base64-decode.c and ssl-http2.c is under MIT license with FPC exception.
# sha1-hollerbach is under BSD
# https://fedorahosted.org/fpc/ticket/546
# Test suite is licensed as Public domain (CC-zero)
License:        LGPLv2 and Public Domain and BSD and MIT and zlib
URL:            http://libwebsockets.org
Source0:        https://github.com/warmcat/libwebsockets/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
ExcludeArch:    i686

BuildRequires:  cmake
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
#BuildRequires:  libev-devel

Provides:       bundled(sha1-hollerbach)
Provides:       bundled(base64-decode)
Provides:       bundled(ssl-http2)

%description
This is the libwebsockets C library for lightweight websocket clients and
servers.

%package devel
Summary:        Headers for developing programs that will use %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the header files needed for developing
%{name} applications.

%package tests
Summary:        Tests to use with %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description tests
This package contains the tests for %{name} applications.

%prep
%setup -q -n %{name}-%{version}

%build
mkdir -p build
cd build
%cmake \
    -D LWS_LINK_TESTAPPS_DYNAMIC=ON \
    -D LWS_WITHOUT_BUILTIN_GETIFADDRS=ON \
    -D LWS_WITHOUT_BUILTIN_SHA1=ON \
    -D LWS_WITH_STATIC=OFF \
    ..
make %{?_smp_mflags}

%install
cd build
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -exec rm -f {} ';'
find %{buildroot} -name '*.cmake' -exec rm -f {} ';'
find %{buildroot} -name '*_static.pc' -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc README.md changelog
%license LICENSE
%{_libdir}/%{name}.so.*

%files devel
%doc READMEs/README.coding.md READMEs/ changelog
%license LICENSE
%{_includedir}/*.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files tests
%doc READMEs/README.coding.md READMEs/README.test-apps.md
%license LICENSE
%{_bindir}/%{name}-test-*
%{_datadir}/%{name}-test-server/

%changelog
* Mon Oct  1 2018 Irina Boverman <iboverma@redhat.com> - 2.4.2-2
- Added multi-arches

* Thu Jun 28 2018 Irina Boverman <iboverma@redhat.com> - 2.4.2-1
- Rebase to 2.4.2

* Wed Jan  4 2017 Irina Boverman <iboverma@redhat.com> - 2.1.0-3
- Added patches from  https://github.com/alanconway/libwebsockets.git

* Wed Nov 30 2016 Irina Boverman <iboverma@redhat.com> - 2.1.0-2
- Initial build for AMQ Interconnect

* Thu Nov 17 2016 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.0-2
- Move tests (rhbz#1390538)

* Thu Nov 17 2016 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.0-1
- Update to latest upstream release 2.1.0 (rhbz#1376257)

* Mon Oct 31 2016 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.3-1
- Update to latest upstream release 2.0.3

* Wed Aug 03 2016 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.2-1
- Update to latest upstream release 2.0.2 (rhbz#1358988)

* Sat Apr 16 2016 Fabian Affolter <mail@fabian-affolter.ch> - 1.7.5-1
- Update licenses
- Update to latest upstream release 1.7.5

* Tue Mar 22 2016 Fabian Affolter <mail@fabian-affolter.ch> - 1.7.4-1
- Update licenses
- Update to latest upstream release 1.7.4

* Sun Jan 24 2016 Fabian Affolter <mail@fabian-affolter.ch> - 1.6.1-2
- Update to latest upstream release 1.6.1

* Fri Jan 22 2016 Fabian Affolter <mail@fabian-affolter.ch> - 1.5.1-2
- Update spec file
- Update to latest upstream release 1.5.1

* Wed Mar 04 2015 Fabian Affolter <mail@fabian-affolter.ch> - 1.3-2
- Introduce license tag
- Including .cmake files in dev package
- Switch to github source

* Wed Mar 04 2015 Fabian Affolter <mail@fabian-affolter.ch> - 1.3-1
- Initial package for Fedora
