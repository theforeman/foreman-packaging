# Created by pyp2rpm-3.3.3
%global pypi_name pyparsing

Name:           python-%{pypi_name}
Version:        2.4.6
Release:        2%{?dist}
Summary:        Python parsing module

License:        MIT License
URL:            https://github.com/pyparsing/pyparsing/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
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
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc examples/0README.html README.rst
%{python3_sitelib}/__pycache__/%{pypi_name}.*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.4.6-2
- Bump release to build for el8

* Mon Jan 06 2020 Evgeni Golov 2.4.6-1
- Update to 2.4.6

* Mon Nov 18 2019 Evgeni Golov - 2.4.5-1
- Initial package.
