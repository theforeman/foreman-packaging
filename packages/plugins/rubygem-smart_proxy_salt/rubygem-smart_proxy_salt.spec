%if 0%{?rhel} == 7 || (0%{?fedora} && 0%{?fedora} <= 29)
%bcond_without python2
%else
%bcond_with python2
%endif

%if 0%{?rhel} >= 8 || 0%{?fedora} || 0%{?epel}
%bcond_without python3
%else
%bcond_with python3
%endif

%{!?_root_localstatedir:%global _root_localstatedir %{_localstatedir}}

%global gem_name smart_proxy_salt

%global foreman_proxy_dir /usr/share/foreman-proxy
%global foreman_proxy_statedir %{_root_localstatedir}/lib/foreman-proxy
%global foreman_proxy_bundlerd_dir %{foreman_proxy_dir}/bundler.d
%global foreman_proxy_settingsd_dir %{_sysconfdir}/foreman-proxy/settings.d
%global smart_proxy_dynflow_bundlerd_dir %{?rhel:/opt/theforeman/tfm/root/}%{_datadir}/smart_proxy_dynflow_core/bundler.d

%global salt_config_dir %{_sysconfdir}/salt

Summary: SaltStack support for Foreman Smart-Proxy
Name: rubygem-%{gem_name}
Version: 3.1.2
Release: 1%{?dist}
Group: Applications/System
License: GPLv3
URL: https://github.com/theforeman/smart_proxy_salt
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: ruby(rubygems)
Requires: foreman-proxy >= 1.8.0
Requires: salt-master
%if %{with python2}
Requires: python
%endif
%if %{with python3}
Requires: python3
%endif
Requires: /etc/cron.d

%if 0%{?rhel} == 7
Requires: tfm-rubygem(smart_proxy_dynflow_core) >= 0.2.2
Requires: tfm-rubygem(smart_proxy_salt_core)
%else
Requires: rubygem(smart_proxy_dynflow_core) >= 0.2.2
Requires: rubygem(smart_proxy_salt_core)
%endif

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
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

%if %{with python2}
sed -i -e '1s|^#!.*$|#!%{__python2}|' sbin/upload-salt-reports
%endif

%if %{with python3}
sed -i -e '1s|^#!.*$|#!%{__python3}|' sbin/upload-salt-reports
%endif

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_sysconfdir}/cron.d

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{foreman_proxy_bundlerd_dir}
cp -pa .%{gem_instdir}/bundler.d/salt.rb %{buildroot}%{foreman_proxy_bundlerd_dir}
mkdir -p  %{buildroot}%{foreman_proxy_settingsd_dir}
cp -pa .%{gem_instdir}/settings.d/salt.yml.example %{buildroot}%{foreman_proxy_settingsd_dir}/salt.yml
cp -pa .%{gem_instdir}/settings.d/salt.saltfile.example %{buildroot}%{foreman_proxy_settingsd_dir}/salt.saltfile
mkdir -p  %{buildroot}%{salt_config_dir}
cp -pa .%{gem_instdir}/etc/foreman.yaml.example %{buildroot}%{salt_config_dir}/foreman.yaml
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/foreman-node %{buildroot}%{_bindir}/foreman-node
cp -pa .%{gem_instdir}/sbin/upload-salt-reports %{buildroot}%{_sbindir}/upload-salt-reports
install -Dp -m0644 .%{gem_instdir}/cron/smart_proxy_salt %{buildroot}%{_sysconfdir}/cron.d/%{gem_name}
mkdir -p %{buildroot}%{smart_proxy_dynflow_bundlerd_dir}
cat <<EOF > %{buildroot}%{smart_proxy_dynflow_bundlerd_dir}/smart_proxy_salt_core.rb
gem 'smart_proxy_salt_core'
EOF

%files
%dir %{gem_instdir}
%{gem_instdir}/bin
%{gem_instdir}/sbin
%{gem_instdir}/cron
%{gem_instdir}/salt
%{gem_instdir}/lib
%{gem_instdir}/bundler.d
%{gem_instdir}/settings.d
%{foreman_proxy_bundlerd_dir}/salt.rb
%{smart_proxy_dynflow_bundlerd_dir}/smart_proxy_salt_core.rb
%config(noreplace) %{_sysconfdir}/foreman-proxy/settings.d/salt.yml
%config(noreplace) %{salt_config_dir}/foreman.yaml
%config(noreplace) %{foreman_proxy_settingsd_dir}/salt.saltfile
%config %{_sysconfdir}/cron.d/%{gem_name}
%{_bindir}/foreman-node
%{_sbindir}/upload-salt-reports
%doc %{gem_instdir}/LICENSE

%exclude %{gem_cache}
%exclude %{gem_instdir}/etc
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Tue Jun 09 2020 Bernhard Suttner <suttner@atix.de> 3.1.2-1
- Update to 3.1.2
- Move local state to /var/lib
  (Co-Authored-By: Adam Ruzicka <aruzicka@redhat.com>)
- Prevent local state from being put to /usr/com
  (Co-Authored-By: Adam Ruzicka <aruzicka@redhat.com>)
- Adapt prep- and build-section to latest version
  (Co-Authored-By: Markus Bucher <bucher@atix.de>)

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
