%global gem_name smart_proxy_realm_ad_plugin
%global plugin_name realm_ad_plugin

%global foreman_proxy_dir %{_datarootdir}/foreman-proxy
%global foreman_proxy_bundlerd_dir %{foreman_proxy_dir}/bundler.d
%global foreman_proxy_settingsd_dir %{_sysconfdir}/foreman-proxy/settings.d

Name: rubygem-%{gem_name}
Version: 0.1
Release: 2%{?foremandist}%{?dist}
Summary: A realm ad provider plugin for Foreman's smart proxy
Group: Applications/Internet
License: GPLv3+
URL: https://github.com/martencassel/smart_proxy_realm_ad_plugin
Source0: https://rubygems.org/downloads/%{gem_name}-%{version}.gem
Requires: foreman-proxy >= 1.15
Requires: ruby(release)
Requires: ruby
Requires: ruby(rubygems)
Requires: rubygem(rkerberos)
Requires: rubygem(radcli)
BuildRequires: ruby(release)
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}
Provides: foreman-proxy-plugin-%{plugin_name}

%description
A realm ad provider plugin for Foreman's smart proxy.


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
mv %{buildroot}%{gem_instdir}/config/realm_ad.yml.example \
   %{buildroot}%{foreman_proxy_settingsd_dir}/realm_ad.yml

%files
%dir %{gem_instdir}
%config(noreplace) %attr(0640, root, foreman-proxy) %{foreman_proxy_settingsd_dir}/realm_ad.yml
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
* Wed Sep 12 2018 Bryan Kearney <bryan.kearney@gmail.com> - 0.1-2
- Move licenes which are GPL-* to GPLv3

* Thu Jan 04 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.1-1
- new package built with tito

