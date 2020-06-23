# Created by pyp2rpm-3.3.3
%global pypi_name pyflakes

Name:           python-%{pypi_name}
Version:        2.2.0
Release:        1%{?dist}
Summary:        passive checker of Python programs

License:        MIT
URL:            https://github.com/PyCQA/pyflakes
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

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
%{_bindir}/pyflakes
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Jun 23 2020 Evgeni Golov - 2.2.0-1
- Initial package.
