# template: smart_proxy_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%{!?_root_bindir:%global _root_bindir %{_bindir}}
%{!?_root_datadir:%global _root_datadir %{_datadir}}
%{!?_root_localstatedir:%global _root_localstatedir %{_localstatedir}}
%{!?_root_sysconfdir:%global _root_sysconfdir %{_sysconfdir}}

%global gem_name smart_proxy_omaha
%global plugin_name omaha

%global foreman_proxy_min_version 1.25
%global foreman_proxy_dir %{_root_datadir}/foreman-proxy
%global foreman_proxy_statedir %{_root_localstatedir}/foreman-proxy
%global foreman_proxy_bundlerd_dir %{foreman_proxy_dir}/bundler.d
%global foreman_proxy_settingsd_dir %{_root_sysconfdir}/foreman-proxy/settings.d
%global smart_proxy_dynflow_bundlerd_dir %{!?scl:/opt/theforeman/tfm/root}%{_datadir}/smart_proxy_dynflow_core/bundler.d

%global content_dir %{foreman_proxy_statedir}/openscap

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.0.5
Release: 2%{?foremandist}%{?dist}
Summary: Omaha protocol support for smart-proxy
Group: Applications/Internet
License: GPLv3
URL: https://github.com/theforeman/smart_proxy_omaha
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: foreman-proxy >= %{foreman_proxy_min_version}
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ror}rubygem(nokogiri) >= 1.5.11
Requires: %{?scl_prefix_ruby}rubygem(json)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-proxy-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

%description
This plug-in adds support for the Omaha Procotol to Foreman's Smart Proxy.


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

mkdir -p %{buildroot}%{_root_bindir}
cp -a .%{_root_bindir}/* \
        %{buildroot}%{_root_bindir}/
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

# bundler file
mkdir -p %{buildroot}%{foreman_proxy_bundlerd_dir}
mv %{buildroot}%{gem_instdir}/bundler.d/%{plugin_name}.rb \
   %{buildroot}%{foreman_proxy_bundlerd_dir}

# sample config
mkdir -p %{buildroot}%{foreman_proxy_settingsd_dir}
mv %{buildroot}%{gem_instdir}/settings.d/omaha.yml.example \
   %{buildroot}%{foreman_proxy_settingsd_dir}/omaha.yml

#crontab
mkdir -p %{buildroot}%{_root_sysconfdir}/cron.d/
mv %{buildroot}%{gem_instdir}/extra/foreman-proxy-omaha-sync.cron \
   %{buildroot}%{_root_sysconfdir}/cron.d/%{name}

# content directory
mkdir -p %{buildroot}%{content_dir}

%files
%dir %{gem_instdir}
%attr(-,%{proxy_user},%{proxy_user}) %{content_dir}
%{_root_bindir}/smart-proxy-omaha-sync
%config(noreplace) %attr(0644, root, root) %{_root_sysconfdir}/cron.d/%{name}
%config(noreplace) %attr(0640, root, foreman-proxy) %{foreman_proxy_settingsd_dir}/omaha.yml
%license %{gem_instdir}/LICENSE
%{gem_instdir}/bin
%{gem_libdir}
%{foreman_proxy_bundlerd_dir}/%{plugin_name}.rb
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/smart_proxy_omaha.gemspec
%{gem_instdir}/test

%changelog
* Thu Sep 26 2019 Eric D. Helms <ericdhelms@gmail.com> - 0.0.5-2
- Update to SCL based template

* Fri Aug 24 2018 Timo Goebel <mail@timogoebel.name> - 0.0.5-1
- Update smart_proxy_omaha to 0.0.5

* Mon Jun 18 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 0.0.4-2
- Relax nokogiri dependency
- Remove EL6 compatibility

* Tue Jun 12 2018 Timo Goebel <mail@timogoebel.name> - 0.0.4-1
- Update smart_proxy_omaha to 0.0.4

* Tue Oct 24 2017 Daniel Lobato Garcia <me@daniellobato.me> 0.0.3-1
- Update smart_proxy_omaha to 0.0.3 (mail@timogoebel.name)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Mon Aug 14 2017 Eric D. Helms <ericdhelms@gmail.com> 0.0.2-1
- Update smart_proxy_omaha to 0.0.2 (mail@timogoebel.name)

* Mon Oct 17 2016 Dominic Cleal <dominic@cleal.org> 0.0.1-1
- new package built with tito
