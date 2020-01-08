# Created by pyp2rpm-3.3.3
%global pypi_name multidict

Name:           python-%{pypi_name}
Version:        4.7.3
Release:        1%{?dist}
Summary:        multidict implementation

License:        Apache 2
URL:            https://github.com/aio-libs/multidict
Source0:        https://files.pythonhosted.org/packages/source/m/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

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
%doc README.rst
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Jan 06 2020 Evgeni Golov 4.7.3-1
- Update to 4.7.3

* Fri Dec 13 2019 Evgeni Golov 4.7.1-1
- Update to 4.7.1

* Mon Nov 18 2019 Evgeni Golov - 4.5.2-1
- Initial package.
