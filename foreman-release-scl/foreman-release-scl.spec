Name:     foreman-release-scl
Version:  2
Release:  1%{?dist}

Summary:  Foreman Software Collections repositories meta-package
Group:    Applications/System
License:  GPLv3+
URL:      http://theforeman.org

BuildArch: noarch

Requires: centos-release-scl

%description
Software Collection repositories provide additional sets of software packages,
typically newer versions than those available in an OS distribution.

This meta-package depends on those packages that contain the Yum repository
configuration files required for Foreman.  It's designed for use on Red Hat
Enterprise Linux rebuilds, such as CentOS.

%files

%changelog
* Wed Jan 06 2016 Dominic Cleal <dcleal@redhat.com> 2-1
- Depend on ror41 and ruby22 collections (dcleal@redhat.com)

* Mon Oct 06 2014 Dominic Cleal <dcleal@redhat.com> 1-1
- new package built with tito

