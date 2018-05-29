%global gem_name smart_proxy_remote_execution_ssh
%global foreman_proxy_dir /usr/share/foreman-proxy
%global foreman_proxy_statedir %{_localstatedir}/lib/foreman-proxy
%global foreman_proxy_bundlerd_dir %{foreman_proxy_dir}/bundler.d
%global foreman_proxy_settingsd_dir %{_sysconfdir}/foreman-proxy/settings.d
%global smart_proxy_dynflow_bundlerd_dir %{?rhel:/opt/theforeman/tfm/root/}%{_datadir}/smart_proxy_dynflow_core/bundler.d

Summary: SSH remote execution provider for Foreman smart proxy
Name: rubygem-%{gem_name}
Version: 0.2.0
Release: 2%{?dist}
Group: Applications/System
License: GPLv3
URL: https://github.com/theforeman/smart_proxy_remote_execution_ssh
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?rhel:tfm-}rubygem(smart_proxy_dynflow_core) >= 0.1.5
Requires: %{?rhel:tfm-}rubygem(foreman_remote_execution_core)
Requires: foreman-proxy >= 1.11.0
Requires: rubygem(smart_proxy_dynflow) >= 0.1.0
Requires: rubygem(smart_proxy_dynflow) < 0.3.0

Requires: ruby
Requires: ruby(rubygems)
Requires: ruby(release)
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildArch: noarch
Obsoletes: %{?rhel:tfm-}rubygem-smart_proxy_remote_execution_ssh_core < 0.1.4

Provides: rubygem(%{gem_name}) = %{version}
Provides: foreman-proxy-plugin-remote-execution-ssh

%description
SSH remote execution provider for Foreman smart proxy

%package doc
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}
Obsoletes: %{?rhel:tfm-}rubygem-smart_proxy_remote_execution_ssh_core-doc < 0.1.4
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep

%setup -q -c -T
%gem_install -n %{SOURCE0}

%build

%pre
if [ -d %{foreman_proxy_dir}/.ssh ] && [ ! -L %{foreman_proxy_dir}/.ssh ] ; then
  mv %{foreman_proxy_dir}/.ssh %{foreman_proxy_statedir}/ssh
fi

%install
mkdir -p %{buildroot}%{foreman_proxy_statedir}/ssh
mkdir -p %{buildroot}%{foreman_proxy_dir}
ln -sv %{foreman_proxy_statedir}/ssh %{buildroot}%{foreman_proxy_dir}/.ssh

mkdir -p %{buildroot}%{gem_dir}

cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{foreman_proxy_bundlerd_dir}
cp -pa .%{gem_instdir}/bundler.plugins.d/remote_execution_ssh.rb %{buildroot}%{foreman_proxy_bundlerd_dir}

mkdir -p  %{buildroot}%{foreman_proxy_settingsd_dir}
cp -pa .%{gem_instdir}/settings.d/remote_execution_ssh.yml.example %{buildroot}%{foreman_proxy_settingsd_dir}/remote_execution_ssh.yml

mkdir -p %{buildroot}%{smart_proxy_dynflow_bundlerd_dir}
cat <<EOF > %{buildroot}%{smart_proxy_dynflow_bundlerd_dir}/foreman_remote_execution_core.rb
gem 'foreman_remote_execution_core'
EOF

%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%{gem_instdir}/settings.d
%{foreman_proxy_bundlerd_dir}/remote_execution_ssh.rb
%config(noreplace) %{foreman_proxy_settingsd_dir}/remote_execution_ssh.yml
%license %{gem_instdir}/LICENSE
%{smart_proxy_dynflow_bundlerd_dir}/foreman_remote_execution_core.rb
%{foreman_proxy_dir}/.ssh
%attr(0750,foreman-proxy,foreman-proxy) %{foreman_proxy_statedir}/ssh
%exclude %{gem_instdir}/bundler.plugins.d
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_instdir}/README.md
%doc %{gem_docdir}

%changelog
* Tue May 29 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 0.2.0-2
- Handle .ssh symlinks

* Fri Apr 06 2018 Adam Ruzicka <aruzicka@redhat.com> 0.2.0-1
- Update to 0.2.0

* Wed Apr 04 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.1.5-2
- Move state files to /var
- Remove EL6 packaging compatibility
- Mark remote_execution_ssh.yml as noreplace

* Mon Jul 17 2017 Eric D. Helms <ericdhelms@gmail.com> 0.1.5-1
- Update smart_proxy_remote_execution_ssh_core to 0.1.5 (inecas@redhat.com)

* Tue Sep 20 2016 Dominic Cleal <dominic@cleal.org> 0.1.4-1
- Update smart_proxy_remote_execution to 0.1.4 (inecas@redhat.com)

* Tue Aug 23 2016 Dominic Cleal <dominic@cleal.org> 0.1.3-1
- Update smart_proxy_remote_execution_ssh to 0.1.3 (inecas@redhat.com)

* Fri Jun 24 2016 Dominic Cleal <dominic@cleal.org> 0.1.2-1
- Release smart_proxy_remote_execution_ssh 0.1.2 (stephen@redhat.com)

* Wed Feb 17 2016 Dominic Cleal <dominic@cleal.org> 0.0.13-1
- Release smart_proxy_remote_execution_ssh 0.0.13 (stbenjam@redhat.com)

* Mon Jan 25 2016 Dominic Cleal <dcleal@redhat.com> 0.0.12-1
- Release smart_proxy_remote_execution_ssh 0.0.12 (RPM) (stbenjam@redhat.com)

* Mon Jan 18 2016 Dominic Cleal <dcleal@redhat.com> 0.0.11-1
- Release smart_proxy_remote_execution_ssh 0.0.11 (stbenjam@redhat.com)

* Wed Dec 23 2015 Dominic Cleal <dcleal@redhat.com> 0.0.10-1
- Update smart_proxy_remote_execution_ssh to 0.0.10 (stbenjam@redhat.com)

* Fri Nov 13 2015 Dominic Cleal <dcleal@redhat.com> 0.0.8-1
- Update smart_proxy_remote_execution_ssh to 0.0.8 (stbenjam@redhat.com)

* Wed Oct 07 2015 Dominic Cleal <dcleal@redhat.com> 0.0.6-1
- Release smart_proxy_remote_execution_ssh 0.0.6 (RPM) (stbenjam@redhat.com)

* Wed Sep 02 2015 Dominic Cleal <dcleal@redhat.com> 0.0.5-1
- Release Remote Execution Plugins 0.0.5 (stbenjam@redhat.com)

* Mon Aug 10 2015 Stephen Benjamin <stephen@redhat.com> 0.0.3-1
- Initial release of 0.0.3
