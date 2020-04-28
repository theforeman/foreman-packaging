# Created by pyp2rpm-3.3.3
%global pypi_name et-xmlfile

Name:           python-%{pypi_name}
Version:        1.0.1
Release:        1%{?dist}
Summary:        An implementation of lxml.xmlfile for the standard library

License:        MIT
URL:            https://bitbucket.org/openpyxl/et_xmlfile
Source0:        https://files.pythonhosted.org/packages/source/e/%{pypi_name}/et_xmlfile-%{version}.tar.gz
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
%autosetup -n et_xmlfile-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%{python3_sitelib}/et_xmlfile
%{python3_sitelib}/et_xmlfile-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Apr 28 2020 Evgeni Golov - 1.0.1-1
- Initial package.
