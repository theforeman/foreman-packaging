# Created by pyp2rpm-3.3.3
%global pypi_name pycryptodomex

Name:           python-%{pypi_name}
Version:        3.9.6
Release:        2%{?dist}
Summary:        Cryptographic library for Python

License:        BSD, Public Domain, Apache
URL:            https://www.pycryptodome.org
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
%license Doc/LEGAL/copy/LICENSE.libtom Doc/LEGAL/copy/LICENSE.orig Doc/LEGAL/copy/LICENSE.python-2.2 Doc/ocb/license1.pdf Doc/ocb/license2.pdf Doc/ocb/license3.pdf Doc/src/license.rst LICENSE.rst
%doc Doc/ocb/README.txt README.rst lib/Cryptodome/SelfTest/Cipher/test_vectors/AES/README.txt lib/Cryptodome/SelfTest/Cipher/test_vectors/TDES/README.txt lib/Cryptodome/SelfTest/Hash/test_vectors/keccak/readme.txt lib/Cryptodome/SelfTest/Signature/test_vectors/ECDSA/README.txt
%{python3_sitearch}/Cryptodome
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.9.6-2
- Bump release to build for el8

* Wed Feb 05 2020 Evgeni Golov 3.9.6-1
- Update to 3.9.6

* Tue Nov 19 2019 Evgeni Golov - 3.9.4-1
- Initial package.
