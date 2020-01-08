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
%global foreman_proxy_statedir %{_root_localstatedir}/foreman-proxy
%global foreman_proxy_bundlerd_dir %{foreman_proxy_dir}/bundler.d
%global foreman_proxy_settingsd_dir %{_root_sysconfdir}/foreman-proxy/settings.d
%global smart_proxy_dynflow_bundlerd_dir %{!?scl:/opt/theforeman/tfm/root}%{_datadir}/smart_proxy_dynflow_core/bundler.d

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.0.15
Release: 2%{?foremandist}%{?dist}
Summary: Infoblox DHCP provider plugin for Foreman's smart proxy
Group: Applications/Internet
License: GPLv3
URL: https://github.com/theforeman/smart_proxy_dhcp_infoblox
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: foreman-proxy >= %{foreman_proxy_min_version}
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(infoblox) >= 3.0
Requires: %{?scl_prefix}rubygem(infoblox) < 4
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-proxy-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

%description
Infoblox DHCP provider plugin for Foreman's smart proxy.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

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
