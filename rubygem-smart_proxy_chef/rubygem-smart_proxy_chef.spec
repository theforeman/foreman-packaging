%global gem_name smart_proxy_chef

%global foreman_proxy_dir /usr/share/foreman-proxy
%global foreman_proxy_bundlerd_dir %{foreman_proxy_dir}/bundler.d
%global foreman_proxy_settingsd_dir %{_sysconfdir}/foreman-proxy/settings.d

Summary: Chef support for Foreman Smart-Proxy
Name: rubygem-%{gem_name}
Version: 0.1.3
Release: 1%{?dist}
Group: Applications/System
License: GPLv3
URL: https://github.com/theforeman/smart_proxy_chef
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem

Requires: ruby(rubygems)
Requires: foreman-proxy >= 1.6.0
Requires: ruby(release)
Requires: rubygem(chef-api)

BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby(rubygems)

BuildArch: noarch

Provides: rubygem(%{gem_name}) = %{version}
Provides: foreman-proxy-plugin-chef

%description
Chef support for Foreman Smart-Proxy.

%package doc
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep

%setup -q -c -T
%gem_install -n %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{foreman_proxy_bundlerd_dir}
cp -pa .%{gem_instdir}/bundler.d/chef.rb %{buildroot}%{foreman_proxy_bundlerd_dir}
mkdir -p  %{buildroot}%{foreman_proxy_settingsd_dir}
cp -pa .%{gem_instdir}/settings.d/chef.yml.example %{buildroot}%{foreman_proxy_settingsd_dir}/chef.yml

%files
%dir %{gem_instdir}
%{gem_instdir}/bundler.d
%{gem_libdir}
%{gem_instdir}/settings.d
%{foreman_proxy_bundlerd_dir}/chef.rb
%{foreman_proxy_settingsd_dir}/chef.yml
%doc %{gem_instdir}/LICENSE

%exclude %{gem_cache}
%exclude %{gem_instdir}/Gemfile
%{gem_spec}

%files doc
%doc %{gem_docdir}

%changelog
* Wed Jan 14 2015 Dominic Cleal <dcleal@redhat.com> 0.1.2-1
- Update smart_proxy_chef to 0.1.2 (dcleal@redhat.com)

* Tue Nov 11 2014 Dominic Cleal <dcleal@redhat.com> 0.1.1-1
- new package built with tito (mhulan@redhat.com)

