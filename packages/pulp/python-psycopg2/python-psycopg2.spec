# Created by pyp2rpm-3.3.3
%global pypi_name psycopg2

Name:           python-%{pypi_name}
Version:        2.8.4
Release:        1%{?dist}
Summary:        psycopg2 - Python-PostgreSQL Database Adapter

License:        LGPL with exceptions or ZPL
URL:            http://initd.org/psycopg/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  postgresql-devel

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

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
%license doc/src/license.rst LICENSE doc/COPYING.LESSER
%doc doc/README.rst README.rst
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Nov 18 2019 Evgeni Golov - 2.8.4-1
- Initial package.
