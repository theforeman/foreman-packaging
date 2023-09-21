%define debug_package %{nil}

# https://github.com/theforeman/foreman_ygg_worker

%global repo_orgname theforeman
%global repo_name foreman_ygg_worker
%global yggdrasil_libexecdir %{_libexecdir}/yggdrasil
%{!?_root_sysconfdir:%global _root_sysconfdir %{_sysconfdir}}
%global yggdrasil_worker_conf_dir %{_root_sysconfdir}/yggdrasil/workers

%global goipath         github.com/%{repo_orgname}/%{repo_name}

%if 0%{?rhel} > 7 && ! 0%{?fedora}
%define gobuild(o:) \
        go build -buildmode pie -compiler gc -tags="rpm_crashtraceback libtrust_openssl ${BUILDTAGS:-}" -ldflags "${LDFLAGS:-} -linkmode=external -compressdwarf=false -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n') -extldflags '%__global_ldflags'" -a -v %{?**};
%else
%if ! 0%{?gobuild:1}
%define gobuild(o:) GO111MODULE=off go build -buildmode pie -compiler gc -tags="rpm_crashtraceback ${BUILDTAGS:-}" -ldflags "${LDFLAGS:-} -linkmode=external -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n') -extldflags '-Wl,-z,relro -Wl,-z,now -specs=/usr/lib/rpm/redhat/redhat-hardened-ld '" -a -v %{?**};
%endif
%endif

Name: foreman_ygg_worker
Version: 0.2.1
Summary: Worker service for yggdrasil that can act as pull client for Foreman Remote Execution
Release: 1%{?dist}
License: MIT

Source0: https://github.com/%{repo_orgname}/%{repo_name}/releases/download/v%{version}/%{repo_name}-%{version}.tar.gz
Url: https://github.com/%{repo_orgname}/%{repo_name}/

# EL7 doesn't define go_arches
%if ! 0%{?go_arches:1}
%define go_arches %{ix86} x86_64 %{arm} aarch64 ppc64le
%endif
ExclusiveArch: %{go_arches}

BuildRequires: golang
Requires: yggdrasil

%description
Worker service for yggdrasil that can act as pull client for Foreman Remote Execution.

%prep
%setup -q

%build
mkdir -p _gopath/src
ln -fs $(pwd)/src _gopath/src/%{name}-%{version}
ln -fs $(pwd)/vendor _gopath/src/%{name}-%{version}/vendor
export GOPATH=$(pwd)/_gopath
pushd _gopath/src/%{name}-%{version}
%{gobuild}
strip %{name}-%{version}
popd

%install
install -D -m 755 _gopath/src/%{name}-%{version}/%{name}-%{version} %{buildroot}%{yggdrasil_libexecdir}/%{name}
install -D -d -m 755 %{buildroot}%{yggdrasil_worker_conf_dir}

cat <<EOF >%{buildroot}%{yggdrasil_worker_conf_dir}/foreman.toml
exec = "%{yggdrasil_libexecdir}/%{name}"
protocol = "grpc"
env = []
EOF

%files
%{yggdrasil_libexecdir}/%{name}
%{yggdrasil_worker_conf_dir}/foreman.toml
%license LICENSE
%doc README.md

%changelog
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
