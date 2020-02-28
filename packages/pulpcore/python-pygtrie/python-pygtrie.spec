# Created by pyp2rpm-3.3.3
%global pypi_name pygtrie

Name:           python-%{pypi_name}
Version:        2.3.2
Release:        2%{?dist}
Summary:        Trie data structure implementation

License:        Apache-2.0
URL:            https://github.com/mina86/pygtrie
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

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%{python3_sitelib}/__pycache__/%{pypi_name}.*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.3.2-2
- Bump release to build for el8

* Fri Dec 13 2019 Evgeni Golov - 2.3.2-1
- Initial package.
