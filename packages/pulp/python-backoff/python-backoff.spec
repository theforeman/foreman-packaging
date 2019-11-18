# Created by pyp2rpm-3.3.3
%global pypi_name backoff

Name:           python-%{pypi_name}
Version:        1.9.0
Release:        1%{?dist}
Summary:        Function decoration for backoff and retry

License:        None
URL:            https://github.com/litl/backoff
Source0:        https://files.pythonhosted.org/packages/source/b/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
 **Function decoration for backoff and retry**This module provides function
decorators which can be used to wrap a function such that it will be retried
until some condition is met. It is meant to be of use when accessing unreliable
resources with the potential for intermittent failures i.e. network resources
and external

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
 **Function decoration for backoff and retry**This module provides function
decorators which can be used to wrap a function such that it will be retried
until some condition is met. It is meant to be of use when accessing unreliable
resources with the potential for intermittent failures i.e. network resources
and external

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE LICENSE
%doc README.rst README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Nov 18 2019 Evgeni Golov - 1.9.0-1
- Initial package.
