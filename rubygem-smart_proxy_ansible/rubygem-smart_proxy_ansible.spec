%global gem_name smart_proxy_ansible

%global foreman_proxy_dir /usr/share/foreman-proxy
%global foreman_proxy_bundlerd_dir %{foreman_proxy_dir}/bundler.d
%global foreman_proxy_settingsd_dir %{_sysconfdir}/foreman-proxy/settings.d
%global smart_proxy_dynflow_bundlerd_dir %{?rhel:/opt/theforeman/tfm/root/}%{_datadir}/smart_proxy_dynflow_core/bundler.d

Summary: Ansible support for Foreman smart proxy
Name: rubygem-%{gem_name}
Version: 2.0.2
Release: 1%{?foremandist}%{?dist}
Group: Applications/System
License: GPLv3
URL: https://github.com/theforeman/smart_proxy_ansible
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?rhel:tfm-}rubygem(smart_proxy_dynflow_core) >= 0.1.5
Requires: %{?rhel:tfm-}rubygem(foreman_ansible_core) >= 2.0.2
Requires: %{?rhel:tfm-}rubygem(foreman_ansible_core) < 3.0.0
Requires: foreman-proxy >= 1.11.0
Requires: rubygem(smart_proxy_dynflow) >= 0.1
Requires: rubygem(smart_proxy_dynflow) < 1.0

Requires: ruby
Requires: ruby(rubygems)

Requires: ansible >= 2.2

Requires: ruby(release)
BuildRequires: ruby(release)
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
cat <<EOF > %{buildroot}%{smart_proxy_dynflow_bundlerd_dir}/foreman_ansible_core.rb
gem 'foreman_ansible_core'
EOF

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
* Mon Feb 13 2017 Dominic Cleal <dominic@cleal.org> 1.1.1-1
- Update smart_proxy_ansible to 1.1.1 (me@daniellobato.me)

* Fri Jan 20 2017 Dominic Cleal <dominic@cleal.org> 1.0.1-1
- Release 1.0.1 smart_proxy_ansible (me@daniellobato.me)
- Add Ansible dependency for Ansible proxy plugin (tbrisker@gmail.com)

* Wed Oct 05 2016 Dominic Cleal <dominic@cleal.org> 1.0.0-1
- new package built with tito

