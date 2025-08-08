%global debug_package %{nil}

%global collection_namespace theforeman
%global collection_name foreman
%global collection_directory %{_datadir}/ansible/collections/ansible_collections/%{collection_namespace}/%{collection_name}

%global release 1

Name:       ansible-collection-%{collection_namespace}-%{collection_name}
Version:    5.5.0
Release:    %{?prerelease:0.}%{release}%{?prerelease}%{?nightly}%{?dist}
Summary:    The Foreman Project Ansible modules collection

License:    GPLv3+
URL:        https://theforeman.org/plugins/foreman-ansible-modules
Source0:    https://galaxy.ansible.com/download/%{collection_namespace}-%{collection_name}-%{version}.tar.gz
BuildArch:  noarch

Provides: ansible-collection(%{collection_namespace}.%{collection_name}) = %{version}
Provides: bundled(python-apypie) = 0.7.0

Requires: ansible-core
Requires: (python3-requests if (ansible-core >= 1:2.14.7 and ansible-core < 1:2.16.14-3))
Requires: (python3-pyyaml if (ansible-core >= 1:2.14.7 and ansible-core < 1:2.16.14-3))
Requires: (python3.11-requests if (ansible-core >= 2.14.2-3 and ansible-core < 1:2.14.7))
Requires: (python3.11-pyyaml if (ansible-core >= 2.14.2-3 and ansible-core < 1:2.14.7))
Requires: (python3.12-requests if ansible-core >= 1:2.16.14-3)
Requires: (python3.12-pyyaml if ansible-core >= 1:2.16.14-3)


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
* Fri Aug 08 2025 Evgeni Golov - 5.5.0-1
- Release ansible-collection-theforeman-foreman 5.5.0

* Tue Jun 10 2025 Evgeni Golov - 5.4.0-1
- Release ansible-collection-theforeman-foreman 5.4.0

* Thu Mar 20 2025 Evgeni Golov - 5.3.0-1
- Release ansible-collection-theforeman-foreman 5.3.0

* Tue Mar 11 2025 Evgeni Golov - 5.2.0-1
- Release ansible-collection-theforeman-foreman 5.2.0

* Wed Feb 19 2025 Odilon Sousa <osousa@redhat.com> - 5.1.0-2
- Update requests and pyaml requirements to python 3.12

* Fri Dec 06 2024 Evgeni Golov - 5.1.0-1
- Release ansible-collection-theforeman-foreman 5.1.0

* Fri Nov 22 2024 Evgeni Golov - 5.0.0-1
- Release ansible-collection-theforeman-foreman 5.0.0

* Fri Aug 30 2024 Evgeni Golov - 4.2.0-1
- Release ansible-collection-theforeman-foreman 4.2.0

* Wed Jul 17 2024 Evgeni Golov - 4.1.0-1
- Release ansible-collection-theforeman-foreman 4.1.0

* Thu Feb 15 2024 Evgeni Golov - 4.0.0-2
- Adjust requirements for Ansible using Python 3.12

* Fri Jan 12 2024 Evgeni Golov - 4.0.0-1
- Release ansible-collection-theforeman-foreman 4.0.0

* Mon Jan 08 2024 Evgeni Golov - 3.14.0-2
- Adjust requiements for Ansible on EL9

* Fri Sep 08 2023 Evgeni Golov - 3.14.0-1
- Release ansible-collection-theforeman-foreman 3.14.0

* Wed Aug 23 2023 Evgeni Golov - 3.13.0-1
- Release ansible-collection-theforeman-foreman 3.13.0

* Mon Jul 10 2023 Evgeni Golov - 3.12.0-1
- Release ansible-collection-theforeman-foreman 3.12.0

* Wed Jun 14 2023 Evgeni Golov - 3.11.0-1
- Release ansible-collection-theforeman-foreman 3.11.0

* Tue Apr 04 2023 Evgeni Golov - 3.10.0-1
- Release ansible-collection-theforeman-foreman 3.10.0

* Fri Mar 03 2023 Evgeni Golov - 3.9.0-2
- Use Python 3.11 for Ansible in EL8.8

* Mon Feb 20 2023 Evgeni Golov - 3.9.0-1
- Release ansible-collection-theforeman-foreman 3.9.0

* Tue Dec 20 2022 Evgeni Golov - 3.8.0-1
- Release ansible-collection-theforeman-foreman 3.8.0

* Fri Oct 07 2022 Evgeni Golov - 3.7.0-2
- Use python39 packages with ansible-core 2.13+

* Wed Oct 05 2022 Evgeni Golov - 3.7.0-1
- Release ansible-collection-theforeman-foreman 3.7.0

* Fri Sep 02 2022 Evgeni Golov - 3.6.0-1
- Release ansible-collection-theforeman-foreman 3.6.0

* Thu Aug 25 2022 Evgeni Golov - 3.5.0-1
- Release ansible-collection-theforeman-foreman 3.5.0

* Tue May 17 2022 Evgeni Golov - 3.4.0-1
- Release ansible-collection-theforeman-foreman 3.4.0

* Wed Apr 06 2022 Evgeni Golov - 3.3.0-1
- Release ansible-collection-theforeman-foreman 3.3.0

* Tue Mar 15 2022 Evgeni Golov - 3.2.0-2
- adjust dependencies to pull in right requests and pyyaml

* Wed Mar 02 2022 Evgeni Golov - 3.2.0-1
- Release ansible-collection-theforeman-foreman 3.2.0

* Wed Feb 23 2022 Evgeni Golov - 3.1.0-2
- Require ansible or ansible-core on EL8+

* Mon Jan 17 2022 Evgeni Golov - 3.1.0-1
- Release ansible-collection-theforeman-foreman 3.1.0

* Fri Nov 12 2021 Evgeni Golov - 3.0.0-1
- Release ansible-collection-theforeman-foreman 3.0.0

* Wed Aug 25 2021 Evgeni Golov - 2.2.0-1
- Release ansible-collection-theforeman-foreman 2.2.0

* Tue Jul 13 2021 Evgeni Golov - 2.1.2-1
- Release ansible-collection-theforeman-foreman 2.1.2

* Wed Jun 23 2021 Evgeni Golov - 2.1.1-1
- Release ansible-collection-theforeman-foreman 2.1.1

* Thu May 20 2021 Evgeni Golov - 2.1.0-1
- Release ansible-collection-theforeman-foreman 2.1.0

* Wed Mar 03 2021 Evgeni Golov - 2.0.1-1
- Release ansible-collection-theforeman-foreman 2.0.1

* Mon Feb 22 2021 Evgeni Golov - 2.0.0-1
- Release ansible-collection-theforeman-foreman 2.0.0

* Mon Dec 14 2020 Evgeni Golov - 1.5.1-1
- Release ansible-collection-theforeman-foreman 1.5.1

* Thu Dec 03 2020 Evgeni Golov - 1.5.0-1
- Release ansible-collection-theforeman-foreman 1.5.0

* Thu Oct 22 2020 Evgeni Golov - 1.4.0-1
- Release ansible-collection-theforeman-foreman 1.4.0

* Tue Sep 22 2020 Evgeni Golov - 1.3.0-1
- Release ansible-collection-theforeman-foreman 1.3.0

* Fri Sep 04 2020 Evgeni Golov - 1.2.0-1
- Release ansible-collection-theforeman-foreman 1.2.0

* Mon Aug 17 2020 Evgeni Golov - 1.1.0-1
- Release ansible-collection-theforeman-foreman 1.1.0
- Add a provides for ansible-collection(theforeman.foreman)

* Tue Jun 30 2020 Evgeni Golov - 1.0.1-1
- Release ansible-collection-theforeman-foreman 1.0.1

* Fri Jun 19 2020 Evgeni Golov - 1.0.0-1
- Release ansible-collection-theforeman-foreman 1.0.0

* Fri Jun 05 2020 Evgeni Golov - 0.8.1-1
- Release ansible-collection-theforeman-foreman 0.8.1

* Tue Apr 21 2020 Evgeni Golov - 0.8.0-1
- Release ansible-collection-theforeman-foreman 0.8.0

* Wed Mar 18 2020 Evgeni Golov - 0.7.0-1
- Release ansible-collection-theforeman-foreman 0.7.0

* Tue Mar 10 2020 Evgeni Golov - 0.6.0-1
- Release ansible-collection-theforeman-foreman 0.6.0

* Thu Jan 23 2020 Evgeni Golov - 0.4.1-1
- Release ansible-collection-theforeman-foreman 0.4.1

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
