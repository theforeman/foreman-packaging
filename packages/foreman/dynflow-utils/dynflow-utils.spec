%define debug_package %{nil}

Name:    dynflow-utils
Version: 2.0.1
Release: 2%{?dist}
Summary: Supplemental Dynflow utilities
License: GPLv3
URL:     https://github.com/dynflow/dynflow

Source0: https://github.com/dynflow/dynflow/releases/download/v%{version}/dynflow-expand-%{version}.tar.gz

ExclusiveArch: %{golang_arches}

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
* Wed Jul 29 2026 Zach Huntington-Meath <zhunting@redhat.com> - 2.0.1-2
- Rebuild for EL10

* Tue Apr 28 2026 Adam Ruzicka <aruzicka@redhat.com> - 2.0.1-1
- Rebuild with newer go 

* Sun Nov 30 2025 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.6.3-2
- Use OS provided golang_arches macro

* Thu Jan 20 2022 Adam Ruzicka <aruzicka@redhat.com> - 1.6.3-1
- Initial release
