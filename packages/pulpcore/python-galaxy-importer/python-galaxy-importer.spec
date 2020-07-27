# Created by pyp2rpm-3.3.3
%global pypi_name galaxy-importer

Name:           python-%{pypi_name}
Version:        0.2.5
Release:        2%{?dist}
Summary:        Galaxy content importer

License:        Apache-2.0
URL:            https://github.com/ansible/galaxy-importer
Source0:        https://files.pythonhosted.org/packages/source/g/%{pypi_name}/galaxy_importer-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
# We don't care if Ansible is Python 2 or 3 as we just call the CLI
Requires:       ansible
Requires:       /usr/bin/ansible-test
# technically, we need ansible-lint to lint imported roles
# but building it on EL is hard, and roles should import fine without
#Requires:      python3-ansible-lint < 5.0
#Requires:      python3-ansible-lint >= 4.2.0
Requires:       python3-attrs < 20
Requires:       python3-attrs >= 19.3.0
Requires:       python3-bleach < 4
Requires:       python3-bleach >= 3.1.3
Requires:       python3-bleach-whitelist < 1
Requires:       python3-bleach-whitelist >= 0.0.10
Requires:       python3-flake8 < 4
Requires:       python3-flake8 >= 3.7.9
Requires:       python3-markdown < 4
Requires:       python3-markdown >= 3.2.1
Requires:       python3-pyyaml < 6
Requires:       python3-pyyaml >= 5.2
Requires:       python3-requests < 3
Requires:       python3-requests >= 2.23.0
Requires:       python3-semantic-version < 3
Requires:       python3-semantic-version >= 2.8.4

%description -n python3-%{pypi_name}
%{summary}

%prep
%autosetup -n galaxy_importer-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

sed -i -E '/\s+ansible($|-lint)/d' setup.cfg

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license galaxy_importer/utils/spdx_licenses.py galaxy_importer/utils/spdx_licenses.json
%doc README.md
%{python3_sitelib}/galaxy_importer
%{python3_sitelib}/tests
%{python3_sitelib}/galaxy_importer-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Jul 27 2020 Evgeni Golov - 0.2.5-2
- Patch out Ansible and ansible-lint dependencies from the Python egg

* Tue Jun 23 2020 Evgeni Golov - 0.2.5-1
- Initial package.
