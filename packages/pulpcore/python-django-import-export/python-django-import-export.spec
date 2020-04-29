# Created by pyp2rpm-3.3.3
%global pypi_name django-import-export

Name:           python-%{pypi_name}
Version:        2.0.2
Release:        1%{?dist}
Summary:        Django application and library for importing and exporting data with included admin integration

License:        BSD License
URL:            https://github.com/django-import-export/django-import-export
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3-django >= 2.0
Requires:       python3-diff-match-patch
Requires:       python3-tablib >= 0.14.0

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
%doc README.rst
%{python3_sitelib}/import_export
%{python3_sitelib}/django_import_export-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Apr 28 2020 Evgeni Golov - 2.0.2-1
- Initial package.
