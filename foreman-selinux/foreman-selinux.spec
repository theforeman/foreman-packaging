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
%define selinux_modules foreman foreman-proxy

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

Name:           foreman-selinux
Version:        1.8.0
Release:        0.develop%{?dotalphatag}%{?dist}
Summary:        SELinux policy module for Foreman

Group:          System Environment/Base
License:        GPLv3+
URL:            http://www.theforeman.org
Source0:        http://downloads.theforeman.org/%{name}/%{name}-%{version}%{?dashalphatag}.tar.bz2

BuildRequires:  checkpolicy, selinux-policy-devel, hardlink, /usr/sbin/semodule
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
# list available modules (if this fails, we are missing base policy in the buildroot)
semodule -l

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
%doc Contributors CHANGELOG LICENSE foreman.fc foreman.if foreman.te foreman.sh
%attr(0600,root,root) %{_datadir}/selinux/*/foreman.pp.bz2
%{_datadir}/selinux/devel/include/%{moduletype}/foreman.if
%attr(0755,root,root) %{_sbindir}/%{name}-enable
%attr(0755,root,root) %{_sbindir}/%{name}-disable
%attr(0755,root,root) %{_sbindir}/%{name}-relabel
%{_mandir}/man8/%{name}-enable.8.gz
%{_mandir}/man8/%{name}-disable.8.gz
%{_mandir}/man8/%{name}-relabel.8.gz

%package -n foreman-proxy-selinux
Summary: SELinux policy module for Foreman Proxy
Group:   System Environment/Base

Requires:           selinux-policy >= %{selinux_policy_ver}
Requires(post):     /usr/sbin/semodule, /sbin/restorecon, /usr/sbin/setsebool, /usr/sbin/selinuxenabled, /usr/sbin/semanage
Requires(post):     policycoreutils-python
Requires(post):     selinux-policy-targeted
Requires(postun):   /usr/sbin/semodule, /sbin/restorecon

%description -n foreman-proxy-selinux
SELinux policy module for Foreman Proxy

%post -n foreman-proxy-selinux
if /usr/sbin/selinuxenabled; then
    # install and upgrade
    %{_sbindir}/foreman-proxy-selinux-enable
fi

%posttrans -n foreman-proxy-selinux
if /usr/sbin/selinuxenabled; then
    # install and upgrade
    %{_sbindir}/foreman-proxy-selinux-relabel
fi

%preun -n foreman-proxy-selinux
if /usr/sbin/selinuxenabled; then
    # uninstall only
    if [ $1 -eq 0 ]; then
        %{_sbindir}/foreman-proxy-selinux-disable
    fi
    # upgrade and uninstall
    %{_sbindir}/foreman-proxy-selinux-relabel
fi

%files -n foreman-proxy-selinux
%doc Contributors CHANGELOG LICENSE
%doc foreman-proxy.fc foreman-proxy.if foreman-proxy.te
%attr(0600,root,root) %{_datadir}/selinux/*/foreman-proxy.pp.bz2
%{_datadir}/selinux/devel/include/%{moduletype}/foreman-proxy.if
%attr(0755,root,root) %{_sbindir}/foreman-proxy-selinux-enable
%attr(0755,root,root) %{_sbindir}/foreman-proxy-selinux-disable
%attr(0755,root,root) %{_sbindir}/foreman-proxy-selinux-relabel
%{_mandir}/man8/foreman-proxy-selinux-enable.8.gz
%{_mandir}/man8/foreman-proxy-selinux-disable.8.gz
%{_mandir}/man8/foreman-proxy-selinux-relabel.8.gz

%changelog
* Tue Oct 28 2014 Dominic Cleal <dcleal@redhat.com> - 1.8.0-0.develop
- Bump version to 1.8-develop

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
