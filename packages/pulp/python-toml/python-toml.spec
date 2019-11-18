# Created by pyp2rpm-3.3.3
%global pypi_name toml

Name:           python-%{pypi_name}
Version:        0.10.0
Release:        1%{?dist}
Summary:        Python Library for Tom's Obvious, Minimal Language

License:        MIT
URL:            https://github.com/uiri/toml
Source0:        https://files.pythonhosted.org/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
TOML A Python library for parsing and creating TOML < module passes the TOML
test suite < also:* The TOML Standard < * The currently supported TOML
specification <

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
TOML A Python library for parsing and creating TOML < module passes the TOML
test suite < also:* The TOML Standard < * The currently supported TOML
specification <

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
* Mon Nov 18 2019 Evgeni Golov - 0.10.0-1
- Initial package.
