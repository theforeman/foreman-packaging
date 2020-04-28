# Created by pyp2rpm-3.3.3
%global pypi_name python-gnupg
%global srcname gnupg

Name:           python-%{srcname}
Version:        0.4.6
Release:        1%{?dist}
Summary:        A wrapper for the Gnu Privacy Guard (GPG or GnuPG)

License:        Copyright (C) 2008-2019 by Vinay Sajip. All Rights Reserved. See LICENSE.txt for license.
URL:            https://docs.red-dove.com/python-gnupg/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
%{summary}

%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

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
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/__pycache__/gnupg.*
%{python3_sitelib}/gnupg.py
%{python3_sitelib}/python_gnupg-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Apr 28 2020 Evgeni Golov 0.4.6-1
- Update to 0.4.6

* Wed Mar 18 2020 Samir Jha - 0.4.5-1
- Initial package.
