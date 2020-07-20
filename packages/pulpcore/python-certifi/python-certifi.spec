# Created by pyp2rpm-3.3.3
%global pypi_name certifi

Name:           python-%{pypi_name}
Version:        2020.6.20
Release:        1%{?dist}
Summary:        Python package for providing Mozilla's CA Bundle

License:        MPL-2.0
URL:            https://certifiio.readthedocs.io/en/latest/
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Patch0:         certifi-2020.6.20-use-system-cert.patch
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  ca-certificates

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Requires:       ca-certificates
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{summary}

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# Remove bundled Root Certificates collection
rm -rf certifi/*.pem

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Jul 20 2020 Evgeni Golov - 2020.6.20-1
- Initial package.
