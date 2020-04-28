# Created by pyp2rpm-3.3.3
%global pypi_name xlrd

Name:           python-%{pypi_name}
Version:        1.2.0
Release:        1%{?dist}
Summary:        Library for developers to extract data from Microsoft Excel (tm) spreadsheet files

License:        BSD
URL:            http://www.python-excel.org/
Source0:        https://files.pythonhosted.org/packages/source/x/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

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

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license docs/licenses.rst LICENSE
%doc README.md
%{_bindir}/runxlrd.py
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Apr 28 2020 Evgeni Golov - 1.2.0-1
- Initial package.
