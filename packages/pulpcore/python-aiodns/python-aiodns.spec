# Created by pyp2rpm-3.3.3
%global pypi_name aiodns

Name:           python-%{pypi_name}
Version:        2.0.0
Release:        2%{?dist}
Summary:        Simple DNS resolver for asyncio

License:        None
URL:            http://github.com/saghul/aiodns
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3-pycares >= 3.0.0
Requires:       python3-typing

%description -n python3-%{pypi_name}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Apr 01 2020 Evgeni Golov - 2.0.0-2
- Add python3-typing to Requires

* Wed Mar 18 2020 Samir Jha - 2.0.0-1
- Initial package.
