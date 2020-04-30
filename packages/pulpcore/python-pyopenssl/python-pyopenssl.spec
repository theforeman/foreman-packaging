# Created by pyp2rpm-3.3.3
%global pypi_name pyOpenSSL
%global srcname pyopenssl

Name:           python-%{srcname}
Version:        19.1.0
Release:        1%{?dist}
Summary:        Python wrapper module around the OpenSSL library

License:        Apache License, Version 2.0
URL:            https://pyopenssl.org/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-cryptography >= 2.8
BuildRequires:  python3-setuptools
BuildRequires:  python3-six >= 1.5.2

%description
%{summary}

%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
Requires:       python3-cryptography >= 2.8
Requires:       python3-six >= 1.5.2

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
%{python3_sitelib}/OpenSSL
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Thu Apr 30 2020 Evgeni Golov - 19.1.0-1
- Initial package.
