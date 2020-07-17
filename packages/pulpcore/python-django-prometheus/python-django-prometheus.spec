# Created by pyp2rpm-3.3.3
%global pypi_name django-prometheus

Name:           python-%{pypi_name}
Version:        2.0.0
Release:        1%{?dist}
Summary:        Django middlewares to monitor your application with Prometheus

License:        Apache
URL:            http://github.com/korfuri/django-prometheus
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3-prometheus-client >= 0.7

%description -n python3-%{pypi_name}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

sed -i 's/"pytest-runner"//' setup.py

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/django_prometheus
%{python3_sitelib}/django_prometheus-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Jul 17 2020 Evgeni Golov - 2.0.0-1
- Initial package.
