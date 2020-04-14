# Created by pyp2rpm-3.3.3
%global pypi_name PyYAML
%global srcname pyyaml

Name:           python-%{srcname}
Version:        5.3.1
Release:        1%{?dist}
Summary:        YAML parser and emitter for Python

License:        MIT
URL:            https://github.com/yaml/pyyaml
Source0:        https://files.pythonhosted.org/packages/source/P/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

BuildRequires:  gcc
BuildRequires:  libyaml-devel

%description
%{summary}

%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE
%{python3_sitearch}/yaml
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitearch}/_yaml.cpython-3?m-%{_arch}-linux-gnu.so

%changelog
* Tue Apr 14 2020 Evgeni Golov 5.3.1-1
- Update to 5.3.1

* Wed Mar 18 2020 Samir Jha 5.3-1
- Update to 5.3

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 5.2-2
- Bump release to build for el8

* Fri Dec 13 2019 Evgeni Golov 5.2-1
- Update to 5.2

* Mon Nov 18 2019 Evgeni Golov - 5.1.2-1
- Initial package.
