# Created by pyp2rpm-3.3.3
%global pypi_name redis

Name:           python-%{pypi_name}
Version:        3.1.0
Release:        1%{?dist}
Summary:        Python client for Redis key-value store

License:        MIT
URL:            https://github.com/andymccurdy/redis-py
Source0:        https://files.pythonhosted.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
The Python interface to the Redis key-value store. Installation redis-py
requires a running Redis server. See Redis's quickstart < for installation
instructions.redis-py can be installed using pip similar to other Python
packages. Do not use sudo

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
The Python interface to the Redis key-value store. Installation redis-py
requires a running Redis server. See Redis's quickstart < for installation
instructions.redis-py can be installed using pip similar to other Python
packages. Do not use sudo

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
* Mon Nov 18 2019 Evgeni Golov - 3.1.0-1
- Initial package.
