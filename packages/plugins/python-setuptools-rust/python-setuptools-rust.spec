%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.7
%global pypi_name setuptools-rust
%global pkg_name setuptools_rust

Name:           python-%{pypi_name}
Version:        1.9.0
Release:        2%{?dist}
Summary:        Setuptools Rust extension plugin

License:        MIT
URL:            https://github.com/PyO3/setuptools-rust
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-setuptools >= 62.4
BuildRequires:  python%{python3_pkgversion}-setuptools-scm
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros


%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Requires:       python%{python3_pkgversion}-semantic-version >= 2.6
Requires:       python%{python3_pkgversion}-semantic-version < 3
Requires:       python%{python3_pkgversion}-setuptools >= 62.4


%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}

%prep
set -ex
%autosetup -n %{pypi_name}-%{version}


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%{python3_sitelib}/%{pkg_name}
%{python3_sitelib}/%{pkg_name}-%{version}.dist-info/


%changelog
* Fri Jan 31 2025 Odilon Sousa <osousa@redhat.com> - 1.9.0-2
- Rebuild against python 3.12

* Fri Mar 22 2024 Odilon Sousa <osousa@redhat.com> - 1.9.0-1
- Release python-setuptools-rust 1.9.0

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 1.6.0-4
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 1.6.0-3
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 1.6.0-2
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.6.0-1
- Release python-setuptools-rust 1.6.0

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 0.11.5-3
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane - 0.11.5-2
- Build against python 3.9.

* Thu Sep 09 2021 Evgeni Golov - 0.11.5-1
- Initial package.
