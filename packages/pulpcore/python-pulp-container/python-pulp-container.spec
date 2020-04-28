# Created by pyp2rpm-3.3.3
%global pypi_name pulp-container

Name:           python-%{pypi_name}
Version:        1.3.0
Release:        1%{?dist}
Summary:        Container plugin for the Pulp Project

License:        GPLv2+
URL:            https://pulpproject.org/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
Requires:       python3-ecdsa >= 0.13.2
Conflicts:      python3-ecdsa >= 0.14
Requires:       python3-pyjwkest >= 1.4.0
Conflicts:      python3-pyjwkest >= 1.5
Requires:       python3-pyjwt >= 1.7.1
Conflicts:      python3-pyjwt >= 1.8
BuildRequires:  python3-setuptools

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3-ecdsa >= 0.13.2
Conflicts:      python3-ecdsa >= 0.14
Requires:       python3-pulpcore < 3.4
Requires:       python3-pulpcore >= 3.3
Requires:       python3-pyjwkest >= 1.4.0
Conflicts:      python3-pyjwkest >= 1.5
Requires:       python3-pyjwt >= 1.7.1
Conflicts:      python3-pyjwt >= 1.8
Requires:       python3-setuptools

%description -n python3-%{pypi_name}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/pulp_container
%{python3_sitelib}/pulp_container-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Apr 28 2020 Evgeni Golov 1.3.0-1
- Update to 1.3.0

* Wed Mar 18 2020 Samir Jha 1.2.0-1
- Update to 1.2.0

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.0.0-2
- Bump release to build for el8

* Fri Dec 13 2019 Evgeni Golov 1.0.0-1
- Update to 1.0.0

* Tue Nov 19 2019 Evgeni Golov - 1.0.0rc1-1
- Initial package.
