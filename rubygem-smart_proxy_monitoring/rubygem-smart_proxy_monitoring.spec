%global gem_name smart_proxy_monitoring
%global plugin_name monitoring

%global foreman_proxy_dir %{_datarootdir}/foreman-proxy
%global foreman_proxy_bundlerd_dir %{foreman_proxy_dir}/bundler.d
%global foreman_proxy_settingsd_dir %{_sysconfdir}/foreman-proxy/settings.d

Name: rubygem-%{gem_name}
Version: 0.1.1
Release: 1%{?foremandist}%{?dist}
Summary: Monitoring plug-in for Foreman's smart proxy
Group: Applications/Internet
License: GPLv3
URL: https://github.com/theforeman/smart_proxy_monitoring
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: foreman-proxy >= 1.12
Requires: ruby(release)
Requires: ruby
Requires: ruby(rubygems)
Requires: rubygem(rest-client)
Requires: rubygem(json)
BuildRequires: ruby(release)
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}
Provides: foreman-proxy-plugin-%{plugin_name}

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
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

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
mkdir -p %{buildroot}%{_sysconfdir}/foreman-proxy/monitoring

%files
%dir %{gem_instdir}
%config(noreplace) %attr(0640, root, foreman-proxy) %{foreman_proxy_settingsd_dir}/monitoring.yml
%config(noreplace) %attr(0640, root, foreman-proxy) %{foreman_proxy_settingsd_dir}/monitoring_icinga2.yml
%config(noreplace) %attr(0640, root, foreman-proxy) %{foreman_proxy_settingsd_dir}/monitoring_icingadirector.yml
%doc %{gem_instdir}/LICENSE
%{gem_instdir}/bundler.d
%{gem_libdir}
%{gem_instdir}/settings.d
%{foreman_proxy_bundlerd_dir}/%{plugin_name}.rb
%exclude %{gem_cache}
%{gem_spec}
%dir %{_sysconfdir}/foreman-proxy/monitoring

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Thu Apr 13 2017 Dirk Goetz <dirk.goetz@netways.de> - 0.1.0-1
- updated upstream

* Fri Aug 19 2016 Dirk Goetz <dirk.goetz@netways.de> - 0.0.1-1
- inital build
