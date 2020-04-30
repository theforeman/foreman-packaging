# Created by pyp2rpm-3.3.2
%global pypi_name python-debian
%global srcname debian

Name:           python-%{srcname}
Version:        0.1.37
Release:        1%{?dist}
Summary:        Debian package related modules

License:        GPL-2+
URL:            https://salsa.debian.org/python-debian-team/python-debian
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-chardet
BuildRequires:  python3-setuptools
BuildRequires:  python3-six

%description
This package provides Python 3 modules that abstract many formats of Debian
related files. Currently handled are: * Debtags information (debian.debtags
module) * debian/changelog (debian.changelog module) * Packages files, pdiffs
(debian.debian_support module) * Control files of single or multiple
RFC822-style paragraphs, e.g. debian/control, .changes, .dsc, Packages,
Sources, Release, etc....

%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

Requires:       python3-chardet
Requires:       python3-six
%description -n python3-%{srcname}
This package provides Python 3 modules that abstract many formats of Debian
related files. Currently handled are: * Debtags information (debian.debtags
module) * debian/changelog (debian.changelog module) * Packages files, pdiffs
(debian.debian_support module) * Control files of single or multiple
RFC822-style paragraphs, e.g. debian/control, .changes, .dsc, Packages,
Sources, Release, etc....


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%doc README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/deb822.py
%{python3_sitelib}/debian
%{python3_sitelib}/debian_bundle
%{python3_sitelib}/python_debian-%{version}-py?.?.egg-info

%changelog
* Thu Apr 30 2020 Markus Bucher <bucher@atix.de> - 0.1.37-1
- Initial package.
