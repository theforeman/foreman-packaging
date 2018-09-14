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

%global release 5
%global prerelease develop

Name:     foreman-release
Version:  1.20.0
Release:  %{?prerelease:0.}%{release}%{?prerelease:.}%{?prerelease}%{?dist}

Summary:  Foreman repositories meta-package
Group:    Applications/System
License:  GPLv3+
URL:      https://theforeman.org
Source0:  foreman.repo
Source1:  foreman-plugins.repo
Source2:  foreman.gpg
Source3:  foreman-rails.repo
Source4:  foreman-rails.gpg
Source5:  foreman-client.repo

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
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-foreman

%if 0%{?suse_version}
%dir /etc/pki
%dir /etc/pki/rpm-gpg
%dir /etc/zypp
%dir %{repo_dir}
%endif

%install
install -Dpm0644 %{SOURCE0} %{buildroot}%{repo_dir}/foreman.repo
install -Dpm0644 %{SOURCE1} %{buildroot}%{repo_dir}/foreman-plugins.repo
install -Dpm0644 %{SOURCE3} %{buildroot}%{repo_dir}/foreman-rails.repo
install -Dpm0644 %{SOURCE5} %{buildroot}%{repo_dir}/foreman-client.repo

trimmed_dist=`echo %{repo_dist} | sed 's/^\.//'`
sed "s/\$DIST/${trimmed_dist}/g" -i %{buildroot}%{repo_dir}/*.repo

if [[ '%{release}' != *"develop"* ]];then
  VERSION="%{version}"
  sed "s/nightly/${VERSION%.*}/g" -i %{buildroot}%{_sysconfdir}/yum.repos.d/*.repo
  sed "s/gpgcheck=0/gpgcheck=1/g" -i %{buildroot}%{_sysconfdir}/yum.repos.d/foreman.repo
  sed "s/gpgcheck=0/gpgcheck=1/g" -i %{buildroot}%{_sysconfdir}/yum.repos.d/foreman-rails.repo
fi

install -Dpm0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-foreman
install -Dpm0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-foreman-rails

%files
%config %{repo_dir}/foreman.repo
%config %{repo_dir}/foreman-plugins.repo
%config %{repo_dir}/foreman-rails.repo
%{_sysconfdir}/pki/rpm-gpg/*

%changelog
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
