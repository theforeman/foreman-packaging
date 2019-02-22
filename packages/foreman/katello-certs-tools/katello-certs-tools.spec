Name:      katello-certs-tools
Summary:   Katello SSL Key/Cert Tool
Group:     Applications/Internet
License:   GPLv2
Version:   2.4.0
Release:   1%{?dist}
URL:       https://github.com/katello/katello-certs-tools
Source0:   https://codeload.github.com/Katello/%{name}/tar.gz/%{version}
BuildArch: noarch

#BZ 1022017
Requires: openssl >= 1.0.1e-16

Requires: rpm-build

BuildRequires: docbook-utils
BuildRequires: python

%description
This package contains tools to generate the SSL certificates required by
Katello.

%prep
%setup -q

%build
/usr/bin/docbook2man katello-ssl-tool.sgml
%{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT
chmod +x $RPM_BUILD_ROOT/%{python_sitelib}/katello_certs_tools/katello_ssl_tool.py
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/pki/%{name}
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/pki/%{name}/certs
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/pki/%{name}/private

%files
%{python_sitelib}/*
%dir %{_sysconfdir}/pki/%{name}
%dir %{_sysconfdir}/pki/%{name}/certs
%dir %{_sysconfdir}/pki/%{name}/private
%attr(755,root,root) %{_bindir}/katello-sudo-ssl-tool
%attr(755,root,root) %{_bindir}/katello-ssl-tool
%attr(755,root,root) %{_bindir}/katello-certs-gen-rpm
%attr(755,root,root) %{_bindir}/katello-certs-sign
%doc %{_mandir}/man1/katello-*.1*
%license LICENSE

%changelog
* Wed Jul 29 2015 Eric D. Helms <ericdhelms@gmail.com> 2.4.0-1
- new package built with tito

* Tue Jul 07 2015 Stephen Benjamin <stbenjam@redhat.com> 2.4.0-1
- Bump to 2.4.0

* Tue Jul 07 2015 Stephen Benjamin <stbenjam@redhat.com> 2.3.0-2
- Update for Katello 2.3

* Fri Jun 12 2015 Eric D. Helms <ericdhelms@gmail.com> 2.3.0-1
- refs #10777 Use sha256 as default signing algorithm.
  (Roger.Spencer@humedica.com)

* Fri Dec 19 2014 David Davis <daviddavis@redhat.com> 2.2.0-1
-

* Fri Sep 12 2014 Justin Sherrill <jsherril@redhat.com> 2.1.0-1
- bumping version to 2.1 (jsherril@redhat.com)

* Fri Sep 12 2014 Justin Sherrill <jsherril@redhat.com> 2.0.1-1
- add minimum openssl version (jmontleo@redhat.com)

* Fri Mar 07 2014 Eric D. Helms <ericdhelms@gmail.com> 1.5.2-1
- Removing dependence on /usr/share/katello and turning into a stand alone
  katello-certs-tools package. Includes updates to support specifying the certs
  deployment directory and using a password file to specify the password for
  cert generation. (ericdhelms@gmail.com)

* Fri Oct 11 2013 Partha Aji <paji@redhat.com> 1.5.1-1
- Bumping package versions for 1.5 (paji@redhat.com)

* Wed Sep 04 2013 Ivan Necas <inecas@redhat.com> 1.4.4-1
- Support for generating client certs (inecas@redhat.com)

* Tue Sep 03 2013 Partha Aji <paji@redhat.com> 1.4.3-1
-

* Sat Apr 27 2013 Justin Sherrill <jsherril@redhat.com> 1.4.2-1
- Add 'certs-tools/' from commit '5111c76d8d4b3a88da112166d35360cd08c05f46'
  (jsherril@redhat.com)

* Fri Apr 12 2013 Justin Sherrill <jsherril@redhat.com> 1.4.1-1
- version bump to 1.4 (jsherril@redhat.com)

* Fri Apr 12 2013 Justin Sherrill <jsherril@redhat.com> 1.3.1-1
- copyright update (jsherril@redhat.com)
- remove old changelog entries (msuchy@redhat.com)

* Fri Oct 12 2012 Lukas Zapletal <lzap+git@redhat.com> 1.1.9-1
- updating copyrights

* Sat Aug 11 2012 Miroslav Suchý <msuchy@redhat.com> 1.1.8-1
- various pylint cleaning
- there is no Python license in cert-tools (msuchy@redhat.com)
- buildroot and %%clean section is not needed (msuchy@redhat.com)

* Tue Jul 31 2012 Miroslav Suchý <msuchy@redhat.com> 1.1.7-1
- update copyright years (msuchy@redhat.com)
- %%defattr is not needed since rpm 4.4 (msuchy@redhat.com)

* Thu May 10 2012 Lukas Zapletal <lzap+git@redhat.com> 1.1.6-1
- 818261 - consumer rpm was not installable on RHEL5

* Thu Mar 22 2012 Mike McCune <mmccune@redhat.com> 1.1.5-1
- 781210 - remove from specfile a txt file that was removed in dcdde7a876
  (mmccune@redhat.com)

* Tue Mar 20 2012 Lukas Zapletal <lzap+git@redhat.com> 1.1.4-1
- 781210 - cert tools man page review

* Tue Mar 06 2012 Mike McCune <mmccune@redhat.com> 1.1.3-1
- 800093 - CRL was non functional without these config options
  (jmatthew@redhat.com)
- 788708 - removing legacy bootstrap script and generator (lzap+git@redhat.com)
