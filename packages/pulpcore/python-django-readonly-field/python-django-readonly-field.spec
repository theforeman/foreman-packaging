# Created by pyp2rpm-3.3.3
%global pypi_name django-readonly-field

Name:           python-%{pypi_name}
Version:        1.0.5
Release:        1%{?dist}
Summary:        Make Django model fields readonly

License:        MIT
URL:            https://github.com/peopledoc/django-readonly-field
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-django >= 1.11
BuildRequires:  python3-setuptools
BuildRequires:  python3-tox

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3-django >= 1.11

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
%{python3_sitelib}/django_readonly_field
%{python3_sitelib}/django_readonly_field-%{version}-py%{python3_version}.egg-info

%changelog
* Thu Jul 30 2020 Samir Jha - 1.0.5-1
- Initial package.
