%define debug_package %{nil}

%global go_arches x86_64 s390x ppc64le

Name:    dynflow-utils
Version: 1.6.3
Release: 1%{?dist}
Summary: Supplemental Dynflow utilities
License: GPLv3
URL:     https://github.com/dynflow/dynflow

Source0: https://github.com/dynflow/dynflow/releases/download/v%{version}/dynflow-expand-%{version}.tar.gz

ExclusiveArch: %{go_arches}

BuildRequires: git
BuildRequires: golang

%description
A collection of supplemental utilities useful when dealing with Dynflow.

%prep
%setup -n dynflow-expand-%{version}

%build
go build -o dynflow-expand

cat <<SCRIPT >psql-msgpack-decode
#!/bin/sh

psql "\$@" | %{_libexecdir}/dynflow-expand
SCRIPT

%install
install -D -m755 psql-msgpack-decode %{buildroot}%{_libexecdir}/psql-msgpack-decode
install -D -m755 dynflow-expand %{buildroot}%{_libexecdir}/dynflow-expand

%files
%doc README.md
%{_libexecdir}/psql-msgpack-decode
%{_libexecdir}/dynflow-expand

%changelog
* Thu Jan 20 2022 Adam Ruzicka <aruzicka@redhat.com> - 1.6.3-1
- Initial release
