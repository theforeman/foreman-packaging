# template: smart_proxy_plugin
%global gem_name smart_proxy_container_gateway
%global plugin_name container_gateway

%global foreman_proxy_min_version 1.24
%global foreman_proxy_dir %{_datadir}/foreman-proxy
%global foreman_proxy_statedir %{_sharedstatedir}/foreman-proxy
%global foreman_proxy_bundlerd_dir %{foreman_proxy_dir}/bundler.d
%global foreman_proxy_settingsd_dir %{_sysconfdir}/foreman-proxy/settings.d

Name: rubygem-%{gem_name}
Version: 1.0.9
Release: 1%{?foremandist}%{?dist}
Summary: Pulp 3 container registry support for Foreman/Katello Smart-Proxy
License: GPLv3
URL: https://github.com/ianballou/smart_proxy_container_gateway
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: foreman-proxy >= %{foreman_proxy_min_version}
Requires: ruby >= 2.5
Requires: ruby < 3
BuildRequires: ruby >= 2.5
BuildRequires: ruby < 3
BuildRequires: rubygems-devel
BuildArch: noarch
Provides: foreman-proxy-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

%description
Pulp 3 container registry support for Foreman/Katello Smart-Proxy.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

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
mv %{buildroot}%{gem_instdir}/settings.d/container_gateway.yml.example \
   %{buildroot}%{foreman_proxy_settingsd_dir}/container_gateway.yml

%files
%dir %{gem_instdir}
%config(noreplace) %attr(0640, root, foreman-proxy) %{foreman_proxy_settingsd_dir}/container_gateway.yml
%license %{gem_instdir}/LICENSE
%exclude %{gem_instdir}/bundler.d
%{gem_libdir}
%exclude %{gem_instdir}/settings.d
%{foreman_proxy_bundlerd_dir}/%{plugin_name}.rb
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Tue Sep 26 2023 Ian Ballou <ianballou67@gmail.com> 1.0.9-1
- Update to 1.0.9

* Wed Aug 02 2023 ianballou <ianballou67@gmail.com> 1.0.8-1
- Update to 1.0.8

* Tue Nov 29 2022 ianballou <ianballou67@gmail.com> 1.0.7-1
- Update to 1.0.7

* Wed Sep 29 2021 ianballou <ianballou67@gmail.com> 1.0.6-1
- Update to 1.0.6

* Thu Jun 17 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.0.5-2
- Add foremandist

* Mon Jun 14 2021 ianballou <ianballou67@gmail.com> 1.0.5-1
- Update to 1.0.5

* Mon Apr 26 2021 ianballou <ianballou67@gmail.com> 1.0.4-1
- Update to 1.0.4

* Thu Apr 15 2021 ianballou <ianballou67@gmail.com> 1.0.3-1
- Update to 1.0.3

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.0.2-2
- Rebuild plugins for Ruby 2.7

* Tue Feb 02 2021 ianballou <ianballou67@gmail.com> 1.0.2-1
- Update to 1.0.2

* Wed Jan 27 2021 ianballou <ianballou67@gmail.com> 1.0.1-1
- Update to 1.0.1

* Fri Jan 22 2021 ianballou <ianballou67@gmail.com> 1.0.0-1
- Add rubygem-smart_proxy_container_gateway generated by gem2rpm using the scl template

