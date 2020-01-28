# Created by pyp2rpm-3.3.3
%global pypi_name jsonschema

Name:           python-%{pypi_name}
Version:        3.2.0
Release:        1%{?dist}
Summary:        An implementation of JSON Schema validation for Python

License:        None
URL:            https://github.com/Julian/jsonschema
Source0:        https://files.pythonhosted.org/packages/source/j/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools-scm

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3-attrs >= 17.4.0
Requires:       python3-pyrsistent >= 0.14.0
Requires:       python3-setuptools
Requires:       python3-six >= 1.11.0

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
%license json/LICENSE
%doc json/README.md README.rst
%{_bindir}/jsonschema
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Jan 28 2020 Evgeni Golov - 3.2.0-1
- Initial package.
