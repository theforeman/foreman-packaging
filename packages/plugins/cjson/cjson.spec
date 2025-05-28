Name:           cjson
Version:        1.7.18
Release:        1%{?dist}
Summary:        Ultralightweight JSON parser in ANSI C

License:        MIT and ASL 2.0
URL:            https://github.com/DaveGamble/cJSON
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  cmake

%description
cJSON aims to be the dumbest possible parser that you can get your job
done with. It's a single file of C, and a single header file.

%package devel
Summary:        Development files for cJSON
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
Requires:       cmake-filesystem

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use cJSON.

%prep
%autosetup -n cJSON-%{version}

%build
%cmake -DENABLE_CJSON_TEST=ON -DENABLE_TARGET_EXPORT=ON
%cmake_build

%install
%cmake_install
rm -f %{buildroot}%{_libdir}/*.{la,a}

%check
%ctest

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSE
%doc README.md
%{_libdir}/libcjson*.so.*

%files devel
%doc CHANGELOG.md CONTRIBUTORS.md
%{_libdir}/libcjson.so
%{_libdir}/pkgconfig/libcjson.pc
%{_libdir}/cmake/cJSON/
%{_includedir}/cjson/

%changelog
* Wed May 28 2025 Odilon Sousa <osousa@redhat.com> - 1.7.18-1
- Release cjson 1.7.18

* Fri Jan 26 2024 Eric D. Helms <ericdhelms@gmail.com> - 1.7.17-1
- Release 1.7.17

* Wed Mar 01 2023 Petr Menšík <pemensik@redhat.com> - 1.7.15-1
- Update to 1.7.15
- Export also CMake module

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 11 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.7.14-2
- Adjust license tag, it's MIT and ASL 2.0 (#1905273)
- Replace ldconfig scriplets
- Fix requires:

* Mon Dec 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.7.14-1
- Initial package for Fedora
