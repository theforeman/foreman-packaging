# template: smart_proxy_plugin
%global gem_name smart_proxy_remote_execution_ssh
%global plugin_name remote_execution_ssh

%global foreman_proxy_min_version 1.24
%global foreman_proxy_dir %{_datadir}/foreman-proxy
%global foreman_proxy_statedir %{_sharedstatedir}/foreman-proxy
%global foreman_proxy_bundlerd_dir %{foreman_proxy_dir}/bundler.d
%global foreman_proxy_settingsd_dir %{_sysconfdir}/foreman-proxy/settings.d

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.11.7
Release: 1%{?foremandist}%{?dist}
Summary: Ssh remote execution provider for Foreman Smart-Proxy
License: GPLv3
URL: https://github.com/theforeman/smart_proxy_remote_execution_ssh
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: foreman-proxy >= %{foreman_proxy_min_version}
Requires: ruby >= 2.7.0
BuildRequires: ruby >= 2.7.0
BuildRequires: rubygems-devel
BuildArch: noarch
Provides: foreman-proxy-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

%description
Ssh remote execution provider for Foreman Smart-Proxy.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%pre
if [ -d %{foreman_proxy_dir}/.ssh ] && [ ! -L %{foreman_proxy_dir}/.ssh ] ; then
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
mv %{buildroot}%{gem_instdir}/bundler.d/%{plugin_name}.rb \
   %{buildroot}%{foreman_proxy_bundlerd_dir}

# sample config
mkdir -p %{buildroot}%{foreman_proxy_settingsd_dir}
mv %{buildroot}%{gem_instdir}/settings.d/remote_execution_ssh.yml.example \
   %{buildroot}%{foreman_proxy_settingsd_dir}/remote_execution_ssh.yml

%files
%dir %{gem_instdir}
%config(noreplace) %attr(0640, root, foreman-proxy) %{foreman_proxy_settingsd_dir}/remote_execution_ssh.yml
%license %{gem_instdir}/LICENSE
%exclude %{gem_instdir}/bundler.d
%{gem_libdir}
%exclude %{gem_instdir}/settings.d
%{foreman_proxy_bundlerd_dir}/%{plugin_name}.rb
%exclude %{gem_cache}
%{gem_spec}
%{foreman_proxy_dir}/.ssh
%attr(0700,foreman-proxy,foreman-proxy) %{foreman_proxy_statedir}/ssh

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Sun Aug 17 2025 Foreman Packaging Automation <packaging@theforeman.org> - 0.11.7-1
- Update to 0.11.7

* Thu Jun 26 2025 Foreman Packaging Automation <packaging@theforeman.org> - 0.11.6-1
- Update to 0.11.6

* Wed Dec 18 2024 Adam Ruzicka <aruzicka@redhat.com> - 0.11.5-1
- Update to 0.11.5

* Sun Oct 06 2024 Foreman Packaging Automation <packaging@theforeman.org> - 0.11.4-1
- Update to 0.11.4

* Tue Sep 24 2024 Foreman Packaging Automation <packaging@theforeman.org> - 0.11.3-1
- Update to 0.11.3

* Wed Sep 04 2024 Foreman Packaging Automation <packaging@theforeman.org> - 0.11.2-1
- Update to 0.11.2

* Wed Aug 28 2024 Foreman Packaging Automation <packaging@theforeman.org> - 0.11.1-1
- Update to 0.11.1

* Wed Jul 10 2024 Adam Ruzicka <aruzicka@redhat.com> - 0.11.0-1
- Update to 0.11.0

* Tue Jun 18 2024 Adam Ruzicka <aruzicka@redhat.com> - 0.10.6-1
- Update to 0.10.6

* Thu May 30 2024 Adam Ruzicka <aruzicka@redhat.com> - 0.10.5-1
- Update to 0.10.5

* Sun Mar 10 2024 Foreman Packaging Automation <packaging@theforeman.org> - 0.10.4-1
- Update to 0.10.4

* Tue Nov 14 2023 Adam Ruzicka <aruzicka@redhat.com> 0.10.3-1
- Update to 0.10.3

* Fri Oct 27 2023 Adam Ruzicka <aruzicka@redhat.com> 0.10.2-2
- Regenerate the spec based on latest template

* Thu Oct 26 2023 Foreman Packaging Automation <packaging@theforeman.org> 0.10.2-1
- Update to 0.10.2

* Sun Jan 22 2023 Foreman Packaging Automation <packaging@theforeman.org> 0.10.1-1
- Update to 0.10.1

* Mon Dec 12 2022 Adam Ruzicka <aruzicka@redhat.com> 0.10.0-1
- Update to 0.10.0

* Mon Nov 14 2022 Adam Ruzicka <aruzicka@redhat.com> 0.9.0-1
- Update to 0.9.0

* Sun Aug 28 2022 Foreman Packaging Automation <packaging@theforeman.org> 0.8.0-1
- Update to 0.8.0

* Fri May 13 2022 Adam Ruzicka <aruzicka@redhat.com> 0.7.0-1
- Update to 0.7.0

* Tue Apr 19 2022 Adam Ruzicka <aruzicka@redhat.com> 0.6.0-1
- Update to 0.6.0

* Wed Apr 13 2022 Eric D. Helms <ericdhelms@gmail.com> - 0.5.2-2
- Update ssh_identity_dir permissions

* Mon Feb 07 2022 Adam Ruzicka <aruzicka@redhat.com> 0.5.2-1
- Update to 0.5.2

* Mon Jan 10 2022 Evgeni Golov - 0.5.1-2
- use versioned obsoletes for proxy plugins

* Tue Jan 04 2022 Adam Ruzicka <aruzicka@redhat.com> 0.5.1-1
- Update to 0.5.1

* Tue Nov 16 2021 Adam Ruzicka <aruzicka@redhat.com> 0.5.0-1
- Update to 0.5.0

* Fri Jul 09 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.4.1-2
- Do not obsolete foreman_remote_execution_core

* Fri Jul 09 2021 Adam Ruzicka <aruzicka@redhat.com> 0.4.1-1
- Update to 0.4.1

* Mon Jun 07 2021 Adam Ruzicka <aruzicka@redhat.com> 0.4.0-1
- Update to 0.4.0

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.3.1-3
- Rebuild for Ruby 2.7

* Wed Mar 17 2021 Adam Ruzicka <aruzicka@redhat.com> 0.3.1-2
- Deploy bundlerd file for foreman proxy

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
