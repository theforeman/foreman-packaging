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
Version:        0.2.0
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
Apipie bindings for Python

%if %{with python2}
%package -n     python2-%{pypi_name}
Summary:        Apipie bindings for Python
Requires:       python-requests >= 2.4.2

%description -n python2-%{pypi_name}
Apipie bindings for Python2
%endif

%if %{with python3}
%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        Apipie bindings for Python
Requires:       python%{python3_pkgversion}-requests >= 2.4.2

%description -n python%{python3_pkgversion}-%{pypi_name}
Apipie bindings for Python3
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
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif

%if %{with python3}
%files -n python%{python3_pkgversion}-%{pypi_name}
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif

%changelog
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
