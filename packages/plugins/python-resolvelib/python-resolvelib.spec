%global python3_pkgversion 3.12
%global __python3 /usr/bin/python3.12

# Created by pyp2rpm-3.3.3
%global pypi_name resolvelib

Name:           python-%{pypi_name}
Version:        1.0.1
Release:        2%{?dist}
Summary:        Resolve abstract dependencies into concrete ones

License:        ISC License
URL:            https://github.com/sarugaku/resolvelib
Source0:        https://files.pythonhosted.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-rpm-macros
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  python%{python3_pkgversion}-pip

%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}


%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
%autosetup -n %{pypi_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%files
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info



%changelog
* Wed Jan 29 2025 Odilon Sousa <osousa@redhat.com> - 1.0.1-2
- Rebuild against python 3.12

* Thu Feb 08 2024 Satoe Imaishi <simaishi@redhat.com> - 1.0.1-1
- Update to 1.0.1
- Rebuild for python 3.11

* Mon Jun 14 2021 Paul Belanger <pabelanger@redhat.com> - 0.5.4-1
- Initial package.
- Forked from https://fedora.pkgs.org/rawhide/fedora-x86_64/python3-resolvelib-0.5.5-2.fc35.noarch.rpm.html however
  downgraded to 0.5.4 due to 0.5.5 being yanked from pypi.

