# Created by pyp2rpm-3.3.3
%global pypi_name pulp-file

Name:           python-%{pypi_name}
Version:        0.2.0
Release:        1%{?dist}
Summary:        File plugin for the Pulp Project

License:        GPLv2+
URL:            https://pulpproject.org/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pulpcore < 3.3
BuildRequires:  python3-pulpcore >= 3.0
BuildRequires:  python3-setuptools

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3-pulpcore < 3.3
Requires:       python3-pulpcore >= 3.0
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
%{python3_sitelib}/pulp_file
%{python3_sitelib}/pulp_file-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Mar 18 2020 Samir Jha 0.2.0-1
- Update to 0.2.0

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.1.1-2
- Bump release to build for el8

* Wed Feb 05 2020 Evgeni Golov 0.1.1-1
- Update to 0.1.1

* Fri Dec 13 2019 Evgeni Golov 0.1.0-1
- Update to 0.1.0

* Mon Nov 18 2019 Evgeni Golov - 0.1.0rc1-1
- Initial package.
