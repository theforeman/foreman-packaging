# Created by pyp2rpm-3.3.2
%global pypi_name pulp-deb

Name:           python-%{pypi_name}
Version:        2.3.0
Release:        0.1.b1%{?dist}
Summary:        pulp-deb plugin for the Pulp Project

License:        GPLv2+
URL:            https://pulpproject.org/#deb
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}b1.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-pulpcore < 3.4
Requires:       python3-pulpcore >= 3.3
Requires:       python3-debian >= 0.1.36
Requires:       python3-setuptools
%description -n python3-%{pypi_name}



%prep
%autosetup -n %{pypi_name}-%{version}b1
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%{python3_sitelib}/pulp_deb
%{python3_sitelib}/pulp_deb-%{version}b1-py?.?.egg-info

%changelog
* Thu Apr 30 2020 ATIX AG <info@atix.de> - 2.3.0-0.1.b1
- Initial package.
