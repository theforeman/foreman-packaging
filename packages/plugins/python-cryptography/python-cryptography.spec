%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

%define debug_package %{nil}

# Created by pyp2rpm-3.3.3
%global pypi_name cryptography

Name:           python-%{pypi_name}
Version:        43.0.1
Release:        2%{?dist}
Summary:        cryptography is a package which provides cryptographic recipes and primitives to Python developers

License:        BSD or Apache License, Version 2.0
URL:            https://github.com/pyca/cryptography
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Source1:        https://downloads.theforeman.org/vendor/%{pypi_name}-%{version}-vendor.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildConflicts: python%{python3_pkgversion}-cffi = 1.11.3
BuildRequires:  python%{python3_pkgversion}-cffi >= 1.12
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools-rust >= 1.7.0
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  python%{python3_pkgversion}-maturin >= 1
BuildRequires:  python%{python3_pkgversion}-maturin < 2
BuildRequires:  pyproject-rpm-macros

BuildRequires:  rust-toolset
BuildRequires:  openssl-devel
BuildRequires:  gcc

%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-cffi >= 1.12


%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}
%cargo_prep -V 1


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}.dist-info/


%changelog
* Mon Feb 03 2025 Odilon Sousa <osousa@redhat.com> - 43.0.1-2
- Rebuild against python 3.12

* Sun Sep 22 2024 Foreman Packaging Automation <packaging@theforeman.org> - 43.0.1-1
- Update to 43.0.1

* Wed Aug 07 2024 Odilon Sousa <osousa@redhat.com> - 42.0.8-1
- Release python-cryptography 42.0.8

* Fri Mar 22 2024 Odilon Sousa <osousa@redhat.com> - 42.0.5-1
- Release python-cryptography 42.0.5

* Tue Jan 30 2024 Odilon Sousa <osousa@redhat.com> - 41.0.6-1
- Release python-cryptography 41.0.6

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 38.0.4-5
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 38.0.4-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 38.0.4-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 38.0.4-2
- Build against python 3.11

* Wed Jan 25 2023 Odilon Sousa <osousa@redhat.com> - 38.0.4-1
- Release python-cryptography 38.0.4

* Tue Apr 26 2022 Odilon Sousa <osousa@redhat.com> - 3.4.8-1
- Release python-cryptography 3.4.8

* Mon Sep 13 2021 Evgeni Golov - 3.1.1-1
- Release python-cryptography 3.1.1

* Wed Sep 08 2021 Evgeni Golov - 2.9.2-2
- Build against Python 3.8

* Tue Apr 28 2020 Evgeni Golov 2.9.2-1
- Update to 2.9.2

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.8-2
- Bump release to build for el8

* Tue Nov 19 2019 Evgeni Golov - 2.8-1
- Initial package.
