%{?scl:%scl_package python-%{srcname}}
%{!?scl:%global pkg_name %{name}}
%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.8
%global pypi_name python-daemon
%global srcname daemon

Name:           %{?scl_prefix}python-%{srcname}
Version:        2.3.1
Release:        3%{?dist}
Summary:        Library to implement a well-behaved Unix daemon process

License:        Apache-2
URL:            https://pagure.io/python-daemon/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Patch0:         remove-twine-dependency.patch

BuildArch:      noarch
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-docutils
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Requires:       %{?scl_prefix}python%{python3_pkgversion}-docutils
Requires:       %{?scl_prefix}python%{python3_pkgversion}-lockfile >= 0.10

%if 0%{?rhel} == 8
Obsoletes:      python39-%{srcname} < %{version}-%{release}
%endif

%description -n %{?scl_prefix}python%{python3_pkgversion}-%{srcname}
%{summary}


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
%{?scl:EOF}


%build
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%py3_build
%{?scl:EOF}


%install
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%py3_install
%{?scl:EOF}


%files -n %{?scl_prefix}python%{python3_pkgversion}-%{srcname}
%license LICENSE.ASF-2 LICENSE.GPL-3
%{python3_sitelib}/daemon
%{python3_sitelib}/python_daemon-%{version}-py%{python3_version}.egg-info


%changelog
* Mon Dec 18 2023 Evgeni Golov - 2.3.1-3
- Obsolete Python 3.9 package to smoothen upgrade path

* Mon Dec 18 2023 Odilon Sousa <osousa@redhat.com> - 2.3.1-2
- Rebuild against python 3.11

* Wed Aug 31 2022 Eric D. Helms <ericdhelms@gmail.com> - 2.3.1-1
- Initial package.
