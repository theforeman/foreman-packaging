# Created by pyp2rpm-3.3.3
%global pypi_name ansible-lint

Name:           %{pypi_name}
Version:        4.2.0
Release:        1%{?dist}
Summary:        Best practices checker for Ansible

License:        Apache-2.0
URL:            https://github.com/ansible/ansible-lint
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/ansible-lint-%{version}.tar.gz
Source1:        setup.py
BuildArch:      noarch

%if 0%{?rhel} == 7
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  python-six
BuildRequires:  PyYAML
BuildRequires:  python2-ruamel-yaml
%else
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
BuildRequires:  python3-pyyaml
BuildRequires:  python3-ruamel-yaml
BuildRequires:  python3-setuptools-scm
BuildRequires:  python3-setuptools_scm_git_archive
%endif
BuildRequires:  ansible >= 2.8

%description
%{summary}

%if 0%{?rhel} == 7
Requires:       PyYAML
Requires:       python-pathlib
Requires:       python-six
Requires:       python2-ruamel-yaml >= 0.15.34
%else
Requires:       python3-pyyaml
Requires:       python3-ruamel-yaml >= 0.15.34
Requires:       python3-six
Requires:       python3-typing-extensions
%endif
Requires:       ansible >= 2.8

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

cp %{SOURCE1} setup.py

%build
%if 0%{?rhel} == 7
%py_build
%else
%py3_build
%endif

%install
%if 0%{?rhel} == 7
%py_install
%else
%py3_install
%endif

%files -n %{pypi_name}
%doc README.rst
%if 0%{?rhel} == 7
%{python_sitelib}/ansiblelint
%{python_sitelib}/ansible_lint-%{version}-py%{python_version}.egg-info
%else
%{python3_sitelib}/ansiblelint
%{python3_sitelib}/ansible_lint-%{version}-py%{python3_version}.egg-info
%endif
%{_bindir}/ansible-lint

%changelog
* Mon Jul 27 2020 Evgeni Golov 4.2.0-1
- package ansible-lint
