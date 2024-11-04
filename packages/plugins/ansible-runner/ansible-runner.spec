%global python3_pkgversion 3.11
%global __python3 /usr/bin/python3.11
%global pypi_name ansible-runner

Name:           %{pypi_name}
Version:        2.3.6
Release:        1%{?dist}
Summary:        A tool and python library to interface with Ansible

License:        ASL 2.0
URL:            https://github.com/ansible/ansible-runner
Source0:        https://github.com/ansible/%{pypi_name}/archive/%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-setuptools
BuildRequires: python%{python3_pkgversion}-pbr
BuildRequires: python%{python3_pkgversion}-rpm-macros
Requires:      python%{python3_pkgversion}-%{pypi_name} = %{version}-%{release}
Obsoletes:     python3-%{pypi_name} < %{version}
Obsoletes:     python38-%{pypi_name} < %{version}
Obsoletes:     python39-%{pypi_name} < %{version}-%{release}

%description
Ansible Runner is a tool and python library that helps when interfacing with
Ansible from other systems whether through a container image interface, as a
standalone tool, or imported into a python project.

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Requires:       python%{python3_pkgversion}-pyyaml
Requires:       python%{python3_pkgversion}-setuptools
Requires:       python%{python3_pkgversion}-daemon
Requires:       python%{python3_pkgversion}-six
Requires:       python%{python3_pkgversion}-packaging
Requires:       python%{python3_version}dist(pexpect) >= 4.6

%description -n python%{python3_pkgversion}-%{pypi_name}
Ansible Runner is a tool and python library that helps when interfacing with
Ansible from other systems whether through a container image interface, as a
standalone tool, or imported into a python project.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
export PBR_VERSION=%{version}
%py3_build

%install
export PBR_VERSION=%{version}
%py3_install

cp %{buildroot}/%{_bindir}/ansible-runner %{buildroot}/%{_bindir}/ansible-runner-%{python3_version}
ln -s %{_bindir}/ansible-runner-%{python3_version} %{buildroot}/%{_bindir}/ansible-runner-3

%files
%defattr(-,root,root)
%{_bindir}/ansible-runner
%{_bindir}/ansible-runner-3
%{_bindir}/ansible-runner-%{python3_version}
%{_datadir}/ansible-runner/*
%exclude %{_datadir}/packaging
%exclude %{_datadir}/utils

%files -n python%{python3_pkgversion}-%{pypi_name}
%{python3_sitelib}/*

%changelog
* Fri Sep 06 2024 Evgeni Golov - 2.3.6-1
- Release ansible-runner 2.3.6

* Mon Jan 15 2024 Eric D. Helms <ericdhelms@gmail.com> - 2.2.1-6
- Exclude packaging directory

* Mon Dec 18 2023 Evgeni Golov - 2.2.1-5
- Obsolete Python 3.9 package to smoothen upgrade path

* Fri Dec 01 2023 Odilon Sousa <osousa@redhat.com> - 2.2.1-4
- Rebuild ansible-runner against python 3.11

* Tue Sep 27 2022 Eric D. Helms <ericdhelms@gmail.com> - 2.2.1-3
- Add obsolete on python3-ansible-runner
- Move ansible-runner binary to ansible-runner package

* Thu Sep 22 2022 Eric D. Helms <ericdhelms@gmail.com> - 2.2.1-2
- Add requires for python-packaging

* Tue Jun 21 2022 Dimitri Savineau <dsavinea@redhat.com> - 2.2.1-1
- Ansible Runner 2.2.1-1

* Fri May 06 2022 Satoe Imaishi <simaishi@redhat.com> - 2.2.0-2
- Ansible Runner 2.2.0-2

* Wed Nov 17 2021 Satoe Imaishi <simaishi@redhat.com> - 2.1.1-1
- Ansible Runner 2.1.1-1

* Fri Jul 02 2021 Satoe Imaishi <simaishi@redhat.com> - 2.0.1-1
- Ansible Runner 2.0.1-1

* Mon Jun 28 2021 Satoe Imaishi <simaishi@redhat.com> - 2.0.0-1
- Ansible Runner 2.0.0-1

* Thu Mar 19 2020 Ryan Petrello <rpetrell@redhat.com> - 1.4.6-1
- Ansible Runner 1.4.6-1

* Thu Mar 19 2020 Matthew Jones <matburt@redhat.com> - 1.4.5-1
- Ansible Runner 1.4.5-1

* Tue Feb 25 2020 Yanis Guenane <yguenane@redhat.com> - 1.4.4-3
- Ansible Runner 1.4.4-3

* Fri Oct 25 2019 Matthew Jones <matburt@redhat.com> - 1.4.4-1
- Ansible Runner 1.4.4-1

* Thu Oct 17 2019 Matthew Jones <matburt@redhat.com> - 1.4.2-1
- Ansible Runner 1.4.2-1

* Thu Oct 03 2019 Matthew Jones <matburt@redhat.com> - 1.4.1-1
- Ansible Runner 1.4.1-1

* Mon Sep 23 2019 Shane McDonald <shanemcd@redhat.com> - 1.4.0-1
- Ansible Runner 1.4.0-1
- Support for EL 7.7 (defaults to python2)

* Wed Apr 24 2019 Shane McDonald <shanemcd@redhat.com> - 1.3.4-1
- Ansible Runner 1.3.4-1
- Adopted modified upstream spec file for python3 support
