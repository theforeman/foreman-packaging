# Created by pyp2rpm-3.3.3
%global pypi_name drf-spectacular

Name:           python-%{pypi_name}
Version:        0.9.12
Release:        1%{?dist}
Summary:        Sane and flexible OpenAPI 3 schema generation for Django REST framework

License:        BSD
URL:            https://github.com/tfranzel/drf-spectacular
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3-django >= 2.2
Requires:       python3-pyyaml >= 5.1
Requires:       python3-djangorestframework >= 3.10
Requires:       python3-inflection >= 0.3.1
Requires:       python3-jsonschema >= 2.6.0
Requires:       python3-uritemplate >= 2.0.0

%description -n python3-%{pypi_name}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

sed -i "s/long_description = readme.read()/long_description = description/" setup.py

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE docs/license.rst
%doc README.rst docs/readme.rst
%{python3_sitelib}/drf_spectacular
%{python3_sitelib}/drf_spectacular/contrib
%{python3_sitelib}/drf_spectacular/management
%{python3_sitelib}/drf_spectacular/management/commands
%{python3_sitelib}/drf_spectacular/validation
%{python3_sitelib}/drf_spectacular-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Aug 10 2020 Evgeni Golov - 0.9.12-1
- Initial package.
