# template: smart_proxy_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%{!?_root_datadir:%global _root_datadir %{_datadir}}
%{!?_root_localstatedir:%global _root_localstatedir %{_localstatedir}}
%{!?_root_sysconfdir:%global _root_sysconfdir %{_sysconfdir}}

%global gem_name smart_proxy_chef
%global plugin_name chef

%global foreman_proxy_min_version 1.25
%global foreman_proxy_dir %{_root_datadir}/foreman-proxy
%global foreman_proxy_statedir %{_root_localstatedir}/lib/foreman-proxy
%global foreman_proxy_bundlerd_dir %{foreman_proxy_dir}/bundler.d
%global foreman_proxy_settingsd_dir %{_root_sysconfdir}/foreman-proxy/settings.d
%global smart_proxy_dynflow_bundlerd_dir %{_datadir}/smart_proxy_dynflow_core/bundler.d

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.2.0
Release: 6%{?foremandist}%{?dist}
Summary: Chef support for Foreman Smart-Proxy
Group: Applications/Internet
License: GPLv3
URL: https://github.com/theforeman/smart_proxy_chef
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: foreman-proxy >= %{foreman_proxy_min_version}
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(chef-api)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-proxy-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

%description
Chef support for Foreman Smart-Proxy.


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
mv %{buildroot}%{gem_instdir}/settings.d/chef.yml.example \
   %{buildroot}%{foreman_proxy_settingsd_dir}/chef.yml

%files
%dir %{gem_instdir}
%config(noreplace) %attr(0640, root, foreman-proxy) %{foreman_proxy_settingsd_dir}/chef.yml
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%{foreman_proxy_bundlerd_dir}/%{plugin_name}.rb
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile

%changelog
* Mon Jun 22 2020 Evgeni Golov - 0.2.0-6
- Fix bundler.d location on EL8

* Tue May 26 2020 Adam Ruzicka <aruzicka@redhat.com> 0.2.0-5
- Move local state to /var/lib

* Tue May 12 2020 Adam Ruzicka <aruzicka@redhat.com> 0.2.0-4
- Change localstatedir to sharedstatedir

* Tue Jan 07 2020 Eric D. Helms <ericdhelms@gmail.com> - 0.2.0-3
- Build for SCL

* Thu Sep 26 2019 Eric D. Helms <ericdhelms@gmail.com> - 0.2.0-2
- Update to SCL based template

* Mon Jan 30 2017 Dominic Cleal <dominic@cleal.org> 0.2.0-1
- Update smart_proxy_chef to 0.2.0 (mhulan@redhat.com)

* Wed Jun 22 2016 Dominic Cleal <dominic@cleal.org> 0.1.8-1
- Update smart_proxy_chef to 0.1.8 (mhulan@redhat.com)

* Fri Apr 08 2016 Dominic Cleal <dominic@cleal.org> 0.1.7-1
- Update smart_proxy_chef to 0.1.7 (mhulan@redhat.com)

* Fri Dec 18 2015 Dominic Cleal <dcleal@redhat.com> 0.1.6-1
- Update smart_proxy_chef to 0.1.6 (mhulan@redhat.com)

* Tue Oct 06 2015 Dominic Cleal <dcleal@redhat.com> 0.1.5-1
- Update smart_proxy_chef to 0.1.5 (mhulan@redhat.com)

* Mon Jun 22 2015 Marek Hulan <mhulan@redhat.com> 0.1.4-1
- Update smart_proxy_chef to 0.1.4 (mhulan@redhat.com)

* Wed Mar 18 2015 Marek Hulan <mhulan@redhat.com> 0.1.3-2
- Fixes the overriding of config file (mhulan@redhat.com)

* Tue Mar 17 2015 Marek Hulan <mhulan@redhat.com> 0.1.3-1
- Update smart_proxy_chef to 0.1.3 (mhulan@redhat.com)

* Wed Jan 14 2015 Dominic Cleal <dcleal@redhat.com> 0.1.2-1
- Update smart_proxy_chef to 0.1.2 (dcleal@redhat.com)

* Tue Nov 11 2014 Dominic Cleal <dcleal@redhat.com> 0.1.1-1
- new package built with tito (mhulan@redhat.com)
