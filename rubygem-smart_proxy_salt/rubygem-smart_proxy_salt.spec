%global gem_name smart_proxy_salt

%global foreman_proxy_dir /usr/share/foreman-proxy
%global foreman_proxy_bundlerd_dir %{foreman_proxy_dir}/bundler.d
%global foreman_proxy_settingsd_dir %{_sysconfdir}/foreman-proxy/settings.d

%global salt_config_dir %{_sysconfdir}/salt

Summary: SaltStack support for Foreman Smart-Proxy
Name: rubygem-%{gem_name}
Version: 2.1.5
Release: 1%{?dist}
Group: Applications/System
License: GPLv3
URL: https://github.com/theforeman/smart_proxy_salt
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem

Requires: ruby(rubygems)
Requires: foreman-proxy >= 1.8.0
Requires: salt-master
Requires: python
Requires: /etc/cron.d

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
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_sysconfdir}/cron.d

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
cp -pa .%{gem_instdir}/sbin/upload-salt-reports %{buildroot}%{_sbindir}/upload-salt-reports
install -Dp -m0644 .%{gem_instdir}/cron/smart_proxy_salt %{buildroot}%{_sysconfdir}/cron.d/%{gem_name}

%files
%dir %{gem_instdir}
%{gem_instdir}/bin
%{gem_instdir}/sbin
%{gem_instdir}/cron
%{gem_instdir}/lib
%{gem_instdir}/bundler.d
%{gem_instdir}/settings.d
%{foreman_proxy_bundlerd_dir}/salt.rb
%config(noreplace) %{_sysconfdir}/foreman-proxy/settings.d/salt.yml
%config(noreplace) %{salt_config_dir}/foreman.yaml
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
