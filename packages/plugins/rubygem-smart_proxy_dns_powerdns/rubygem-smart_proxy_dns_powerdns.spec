# Generated from smart_proxy_dns_powerdns-0.4.0.gem by gem2rpm -*- rpm-spec -*-
# template: smart_proxy_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name smart_proxy_dns_powerdns
%global plugin_name dns_powerdns

%global foreman_proxy_min_version 1.24
%global foreman_proxy_dir /usr/share/foreman-proxy
%global foreman_proxy_bundlerd_dir %{foreman_proxy_dir}/bundler.d
%global foreman_proxy_settingsd_dir %{_sysconfdir}/foreman-proxy/settings.d

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.4.0
Release: 1%{?foremandist}%{?dist}
Summary: PowerDNS DNS provider plugin for Foreman's smart proxy
Group: Applications/Internet
License: GPL-3.0
URL: https://github.com/theforeman/smart_proxy_dns_powerdns
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: foreman-proxy >= %{foreman_proxy_min_version}
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(mysql2)
Requires: %{?scl_prefix}rubygem(pg)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-proxy-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

%description
PowerDNS DNS provider plugin for Foreman's smart proxy.


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
mv %{buildroot}%{gem_instdir}/config/dns_powerdns.yml \
   %{buildroot}%{foreman_proxy_settingsd_dir}/dns_powerdns.yml

%files
%dir %{gem_instdir}
%config(noreplace) %attr(0640, root, foreman-proxy) %{foreman_proxy_settingsd_dir}/dns_powerdns.yml
%license %{gem_instdir}/LICENSE
%{gem_instdir}/bundler.d
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
* Tue Sep 17 2019 Eric D. Helms <ericdhelms@gmail.com> 0.4.0-1
- Update to 0.4.0-1

* Tue Aug 13 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.4.0-1
- Update to 0.4.0

* Tue Jan 03 2017 Dominic Cleal <dominic@cleal.org> 0.3.0-1
- Bump rubygem-smart_proxy_dns_powerdns to 0.3.0 (ewoud@kohlvanwijngaarden.nl)

* Wed Aug 10 2016 Dominic Cleal <dominic@cleal.org> 0.2.1-1
- Bump smart_proxy_dns_powerdns to 0.2.1 (ekohlvanwijngaarden@antagonist.nl)

* Tue Nov 10 2015 Dominic Cleal <dcleal@redhat.com> 0.1.0-1
- new package built with tito

* Thu Oct 08 2015 Ewoud Kohl van Wijngaarden 0.1.0-1
- Initial packaging
