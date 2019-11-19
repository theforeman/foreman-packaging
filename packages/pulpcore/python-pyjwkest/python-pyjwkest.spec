# Created by pyp2rpm-3.3.3
%global pypi_name pyjwkest

Name:           python-%{pypi_name}
Version:        1.4.2
Release:        1%{?dist}
Summary:        Python implementation of JWT, JWE, JWS and JWK

License:        Apache 2.0
URL:            None
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3-future
Requires:       python3-pycryptodomex
Requires:       python3-requests
Requires:       python3-six

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
%doc README.rst
%{_bindir}/gen_symkey.py
%{_bindir}/jwdecrypt.py
%{_bindir}/jwenc.py
%{_bindir}/jwk_create.py
%{_bindir}/jwk_export.py
%{_bindir}/jwkutil.py
%{_bindir}/peek.py
%{python3_sitelib}/jwkest
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Nov 19 2019 Evgeni Golov - 1.4.2-1
- Initial package.
