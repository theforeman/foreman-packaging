# Created by pyp2rpm-3.3.3
%global pypi_name pymongo

Name:           python-%{pypi_name}
Version:        3.10.1
Release:        1%{?dist}
Summary:        Python driver for MongoDB

License:        Apache License, Version 2.0
URL:            http://github.com/mongodb/mongo-python-driver
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

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
%license LICENSE
%doc tools/README.rst README.rst
%{python3_sitearch}/bson
%{python3_sitearch}/gridfs
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Jan 28 2020 Evgeni Golov - 3.10.1-1
- Initial package.
