# Created by pyp2rpm-3.3.3
%global pypi_name backoff

Name:           python-%{pypi_name}
Version:        1.10.0
Release:        2%{?dist}
Summary:        Function decoration for backoff and retry

License:        None
URL:            https://github.com/litl/backoff
Source0:        https://files.pythonhosted.org/packages/source/b/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
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

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.10.0-2
- Bump release to build for el8

* Fri Dec 13 2019 Evgeni Golov 1.10.0-1
- Update to 1.10.0

* Mon Nov 18 2019 Evgeni Golov - 1.9.0-1
- Initial package.
