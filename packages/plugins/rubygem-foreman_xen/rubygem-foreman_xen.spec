# This package contains macros that provide functionality relating to
# Software Collections. These macros are not used in default
# Fedora builds, and should not be blindly copied or enabled.
# Specifically, the "scl" macro must not be defined in official Fedora
# builds. For more information, see:
# http://docs.fedoraproject.org/en-US/Fedora_Contributor_Documentation
# /1/html/Software_Collections_Guide/index.html

%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_xen
%global plugin_name xen

%global foreman_dir /usr/share/foreman
%global foreman_bundlerd_dir %{foreman_dir}/bundler.d
%global foreman_pluginconf_dir %{foreman_dir}/config/settings.plugins.d

Summary:    Provision and manage XEN Server from Foreman
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    0.5.2
Release:    2%{?foremandist}%{?dist}
Group:      Applications/System
License:    GPLv3
URL:        https://github.com/theforeman/foreman-xen
Source0:    https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires:   foreman >= 1.13.0

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}rubygems
Requires: %{?scl_prefix}rubygem(fog-xenserver) >= 0.2.0
Requires: %{?scl_prefix}rubygem(fog-xenserver) < 1.0.0

BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems
BuildRequires: foreman-plugin >= 1.13.0
BuildRequires: foreman-assets
BuildRequires: %{?scl_prefix}rubygem(fog-xenserver) >= 0.2.0
BuildRequires: %{?scl_prefix}rubygem(fog-xenserver) < 1.0.0

BuildArch: noarch

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-%{plugin_name}
Provides: foreman-xen
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
This plugin enables provisioning and managing XEN Server in Foreman.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%{?scl:scl enable %{scl} - << \EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

%foreman_bundlerd_file
%foreman_precompile_plugin -s

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/LICENSE
%{gem_instdir}/app
%{gem_instdir}/config
%{gem_instdir}/lib
%{gem_instdir}/locale
%{gem_spec}
%{foreman_bundlerd_plugin}
%{foreman_assets_plugin}
%{gem_instdir}/public/assets/compute_resources/xenserver

%exclude %{gem_cache}
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/test

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.md

%changelog
* Wed Jan 10 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.5.2-2
- Bump Foreman plugins release (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Wed May 24 2017 Dominic Cleal <dominic@cleal.org> 0.5.2-1
- update foreman_xen to 0.5.2 (kvedulv@kvedulv.de)

* Fri Mar 03 2017 Dominic Cleal <dominic@cleal.org> 0.5.1-1
- update foreman_xen to 0.5.1 (kvedulv@kvedulv.de)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Tue Jan 03 2017 Dominic Cleal <dominic@cleal.org> 0.4.1-1
- update foreman_xen to 0.4.1 (kvedulv@kvedulv.de)

* Wed Nov 02 2016 Dominic Cleal <dominic@cleal.org> 0.4.0-1
- update foreman_xen to 0.4.0 (kvedulv@kvedulv.de)

* Wed Aug 31 2016 Dominic Cleal <dominic@cleal.org> 0.3.1-1
- update foreman_xen to 0.3.1 (kvedulv@kvedulv.de)

* Mon Feb 29 2016 Dominic Cleal <dominic@cleal.org> 0.3.0-1
- update foreman_xen to 0.3.0 (kvedulv@kvedulv.de)

* Mon Jan 18 2016 Dominic Cleal <dcleal@redhat.com> 0.2.4-1
- update foreman_xen to 0.2.4 (kvedulv@kvedulv.de)

* Thu Dec 24 2015 Dominic Cleal <dcleal@redhat.com> 0.2.3-2
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Wed Nov 18 2015 Dominic Cleal <dcleal@redhat.com> 0.2.3-1
- update foreman_xen to 0.2.3 (kvedulv@kvedulv.de)

* Tue Nov 10 2015 Dominic Cleal <dcleal@redhat.com> 0.2.2-1
- update foreman_xen to 0.2.2 (kvedulv@kvedulv.de)
- Add foremandist macro (dcleal@redhat.com)

* Tue Oct 20 2015 Dominic Cleal <dcleal@redhat.com> 0.2.1-1
- update foreman_xen to 0.2.1 (kvedulv@kvedulv.de)

* Mon Sep 21 2015 Dominic Cleal <dcleal@redhat.com> 0.1.3-1
- update foreman_xen to 0.1.3 (kvedulv@kvedulv.de)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 0.1.2-2
- Converted to tfm SCL (dcleal@redhat.com)

* Fri Jul 31 2015 Dominic Cleal <dcleal@redhat.com> 0.1.2-1
- update foreman_xen to 0.1.2 (kvedulv@kvedulv.de)

* Wed May 27 2015 Dominic Cleal <dcleal@redhat.com> 0.1.1-1
- update foreman_xen to 0.1.1 (kvedulv@kvedulv.de)

* Wed May 20 2015 Dominic Cleal <dcleal@redhat.com> 0.1.0-1
- update foreman_xen to 0.1.0 (kvedulv@kvedulv.de)

* Wed May 13 2015 Dominic Cleal <dcleal@redhat.com> 0.0.6-1
- update foreman_xen to 0.0.6 (kvedulv@kvedulv.de)

* Fri Jan 02 2015 Dominic Cleal <dcleal@redhat.com> 0.0.5.1-1
- Update foreman_xen to 0.0.5.1 (dcleal@redhat.com)

* Thu Dec 18 2014 Dominic Cleal <dcleal@redhat.com> 0.0.5-1
- Update foreman_xen to 0.0.5 (dcleal@redhat.com)

* Fri Nov 21 2014 Dominic Cleal <dcleal@redhat.com> 0.0.4.1-1
- Update to 0.0.4.1 (dcleal@redhat.com)

* Wed Jul 02 2014 Dominic Cleal <dcleal@redhat.com> 0.0.3-1
- Update to 0.0.3 (dcleal@redhat.com)

* Mon Jun 16 2014 Dominic Cleal <dcleal@redhat.com> 0.0.2-1
- Update to 0.0.2 (dcleal@redhat.com)

* Wed May 21 2014 Dominic Cleal <dcleal@redhat.com> 0.0.1-1
- new package built with tito
