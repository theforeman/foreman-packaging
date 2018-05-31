Name:     foreman-release-scl
Version:  4
Release:  2%{?dist}

Summary:  Foreman Software Collections repositories meta-package
Group:    Applications/System
License:  GPLv3+
URL:      http://theforeman.org
Source0:  tfm-ror51.repo

BuildArch: noarch

Requires: centos-release-scl

%description
Software Collection repositories provide additional sets of software packages,
typically newer versions than those available in an OS distribution.

This meta-package depends on those packages that contain the Yum repository
configuration files required for Foreman.  It's designed for use on Red Hat
Enterprise Linux rebuilds, such as CentOS.

%install
install -d -m 0755 %{buildroot}%{_sysconfdir}/yum.repos.d

install -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/

%files
%config %{_sysconfdir}/yum.repos.d/*.repo

%changelog
* Thu May 31 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 4-2
- Point to yum.theforeman.org for tfm-ror51

* Fri Jan 05 2018 Eric D. Helms <ericdhelms@gmail.com> 4-1
- Add tfm-ror51 repo to foreman-release-scl (ericdhelms@gmail.com)

* Tue Apr 05 2016 Dominic Cleal <dominic@cleal.org> 3-1
- Switch to CentOS SCLo SIG builds (#12912, dominic@cleal.org)

* Wed Jan 06 2016 Dominic Cleal <dcleal@redhat.com> 2-1
- Depend on ror41 and ruby22 collections (dcleal@redhat.com)

* Mon Oct 06 2014 Dominic Cleal <dcleal@redhat.com> 1-1
- new package built with tito

