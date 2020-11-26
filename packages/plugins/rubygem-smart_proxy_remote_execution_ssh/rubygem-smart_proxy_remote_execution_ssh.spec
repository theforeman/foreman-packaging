# template: smart_proxy_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%{!?_root_datadir:%global _root_datadir %{_datadir}}
%{!?_root_localstatedir:%global _root_localstatedir %{_localstatedir}}
%{!?_root_sysconfdir:%global _root_sysconfdir %{_sysconfdir}}

%global gem_name smart_proxy_remote_execution_ssh
%global plugin_name remote_execution_ssh

%global foreman_proxy_min_version 1.25
%global foreman_proxy_dir %{_root_datadir}/foreman-proxy
%global foreman_proxy_statedir %{_root_localstatedir}/lib/foreman-proxy
%global foreman_proxy_bundlerd_dir %{foreman_proxy_dir}/bundler.d
%global foreman_proxy_settingsd_dir %{_root_sysconfdir}/foreman-proxy/settings.d
%global smart_proxy_dynflow_bundlerd_dir %{_datadir}/smart_proxy_dynflow_core/bundler.d

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.3.1
Release: 2%{?foremandist}%{?dist}
Summary: Ssh remote execution provider for Foreman Smart-Proxy
Group: Applications/Internet
License: GPLv3
URL: https://github.com/theforeman/smart_proxy_remote_execution_ssh
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

%if 0%{?rhel} == 7
Requires: tfm-rubygem(smart_proxy_dynflow_core) >= 0.1.5
Requires: tfm-rubygem(foreman_remote_execution_core)
%else
Requires: rubygem(smart_proxy_dynflow_core) >= 0.1.5
Requires: rubygem(foreman_remote_execution_core)
%endif

# start specfile generated dependencies
Requires: foreman-proxy >= %{foreman_proxy_min_version}
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(smart_proxy_dynflow) >= 0.1
Requires: %{?scl_prefix}rubygem(smart_proxy_dynflow) < 1
Requires: %{?scl_prefix}rubygem(net-ssh)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-proxy-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

%{?scl:Obsoletes: rubygem-%{gem_name}}

%description
Ssh remote execution provider for Foreman Smart-Proxy.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%{?scl:Obsoletes: rubygem-%{gem_name}-doc}

%description doc
Documentation for %{name}.

%prep
%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} - << \EOF}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:EOF}

%build
# Create the gem as gem install only works on a gem file
%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%{?scl:EOF}

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%{?scl:scl enable %{scl} - << \EOF}
%gem_install
%{?scl:EOF}

%pre
if [ -d %{foreman_proxy_dir}/.ssh ] && [ ! -L %{foreman_proxy_dir}/.ssh ] ; then
  if [ -d %{foreman_proxy_statedir}/ssh ] ; then
    mv %{foreman_proxy_statedir}/ssh %{foreman_proxy_statedir}/ssh.save$(date '+%%y%%m%%d%%H%%M')
  fi
  mv %{foreman_proxy_dir}/.ssh %{foreman_proxy_statedir}/ssh
fi

%install
mkdir -p %{buildroot}%{foreman_proxy_statedir}/ssh
mkdir -p %{buildroot}%{foreman_proxy_dir}
ln -sv %{foreman_proxy_statedir}/ssh %{buildroot}%{foreman_proxy_dir}/.ssh

mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

# bundler file
mkdir -p %{buildroot}%{foreman_proxy_bundlerd_dir}
mv %{buildroot}%{gem_instdir}/bundler.plugins.d/%{plugin_name}.rb \
   %{buildroot}%{foreman_proxy_bundlerd_dir}

# sample config
mkdir -p %{buildroot}%{foreman_proxy_settingsd_dir}
mv %{buildroot}%{gem_instdir}/settings.d/remote_execution_ssh.yml.example \
   %{buildroot}%{foreman_proxy_settingsd_dir}/remote_execution_ssh.yml

mkdir -p %{buildroot}%{smart_proxy_dynflow_bundlerd_dir}
cat <<EOF > %{buildroot}%{smart_proxy_dynflow_bundlerd_dir}/foreman_remote_execution_core.rb
gem 'foreman_remote_execution_core'
EOF

%files
%dir %{gem_instdir}
%config(noreplace) %attr(0640, root, foreman-proxy) %{foreman_proxy_settingsd_dir}/remote_execution_ssh.yml
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%{foreman_proxy_bundlerd_dir}/%{plugin_name}.rb
%exclude %{gem_cache}
%{gem_spec}
%{smart_proxy_dynflow_bundlerd_dir}/foreman_remote_execution_core.rb
%{foreman_proxy_dir}/.ssh
%attr(0750,foreman-proxy,foreman-proxy) %{foreman_proxy_statedir}/ssh

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Thu Nov 26 2020 Markus Bucher <bucher@atix.de> 0.3.1-2
- Fix remove files and dirs from ssh-dir before move

* Mon Nov 09 2020 Adam Ruzicka <aruzicka@redhat.com> 0.3.1-1
- Update to 0.3.1

* Mon Jun 22 2020 Evgeni Golov - 0.3.0-4
- Fix bundler.d location on EL8

* Tue May 26 2020 Adam Ruzicka <aruzicka@redhat.com> 0.3.0-3
- Move local state to /var/lib

* Tue May 12 2020 Adam Ruzicka <aruzicka@redhat.com> 0.3.0-2
- Move local state to /var/lib

* Wed May 06 2020 Adam Ruzicka <aruzicka@redhat.com> 0.3.0-1
- Update to 0.3.0

* Tue Jan 07 2020 Eric D. Helms <ericdhelms@gmail.com> - 0.2.1-4
- Build for SCL

* Thu May 16 2019 Eric D. Helms <ericdhelms@gmail.com> - 0.2.1-3
- Require SCL prefix only on EL7

* Wed Apr 24 2019 Ivan Nečas <inecas@redhat.com> 0.2.1-1
- Update to 0.2.1

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
