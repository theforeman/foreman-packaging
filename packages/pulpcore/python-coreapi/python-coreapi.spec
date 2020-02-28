# Created by pyp2rpm-3.3.3
%global pypi_name coreapi

Name:           python-%{pypi_name}
Version:        2.3.3
Release:        2%{?dist}
Summary:        Python client library for Core API

License:        BSD
URL:            https://github.com/core-api/python-client
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3-coreschema
Requires:       python3-itypes
Requires:       python3-requests
Requires:       python3-setuptools
Requires:       python3-uritemplate

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
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/coreapi/codecs
%{python3_sitelib}/coreapi/transports
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.3.3-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 2.3.3-1
- Initial package.
