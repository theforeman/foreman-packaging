# Created by pyp2rpm-3.3.3
%global pypi_name dynaconf

%global real_version %{version}rc1

Name:           python-%{pypi_name}
Version:        3.0.0
Release:        0.1.rc1%{?dist}
Summary:        The dynamic configurator for your Python Project

License:        MIT
URL:            https://github.com/rochacbruno/dynaconf
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{real_version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-box
BuildRequires:  python3-click
BuildRequires:  python3-dotenv
BuildRequires:  python3-setuptools >= 38.6.0
BuildRequires:  python3-toml

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3-box
Requires:       python3-click
Requires:       python3-dotenv
Requires:       python3-setuptools
Requires:       python3-toml

%description -n python3-%{pypi_name}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{real_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{_bindir}/dynaconf
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{real_version}-py%{python3_version}.egg-info

%changelog
* Wed Mar 18 2020 Samir Jha 3.0.0-0.1.rc1
- Update to 3.0.0rc1

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.2.2-2
- Bump release to build for el8

* Mon Jan 06 2020 Evgeni Golov 2.2.2-1
- Update to 2.2.2

* Fri Dec 13 2019 Evgeni Golov 2.2.1-1
- Update to 2.2.1

* Mon Nov 18 2019 Evgeni Golov - 2.2.0-1
- Initial package.
