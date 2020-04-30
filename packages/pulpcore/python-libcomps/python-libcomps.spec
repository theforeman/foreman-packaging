# Created by pyp2rpm-3.3.3
%global pypi_name libcomps

Name:           python-%{pypi_name}
Version:        0.1.14.post1
Release:        1%{?dist}
Summary:        Comps XML file manipulation library

License:        GPLv2+
URL:            https://github.com/rpm-software-management
Source0:        https://files.pythonhosted.org/packages/source/l/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Patch1:         Python_ADDITIONAL_VERSIONS.patch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  libxml2-devel
BuildRequires:  check-devel
BuildRequires:  expat-devel
BuildRequires:  zlib-devel

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{version} -p1
mkdir build

%build
pushd build
  %cmake ../libcomps/ -DPYTHON_DESIRED:STRING=3 -DENABLE_DOCS=OFF -DENABLE_TESTS=OFF
  make %{?_smp_mflags} RPM_OPT_FLAGS="%{optflags}"
popd

%install
pushd build
  make install DESTDIR=%{buildroot}
popd

%files -n python3-%{pypi_name}
%doc README.md
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-*-py%{python3_version}.egg-info
%{_libdir}/libcomps*
%exclude %{_includedir}/libcomps/
%exclude %{_libdir}/pkgconfig/libcomps.pc

%changelog
* Thu Apr 30 2020 Evgeni Golov - 0.1.14.post1-1
- Initial package.
