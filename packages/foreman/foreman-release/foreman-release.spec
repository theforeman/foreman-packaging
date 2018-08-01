%global release 1
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

BuildArch: noarch

BuildRequires: sed

%description
Foreman repository contains open source and other distributable software for
distributions in RPM format. This package contains the repository configuration
for Yum.

%install
install -Dpm0644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/foreman.repo
install -Dpm0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/yum.repos.d/foreman-plugins.repo
install -Dpm0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/yum.repos.d/foreman-rails.repo

sed "s/\$DIST/$(echo %{?dist} | cut -d. -f2)/g" -i %{buildroot}%{_sysconfdir}/yum.repos.d/*.repo

if [[ '%{release}' != *"develop"* ]];then
  VERSION="%{version}"
  sed "s/nightly/${VERSION%.*}/g" -i %{buildroot}%{_sysconfdir}/yum.repos.d/*.repo
  sed "s/gpgcheck=0/gpgcheck=1/g" -i %{buildroot}%{_sysconfdir}/yum.repos.d/foreman.repo
fi

install -Dpm0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-foreman
install -Dpm0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-foreman-rails

%files
%config %{_sysconfdir}/yum.repos.d/*.repo
%{_sysconfdir}/pki/rpm-gpg/*

%changelog
* Wed Aug 01 2018 Eric D. Helms <ericdhelms@gmail.com> 1.20.0-0.1.develop
- Splitting out foreman-release package
