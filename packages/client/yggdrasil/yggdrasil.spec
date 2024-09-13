%define debug_package %{nil}

Name:    yggdrasil
Version: 0.4.1
Release: 1%{?dist}
Summary: Message dispatch agent for cloud-connected systems
License: GPL-3.0-only
URL:     https://github.com/redhatinsights/yggdrasil

Source0: https://github.com/redhatinsights/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz

# EL7 doesn't define go_arches
%if ! 0%{?go_arches:1}
%define go_arches %{ix86} x86_64 %{arm} aarch64 ppc64le
%endif
ExclusiveArch: %{go_arches}

BuildRequires: git
%if 0%{?suse_version}
BuildRequires: dbus-1-devel
BuildRequires: go
# see https://lists.opensuse.org/archives/list/bugs@lists.opensuse.org/message/Q5R6VVHE5ZCP75XI3MB2B7EXNWXAY2P4/
BuildRequires: systemd
%else
BuildRequires: dbus-devel
BuildRequires: golang
%endif
BuildRequires: systemd-devel
BuildRequires: systemd-rpm-macros
BuildRequires: meson
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(systemd)
BuildRequires: pkgconfig(bash-completion)


%description
%{name} is pair of utilities that register systems with RHSM and establishes
a receiving queue for instructions to be sent to the system via a broker.

%prep
%autosetup -p1

%global ldflags %{expand:-linkmode=external -compressdwarf=false -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n') -extldflags '%__global_ldflags'}
%global buildflags %{expand:-compiler gc -buildmode pie -tags=\\"rpm_crashtraceback libtrust_openssl\\" -ldflags \\"%ldflags\\" -a -v -x %{?**}}

%build
%meson "-Dgobuildflags=%buildflags" %ldflags
%meson_build

%global gosupfiles ./ipc/com.redhat.Yggdrasil1.Dispatcher1.xml ./ipc/com.redhat.Yggdrasil1.Worker1.xml
%install
%meson_install

%files
%if 0%{?suse_version}
%dir %{_sysconfdir}/%{name}
%endif
%doc README.md
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/%{name}
%{_unitdir}/*
%{_userunitdir}/*
%{_datadir}/bash-completion/completions/*
%{_datadir}/dbus-1/{interfaces,system-services,system.d}/*
%{_datadir}/doc/%{name}/*
%{_mandir}/man1/*

%changelog
* Thu Aug 29 2024 Adam Ruzicka <aruzicak@redhat.com> - 0.4.1-1
- Fixes for opensuse build service

* Mon Mar 11 2024 Markus Bucher <bucher@atix.de> - 0.2.3-2
- Fixes for opensuse build service
- Require go on SLES

* Wed Oct 18 2023 Adam Ruzicka <aruzicka@redhat.com> - 0.2.3-1
- Bump version to 0.2.3

* Tue Sep 19 2023 Adam Ruzicka <aruzicka@redhat.com> - 0.2.0-3
- Pass FOREMAN_REX_WORKDIR env var to the workers

* Mon Feb 21 2022 Adam Ruzicka <aruzicka@redhat.com> - 0.2.0-2
- Standardize go_arches

* Mon Oct 18 2021 Adam Ruzicka <aruzicka@redhat.com> - 0.2.0-1
- Initial release
