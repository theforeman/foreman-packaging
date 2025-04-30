%define debug_package %{nil}

# https://github.com/theforeman/foreman_ygg_worker

%global repo_orgname theforeman
%global repo_name foreman_ygg_worker
%global yggdrasil_libexecdir %{_libexecdir}/yggdrasil
%global yggdrasil_worker_conf_dir %{_sysconfdir}/yggdrasil/workers

%global goipath         github.com/%{repo_orgname}/%{repo_name}

%if 0%{?suse_version}
%define gobuild(o:) GO111MODULE=off go build -buildmode pie -compiler gc -tags="rpm_crashtraceback ${BUILDTAGS:-}" -ldflags "${LDFLAGS:-} -linkmode=external -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n') -extldflags '-Wl,-z,relro -Wl,-z,now '" -a -v %{?**};
%endif

Name: foreman_ygg_worker
Version: 0.3.1
Summary: Worker service for yggdrasil that can act as pull client for Foreman Remote Execution
Release: 1%{?dist}
License: MIT

Source0: https://github.com/%{repo_orgname}/%{repo_name}/releases/download/v%{version}/%{repo_name}-%{version}.tar.gz
Url: https://github.com/%{repo_orgname}/%{repo_name}/

# suse leap 15.5 doesn't define go_arches
%if 0%{?suse_version}
%define go_arches %{ix86} x86_64 %{arm} aarch64 ppc64le
%endif
ExclusiveArch: %{go_arches}

BuildRequires: systemd-rpm-macros
%if 0%{?suse_version}
BuildRequires: go
BuildRequires: golang-packaging
%else
BuildRequires: golang
%if 0%{?rhel} >= 9 || 0%{?fedora}
BuildRequires: go-rpm-macros
%else
%if 0%{?rhel} == 8
BuildRequires: go-srpm-macros
%endif
%endif
%endif

Requires: (yggdrasil >= 0.2 with yggdrasil < 0.5)

%description
Worker service for yggdrasil that can act as pull client for Foreman Remote Execution.

%prep
%setup -q

%build
mkdir -p _gopath/src
cp -av $(pwd)/src _gopath/src/%{name}-%{version}
ln -fs $(pwd)/vendor _gopath/src/%{name}-%{version}/vendor
ln -fs $(pwd)/go.mod _gopath/src/%{name}-%{version}/go.mod
export GOPATH=$(pwd)/_gopath
pushd _gopath/src/%{name}-%{version}
%gobuild -o %{name}-%{version}
strip %{name}-%{version}
popd
make data LIBEXECDIR=%{yggdrasil_libexecdir}

%install
install -D -m 755 _gopath/src/%{name}-%{version}/%{name}-%{version} %{buildroot}%{yggdrasil_libexecdir}/%{name}
install -D -d -m 755 %{buildroot}%{yggdrasil_worker_conf_dir}
install -D -m 644 build/data/com.redhat.Yggdrasil1.Worker1.foreman.conf %{buildroot}%{_datadir}/dbus-1/system.d/com.redhat.Yggdrasil1.Worker1.foreman.conf
install -D -m 644 data/dbus_com.redhat.Yggdrasil1.Worker1.foreman.service %{buildroot}%{_datadir}/dbus-1/system-services/com.redhat.Yggdrasil1.Worker1.foreman.service
install -D -m 644 build/data/com.redhat.Yggdrasil1.Worker1.foreman.service %{buildroot}%{_unitdir}/com.redhat.Yggdrasil1.Worker1.foreman.service

cat <<EOF >%{buildroot}%{yggdrasil_worker_conf_dir}/foreman.toml
exec = "%{yggdrasil_libexecdir}/%{name}"
protocol = "grpc"
env = []
EOF

%files
%if 0%{?suse_version}
%dir %{yggdrasil_libexecdir}
%dir %{_sysconfdir}/yggdrasil
%dir %{yggdrasil_worker_conf_dir}
%endif
%{yggdrasil_libexecdir}/%{name}
%{yggdrasil_worker_conf_dir}/foreman.toml
%{_datadir}/dbus-1/system.d/com.redhat.Yggdrasil1.Worker1.foreman.conf
%{_datadir}/dbus-1/system-services/com.redhat.Yggdrasil1.Worker1.foreman.service
%{_unitdir}/com.redhat.Yggdrasil1.Worker1.foreman.service
%license LICENSE
%doc README.md

%changelog
* Wed Apr 30 2025 Odilon Sousa <osousa@redhat.com> - 0.3.1-1
- Release foreman_ygg_worker 0.3.1

* Thu Jan 16 2025 Adam Ruzicka <aruzicka@redhat.com> - 0.3.0-2
- Make it build on EL10

* Wed Sep 25 2024 Adam Ruzicka <aruzicka@redhat.com> - 0.3.0-1
- Release 0.3.0

* Wed Sep 11 2024 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 0.2.2-4
- Narrow yggdrasil version requirement

* Thu Aug 01 2024 Markus Bucher <bucher@atix.de> - 0.2.2-3
- Fixes for opensuse build service
- Require go and disable hardened go linker on SLES

* Fri Nov 10 2023 Bernhard Suttner <suttner@atix.de> - 0.2.2-2
- Fix build on CentOS 9-stream

* Fri Oct 13 2023 Eric D. Helms <ericdhelms@gmail.com> - 0.2.2-1
- Release 0.2.2

* Thu Sep 21 2023 Adam Ruzicka <aruzicka@redhat.com> - 0.2.1-1
- Bump version to 0.2.1

* Thu Nov 10 2022 Adam Ruzicka <aruzicka@redhat.com> - 0.2.0-1
- Bump version to 0.2.0

* Mon Oct 10 2022 Adam Ruzicka <aruzicka@redhat.com> - 0.1.1-2
- Bump version to 0.1.1

* Tue Sep 13 2022 Adam Ruzicka <aruzicka@redhat.com> - 0.1.1-1
- Bump version to 0.1.1

* Fri May 13 2022 Adam Ruzicka <aruzicka@redhat.com> - 0.1.0-1
- Bump version to 0.1.0

* Wed Oct 13 2021 Adam Ruzicka <aruzicka@redhat.com> - 0.0.3-1
- Initial packaging of 0.0.3
