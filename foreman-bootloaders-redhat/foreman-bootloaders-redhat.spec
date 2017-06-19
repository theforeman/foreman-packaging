%define _binaries_in_noarch_packages_terminate_build 0

Name: foreman-bootloaders-redhat
Version: 201705231433
Release: 1%{?dist}
Summary: Binaries of Grub1, Grub2 and Shim bootloaders

Group: Applications/System
License: GPLv2+ and GPLv3+ and BSD
URL: https://github.com/theforeman/foreman-bootloaders
Source0: http://downloads.theforeman.org/foreman-bootloaders/%{name}-%{version}.tar.bz2
BuildArch: noarch


%description
The package contains binaries of Grub and Grub2 bootloaders for PXE/BOOTP use
on TFTP Foreman Proxy extracted from Red Hat Enterprise Linux 6 and 7. This
noarch package contains binaries for multiple architectures, including x86_64,
i386, ARM64, PPC64 and PPC64 LE.

%package tftpboot
Summary: Copies of bootloaders for PXE
Group: Applications/System
Requires: coreutils
Requires: %{name}
Requires: /var/lib/tftpboot
Requires: foreman-proxy

%description tftpboot
Contains copies of bootloaders for use with TFTP servers installed at
/var/lib/tftpboot.


%prep
%setup -q -n tftpboot


%build


%install
install -d -m0755 %{buildroot}%{_datarootdir}/%{name}
install -d -m0755 %{buildroot}%{_datarootdir}/%{name}/grub
install -d -m0755 %{buildroot}%{_datarootdir}/%{name}/grub2
install -m0644 -t %{buildroot}%{_datarootdir}/%{name}/grub grub/*
install -m0644 -t %{buildroot}%{_datarootdir}/%{name}/grub2 grub2/*
install -d -m0755 %{buildroot}%{_sharedstatedir}/tftpboot


%files
%attr(755,root,root)
%dir %{_datarootdir}/%{name}/grub
%dir %{_datarootdir}/%{name}/grub2
%attr(644,root,root)
%{_datarootdir}/%{name}/grub/grubia32.efi
%{_datarootdir}/%{name}/grub/grubx64.efi
%{_datarootdir}/%{name}/grub2/grubaa64.efi
%{_datarootdir}/%{name}/grub2/grubia32.efi
%{_datarootdir}/%{name}/grub2/grubppc64.efi
%{_datarootdir}/%{name}/grub2/grubppc64.elf
%{_datarootdir}/%{name}/grub2/grubppc64le.efi
%{_datarootdir}/%{name}/grub2/grubppc64le.elf
%{_datarootdir}/%{name}/grub2/grubx64.efi
%{_datarootdir}/%{name}/grub2/shimaa64.efi
%{_datarootdir}/%{name}/grub2/shimaa64-redhat.efi
%{_datarootdir}/%{name}/grub2/shimia32.efi
%{_datarootdir}/%{name}/grub2/shimia32-redhat.efi
%{_datarootdir}/%{name}/grub2/shimx64.efi
%{_datarootdir}/%{name}/grub2/shimx64-redhat.efi


%files tftpboot
%ghost %{_sharedstatedir}/tftpboot/grub
%ghost %{_sharedstatedir}/tftpboot/grub2
%ghost %{_sharedstatedir}/tftpboot/grub/grubia32.efi
%ghost %{_sharedstatedir}/tftpboot/grub/grubx64.efi
%ghost %{_sharedstatedir}/tftpboot/grub2/grubaa64.efi
%ghost %{_sharedstatedir}/tftpboot/grub2/grubia32.efi
%ghost %{_sharedstatedir}/tftpboot/grub2/grubppc64.efi
%ghost %{_sharedstatedir}/tftpboot/grub2/grubppc64.elf
%ghost %{_sharedstatedir}/tftpboot/grub2/grubppc64le.efi
%ghost %{_sharedstatedir}/tftpboot/grub2/grubppc64le.elf
%ghost %{_sharedstatedir}/tftpboot/grub2/grubx64.efi
%ghost %{_sharedstatedir}/tftpboot/grub2/shimaa64.efi
%ghost %{_sharedstatedir}/tftpboot/grub2/shimaa64-redhat.efi
%ghost %{_sharedstatedir}/tftpboot/grub2/shimia32.efi
%ghost %{_sharedstatedir}/tftpboot/grub2/shimia32-redhat.efi
%ghost %{_sharedstatedir}/tftpboot/grub2/shimx64.efi
%ghost %{_sharedstatedir}/tftpboot/grub2/shimx64-redhat.efi


%post tftpboot
# create copies (hardlinks) of files in tftpboot directory
install -d -m0755 -o foreman-proxy %{buildroot}%{_sharedstatedir}/tftpboot/grub
install -d -m0755 -o foreman-proxy %{buildroot}%{_sharedstatedir}/tftpboot/grub2
cp -lpf %{_datarootdir}/%{name}/grub/* %{_sharedstatedir}/tftpboot/grub/
cp -lpf %{_datarootdir}/%{name}/grub2/* %{_sharedstatedir}/tftpboot/grub2/



%changelog
* Mon Jun 19 2017 Eric D. Helms <ericdhelms@gmail.com> 201705231433-1
- new package built with tito

