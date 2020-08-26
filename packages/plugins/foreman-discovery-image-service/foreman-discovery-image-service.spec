Name: foreman-discovery-image-service
Version: 1.0.0
Release: 4%{?dist}
Summary: Metapackage with dependencies for FDI

Group: Applications/System
License: GPLv2+
URL: https://github.com/theforeman/foreman-discovery-image

# explicitly define, as we build on top of an scl, not inside with scl_package 
%{?scl:%global scl_prefix %{scl}-} 

Requires:	foreman-proxy
Requires:	%{?scl_prefix}rubygem-smart_proxy_discovery_image

%description
Metapackage with dependencies for FDI

%package tui
Summary: Metapackage with dependencies for FDI TUI
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(newt)
Requires: %{?scl_prefix}rubygem(fast_gettext)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby-devel
BuildRequires: %{?scl_prefix_ruby}rubygems-devel

%description tui
Metapackage with dependencies for FDI text-user interface

%prep

%build

%install

%files

%files tui

%changelog
* Wed Aug 26 2020 Lukas Zapletal <lzap+rpm@redhat.com - 1.0.0-4
- TUI requires SCL dependencies

* Mon May 11 2020 Zach Huntington-Meath - 1.0.0-3
- Add scl macro to FDI dependency

* Thu Jan 16 2020 Evgeni Golov - 1.0.0-2
- Depend on SCL'ed FDI plugin package

* Wed Aug 15 2018 Lukas Zapletal <lzap+rpm@redhat.com> 1.0.0-1
- Initial version
