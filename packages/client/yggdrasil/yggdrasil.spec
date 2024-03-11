%define debug_package %{nil}

Name:    yggdrasil
Version: 0.2.3
Release: 2%{?dist}
Summary: Message dispatch agent for cloud-connected systems
%if 0%{?suse_version}
License: GPL-3.0-only
%else
License: GPLv3
%endif
URL:     https://github.com/redhatinsights/yggdrasil

Source0: https://github.com/redhatinsights/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz

Patch0:  Use-gzip-c-instead-of-k.patch
Patch1:  build-Remove-the-Makefile-preamble.patch
Patch2:  Propagate-FOREMAN_REX_WORKDIR-to-workers.patch

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

Requires: subscription-manager

%description
%{name} is pair of utilities that register systems with RHSM and establishes
a receiving queue for instructions to be sent to the system via a broker.

%prep
%autosetup -p1

%global ldflags %{expand:-linkmode=external -compressdwarf=false -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n') -extldflags '%__global_ldflags'}
%global buildflags %{expand:-compiler gc -buildmode pie -tags=\\"rpm_crashtraceback libtrust_openssl\\" -ldflags \\"%ldflags\\" -a -v -x %{?**}}

%build
CGO_CPPFLAGS="-D_FORTIFY_SOURCE=2 -fstack-protector-all"  \
BUILDFLAGS="%buildflags" \
make PREFIX=%{_prefix} \
     SYSCONFDIR=%{_sysconfdir} \
     LOCALSTATEDIR=%{_localstatedir} \
     SHORTNAME=%{name} \
     LONGNAME=%{name} \
     PKGNAME=%{name} \
     VERSION=%{version}

%install
CGO_CPPFLAGS="-D_FORTIFY_SOURCE=2 -fstack-protector-all"  \
BUILDFLAGS="%buildflags" \
make PREFIX=%{_prefix} \
     SYSCONFDIR=%{_sysconfdir} \
     LOCALSTATEDIR=%{_localstatedir} \
     DESTDIR=%{buildroot} \
     SHORTNAME=%{name} \
     LONGNAME=%{name} \
     PKGNAME=%{name} \
     VERSION=%{version} \
     install

%files
%if 0%{?suse_version}
%dir %{_sysconfdir}/%{name}
%endif
%doc README.md
%{_bindir}/%{name}
%{_sbindir}/%{name}d
%config(noreplace) %{_sysconfdir}/%{name}/config.toml
%{_unitdir}/%{name}d.service
%{_datadir}/bash-completion/completions/*
%{_mandir}/man1/*
%{_prefix}/share/pkgconfig/%{name}.pc
%{_libexecdir}/%{name}

%changelog
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
