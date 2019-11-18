# Created by pyp2rpm-3.3.3
%global pypi_name django-filter

Name:           python-%{pypi_name}
Version:        2.2.0
Release:        1%{?dist}
Summary:        Django-filter is a reusable Django application for allowing users to filter querysets dynamically

License:        BSD
URL:            https://github.com/carltongibson/django-filter/tree/master
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Django Filter Django-filter is a reusable Django application allowing users to
declaratively add dynamic QuerySet filtering from URL parameters.Full
documentation on read the docs_. :target:

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-django >= 1.11
%description -n python3-%{pypi_name}
Django Filter Django-filter is a reusable Django application allowing users to
declaratively add dynamic QuerySet filtering from URL parameters.Full
documentation on read the docs_. :target:

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
%{python3_sitelib}/django_filters
%{python3_sitelib}/django_filter-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Nov 18 2019 Evgeni Golov - 2.2.0-1
- Initial package.
