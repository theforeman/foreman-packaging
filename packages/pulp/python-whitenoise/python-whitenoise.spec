# Created by pyp2rpm-3.3.3
%global pypi_name whitenoise

Name:           python-%{pypi_name}
Version:        4.1.4
Release:        1%{?dist}
Summary:        Radically simplified static file serving for WSGI applications

License:        MIT
URL:            http://whitenoise.evans.io
Source0:        https://files.pythonhosted.org/packages/source/w/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
WhiteNoise :target: :target: .. image::

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
WhiteNoise :target: :target: .. image::

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Nov 18 2019 Evgeni Golov - 4.1.4-1
- Initial package.
