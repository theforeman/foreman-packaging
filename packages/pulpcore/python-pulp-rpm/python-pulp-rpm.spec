# Created by pyp2rpm-3.3.3
%global pypi_name pulp-rpm

Name:           python-%{pypi_name}
Version:        3.5.0
Release:        1%{?dist}
Summary:        RPM plugin for the Pulp Project

License:        GPLv2+
URL:            http://www.pulpproject.org
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
%if 0%{?rhel} == 7
Requires:       python36-gobject
Requires:       libmodulemd2
%else
Requires:       python3-gobject
Requires:       libmodulemd >= 2.0
%endif
Requires:       python3-createrepo_c < 1.0
Requires:       python3-createrepo_c >= 0.15.10
Requires:       python3-django-readonly-field
Requires:       python3-jsonschema >= 3.0
Requires:       python3-libcomps >= 0.1.12
Conflicts:      python3-libcomps >= 0.2
Requires:       python3-productmd >= 1.25
Requires:       python3-pulpcore < 3.6
Requires:       python3-pulpcore >= 3.4
Requires:       python3-setuptools
Requires:       python3-solv

%description -n python3-%{pypi_name}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# remove "solv" dependency from setup.py as python3-solv does not provide an egg
sed -i "/solv/d" requirements.txt

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/pulp_rpm
%{python3_sitelib}/pulp_rpm-%{version}-py%{python3_version}.egg-info

%changelog
* Thu Jul 30 2020 Samir Jha 3.5.0-1
- Update to 3.5.0

* Tue Jun 09 2020 Justin Sherrill <jsherril@redhat.com> 3.4.1-2
- solv dep moved to requirements.txt

* Thu Jun 04 2020 Evgeni Golov 3.4.1-1
- Update to 3.4.1

* Thu Jun 04 2020 Evgeni Golov - 3.3.1-5
- Make libmodulemd dependency versioned

* Thu Jun 04 2020 Evgeni Golov <evgeni@golov.de> - 3.3.1-4
- Bump libcomps require to get a version with egg info

* Wed Jun 03 2020 Evgeni Golov - 3.3.1-3
- Add Requires on libmodulemd

* Tue May 26 2020 Evgeni Golov - 3.3.1-2
- remove "solv" dependency from setup.py as python3-solv does not provide an egg

* Fri May 08 2020 Evgeni Golov - 3.3.1-1
- Release python-pulp-rpm 3.3.1

* Thu Apr 30 2020 Evgeni Golov - 3.3.0-1
- Initial package.
