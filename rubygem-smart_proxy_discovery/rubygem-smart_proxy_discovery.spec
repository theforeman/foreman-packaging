%global gem_name smart_proxy_discovery

%global foreman_proxy_dir %{_datarootdir}/foreman-proxy
%global foreman_proxy_bundlerd_dir %{foreman_proxy_dir}/bundler.d
%global foreman_proxy_settingsd_dir %{_sysconfdir}/foreman-proxy/settings.d

Name: rubygem-%{gem_name}
Version: 1.0.2
Release: 1%{?dist}
Summary: Discovery plugin for Foreman's smart proxy
Group: Applications/Internet
License: GPLv3
URL: http://github.com/theforeman/smart_proxy_discovery
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem

Requires: ruby(rubygems)
Requires: foreman-proxy >= 1.7.0
Requires: rubygem(rest-client) > 1.6.2
Requires: rubygem(rest-client) < 1.7


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
Provides: foreman-proxy-plugin-discovery

%description
This smart proxy plugin, together with a Foreman plugin, add the capability to
discover unknown bare-metal. This plugin provides proxy API for nodes to
communicate with Foreman instance and vice versa.

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
mv %{buildroot}%{gem_instdir}/bundler.d/discovery.rb \
   %{buildroot}%{foreman_proxy_bundlerd_dir}

# sample config
mkdir -p %{buildroot}%{foreman_proxy_settingsd_dir}
mv %{buildroot}%{gem_instdir}/settings.d/discovery.yml.example \
   %{buildroot}%{foreman_proxy_settingsd_dir}/discovery.yml

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_spec}
%{foreman_proxy_bundlerd_dir}/discovery.rb
%config(noreplace) %{foreman_proxy_settingsd_dir}/discovery.yml
%doc %{gem_instdir}/LICENSE
%exclude %{gem_cache}


%files doc
%{gem_docdir}
%{gem_instdir}/README.md

%changelog
* Fri Jan 09 2015 Lukas Zapletal <lzap+rpm@redhat.com> 1.0.1-1
- Bumped to version 1.0.1

* Thu Jan 08 2015 Lukas Zapletal <lzap+rpm@redhat.com> 1.0.0-1
- Initial version
