%define relabel_files() \
restorecon -R /usr/share/foreman/; \
restorecon -R /etc/foreman; \
restorecon -R /var/lib/foreman; \
restorecon /etc/logrotate.d/foreman; \

%define selinux_policyver 3.11.1-81

Name:   foreman-selinux
Version:	1.1
Release:	3%{?dist}
Summary:	SELinux policy module for foreman

Group:	System Environment/Base
License:	GPLv3+
URL:		http://theforeman.org
Source0:	foreman.pp
Source1:	foreman.if
Source2:	httpd_foreman_script_selinux.8

Requires: policycoreutils, libselinux-utils
Requires(post): selinux-policy-base >= %{selinux_policyver}, policycoreutils
Requires(postun): policycoreutils
BuildArch: noarch

%description
This package installs and sets up the SELinux policy security module for foreman.

%install
install -d %{buildroot}%{_datadir}/selinux/packages
install -m 644 %{SOURCE0} %{buildroot}%{_datadir}/selinux/packages
install -d %{buildroot}%{_datadir}/selinux/devel/include/contrib
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/selinux/devel/include/contrib/
install -d %{buildroot}%{_mandir}/man8/
install -m 644 %{SOURCE2} %{buildroot}%{_mandir}/man8/

%post
semodule -n -i %{_datadir}/selinux/packages/foreman.pp
if /usr/sbin/selinuxenabled ; then
    /usr/sbin/load_policy
    %relabel_files
fi;
exit 0

%posttrans
if [ $1 -eq 0 ]; then
    semodule -n -r foreman
    if /usr/sbin/selinuxenabled ; then
       /usr/sbin/load_policy
       %relabel_files
    fi;
fi;
exit 0

%files
%attr(0600,root,root) %{_datadir}/selinux/packages/foreman.pp
%{_datadir}/selinux/devel/include/contrib/foreman.if
%{_mandir}/man8/httpd_foreman_script_selinux.8.*

%changelog
* Tue Feb 26 2013 Sam Kottler <shk@redhat.com> 1.1.1-3
- Initial version
