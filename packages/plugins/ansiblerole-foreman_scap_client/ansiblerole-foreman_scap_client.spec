%global repo_orgname theforeman
%global repo_name ansible-foreman_scap_client

%global role_orgname %{repo_orgname}
%global role_name foreman_scap_client

Name: ansiblerole-foreman_scap_client
Summary: Packaging of the foreman_scap_client Ansible role
Version: 0.4.0
Release: 1%{?dist}
License: GPLv3

Source0: https://github.com/%{repo_orgname}/%{repo_name}/archive/%{version}.tar.gz#/%{role_name}-%{version}.tar.gz
Url: https://github.com/%{repo_orgname}/%{repo_name}/
BuildArch: noarch

%if 0%{?rhel} == 7
Requires: ansible
%else
Requires: (ansible or ansible-core)
%endif

%description
This package installs the foreman_scap_client Ansibile role.

Make sure that "/usr/share/ansible/roles" is on your Ansible role_path.

%prep

%setup -qc

%build

%install
mkdir -p %{buildroot}%{_datadir}/ansible/roles
cp -pR %{repo_name}-%{version} %{buildroot}%{_datadir}/ansible/roles/%{role_orgname}.%{role_name}

%files
%{_datadir}/ansible/roles/%{role_orgname}.%{role_name}
%doc %{repo_name}-%{version}/README.md

%changelog
* Thu Mar 06 2025 Adam Ruzicka <aruzicka@redhat.com> - 0.4.0-1
- Update to 0.4.0

* Thu Mar 06 2025 Adam Ruzicka <aruzicka@redhat.com> - 0.3.1-1
- Update to 0.3.1

* Mon Jun 17 2024 Adam Ruzicka <aruzicka@redhat.com> - 0.3.0-1
- Update to 0.3.0

* Wed Feb 23 2022 Evgeni Golov - 0.2.0-2
- Require ansible or ansible-core on EL8+

* Tue May 18 2021 Ondrej Prazak <oprazak@redhat.com> 0.2.0-1
- Update to 0.2.0

* Thu Nov 05 2020 Ondrej Prazak <oprazak@redhat.com> 0.1.0-1
- Update to 0.1.0

* Thu Jul 30 2020 Ondrej Prazak <oprazak@redhat.com> 0.0.6-1
- Update to 0.0.6

* Thu May 21 2020 Ondrej Prazak <oprazak@redhat.com> 0.0.5-1
- Update to 0.0.5

* Wed Nov 20 2019 Ondrej Prazak <oprazak@redhat.com> - 0.0.4-1
- Update to version 0.0.4
* Wed Jul 24 2019 Ondrej Prazak <oprazak@redhat.com> - 0.0.3-1
- Update to version 0.0.3
* Mon Mar 25 2019 Ondrej Prazak <oprazak@redhat.com> - 0.0.2-1
- Update to version 0.0.2
* Thu Feb 14 2019 Ondrej Prazak <oprazak@redhat.com> - 0.0.1-1
- Initial release.
