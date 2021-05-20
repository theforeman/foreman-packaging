%global pulpcore_version 3.9

%define repo_dir %{_sysconfdir}/yum.repos.d
%define repo_dist %{dist}

%global release 1

Name:           katello-repos
Version:        4.0.1
Release:        %{?prerelease:0.}%{release}%{?prerelease}%{?dist}
Summary:        Definition of yum repositories for Katello

Group:          Applications/Internet
License:        GPLv2
URL:            https://theforeman.org/plugins/katello/
Source0:        katello.repo

BuildArch:      noarch

BuildRequires:  sed

Requires:       foreman-release

%description
Defines yum repositories for Katello and its sub projects, Candlepin and Pulp.

%prep

%build

%install
rm -rf %{buildroot}

#prepare dir structure
install -d -m 0755 %{buildroot}%{repo_dir}
install -d -m 0755 %{buildroot}%{_sysconfdir}/pki/rpm-gpg/

install -m 644 %{SOURCE0} %{buildroot}%{repo_dir}/

if [[ '%{release}' == *"nightly"* ]];then
    REPO_VERSION='nightly'
    REPO_NAME='Nightly'
    REPO_GPGCHECK=0
else
    # Get major.minor from the version
    REPO_VERSION="$(echo '%{version}' | sed 's/\([^\.]\+\.[^\.]\+\)\..\+/\1/')"
    REPO_NAME=$REPO_VERSION
    REPO_GPGCHECK=1
fi

for repofile in %{buildroot}%{repo_dir}/*.repo; do
    trimmed_dist=`echo %{repo_dist} | sed 's/^\.//'`
    sed -i "s/@DIST@/${trimmed_dist}/" $repofile
    sed -i "s/@RHEL@/%{rhel}/" $repofile
    sed -i "s/@REPO_VERSION@/${REPO_VERSION}/" $repofile
    sed -i "s/@REPO_NAME@/${REPO_NAME}/" $repofile
    sed -i "s/@REPO_GPGCHECK@/${REPO_GPGCHECK}/" $repofile
    sed -i "s/@PULPCORE_VERSION@/%pulpcore_version/" $repofile
done

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%config %{repo_dir}/*.repo

%changelog
* Thu May 20 2021 Patrick Creech <pcreech@redhat.com> - 4.0.1-1
- Release katello-repos 4.0.1

* Tue Apr 20 2021 Zach Huntington-Meath <zhunting@redhat.com> - 4.0.0-1
- Release katello-repos 4.0.0

* Tue Mar 23 2021 Evgeni Golov - 4.0.0-0.5.rc3
- Consume repositories from yum.theforeman.org

* Fri Mar 19 2021 Patrick Creech <pcreech@redhat.com> - 4.0.0-0.4.rc3
- Release katello-repos 4.0.0

* Wed Mar 03 2021 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 4.0.0-0.4.rc1
- Remove Pulp 2 and qpid copr repository definitions
- Always GPG check pulpcore repositories

* Tue Feb 09 2021 Evgeni Golov - 4.0.0-0.3.rc1
- Release katello-repos 4.0.0

* Mon Jan 11 2021 Ian Ballou <ianballou67@gmail.com> - 4.0-0.3.nightly
- use pulpcore 3.9 repos

* Wed Nov 25 2020 Evgeni Golov - 4.0-0.2.nightly
- add qpid copr

* Wed Nov 04 2020 Jonathon Turel <jturel@gmail.com> - 4.0-0.1.nightly
- Bump version to 4.0.0

* Thu Oct 29 2020 Justin Sherrill <jsherril@redhat.com> 3.18-0.5.nightly
- use pulpcore 3.7 repos

* Thu Sep 24 2020 Evgeni Golov - 3.18-0.4.nightly
- Only enable Pulp2 repos on EL7

* Wed Sep 16 2020 Evgeni Golov - 3.18-0.3.nightly
- load pulpcore gpg keys from the server

* Mon Aug 31 2020 Evgeni Golov - 3.18-0.2.nightly
- Use the new pulpcore repos

* Tue Aug 11 2020 Eric D. Helms <ericdhelms@gmail.com> - 3.18-0.1.nightly
- Bump to 3.18.0

* Thu May 14 2020 Eric D. Helms <ericdhelms@gmail.com> - 4.0.0-0.1.nightly
- Update to 4.0

* Wed Apr 22 2020 Eric D. Helms <ericdhelms@gmail.com> - 3.15.0-0.4.nightly
- Add module_hotfixes to repo files

* Fri Dec 13 2019 Evgeni Golov - 3.15.0-0.3.nightly
- Add pulpcore repository

* Mon Nov 18 2019 Evgeni Golov - 3.15.0-0.2.nightly
- Unify prerelease macro handling

* Fri Nov 01 2019 Jonathon Turel <jturel@gmail.com> - 3.15.0-0.1.nightly
- Bump version to 3.15.0

* Mon Oct 21 2019 Evgeni Golov - 3.14.0-0.4.nightly
- Use RPM-GPG-KEY-foreman from foreman-release

* Mon Oct 21 2019 Evgeni Golov - 3.14.0-0.3.nightly
- Automatically set gpgcheck=1 for release versions

* Tue Oct 08 2019 Partha Aji <paji@redhat.com> - 3.14.0-0.2.nightly
- Adding pulp 2.21 GA

* Wed Aug 07 2019 Evgeni Golov - 3.14.0-0.1.nightly
- Bump version to 3.14

* Thu Aug 1 2019 Justin Sherrill <jlsherrill@gmail.com> - 3.13.0-0.2.nightly
- use pulp 2.20

* Tue Apr 23 2019 Evgeni Golov <evgeni@golov.de> - 3.13.0-0.1.nightly
- Bump version to 3.13-nightly

* Sat Apr 06 2019 Partha Aji <paji@redhat.com> - 3.12.0-0.2.nightly
- use stable pulp 2.19 repository

* Wed Jan 16 2019 Eric D. Helms <ericdhelms@gmail.com> - 3.12.0-0.1.nightly
- Bump version to 3.12

* Tue Jan 15 2019 Justin Sherrill <jlsherrill@gmail.com> - 3.11.0-0.2.nightly
- use stable pulp 2.18 repository

* Fri Nov 30 2018 Eric D. Helms <ericdhelms@gmail.com> - 3.11.0-0.1.nightly
- Bump version to 3.11

* Mon Nov 26 2018 John Mitsch <parthaa@redhat.com> - 3.10.0-0.4.nightly
- Switch to Pulp 2-18 beta

* Wed Oct 24 2018 John Mitsch <jomitsch@redhat.com> - 3.10.0-0.3.nightly
- Switch to Pulp nightly

* Mon Oct 22 2018 Eric D. Helms <ericdhelms@gmail.com> - 3.10.0-0.2.nightly
- Drop client repos

* Thu Oct 18 2018 Eric D. Helms <ericdhelms@gmail.com> - 3.10.0-0.1.nightly
- Bump version to 3.10

* Fri Aug 17 2018 Partha Aji <paji@redhat.com> - 3.9.0-0.4.nightly
- Switch to Pulp 2.17 beta

* Wed Jul 25 2018 Eric D. Helms <ericdhelms@gmail.com> - 3.9.0-0.3.nightly
- Add nightly back to release

* Tue Jul 24 2018 Eric D. Helms <ericdhelms@gmail.com> - 3.9.0-2
- Add prerelease macro support

* Wed Jul 18 2018 Eric D. Helms <ericdhelms@gmail.com> 3.9.0-1.nightly
- Bump

* Wed Jun 27 2018 Jonathon Turel <jturel@gmail.com> 3.8.0-2.nightly
- remove gofer-copr.repo

* Thu Apr 19 2018 Eric D. Helms <ericdhelms@gmail.com> 3.7.0-3.nightly
- Switch to using Pulp 2.16 stable (ericdhelms@gmail.com)

* Tue Jan 30 2018 Eric D. Helms <ericdhelms@gmail.com> 3.7.0-2.nightly
- Switch to using Pulp 2.15 stable (ericdhelms@gmail.com)

* Tue Jan 16 2018 Eric D. Helms <ericdhelms@gmail.com> 3.7.0-1.nightly
- Bump katello RPMs to 3.7.0 (ericdhelms@gmail.com)
- Automatic commit of package [katello-repos] minor release
  [3.6.0-2.nightly.fm1_18]. (ericdhelms@gmail.com)

* Mon Jan 15 2018 Eric D. Helms <ericdhelms@gmail.com> 3.6.0-2.nightly
- new package built with tito

* Wed Jul 05 2017 Eric D. Helms <ericdhelms@gmail.com> 3.5.0-1.nightly
- Bump specs to 3.5.0 (ericdhelms@gmail.com)
- Update katello-repos.spec so that repo files are config files
  (Klaas-@users.noreply.github.com)
- Bumping nightly builds to 3.4.0 (jsherril@redhat.com)
- Updated for fedora 24 (jomitsch@redhat.com)
- Katello version bump to 3.3.0 (jomitsch@redhat.com)
- allow for easier repo version setting (jsherril@redhat.com)

* Thu Jul 21 2016 Justin Sherrill <jsherril@redhat.com> 3.2.0-2.nightly
- Refs #13017 - include qpid-copr for client repos (jsherril@redhat.com)

* Wed Jul 20 2016 Justin Sherrill <jsherril@redhat.com> 3.2.0-1.nightly
- Fixes #13017 - remove priorities to use qpid from epel (jsherril@redhat.com)

* Fri Mar 18 2016 Eric D Helms <ericdhelms@gmail.com> 3.1.0-2.nightly
- Fixes #14260: Ensure the leading dot is removed from dist in repos RPM
  (ericdhelms@gmail.com)

* Wed Mar 16 2016 Eric D Helms <ericdhelms@gmail.com> 3.1.0-1.nightly
- Fixes #14189: Move repo definitions to be dist based (ericdhelms@gmail.com)
- updating nightly to 2.5 (jsherril@redhat.com)
- Fixes #11746: Correct source URL for repositories RPM (ericdhelms@gmail.com)

* Fri Aug 07 2015 Eric D. Helms <ericdhelms@gmail.com> 2.4.0-2.nightly
- Add priority back to repos. (ericdhelms@gmail.com)

* Wed Jul 29 2015 Eric D. Helms <ericdhelms@gmail.com> 2.4.0-1.nightly
- new package built with tito

* Tue Mar 24 2015 Eric D. Helms <ericdhelms@gmail.com> 2.3.0-2
- Fixes #7760: Adds client repo (ericdhelms@gmail.com)

* Tue Feb 24 2015 Eric D. Helms <ericdhelms@gmail.com> 2.3.0-1
-

* Tue Feb 24 2015 Eric D. Helms <ericdhelms@gmail.com> 2.2.0-2
- Bump release to 2.2.0-2 (ericdhelms@gmail.com)
- Update repo name to nightly for Katello. (ericdhelms@gmail.com)
- fixing repo urls to match new format (jsherril@redhat.com)
- fixes #7959 - use https for yum repos and local gpg key (jsherril@redhat.com)
- fixes #7739 - combine three katello repo files into one (jsherril@redhat.com)

* Tue Feb 24 2015 Eric D. Helms <ericdhelms@gmail.com>
- Update repo name to nightly for Katello. (ericdhelms@gmail.com)
- fixing repo urls to match new format (jsherril@redhat.com)
- fixes #7959 - use https for yum repos and local gpg key (jsherril@redhat.com)
- fixes #7739 - combine three katello repo files into one (jsherril@redhat.com)

* Fri Dec 19 2014 David Davis <daviddavis@redhat.com> 2.2.0-1
- Merge pull request #39 from ehelms/fixes-7442 (eric.d.helms@gmail.com)
- Fixes #7442: Change repo structure to group by version and project.
  (ericdhelms@gmail.com)

* Fri Sep 12 2014 Justin Sherrill <jsherril@redhat.com> 2.1.0-1
- removing katello-foreman repo (mmccune@redhat.com)

* Fri Oct 11 2013 Partha Aji <paji@redhat.com> 1.5.1-1
- Bumping package versions for 1.5 (paji@redhat.com)

* Sat Apr 27 2013 Justin Sherrill <jsherril@redhat.com> 1.4.2-1
- Add 'repos/' from commit 'b3df18719d52a3a21ac88709d9d5a70e5f9be796'
  (jsherril@redhat.com)

* Fri Apr 12 2013 Justin Sherrill <jsherril@redhat.com> 1.4.1-1
- version bump to 1.4 (jsherril@redhat.com)

* Fri Apr 12 2013 Justin Sherrill <jsherril@redhat.com> 1.3.3-1
- remove old changelog entries (msuchy@redhat.com)

* Tue Dec 18 2012 Miroslav Suchý <msuchy@redhat.com> 1.3.2-1
- rebuild

* Thu Dec 06 2012 Eric D Helms <ehelms@redhat.com> 1.3.1-1
- Bumping package versions for 1.3. (ehelms@redhat.com)

* Thu Dec 06 2012 Eric D Helms <ehelms@redhat.com> 1.2.2-1
- Do not skip our repo (msuchy@redhat.com)

* Mon Oct 15 2012 Lukas Zapletal <lzap+git@redhat.com> 1.2.1-1
- Bumping package versions for 1.1.

* Mon Aug 20 2012 Miroslav Suchý <msuchy@redhat.com> 1.1.2-1
- replace SUBDIR also in katello-foreman.repo (msuchy@redhat.com)
- add katello-foreman.repo (msuchy@redhat.com)

* Fri Aug 03 2012 Miroslav Suchý <msuchy@redhat.com> 1.1.1-1
- use Katello gpg key (msuchy@redhat.com)
- fedora-pulp.repo is not used any more (msuchy@redhat.com)
- Bumping package versions for 1.1. (msuchy@redhat.com)

* Tue Jul 31 2012 Miroslav Suchý <msuchy@redhat.com> 1.0.1-1
- bump up version to 1.0 (msuchy@redhat.com)

* Mon Jul 30 2012 Miroslav Suchý <msuchy@redhat.com> 0.2.10-1
- fix typo caused by copy'n'paste' (msuchy@redhat.com)

* Sun Jul 29 2012 Miroslav Suchý <msuchy@redhat.com> 0.2.9-1
- fixing urls so they don't throw a 404 (adprice@redhat.com)
- point Source0 to fedorahosted.org where tar.gz are stored (msuchy@redhat.com)

* Fri Jul 27 2012 Miroslav Suchý <msuchy@redhat.com> 0.2.8-1
- fix typo in repo files (msuchy@redhat.com)

* Thu Jul 26 2012 Miroslav Suchý <msuchy@redhat.com> 0.2.7-1
- refactor katello-repos (msuchy@redhat.com)

* Tue Jul 17 2012 Lukas Zapletal <lzap+git@redhat.com> 0.2.6-1
- temporarily disabling pulp testing repo
- %%defattr is not needed since rpm 4.4

* Mon Jul 16 2012 Lukas Zapletal <lzap+git@redhat.com> 0.2.5-1
- correcting pulp testing URL in the repofile

* Thu May 10 2012 Lukas Zapletal <lzap+git@redhat.com> 0.2.4-1
- putting releasever instead of 6Server

* Thu May 10 2012 Lukas Zapletal <lzap+git@redhat.com> 0.2.3-1
- repos - testing rpm now has katello testing repo file
- repos - fixing name of katello repos

* Fri Apr 27 2012 Lukas Zapletal <lzap+git@redhat.com> 0.2.2-1
- correcting pulp testing repofile url
