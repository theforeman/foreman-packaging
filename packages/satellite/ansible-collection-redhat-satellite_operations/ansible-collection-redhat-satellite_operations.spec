%global debug_package %{nil}

%global collection_namespace redhat
%global collection_name satellite_operations
%global collection_directory %{_datadir}/ansible/collections/ansible_collections/%{collection_namespace}/%{collection_name}

%global release 1

Name:       ansible-collection-%{collection_namespace}-%{collection_name}
Version:    3.0.0
Release:    %{?prerelease:0.}%{release}%{?prerelease}%{?nightly}%{?dist}
Summary:    Red Hat Satellite Ansible operations collection

License:    GPLv3+
URL:        https://github.com/RedHatSatellite/satellite-operations-collection
Source0:    https://github.com/RedHatSatellite/satellite-operations-collection/releases/download/v%{version}/%{collection_namespace}-%{collection_name}-%{version}.tar.gz
BuildArch:  noarch

Provides: ansible-collection(%{collection_namespace}.%{collection_name}) = %{version}
Requires: ansible-core

%description
Ansible assets for managing Satellite operations such as install, upgrade or maintenance tasks.

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
* Mon Apr 08 2024 Evgeni Golov - 3.0.0-1
- Release ansible-collection-redhat-satellite_operations 3.0.0

* Mon Sep 04 2023 Evgeni Golov - 2.1.0-1
- Release ansible-collection-redhat-satellite_operations 2.1.0

* Mon May 15 2023 Eric D. Helms <ericdhelms@gmail.com> - 2.0.0-1
- Release ansible-collection-redhat-satellite_operations 2.0.0

* Thu Jan 19 2023 Evgeni Golov - 1.3.0-2
- Correct Ansible requirement

* Thu Jan 12 2023 Evgeni Golov - 1.3.0-1
- Release ansible-collection-redhat-satellite_operations 1.3.0

* Wed Jun 15 2022 Evgeni Golov - 1.2.3-1
- Release ansible-collection-redhat-satellite_operations 1.2.3

* Thu Jun 09 2022 Eric D. Helms <ericdhelms@gmail.com> - 1.2.2-1
- Release 1.2.2

* Mon May 23 2022 Eric D. Helms <ericdhelms@gmail.com> - 1.2.1-1
- Release 1.2.1

* Tue May 17 2022 Eric D. Helms <ericdhelms@gmail.com> - 1.2.0-1
- Release 1.2.0

* Mon May 09 2022 Eric D. Helms <ericdhelms@gmail.com> - 1.1.1-1
- Release ansible-collection-redhat-satellite_operations 1.1.1

* Mon May 02 2022 Evgeni Golov - 1.1.0-2
- Support ansible-core 2.12

* Tue Apr 26 2022 Eric D. Helms <ericdhelms@gmail.com> - 1.1.0-1
- Release ansible-collection-redhat-satellite_operations 1.1.0

* Wed May 26 2021 Eric Helms - 0.3.2-1
- Initial package
