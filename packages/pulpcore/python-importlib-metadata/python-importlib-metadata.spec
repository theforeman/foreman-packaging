# Created by pyp2rpm-3.3.3
%global pypi_name importlib-metadata

Name:           python-%{pypi_name}
Version:        1.4.0
Release:        1%{?dist}
Summary:        Read metadata from Python packages

License:        Apache Software License
URL:            http://importlib-metadata.readthedocs.io/
Source0:        https://files.pythonhosted.org/packages/source/i/%{pypi_name}/importlib_metadata-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools-scm

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3-zipp >= 0.5

%description -n python3-%{pypi_name}
%{summary}

%prep
%autosetup -n importlib_metadata-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/importlib_metadata
%{python3_sitelib}/importlib_metadata-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Jan 28 2020 Evgeni Golov - 1.4.0-1
- Initial package.
