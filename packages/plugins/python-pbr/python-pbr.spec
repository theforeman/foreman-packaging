%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11

# Created by pyp2rpm-3.3.3
%global pypi_name pbr

Name:           python-%{pypi_name}
Version:        5.8.0
Release:        5%{?dist}
Summary:        Python Build Reasonableness

License:        None
URL:            https://docs.openstack.org/pbr/latest/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-wheel >= 0.32.0

BuildArch:      noarch

%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-setuptools

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
%license LICENSE pbr/tests/testpackage/LICENSE.txt
%doc README.rst pbr/tests/testpackage/README.txt
%exclude %{_bindir}/pbr
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Sat Nov 11 2023 Odilon Sousa <osousa@redhat.com> - 5.8.0-5
- Build against python 3.11

* Mon Jun 13 2022 Odilon Sousa <osousa@redhat.com> - 5.8.0-4
- Exclude files in bin for a better upgrade from python38 to python39 and
  removes Obsolete

* Mon May 23 2022 Odilon Sousa <osousa@redhat.com> - 5.8.0-3
- Obsolete the old Python 3.8 package for smooth upgrade

* Fri Apr 22 2022 Odilon Sousa <osousa@redhat.com> - 5.8.0-2
- Rebuild against python 3.9

* Fri Feb 04 2022 Odilon Sousa <osousa@redhat.com> - 5.8.0-1
- Release python-pbr 5.8.0

* Wed Sep 08 2021 Evgeni Golov - 5.6.0-1
- Initial package.
