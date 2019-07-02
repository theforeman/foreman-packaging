# template: smart_proxy_plugin
%global gem_name smart_proxy_dns_infoblox
%global plugin_name dns_infoblox

%global foreman_proxy_min_version 1.16.0
%global foreman_proxy_dir %{_datarootdir}/foreman-proxy
%global foreman_proxy_bundlerd_dir %{foreman_proxy_dir}/bundler.d
%global foreman_proxy_settingsd_dir %{_sysconfdir}/foreman-proxy/settings.d

Name: rubygem-%{gem_name}
Version: 0.0.9
Release: 2%{?foremandist}%{?dist}
Summary: Infoblox DNS provider plugin for Foreman's smart proxy
Group: Applications/Internet
License: GPLv3
URL: https://github.com/theforeman/smart_proxy_dns_infoblox
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: foreman-proxy >= %{foreman_proxy_min_version}
Requires: ruby(release)
Requires: ruby
Requires: ruby(rubygems)
BuildRequires: ruby(release)
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}
Provides: foreman-proxy-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

%description
Infoblox DNS provider plugin for Foreman's smart proxy.


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
mv %{buildroot}%{gem_instdir}/config/dns_infoblox.yml.example \
   %{buildroot}%{foreman_proxy_settingsd_dir}/dns_infoblox.yml

%files
%dir %{gem_instdir}
%config(noreplace) %attr(0640, root, foreman-proxy) %{foreman_proxy_settingsd_dir}/dns_infoblox.yml
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%{foreman_proxy_bundlerd_dir}/%{plugin_name}.rb
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/test

%changelog
* Tue Jul 02 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.0.9-2
- Regenerate spec file based on smart_proxy_plugin

* Tue May 07 2019 Lukas Zapletal <lzap+rpm@redhat.com> 0.0.9-1
- Updated to 0.0.9 upstream version

* Wed Dec 12 2018 Lukas Zapletal <lzap+rpm@redhat.com> 0.0.7-1
- Bumped to match upstream version

* Mon Aug 14 2017 Eric D. Helms <ericdhelms@gmail.com> 0.0.6-1
- Update smart_proxy_dns_infoblox to 0.0.6 (dmitri@appliedlogic.ca)

* Mon Sep 12 2016 Dominic Cleal <dominic@cleal.org> 0.0.4-1
- new package built with tito

