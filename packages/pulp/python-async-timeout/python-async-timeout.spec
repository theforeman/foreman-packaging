# Created by pyp2rpm-3.3.3
%global pypi_name async-timeout

Name:           python-%{pypi_name}
Version:        3.0.1
Release:        1%{?dist}
Summary:        Timeout context manager for asyncio programs

License:        Apache 2
URL:            https://github.com/aio-libs/async_timeout/
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
async-timeout asyncio-compatible timeout context manager. Usage example - The
context manager is useful in cases when you want to apply timeout

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
async-timeout asyncio-compatible timeout context manager. Usage example - The
context manager is useful in cases when you want to apply timeout

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
%{python3_sitelib}/async_timeout
%{python3_sitelib}/async_timeout-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Nov 18 2019 Evgeni Golov - 3.0.1-1
- Initial package.
