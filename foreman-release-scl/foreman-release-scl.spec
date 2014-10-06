Name:     foreman-release-scl
Version:  1
Release:  1%{?dist}

Summary:  Foreman Software Collections repositories meta-package
Group:    Applications/System
License:  GPLv3+
URL:      http://theforeman.org

Requires: rhscl-ruby193-epel-%{rhel}-%{_arch}
Requires: rhscl-v8314-epel-%{rhel}-%{_arch}

%description
Software Collection repositories provide additional sets of software packages,
typically newer versions than those available in an OS distribution.

This meta-package depends on those packages that contain the Yum repository
configuration files required for Foreman.  It's designed for use on Red Hat
Enterprise Linux rebuilds, such as CentOS.

%files

%changelog
* Mon Oct 06 2014 Dominic Cleal <dcleal@redhat.com> 1-1
- new package built with tito

