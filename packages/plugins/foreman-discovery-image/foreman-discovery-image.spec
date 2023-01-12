# TODO: get rid of the hash in the filename?
%define version_major_minor 4.1
%define version_patch 0
%define hash 24d62de
%define tftproot /var/lib/tftpboot

Name:      foreman-discovery-image
Version:   %{version_major_minor}.%{version_patch}
Release:   1%{?dist}
Summary:   Foreman Discovery Image
License:   GPL-2.0
URL:       https://github.com/theforeman/foreman-discovery-image
# TODO: Avoid major.minor as a directory? Get it via substring?
Source:    https://downloads.theforeman.org/discovery/releases/%{version_major_minor}/fdi-image-%{version}-%{hash}.tar
BuildArch: noarch

%description
The Foreman Discovery Image is a minimal OS installation that registers itself
to Foreman when it boots up. That allows the user to then further provision the
machine.

%prep
%autosetup -n fdi-image

%build

%install
mkdir -p %{buildroot}%{tftproot}
mv initrd0.img vmlinuz0 %{buildroot}%{tftproot}

%files
%dir %{tftproot}
%{tftproot}/initrd0.img
%{tftproot}/vmlinuz0
%doc README

%changelog
* Thu Jan 12 2023 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 4.1.0-1
- Initial package

