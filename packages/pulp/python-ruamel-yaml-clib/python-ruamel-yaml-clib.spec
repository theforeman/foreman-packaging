# Created by pyp2rpm-3.3.3
%global pypi_name ruamel.yaml.clib
%global srcname ruamel-yaml-clib

Name:           python-%{srcname}
Version:        0.2.0
Release:        1%{?dist}
Summary:        C version of reader, parser and emitter for ruamel

License:        MIT
URL:            https://bitbucket.org/ruamel/yaml.clib
Source0:        https://files.pythonhosted.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

BuildRequires:  gcc
BuildRequires:  libyaml-devel

%description
ruamel.yaml.clib ruamel.yaml.clib is the C based reader/scanner and emitter for
ruamel.yaml:version: 0.2.0 :updated: 2019-09-26 :documentation: :repository:
:pypi: package was split of from ruamel.yaml, so that ruamel.yaml can be build
as a universal wheel. Apart from the C code seldom changing, and taking a long
time to compile for all platforms, this allows installation of the .so on
Linux...

%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
ruamel.yaml.clib ruamel.yaml.clib is the C based reader/scanner and emitter for
ruamel.yaml:version: 0.2.0 :updated: 2019-09-26 :documentation: :repository:
:pypi: package was split of from ruamel.yaml, so that ruamel.yaml can be build
as a universal wheel. Apart from the C code seldom changing, and taking a long
time to compile for all platforms, this allows installation of the .so on
Linux...

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%{__python3} setup.py install --single-version-externally-managed --skip-build --root $RPM_BUILD_ROOT

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitearch}/ruamel
%{python3_sitearch}/_ruamel_yaml.cpython-3*m-x86_64-linux-gnu.so
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Nov 18 2019 Evgeni Golov - 0.2.0-1
- Initial package.
