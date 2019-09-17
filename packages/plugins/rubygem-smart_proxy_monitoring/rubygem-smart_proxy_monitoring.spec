# Generated from smart_proxy_monitoring-0.1.2.gem by gem2rpm -*- rpm-spec -*-
# template: smart_proxy_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name smart_proxy_monitoring
%global plugin_name monitoring

%global foreman_proxy_min_version 1.24
%global foreman_proxy_dir /usr/share/foreman-proxy
%global foreman_proxy_bundlerd_dir %{foreman_proxy_dir}/bundler.d
%global foreman_proxy_settingsd_dir %{_sysconfdir}/foreman-proxy/settings.d

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.1.2
Release: 1%{?foremandist}%{?dist}
Summary: Monitoring plug-in for Foreman's smart proxy
Group: Applications/Internet
License: GPLv3
URL: http://github.com/theforeman/smart_proxy_monitoring
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: foreman-proxy >= %{foreman_proxy_min_version}
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(rest-client)
Requires: %{?scl_prefix_ruby}rubygem(json)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-proxy-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

%description
Monitoring plug-in for Foreman's smart proxy.


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
mv %{buildroot}%{gem_instdir}/settings.d/monitoring.yml.example \
   %{buildroot}%{foreman_proxy_settingsd_dir}/monitoring.yml
mv %{buildroot}%{gem_instdir}/settings.d/monitoring_icinga2.yml.example \
   %{buildroot}%{foreman_proxy_settingsd_dir}/monitoring_icinga2.yml
mv %{buildroot}%{gem_instdir}/settings.d/monitoring_icingadirector.yml.example \
   %{buildroot}%{foreman_proxy_settingsd_dir}/monitoring_icingadirector.yml

%files
%dir %{gem_instdir}
%config(noreplace) %attr(0640, root, foreman-proxy) %{foreman_proxy_settingsd_dir}/monitoring.yml
%config(noreplace) %attr(0640, root, foreman-proxy) %{foreman_proxy_settingsd_dir}/monitoring_icinga2.yml
%config(noreplace) %attr(0640, root, foreman-proxy) %{foreman_proxy_settingsd_dir}/monitoring_icingadirector.yml
%license %{gem_instdir}/LICENSE
%{gem_instdir}/bundler.d
%{gem_libdir}
%{gem_instdir}/settings.d
%{foreman_proxy_bundlerd_dir}/%{plugin_name}.rb
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Tue Sep 17 2019 Eric D. Helms <ericdhelms@gmail.com> 0.1.2-1
- Update to 0.1.2-1

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
