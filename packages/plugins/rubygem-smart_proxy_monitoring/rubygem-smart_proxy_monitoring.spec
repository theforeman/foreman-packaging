# template: smart_proxy_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%{!?_root_datadir:%global _root_datadir %{_datadir}}
%{!?_root_localstatedir:%global _root_localstatedir %{_localstatedir}}
%{!?_root_sysconfdir:%global _root_sysconfdir %{_sysconfdir}}

%global gem_name smart_proxy_monitoring
%global plugin_name monitoring

%global foreman_proxy_min_version 1.25
%global foreman_proxy_dir %{_root_datadir}/foreman-proxy
%global foreman_proxy_statedir %{_root_localstatedir}/lib/foreman-proxy
%global foreman_proxy_bundlerd_dir %{foreman_proxy_dir}/bundler.d
%global foreman_proxy_settingsd_dir %{_root_sysconfdir}/foreman-proxy/settings.d

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.3.0
Release: 1%{?foremandist}%{?dist}
Summary: Monitoring plug-in for Foreman's smart proxy
Group: Applications/Internet
License: GPLv3
URL: https://github.com/theforeman/smart_proxy_monitoring
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: foreman-proxy >= %{foreman_proxy_min_version}
Requires: ruby >= 2.7
Requires: ruby < 4
BuildRequires: ruby >= 2.7
BuildRequires: ruby < 4
BuildRequires: rubygems-devel
BuildArch: noarch
Provides: foreman-proxy-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

%{?scl:Obsoletes: rubygem-%{gem_name} < %{version}-%{release}}

%description
Monitoring plug-in for Foreman's smart proxy.


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
mv %{buildroot}%{gem_instdir}/settings.d/monitoring.yml.example \
   %{buildroot}%{foreman_proxy_settingsd_dir}/monitoring.yml
mv %{buildroot}%{gem_instdir}/settings.d/monitoring_icinga2.yml.example \
   %{buildroot}%{foreman_proxy_settingsd_dir}/monitoring_icinga2.yml
mv %{buildroot}%{gem_instdir}/settings.d/monitoring_icingadirector.yml.example \
   %{buildroot}%{foreman_proxy_settingsd_dir}/monitoring_icingadirector.yml

# additional config
mkdir -p %{buildroot}%{_root_sysconfdir}/foreman-proxy/monitoring

%files
%dir %{gem_instdir}
%config(noreplace) %attr(0640, root, foreman-proxy) %{foreman_proxy_settingsd_dir}/monitoring.yml
%config(noreplace) %attr(0640, root, foreman-proxy) %{foreman_proxy_settingsd_dir}/monitoring_icinga2.yml
%config(noreplace) %attr(0640, root, foreman-proxy) %{foreman_proxy_settingsd_dir}/monitoring_icingadirector.yml
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%{foreman_proxy_bundlerd_dir}/%{plugin_name}.rb
%exclude %{gem_cache}
%{gem_spec}
%dir %{_root_sysconfdir}/foreman-proxy/monitoring

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Thu Jun 06 2024 Foreman Packaging Automation <packaging@theforeman.org> - 0.3.0-1
- Update to 0.3.0

* Mon May 09 2022 Eric D. Helms <ericdhelms@gmail.com> - 0.2.0-2
- Drop unused smart_proxy_dynflow_core_bundlerd_dir macro

* Mon May 02 2022 Dirk Goetz <dirk.goetz@netways.de> 0.2.0-1
- Update to 0.2.0

* Mon Jan 10 2022 Evgeni Golov - 0.1.2-8
- use versioned obsoletes for proxy plugins

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.1.2-7
- Rebuild for Ruby 2.7

* Mon Jun 22 2020 Evgeni Golov - 0.1.2-6
- Fix bundler.d location on EL8

* Tue May 26 2020 Adam Ruzicka <aruzicka@redhat.com> 0.1.2-5
- Move local state to /var/lib

* Tue May 12 2020 Adam Ruzicka <aruzicka@redhat.com> - 0.1.2-4
- Change localstatedir to sharedstatedir

* Tue Jan 07 2020 Eric D. Helms <ericdhelms@gmail.com> - 0.1.2-3
- Build for SCL

* Thu Sep 26 2019 Eric D. Helms <ericdhelms@gmail.com> - 0.1.2-2
- Update to SCL based template

* Tue Jun 12 2018 Timo Goebel <mail@timogoebel.name> - 0.1.2-1
- Update smart_proxy_monitoring to 0.1.2

* Tue Oct 24 2017 Daniel Lobato Garcia <me@daniellobato.me> 0.1.1-1
- Update smart_proxy_monitoring to 0.1.1 (mail@timogoebel.name)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Thu Apr 13 2017 Dirk Goetz <dirk.goetz@netways.de> - 0.1.0-1
- updated upstream

* Fri Aug 19 2016 Dirk Goetz <dirk.goetz@netways.de> - 0.0.1-1
- inital build
