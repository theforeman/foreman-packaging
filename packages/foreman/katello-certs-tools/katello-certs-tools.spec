Name:      katello-certs-tools
Summary:   Katello SSL Key/Cert Tool
Group:     Applications/Internet
License:   GPLv2
Version:   2.8.0
Release:   1%{?dist}
URL:       https://github.com/katello/katello-certs-tools
Source0:   https://codeload.github.com/Katello/%{name}/tar.gz/%{version}#/%{name}-%{version}.tar.gz
BuildArch: noarch

Requires: openssl
Requires: rpm-build

BuildRequires: docbook-utils
%if 0%{?rhel} == 7
BuildRequires: python-devel >= 2.6
BuildRequires: python-setuptools
Requires: python-setuptools
%else
BuildRequires: python3-devel
BuildRequires: python3-setuptools
%endif

%description
This package contains tools to generate the SSL certificates required by
Katello.

%prep
%setup -q

%build
/usr/bin/docbook2man katello-ssl-tool.sgml
%if 0%{?rhel} == 7
%{py2_build}
%else
%{py3_build}
%endif

%install
%if 0%{?rhel} == 7
%{__python2} setup.py install --skip-build --root $RPM_BUILD_ROOT
%else
%{__python3} setup.py install --skip-build --root $RPM_BUILD_ROOT
%endif
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/pki/%{name}
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/pki/%{name}/certs
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/pki/%{name}/private

%files
%if 0%{?rhel} == 7
%{python2_sitelib}/katello_certs_tools
%{python2_sitelib}/*.egg-info
%else
%{python3_sitelib}/katello_certs_tools
%{python3_sitelib}/*.egg-info
%endif
%dir %{_sysconfdir}/pki/%{name}
%dir %{_sysconfdir}/pki/%{name}/certs
%dir %{_sysconfdir}/pki/%{name}/private
%attr(755,root,root) %{_bindir}/katello-ssl-tool
%attr(755,root,root) %{_bindir}/katello-certs-gen-rpm
%attr(755,root,root) %{_bindir}/katello-certs-sign
%doc %{_mandir}/man1/katello-*.1*
%license LICENSE

%changelog
* Fri Jun 04 2021 Eric D. Helms <ericdhelms@gmail.com> - 2.8.0-1
- Release katello-certs-tools 2.8.0

* Fri Sep 11 2020 Eric D. Helms <ericdhelms@gmail.com> - 2.7.3-1
- Release katello-certs-tools 2.7.3

* Fri Sep 11 2020 Eric D. Helms <ericdhelms@gmail.com> - 2.7.2-1
- Release katello-certs-tools 2.7.2

* Mon Jun 22 2020 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.7.1-2
- Require python-setuptools on EL7

* Tue Jun 09 2020 Eric D. Helms <ericdhelms@gmail.com> - 2.7.1-1
- Release katello-certs-tools 2.7.1

* Tue May 12 2020 Eric D. Helms <ericdhelms@gmail.com> - 2.7.0-1
- Release katello-certs-tools 2.7.0

* Wed Apr 22 2020 Eric D. Helms <ericdhelms@gmail.com> - 2.6.1-1
- Release katello-certs-tools 2.6.1

* Tue Apr 07 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.6.0-3
- Bump to release for EL8

* Tue Mar 31 2020 Eric D. Helms <ericdhelms@gmail.com> - 2.6.0-2
- Rebuild for EL8

* Fri Sep 13 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 2.6.0-1
- Update to 2.6.0

* Tue Mar 05 2019 Eric D. Helms <ericdhelms@gmail.com> - 2.5.3-1
- Release katello-certs-tools 2.5.3

* Fri Mar 01 2019 Eric D. Helms <ericdhelms@gmail.com> - 2.5.2-1
- Release katello-certs-tools 2.5.2

* Thu Feb 28 2019 Evgeni Golov - 2.5.1-1
- Release 2.5.1
- Fixes #26188 - don't duplicate -s in the python shebang

* Wed Feb 27 2019 Eric D. Helms <ericdhelms@gmail.com> - 2.5.0-1
- Release 2.5.0 with python3 support

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
