# Created by pyp2rpm-3.3.3
%global pypi_name yarl

Name:           python-%{pypi_name}
Version:        1.3.0
Release:        1%{?dist}
Summary:        Yet another URL library

License:        Apache 2
URL:            https://github.com/aio-libs/yarl/
Source0:        https://files.pythonhosted.org/packages/source/y/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3-idna >= 2.0
Requires:       python3-multidict >= 4.0

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
* Mon Nov 18 2019 Evgeni Golov - 1.3.0-1
- Initial package.
