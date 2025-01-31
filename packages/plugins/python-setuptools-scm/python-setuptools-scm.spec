%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name setuptools-scm

Name:           python-%{pypi_name}
Version:        8.1.0
Release:        1%{?dist}
Summary:        the blessed package to manage your versions by scm tags

License:        MIT
URL:            https://github.com/pypa/setuptools_scm/
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/setuptools_scm-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-rpm-macros
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-packaging >= 20.0
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  python%{python3_pkgversion}-pip


%description
setuptools_scm setuptools_scm handles managing your Python package versions in
SCM metadata instead of declaring them as the version argument or in a SCM
managed file.It also handles file finders for the supported SCMs. setup.py
usage To use setuptools_scm just modify your project's setup.py file like
this:* Add setuptools_scm to the setup_requires parameter. * Add the
use_scm_version...


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Requires:       python%{python3_pkgversion}-setuptools >= 45
Requires:       python%{python3_pkgversion}-packaging >= 20.0


%description -n python%{python3_pkgversion}-%{pypi_name}
setuptools_scm setuptools_scm handles managing your Python package versions in
SCM metadata instead of declaring them as the version argument or in a SCM
managed file.It also handles file finders for the supported SCMs. setup.py
usage To use setuptools_scm just modify your project's setup.py file like
this:* Add setuptools_scm to the setup_requires parameter. * Add the
use_scm_version...


%prep
set -ex
%autosetup -n setuptools_scm-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%{python3_sitelib}/setuptools_scm
%{python3_sitelib}/setuptools_scm-%{version}.dist-info/


%changelog
* Fri Jan 31 2025 Odilon Sousa <osousa@redhat.com> - 8.1.0-1
- Release python-setuptools-scm 8.1.0

* Fri Jan 31 2025 Odilon Sousa <osousa@redhat.com> - 7.1.0-5
- Rebuild against python 3.12

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 7.1.0-4
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 7.1.0-3
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 7.1.0-2
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 7.1.0-1
- Release python-setuptools-scm 7.1.0

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 6.4.0-2
- Build against python 3.11

* Mon Jul 24 2023 Odilon Sousa <osousa@redhat.com> - 6.4.0-1
- Release python-setuptools-scm 6.4.0

* Thu Apr 21 2022 Yanis Guenane - 3.5.0-3
- Build against Python 3.9

* Mon Sep 06 2021 Evgeni Golov - 3.5.0-2
- Build against Python 3.8

* Wed Mar 31 2021 Evgeni Golov - 3.5.0-1
- Release python-setuptools-scm 3.5.0

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.4.3-2
- Bump release to build for el8

* Wed Jan 29 2020 Evgeni Golov 3.4.3-1
- Update to 3.4.3

* Fri Nov 15 2019 Evgeni Golov - 3.3.3-1
- Initial package.
