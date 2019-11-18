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
Typing Extensions -- Backported and Experimental Type Hints for PythonThe
typing module was added to the standard library in Python 3.5 on a provisional
basis and will no longer be provisional in Python 3.7. However, this means
users of Python 3.5 - 3.6 who are unable to upgrade will not be able to take
advantage of new types added to the typing module, such as typing.Text or...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Typing Extensions -- Backported and Experimental Type Hints for PythonThe
typing module was added to the standard library in Python 3.5 on a provisional
basis and will no longer be provisional in Python 3.7. However, this means
users of Python 3.5 - 3.6 who are unable to upgrade will not be able to take
advantage of new types added to the typing module, such as typing.Text or...

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
