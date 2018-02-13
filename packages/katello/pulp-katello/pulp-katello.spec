# Copyright (c) 2013 Red Hat, Inc.
#
# This software is licensed to you under the GNU General Public
# License as published by the Free Software Foundation; either version
# 2 of the License (GPLv2) or (at your option) any later version.
# There is NO WARRANTY for this software, express or implied,
# including the implied warranties of MERCHANTABILITY,
# NON-INFRINGEMENT, or FITNESS FOR A PARTICULAR PURPOSE. You should
# have received a copy of GPLv2 along with this software; if not, see
# http://www.gnu.org/licenses/old-licenses/gpl-2.0


%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}


Name: pulp-katello
Version: 1.0.2
Release: 1%{?dist}
Summary: Plugins useful for katello interactions with pulp
Group: Development/Languages
License: GPLv2
URL: https://github.com/katello/pulp-katello
Source0: https://codeload.github.com/Katello/pulp-katello/tar.gz/%{version}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-nose
BuildRequires:  rpm-python
BuildRequires:  python-lxml

Requires: python-pulp-rpm-common
Requires: python-lxml
Requires: pulp-server >= 2.8

Obsoletes: pulp-katello-plugins

%description
Provides a collection of platform plugins, client extensions and agent
handlers that provide RPM support.

%prep
%setup  -n %{name}-%{version}%{?dashalphatag}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{python_sitelib}/pulp_katello/
%{python_sitelib}/pulp_katello*.egg-info
%license LICENSE
%doc README.md


%changelog
* Mon Aug 01 2016 Justin Sherrill <jsherril@redhat.com> 1.0.2-1
- Rebuild pulp-katello to 1.0.2 (jsherril@redhat.com)

* Thu Jul 07 2016 Eric D Helms <ericdhelms@gmail.com> 1.0.1-1
- Update pulp-katello to 1.0.1 (#249) (eric.d.helms@gmail.com)

* Mon Feb 01 2016 Justin Sherrill <jsherril@redhat.com> 1.0-1
-  updating pulp-katello to 1.0 (jsherril@redhat.com)

* Wed Jul 29 2015 Eric D. Helms <ericdhelms@gmail.com> 0.4-3
- new package built with tito

* Tue Jun 09 2015 Eric D. Helms <ericdhelms@gmail.com> 0.4-2
- Change to ReleaseTagger. (ericdhelms@gmail.com)
- Fixes #10574: Remove unneeded dependencies from spec file.
  (ericdhelms@gmail.com)

* Tue Jun 09 2015 Eric D. Helms <ericdhelms@gmail.com>
- Change to ReleaseTagger. (ericdhelms@gmail.com)
- Fixes #10574: Remove unneeded dependencies from spec file.
  (ericdhelms@gmail.com)

* Tue Jun 09 2015 Eric D. Helms <ericdhelms@gmail.com>
- Fixes #10574: Remove unneeded dependencies from spec file.
  (ericdhelms@gmail.com)

* Thu Apr 09 2015 Justin Sherrill <jsherril@redhat.com> 0.4-1
- fixes #9904 - updated repomd.xml timestamps with every yum_clone publish
  (jsherril@redhat.com)
- fixes #9801 - spec require qpid-cpp-server-linearstore instead of qpid-cpp-
  server-store (dtsang@redhat.com)
- fixes #7279 - adding Requires on cyrus-sasl-plain (bbuckingham@redhat.com)

* Tue Mar 17 2015 Dustin Tsang<dustint@redhat.com> 0.3-4
- update to use qpid-cpp-server-linearstore instead of qpid-cpp-server-store

* Fri Aug 22 2014 Justin Sherrill <jsherril@redhat.com> 0.3-3
- initial tag of pulp-katello

* Mon Jun 2 2014 Jason Montleon <jmontleo@redhat.com> 0.3-3
- Obsolete pulp-katello-plugins

* Mon Jun 2 2014 Jason Montleon <jmontleo@redhat.com> 0.3-2
- Rename package to pulp-katello
- add qpid dependencies

* Fri May 16 2014 Justin Sherrill <jsherril@redhat.com> 0.3-1
- Refs #5377 - Adapting for pulp 2.4 support
- Fixes #4649 - support index file creation (jsherril@redhat.com)

* Mon Jul 22 2013 Justin Sherrill <jsherril@redhat.com> 0.2-1
- fixing rpm spec requires to not depend on specific pulp version
  (jsherril@redhat.com)

* Mon Jul 22 2013 Justin Sherrill <jsherril@redhat.com> 0.1-0.1
- new package built with tito
