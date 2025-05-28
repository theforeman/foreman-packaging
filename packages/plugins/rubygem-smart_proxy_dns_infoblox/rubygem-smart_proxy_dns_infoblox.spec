# template: smart_proxy_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%{!?_root_datadir:%global _root_datadir %{_datadir}}
%{!?_root_localstatedir:%global _root_localstatedir %{_localstatedir}}
%{!?_root_sysconfdir:%global _root_sysconfdir %{_sysconfdir}}

%global gem_name smart_proxy_dns_infoblox
%global plugin_name dns_infoblox

%global foreman_proxy_min_version 1.25
%global foreman_proxy_dir %{_root_datadir}/foreman-proxy
%global foreman_proxy_statedir %{_root_localstatedir}/lib/foreman-proxy
%global foreman_proxy_bundlerd_dir %{foreman_proxy_dir}/bundler.d
%global foreman_proxy_settingsd_dir %{_root_sysconfdir}/foreman-proxy/settings.d

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.2.0
Release: 1%{?foremandist}%{?dist}
Summary: Infoblox DNS provider plugin for Foreman's smart proxy
Group: Applications/Internet
License: GPLv3
URL: https://github.com/theforeman/smart_proxy_dns_infoblox
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
Infoblox DNS provider plugin for Foreman's smart proxy.


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
mv %{buildroot}%{gem_instdir}/config/dns_infoblox.yml.example \
   %{buildroot}%{foreman_proxy_settingsd_dir}/dns_infoblox.yml

%files
%dir %{gem_instdir}
%config(noreplace) %attr(0640, root, foreman-proxy) %{foreman_proxy_settingsd_dir}/dns_infoblox.yml
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
* Tue Jul 02 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.2.0-1
- Update to 1.2.0

* Mon May 09 2022 Eric D. Helms <ericdhelms@gmail.com> - 1.1.0-7
- Drop unused smart_proxy_dynflow_core_bundlerd_dir macro

* Mon Jan 10 2022 Evgeni Golov - 1.1.0-6
- use versioned obsoletes for proxy plugins

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.1.0-5
- Rebuild for Ruby 2.7

* Fri Jul 10 2020 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.1.0-4
- Add infoblox dependency back (#30367)

* Mon Jun 22 2020 Evgeni Golov - 1.1.0-3
- Fix bundler.d location on EL8

* Tue May 26 2020 Adam Ruzicka <aruzicka@redhat.com> 1.1.0-2
- Move local state to /var/lib

* Thu May 21 2020 Lukas Zapletal <lzap+rpm@redhat.com> 1.1.0-1
- Update to 1.1.0

* Tue May 12 2020 Adam Ruzicka <aruzicka@redhat.com> - 1.0.0-4
- Change localstatedir to sharedstatedir

* Tue Jan 07 2020 Eric D. Helms <ericdhelms@gmail.com> - 1.0.0-3
- Build for SCL

* Thu Sep 26 2019 Eric D. Helms <ericdhelms@gmail.com> - 1.0.0-2
- Update to SCL based template

* Thu Jul 25 2019 Lukas Zapletal <lzap+rpm@redhat.com> 1.0.0-1
- Updated to 1.0.0 upstream version

* Tue May 07 2019 Lukas Zapletal <lzap+rpm@redhat.com> 0.0.9-1
- Updated to 0.0.9 upstream version

* Wed Dec 12 2018 Lukas Zapletal <lzap+rpm@redhat.com> 0.0.7-1
- Bumped to match upstream version

* Mon Aug 14 2017 Eric D. Helms <ericdhelms@gmail.com> 0.0.6-1
- Update smart_proxy_dns_infoblox to 0.0.6 (dmitri@appliedlogic.ca)

* Mon Sep 12 2016 Dominic Cleal <dominic@cleal.org> 0.0.4-1
- new package built with tito
