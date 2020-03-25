# Created by pyp2rpm-3.3.3
%global pypi_name packaging

Name:           python-%{pypi_name}
Version:        20.3
Release:        1%{?dist}
Summary:        Core utilities for Python packages

License:        BSD or Apache License, Version 2.0
URL:            https://github.com/pypa/packaging
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pyparsing >= 2.0.2
BuildRequires:  python3-setuptools
BuildRequires:  python3-six

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3-pyparsing >= 2.0.2
Requires:       python3-six

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
%license LICENSE LICENSE.APACHE LICENSE.BSD
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Mar 18 2020 Samir Jha 20.3-1
- Update to 20.3

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 20.1-2
- Bump release to build for el8

* Tue Jan 28 2020 Evgeni Golov 20.1-1
- Update to 20.1

* Mon Jan 06 2020 Evgeni Golov 20.0-1
- Update to 20.0

* Mon Nov 18 2019 Evgeni Golov - 19.2-1
- Initial package.
