%global pypi_name obsah

Name:           python-%{pypi_name}
Version:        1.4.0
Release:        1%{?dist}
Summary:        easily build CLI applications using ansible playbooks

License:        None
URL:            https://github.com/theforeman/obsah
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Easily build CLI applications using ansible playbooks.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Easily build CLI applications using ansible playbooks.


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
%{_bindir}/obsah
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Aug 25 2025 Evgeni Golov - 1.4.0-1
- Update to 1.4.0

* Thu Jun 26 2025 Evgeni Golov - 1.3.2-1
- Update to 1.3.2

* Thu Jun 26 2025 Evgeni Golov - 1.3.1-1
- Update to 1.3.1

* Mon Jun 02 2025 Evgeni Golov - 1.3.0-1
- Update to 1.3.0

* Wed Apr 30 2025 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.1.0-1
- Update to 1.1.0

* Wed Aug 23 2023 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 0.0.3-1
- Update to 0.0.3

* Sun Oct 25 2020 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 0.0.2-1
- Update to 0.0.2

* Wed May 13 2020 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 0.0.1-2
- Allow building with Python 2 on EPEL7

* Thu Nov 28 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 0.0.1-1
- Initial package.
