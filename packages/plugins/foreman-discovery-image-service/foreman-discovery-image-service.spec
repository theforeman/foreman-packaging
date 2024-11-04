Name: foreman-discovery-image-service
Version: 1.0.0
Release: 5%{?dist}
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
Requires: ruby
Requires: ruby(rubygems)
Requires: rubygem(newt)
Requires: rubygem(fast_gettext)
BuildRequires: ruby(release)
BuildRequires: ruby-devel
BuildRequires: rubygems-devel

%description tui
Metapackage with dependencies for FDI text-user interface

%prep

%build

%install

%files

%files tui

%changelog
* Wed Sep 25 2024 Leos Stejskal <lstejska@redhat.com - 1.0.0-5
- Update spec file

* Wed Aug 26 2020 Lukas Zapletal <lzap+rpm@redhat.com - 1.0.0-4
- TUI requires SCL dependencies

* Mon May 11 2020 Zach Huntington-Meath - 1.0.0-3
- Add scl macro to FDI dependency

* Thu Jan 16 2020 Evgeni Golov - 1.0.0-2
- Depend on SCL'ed FDI plugin package

* Wed Aug 15 2018 Lukas Zapletal <lzap+rpm@redhat.com> 1.0.0-1
- Initial version
