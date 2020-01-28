# Created by pyp2rpm-3.3.3
%global pypi_name zipp

Name:           python-%{pypi_name}
Version:        2.1.0
Release:        1%{?dist}
Summary:        Backport of pathlib-compatible object wrapper for zip files

License:        None
URL:            https://github.com/jaraco/zipp
Source0:        https://files.pythonhosted.org/packages/source/z/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools-scm >= 3.4.1

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# Force setuptools_scm usage for older setuptools
sed -i 's/setuptools.setup.*/setuptools.setup(use_scm_version=True)/' setup.py

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/__pycache__/%{pypi_name}.*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Jan 28 2020 Evgeni Golov - 2.1.0-1
- Initial package.
