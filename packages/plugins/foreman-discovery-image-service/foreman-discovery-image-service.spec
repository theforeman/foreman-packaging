Name: foreman-discovery-image-service
Version: 1.0.0
Release: 3%{?dist}
Summary: Metapackage with dependencies for FDI

Group: Applications/System
License: GPLv2+
URL: https://github.com/theforeman/foreman-discovery-image

Requires:	foreman-proxy
%if 0%{?rhel} == 7
Requires:	tfm-rubygem-smart_proxy_discovery_image
%else
Requires:	rubygem-smart_proxy_discovery_image
%endif

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
* Mon May 11 2020 Zach Huntington-Meath - 1.0.0-3
- Add scl macro to FDI dependency

* Thu Jan 16 2020 Evgeni Golov - 1.0.0-2
- Depend on SCL'ed FDI plugin package

* Wed Aug 15 2018 Lukas Zapletal <lzap+rpm@redhat.com> 1.0.0-1
- Initial version
