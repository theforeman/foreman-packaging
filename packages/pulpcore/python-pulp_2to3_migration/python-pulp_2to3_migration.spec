# Created by pyp2rpm-3.3.3
%global pypi_name pulp-2to3-migration

# We use a wrong source RPM name here, as the original one triggers a bug in tito
# See https://github.com/dgoodwin/tito/pull/333
Name:           python-pulp_2to3_migration
Version:        0.2.0
Release:        0.1.b2%{?dist}
Summary:        Pulp 2 to Pulp 3 migration tool

License:        GPLv2+
URL:            http://www.pulpproject.org
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}b2.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-pulpcore >= 3.3
Requires:       python3-jsonschema
Requires:       python3-mongoengine
Requires:       python3-semantic-version
Requires:       python3-setuptools

%description -n python3-%{pypi_name}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{version}b2
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
%{python3_sitelib}/pulp_2to3_migration
%{python3_sitelib}/pulp_2to3_migration-%{version}b2-py%{python3_version}.egg-info

%changelog
* Wed Apr 29 2020 Evgeni Golov - 0.2.0-0.1.b2
- Update to 0.2.0-b2

* Wed Mar 25 2020 Samir Jha <sjha4@ncsu.edu> - 0.2.0-0.1.b1
- Update to 0.2.0-b1

* Tue Mar 03 2020 Evgeni Golov - 0.1.0-0.1.rc1
- Update to 0.1.0-rc1

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.0.1-0.2.rc1
- Bump release to build for el8

* Wed Feb 19 2020 Evgeni Golov - 0.0.1-0.1.rc1
- Update to 0.0.1-rc1

* Tue Jan 28 2020 Evgeni Golov - 0.0.1-0.1.beta1
- Initial package.
