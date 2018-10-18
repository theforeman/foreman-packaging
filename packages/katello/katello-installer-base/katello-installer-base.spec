# Not building for scl right now
%undefine scl_prefix
%global scl_ruby /usr/bin/ruby

%global prerelease .rc1
%global release 2

Name:    katello-installer-base
Version: 3.9.0
Release: %{?prerelease:0.}%{release}%{?prerelease}%{?dist}
Summary: Puppet-based installer for the Katello and Katello Capsule
Group:   Applications/System
License: GPLv3+ and ASL 2.0
URL:     https://theforeman.org/plugins/katello
Source0: https://fedorapeople.org/groups/katello/releases/source/tarball/katello-installer-%{version}%{?prerelease}.tar.gz

BuildArch: noarch
Obsoletes: katello-installer < 2.1.0

Requires: foreman-installer >= 1.17.0
Requires: %{?scl_prefix}puppet >= 4.0.0
Requires: katello-selinux
Requires: openssl
Requires: katello-certs-tools
Requires: foreman-proxy
Requires: /bin/readlink

%package -n foreman-installer-katello
Summary: Foreman-installer scenarios for Katello and Foreman proxies with content
Group:	 Applications/System
Obsoletes: katello-installer
Obsoletes: capsule-installer
Requires: %{name} = %{version}-%{release}
Requires: katello-service >= 3.0.0

%description -n foreman-installer-katello
A set of tools for installation of Katello and Foreman proxies with content

%posttrans -n foreman-installer-katello
# See if the currently selected scenario is capsule - and migrate it to be foreman-proxy-content
if [[ "`/bin/readlink -f /etc/foreman-installer/scenarios.d/last_scenario.yaml`" == "/etc/foreman-installer/scenarios.d/capsule.yaml" ]];
then
  mv /etc/foreman-installer/scenarios.d/capsule-answers.yaml /etc/foreman-installer/scenarios.d/foreman-proxy-content-answers.yaml
  ln -snf /etc/foreman-installer/scenarios.d/foreman-proxy-content.yaml /etc/foreman-installer/scenarios.d/last_scenario.yaml
fi

foreman-installer --scenario katello --migrations-only > /dev/null
foreman-installer --scenario foreman-proxy-content --migrations-only > /dev/null

%files -n foreman-installer-katello
%{_datadir}/foreman-installer-katello/bin
%config(noreplace) %attr(600, root, root) %{_sysconfdir}/foreman-installer/scenarios.d/katello-answers.yaml
%config(noreplace) %attr(600, root, root) %{_sysconfdir}/foreman-installer/scenarios.d/katello.yaml
%config(noreplace) %attr(600, root, root) %{_sysconfdir}/foreman-installer/scenarios.d/foreman-proxy-content-answers.yaml
%config(noreplace) %attr(600, root, root) %{_sysconfdir}/foreman-installer/scenarios.d/foreman-proxy-content.yaml
%dir %{_sysconfdir}/foreman-installer/scenarios.d/katello.migrations
%{_sysconfdir}/foreman-installer/scenarios.d/katello.migrations
%dir %{_sysconfdir}/foreman-installer/scenarios.d/foreman-proxy-content.migrations
%{_sysconfdir}/foreman-installer/scenarios.d/foreman-proxy-content.migrations
%{_sbindir}/foreman-proxy-certs-generate
%{_sbindir}/katello-certs-check

%description
A set of tools for installation of Katello and Katello Capsule,
including Foreman and Foreman Proxy.

%prep
%setup -q -n katello-installer-%{version}%{?prerelease}

%build
#replace shebangs
sed -ri '1sX(/usr/bin/ruby|/usr/bin/env ruby)X%{scl_ruby}X' bin/*

#configure the paths
sed -ri 'sX\./configX%{_sysconfdir}/foreman-installer/scenarios.dXg' config/katello-answers.yaml config/katello.yaml bin/foreman-proxy-certs-generate
sed -ri 'sX\./configX%{_sysconfdir}/foreman-installer/scenarios.dXg' config/foreman-proxy-content.yaml

sed -ri 'sX  INSTALLER_DIR.*$X  INSTALLER_DIR = "%{_datadir}/katello-installer-base"Xg' bin/foreman-proxy-certs-generate
sed -ri 'sX\:installer_dir.*$X:installer_dir: %{_datadir}/katello-installer-baseXg' config/*.yaml

# module paths
sed -ri 'sX./_build/modulesX%{_datadir}/foreman-installer/modulesXg' config/*.yaml
sed -ri 'sX../katello-installer/modulesX%{_datadir}/katello-installer-base/modulesXg' config/*.yaml

#hooks
sed -i -e 'sX../katello-installer/hooksX%{_datadir}/katello-installer-base/hooksXg' config/*.yaml

%install
install -d -m0755 %{buildroot}%{_sysconfdir}/foreman-installer/scenarios.d

install -d -m0755 %{buildroot}/%{_datadir}/katello-installer-base
install -d -m0755 %{buildroot}/%{_datadir}/foreman-installer-katello/bin

install -d -m0755 %{buildroot}/%{_sbindir}

cp -dpR checks modules hooks parser_cache %{buildroot}/%{_datadir}/katello-installer-base

cp -dpR bin/foreman-proxy-certs-generate %{buildroot}/%{_datadir}/foreman-installer-katello/bin/foreman-proxy-certs-generate
cp -dpR bin/katello-certs-check %{buildroot}/%{_datadir}/foreman-installer-katello/bin/katello-certs-check

cp -dpR config/katello-answers.yaml %{buildroot}/%{_sysconfdir}/foreman-installer/scenarios.d
cp -dpR config/foreman-proxy-content-answers.yaml %{buildroot}/%{_sysconfdir}/foreman-installer/scenarios.d

cp -dpR config/katello.yaml %{buildroot}/%{_sysconfdir}/foreman-installer/scenarios.d
cp -dpR config/katello.migrations %{buildroot}/%{_sysconfdir}/foreman-installer/scenarios.d
cp -dpR config/foreman-proxy-content.yaml %{buildroot}/%{_sysconfdir}/foreman-installer/scenarios.d
cp -dpR config/foreman-proxy-content.migrations %{buildroot}/%{_sysconfdir}/foreman-installer/scenarios.d

ln -sf %{_datadir}/foreman-installer-katello/bin/foreman-proxy-certs-generate %{buildroot}/%{_sbindir}/foreman-proxy-certs-generate
ln -sf %{_datadir}/foreman-installer-katello/bin/katello-certs-check %{buildroot}/%{_sbindir}/katello-certs-check

%files
%defattr(-,root,root,-)
%{_datadir}/katello-installer-base/modules
%{_datadir}/katello-installer-base/hooks
%{_datadir}/katello-installer-base/checks
%{_datadir}/katello-installer-base/parser_cache
%doc README.*

%changelog
* Thu Oct 18 2018 Eric D. Helms <ericdhelms@gmail.com> - 3.9.0-0.2.rc1
- Release RC1

* Tue Jul 24 2018 Eric D. Helms <ericdhelms@gmail.com> 3.9.0-2
- Add prerelease macro support

* Wed Jul 18 2018 Eric D. Helms <ericdhelms@gmail.com> 3.9.0-1.nightly
- Bump to 3.9

