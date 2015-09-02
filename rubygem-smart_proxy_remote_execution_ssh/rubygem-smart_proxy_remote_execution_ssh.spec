%global gem_name smart_proxy_remote_execution_ssh

%global foreman_proxy_dir /usr/share/foreman-proxy
%global foreman_proxy_bundlerd_dir %{foreman_proxy_dir}/bundler.d
%global foreman_proxy_settingsd_dir %{_sysconfdir}/foreman-proxy/settings.d

Summary: SSH remote execution provider for Foreman smart proxy
Name: rubygem-%{gem_name}
Version: 0.0.5
Release: 1%{?dist}
Group: Applications/System
License: GPLv3
URL: https://github.com/theforeman/smart_proxy_remote_execution_ssh
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem

Requires: foreman-proxy >= 1.9.0
Requires: rubygem(smart_proxy_dynflow) >= 0.0.3
Requires: rubygem(smart_proxy_dynflow) < 0.1.0

Requires: ruby(rubygems)
Requires: ruby
Requires: rubygem(net-ssh)
Requires: rubygem(net-scp)

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
Provides: foreman-proxy-plugin-remote-execution-ssh

%description
SSH remote execution provider for Foreman smart proxy

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
cp -pa .%{gem_instdir}/bundler.d/remote_execution_ssh.rb %{buildroot}%{foreman_proxy_bundlerd_dir}
mkdir -p  %{buildroot}%{foreman_proxy_settingsd_dir}
cp -pa .%{gem_instdir}/settings.d/remote_execution_ssh.yml.example %{buildroot}%{foreman_proxy_settingsd_dir}/remote_execution_ssh.yml

%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%{gem_instdir}/bundler.d
%{gem_instdir}/settings.d
%{foreman_proxy_bundlerd_dir}/remote_execution_ssh.rb
%config %{foreman_proxy_settingsd_dir}/remote_execution_ssh.yml
%doc %{gem_instdir}/LICENSE

%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_instdir}/README.md
%doc %{gem_docdir}

%changelog
* Wed Sep 02 2015 Dominic Cleal <dcleal@redhat.com> 0.0.5-1
- Release Remote Execution Plugins 0.0.5 (stbenjam@redhat.com)

* Mon Aug 10 2015 Stephen Benjamin <stephen@redhat.com> 0.0.3-1
- Initial release of 0.0.3
