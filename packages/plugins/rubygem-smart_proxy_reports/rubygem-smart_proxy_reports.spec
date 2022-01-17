# template: smart_proxy_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%{!?_root_datadir:%global _root_datadir %{_datadir}}
%{!?_root_localstatedir:%global _root_localstatedir %{_localstatedir}}
%{!?_root_sysconfdir:%global _root_sysconfdir %{_sysconfdir}}

%global gem_name smart_proxy_reports
%global plugin_name reports

%global foreman_proxy_min_version 2.5
%global foreman_proxy_dir %{_root_datadir}/foreman-proxy
%global foreman_proxy_statedir %{_root_localstatedir}/lib/foreman-proxy
%global foreman_proxy_bundlerd_dir %{foreman_proxy_dir}/bundler.d
%global foreman_proxy_settingsd_dir %{_root_sysconfdir}/foreman-proxy/settings.d

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.0.7
Release: 1%{?foremandist}%{?dist}
Summary: Transform and forward reports from config management or hosts
Group: Applications/Internet
License: GPLv3
URL: https://github.com/theforeman/%{gem_name}
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: foreman-proxy >= %{foreman_proxy_min_version}
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby >= 2.5
Requires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby >= 2.5
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-proxy-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

%description
Foreman Host Reports provides an API for configuration management platforms
like Ansible or Puppet, or managed hosts, to upload reports and facts.


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

# data dir
install -d -m755 %{buildroot}%{foreman_proxy_statedir}/%{plugin_name}

%files
%dir %{gem_instdir}
%config(noreplace) %attr(0640, root, foreman-proxy) %{foreman_proxy_settingsd_dir}/%{plugin_name}.yml
%license %{gem_instdir}/LICENSE
%exclude %{gem_instdir}/settings.d
%{gem_libdir}
%{foreman_proxy_bundlerd_dir}/%{plugin_name}.rb
%exclude %{gem_cache}
%{gem_spec}
%attr(0755, foreman-proxy, foreman-proxy) %{foreman_proxy_statedir}/%{plugin_name}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Mon Jan 17 2022 Foreman Packaging Automation <packaging@theforeman.org> 0.0.7-1
- Update to 0.0.7

* Fri Oct 22 2021 Lukas Zapletal <lzap+rpm@redhat.com> 0.0.5-1
- Update to 0.0.5

* Fri Oct 15 2021 Lukas Zapletal <lzap+rpm@redhat.com> 0.0.3-1
- Initial version
