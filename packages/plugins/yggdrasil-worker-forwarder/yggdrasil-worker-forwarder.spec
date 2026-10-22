%define debug_package %{nil}

# EL7 doesn't define gobuild (it is available in go-srpm-macros which is EL8+)
%if ! 0%{?gobuild:1}
%define gobuild(o:) GO111MODULE=off go build -buildmode pie -compiler gc -tags="rpm_crashtraceback ${BUILDTAGS:-}" -ldflags "${LDFLAGS:-} -linkmode=external -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n') -extldflags '-Wl,-z,relro -Wl,-z,now -specs=/usr/lib/rpm/redhat/redhat-hardened-ld '" -a -v %{?**};
%endif

Name: yggdrasil-worker-forwarder
Version: 0.2.1
Summary: Worker service for Yggdrasil that can forward requests to an API endpoint
Release: 1%{?dist}
License: GPLv3

Source0: https://github.com/theforeman/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1: %{name}.sysusers
Url: https://github.com/theforeman/%{name}/

# EL7 doesn't define go_arche (it is available in go-srpm-macros which is EL8+)s
%if ! 0%{?go_arches:1}
%define go_arches %{ix86} x86_64 %{arm} aarch64 ppc64le
%endif
ExclusiveArch: %{go_arches}

BuildRequires: golang
BuildRequires: go-srpm-macros
BuildRequires: go-rpm-macros
BuildRequires: make
BuildRequires: systemd-rpm-macros
%if 0%{?rhel} >= 9
%{?sysusers_requires_compat}
%endif

%description
Worker service for Yggdrasil that can forward requests to an API endpoint

%prep
%autosetup

%build
%if 0%{?rhel} == 7
mkdir -p _gopath/src/%{name}-%{version}
cp -rf $(pwd)/*.go _gopath/src/%{name}-%{version}
cp -rf $(pwd)/vendor _gopath/src/%{name}-%{version}
export GOPATH=$(pwd)/_gopath
pushd _gopath/src/%{name}-%{version}
%{gobuild}
strip %{name}-%{version}
cp %{name}-%{version} %{_builddir}/%{name}-%{version}/%{name}
popd
%else
export GO111MODULE=on
%{gobuild -o %{name} .}
%endif
make data LIBEXECDIR=%{_libexecdir}

%install
mkdir -p %{buildroot}%{_libexecdir}
%{__install} -m 755 %{_builddir}/%{name}-%{version}/%{name} %{buildroot}/%{_libexecdir}
%{__install} -D -m 644 _build/data/com.redhat.Yggdrasil1.Worker1.foreman_rh_cloud.conf %{buildroot}%{_datadir}/dbus-1/system.d/com.redhat.Yggdrasil1.Worker1.foreman_rh_cloud.conf
%{__install} -D -m 644 data/dbus_com.redhat.Yggdrasil1.Worker1.foreman_rh_cloud.service %{buildroot}%{_datadir}/dbus-1/system-services/com.redhat.Yggdrasil1.Worker1.foreman_rh_cloud.service
%{__install} -D -m 644 _build/data/com.redhat.Yggdrasil1.Worker1.foreman_rh_cloud.service %{buildroot}%{_unitdir}/com.redhat.Yggdrasil1.Worker1.foreman_rh_cloud.service
install -d %{buildroot}%{_sysconfdir}/rhc/workers
%if 0%{?rhel} >= 9
install -D -m 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/%{name}.conf
%endif

%if 0%{?rhel} >= 9
%pre
%sysusers_create_compat %{SOURCE1}
%endif

%files
%{_libexecdir}/%{name}
%{_datadir}/dbus-1/system.d/com.redhat.Yggdrasil1.Worker1.foreman_rh_cloud.conf
%{_datadir}/dbus-1/system-services/com.redhat.Yggdrasil1.Worker1.foreman_rh_cloud.service
%{_unitdir}/com.redhat.Yggdrasil1.Worker1.foreman_rh_cloud.service
%if 0%{?rhel} >= 9
%{_sysusersdir}/%{name}.conf
%endif
%dir %{_sysconfdir}/rhc
%dir %{_sysconfdir}/rhc/workers
%license LICENSE
%doc README.md

%changelog
* Thu Oct 22 2026 Odilon Sousa <osousa@redhat.com> - 0.2.1-1
- Update to 0.2.1 with grpc-go 1.82.2 (CVE-2026-84445)
- Provision the yggdrasil-worker group on EL9+ for D-Bus activation

* Tue Sep 08 2026 Odilon Sousa <osousa@redhat.com> - 0.1.0-2
- Rebuild against new golang version

* Fri Jul 31 2026 Zach Huntington-Meath <zhunting@redhat.com> - 0.1.0-1
- Release yggdrasil-worker-forwarder 0.1.0

* Thu Jul 02 2026 Eric D. Helms <ericdhelms@gmail.com> - 0.0.4-1
- Release yggdrasil-worker-forwarder 0.0.4

* Mon Oct 16 2023 Eric D. Helms <ericdhelms@gmail.com> - 0.0.3-1
- Release 0.0.3

* Tue Apr 05 2022 Eric D. Helms <ericdhelms@gmail.com> - 0.0.1-1
- Release 0.0.1

