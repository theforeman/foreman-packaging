# Created by pyp2rpm-3.3.3
%global pypi_name dynaconf

Name:           python-%{pypi_name}
Version:        2.2.2
Release:        1%{?dist}
Summary:        The dynamic configurator for your Python Project

License:        MIT
URL:            https://github.com/rochacbruno/dynaconf
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools >= 38.6.0

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3-box < 4.0.0
Requires:       python3-click <= 7.0
Requires:       python3-dotenv <= 0.10.3
Requires:       python3-setuptools
Requires:       python3-toml <= 0.10.0

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
%doc README.md
%{_bindir}/dynaconf
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Jan 06 2020 Evgeni Golov 2.2.2-1
- Update to 2.2.2

* Fri Dec 13 2019 Evgeni Golov 2.2.1-1
- Update to 2.2.1

* Mon Nov 18 2019 Evgeni Golov - 2.2.0-1
- Initial package.
