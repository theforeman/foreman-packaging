# Created by pyp2rpm-3.3.3
%global pypi_name pulp-ansible

Name:           python-%{pypi_name}
Version:        0.2.0b14
Release:        1%{?dist}
Summary:        Pulp plugin to manage Ansible content, e.g. roles

License:        GPLv2+
URL:            https://github.com/pulp/pulp_ansible
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3-PyYAML
Requires:       python3-galaxy-importer
Requires:       python3-packaging
Requires:       python3-pulpcore < 3.5
Requires:       python3-pulpcore >= 3.0
Requires:       python3-semantic-version
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
%{python3_sitelib}/pulp_ansible
%{python3_sitelib}/pulp_ansible-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Jun 23 2020 Evgeni Golov - 0.2.0b14-1
- Initial package.
