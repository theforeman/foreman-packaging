# Created by pyp2rpm-3.3.3
%global pypi_name cryptography

Name:           python-%{pypi_name}
Version:        2.8
Release:        1%{?dist}
Summary:        cryptography is a package which provides cryptographic recipes and primitives to Python developers

License:        BSD or Apache License, Version 2.0
URL:            https://github.com/pyca/cryptography
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildConflicts: python3-cffi = 1.11.3
BuildRequires:  python3-cffi >= 1.8
BuildRequires:  python3-setuptools

BuildRequires:  openssl-devel
BuildRequires:  gcc

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Conflicts:      python3-cffi = 1.11.3
Requires:       python3-cffi >= 1.8
Requires:       python3-six >= 1.4.1

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
%license LICENSE LICENSE.APACHE LICENSE.BSD LICENSE.PSF
%doc README.rst
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Nov 19 2019 Evgeni Golov - 2.8-1
- Initial package.
