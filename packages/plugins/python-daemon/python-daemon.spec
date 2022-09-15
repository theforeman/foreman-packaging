%{?scl:%scl_package python-%{srcname}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.8
%global pypi_name python-daemon
%global srcname daemon

Name:           %{?scl_prefix}python-%{srcname}
Version:        2.3.1
Release:        1%{?dist}
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
* Wed Aug 31 2022 Eric D. Helms <ericdhelms@gmail.com> - 2.3.1-1
- Initial package.
