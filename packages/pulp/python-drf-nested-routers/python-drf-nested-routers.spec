# Created by pyp2rpm-3.3.3
%global pypi_name drf-nested-routers

Name:           python-%{pypi_name}
Version:        0.91
Release:        1%{?dist}
Summary:        Nested resources for the Django Rest Framework

License:        Apache
URL:            https://github.com/alanjds/drf-nested-routers
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3-django >= 1.11
Requires:       python3-django-rest-framework >= 3.6.0

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
%doc README.md README.rst
%{python3_sitelib}/rest_framework_nested
%{python3_sitelib}/rest_framework_nested/runtests
%{python3_sitelib}/drf_nested_routers-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Nov 18 2019 Evgeni Golov - 0.91-1
- Initial package.
