# Created by pyp2rpm-3.3.3
%global pypi_name pulp-certguard

Name:           python-%{pypi_name}
Version:        0.1.0
Release:        0.1.rc5%{?dist}
Summary:        X.509 Certguards plugin for the Pulp Project

License:        GPLv2+
URL:            http://www.pulpproject.org
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}rc5.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
A Pulp plugin that provides an X.509 capable ContentGuard for pulpcore.
Instances of X509CertGuard are useful for requiring clients to submit
a certificate proving their entitlement to content before receiving the content.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3-pyopenssl
Requires:       python3-pulpcore < 3.5
Requires:       python3-pulpcore >= 3.3.0
Requires:       python3-setuptools

%description -n python3-%{pypi_name}
A Pulp plugin that provides an X.509 capable ContentGuard for pulpcore.
Instances of X509CertGuard are useful for requiring clients to submit
a certificate proving their entitlement to content before receiving the content.

%prep
%autosetup -n %{pypi_name}-%{version}rc5
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/pulp_certguard
%{python3_sitelib}/pulp_certguard-%{version}rc5-py%{python3_version}.egg-info

%changelog
* Wed May 27 2020 Justin Sherrill <jsherril@redhat.com> 0.1.0-0.1.rc5
- Update to 0.1.rc5

* Thu Apr 30 2020 Evgeni Golov - 0.1.0-0.1.rc4
- Initial package.
