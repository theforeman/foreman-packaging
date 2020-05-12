# template: smart_proxy_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%{!?_root_datadir:%global _root_datadir %{_datadir}}
%{!?_root_sharedstatedir:%global _root_sharedstatedir %{_sharedstatedir}}
%{!?_root_sysconfdir:%global _root_sysconfdir %{_sysconfdir}}

%global gem_name smart_proxy_discovery_image
%global plugin_name discovery_image

%global foreman_proxy_min_version 1.25
%global foreman_proxy_dir %{_root_datadir}/foreman-proxy
%global foreman_proxy_statedir %{_root_sharedstatedir}/foreman-proxy
%global foreman_proxy_bundlerd_dir %{foreman_proxy_dir}/bundler.d
%global foreman_proxy_settingsd_dir %{_root_sysconfdir}/foreman-proxy/settings.d
%global smart_proxy_dynflow_bundlerd_dir %{!?scl:/opt/theforeman/tfm/root}%{_datadir}/smart_proxy_dynflow_core/bundler.d

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.0.9
Release: 4%{?foremandist}%{?dist}
Summary: FDI API for Foreman Smart-Proxy
Group: Applications/Internet
License: GPLv3
URL: https://github.com/theforeman/smart_proxy_discovery_image
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: foreman-proxy >= %{foreman_proxy_min_version}
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-proxy-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

%{?scl:Obsoletes: rubygem-%{gem_name}}

%description
Smart Proxy plugin providing Image API on discovered nodes. This plugin is
only
useful on discovered nodes, do not install on regular Smart Proxy deployments.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%{?scl:Obsoletes: rubygem-%{gem_name}-doc}

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
mv %{buildroot}%{gem_instdir}/settings.d/discovery_image.yml.example \
   %{buildroot}%{foreman_proxy_settingsd_dir}/discovery_image.yml

%files
%dir %{gem_instdir}
%config(noreplace) %attr(0640, root, foreman-proxy) %{foreman_proxy_settingsd_dir}/discovery_image.yml
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%{foreman_proxy_bundlerd_dir}/%{plugin_name}.rb
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md

%changelog
* Tue May 12 2020 Adam Ruzicka <aruzicka@redhat.com> 1.0.9-4
- Change localstatedir to sharedstatedir

* Tue Jan 07 2020 Eric D. Helms <ericdhelms@gmail.com> - 1.0.9-3
- Build for SCL

* Thu Sep 26 2019 Eric D. Helms <ericdhelms@gmail.com> - 1.0.9-2
- Update to SCL based template

* Tue Nov 07 2017 Daniel Lobato Garcia <me@daniellobato.me> 1.0.9-1
- Updated smart_proxy_discovery_image to 1.0.9 (lzap@redhat.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Mon Aug 14 2017 Eric D. Helms <ericdhelms@gmail.com> 1.0.7-1
- Update smart_proxy_discovery_image-1.0.7.gem (lzap+git@redhat.com)

* Wed May 24 2017 Dominic Cleal <dominic@cleal.org> 1.0.6-1
- Update smart_proxy_discovery_image-1.0.6 (lzap+git@redhat.com)

* Tue Oct 20 2015 Dominic Cleal <dcleal@redhat.com> 1.0.5-1
- Update smart_proxy_discovery_image to 1.0.5 (lzap+git@redhat.com)

* Fri Sep 11 2015 Lukas Zapletal <lzap+git@redhat.com>
- new package built with tito
