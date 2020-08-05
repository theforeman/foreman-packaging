# Created by pyp2rpm-3.3.2
%global pypi_name setuptools_scm_git_archive

Name:           python-%{pypi_name}
Version:        1.1
Release:        1%{?dist}
Summary:        setuptools_scm plugin for git archives

License:        MIT
URL:            https://github.com/Changaco/setuptools_scm_git_archive/
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools-scm

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

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
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Mon Aug 03 2020 Evgeni Golov - 1.1-1
- Initial package.
