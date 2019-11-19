# Created by pyp2rpm-3.3.3
%global pypi_name djangorestframework-queryfields

Name:           python-%{pypi_name}
Version:        1.0.0
Release:        1%{?dist}
Summary:        Serialize a partial subset of fields in the API

License:        None
URL:            https://github.com/wimglenn/djangorestframework-queryfields
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
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
%doc README.rst
%{python3_sitelib}/drf_queryfields
%{python3_sitelib}/djangorestframework_queryfields-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Nov 18 2019 Evgeni Golov - 1.0.0-1
- Initial package.
