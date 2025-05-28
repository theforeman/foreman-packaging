%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12
%define debug_package %{nil}

# Created by pyp2rpm-3.3.3
%global pypi_name MarkupSafe
%global srcname markupsafe

# Our EL8 buildroots default to Python 3.8, but let's also build 3.6, just to be safe
# to make dnf happy
%if 0%{?rhel} == 8
%bcond_without python39
%else
%bcond_with python3
%endif

Name:           python-%{srcname}
Version:        3.0.2
Release:        2%{?dist}
Summary:        Safely add untrusted strings to HTML/XML markup

License:        BSD-3-Clause
URL:            https://palletsprojects.com/p/markupsafe/
Source0:        https://files.pythonhosted.org/packages/source/m/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}


%description -n python%{python3_pkgversion}-%{srcname}
%{summary}

%if %{with python36}
%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python36-devel
Provides:       python36-%{srcname} = %{version}-%{release}

%description -n python3-%{srcname}
%{summary}
%endif

%prep
set -ex
%autosetup -n %{srcname}-%{version}
# Remove bundled egg-info
rm -rf %{srcname}.egg-info


%build
set -ex
%py3_build

%if %{with python36}
CFLAGS="${CFLAGS:-${RPM_OPT_FLAGS}}" LDFLAGS="${LDFLAGS:-${RPM_LD_FLAGS}}"\
 /usr/bin/python3.6 setup.py  build --executable="/usr/bin/python3.6 -s"
%endif


%install
set -ex
%py3_install

%if %{with python36}
CFLAGS="${CFLAGS:-${RPM_OPT_FLAGS}}" LDFLAGS="${LDFLAGS:-${RPM_LD_FLAGS}}"\
 /usr/bin/python3.6 setup.py  install --skip-build --root %{buildroot}
%endif


%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE.txt
%doc README.md
%{python3_sitearch}/markupsafe
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%if %{with python36}
%files -n python3-%{srcname}
/usr/lib64/python3.6/site-packages/markupsafe
/usr/lib64/python3.6/site-packages/%{pypi_name}-%{version}-py*.egg-info
%endif

%changelog
* Mon Feb 03 2025 Odilon Sousa <osousa@redhat.com> - 3.0.2-2
- Rebuild against python 3.12

* Wed Oct 23 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.0.2-1
- Update to 3.0.2

* Mon Oct 14 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.0.1-1
- Update to 3.0.1

* Mon Sep 16 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.1.5-1
- Update to 2.1.5

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 2.1.2-5
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 2.1.2-4
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 2.1.2-3
- Add python39 obsoletes to package

* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 2.1.2-2
- Build against python 3.11

* Fri Feb 03 2023 Odilon Sousa 2.1.2-1
- Update to 2.1.2

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 2.0.1-3
- Build against python 3.9

* Thu Jan 13 2022 Evgeni Golov - 2.0.1-2
- build markupsafe for Python 3.6 too

* Wed Nov 03 2021 Odilon Sousa 2.0.1-1
- Update to 2.0.1

* Mon Sep 06 2021 Evgeni Golov - 1.1.1-3
- Build against Python 3.8

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.1.1-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 1.1.1-1
- Initial package.
