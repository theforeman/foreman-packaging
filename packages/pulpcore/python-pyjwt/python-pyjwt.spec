# Created by pyp2rpm-3.3.3
%global pypi_name PyJWT
%global srcname pyjwt

Name:           python-%{srcname}
Version:        1.7.1
Release:        1%{?dist}
Summary:        JSON Web Token implementation in Python

License:        MIT
URL:            http://github.com/jpadilla/pyjwt
Source0:        https://files.pythonhosted.org/packages/source/P/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
%{summary}

%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
Provides:       python3-jwt = %{version}-%{release}
Requires:       python3-cryptography >= 1.4
Requires:       python3-setuptools

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
%{_bindir}/pyjwt
%{python3_sitelib}/jwt
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Nov 19 2019 Evgeni Golov - 1.7.1-1
- Initial package.
