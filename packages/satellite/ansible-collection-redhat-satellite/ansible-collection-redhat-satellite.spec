%global debug_package %{nil}

%global collection_namespace redhat
%global collection_name satellite
%global collection_directory %{_datadir}/ansible/collections/ansible_collections/%{collection_namespace}/%{collection_name}

%global release 1

Name:       ansible-collection-%{collection_namespace}-%{collection_name}
Version:    5.3.0
Release:    %{?prerelease:0.}%{release}%{?prerelease}%{?nightly}%{?dist}
Summary:    Red Hat Satellite Ansible Modules Collection

License:    GPLv3+
URL:        https://github.com/RedHatSatellite/satellite-ansible-collection
Source0:    https://github.com/RedHatSatellite/satellite-ansible-collection/releases/download/%{version}/%{collection_namespace}-%{collection_name}-%{version}.tar.gz
BuildArch:  noarch

Provides: ansible-collection(%{collection_namespace}.%{collection_name}) = %{version}
Provides: ansible-collection-theforeman-foreman = %{version}
Provides: bundled(python-apypie) = 0.7.0

Requires: ansible-core
Requires: (python3-requests if (ansible-core >= 1:2.14.7 and ansible-core < 1:2.16.14-3))
Requires: (python3-pyyaml if (ansible-core >= 1:2.14.7 and ansible-core < 1:2.16.14-3))
Requires: (python3.11-requests if (ansible-core >= 2.14.2-3 and ansible-core < 1:2.14.7))
Requires: (python3.11-pyyaml if (ansible-core >= 2.14.2-3 and ansible-core < 1:2.14.7))
Requires: (python3.12-requests if ansible-core >= 1:2.16.14-3)
Requires: (python3.12-pyyaml if ansible-core >= 1:2.16.14-3)


%description
Collection of Ansible Modules to manage Satellite installations.

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
* Thu Mar 20 2025 Evgeni Golov - 5.3.0-1
- Release ansible-collection-redhat-satellite 5.3.0

* Tue Mar 11 2025 Evgeni Golov - 5.2.0-1
- Release ansible-collection-redhat-satellite 5.2.0

* Wed Feb 19 2025 Odilon Sousa <osousa@redhat.com> - 5.1.0-2
- Update requests and pyaml requirements to python 3.12

* Fri Dec 06 2024 Evgeni Golov - 5.1.0-1
- Release ansible-collection-redhat-satellite 5.1.0

* Fri Nov 22 2024 Evgeni Golov - 5.0.0-1
- Release ansible-collection-redhat-satellite 5.0.0

* Mon Sep 02 2024 Evgeni Golov - 4.2.0-1
- Release ansible-collection-redhat-satellite 4.2.0

* Wed Jul 17 2024 Evgeni Golov - 4.1.0-1
- Release ansible-collection-redhat-satellite 4.1.0

* Mon Feb 19 2024 Odilon Sousa <osousa@redhat.com> - 4.0.0-2
- Adjust requirements for Ansible using Python 3.12

* Mon Jan 15 2024 Evgeni Golov - 4.0.0-1
- Release ansible-collection-redhat-satellite 4.0.0

* Fri Dec 15 2023 Evgeni Golov - 3.15.0-1
- Release ansible-collection-redhat-satellite 3.15.0

* Fri Sep 08 2023 Evgeni Golov - 3.14.0-1
- Release ansible-collection-redhat-satellite 3.14.0

* Wed Aug 23 2023 Evgeni Golov - 3.13.0-1
- Release ansible-collection-redhat-satellite 3.13.0

* Mon Jul 10 2023 Evgeni Golov - 3.12.0-1
- Release ansible-collection-redhat-satellite 3.12.0

* Mon Jun 26 2023 Evgeni Golov - 3.11.0-1
- Release ansible-collection-redhat-satellite 3.11.0

* Mon Apr 24 2023 Evgeni Golov - 3.10.0-1
- Release ansible-collection-redhat-satellite 3.10.0

* Fri Mar 03 2023 Evgeni Golov - 3.9.0-2
- BZ#2170034 - Use Python 3.11 for Ansible in EL8.8

* Mon Feb 20 2023 Evgeni Golov - 3.9.0-1
- Release ansible-collection-redhat-satellite 3.9.0

* Fri Jan 13 2023 Evgeni Golov - 3.8.0-1
- Release ansible-collection-redhat-satellite 3.8.0

* Fri Nov 25 2022 Evgeni Golov - 3.7.0-3
- Use python39 packages with ansible-core 2.13+

* Fri Oct 07 2022 Eric D. Helms <ericdhelms@gmail.com> - 3.7.0-2
- Match upstream packaging requirements, fix ansible vs ansible-core

* Thu Oct 06 2022 Patrick Creech <pcreech@redhat.com> - 3.7.0-1
- Release ansible-collection-redhat-satellite 3.7.0

* Fri Sep 02 2022 Evgeni Golov - 3.6.0-1
- Release ansible-collection-redhat-satellite 3.6.0

* Wed Apr 06 2022 Evgeni Golov - 3.3.0-1
- Release ansible-collection-redhat-satellite 3.3.0

* Fri Jan 28 2022 Evgeni Golov - 3.1.0-1
- Release ansible-collection-redhat-satellite 3.1.0

* Mon Nov 29 2021 Evgeni Golov - 3.0.0-1
- Release ansible-collection-redhat-satellite 3.0.0

* Mon Sep 20 2021 Zach Huntington-Meath - 2.2.0-1
- BZ #1997724 - Updating a hostgroup with AK via parameters fails if AK alredy exists

* Wed Jul 21 2021 Evgeni Golov - 2.1.2-1
- Release ansible-collection-redhat-satellite 2.1.2

* Thu Jun 24 2021 Evgeni Golov - 2.1.1-1
- Release ansible-collection-redhat-satellite 2.1.1

* Fri May 21 2021 Evgeni Golov - 2.1.0-1
- Release ansible-collection-redhat-satellite 2.1.0

* Wed Mar 03 2021 Evgeni Golov - 2.0.1-1
- Release ansible-collection-redhat-satellite 2.0.1

* Mon Dec 14 2020 Evgeni Golov - 1.5.1-1
- Release ansible-collection-redhat-satellite 1.5.1

* Thu Dec 10 2020 Evgeni Golov - 1.5.0-1
- Release ansible-collection-redhat-satellite 1.5.0

* Wed Sep 23 2020 Evgeni Golov - 1.3.0-1
- Release ansible-collection-redhat-satellite 1.3.0

* Mon Sep 07 2020 Evgeni Golov - 1.2.0-1
- Release ansible-collection-redhat-satellite 1.2.0

* Tue Jul 14 2020 Evgeni Golov - 1.0.1-1
- Release ansible-collection-redhat-satellite 1.0.1

* Mon Jun 29 2020 Evgeni Golov - 1.0.0-1
- Release ansible-collection-redhat-satellite 1.0.0

* Fri May 08 2020 Evgeni Golov - 0.8.0-1
- Release ansible-collection-redhat-satellite 0.8.0
