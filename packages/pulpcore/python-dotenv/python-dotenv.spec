# Created by pyp2rpm-3.3.3
%global pypi_name python-dotenv
%global srcname dotenv

Name:           python-%{srcname}
Version:        0.12.0
Release:        1%{?dist}
Summary:        Add .env support to your django/flask apps in development and deployments

License:        None
URL:            http://github.com/theskumar/python-dotenv
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-click >= 5.0
BuildRequires:  python3-setuptools
BuildRequires:  python3-typing

%description
%{summary}

%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
Requires:       python3-click >= 5.0
Requires:       python3-typing

%description -n python3-%{srcname}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# setup.py loads the contents of README.md and CHANGELOG.md into long_description
# these files contain unicode charactes and thus fail to load in a non-unicode	
# environment like some EL7 builds	
sed -i 's/long_description = f.read.*/long_description = "dotenv"/' setup.py

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/dotenv
%{python3_sitelib}/python_dotenv-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Mar 18 2020 Samir Jha 0.12.0-1
- Update to 0.12.0

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.10.3-2
- Bump release to build for el8

* Mon Nov 18 2019 Evgeni Golov - 0.10.3-1
- Initial package.
