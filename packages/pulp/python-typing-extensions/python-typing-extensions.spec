# Created by pyp2rpm-3.3.3
%global pypi_name typing-extensions

Name:           python-%{pypi_name}
Version:        3.7.4.1
Release:        1%{?dist}
Summary:        Backported and Experimental Type Hints for Python 3

License:        PSF
URL:            https://github.com/python/typing/blob/master/typing_extensions/README.rst
Source0:        https://files.pythonhosted.org/packages/source/t/%{pypi_name}/typing_extensions-%{version}.tar.gz
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
%autosetup -n typing_extensions-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/typing_extensions.py
%{python3_sitelib}/typing_extensions-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Nov 18 2019 Evgeni Golov - 3.7.4.1-1
- Initial package.
