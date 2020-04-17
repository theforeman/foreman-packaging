# Created by pyp2rpm-3.3.2
%global pypi_name keycloak-httpd-client-install
%global summary Tools to configure Apache HTTPD as Keycloak client

%if 0%{?rhel} == 7
%bcond_without python2
%bcond_with python3
%else
%bcond_with python2
%bcond_without python3
%endif

Name:           %{pypi_name}
Version:        1.2.2
Release:        2%{?dist}
Summary:        %{summary}

License:        GPLv3
URL:            https://github.com/latchset/keycloak-httpd-client-install
Source0:        https://files.pythonhosted.org/packages/source/k/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%if %{with python2}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%endif

%if %{with python3}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%endif

Requires:       %{_bindir}/keycloak-httpd-client-install

%description
Keycloak is a federated Identity Provider (IdP). Apache HTTPD supports
a variety of authentication modules which can be configured to utilize
a Keycloak IdP to perform authentication. This package contains
libraries and tools which can automate and simplify configuring an
Apache HTTPD authentication module and registering as a client of a
Keycloak IdP.

%if 0%{?with_python2}
%package -n     python2-%{pypi_name}
Summary:        %{summary}

%{?python_provide:%python_provide python2-%{pypi_name}}

Requires:       %{name} = %{version}-%{release}
Requires:       python2-jinja2
Requires:       python-lxml
Requires:       python-requests
Requires:       python2-requests-oauthlib
Requires:       python-setuptools
Requires:       python-six
Requires:       %{_bindir}/keycloak-httpd-client-install

%description -n python2-%{pypi_name}
Keycloak is an authentication server. This package contains libraries and
programs which can invoke the Keycloak REST API and configure clients
of a Keycloak server.
%endif

%if 0%{?with_python3}
%package -n     python3-%{pypi_name}
Summary:        %{summary}

%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       %{name} = %{version}-%{release}
Requires:       python3-jinja2
Requires:       python3-lxml
Requires:       python3-requests
Requires:       python3-requests-oauthlib
Requires:       python3-setuptools
Requires:       python3-six
Requires:       %{_bindir}/keycloak-httpd-client-install

%description -n python3-%{pypi_name}
Keycloak is an authentication server. This package contains libraries and
programs which can invoke the Keycloak REST API and configure clients
of a Keycloak server.
%endif

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%if %{with python2}
%py2_build
%endif

%if 0%{?with_python3}
%py3_build
%endif

%install
%if 0%{?with_python2}
%py2_install
%endif

%if %{with python3}
%py3_install
%endif

install -d -m 755 %{buildroot}/%{_mandir}/man8
install -c -m 644 doc/keycloak-httpd-client-install.8 %{buildroot}/%{_mandir}/man8

%files
%license LICENSE.txt
%doc README.md doc/ChangeLog
%{_datadir}/%{pypi_name}/

%if %{with python2}
%files -n python2-%{pypi_name}
%{python2_sitelib}/*
%{_bindir}/keycloak-httpd-client-install
%{_bindir}/keycloak-rest
%{_mandir}/man8/*
%endif

%if %{with python3}
%files -n python3-%{pypi_name}
%{python3_sitelib}/*
%{_bindir}/keycloak-httpd-client-install
%{_bindir}/keycloak-rest
%{_mandir}/man8/*
%endif

%changelog
* Wed Apr 15 2020 Eric D. Helms <ericdhelms@gmail.com> - 1.2.2-2
- Build keycloak-httpd-client-install for Python 3 on EL8

* Wed Nov 20 2019 Amit Upadhye <upadhyeammit@gmail.com> - 1.2.2-1
- Initial package.
