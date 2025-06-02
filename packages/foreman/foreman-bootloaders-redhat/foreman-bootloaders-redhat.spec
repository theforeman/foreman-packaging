Name: foreman-bootloaders-redhat
Version: 202506020000
Release: 1%{?dist}
Summary: Metapackage with Grub2 and Shim TFTP bootloaders

Group: Applications/System
License: GPLv2+ and GPLv3+ and BSD
URL: https://github.com/theforeman/foreman
BuildArch: noarch

Source0: foreman-generate-bootloaders

Requires: /usr/bin/grub2-mknetdir
Requires: /usr/bin/grub2-mkimage

%if 0%{rhel} < 9
Requires: grub2-efi-ia32-modules
Requires: shim-ia32
%endif
Requires: grub2-efi-x64-modules
Requires: grub2-pc-modules
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
# the following files are managed by foreman-installer (puppet)
%ghost %attr(755, foreman-proxy, root) %{_sharedstatedir}/tftpboot/grub2
%ghost %attr(644, root, root) %{_sharedstatedir}/tftpboot/grub2/shim.efi
%ghost %attr(644, root, root) %{_sharedstatedir}/tftpboot/grub2/grubx64.efi
# the following files are not managed by foreman-installer
%ghost %attr(644, foreman-proxy, root) %{_sharedstatedir}/tftpboot/grub2/grubaa64.efi
%ghost %attr(644, foreman-proxy, root) %{_sharedstatedir}/tftpboot/grub2/grubia32.0
%ghost %attr(644, foreman-proxy, root) %{_sharedstatedir}/tftpboot/grub2/grubia32.efi
%ghost %attr(644, foreman-proxy, root) %{_sharedstatedir}/tftpboot/grub2/grubppc64.efi
%ghost %attr(644, foreman-proxy, root) %{_sharedstatedir}/tftpboot/grub2/grubppc64.elf
%ghost %attr(644, foreman-proxy, root) %{_sharedstatedir}/tftpboot/grub2/grubppc64le.efi
%ghost %attr(644, foreman-proxy, root) %{_sharedstatedir}/tftpboot/grub2/grubppc64le.elf
%ghost %attr(644, foreman-proxy, root) %{_sharedstatedir}/tftpboot/grub2/grubppc.efi
%ghost %attr(644, foreman-proxy, root) %{_sharedstatedir}/tftpboot/grub2/grubppc.elf
%ghost %attr(644, foreman-proxy, root) %{_sharedstatedir}/tftpboot/grub2/shimx64.efi
%ghost %attr(644, foreman-proxy, root) %{_sharedstatedir}/tftpboot/grub2/shimx64-redhat.efi
%ghost %attr(644, foreman-proxy, root) %{_sharedstatedir}/tftpboot/grub2/shimaa64.efi
%ghost %attr(644, foreman-proxy, root) %{_sharedstatedir}/tftpboot/grub2/shimaa64-redhat.efi
%ghost %attr(644, foreman-proxy, root) %{_sharedstatedir}/tftpboot/grub2/mmx64.efi


%post tftpboot
%{_bindir}/foreman-generate-bootloaders x86_64 noinstall


%changelog
* Mon Jun 02 2025 Leos Stejskal <lstejska@redhat.com> 202506020000-1
- Add mmx64.efi to the list of files in grub2 directory

* Mon Nov 11 2024 Evgeni Golov 202102220000-4
- Don't fail if shim-ia32 is missing

* Sat Mar 23 2024 Eric D. Helms <ericdhelms@gmail.com> 202102220000-3
- Only requires shim-ia32 on RHEL 8 or less

* Wed Jan 03 2024 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 202102220000-2
- EL9 compatibility

* Fri Feb 19 2021 Oliver Freyermuth <o.freyermuth@googlemail.com> 202102220000-1
- Add efinet module only on *-efi platforms.

* Mon Jan 25 2021 Oliver Freyermuth <o.freyermuth@googlemail.com> 202102211600-1
- Add efinet module to Grub2 modules.
- Set prefix "grub2" in generated Grub2.

* Fri Apr 17 2020 Lukas Zapletal <lzap+rpm@redhat.com> 202005201200-1
- BZ#1702434 - unmanaged files and permissions

* Tue Apr 07 2020 Zach Huntington-Meath <zhunting@redhat.com> - 201901011200-2
- Bump to release for EL8

* Wed Apr 24 2019 Lukas Zapletal <lzap+rpm@redhat.com> 201901011200-1
- Fix BZ#1702434

* Wed Mar 06 2019 Eric D. Helms <ericdhelms@gmail.com> - 201801241201-4
- Fix BZ#1672498

* Fri Feb 02 2018 Eric D. Helms <ericdhelms@gmail.com> 201801241201-2
- Fixes #22499 - fixed bootloader generator (lzap+git@redhat.com)

* Thu Jan 25 2018 Eric D. Helms <ericdhelms@gmail.com> 201801241201-1
- Foreman-bootloaders no longer ships binaries (lzap@teepee.home.lan)

* Mon Jul 17 2017 Eric D. Helms <ericdhelms@gmail.com> 201707171807-1
- Foreman-bootloaders rebase to 201707171807 (lzap+git@redhat.com)

* Mon Jun 19 2017 Eric D. Helms <ericdhelms@gmail.com> 201705231433-1
- new package built with tito

