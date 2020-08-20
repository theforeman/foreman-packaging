# Created by pyp2rpm-3.3.3
%global pypi_name python-dateutil
%global srcname dateutil

Name:           python-%{srcname}
Version:        2.8.1
Release:        2%{?dist}
Summary:        Extensions to the standard Python datetime module

License:        Dual License
URL:            https://dateutil.readthedocs.io
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools-scm
BuildRequires:  python3-six >= 1.5

Obsoletes: python36-dateutil

%description
%{summary}

%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
Requires:       python3-six >= 1.5

%description -n python3-%{srcname}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/dateutil
%{python3_sitelib}/python_dateutil-%{version}-py%{python3_version}.egg-info

%changelog
* Thu Aug 20 2020 Eric D. Helms <ericdhelms@gmail.com> - 2.8.1-2
- Obsolete python36-dateutil

* Fri Jul 17 2020 Evgeni Golov - 2.8.1-1
- Initial package.
