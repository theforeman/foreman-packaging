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

%if 0%{?rhel}
%define repo_dist el%{rhel}
%endif
%endif

%global release 1
%global prereleasesource develop
%global prerelease %{?prereleasesource}

Name:     foreman-release
Version:  3.17.0
Release:  %{?prerelease:0.}%{release}%{?prerelease:.}%{?prerelease}%{?dist}

Summary:  Foreman repositories meta-package
Group:    Applications/System
License:  GPLv3+
URL:      https://theforeman.org
Source0:  foreman.repo
Source1:  foreman-plugins.repo
Source2:  foreman.gpg
Source5:  foreman-client.repo

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
* Wed Aug 13 2025 Ondřej Gajdušek <ogajduse@redhat.com> - 3.17.0-0.1.develop
- Bump version to 3.17-develop

* Mon May 19 2025 Ondřej Gajdušek <ogajduse@redhat.com> - 3.16.0-0.1.develop
- Bump version to 3.16-develop

* Tue Feb 18 2025 Patrick Creech <pcreech@redhat.com> - 3.15.0-0.1.develop
- Bump version to 3.15-develop

* Wed Nov 06 2024 Patrick Creech <pcreech@redhat.com> - 3.14.0-0.1.develop
- Bump version to 3.14-develop

* Tue Aug 20 2024 Patrick Creech <pcreech@redhat.com> - 3.13.0-0.1.develop
- Bump version to 3.13-develop

* Wed May 22 2024 Zach Huntington-Meath <zhunting@redhat.com> - 3.12.0-0.1.develop
- Bump version to 3.12-develop

* Tue Feb 20 2024 Patrick Creech <pcreech@redhat.com> - 3.11.0-0.1.develop
- Bump version to 3.11-develop

* Tue Dec 12 2023 Eric D. Helms <ericdhelms@gmail.com> - 3.10.0-0.2.develop
- Hardcode EL7 dist to 7

* Wed Nov 29 2023 Zach Huntington-Meath <zhunting@redhat.com> - 3.10.0-0.1.develop
- Bump version to 3.10-develop

* Fri Sep 29 2023 Eric D. Helms <ericdhelms@gmail.com> - 3.9.0-0.2.develop
- Drop qpid repo

* Wed Aug 23 2023 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 3.9.0-0.1.develop
- Bump version to 3.9-develop

* Tue May 23 2023 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 3.8.0-0.1.develop
- Bump version to 3.8-develop

* Wed Feb 22 2023 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 3.7.0-0.1.develop
- Bump version to 3.7-develop

* Tue Nov 08 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 3.6.0-0.1.develop
- Bump version to 3.6-develop

* Wed Aug 10 2022 Patrick Creech <pcreech@redhat.com> - 3.5.0-0.1.develop
- Bump version to 3.5-develop

* Tue May 17 2022 Eric D. Helms <ericdhelms@gmail.com> - 3.4.0-0.2.develop
- Drop use of module_hotfixes, there are modules now

* Tue May 10 2022 Odilon Sousa <osousa@redhat.com> - 3.4.0-0.1.develop
- Bump version to 3.4-develop

* Thu Feb 10 2022 Zach Huntington-Meath <zhunting@redhat.com> - 3.3.0-0.1.develop
- Bump version to 3.3-develop

* Tue Jan 25 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 3.2.0-0.2.develop
- Drop EL6 compatibility

* Fri Nov 12 2021 Odilon Sousa <osousa@redhat.com> - 3.2.0-0.1.develop
- Bump version to 3.2-develop

* Thu Sep 16 2021 Evgeni Golov - 3.1.0-0.2.develop
- Enable the qpid copr for EL7 clients

* Thu Aug 05 2021 Patrick Creech <pcreech@redhat.com> - 3.1.0-0.1.develop
- Bump version to 3.1-develop

* Thu Jul 22 2021 Tomer Brisker <tbrisker@gmail.com> - 3.0.0-0.1.develop
- Bump version to 3.0-develop

* Tue May 04 2021 Zach Huntington-Meath <zhunting@redhat.com> - 2.6.0-0.1.develop
- Bump version to 2.6-develop

* Tue Feb 02 2021 Evgeni Golov - 2.5.0-0.1.develop
- Bump version to 2.5-develop

* Mon Dec 07 2020 Evgeni Golov - 2.4.0-0.2.develop
- remove EL5 bits that aren't longer needed

* Mon Nov 02 2020 Patrick Creech <pcreech@redhat.com> - 2.4.0-0.1.develop
- Bump version to 2.4-develop

* Tue Aug 11 2020 Eric D. Helms <ericdhelms@gmail.com> - 2.3.0-0.1.develop
- Bump version to 2.3-develop

* Wed May 13 2020 Eric D. Helms <ericdhelms@gmail.com> - 2.2.0-0.3.develop
- Bump version to 2.2-develop

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
