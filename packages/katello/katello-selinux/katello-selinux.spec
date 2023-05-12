# vim: sw=4:ts=4:et
#
# Copyright (c) 2013 Red Hat, Inc.

# This program and entire repository is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the License,
# or any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.
#

%define selinux_variants targeted
%define selinux_modules katello

%define moduletype apps


Name:           katello-selinux
Version:        5.0.2
Release:        1%{?dotalphatag}%{?dist}
Summary:        SELinux policy module for katello

Group:          System Environment/Base
License:        GPLv3+
URL:            http://www.katello.org
Source0:        https://codeload.github.com/Katello/%{name}/tar.gz/%{version}

BuildRequires:  checkpolicy
BuildRequires:  selinux-policy-devel
BuildRequires:  hardlink
BuildRequires:  policycoreutils
BuildRequires:  /usr/bin/pod2man
BuildArch:      noarch

Requires:           foreman-selinux
Requires:           candlepin-selinux >= 3.1.10
Requires:           selinux-policy >= %{_selinux_policy_version}
Requires(post):     /usr/sbin/semodule
Requires(post):     /sbin/restorecon
Requires(post):     /usr/sbin/setsebool
Requires(post):     /usr/sbin/selinuxenabled
Requires(post):     /usr/sbin/semanage
Requires(post):     selinux-policy-targeted
Requires(postun):   /usr/sbin/semodule
Requires(postun):   /sbin/restorecon

Obsoletes: crane-selinux < 4.0.0

%if 0%{?rhel} == 7
Requires(post):     policycoreutils-python
%else
Requires(post):     policycoreutils-python-utils
%endif

%description
SELinux policy module for Katello

%prep
%setup -q -n %{name}-%{version}%{?dashalphatag}

%build
# determine distribution name and version
%if 0%{?rhel} >= 6
%define distver rhel%{rhel}
%endif
%if 0%{?fedora} >= 18
%define distver fedora%{fedora}
%endif

# build policy
for selinuxvariant in %{selinux_variants}; do
    make clean all NAME=${selinuxvariant} DISTRO=%{distver} VERSION=%{version} INSTPREFIX=%{buildroot}
    for selinuxmodule in %{selinux_modules}; do
        mv ${selinuxmodule}.pp.bz2 ${selinuxmodule}-${selinuxvariant}.pp.bz2
    done
done

%install
# install policy modules manually
for selinuxvariant in %{selinux_variants}; do
    install -d %{buildroot}%{_datadir}/selinux/${selinuxvariant}
    for selinuxmodule in %{selinux_modules}; do
        install -p -m 644 ${selinuxmodule}-${selinuxvariant}.pp.bz2 \
            %{buildroot}%{_datadir}/selinux/${selinuxvariant}/${selinuxmodule}.pp.bz2
    done
done

# install the rest
make clean install-data NAME=${selinuxvariant} DISTRO=%{distver} VERSION=%{version} INSTPREFIX=%{buildroot}

%post
# install and upgrade
%{_sbindir}/%{name}-enable

%posttrans
if /usr/sbin/selinuxenabled; then
    # install and upgrade
    %{_sbindir}/%{name}-relabel
fi

%preun
# uninstall only
if [ $1 -eq 0 ]; then
    %{_sbindir}/%{name}-disable
fi

# upgrade and uninstall
if /usr/sbin/selinuxenabled; then
    %{_sbindir}/%{name}-relabel
fi

%files
%license LICENSE
%doc katello.fc katello.if katello.te
%attr(0600,root,root) %{_datadir}/selinux/*/katello.pp.bz2
%{_datadir}/selinux/devel/include/%{moduletype}/katello.if
%attr(0755,root,root) %{_sbindir}/%{name}-enable
%attr(0755,root,root) %{_sbindir}/%{name}-disable
%attr(0755,root,root) %{_sbindir}/%{name}-relabel
%{_mandir}/man8/%{name}-enable.8.gz
%{_mandir}/man8/%{name}-disable.8.gz
%{_mandir}/man8/%{name}-relabel.8.gz

%changelog
* Fri May 12 2023 Eric D. Helms <ericdhelms@gmail.com> 5.0.2-1
- Update to 5.0.2

* Thu May 11 2023 Eric D. Helms <ericdhelms@gmail.com> 5.0.1-1
- Update to 5.0.1

* Wed May 03 2023 Eric D. Helms <ericdhelms@gmail.com> 5.0.0-1
- Update to 5.0.0

* Wed Dec 07 2022 Evgeni Golov - 4.0.2-3
- Use _selinux_policy_version macro from selinux-policy package

* Tue Jul 12 2022 Evgeni Golov - 4.0.2-2
- Fixes #35198 - always load SELinux definitions

* Tue Jun 29 2021 Eric D. Helms <ericdhelms@gmail.com> - 4.0.2-1
- Release katello-selinux 4.0.2

* Fri Feb 05 2021 Eric D. Helms <ericdhelms@gmail.com> - 4.0.0-1
- Release katello-selinux 4.0.0

* Wed Feb 03 2021 Eric D. Helms <ericdhelms@gmail.com> - 3.6.0-1
- Release katello-selinux 3.6.0

* Mon Jan 04 2021 Eric D. Helms <ericdhelms@gmail.com> - 3.5.1-1
- Release katello-selinux 3.5.1

* Tue Aug 25 2020 Eric D. Helms <ericdhelms@gmail.com> - 3.5.0-1
- Release katello-selinux 3.5.0

* Wed Jul 29 2020 Eric D. Helms <ericdhelms@gmail.com> - 3.4.0-1
- Add crane-selinux sub-package

* Wed Jul 15 2020 Eric D. Helms <ericdhelms@gmail.com> - 3.3.1-1
- Release katello-selinux 3.3.1

* Wed Jul 01 2020 Eric D. Helms <ericdhelms@gmail.com> - 3.3.0-1
- Release katello-selinux 3.3.0

* Thu Jun 18 2020 Eric D. Helms <ericdhelms@gmail.com> - 3.2.0-1
- Release katello-selinux 3.2.0

* Tue May 05 2020 Jonathon Turel <jturel@gmail.com> - 3.1.2-1
- Require candlepin-selinux

* Tue Apr 07 2020 Eric D. Helms <ericdhelms@gmail.com> - 3.1.1-2
- Update spec and build for EL8

* Thu Apr 04 2019 Tomer Brisker <tbrisker@gmail.com> - 3.1.1-1
- Release katello-selinux 3.1.1

* Wed Apr 03 2019 Eric D. Helms <ericdhelms@gmail.com> - 3.1.0-1
- Release katello-selinux 3.1.0

* Thu Jul 27 2017 Justin Sherrill <jsherril@redhat.com> 3.0.3-1
- Upgrade katello-selinux to 3.0.3 (akofink@redhat.com)

* Wed Dec 21 2016 Justin Sherrill <jsherril@redhat.com> 3.0.2-1
- build katello-selinux 3.0.2 (jsherril@redhat.com)

* Tue Feb 23 2016 Eric D Helms <ericdhelms@gmail.com> 3.0.1-1
- Updating katello-selinux to 3.0.1 (cduryee@redhat.com)

* Wed Jul 29 2015 Eric D. Helms <ericdhelms@gmail.com> 2.2.2-1
- new package built with tito

* Wed Feb 18 2015 Justin Sherrill <jsherril@redhat.com> 2.2.1-1
- fixing spec file name and SOURCE extension (jsherril@redhat.com)

* Wed Feb 18 2015 Justin Sherrill <jsherril@redhat.com> 2.2.0-0
- new package built with tito


