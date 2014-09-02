%global gem_name smart_proxy_salt

%global foreman_proxy_dir /usr/share/foreman-proxy
%global foreman_proxy_bundlerd_dir %{foreman_proxy_dir}/bundler.d
%global foreman_proxy_settingsd_dir %{_sysconfdir}/foreman-proxy/settings.d

%global salt_config_dir %{_sysconfdir}/salt

Summary: SaltStack support for Foreman Smart-Proxy
Name: rubygem-%{gem_name}
Version: 0.0.2
Release: 1%{?dist}
Group: Applications/System
License: GPLv3
URL: https://github.com/theforeman/smart_proxy_salt
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem

Requires: ruby(rubygems)
Requires: foreman-proxy >= 1.6.0
Requires: salt-master

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
%gem_install -n %{SOURCE0} --bindir %{_bindir}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{foreman_proxy_bundlerd_dir}
cp -pa .%{gem_instdir}/bundler.d/salt.rb %{buildroot}%{foreman_proxy_bundlerd_dir}
mkdir -p  %{buildroot}%{foreman_proxy_settingsd_dir}
cp -pa .%{gem_instdir}/settings.d/salt.yml.example %{buildroot}%{foreman_proxy_settingsd_dir}/salt.yml
mkdir -p  %{buildroot}%{salt_config_dir}
cp -pa .%{gem_instdir}/etc/foreman.yaml.example %{buildroot}%{salt_config_dir}/foreman.yaml
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/foreman-node %{buildroot}%{_bindir}/foreman-node

%files
%dir %{gem_instdir}
%{gem_instdir}/bin
%{gem_instdir}/lib
%{gem_instdir}/bundler.d
%{gem_instdir}/settings.d
%{foreman_proxy_bundlerd_dir}/salt.rb
%config(noreplace) %{_sysconfdir}/foreman-proxy/settings.d/salt.yml
%config(noreplace) %{salt_config_dir}/foreman.yaml
%{_bindir}/foreman-node
%doc %{gem_instdir}/LICENSE

%exclude %{gem_cache}
%exclude %{gem_instdir}/etc
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Sun Aug 31 2014 Michael Moll <mmoll@mmoll.at>
- update to 0.0.2

* Wed Aug 20 2014 Michael Moll <mmoll@mmoll.at>
- create package
