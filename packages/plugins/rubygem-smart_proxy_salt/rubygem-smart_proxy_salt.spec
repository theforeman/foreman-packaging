# template: smart_proxy_plugin
%global gem_name smart_proxy_salt
%global plugin_name salt

%global foreman_proxy_min_version 1.8.0
%global foreman_proxy_dir %{_datarootdir}/foreman-proxy
%global foreman_proxy_bundlerd_dir %{foreman_proxy_dir}/bundler.d
%global foreman_proxy_settingsd_dir %{_sysconfdir}/foreman-proxy/settings.d

%global salt_config_dir %{_sysconfdir}/salt

Name: rubygem-%{gem_name}
Version: 2.1.9
Release: 2%{?foremandist}%{?dist}
Summary: SaltStack Plug-In for Foreman's Smart Proxy
Group: Applications/Internet
License: GPLv3
URL: https://github.com/theforeman/smart_proxy_salt
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: salt-master
Requires: python
Requires: /etc/cron.d

# start specfile generated dependencies
Requires: foreman-proxy >= %{foreman_proxy_min_version}
Requires: ruby(release)
Requires: ruby
Requires: ruby(rubygems)
BuildRequires: ruby(release)
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}
Provides: foreman-proxy-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

%description
SaltStack Plug-In for Foreman's Smart Proxy.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

mkdir -p %{buildroot}%{_sbindir}
cp -pa .%{gem_instdir}/sbin/upload-salt-reports \
        %{buildroot}%{_sbindir}/upload-salt-reports

# bundler file
mkdir -p %{buildroot}%{foreman_proxy_bundlerd_dir}
mv %{buildroot}%{gem_instdir}/bundler.d/%{plugin_name}.rb \
   %{buildroot}%{foreman_proxy_bundlerd_dir}

# sample config
mkdir -p %{buildroot}%{foreman_proxy_settingsd_dir}
mv %{buildroot}%{gem_instdir}/settings.d/salt.yml.example \
   %{buildroot}%{foreman_proxy_settingsd_dir}/salt.yml

mkdir -p  %{buildroot}%{salt_config_dir}
cp -pa .%{gem_instdir}/etc/foreman.yaml.example %{buildroot}%{salt_config_dir}/foreman.yaml

mkdir -p %{buildroot}%{_sysconfdir}/cron.d
install -Dp -m0644 .%{gem_instdir}/cron/smart_proxy_salt %{buildroot}%{_sysconfdir}/cron.d/%{gem_name}

%files
%dir %{gem_instdir}
%{_bindir}/foreman-node
%config(noreplace) %attr(0640, root, foreman-proxy) %{foreman_proxy_settingsd_dir}/salt.yml
%license %{gem_instdir}/LICENSE
%exclude %{gem_instdir}/bin
%exclude %{gem_instdir}/bundler.d
%exclude %{gem_instdir}/cron
%{gem_instdir}/etc
%{gem_libdir}
%exclude %{gem_instdir}/sbin
%exclude %{gem_instdir}/settings.d
%{foreman_proxy_bundlerd_dir}/%{plugin_name}.rb
%config(noreplace) %{salt_config_dir}/foreman.yaml
%config %{_sysconfdir}/cron.d/%{gem_name}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Tue Jul 02 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 2.1.9-2
- Regenerate spec file based on smart_proxy_plugin

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
