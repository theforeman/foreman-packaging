%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.8
%global pypi_name python-daemon
%global srcname daemon

Name:           python%{python3_pkgversion}-%{srcname}
Version:        2.3.1
Release:        5%{?dist}
Summary:        Library to implement a well-behaved Unix daemon process

License:        Apache-2
URL:            https://pagure.io/python-daemon/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Patch0:         remove-twine-dependency.patch

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-docutils
BuildRequires:  python%{python3_pkgversion}-setuptools

%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Requires:       python%{python3_pkgversion}-docutils
Requires:       python%{python3_pkgversion}-lockfile >= 0.10

Obsoletes:      python3.11-%{srcname} < %{version}-%{release}

%description
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


%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE.ASF-2 LICENSE.GPL-3
%{python3_sitelib}/daemon
%{python3_sitelib}/python_daemon-%{version}-py%{python3_version}.egg-info


%changelog
* Wed Apr 30 2025 Odilon Sousa <osousa@redhat.com> - 2.3.1-5
- Obsolete python3.11 package for better upgrade

* Wed Jan 29 2025 Odilon Sousa <osousa@redhat.com> - 2.3.1-4
- Rebuild against python 3.12

* Mon Dec 18 2023 Evgeni Golov - 2.3.1-3
- Obsolete Python 3.9 package to smoothen upgrade path

* Mon Dec 18 2023 Odilon Sousa <osousa@redhat.com> - 2.3.1-2
- Rebuild against python 3.11

* Wed Aug 31 2022 Eric D. Helms <ericdhelms@gmail.com> - 2.3.1-1
- Initial package.
