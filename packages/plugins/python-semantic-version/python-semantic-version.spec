%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name semantic-version

Name:           python-%{pypi_name}
Version:        2.10.0
Release:        6%{?dist}
Summary:        A library implementing the 'SemVer' scheme

License:        BSD
URL:            https://github.com/rbarrois/python-semanticversion
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/semantic_version-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools >= 0.8


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}


%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
set -ex
%autosetup -n semantic_version-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
set -ex
%py3_build


%install
set -ex
%py3_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/semantic_version
%{python3_sitelib}/semantic_version-%{version}-py%{python3_version}.egg-info


%changelog
* Fri Jan 31 2025 Odilon Sousa <osousa@redhat.com> - 2.10.0-6
- Rebuild against python 3.12

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 2.10.0-5
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 2.10.0-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 2.10.0-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 2.10.0-2
- Build against python 3.11

* Wed Aug 24 2022 Odilon Sousa <osousa@redhat.com> - 2.10.0-1
- Release python-semantic-version 2.10.0

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 2.8.5-3
- Build against python 3.9

* Mon Sep 06 2021 Evgeni Golov - 2.8.5-2
- Build against Python 3.8

* Mon Jul 20 2020 Evgeni Golov 2.8.5-1
- Update to 2.8.5

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.8.4-2
- Bump release to build for el8

* Tue Jan 28 2020 Evgeni Golov - 2.8.4-1
- Initial package.
