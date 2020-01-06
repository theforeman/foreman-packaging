# Created by pyp2rpm-3.3.3
%global pypi_name python-box
%global srcname box

Name:           python-%{srcname}
Version:        3.4.6
Release:        1%{?dist}
Summary:        Advanced Python dictionaries with dot notation access

License:        MIT
URL:            https://github.com/cdgriffith/Box
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
%{summary}

%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# setup.py contains a setup_requires for pytest-runner,
# but we don't run tests here and don't need it, so let's remove it
sed -i '/setup_requires/d' setup.py

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{_bindir}/box.py
%{python3_sitelib}/__pycache__/box.*
%{python3_sitelib}/box.py
%{python3_sitelib}/python_box-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Jan 06 2020 Evgeni Golov 3.4.6-1
- Update to 3.4.6

* Mon Nov 18 2019 Evgeni Golov - 3.4.5-1
- Initial package.
