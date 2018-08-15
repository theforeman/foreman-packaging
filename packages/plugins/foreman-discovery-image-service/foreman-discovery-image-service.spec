Name: foreman-discovery-image-service
Version: 1.0.0
Release: 1%{?dist}
Summary: Metapackage with dependencies for FDI

Group: Applications/System
License: GPLv2+
URL: https://github.com/theforeman/foreman-discovery-image

Requires:	foreman-proxy
Requires:	rubygem-smart_proxy_discovery_image

%description
Metapackage with dependencies for FDI

%package tui
Summary: Metapackage with dependencies for FDI TUI
Requires: ruby(release)
Requires: rubygem(newt)
Requires: rubygem(fast_gettext)

%description tui
Metapackage with dependencies for FDI text-user interface

%prep

%build

%install

%files

%files tui

%changelog
* Wed Aug 15 2018 Lukas Zapletal <lzap+rpm@redhat.com> 1.0.0-1
- Initial version
