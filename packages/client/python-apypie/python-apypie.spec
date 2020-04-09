# Created by pyp2rpm-3.3.2
%global pypi_name apypie

%if 0%{?rhel} == 7 || (0%{?fedora} && 0%{?fedora} <= 29)
%bcond_without python2
%else
%bcond_with python2
%endif

%if 0%{?rhel} >= 8 || 0%{?fedora} || 0%{?epel}
%bcond_without python3
%else
%bcond_with python3
%endif

Name:           python-%{pypi_name}
Version:        0.2.2
Release:        1%{?dist}
Summary:        Apipie bindings for Python

License:        MIT
URL:            https://github.com/Apipie/apypie
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%if %{with python2}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%endif

%if %{with python3}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%endif

%description
Python bindings for the Apipie - Ruby on Rails API documentation tool.

%if %{with python2}
%package -n     python2-%{pypi_name}
Summary:        Apipie bindings for Python2
Requires:       python-requests >= 2.4.2

%description -n python2-%{pypi_name}
Python2 bindings for the Apipie - Ruby on Rails API documentation tool.
%endif

%if %{with python3}
%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        Apipie bindings for Python3
Requires:       python%{python3_pkgversion}-requests >= 2.4.2

%description -n python%{python3_pkgversion}-%{pypi_name}
Python3 bindings for the Apipie - Ruby on Rails API documentation tool.
%endif

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%if %{with python2}
%{__python2} setup.py build
%endif
%if %{with python3}
%{__python3} setup.py build
%endif

%install
%if %{with python2}
%{__python2} setup.py install --skip-build --root %{buildroot}
%endif
%if %{with python3}
%{__python3} setup.py install --skip-build --root %{buildroot}
%endif

%if %{with python2}
%files -n python2-%{pypi_name}
%doc README.md
%license LICENSE
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif

%if %{with python3}
%files -n python%{python3_pkgversion}-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif

%changelog
* Thu Apr 09 2020 Evgeni Golov - 0.2.2-1
- Release python-apypie 0.2.2

* Wed Jan 08 2020 Evgeni Golov - 0.2.1-2
- Rebuild for EL8 client repository

* Mon Nov 25 2019 Evgeni Golov - 0.2.1-1
- Release python-apypie 0.2.1

* Mon Nov 04 2019 Evgeni Golov - 0.2.0-1
- Release python-apypie 0.2.0

* Tue Sep 10 2019 Evgeni Golov - 0.1.0-1
- Update to apypie 0.1.0

* Thu Aug 15 2019 Evgeni Golov - 0.0.5-1
- Update to apypie 0.0.5

* Fri Aug 09 2019 Evgeni Golov - 0.0.4-1
- Update to apypie 0.0.4

* Wed Jul 17 2019 Evgeni Golov - 0.0.3-1
- Initial package.
