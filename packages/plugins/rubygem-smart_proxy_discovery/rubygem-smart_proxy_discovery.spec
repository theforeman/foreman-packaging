# Generated from smart_proxy_discovery-1.0.5.gem by gem2rpm -*- rpm-spec -*-
# template: smart_proxy_plugin
%global gem_name smart_proxy_discovery
%global plugin_name discovery

%global foreman_proxy_min_version 1.7.0
%global foreman_proxy_dir %{_datarootdir}/foreman-proxy
%global foreman_proxy_bundlerd_dir %{foreman_proxy_dir}/bundler.d
%global foreman_proxy_settingsd_dir %{_sysconfdir}/foreman-proxy/settings.d

Name: rubygem-%{gem_name}
Version: 1.0.5
Release: 1%{?foremandist}%{?dist}
Summary: Discovery plugin for Foreman's smart proxy
Group: Applications/Internet
License: GPLv3
URL: https://github.com/theforeman/smart_proxy_discovery
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: foreman-proxy >= %{foreman_proxy_min_version}
Requires: ruby(release)
Requires: ruby
Requires: ruby(rubygems)
Requires: rubygem(rest-client)
BuildRequires: ruby(release)
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}
Provides: foreman-proxy-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

%description
This smart proxy plugin, together with a Foreman plugin, add the capability to
discover unknown bare-metal. This plugin provides proxy API for nodes to
communicate with Foreman instance and vice versa.


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
mv %{buildroot}%{gem_instdir}/settings.d/discovery.yml.example \
   %{buildroot}%{foreman_proxy_settingsd_dir}/discovery.yml

%files
%dir %{gem_instdir}
%config(noreplace) %attr(0640, root, foreman-proxy) %{foreman_proxy_settingsd_dir}/discovery.yml
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
* Fri Apr 26 2019 Evgeni Golov 1.0.5-1
- Update to 1.0.5-1

* Fri Apr 26 2019 Evgeni Golov 1.0.4-2
- Regenerate RPM spec based on latest template

* Fri Apr 29 2016 Dominic Cleal <dominic@cleal.org> 1.0.4-1
- Update smart_proxy_discovery to 1.0.4 (dominic@cleal.org)

* Tue Oct 20 2015 Dominic Cleal <dcleal@redhat.com> 1.0.3-1
- Updated rubygem-smart_proxy_discovery to 1.0.3 (RPM) (lzap+git@redhat.com)

* Tue Feb 24 2015 Dominic Cleal <dcleal@redhat.com> 1.0.2-1
- Bumped smart_proxy_discovery to 1.0.2 (lzap+git@redhat.com)

* Fri Jan 09 2015 Lukas Zapletal <lzap+rpm@redhat.com> 1.0.1-1
- Bumped to version 1.0.1

* Thu Jan 08 2015 Lukas Zapletal <lzap+rpm@redhat.com> 1.0.0-1
- Initial version
