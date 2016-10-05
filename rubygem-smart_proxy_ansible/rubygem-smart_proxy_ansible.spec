%global gem_name smart_proxy_ansible

%global foreman_proxy_dir /usr/share/foreman-proxy
%global foreman_proxy_bundlerd_dir %{foreman_proxy_dir}/bundler.d
%global foreman_proxy_settingsd_dir %{_sysconfdir}/foreman-proxy/settings.d
%global smart_proxy_dynflow_bundlerd_dir %{?rhel:/opt/theforeman/tfm/root/}%{_datadir}/smart_proxy_dynflow_core/bundler.d

Summary: Ansible support for Foreman smart proxy
Name: rubygem-%{gem_name}
Version: 1.0.0
Release: 1%{?foremandist}%{?dist}
Group: Applications/System
License: GPLv3
URL: https://github.com/theforeman/smart_proxy_ansible
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem

Requires: %{?rhel:tfm-}rubygem(smart_proxy_dynflow_core) >= 0.1.5
Requires: %{?rhel:tfm-}rubygem(foreman_ansible_core)
Requires: foreman-proxy >= 1.11.0
Requires: rubygem(smart_proxy_dynflow) >= 0.1
Requires: rubygem(smart_proxy_dynflow) < 1.0

Requires: ruby
Requires: ruby(rubygems)

%if 0%{?rhel} == 6
Requires: ruby(abi)
BuildRequires: ruby(abi)
%else
Requires: ruby(release)
BuildRequires: ruby(release)
%endif
BuildRequires: rubygems-devel
BuildArch: noarch

Provides: rubygem(%{gem_name}) = %{version}
Provides: foreman-proxy-plugin-ansible

%description
Ansible support for Foreman smart proxy

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
cp -pa .%{gem_instdir}/bundler.plugins.d/smart_proxy_ansible.rb %{buildroot}%{foreman_proxy_bundlerd_dir}

mkdir -p  %{buildroot}%{foreman_proxy_settingsd_dir}
cp -pa .%{gem_instdir}/settings.d/ansible.yml.example %{buildroot}%{foreman_proxy_settingsd_dir}/ansible.yml

mkdir -p %{buildroot}%{smart_proxy_dynflow_bundlerd_dir}
cp -pa .%{gem_instdir}/bundler.plugins.d/foreman_ansible_core.rb %{buildroot}/%{smart_proxy_dynflow_bundlerd_dir}

%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%{gem_instdir}/settings.d
%{foreman_proxy_bundlerd_dir}/smart_proxy_ansible.rb
%config %{foreman_proxy_settingsd_dir}/ansible.yml
%doc %{gem_instdir}/LICENSE
%{smart_proxy_dynflow_bundlerd_dir}/foreman_ansible_core.rb

%exclude %{gem_instdir}/bundler.plugins.d
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_instdir}/README.md
%doc %{gem_docdir}

%changelog
