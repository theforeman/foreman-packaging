# Created by pyp2rpm-3.3.3
%global pypi_name pulp-rpm

Name:           python-%{pypi_name}
Version:        3.3.1
Release:        2%{?dist}
Summary:        RPM plugin for the Pulp Project

License:        GPLv2+
URL:            http://www.pulpproject.org
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
%if 0%{?rhel} == 7
Requires:       python36-gobject
%else
Requires:       python3-gobject
%endif
Requires:       python3-createrepo_c < 1.0
Requires:       python3-createrepo_c >= 0.15.10
Requires:       python3-jsonschema
Requires:       python3-libcomps >= 0.1.11
Conflicts:      python3-libcomps >= 0.2
Requires:       python3-productmd >= 1.25
Requires:       python3-pulpcore < 3.4
Requires:       python3-pulpcore >= 3.3
Requires:       python3-setuptools
Requires:       python3-solv

%description -n python3-%{pypi_name}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# remove "solv" dependency from setup.py as python3-solv does not provide an egg
sed -i "/'solv'/d" setup.py

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/pulp_rpm
%{python3_sitelib}/pulp_rpm-%{version}-py%{python3_version}.egg-info

%changelog
* Tue May 26 2020 Evgeni Golov - 3.3.1-2
- remove "solv" dependency from setup.py as python3-solv does not provide an egg

* Fri May 08 2020 Evgeni Golov - 3.3.1-1
- Release python-pulp-rpm 3.3.1

* Thu Apr 30 2020 Evgeni Golov - 3.3.0-1
- Initial package.
