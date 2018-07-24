%global pulp_release stable
%global pulp_version 2.16
#%%global prever .rc2

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

Name:           katello-repos
Version:        3.7.0
Release:        1%{?prever}%{?dist}
Summary:        Definition of yum repositories for Katello

Group:          Applications/Internet
License:        GPLv2
URL:            https://theforeman.org/plugins/katello/
Source0:        katello.repo
Source1:        katello-client.repo
Source2:        RPM-GPG-KEY-katello-2015
Source3:        qpid-copr.repo

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires: sed

%description
Defines yum repositories for Katello and its sub projects, Candlepin and Pulp.

%package -n katello-client-repos
Summary:   Definition of yum repositories for Katello clients
Group:     Applications/System
Conflicts: katello-repos

%description -n katello-client-repos
Defines yum repositories for Katello clients.

%files -n katello-client-repos
%defattr(-, root, root)
%config %{repo_dir}/katello-client.repo
%if 0%{?rhel} == 6
%config %{repo_dir}/qpid-copr.repo
%endif

%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-katello

%prep

%build

%install
rm -rf %{buildroot}

#prepare dir structure
install -d -m 0755 %{buildroot}%{repo_dir}
install -d -m 0755 %{buildroot}%{_sysconfdir}/pki/rpm-gpg/

install -m 644 %{SOURCE0} %{buildroot}%{repo_dir}/
install -m 644 %{SOURCE1} %{buildroot}%{repo_dir}/

%if 0%{?rhel} == 6
install -m 644 %{SOURCE3} %{buildroot}%{repo_dir}/
%endif

install -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-katello

if [[ '%{release}' == *"nightly"* ]];then
    REPO_VERSION='nightly'
    REPO_NAME='Nightly'
else
    # Get major.minor from the version
    REPO_VERSION="$(echo '%{version}' | sed 's/\([^\.]\+\.[^\.]\+\)\..\+/\1/')"
    REPO_NAME=$REPO_VERSION
fi

for repofile in %{buildroot}%{repo_dir}/*.repo; do
    trimmed_dist=`echo %{repo_dist} | sed 's/^\.//'`
    sed -i "s/@DIST@/${trimmed_dist}/" $repofile
    sed -i "s/@RHEL@/%{rhel}/" $repofile
    sed -i "s/@REPO_VERSION@/${REPO_VERSION}/" $repofile
    sed -i "s/@REPO_NAME@/${REPO_NAME}/" $repofile
    sed -i "s/@PULP_RELEASE@/%pulp_release/" $repofile
    sed -i "s/@PULP_VERSION@/%pulp_version/" $repofile
done

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%config %{repo_dir}/*.repo
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-katello

%if 0%{?suse_version}
%dir /etc/pki
%dir /etc/pki/rpm-gpg
%dir /etc/zypp
%dir %{repo_dir}
%endif

%changelog
* Tue Jul 24 2018 Jonathon Turel <jturel@gmail.com> 3.7.0-1
- Rev for 3.7 GA

* Mon Jul 16 2018 Jonathon Turel <jturel@gmail.com> 3.7.0-1.rc2
- Rev for 3.7 RC2

* Thu Jun 28 2018 Jonathon Turel <jturel@gmail.com> 3.7.0-2.rc1
- remove gofer-copr.repo

* Mon Jun 11 2018 Jonathon Turel <jturel@gmail.com> 3.7.0-1.rc1
- Rev for 3.7 RC1

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
