Name:     rhel8-kickstart-setup
Version:  0.0.2
Release:  1%{?dist}
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

%install
install -D %{name}.py %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%doc README.md
%license LICENSE

%changelog
* Mon Mar 25 2019 Evgeni Golov - 0.0.2-1
- new package
