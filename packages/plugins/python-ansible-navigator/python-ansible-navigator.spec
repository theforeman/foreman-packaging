%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

%global pypi_name ansible-navigator

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        25.9.0
Release:        2%{?dist}
Summary:        A text-based user interface (TUI) for Ansible

License:        Apache-2.0
URL:            https://github.com/ansible/ansible-navigator/
Source0:        https://files.pythonhosted.org/packages/06/fa/caa4ca091c0e4d5d9afa1da859e5f87fa3ddd1e35142d19e5a5eafffacd5/ansible_navigator-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pbr
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools-scm
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  pyproject-rpm-macros

Requires:       podman
Requires:       python%{python3_pkgversion}-PyYAML
Requires:       python%{python3_pkgversion}-setuptools

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Provides:	%{pypi_name}
Obsoletes:      python3.11-%{pypi_name} < %{version}-%{release}

%description
%{summary}

%prep
set -ex
%autosetup -n ansible_navigator-%{version}

%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%{_bindir}/ansible-navigator
%{python3_sitelib}/ansible_navigator
%{python3_sitelib}/ansible_navigator-%{version}.dist-info/

%changelog
* Wed Nov 12 2025 Maximilian Kolb <kolb@atix.de> - 25.9.0-2
- Ensure podman is installed automatically

* Fri Nov 07 2025 Maximilian Kolb <kolb@atix.de> - 25.9.0-1
- Release ansible-navigator 25.9.0
