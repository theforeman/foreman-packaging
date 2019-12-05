# vim: sw=4:ts=4:et
#
# Copyright (c) 2016 Red Hat, Inc.

# This program and entire repository is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the License,
# or any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.
#

Name:           katello-client-bootstrap
Version:        1.7.4
Release:        1%{?dist}
Summary:        Client bootstrap utility for Foreman and Katello

Group:          System Environment/Base
License:        LGPLv2
URL:            http://www.katello.org
Source0:        https://codeload.github.com/Katello/%{name}/tar.gz/%{version}#/%{name}-%{version}.tar.gz

BuildArch:      noarch

%description
Client bootstrap utility for Foreman and Katello

%prep

%setup -q -n %{name}-%{version}

%build

%install
install -m644 -D bootstrap.py %{buildroot}%{_var}/www/html/pub/bootstrap.py

%files
%doc README.md
%doc bootstrap.yml
%defattr(-,apache,apache,-)
%{_var}/www/html/pub
%{_var}/www/html/pub/bootstrap.py

%changelog
* Thu Dec 05 2019 Evgeni Golov - 1.7.4-1
- Release katello-client-bootstrap 1.7.4

* Mon Sep 09 2019 Evgeni Golov - 1.7.3-1
- Release katello-client-boostrap 1.7.3

* Thu Apr 18 2019 Evgeni Golov - 1.7.2-2
- Install bootstrap.py without executable bit

* Mon Apr 01 2019 Evgeni Golov - 1.7.2-1
- Release katello-client-boostrap 1.7.2

* Tue Mar 12 2019 Evgeni Golov - 1.7.1-1
- Release katello-client-boostrap 1.7.1

* Fri Jan 25 2019 Evgeni Golov - 1.7.0-1
- Release katello-client-bootstrap 1.7.0

* Mon Jan 07 2019 Evgeni Golov - 1.6.0-2
- Include the Ansible playbook as part of katello-client-bootstrap documentation.

* Thu Aug 02 2018 Evgeni Golov <evgeni@golov.de> 1.6.0-1
- Release katello-client-bootstrap 1.6.0

* Wed Jan 24 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.5.1-1
- Release katello-client-bootstrap 1.5.1 (evgeni@golov.de)

* Tue Jan 23 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.5.0-1
- new package built with tito

* Mon Oct 09 2017 Evgeni Golov 1.4.2-1
- Release katello-client-bootstrap 1.4.2 (#550) (evgeni@golov.de)

* Wed Aug 30 2017 Eric D. Helms <ericdhelms@gmail.com> 1.4.1-1
- Release katello-client-bootstrap 1.4.1 (evgeni@golov.de)

* Tue Jun 13 2017 Eric D. Helms <ericdhelms@gmail.com> 1.4.0-1
- Release katello-client-bootstrap 1.4.0 (egolov@redhat.com)
- katello-client-update - more friendly filename (komidore64@gmail.com)
- add README.md to katello-client-bootstrap RPM (evgeni@golov.de)

* Fri Jun 09 2017 Evgeni Golov <egolov@redhat.com> 1.4.0-1
- Release katello-client-bootstrap 1.4.0

* Mon Mar 27 2017 Eric D Helms <ericdhelms@gmail.com> 1.3.0-1
- Release katello-client-bootstrap 1.3.0 (ericdhelms@gmail.com)

* Mon Dec 05 2016 Eric D Helms <ericdhelms@gmail.com> 1.2.2-1
- Add katello-client-bootstrap 1.2.2 (zhunting@redhat.com)

* Mon Nov 21 2016 Eric D Helms <ericdhelms@gmail.com> 1.2.0-1
- Add katello-client-boostrap 1.2.0 (ericdhelms@gmail.com)

* Tue May 31 2016 Eric D Helms <ericdhelms@gmail.com> 1.1.0-1
- Fixes #15251 - client-bootstrap 1.1.0 release (#231) (mmccune@gmail.com)

* Fri Apr 08 2016 Eric D Helms <ericdhelms@gmail.com> 1.0.0-1
- new package built with tito

