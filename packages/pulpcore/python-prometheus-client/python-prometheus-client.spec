# Created by pyp2rpm-3.3.3
%global pypi_name prometheus-client

Name:           python-%{pypi_name}
Version:        0.8.0
Release:        1%{?dist}
Summary:        Python client for the Prometheus monitoring system

License:        Apache Software License 2.0
URL:            https://github.com/prometheus/client_python
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/prometheus_client-%{version}.tar.gz
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
%autosetup -n prometheus_client-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
%{python3_sitelib}/prometheus_client
%{python3_sitelib}/prometheus_client-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Jul 17 2020 Evgeni Golov - 0.8.0-1
- Initial package.
