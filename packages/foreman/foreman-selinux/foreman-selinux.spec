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

%define moduletype apps

%global release 1
%global prereleasesource develop
%global prerelease %{?prereleasesource}

Name:           foreman-selinux
Version:        3.16.0
Release:        %{?prerelease:0.}%{release}%{?prerelease:.}%{?prerelease}%{?nightly}%{?dist}
Summary:        SELinux policy module for Foreman

Group:          System Environment/Base
License:        GPLv3+
URL:            https://theforeman.org
Source0:        https://downloads.theforeman.org/%{name}/%{name}-%{version}%{?prerelease:-}%{?prerelease}.tar.bz2

BuildRequires:  checkpolicy
BuildRequires:  selinux-policy-devel
BuildRequires:  hardlink
BuildRequires:  policycoreutils
BuildRequires:  /usr/bin/pod2man
BuildRequires:  systemd
BuildArch:      noarch

Requires:           selinux-policy >= %{_selinux_policy_version}
Requires(post):     /usr/sbin/semodule
Requires(post):     /sbin/restorecon
Requires(post):     /usr/sbin/setsebool
Requires(post):     /usr/sbin/selinuxenabled
Requires(post):     /usr/sbin/semanage
Requires(post):     selinux-policy-targeted
Requires(postun):   /usr/sbin/semodule
Requires(postun):   /sbin/restorecon
%{?systemd_requires}

Requires(post):     policycoreutils-python-utils

%description
SELinux policy module for Foreman

%prep
%setup -q -n %{name}-%{version}%{?prerelease:-}%{?prerelease}

%build
# build policy
for selinuxvariant in %{selinux_variants}; do
    make clean all NAME=${selinuxvariant} VERSION=%{version} INSTPREFIX=%{buildroot}
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
make clean install-data NAME=${selinuxvariant} VERSION=%{version} INSTPREFIX=%{buildroot}

%post
# install and upgrade
%{_sbindir}/%{name}-enable
systemctl daemon-reexec &>/dev/null || :

%posttrans
if /usr/sbin/selinuxenabled; then
    # install and upgrade
    %{_sbindir}/%{name}-relabel
fi

%preun
# uninstall only
if [ $1 -eq 0 ]; then
    %{_sbindir}/%{name}-disable
    systemctl daemon-reexec &>/dev/null || :
fi

# upgrade and uninstall
if /usr/sbin/selinuxenabled; then
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

Requires:           selinux-policy >= %{_selinux_policy_version}
Requires(post):     /usr/sbin/semodule
Requires(post):     /sbin/restorecon
Requires(post):     /usr/sbin/setsebool
Requires(post):     /usr/sbin/selinuxenabled
Requires(post):     /usr/sbin/semanage
Requires(post):     selinux-policy-targeted
Requires(postun):   /usr/sbin/semodule
Requires(postun):   /sbin/restorecon

Requires(post):     policycoreutils-python-utils

%description -n foreman-proxy-selinux
SELinux policy module for Foreman Proxy

%post -n foreman-proxy-selinux
# install and upgrade
%{_sbindir}/foreman-proxy-selinux-enable

%posttrans -n foreman-proxy-selinux
if /usr/sbin/selinuxenabled; then
    # install and upgrade
    %{_sbindir}/foreman-proxy-selinux-relabel
fi

%preun -n foreman-proxy-selinux
# uninstall only
if [ $1 -eq 0 ]; then
    %{_sbindir}/foreman-proxy-selinux-disable
fi

# upgrade and uninstall
if /usr/sbin/selinuxenabled; then
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

* Wed Nov 29 2023 Zach Huntington-Meath <zhunting@redhat.com> - 3.10.0-0.1.develop
- Bump version to 3.10-develop

* Wed Aug 23 2023 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 3.9.0-0.1.develop
- Bump version to 3.9-develop

* Tue May 23 2023 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 3.8.0-0.1.develop
- Bump version to 3.8-develop

* Wed Mar 01 2023 Evgeni Golov - 3.7.0-0.2.develop
- Drop RHEL7 dependencies and Fedora support

* Wed Feb 22 2023 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 3.7.0-0.1.develop
- Bump version to 3.7-develop

* Wed Dec 07 2022 Evgeni Golov - 3.6.0-0.2.develop
- Use _selinux_policy_version macro from selinux-policy package

* Tue Nov 08 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 3.6.0-0.1.develop
- Bump version to 3.6-develop

* Wed Aug 10 2022 Patrick Creech <pcreech@redhat.com> - 3.5.0-0.1.develop
- Bump version to 3.5-develop

* Tue Jul 12 2022 Evgeni Golov - 3.4.0-0.2.develop
- Fixes #35198 - always load SELinux definitions

* Tue May 10 2022 Odilon Sousa <osousa@redhat.com> - 3.4.0-0.1.develop
- Bump version to 3.4-develop

* Thu Feb 10 2022 Zach Huntington-Meath <zhunting@redhat.com> - 3.3.0-0.1.develop
- Bump version to 3.3-develop

* Fri Nov 12 2021 Odilon Sousa <osousa@redhat.com> - 3.2.0-0.1.develop
- Bump version to 3.2-develop

* Thu Aug 05 2021 Patrick Creech <pcreech@redhat.com> - 3.1.0-0.1.develop
- Bump version to 3.1-develop

* Thu Jul 22 2021 Tomer Brisker <tbrisker@gmail.com> - 3.0.0-0.1.develop
- Bump version to 3.0-develop

* Tue May 04 2021 Zach Huntington-Meath <zhunting@redhat.com> - 2.6.0-0.1.develop
- Bump version to 2.6-develop

* Tue Feb 02 2021 Evgeni Golov - 2.5.0-0.1.develop
- Bump version to 2.5-develop

* Fri Nov 27 2020 Evgeni Golov - 2.4.0-0.2.develop
- reexec systemd after policy changes to make socket labeling work

* Mon Nov 02 2020 Patrick Creech <pcreech@redhat.com> - 2.4.0-0.1.develop
- Bump version to 2.4-develop

* Tue Aug 11 2020 Eric D. Helms <ericdhelms@gmail.com> - 2.3.0-0.1.develop
- Bump version to 2.3-develop

* Wed May 13 2020 Eric D. Helms <ericdhelms@gmail.com> - 2.2.0-0.2.develop
- Bump version to 2.2-develop

* Tue Apr 07 2020 Eric D. Helms <ericdhelms@gmail.com> - 2.1.0-0.2.develop
- Update spec and build for EL8

* Thu Feb 13 2020 Tomer Brisker <tbrisker@gmail.com> - 2.1.0-0.1.develop
- Bump version to 2.1-develop

* Mon Jan 06 2020 Tomer Brisker <tbrisker@gmail.com> - 2.0.0-0.1.develop
- Bump version to 2.0-develop

* Mon Nov 18 2019 Evgeni Golov - 1.25.0-0.2.develop
- Unify prerelease macro handling

* Wed Oct 30 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.25.0-0.1.develop
- Bump version to 1.25-develop

* Tue Jul 30 2019 Evgeni Golov - 1.24.0-0.1.develop
- Bump version to 1.24-develop

* Tue Apr 23 2019 Evgeni Golov <evgeni@golov.de> - 1.23.0-0.1.develop
- Bump version to 1.23-develop

* Wed Jan 16 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.22.0-0.1.develop
- Bump to 1.22

* Wed Oct 24 2018 Adam Price <komidore64@gmail.com> - 1.21.0-0.2.develop
- add nightly macro

* Wed Oct 17 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.21.0-0.1.develop
- Bump version to 1.21 and reset release

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
