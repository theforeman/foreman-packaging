# Created by pyp2rpm-3.3.3
%global pypi_name semantic-version

Name:           python-%{pypi_name}
Version:        2.8.4
Release:        1%{?dist}
Summary:        A library implementing the 'SemVer' scheme

License:        BSD
URL:            https://github.com/rbarrois/python-semanticversion
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/semantic_version-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools >= 0.8

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{summary}

%prep
%autosetup -n semantic_version-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/semantic_version
%{python3_sitelib}/semantic_version-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Jan 28 2020 Evgeni Golov - 2.8.4-1
- Initial package.
