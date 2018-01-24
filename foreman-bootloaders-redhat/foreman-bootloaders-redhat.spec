Name: foreman-bootloaders-redhat
Version: 201801241201
Release: 1%{?dist}
Summary: Metapackage with Grub2 and Shim TFTP bootloaders

Group: Applications/System
License: GPLv2+ and GPLv3+ and BSD
URL: https://github.com/theforeman/foreman
BuildArch: noarch

Source0: foreman-generate-bootloaders

Requires: grub2-tools-extra
Requires: grub2-efi-ia32-modules
Requires: grub2-efi-x64-modules
Requires: grub2-pc-modules
Requires: shim-ia32
Requires: shim-x64

%description
Package containing foreman-generate-bootloaders helper script which generates and copies
Grub2 and Shim bootloaders for PC and EFI into /var/lib/tftpboot.

%package tftpboot
Summary: Copies of bootloaders for PXE
Group: Applications/System
Requires: coreutils
Requires: %{name}
Requires: /var/lib/tftpboot
Requires: foreman-proxy

%description tftpboot
This is a metapackage that contains post-install script which generates the
bootloaders using foreman-generate-bootloaders script.

%prep

%build

%install
install -Dp -m0755 %{SOURCE0} %{buildroot}%{_bindir}/foreman-generate-bootloaders

%files
%{_bindir}/foreman-generate-bootloaders

%files tftpboot
%ghost %{_sharedstatedir}/tftpboot/grub2
%ghost %{_sharedstatedir}/tftpboot/grub2/grubaa64.efi
%ghost %{_sharedstatedir}/tftpboot/grub2/grubia32.0
%ghost %{_sharedstatedir}/tftpboot/grub2/grubia32.efi
%ghost %{_sharedstatedir}/tftpboot/grub2/grubppc64.efi
%ghost %{_sharedstatedir}/tftpboot/grub2/grubppc64.elf
%ghost %{_sharedstatedir}/tftpboot/grub2/grubppc64le.efi
%ghost %{_sharedstatedir}/tftpboot/grub2/grubppc64le.elf
%ghost %{_sharedstatedir}/tftpboot/grub2/grubppc.efi
%ghost %{_sharedstatedir}/tftpboot/grub2/grubppc.elf
%ghost %{_sharedstatedir}/tftpboot/grub2/grubx64.efi
%ghost %{_sharedstatedir}/tftpboot/grub2/shim.efi
%ghost %{_sharedstatedir}/tftpboot/grub2/shimx64.efi
%ghost %{_sharedstatedir}/tftpboot/grub2/shimx64-redhat.efi
%ghost %{_sharedstatedir}/tftpboot/grub2/shimaa64.efi
%ghost %{_sharedstatedir}/tftpboot/grub2/shimaa64-redhat.efi


%post tftpboot
%{_bindir}/foreman-generate-bootloaders x86_64 noinstall


%changelog
* Mon Jul 17 2017 Eric D. Helms <ericdhelms@gmail.com> 201707171807-1
- Foreman-bootloaders rebase to 201707171807 (lzap+git@redhat.com)

* Mon Jun 19 2017 Eric D. Helms <ericdhelms@gmail.com> 201705231433-1
- new package built with tito

