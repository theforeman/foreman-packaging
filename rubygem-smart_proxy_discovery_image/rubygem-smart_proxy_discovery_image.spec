%global gem_name smart_proxy_discovery_image

%global foreman_proxy_dir %{_datarootdir}/foreman-proxy
%global foreman_proxy_bundlerd_dir %{foreman_proxy_dir}/bundler.d
%global foreman_proxy_settingsd_dir %{_sysconfdir}/foreman-proxy/settings.d

Name: rubygem-%{gem_name}
Version: 1.0.7
Release: 1%{?dist}
Summary: Discovery image (node) plugin for Foreman's smart proxy
Group: Applications/Internet
License: GPLv3
URL: https://github.com/theforeman/smart_proxy_discovery_image
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: ruby(rubygems)
Requires: foreman-proxy >= 1.7.0


%if 0%{?rhel} == 6
Requires: ruby(abi)
BuildRequires: ruby(abi)
%else
Requires: ruby(release)
BuildRequires: ruby(release)
%endif
BuildRequires: rubygems-devel
BuildRequires: ruby(rubygems)

BuildArch: noarch

Provides: rubygem(%{gem_name}) = %{version}
Provides: foreman-proxy-plugin-discovery-image

%description
Smart Proxy plugin providing Image API on discovered nodes. This plugin is only
useful on discovered nodes, do not install on regular Smart Proxy deployments.

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires:%{name} = %{version}-%{release}

%description doc
Documentation for %{name}

%prep

%setup -q -c -T
%gem_install -n %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
       %{buildroot}%{gem_dir}/

# bundler file
mkdir -p %{buildroot}%{foreman_proxy_bundlerd_dir}
mv %{buildroot}%{gem_instdir}/bundler.d/discovery_image.rb \
   %{buildroot}%{foreman_proxy_bundlerd_dir}

# sample config
mkdir -p %{buildroot}%{foreman_proxy_settingsd_dir}
mv %{buildroot}%{gem_instdir}/settings.d/discovery_image.yml.example \
   %{buildroot}%{foreman_proxy_settingsd_dir}/discovery_image.yml

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_spec}
%{foreman_proxy_bundlerd_dir}/discovery_image.rb
%config %{foreman_proxy_settingsd_dir}/discovery_image.yml
%doc %{gem_instdir}/LICENSE
%exclude %{gem_cache}
%exclude %{gem_instdir}/Gemfile


%files doc
%{gem_docdir}
%{gem_instdir}/README.md

%changelog
* Mon Aug 14 2017 Eric D. Helms <ericdhelms@gmail.com> 1.0.7-1
- Update smart_proxy_discovery_image-1.0.7.gem (lzap+git@redhat.com)

* Wed May 24 2017 Dominic Cleal <dominic@cleal.org> 1.0.6-1
- Update smart_proxy_discovery_image-1.0.6 (lzap+git@redhat.com)

* Tue Oct 20 2015 Dominic Cleal <dcleal@redhat.com> 1.0.5-1
- Update smart_proxy_discovery_image to 1.0.5 (lzap+git@redhat.com)

* Fri Sep 11 2015 Lukas Zapletal <lzap+git@redhat.com>
- new package built with tito

