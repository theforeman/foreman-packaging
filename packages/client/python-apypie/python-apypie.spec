# Created by pyp2rpm-3.3.2
%global pypi_name apypie

Name:           python-%{pypi_name}
Version:        0.0.3
Release:        1%{?dist}
Summary:        Apipie bindings for Python

License:        MIT
URL:            https://github.com/Apipie/apypie
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
Apipie bindings for Python

%package -n     python2-%{pypi_name}
Summary:        Apipie bindings for Python
Requires:       python-requests

%description -n python2-%{pypi_name}
Apipie bindings for Python2

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        Apipie bindings for Python
Requires:       python%{python3_pkgversion}-requests

%description -n python%{python3_pkgversion}-%{pypi_name}
Apipie bindings for Python3


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%{__python2} setup.py build
%{__python3} setup.py build

%install
# Must do the default python version install last because
# the scripts in /usr/bin are overwritten with every setup.py install.
%{__python3} setup.py install --skip-build --root %{buildroot}
%{__python2} setup.py install --skip-build --root %{buildroot}

%files -n python2-%{pypi_name}
%doc README.md
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python%{python3_pkgversion}-%{pypi_name}
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Wed Jul 17 2019 Evgeni Golov - 0.0.3-1
- Initial package.
