# template: smart_proxy_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%{!?_root_bindir:%global _root_bindir %{_bindir}}
%{!?_root_datadir:%global _root_datadir %{_datadir}}
%{!?_root_localstatedir:%global _root_localstatedir %{_localstatedir}}
%{!?_root_sysconfdir:%global _root_sysconfdir %{_sysconfdir}}

%global gem_name smart_proxy_pulp
%global plugin_name pulp

%global foreman_proxy_min_version 2.3
%global foreman_proxy_dir %{_root_datadir}/foreman-proxy
%global foreman_proxy_statedir %{_root_localstatedir}/lib/foreman-proxy
%global foreman_proxy_bundlerd_dir %{foreman_proxy_dir}/bundler.d
%global foreman_proxy_settingsd_dir %{_root_sysconfdir}/foreman-proxy/settings.d

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 3.3.0
Release: 1%{?foremandist}%{?dist}
Summary: Basic Pulp support for Foreman Smart-Proxy
Group: Applications/Internet
License: GPLv3
URL: https://github.com/theforeman/smart-proxy-pulp-plugin
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

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

%{?scl:Obsoletes: rubygem-%{gem_name} < %{version}-%{release}}

%description
Basic Pulp support for Foreman Smart-Proxy.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%{?scl:Obsoletes: rubygem-%{gem_name}-doc < %{version}-%{release}}

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

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

# bundler file
mkdir -p %{buildroot}%{foreman_proxy_bundlerd_dir}
mv %{buildroot}%{gem_instdir}/bundler.d/%{plugin_name}.rb \
   %{buildroot}%{foreman_proxy_bundlerd_dir}

# sample config
mkdir -p %{buildroot}%{foreman_proxy_settingsd_dir}
mv %{buildroot}%{gem_instdir}/settings.d/pulpcore.yml.example \
   %{buildroot}%{foreman_proxy_settingsd_dir}/pulpcore.yml

%files
%dir %{gem_instdir}
%config(noreplace) %attr(0640, root, foreman-proxy) %{foreman_proxy_settingsd_dir}/pulpcore.yml
%license %{gem_instdir}/LICENSE
%exclude %{gem_instdir}/bundler.d
%{gem_libdir}
%exclude %{gem_instdir}/settings.d
%{foreman_proxy_bundlerd_dir}/%{plugin_name}.rb
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile

%changelog
* Mon Jan 08 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.3.0-1
- Update to 3.3.0

* Mon May 09 2022 Eric D. Helms <ericdhelms@gmail.com> - 3.2.0-3
- Drop unused smart_proxy_dynflow_core_bundlerd_dir macro

* Mon Jan 10 2022 Evgeni Golov - 3.2.0-2
- use versioned obsoletes for proxy plugins

* Thu Sep 02 2021 Eric D. Helms <ericdhelms@gmail.com> - 3.2.0-1
- Release rubygem-smart_proxy_pulp 3.2.0

* Tue Jun 22 2021 Eric D. Helms <ericdhelms@gmail.com> - 3.1.0-1
- Release rubygem-smart_proxy_pulp 3.1.0

* Wed Apr 07 2021 Eric D. Helms <ericdhelms@gmail.com> - 3.0.0-1
- Release 3.0.0

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 2.1.0-4
- Rebuild for Ruby 2.7

* Mon Jun 22 2020 Evgeni Golov - 2.1.0-3
- Fix bundler.d location on EL8

* Tue May 26 2020 Adam Ruzicka <aruzicka@redhat.com> 2.1.0-2
- Move local state to /var/lib

* Tue May 19 2020 Justin Sherrill <jsherril@redhat.com> 2.1.0-1
- Update to 2.1.0

* Tue May 12 2020 Adam Ruzicka <aruzicka@redhat.com> - 2.0.0-3
- Change localstatedir to sharedstatedir

* Wed Jan 08 2020 Eric D. Helms <ericdhelms@gmail.com> - 2.0.0-2
- Build for SCL

* Tue Jan 07 2020 Justin Sherrill <jsherril@redhat.com> 2.0.0-1
- Update to 2.0.0

* Mon Jan 06 2020 Justin Sherrill <jsherril@redhat.com> 1.6.0-1
- Update to 1.6.0

* Thu Sep 26 2019 Eric D. Helms <ericdhelms@gmail.com> - 1.5.0-2
- Update to SCL based template

* Wed Sep 18 2019 Justin Sherrill <jsherril@redhat.com> 1.5.0-1
- Update to 1.5.0

* Fri Mar 08 2019 Justin Sherrill <jsherril@redhat.com> 1.4.1-1
- Updated samrt_proxy_pulp to version 1.4.1

* Tue Sep 06 2016 Dominic Cleal <dominic@cleal.org> 1.3.0-1
- Updated smart_proxy_pulp to version 1.3.0 (dmitri@appliedlogic.ca)

* Fri Jul 15 2016 Dominic Cleal <dominic@cleal.org> 1.2.2-1
- Update rubygem-smart_proxy_pulp to 1.2.2 (dmitri@appliedlogic.ca)

* Thu Jun 09 2016 Dominic Cleal <dominic@cleal.org> 1.2.1-1
- Updated rubygem-smart_proxy_pulp to version 1.2.1 (dmitri@appliedlogic.ca)

* Wed Jan 27 2016 Dmitri Dolguikh <dmitri@appliedlogic.ca> 1.2.0-1
- Updated smart_proxy_pulp gem to version 1.2.0

* Wed Mar 18 2015 Marek Hulan <mhulan@redhat.com> 1.0.1-2
- Fixes the overriding of config file (mhulan@redhat.com)

* Thu Aug 07 2014 Dominic Cleal <dcleal@redhat.com> 1.0.1-1
- Add pulpnode.yml config file (dcleal@redhat.com)
- Updated smart_proxy_pulp gem to version 1.0.1 (dmitri@appliedlogic.ca)
- bumping smart_proxy_pulp version to 1.0.1 (jsherril@redhat.com)

* Wed Jul 23 2014 Dominic Cleal <dcleal@redhat.com> 1.0.0-2
- Fix -doc requirement on main package (dcleal@redhat.com)

* Wed Jul 23 2014 Dmitri Dolguikh <dmitri@appliedlogic.ca>
- new package built with tito
