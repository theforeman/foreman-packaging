# Created by pyp2rpm-3.3.3
%global pypi_name yarl

Name:           python-%{pypi_name}
Version:        1.5.1
Release:        1%{?dist}
Summary:        Yet another URL library

License:        Apache 2
URL:            https://github.com/aio-libs/yarl/
Source0:        https://files.pythonhosted.org/packages/source/y/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-idna >= 2.0
BuildRequires:  python3-multidict >= 4.0
BuildRequires:  python3-setuptools
BuildRequires:  python3-typing-extensions >= 3.7.4

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3-idna >= 2.0
Requires:       python3-multidict >= 4.0
Requires:       python3-typing-extensions >= 3.7.4

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
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Aug 10 2020 Evgeni Golov 1.5.1-1
- Update to 1.5.1

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.4.2-2
- Bump release to build for el8

* Fri Dec 13 2019 Evgeni Golov 1.4.2-1
- Update to 1.4.2

* Mon Nov 18 2019 Evgeni Golov - 1.3.0-1
- Initial package.
