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

%if 0%{?rhel} == 5
# absolute minimum versions for RHEL 5
%define selinux_policy_ver 3.11.1-81
%else
# absolute minimum versions for RHEL 6
%define selinux_policy_ver 2.4.6-80
%endif
%define selinux_policycoreutils_ver 1.33.12-1

%define moduletype apps
%define modulename foreman

# set and uncomment all three to set alpha tag
#global alphatag RC2
#global dotalphatag .%{alphatag}
#global dashalphatag -%{alphatag}

Name:           %{modulename}-selinux
Version:        1.7.1
Release:        1%{?dotalphatag}%{?dist}
Summary:        SELinux policy module for Foreman

Group:          System Environment/Base
License:        GPLv3+
URL:            http://www.theforeman.org
Source0:        http://downloads.theforeman.org/%{name}/%{name}-%{version}%{?dashalphatag}.tar.bz2

BuildRequires:  checkpolicy, selinux-policy-devel, hardlink
BuildRequires:  policycoreutils >= %{selinux_policycoreutils_ver}
BuildRequires:  /usr/bin/pod2man
BuildArch:      noarch

Requires:           selinux-policy >= %{selinux_policy_ver}
Requires(post):     /usr/sbin/semodule, /sbin/restorecon, /usr/sbin/setsebool, /usr/sbin/selinuxenabled, /usr/sbin/semanage
Requires(post):     policycoreutils-python
Requires(post):     selinux-policy-targeted
Requires(postun):   /usr/sbin/semodule, /sbin/restorecon

%description
SELinux policy module for Foreman

%prep
%setup -q -n %{name}-%{version}%{?dashalphatag}

%build
# create selinux-friendly version from VR and replace it inplace
perl -i -pe 'BEGIN { $VER = join ".", grep /^\d+$/, split /\./, "%{version}.%{release}"; } s!\@\@VERSION\@\@!$VER!g;' %{modulename}.te

# determine distribution name and version
%if 0%{?rhel} >= 6
    distver=rhel%{rhel}
%endif
%if 0%{?fedora} >= 18
    distver=fedora%{fedora}
%endif

# build policy
for selinuxvariant in %{selinux_variants}
do
    make NAME=${selinuxvariant} -f /usr/share/selinux/devel/Makefile DISTRO=${distver}
    bzip2 -9 %{modulename}.pp
    mv %{modulename}.pp.bz2 %{modulename}.ppbz2.${selinuxvariant}
    make NAME=${selinuxvariant} -f /usr/share/selinux/devel/Makefile clean DISTRO=${distver}
done

# build man pages
/usr/bin/pod2man --name=foreman-selinux-enable -c "Foreman Reference" --section=8 --release=%{version} foreman-selinux-enable.pod foreman-selinux-enable.man8
/usr/bin/pod2man --name=foreman-selinux-disable -c "Foreman Reference" --section=8 --release=%{version} foreman-selinux-disable.pod foreman-selinux-disable.man8
/usr/bin/pod2man --name=foreman-selinux-relabel -c "Foreman Reference" --section=8 --release=%{version} foreman-selinux-relabel.pod foreman-selinux-relabel.man8

%install
# install policy modules
for selinuxvariant in %{selinux_variants}
  do
    install -d %{buildroot}%{_datadir}/selinux/${selinuxvariant}
    install -p -m 644 %{modulename}.ppbz2.${selinuxvariant} \
        %{buildroot}%{_datadir}/selinux/${selinuxvariant}/%{modulename}.pp.bz2
  done

# install interfaces
install -d %{buildroot}%{_datadir}/selinux/devel/include/%{moduletype}
install -p -m 644 %{modulename}.if %{buildroot}%{_datadir}/selinux/devel/include/%{moduletype}/%{modulename}.if

# hardlink identical policy module packages together
/usr/sbin/hardlink -cv %{buildroot}%{_datadir}/selinux

# install enable/relabel scripts which will be called in %posttrans
install -d %{buildroot}%{_sbindir}
install -p -m 755 %{name}-enable %{buildroot}%{_sbindir}/%{name}-enable
install -p -m 755 %{name}-disable %{buildroot}%{_sbindir}/%{name}-disable
install -p -m 755 %{name}-relabel %{buildroot}%{_sbindir}/%{name}-relabel

# install man pages
install -d -m 0755 %{buildroot}%{_mandir}/man8
install -m 0644 foreman-selinux-enable.man8 %{buildroot}%{_mandir}/man8/foreman-selinux-enable.8
install -m 0644 foreman-selinux-disable.man8 %{buildroot}%{_mandir}/man8/foreman-selinux-disable.8
install -m 0644 foreman-selinux-relabel.man8 %{buildroot}%{_mandir}/man8/foreman-selinux-relabel.8

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
%doc Contributors CHANGELOG LICENSE %{modulename}.fc %{modulename}.if %{modulename}.te %{modulename}.sh
%attr(0600,root,root) %{_datadir}/selinux/*/%{modulename}.pp.bz2
%{_datadir}/selinux/devel/include/%{moduletype}/%{modulename}.if
%{_mandir}/man8/*
%attr(0755,root,root) %{_sbindir}/%{name}-enable
%attr(0755,root,root) %{_sbindir}/%{name}-disable
%attr(0755,root,root) %{_sbindir}/%{name}-relabel

%changelog
* Tue Dec 02 2014 Dominic Cleal <dcleal@redhat.com> 1.7.0-1
- Release 1.7.0

* Tue Nov 25 2014 Dominic Cleal <dcleal@redhat.com> 1.7.0-0.2.RC2
- Release 1.7.0-RC2

* Tue Nov 11 2014 Dominic Cleal <dcleal@redhat.com> 1.7.0-0.1.RC1
- Release 1.7.0-RC1

* Mon Aug 11 2014 Dominic Cleal <dcleal@redhat.com> - 1.7.0-0.develop
- Bump version to 1.7-develop

* Wed Apr 16 2014 Dominic Cleal <dcleal@redhat.com> - 1.6.0-0.develop
- Bump to version 1.6-develop

* Thu Jan 16 2014 Dominic Cleal <dcleal@redhat.com> - 1.5.0-0.develop
- Bump to version 1.5-develop

* Thu Nov 21 2013 Dominic Cleal <dcleal@redhat.com> - 1.4.0-0.develop
- Bump and change versioning scheme (#3712)

* Thu Sep 05 2013 Lukas Zapletal <lzap+rpm[@]redhat.com> - 1.3.9999-1
- Bump to version 1.3-develop

* Mon Jun 03 2013 Lukas Zapletal <lzap+rpm[@]redhat.com> - 1.2.9999-1
- Brand new SPEC adopted from Katello project
- Changes to the policy to get SCL working

* Tue Feb 26 2013 Sam Kottler <shk@redhat.com> 1.1.1-1
- Initial version
