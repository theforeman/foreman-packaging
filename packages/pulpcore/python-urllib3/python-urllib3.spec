# Created by pyp2rpm-3.3.3
%global pypi_name urllib3

Name:           python-%{pypi_name}
Version:        1.25.9
Release:        1%{?dist}
Summary:        HTTP library with thread-safe connection pooling, file post, and more

License:        MIT
URL:            https://urllib3.readthedocs.io/
Source0:        https://files.pythonhosted.org/packages/source/u/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
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
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst dummyserver/certs/README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Apr 28 2020 Evgeni Golov 1.25.9-1
- Update to 1.25.9

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.25.8-2
- Bump release to build for el8

* Tue Jan 28 2020 Evgeni Golov 1.25.8-1
- Update to 1.25.8

* Mon Nov 18 2019 Evgeni Golov - 1.25.7-1
- Initial package.
