# template: smart_proxy_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%{!?_root_datadir:%global _root_datadir %{_datadir}}
%{!?_root_localstatedir:%global _root_localstatedir %{_localstatedir}}
%{!?_root_sysconfdir:%global _root_sysconfdir %{_sysconfdir}}

%global gem_name smart_proxy_shellhooks
%global plugin_name shellhooks

%global foreman_proxy_min_version 2.3
%global foreman_proxy_dir %{_root_datadir}/foreman-proxy
%global foreman_proxy_statedir %{_root_localstatedir}/lib/foreman-proxy
%global foreman_proxy_bundlerd_dir %{foreman_proxy_dir}/bundler.d
%global foreman_proxy_settingsd_dir %{_root_sysconfdir}/foreman-proxy/settings.d

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.9.3
Release: 1%{?foremandist}%{?dist}
Summary: Execute scripts via REST API from Foreman Webhooks plugin
Group: Applications/Internet
License: GPLv3
URL: https://github.com/theforeman/%{gem_name}
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

%description
Foreman Webhooks uses this plugin to execute scripts for integration of 3rd
party systems with Foreman.


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
mv %{buildroot}%{gem_instdir}/settings.d/%{plugin_name}.yml.example \
   %{buildroot}%{foreman_proxy_settingsd_dir}/%{plugin_name}.yml

# example scripts
install -d -m755 %{buildroot}%{foreman_proxy_statedir}/%{plugin_name}
mv %{buildroot}%{gem_instdir}/examples/* %{buildroot}%{foreman_proxy_statedir}/%{plugin_name}

%files
%dir %{gem_instdir}
%config(noreplace) %attr(0640, root, foreman-proxy) %{foreman_proxy_settingsd_dir}/%{plugin_name}.yml
%license %{gem_instdir}/LICENSE
%exclude %{gem_instdir}/settings.d
%{gem_libdir}
%{foreman_proxy_bundlerd_dir}/%{plugin_name}.rb
%exclude %{gem_cache}
%{gem_spec}
%{foreman_proxy_statedir}/%{plugin_name}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Wed May 15 2024 Adam Ruzicka <aruzicka@redhat.com> - 0.9.3-1
- Release rubygem-smart_proxy_shellhooks 0.9.3

* Mon May 09 2022 Eric D. Helms <ericdhelms@gmail.com> - 0.9.2-3
- Drop unused smart_proxy_dynflow_core_bundlerd_dir macro

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.9.2-2
- Rebuild for Ruby 2.7

* Tue Mar 16 2021 Lukas Zapletal <lzap+rpm@redhat.com> 0.9.2-1
- Update to 0.9.2

* Thu Dec 17 2020 Lukas Zapletal <lzap+rpm@redhat.com> 0.9.1-1
- Initial version
