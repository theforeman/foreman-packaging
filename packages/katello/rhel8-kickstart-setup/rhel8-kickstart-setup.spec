Name:     rhel8-kickstart-setup
Version:  0.0.2
Release:  3%{?dist}
Summary:  Adjust RHEL8 Kickstart ISOs for Katello/Satellite

Group:    Applications/System
License:  GPLv3
URL:      https://github.com/RedHatSatellite/rhel8-kickstart-setup
Source0:  https://codeload.github.com/RedHatSatellite/rhel8-kickstart-setup/tar.gz/%{version}#/%{name}-%{version}.tar.gz

BuildArch: noarch

%description
Script to extract RHEL8 installation ISOs in a format
that can be used by disconnected Katello and Satellite installations

%prep
%setup -q

%build
sed -i 's#!/usr/bin/env python#!/usr/bin/env python3#' %{name}.py

%install
install -D %{name}.py %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%doc README.md
%license LICENSE

%changelog
* Wed Mar 22 2023 Evgeni Golov - 0.0.2-3
- Use Python3 explicitly

* Wed Sep 18 2019 Eric D. Helms <ericdhelms@gmail.com> - 0.0.2-2
- Corrected the license format

* Mon Mar 25 2019 Evgeni Golov - 0.0.2-1
- new package
