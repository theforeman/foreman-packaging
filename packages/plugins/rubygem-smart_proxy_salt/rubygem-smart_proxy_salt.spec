# template: smart_proxy_plugin
%global gem_name smart_proxy_salt
%global plugin_name salt

%global foreman_proxy_min_version 2.5
%global foreman_proxy_dir %{_datadir}/foreman-proxy
%global foreman_proxy_statedir %{_sharedstatedir}/foreman-proxy
%global foreman_proxy_bundlerd_dir %{foreman_proxy_dir}/bundler.d
%global foreman_proxy_settingsd_dir %{_sysconfdir}/foreman-proxy/settings.d

%global salt_config_dir %{_sysconfdir}/salt
%global salt_proxy_runners_dir %{foreman_proxy_dir}/salt/runners
%global salt_proxy_reactors_dir %{foreman_proxy_dir}/salt/reactors
%global salt_state_grains_dir %{foreman_proxy_statedir}/salt/grains

Name: rubygem-%{gem_name}
Version: 6.0.0
Release: 1%{?foremandist}%{?dist}
Summary: SaltStack Plug-In for Foreman's Smart Proxy
License: GPLv3
URL: https://github.com/theforeman/smart_proxy_salt
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# salt-specific dependencies
Requires: salt-master
Requires: python3
BuildRequires: python3-rpm-macros

# start specfile generated dependencies
Requires: foreman-proxy >= %{foreman_proxy_min_version}
Requires: ruby >= 2.7
Requires: ruby < 4
BuildRequires: ruby >= 2.7
BuildRequires: ruby < 4
BuildRequires: rubygems-devel
BuildArch: noarch
Provides: foreman-proxy-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

%description
This plug-in adds support for Salt to Foreman's Smart Proxy.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

# runners
mkdir -p %{buildroot}%{salt_proxy_runners_dir}
mv %{buildroot}%{gem_instdir}/salt/minion_auth/srv/salt/_runners/* \
   %{buildroot}%{salt_proxy_runners_dir}
mv %{buildroot}%{gem_instdir}/salt/report_upload/srv/salt/_runners/* \
   %{buildroot}%{salt_proxy_runners_dir}
# reactors
mkdir -p %{buildroot}%{salt_proxy_reactors_dir}
mv %{buildroot}%{gem_instdir}/salt/minion_auth/foreman_minion_auth.sls \
   %{buildroot}%{salt_proxy_reactors_dir}/
mv %{buildroot}%{gem_instdir}/salt/report_upload/foreman_report_upload.sls \
   %{buildroot}%{salt_proxy_reactors_dir}/
# grains
mkdir -p %{buildroot}%{salt_state_grains_dir}
touch %{buildroot}%{salt_state_grains_dir}/autosign_key

# bundler file
mkdir -p %{buildroot}%{foreman_proxy_bundlerd_dir}
mv %{buildroot}%{gem_instdir}/bundler.d/%{plugin_name}.rb \
   %{buildroot}%{foreman_proxy_bundlerd_dir}

# sample config
mkdir -p %{buildroot}%{foreman_proxy_settingsd_dir}
mv %{buildroot}%{gem_instdir}/settings.d/salt.saltfile.example \
   %{buildroot}%{foreman_proxy_settingsd_dir}/salt.saltfile
mv %{buildroot}%{gem_instdir}/settings.d/salt.yml.example \
   %{buildroot}%{foreman_proxy_settingsd_dir}/salt.yml

mkdir -p  %{buildroot}%{salt_config_dir}
cp -pa .%{gem_instdir}/etc/foreman.yaml.example %{buildroot}%{salt_config_dir}/foreman.yaml

mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/foreman-node %{buildroot}%{_bindir}/foreman-node

mkdir -p %{buildroot}%{_sbindir}
mv %{buildroot}/%{gem_instdir}/sbin/upload-salt-reports %{buildroot}%{_sbindir}/upload-salt-reports

%files
%dir %{gem_instdir}
%{_bindir}/foreman-node
%{_sbindir}/upload-salt-reports
%config(noreplace) %attr(0640, root, foreman-proxy) %{foreman_proxy_settingsd_dir}/salt.saltfile
%config(noreplace) %attr(0640, root, foreman-proxy) %{foreman_proxy_settingsd_dir}/salt.yml
%license %{gem_instdir}/LICENSE
%{gem_instdir}/bin
%exclude %{gem_instdir}/bundler.d
%{gem_instdir}/etc
%{gem_libdir}
%{gem_instdir}/salt
%{gem_instdir}/sbin
%exclude %{gem_instdir}/settings.d
%{foreman_proxy_bundlerd_dir}/%{plugin_name}.rb
%exclude %{gem_cache}
%{gem_spec}
%config(noreplace) %{salt_config_dir}/foreman.yaml
%exclude %{gem_instdir}/etc
%{salt_proxy_runners_dir}
%{salt_proxy_reactors_dir}
%dir %attr(-,foreman-proxy,foreman-proxy) %{salt_state_grains_dir}
%ghost %{salt_state_grains_dir}/autosign_key

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%post
if [ ! -f %{salt_state_grains_dir}/autosign_key ] ; then
  touch %{salt_state_grains_dir}/autosign_key
  chmod 640 %{salt_state_grains_dir}/autosign_key
  chown foreman-proxy:foreman-proxy %{salt_state_grains_dir}/autosign_key
fi

%changelog
* Thu May 08 2025 Foreman Packaging Automation <packaging@theforeman.org> - 6.0.0-1
- Update to 6.0.0

* Fri Apr 19 2024 Nadja Heitmann <nadjah@atix.de> 5.1.0-1
- Update to 5.1.0-1
- Remove python2 support

* Fri Nov 25 2022 Bastian Schmidt <schmidt@atix.de> 5.0.1-1
- Update to 5.0.1
- Drop cron job

* Thu Aug 18 2022 Bastian Schmidt <schmidt@atix.de> 5.0.0-4
- Add automatic report upload via reactor

* Mon May 09 2022 Eric D. Helms <ericdhelms@gmail.com> - 5.0.0-3
- Drop unused smart_proxy_dynflow_core_bundlerd_dir macro

* Tue Apr 05 2022 Bernhard Suttner <suttner@atix.de> - 5.0.0-2
- Fix wrong rubygem wrapper script for shell script 'salt_python_wrapper'

* Mon Feb 14 2022 Bernhard Suttner <suttner@atix.de> 5.0.0-1
- Update to 5.0.0

* Wed Jan 12 2022 Bastian Schmidt <schmidt@atix.de> 4.0.0-1
- Update to 4.0.0
- Add Autosign via Grains authentication
- Remove smart_proxy_salt_core

* Mon Jan 10 2022 Evgeni Golov - 3.1.2-9
- use versioned obsoletes for proxy plugins

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 3.1.2-8
- Rebuild for Ruby 2.7

* Wed Mar 17 2021 Adam Ruzicka <aruzicka@redhat.com> 3.1.2-7
- Deploy bundlerd file for foreman proxy

* Thu Jul 09 2020 Bernhard Suttner <suttner@atix.de> - 3.1.2-6
- Fix upload-salt-report path
- Fix hashbang for foreman-node helper script

* Fri Jul 03 2020 Stefan Bogner <bogner@b1-systems.de> - 3.1.2-5
- Do not change hashbang on RHEL < 8

* Tue Jun 23 2020 Markus Bucher <bucher@atix.de> - 3.1.2-4
- Fix hashbang in upload-salt-reports

* Mon Jun 22 2020 Adam Ruzicka <aruzicka@redhat.com> 3.1.2-3
- Prevent local state from being put to /usr/com

* Mon Jun 22 2020 Evgeni Golov - 3.1.2-2
- Fix bundler.d location on EL8

* Tue Jun 09 2020 Bernhard Suttner <suttner@atix.de> 3.1.2-1
- Update to 3.1.2
- Move local state to /var/lib (Co-Authored-By: Adam Ruzicka <aruzicka@redhat.com>)

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.1.1-4
- Update spec to remove the ror scl

* Tue Jan 07 2020 Eric D. Helms <ericdhelms@gmail.com> - 3.1.1-3
- Build for SCL

* Mon Nov 18 2019 Eric D. Helms <ericdhelms@gmail.com> - 3.1.1-2
- Update to SCL based template

* Tue Nov 05 2019 Bernhard Suttner <suttner@atix.de> 3.1.1-1
- Update to 3.1.1

* Thu Oct 31 2019 Bernhard Suttner <suttner@atix.de> 3.1.0-1
- Update to 3.1.0

* Fri Aug 02 2019 Adam Ruzicka <aruzicka@redhat.com> 3.0.0-1
- Update to 3.0.0

* Tue May 08 2018 Michael Moll <kvedulv@kvedulv.de> 2.1.9-1
- update smart_proxy_salt to 2.1.9 (kvedulv@kvedulv.de)

* Thu Mar 30 2017 Dominic Cleal <dominic@cleal.org> 2.1.8-1
- update smart_proxy_salt to 2.1.8 (kvedulv@kvedulv.de)

* Mon Oct 10 2016 Dominic Cleal <dominic@cleal.org> 2.1.7-1
- update smart_proxy_salt to 2.1.7 (kvedulv@kvedulv.de)

* Mon Oct 26 2015 Dominic Cleal <dcleal@redhat.com> 2.1.6-1
- Small smart_proxy_salt update (stbenjam@redhat.com)

* Tue Sep 01 2015 Dominic Cleal <dcleal@redhat.com> 2.1.5-1
- Release smart_proxy_salt 2.1.5 (stbenjam@redhat.com)

* Thu Aug 13 2015 Stephen Benjamin <stephen@redhat.com> 2.1.4-1
- Update smart_proxy_salt to 2.1.4

* Fri Jun 26 2015 Dominic Cleal <dcleal@redhat.com> 2.1.3-1
- update smart_proxy_salt to 2.1.3 (kvedulv@kvedulv.de)

* Sat May 09 2015 Stephen Benjamin <stephen@redhat.com> 2.1.2-1
- Update smart_proxy_salt to 2.1.2 (stephen@redhat.com)

* Mon Mar 02 2015 Dominic Cleal <dcleal@redhat.com> 2.0.0-1
- Update smart_proxy_salt to 2.0.0 (dcleal@redhat.com)

* Thu Nov 20 2014 Dominic Cleal <dcleal@redhat.com> 1.0.0-3
- Only require foreman-proxy 1.6.0 or higher (stbenjam@redhat.com)

* Thu Nov 20 2014 Dominic Cleal <dcleal@redhat.com> 1.0.0-2
- Fix cron.d file permissions (stbenjam@redhat.com)

* Wed Nov 19 2014 Stephen Benjamin <stephen@bitbin.de> - 1.0.0-1
- Update to 1.0.0

* Sun Aug 31 2014 Michael Moll <mmoll@mmoll.at> - 0.0.2-1
- update to 0.0.2

* Wed Aug 20 2014 Michael Moll <mmoll@mmoll.at> - 0.0.1-1
- create package
