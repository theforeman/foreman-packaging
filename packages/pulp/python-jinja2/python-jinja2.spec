# Created by pyp2rpm-3.3.3
%global pypi_name Jinja2
%global srcname jinja2

Name:           python-%{srcname}
Version:        2.10.3
Release:        1%{?dist}
Summary:        A very fast and expressive template engine

License:        BSD-3-Clause
URL:            https://palletsprojects.com/p/jinja/
Source0:        https://files.pythonhosted.org/packages/source/J/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
%{summary}

%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
Requires:       python3-markupsafe >= 0.23
Requires:       python3-setuptools

%description -n python3-%{srcname}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE.rst
%doc README.rst
%{python3_sitelib}/jinja2
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Nov 18 2019 Evgeni Golov - 2.10.3-1
- Initial package.
