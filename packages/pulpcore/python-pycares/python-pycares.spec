# Created by pyp2rpm-3.3.3
%global pypi_name pycares

Name:           python-%{pypi_name}
Version:        3.1.1
Release:        1%{?dist}
Summary:        Python interface for c-ares

License:        None
URL:            http://github.com/saghul/pycares
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-cffi >= 1.5.0
BuildRequires:  python3-setuptools

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3-cffi >= 1.5.0
Requires:       python3-idna >= 2.1

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
* Wed Mar 18 2020 Samir Jha - 3.1.1-1
- Initial package.
