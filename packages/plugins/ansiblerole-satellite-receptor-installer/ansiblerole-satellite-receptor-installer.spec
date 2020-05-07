%global repo_orgname project-receptor
%global repo_name satellite-receptor-installer

%global role_orgname %{repo_orgname}
%global role_name satellite_receptor_installer

Name: ansiblerole-satellite-receptor-installer
Summary: Packaging of the satellite_receptor_installer Ansible role
Version: 0.6.6
Release: 1%{?dist}
License: GPLv3

Source0: https://github.com/%{repo_orgname}/%{repo_name}/archive/v%{version}.tar.gz#/%{role_name}-%{version}.tar.gz
Url: https://github.com/%{repo_orgname}/%{repo_name}/
BuildArch: noarch

Requires: ansible

%description
This package installs the satellite_receptor_installer Ansibile role.
The role can be used to install and configure the receptor based on
Foreman organizations. It requires Foreman user in order to read Foreman
data.

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
* Thu May 7 2020 Adam Ruzicka <aruzicka@redhat.com> - 0.6.6-1
- Version bump to 0.6.6

* Mon Apr 27 2020 Marek Hulan <mhulan@redhat.com> - 0.6.5-1
- Version bump to 0.6.5

* Fri Apr 3 2020 Marek Hulan <mhulan@redhat.com> - 0.6.4-1
- Version bump to 0.6.4

* Wed Apr 1 2020 Marek Hulan <mhulan@redhat.com> - 0.6.3-1
- Version bump to 0.6.3

* Thu Mar 19 2020 Marek Hulan <mhulan@redhat.com> - 0.6.2-1
- Version bump to 0.6.2

* Thu Mar 12 2020 Marek Hulan <mhulan@redhat.com> - 0.6.0-2
- Repackage the 0.6.0, the tag has been force changed

* Wed Mar 11 2020 Marek Hulan <mhulan@redhat.com> - 0.6.0-1
- Version bump to 0.6.0

* Tue Nov 26 2019 Marek Hulan <mhulan@redhat.com> - 0.5.0-1
- Initial packaging of 0.5.0
