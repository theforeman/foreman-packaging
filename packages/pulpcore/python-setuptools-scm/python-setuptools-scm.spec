# Created by pyp2rpm-3.3.3
%global pypi_name setuptools-scm

Name:           python-%{pypi_name}
Version:        3.4.3
Release:        2%{?dist}
Summary:        the blessed package to manage your versions by scm tags

License:        MIT
URL:            https://github.com/pypa/setuptools_scm/
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/setuptools_scm-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
setuptools_scm setuptools_scm handles managing your Python package versions in
SCM metadata instead of declaring them as the version argument or in a SCM
managed file.It also handles file finders for the supported SCMs. setup.py
usage To use setuptools_scm just modify your project's setup.py file like
this:* Add setuptools_scm to the setup_requires parameter. * Add the
use_scm_version...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-toml

%description -n python3-%{pypi_name}
setuptools_scm setuptools_scm handles managing your Python package versions in
SCM metadata instead of declaring them as the version argument or in a SCM
managed file.It also handles file finders for the supported SCMs. setup.py
usage To use setuptools_scm just modify your project's setup.py file like
this:* Add setuptools_scm to the setup_requires parameter. * Add the
use_scm_version...

%prep
%autosetup -n setuptools_scm-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/setuptools_scm
%{python3_sitelib}/setuptools_scm-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.4.3-2
- Bump release to build for el8

* Wed Jan 29 2020 Evgeni Golov 3.4.3-1
- Update to 3.4.3

* Fri Nov 15 2019 Evgeni Golov - 3.3.3-1
- Initial package.
