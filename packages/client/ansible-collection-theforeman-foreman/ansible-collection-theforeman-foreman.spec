%global debug_package %{nil}

%global collection_namespace theforeman
%global collection_name foreman
%global collection_directory %{_datadir}/ansible/collections/ansible_collections/%{collection_namespace}/%{collection_name}

%if 0%{?fedora} || 0%{?rhel} >= 8
%global ansible_python python3
%global pyyaml %{ansible_python}-pyyaml
%else
%global ansible_python python2
%global pyyaml PyYAML
%endif

%global release 2

Name:       ansible-collection-%{collection_namespace}-%{collection_name}
Version:    0.4.0
Release:    %{?prerelease:0.}%{release}%{?prerelease}%{?nightly}%{?dist}
Summary:    The Foreman Project Ansible modules collection

License:    GPLv3+
URL:        https://theforeman.org/plugins/foreman-ansible-modules
Source0:    https://galaxy.ansible.com/download/%{collection_namespace}-%{collection_name}-%{version}.tar.gz
BuildArch:  noarch

Requires: ansible >= 2.8
Requires: %{ansible_python}-apypie >= 0.0.5
Requires: %{pyyaml}
%if 0%{?rhel} == 7
Requires: python-ipaddress
%endif

%description
Collection of Ansible Modules to manage Foreman installations.
Includes modules for Katello.

%prep
%setup -q -c

%build

%install
mkdir -p %{buildroot}%{collection_directory}
cp -a ./* %{buildroot}%{collection_directory}



%files
%{collection_directory}/
%license %{collection_directory}/LICENSE
%doc %{collection_directory}/README.md



%changelog
* Mon Jan 13 2020 Evgeni Golov - 0.4.0-2
- Rebuild for EL8 client repository

* Thu Jan 09 2020 Evgeni Golov - 0.4.0-1
- Release ansible-collection-theforeman-foreman 0.4.0

* Fri Dec 06 2019 Evgeni Golov - 0.3.0-1
- Release ansible-collection-theforeman-foreman 0.3.0

* Wed Oct 30 2019 Evgeni Golov - 0.2.0-1
- Release ansible-collection-theforeman-foreman 0.2.0

* Wed Sep 18 2019 Evgeni Golov - 0.1.0-1
- Initial package
