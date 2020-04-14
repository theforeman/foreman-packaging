# Created by pyp2rpm-3.3.3
%global pypi_name scikit-build

Name:           python-%{pypi_name}
Version:        0.10.0
Release:        1%{?dist}
Summary:        Improved build system generator for Python C/C++/Fortran/Cython extensions

License:        MIT
URL:            https://github.com/scikit-build/scikit-build
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-packaging
BuildRequires:  python3-setuptools >= 28.0.0
BuildRequires:  python3-wheel >= 0.29.0

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3-packaging
Requires:       python3-setuptools >= 28.0.0
Requires:       python3-wheel >= 0.29.0

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
%{python3_sitelib}/skbuild
%{python3_sitelib}/scikit_build-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Apr 14 2020 Evgeni Golov - 0.10.0-1
- Initial package.
