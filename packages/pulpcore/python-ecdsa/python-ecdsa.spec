# Created by pyp2rpm-3.3.3
%global pypi_name ecdsa

Name:           python-%{pypi_name}
Version:        0.13.3
Release:        2%{?dist}
Summary:        ECDSA cryptographic signature library (pure python)

License:        MIT
URL:            http://github.com/warner/python-ecdsa
Source0:        https://files.pythonhosted.org/packages/source/e/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
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
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.13.3-2
- Bump release to build for el8

* Tue Nov 19 2019 Evgeni Golov - 0.13.3-1
- Initial package.
