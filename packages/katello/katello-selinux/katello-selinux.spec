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

%if 0%{?rhel} == 5
# absolute minimum versions for RHEL 5
%define selinux_policy_ver 3.11.1-81
%else
# absolute minimum versions for RHEL 6
%define selinux_policy_ver 2.4.6-80
%endif
%define selinux_policycoreutils_ver 1.33.12-1

%define moduletype apps

# set and uncomment all three to set alpha tag
#global alphatag RC1
#global dotalphatag .%{alphatag}
#global dashalphatag -%{alphatag}

Name:           katello-selinux
Version:        3.0.3
Release:        2%{?dotalphatag}%{?dist}
Summary:        SELinux policy module for katello

Group:          System Environment/Base
License:        GPLv3+
URL:            http://www.katello.org
Source0:        https://codeload.github.com/Katello/%{name}/tar.gz/%{version}

BuildRequires:  checkpolicy, selinux-policy-devel, hardlink
BuildRequires:  policycoreutils >= %{selinux_policycoreutils_ver}
BuildRequires:  /usr/bin/pod2man
BuildArch:      noarch

Requires:           selinux-policy >= %{selinux_policy_ver}
Requires:           foreman-selinux >= 1.17
Requires(post):     /usr/sbin/semodule, /sbin/restorecon, /usr/sbin/setsebool, /usr/sbin/selinuxenabled, /usr/sbin/semanage
Requires(post):     policycoreutils-python
Requires(post):     selinux-policy-targeted
Requires(postun):   /usr/sbin/semodule, /sbin/restorecon

%description
SELinux policy module for Katello

%prep
%setup -q -n %{name}-%{version}%{?dashalphatag}

%build
exit 1
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
if /usr/sbin/selinuxenabled; then
    # install and upgrade
    %{_sbindir}/%{name}-enable
fi

%posttrans
if /usr/sbin/selinuxenabled; then
    # install and upgrade
    %{_sbindir}/%{name}-relabel
fi

%preun
if /usr/sbin/selinuxenabled; then
    # uninstall only
    if [ $1 -eq 0 ]; then
        %{_sbindir}/%{name}-disable
    fi
    # upgrade and uninstall
    %{_sbindir}/%{name}-relabel
fi

%files
%doc LICENSE katello.fc katello.if katello.te
%attr(0600,root,root) %{_datadir}/selinux/*/katello.pp.bz2
%{_datadir}/selinux/devel/include/%{moduletype}/katello.if
%attr(0755,root,root) %{_sbindir}/%{name}-enable
%attr(0755,root,root) %{_sbindir}/%{name}-disable
%attr(0755,root,root) %{_sbindir}/%{name}-relabel
%{_mandir}/man8/%{name}-enable.8.gz
%{_mandir}/man8/%{name}-disable.8.gz
%{_mandir}/man8/%{name}-relabel.8.gz

%changelog
* Wed Aug 08 2018 Evgeni Golov <evgeni@golov.de> 3.0.3-2
- test

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


