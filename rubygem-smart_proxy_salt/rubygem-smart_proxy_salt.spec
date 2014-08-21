%global gem_name smart_proxy_salt

%global foreman_proxy_dir /usr/share/foreman-proxy
%global foreman_proxy_bundlerd_dir %{foreman_proxy_dir}/bundler.d
%global foreman_proxy_settingsd_dir %{_sysconfdir}/foreman-proxy/settings.d

Summary: SaltStack support for Foreman Smart-Proxy
Name: rubygem-%{gem_name}
Version: 0.0.1
Release: 1%{?dist}
Group: Applications/System
License: GPLv3
URL: https://github.com/theforeman/smart_proxy_salt
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem

Requires: ruby(rubygems)
Requires: foreman-proxy >= 1.6.0

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
Provides: foreman-proxy-plugin-salt

%description
SaltStack support for Foreman Smart-Proxy.

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
cp -pa .%{gem_instdir}/bundler.d/salt.rb %{buildroot}%{foreman_proxy_bundlerd_dir}
mkdir -p  %{buildroot}%{_sysconfdir}/foreman-proxy/settings.d/
cp -pa .%{gem_instdir}/settings.d/salt.yml.example %{buildroot}%{foreman_proxy_settingsd_dir}/salt.yml

%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%{gem_instdir}/bundler.d
%{gem_instdir}/settings.d
%{foreman_proxy_bundlerd_dir}/salt.rb
%{_sysconfdir}/foreman-proxy/settings.d/salt.yml
%doc %{gem_instdir}/LICENSE

%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Wed Aug 20 2014 Michael Moll <mmoll@mmoll.at>
- create package
