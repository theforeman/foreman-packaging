Name:     foreman-release-scl
Version:  7
Release:  1%{?dist}

Summary:  Foreman Software Collections repositories meta-package
Group:    Applications/System
License:  GPLv3+
URL:      https://theforeman.org

BuildArch: noarch

Requires: centos-release-scl

%description
Software Collection repositories provide additional sets of software packages,
typically newer versions than those available in an OS distribution.

This meta-package depends on those packages that contain the Yum repository
configuration files required for Foreman.  It's designed for use on Red Hat
Enterprise Linux rebuilds, such as CentOS.

%prep

%build

%install

%files

%changelog
* Wed Aug 01 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 7-1
- Move the foreman-rails repository definition from foreman-release-scl to foreman-release

* Wed Jul 18 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 6-1
- Add GPG key
- Bump version for the new release cycle

* Tue Jul 17 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 5-2
- Point to 1.19 repositories

* Tue May 29 2018 Eric D. Helms <ericdhelms@gmail.com> 5-1
- Move to using yum.theforeman.org for tfm-ror51 (ericdhelms@gmail.com)

* Fri Jan 05 2018 Eric D. Helms <ericdhelms@gmail.com> 4-1
- Add tfm-ror51 repo to foreman-release-scl (ericdhelms@gmail.com)

* Tue Apr 05 2016 Dominic Cleal <dominic@cleal.org> 3-1
- Switch to CentOS SCLo SIG builds (#12912, dominic@cleal.org)

* Wed Jan 06 2016 Dominic Cleal <dcleal@redhat.com> 2-1
- Depend on ror41 and ruby22 collections (dcleal@redhat.com)

* Mon Oct 06 2014 Dominic Cleal <dcleal@redhat.com> 1-1
- new package built with tito
