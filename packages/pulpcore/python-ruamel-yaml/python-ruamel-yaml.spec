# Created by pyp2rpm-3.3.3
%global pypi_name ruamel.yaml
%global srcname ruamel-yaml

Name:           python-%{srcname}
Version:        0.16.5
Release:        1%{?dist}
Summary:        ruamel.yaml is a YAML parser/emitter that supports roundtrip preservation of comments, seq/map flow style, and map key order

License:        MIT license
URL:            https://bitbucket.org/ruamel/yaml
Source0:        https://files.pythonhosted.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
%{summary}

%package -n     python3-%{srcname}
Summary:        %{summary}
Requires:       python3-ruamel-yaml-clib
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{summary}

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
%{python3_sitelib}/ruamel
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}-*.pth
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Nov 18 2019 Evgeni Golov - 0.16.5-1
- Initial package.
