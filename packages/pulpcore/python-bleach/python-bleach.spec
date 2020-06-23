# Created by pyp2rpm-3.3.3
%global pypi_name bleach

Name:           python-%{pypi_name}
Version:        3.1.5
Release:        1%{?dist}
Summary:        An easy safelist-based HTML-sanitizing tool

License:        Apache Software License
URL:            https://github.com/mozilla/bleach
Source0:        https://files.pythonhosted.org/packages/source/b/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-six >= 1.9.0

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3-packaging
Requires:       python3-six >= 1.9.0
Requires:       python3-webencodings

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
%license LICENSE bleach/_vendor/html5lib-1.0.1.dist-info/LICENSE.txt
%doc README.rst bleach/_vendor/README.rst tests_website/README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Jun 23 2020 Evgeni Golov - 3.1.5-1
- Initial package.
