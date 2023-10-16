%define debug_package %{nil}

# EL7 doesn't define gobuild (it is available in go-srpm-macros which is EL8+)
%if ! 0%{?gobuild:1}
%define gobuild(o:) GO111MODULE=off go build -buildmode pie -compiler gc -tags="rpm_crashtraceback ${BUILDTAGS:-}" -ldflags "${LDFLAGS:-} -linkmode=external -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n') -extldflags '-Wl,-z,relro -Wl,-z,now -specs=/usr/lib/rpm/redhat/redhat-hardened-ld '" -a -v %{?**};
%endif

Name: yggdrasil-worker-forwarder
Version: 0.0.3
Summary: Worker service for Yggdrasil that can forward requests to an API endpoint
Release: 1%{?dist}
License: GPLv3

Source0: https://github.com/theforeman/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Url: https://github.com/theforeman/%{name}/

# EL7 doesn't define go_arche (it is available in go-srpm-macros which is EL8+)s
%if ! 0%{?go_arches:1}
%define go_arches %{ix86} x86_64 %{arm} aarch64 ppc64le
%endif
ExclusiveArch: %{go_arches}

BuildRequires: golang

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
%{gobuild}
%endif

%install
mkdir -p %{buildroot}%{_libexecdir}
%{__install} -m 755 %{_builddir}/%{name}-%{version}/%{name} %{buildroot}/%{_libexecdir}

%files
%{_libexecdir}/%{name}
%license LICENSE
%doc README.md

%changelog
* Mon Oct 16 2023 Eric D. Helms <ericdhelms@gmail.com> - 0.0.3-1
- Release 0.0.3

* Tue Apr 05 2022 Eric D. Helms <ericdhelms@gmail.com> - 0.0.1-1
- Release 0.0.1

