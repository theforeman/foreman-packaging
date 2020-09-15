%if 0%{?suse_version}
%define dist suse%{?suse_version}
%define repo_dir %{_sysconfdir}/zypp/repos.d

%if 0%{?suse_version} < 1300
%define repo_dist sles11
%else
%define repo_dist sles12
%endif

%else
%define repo_dir %{_sysconfdir}/yum.repos.d
%define repo_dist %{dist}
%endif

%global release 1

Name:     foreman-release
Version:  2.1.2
Release:  %{?prerelease:0.}%{release}%{?prerelease:.}%{?prerelease}%{?dist}

Summary:  Foreman repositories meta-package
Group:    Applications/System
License:  GPLv3+
URL:      https://theforeman.org
Source0:  foreman.repo
Source1:  foreman-plugins.repo
Source2:  foreman.gpg
Source5:  foreman-client.repo
Source6:  qpid-copr.repo
Source7:  subscription-manager-el5.repo
Source8:  pulp.repo
Source9:  subscription-manager-el6.repo

# Required by RHEL5
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

BuildRequires: sed

%description
Foreman repository contains open source and other distributable software for
distributions in RPM format. This package contains the repository configuration
for Yum.

%package   -n foreman-client-release
Summary:   Foreman client repositories meta-package
Group:     Applications/System

%description -n foreman-client-release
Defines yum repositories for Foreman clients.

%files -n foreman-client-release
%config %{repo_dir}/foreman-client.repo
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-foreman-client

%if 0%{?rhel} == 6
%config %{repo_dir}/pulp.repo
%config %{repo_dir}/qpid-copr.repo
%config %{repo_dir}/subscription-manager.repo
%endif

%if 0%{?rhel} == 5
%config %{repo_dir}/pulp.repo
%config %{repo_dir}/subscription-manager.repo
%endif

%if 0%{?suse_version}
%dir /etc/pki
%dir /etc/pki/rpm-gpg
%dir /etc/zypp
%dir %{repo_dir}
%endif

%install
install -Dpm0644 %{SOURCE0} %{buildroot}%{repo_dir}/foreman.repo
install -Dpm0644 %{SOURCE1} %{buildroot}%{repo_dir}/foreman-plugins.repo
install -Dpm0644 %{SOURCE5} %{buildroot}%{repo_dir}/foreman-client.repo

%if 0%{?rhel} == 6
install -m 644 %{SOURCE8} %{buildroot}%{repo_dir}/pulp.repo
install -m 644 %{SOURCE6} %{buildroot}%{repo_dir}/qpid-copr.repo
install -m 644 %{SOURCE9} %{buildroot}%{repo_dir}/subscription-manager.repo
%endif

%if 0%{?rhel} == 5
install -m 644 %{SOURCE8} %{buildroot}%{repo_dir}/pulp.repo
install -m 644 %{SOURCE7} %{buildroot}%{repo_dir}/subscription-manager.repo
%endif

trimmed_dist=`echo %{repo_dist} | sed 's/^\.//'`
sed "s/\$DIST/${trimmed_dist}/g" -i %{buildroot}%{repo_dir}/*.repo

if [[ '%{release}' != *"develop"* ]];then
  VERSION="%{version}"
  sed "s/nightly/${VERSION%.*}/g" -i %{buildroot}%{repo_dir}/*.repo
  sed "s/gpgcheck=0/gpgcheck=1/g" -i %{buildroot}%{repo_dir}/foreman.repo
  sed "s/gpgcheck=0/gpgcheck=1/g" -i %{buildroot}%{repo_dir}/foreman-client.repo
fi

install -Dpm0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-foreman
install -Dpm0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-foreman-client

%files
%config %{repo_dir}/foreman.repo
%config %{repo_dir}/foreman-plugins.repo
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-foreman

%changelog
* Thu Aug 20 2020 Eric D. Helms <ericdhelms@gmail.com> - 2.1.2-1
- Release foreman-release 2.1.2

* Mon Aug 03 2020 Eric D. Helms <ericdhelms@gmail.com> - 2.1.1-1
- Release foreman-release 2.1.1

* Thu Jul 02 2020 Patrick Creech <pcreech@redhat.com> - 2.1.0-1
- Release foreman-release 2.1.0

* Thu Jun 18 2020 Evgeni Golov - 2.1.0-0.4.rc3
- Release foreman-release 2.1.0

* Tue Jun 02 2020 Eric D. Helms <ericdhelms@gmail.com> - 2.1.0-0.4.rc2
- Release foreman-release 2.1.0

* Mon May 18 2020 Evgeni Golov - 2.1.0-0.4.rc1
- Release foreman-release 2.1.0

* Wed May 13 2020 Eric D. Helms <ericdhelms@gmail.com> - 2.1.0-0.4.develop
- Add 2.1 GPG key

* Wed Apr 22 2020 Eric D. Helms <ericdhelms@gmail.com> - 2.1.0-0.3.develop
- Add module_hotfixes to repo files

* Tue Apr 07 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.1.0-0.2.develop
- Bump to release for EL8

* Thu Feb 13 2020 Tomer Brisker <tbrisker@gmail.com> - 2.1.0-0.1.develop
- Bump version to 2.1-develop

* Tue Feb 11 2020 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.0.0-0.3.develop
- Remove foreman-rails repository (#28979)

* Wed Jan 08 2020 Evgeni Golov - 2.0.0-0.2.develop
- Rebuild for EL8 client repository

* Mon Jan 06 2020 Tomer Brisker <tbrisker@gmail.com> - 2.0.0-0.1.develop
- Bump version to 2.0-develop

* Mon Nov 18 2019 Evgeni Golov - 1.25.0-0.2.develop
- Unify prerelease macro handling

* Wed Oct 30 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.25.0-0.1.develop
- Bump version to 1.25-develop

* Tue Jul 30 2019 Evgeni Golov - 1.24.0-0.1.develop
- Bump version to 1.24-develop

* Thu Jun 27 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.23.0-0.3.develop
- GPG sign foreman-client repository

* Fri May 24 2019 Evgeni Golov - 1.23.0-0.2.develop
- Include Pulp repo for EL5 clients

* Tue Apr 23 2019 Evgeni Golov <evgeni@golov.de> - 1.23.0-0.1.develop
- Bump version to 1.23-develop

* Tue Mar 19 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.22.0-0.2.develop
- Remove GPG key from -client package

* Wed Jan 16 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.22.0-0.1.develop
- Bump to 1.22

* Wed Nov 21 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.21.0-0.3.develop
- Remove duplicated sysconfdir macro

* Wed Nov 21 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.21.0-0.2.develop
- Use the correct yum repo dir in non-EL releases

* Wed Oct 17 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.21.0-0.1.develop
- Bump version to 1.21 and reset release

* Wed Oct 03 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.20.0-0.8.develop
- EL6 needs different sub-man repo

* Tue Oct 02 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.20.0-0.7.develop
- Add EL6 subscription-manager repository

* Thu Sep 27 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.20.0-0.6.develop
- Add required repos to deploy in foreman-client-release

* Fri Sep 14 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.20.0-0.5.develop
- Rename client subpackge to foreman-client-release

* Wed Sep 12 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.20.0-0.4.develop
- Add client release

* Wed Sep 12 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.20.0-0.3.develop
- Drop gpgcheck on foreman-rails on nightly

* Tue Sep 04 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.20.0-0.2.develop
- Correct Rails GPG key

* Wed Aug 01 2018 Eric D. Helms <ericdhelms@gmail.com> 1.20.0-0.1.develop
- Splitting out foreman-release package
