%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name pycparser

Name:           python-%{pypi_name}
Version:        2.22
Release:        2%{?dist}
Summary:        C parser in Python

License:        BSD
URL:            https://github.com/eliben/pycparser
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}


%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}
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
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Feb 03 2025 Odilon Sousa <osousa@redhat.com> - 2.22-2
- Rebuild against python 3.12

* Mon Sep 16 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.22-1
- Update to 2.22

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 2.21-6
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 2.21-5
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 2.21-4
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 2.21-3
- Build against python 3.11

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 2.21-2
- Build against python 3.9

* Fri Feb 04 2022 Odilon Sousa <osousa@redhat.com> - 2.21-1
- Release python-pycparser 2.21

* Mon Sep 06 2021 Evgeni Golov - 2.20-2
- Build against Python 3.8

* Wed Mar 18 2020 Samir Jha 2.20-1
- Update to 2.20

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.19-2
- Bump release to build for el8

* Tue Nov 19 2019 Evgeni Golov - 2.19-1
- Initial package.
