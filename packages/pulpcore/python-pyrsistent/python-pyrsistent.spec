# Created by pyp2rpm-3.3.3
%global pypi_name pyrsistent

Name:           python-%{pypi_name}
Version:        0.15.7
Release:        1%{?dist}
Summary:        Persistent/Functional/Immutable data structures

License:        MIT
URL:            http://github.com/tobgu/pyrsistent/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
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
%doc README.rst
%{python3_sitearch}/__pycache__/_pyrsistent_version.*
%{python3_sitearch}/_pyrsistent_version.py
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitearch}/pvectorc.cpython-3*m-x86_64-linux-gnu.so

%changelog
* Tue Jan 28 2020 Evgeni Golov - 0.15.7-1
- Initial package.
