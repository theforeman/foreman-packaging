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
%global selinux_policy_ver %(rpm --qf "%%{version}-%%{release}" -q selinux-policy)

%define moduletype apps

%global release 3
%global prerelease RC1

Name:           foreman-selinux
Version:        1.20.0
Release:        %{?prerelease:0.}%{release}%{?prerelease:.}%{?prerelease}%{?dist}
Summary:        SELinux policy module for Foreman

Group:          System Environment/Base
License:        GPLv3+
URL:            https://theforeman.org
Source0:        https://downloads.theforeman.org/%{name}/%{name}-%{version}%{?prerelease:-}%{?prerelease}.tar.bz2

BuildRequires:  checkpolicy, selinux-policy-devel, hardlink
BuildRequires:  policycoreutils
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
%setup -q -n %{name}-%{version}%{?prerelease:-}%{?prerelease}

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
%doc Contributors CHANGELOG foreman.fc foreman.if foreman.te foreman.sh
%license LICENSE
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
%doc Contributors CHANGELOG
%license LICENSE
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
* Fri Oct 19 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.20.0-0.3.RC1
- Release 1.20.0-RC1

* Wed Sep 05 2018 Lukas Zapletal <lzap+rpm@redhat.com> 1.20.0-0.2.develop
- Updated selinux_policy_ver macro

* Wed Jul 25 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.20.0-0.1.develop
- Add prerelease macro

* Tue Jul 17 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.20.0-0.develop
- Bump version to 1.20-develop

* Thu May 31 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.19.0-0.develop
- Bump version to 1.19-develop

* Mon Aug 28 2017 Daniel Lobato Garcia <me@daniellobato.me> - 1.17.0-0.develop
- Bump version to 1.17-develop

* Wed Mar 29 2017 Eric D Helms <ericdhelms@gmail.com> - 1.16.0-0.develop
- Bump version to 1.16-develop

* Tue Dec 06 2016 Dominic Cleal <dominic@cleal.org> - 1.15.0-0.develop
- Bump version to 1.15-develop

* Wed Sep 07 2016 Dominic Cleal <dominic@cleal.org> - 1.14.0-0.develop
- Bump version to 1.14-develop

* Tue May 31 2016 Dominic Cleal <dominic@cleal.org> - 1.13.0-0.develop
- Bump version to 1.13-develop

* Fri Feb 19 2016 Dominic Cleal <dominic@cleal.org> - 1.12.0-0.develop
- Bump version to 1.12-develop

* Wed Oct 07 2015 Dominic Cleal <dcleal@redhat.com> - 1.11.0-0.develop
- Bump version to 1.11-develop

* Fri Jun 26 2015 Dominic Cleal <dcleal@redhat.com> - 1.10.0-0.develop
- Bump version to 1.10-develop

* Tue Mar 03 2015 Dominic Cleal <dcleal@redhat.com> - 1.9.0-0.develop
- Bump version to 1.9-develop

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
