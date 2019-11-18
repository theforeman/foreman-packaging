# Created by pyp2rpm-3.3.3
%global pypi_name urllib3

Name:           python-%{pypi_name}
Version:        1.25.7
Release:        1%{?dist}
Summary:        HTTP library with thread-safe connection pooling, file post, and more

License:        MIT
URL:            https://urllib3.readthedocs.io/
Source0:        https://files.pythonhosted.org/packages/source/u/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
urllib3 is a powerful, *sanity-friendly* HTTP client for Python. Much of the
Python ecosystem already uses urllib3 and you should too. urllib3 brings many
critical features that are missing from the Python standard libraries:- Thread
safety. - Connection pooling. - Client-side SSL/TLS verification. - File
uploads with multipart encoding. - Helpers for retrying requests and dealing
with HTTP...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
urllib3 is a powerful, *sanity-friendly* HTTP client for Python. Much of the
Python ecosystem already uses urllib3 and you should too. urllib3 brings many
critical features that are missing from the Python standard libraries:- Thread
safety. - Connection pooling. - Client-side SSL/TLS verification. - File
uploads with multipart encoding. - Helpers for retrying requests and dealing
with HTTP...

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
* Mon Nov 18 2019 Evgeni Golov - 1.25.7-1
- Initial package.
