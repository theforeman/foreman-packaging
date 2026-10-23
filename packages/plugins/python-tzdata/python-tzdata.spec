%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

%global pypi_name tzdata

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        2025.2
Release:        1%{?dist}
Summary:        Provider of IANA time zone data

License:        Apache-2.0
URL:            https://github.com/python/tzdata
Source0:        https://files.pythonhosted.org/packages/95/32/1a225d6164441be760d75c2c42e2780dc0873fe382da3e98a2e1e48361e5/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools-scm
BuildRequires:  python%{python3_pkgversion}-wheel

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Provides:	%{pypi_name}

%description
%{summary}

%prep
set -ex
%autosetup -n %{pypi_name}-%{version}

%build
set -ex
%pyproject_wheel

%install
set -ex
%pyproject_install

%files -n python%{python3_pkgversion}-%{pypi_name}
# %%{_bindir}/tzdata
%{python3_sitelib}/tzdata
%{python3_sitelib}/tzdata-%{version}.dist-info/

%changelog
* Mon Nov 10 2025 Maximilian Kolb <kolb@atix.de> - 2025.2-1
- Release python-tzdata 2025.2
