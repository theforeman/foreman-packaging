Name:           cjson
Version:        1.7.14
Release:        6%{?dist}
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

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use cJSON.

%prep
%autosetup -n cJSON-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install
rm -f %{buildroot}%{_libdir}/*.{la,a}
rm -f %{buildroot}%{_libdir}/cmake/cJSON/*.cmake

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
%{_includedir}/cjson/

%changelog
* Mon Jan 08 2024 Evgeni Golov - 1.7.14-6
- Use correct cmake macros for EL9 builds

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
