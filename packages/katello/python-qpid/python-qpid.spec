Name:           python-qpid
Version:        1.37.0
Release:        1%{?dist}
Summary:        Python client library for AMQP

License:        ASL 2.0
URL:            http://qpid.apache.org
Source0:        https://downloads.apache.org/qpid/python/1.37.0/qpid-python-%{version}.tar.gz
#Patch0:         mrg.patch
BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
#BuildRequires:  epydoc

%description
The Apache Qpid Python client library for AMQP.


%package -n python2-qpid
Summary:   The Apache Qpid Python client library for AMQP
Obsoletes: python-qpid-common
Requires:  python2-saslwrapper
Requires:  python2

%description -n python2-qpid
The Apache Qpid Python client library for AMQP

%files -n python2-qpid
%defattr(-,root,root,-)
%doc LICENSE.txt
%doc NOTICE.txt README.md examples
%dir %{python2_sitelib}/qpid
%{python2_sitelib}/qpid/messaging/
%{python2_sitelib}/qpid/saslmech/
%{python2_sitelib}/mllib
%{python2_sitelib}/qpid/*.py*
%{python2_sitelib}/qpid/specs
%{python2_sitelib}/qpid/tests
%{python2_sitelib}/qpid_python-*.egg-info
%{_bindir}/qpid-python-test


%package -n qpid-tests
Summary:   Conformance tests for Apache Qpid
Requires:  python2-qpid >= 1.37.0
Requires:  python2-qpid-qmf >= 1.39.0

%description -n qpid-tests
Conformance tests for Apache Qpid.

%files -n qpid-tests
%defattr(-,root,root,-)
%{python2_sitelib}/qpid_tests/
%doc NOTICE.txt
%license LICENSE.txt
%{python2_sitelib}/qpid_python-*.egg-info


%prep
%setup -q -n qpid-python-%{version}
#%patch0 -p1


%build
RHEL_ALLOW_PYTHON2_FOR_BUILD=1
CFLAGS="$RPM_OPT_FLAGS" %{__python2} setup.py build


%install
RHEL_ALLOW_PYTHON2_FOR_BUILD=1
rm -rf %{buildroot}

%{__python2} setup.py install \
    --install-purelib %{python2_sitelib} \
    --root %{buildroot}

rm -f %{buildroot}/%{_bindir}/qpid-python-test.bat

%clean
rm -rf %{buildroot}


%changelog
* Tue Nov 20 2018 Irina Boverman <iboverma@redhat.com> - 1.37.0-1
- Rebased to 1.37.0
- Initial build for RHEL 8

* Wed Aug 9 2017 Mike Cressman <mcressma@redhat.com> - 1.35.0-5
- Resolved: BZ 1377195 (QPID-7884) - refine the hanging thread fix

* Wed Apr 5 2017 Mike Cressman <mcressma@redhat.com> - 1.35.0-4
- Resolved: BZ 1377195 (QPID-7317) - pulp deadlock, hanging thread
- Added qpid-tests package
- Rebased to 1.35.0

* Fri Jan 6 2017 Mike Cressman <mcressma@redhat.com> - 0.34-3
- Resolved: QPID-7053, adding a callback for asynchronous errors

* Fri Sep 11 2015 Irina Boverman <iboverma@redhat.com> - 0.34-2
- Resolved: 1249608

* Thu Jul  2 2015 Irina Boverman <iboverma@redhat.com> - 0.34-1
- Rebased to 0.34 upstream

* Fri May 29 2015 Irina Boverman <iboverma@redhat.com> - 0.32-2
- Resolved: 1201334

* Thu Apr 16 2015 Irina Boverman <iboverma@redhat.com> - 0.32-1
- Rebased to 0.32 upstream

* Wed Mar 18 2015 Irina Boverman <iboverma@redhat.com> - 0.30-6
- Resolved: 1178829

* Wed Feb  4 2015 Irina Boverman <iboverma@redhat.com> - 0.30-5
- Resolved: 1086816

* Wed Jan 14 2015 Irina Boverman <iboverma@redhat.com> - 0.30-3
- Resolved: 1095849
- Changed python-saslwrapper >= 0.22
- Initial build for qpid 0.30

* Fri Aug 29 2014 Irina Boverman <iboverma@redhat.com> - 0.22-18
- Resolved: 1128051

* Fri Aug  1 2014 Irina Boverman <iboverma@redhat.com> - 0.22-17
- Resolved: 1122856, 1122857

* Wed Jul 23 2014 Irina Boverman <iboverma@redhat.com> - 0.22-16
- Resolved: 1119903

* Tue May 27 2014 Irina Boverman <iboverma@redhat.com> - 0.22-15
- Resolved: 1100442

* Fri Apr 25 2014 Irina Boverman <iboverma@redhat.com> - 0.22-14
- Resolved: 1088003

* Fri Apr  4 2014 Irina Boverman <iboverma@redhat.com> - 0.22-13
- Resolved: 1076470

* Fri Mar  7 2014 Irina Boverman <iboverma@redhat.com> - 0.22-12
- Resolved: 1069757

* Fri Feb  7 2014 Irina Boverman <iboverma@redhat.com> - 0.22-11
- Resolved: 1053761

* Wed Jan 15 2014 Irina Boverman <iboverma@redhat.com> - 0.22-10
- Resolved: 1044003

* Fri Jan  3 2014 Irina Boverman <iboverma@redhat.com> - 0.22-9
- Resolved: 1041574

* Wed Nov 20 2013 Irina Boverman <iboverma@redhat.com> - 0.22-8
- Make it consistent with qpid-cpp-0.22-27

* Wed Nov  6 2013 Irina Boverman <iboverma@redhat.com> - 0.22-7
- Make it consistent with qpid-cpp-0.22-25

* Thu Sep 26 2013 Irina Boverman <iboverma@redhat.com> - 0.22-5
- Resolved bz: 959446

* Fri Jun 28 2013 Irina Boverman <iboverma@redhat.com> - 0.22-4
- Resolved bz: 959446

* Thu Jun 13 2013 Irina Boverman <iboverma@redhat.com> - 0.22-3
- Updated source tarball based 0.22-RC6
- Resolved bz(s): 574571, 696919, 719589, 772028, 788040, 908224 and 950501

* Tue May  7 2013 Irina Boverman <iboverma@redhat.com> - 0.22-2
- Updated source file

* Wed Apr 24 2013 Irina Boverman <iboverma@redhat.com> - 0.22-1
- Rebase to 0.22

* Thu Nov  1 2012 Irina Boverman <iboverma@redhat.com> - 0.18-4
- Resolves: rhbz856299, 0.18-4

* Wed Oct 24 2012 Irina Boverman <iboverma@redhat.com> - 0.18-3
- Resolves: rhbz856299, 0.18-3

* Sun Oct 14 2012 Irina Boverman <iboverma@redhat.com> - 0.18-2
- Resolves: rhbz#861956, 0.18-2

* Thu Oct  4 2012 Irina Boverman <iboverma@redhat.com> - 0.18-1
- Resolves: rhbz#861956
- Rebase to Qpid 0.18+

