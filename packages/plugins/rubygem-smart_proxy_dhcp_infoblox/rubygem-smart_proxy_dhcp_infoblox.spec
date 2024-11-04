# template: smart_proxy_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%{!?_root_datadir:%global _root_datadir %{_datadir}}
%{!?_root_localstatedir:%global _root_localstatedir %{_localstatedir}}
%{!?_root_sysconfdir:%global _root_sysconfdir %{_sysconfdir}}

%global gem_name smart_proxy_dhcp_infoblox
%global plugin_name dhcp_infoblox

%global foreman_proxy_min_version 1.25
%global foreman_proxy_dir %{_root_datadir}/foreman-proxy
%global foreman_proxy_statedir %{_root_localstatedir}/lib/foreman-proxy
%global foreman_proxy_bundlerd_dir %{foreman_proxy_dir}/bundler.d
%global foreman_proxy_settingsd_dir %{_root_sysconfdir}/foreman-proxy/settings.d

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.0.18
Release: 1%{?foremandist}%{?dist}
Summary: Infoblox DHCP provider plugin for Foreman's smart proxy
Group: Applications/Internet
License: GPLv3
URL: https://github.com/theforeman/smart_proxy_dhcp_infoblox
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: foreman-proxy >= %{foreman_proxy_min_version}
Requires: ruby >= 2.5
BuildRequires: ruby >= 2.5
BuildRequires: rubygems-devel
BuildArch: noarch
Provides: foreman-proxy-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

%{?scl:Obsoletes: rubygem-%{gem_name} < %{version}-%{release}}

%description
Infoblox DHCP provider plugin for Foreman's smart proxy.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%{?scl:Obsoletes: rubygem-%{gem_name}-doc < %{version}-%{release}}

%description doc
Documentation for %{name}.

%prep
%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} - << \EOF}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:EOF}

%build
# Create the gem as gem install only works on a gem file
%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%{?scl:EOF}

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%{?scl:scl enable %{scl} - << \EOF}
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

# bundler file
mkdir -p %{buildroot}%{foreman_proxy_bundlerd_dir}
mv %{buildroot}%{gem_instdir}/bundler.d/%{plugin_name}.rb \
   %{buildroot}%{foreman_proxy_bundlerd_dir}

# sample config
mkdir -p %{buildroot}%{foreman_proxy_settingsd_dir}
mv %{buildroot}%{gem_instdir}/config/dhcp_infoblox.yml.example \
   %{buildroot}%{foreman_proxy_settingsd_dir}/dhcp_infoblox.yml

%files
%dir %{gem_instdir}
%config(noreplace) %attr(0640, root, foreman-proxy) %{foreman_proxy_settingsd_dir}/dhcp_infoblox.yml
%license %{gem_instdir}/LICENSE
%{gem_instdir}/config
%{gem_libdir}
%{foreman_proxy_bundlerd_dir}/%{plugin_name}.rb
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/test

%changelog
* Tue Mar 19 2024 Foreman Packaging Automation <packaging@theforeman.org> - 0.0.18-1
- Update to 0.0.18

* Sun Sep 25 2022 Foreman Packaging Automation <packaging@theforeman.org> 0.0.17-1
- Update to 0.0.17

* Mon May 09 2022 Eric D. Helms <ericdhelms@gmail.com> - 0.0.16-7
- Drop unused smart_proxy_dynflow_core_bundlerd_dir macro

* Mon Jan 10 2022 Evgeni Golov - 0.0.16-6
- use versioned obsoletes for proxy plugins

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.0.16-5
- Rebuild for Ruby 2.7

* Mon Jun 22 2020 Evgeni Golov - 0.0.16-4
- Fix bundler.d location on EL8

* Tue May 26 2020 Adam Ruzicka <aruzicka@redhat.com> 0.0.16-3
- Move local state to /var/lib

* Tue May 12 2020 Adam Ruzicka <aruzicka@redhat.com> 0.0.16-2
- Change localstatedir to sharedstatedir

* Mon May 04 2020 Lukas Zapletal <lzap+rpm@redhat.com> - 0.0.16-1
- Update to 0.0.16

* Tue Jan 07 2020 Eric D. Helms <ericdhelms@gmail.com> - 0.0.15-3
- Build for SCL

* Thu Sep 26 2019 Eric D. Helms <ericdhelms@gmail.com> - 0.0.15-2
- Update to SCL based template

* Fri Aug 30 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.0.15-1
- Update to 0.0.15-1

* Wed Dec 12 2018 Lukas Zapletal <lzap+rpm@redhat.com> 0.0.14-1
- New upstream version

* Fri Apr 27 2018 Dmitri Dolguikh <dmitri@appliedlogic.ca> 0.0.13-1
- Update to 0.0.13

* Thu Feb 22 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.0.12-1
- Updated rubygem-smart_proxy_dhcp_infoblox to 0.0.12 (dmitri@appliedlogic.ca)
- Restructure plugin packages to prepare for obal (pcreech@redhat.com)

* Tue Jan 16 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.0.10-1
- Updated smart_proxy_dhcp_infoblox to 0.0.10 (dmitri@appliedlogic.ca)

* Wed Sep 27 2017 Daniel Lobato Garcia <me@daniellobato.me> 0.0.8-1
- Updated smart_proxy_dhcp_infoblox to 0.0.8 (witlessbird@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Thu Sep 14 2017 Daniel Lobato Garcia <me@daniellobato.me> 0.0.7-1
- Updated smart_proxy_dhcp_infoblox to 0.0.7 (witlessbird@gmail.com)

* Wed Jul 12 2017 Eric D. Helms <ericdhelms@gmail.com> 0.0.6-1
- Update smart_proxy_dhcp_infoblox to 0.0.6 (dmitri@appliedlogic.ca)

* Tue Sep 13 2016 Dominic Cleal <dominic@cleal.org> 0.0.5-1
- new package built with tito
