# Created by pyp2rpm-3.3.3
%global pypi_name dynaconf

Name:           python-%{pypi_name}
Version:        2.2.0
Release:        1%{?dist}
Summary:        The dynamic configurator for your Python Project

License:        MIT
URL:            https://github.com/rochacbruno/dynaconf
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools >= 38.6.0

%description
[![Dynaconf]( **dynaconf** - The **dyna**mic **conf**igurator for your Python
Project[![MIT License]( [![PyPI]( [![PyPI]( ![PyPI - Downloads]( [![Build
Status]( ![Azure DevOps builds (branch)]( ![Azure DevOps builds (branch)](
[![codecov]( [![Codacy Badge]( ![GitHub issues]( ![GitHub stars]( ![GitHub
Release Date]( ![GitHub commits since latest release]( ![GitHub last commit](
[![Code Style Black](

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-box
Requires:       python3-click
Requires:       python3-dotenv
Requires:       python3-setuptools
Requires:       python3-toml
%description -n python3-%{pypi_name}
[![Dynaconf]( **dynaconf** - The **dyna**mic **conf**igurator for your Python
Project[![MIT License]( [![PyPI]( [![PyPI]( ![PyPI - Downloads]( [![Build
Status]( ![Azure DevOps builds (branch)]( ![Azure DevOps builds (branch)](
[![codecov]( [![Codacy Badge]( ![GitHub issues]( ![GitHub stars]( ![GitHub
Release Date]( ![GitHub commits since latest release]( ![GitHub last commit](
[![Code Style Black](

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
%doc README.md
%{_bindir}/dynaconf
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Nov 18 2019 Evgeni Golov - 2.2.0-1
- Initial package.
