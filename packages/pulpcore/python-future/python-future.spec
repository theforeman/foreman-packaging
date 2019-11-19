# Created by pyp2rpm-3.3.3
%global pypi_name future

Name:           python-%{pypi_name}
Version:        0.18.2
Release:        1%{?dist}
Summary:        Clean single-source support for Python 3 and 2

License:        MIT
URL:            https://python-future.org
Source0:        https://files.pythonhosted.org/packages/source/f/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3-setuptools

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
%license docs/_themes/LICENSE LICENSE.txt
%doc README.rst
%{_bindir}/futurize
%{_bindir}/pasteurize
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/libfuturize
%{python3_sitelib}/libpasteurize
%{python3_sitelib}/past
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Nov 19 2019 Evgeni Golov - 0.18.2-1
- Initial package.
