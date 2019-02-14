%global repo_orgname theforeman
%global repo_name ansible-foreman_scap_client

%global role_orgname %{repo_orgname}
%global role_name foreman_scap_client

Name: ansiblerole-foreman_scap_client
Summary: Packaging of the foreman_scap_client Ansible role
Version: 0.0.1
Release: 1%{?dist}
License: GPLv3

Source0: https://github.com/%{repo_orgname}/%{repo_name}/archive/%{version}.tar.gz#/%{role_name}-%{version}.tar.gz
Url: https://github.com/%{repo_orgname}/%{repo_name}/
BuildArch: noarch

Requires: ansible

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
* Thu Feb 14 2019 Ondrej Prazak <oprazak@redhat.com> - 0.0.1-1
- Initial release.
