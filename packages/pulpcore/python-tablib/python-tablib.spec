# Created by pyp2rpm-3.3.3
%global pypi_name tablib

Name:           python-%{pypi_name}
Version:        1.1.0
Release:        1%{?dist}
Summary:        Format agnostic tabular data library (XLS, JSON, YAML, CSV)

License:        MIT
URL:            https://tablib.readthedocs.io
Source0:        https://files.pythonhosted.org/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools-scm

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3-markuppy
Requires:       python3-odfpy
Requires:       python3-openpyxl >= 2.4.0
Requires:       python3-pyyaml
Requires:       python3-xlrd
Requires:       python3-xlwt

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
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Apr 28 2020 Evgeni Golov - 1.1.0-1
- Initial package.
