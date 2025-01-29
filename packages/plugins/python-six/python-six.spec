%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name six

Name:           python-%{pypi_name}
Version:        1.17.0
Release:        1%{?dist}
Summary:        Python 2 and 3 compatibility utilities

License:        MIT
URL:            https://github.com/benjaminp/six
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
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
%{python3_sitelib}/__pycache__/%{pypi_name}.*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Wed Dec 11 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.17.0-1
- Update to 1.17.0

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 1.16.0-6
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 1.16.0-5
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 1.16.0-4
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 1.16.0-3
- Build against python 3.11

* Fri Apr 22 2022 Odilon Sousa <osousa@redhat.com> - 1.16.0-2
- Rebuild against python 3.9

* Tue Nov 09 2021 Odilon Sousa <osousa@redhat.com> - 1.16.0-1
- Release python-six 1.16.0

* Mon Sep 06 2021 Evgeni Golov - 1.15.0-2
- Build against Python 3.8

* Thu Jun 04 2020 Evgeni Golov 1.15.0-1
- Update to 1.15.0

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.14.0-2
- Bump release to build for el8

* Fri Jan 17 2020 Evgeni Golov 1.14.0-1
- Update to 1.14.0

* Mon Nov 18 2019 Evgeni Golov - 1.13.0-1
- Initial package.
