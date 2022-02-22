# template: smart_proxy_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%{!?_root_datadir:%global _root_datadir %{_datadir}}
%{!?_root_localstatedir:%global _root_localstatedir %{_localstatedir}}
%{!?_root_sysconfdir:%global _root_sysconfdir %{_sysconfdir}}

%global gem_name smart_proxy_dynflow
%global plugin_name dynflow

%global foreman_proxy_min_version 1.16
%global foreman_proxy_dir %{_root_datadir}/foreman-proxy
%global foreman_proxy_statedir %{_root_localstatedir}/lib/foreman-proxy
%global foreman_proxy_bundlerd_dir %{foreman_proxy_dir}/bundler.d
%global foreman_proxy_settingsd_dir %{_root_sysconfdir}/foreman-proxy/settings.d

Summary: Dynflow runtime for Foreman smart proxy
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.7.0
Release: 1%{?foremandist}%{?dist}
Group: Applications/System
License: GPLv3
URL: https://github.com/theforeman/smart_proxy_dynflow
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix}rubygem(logging)

# start specfile generated dependencies
Requires: foreman-proxy >= %{foreman_proxy_min_version}
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby >= 2.5
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(dynflow) >= 1.6
Requires: %{?scl_prefix}rubygem(dynflow) < 2
Requires: %{?scl_prefix}rubygem(rest-client)
Requires: %{?scl_prefix}rubygem(sqlite3)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby >= 2.5
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-proxy-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

%{?scl:Obsoletes: rubygem-%{gem_name} < %{version}-%{release}}

%description
Use the Dynflow inside Foreman smart proxy.


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
mv %{buildroot}%{gem_instdir}/settings.d/dynflow.yml.example \
   %{buildroot}%{foreman_proxy_settingsd_dir}/dynflow.yml

mkdir -p %{buildroot}%{foreman_proxy_statedir}/dynflow

%files
%dir %{gem_instdir}
%dir %attr(750, foreman-proxy, foreman-proxy) %{foreman_proxy_statedir}/dynflow
%config(noreplace) %attr(0640, root, foreman-proxy) %{foreman_proxy_settingsd_dir}/dynflow.yml
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%{gem_instdir}/settings.d
%{foreman_proxy_bundlerd_dir}/%{plugin_name}.rb
%exclude %{gem_cache}
%exclude %{gem_instdir}/bundler.d
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile

%changelog
* Tue Feb 22 2022 Foreman Packaging Automation <packaging@theforeman.org> 0.7.0-1
- Update to 0.7.0

* Mon Jan 10 2022 Evgeni Golov - 0.6.1-2
- use versioned obsoletes for proxy plugins

* Fri Dec 03 2021 Adam Ruzicka <aruzicka@redhat.com> 0.6.1-1
- Update to 0.6.1

* Thu Nov 11 2021 Adam Ruzicka <aruzicka@redhat.com> 0.6.0-1
- Update to 0.6.0

* Mon Jul 12 2021 Adam Ruzicka <aruzicka@redhat.com> 0.5.2-2
- Do not depend on smart_proxy_dynflow_core

* Thu Jun 24 2021 Adam Ruzicka <aruzicka@redhat.com> 0.5.2-1
- Update to 0.5.2

* Tue Jun 15 2021 Adam Ruzicka <aruzicka@redhat.com> 0.5.1-1
- Update to 0.5.1

* Tue Jun 15 2021 Adam Ruzicka <aruzicka@redhat.com> 0.5.0-1
- Update to 0.5.0

* Mon Jun 07 2021 Adam Ruzicka <aruzicka@redhat.com> 0.4.0-1
- Update to 0.4.0

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.3.0-3
- Rebuild for Ruby 2.7

* Wed Nov 18 2020 Adam Ruzicka <aruzicka@redhat.com> 0.3.0-2
- Loosen dependency on smart_proxy_dynflow_core

* Thu Nov 05 2020 Adam Ruzicka <aruzicka@redhat.com> 0.3.0-1
- Update to 0.3.0

* Mon Jun 22 2020 Evgeni Golov - 0.2.4-6
- Fix bundler.d location on EL8

* Tue May 26 2020 Adam Ruzicka <aruzicka@redhat.com> 0.2.4-5
- Move local state to /var/lib

* Tue May 12 2020 Adam Ruzicka <aruzicka@redhat.com> 0.2.4-4
- Move local state to /var/lib

* Tue Jan 07 2020 Eric D. Helms <ericdhelms@gmail.com> - 0.2.4-3
- Build for SCL

* Mon Nov 18 2019 Eric D. Helms <ericdhelms@gmail.com> - 0.2.4-2
- Update to SCL based template

* Fri Oct 04 2019 Adam Ruzicka <aruzicka@redhat.com> 0.2.4-1
- Update to 0.2.4

* Tue Jun 11 2019 Ivan Nečas <inecas@redhat.com> 0.2.3-1
- Update to 0.2.3

* Thu May 16 2019 Eric D. Helms <ericdhelms@gmail.com> - 0.2.2-2
- Only require tfm- packages on RHEL7

* Mon Jan 14 2019 Ivan Nečas <inecas@redhat.com> 0.2.2-1
- Update to 0.2.2

* Thu Sep 20 2018 Ivan Nečas <inecas@redhat.com> 0.2.1-1
- Update to 0.2.1

* Thu Apr 05 2018 Adam Ruzicka <aruzicka@redhat.com> 0.2.0-1
- Update to 0.2.0

* Mon Jan 29 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.1.10-1
- Bump rubygem-smart_proxy_dynflow{,_core} to 0.1.10 (inecas@redhat.com)

* Tue Jan 23 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.1.9-1
- Bump rubygem-smart_proxy_dynflow{,_core} to 0.1.9
  (ewoud@kohlvanwijngaarden.nl)

* Tue Jan 23 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.1.8-1
- Bump rubygem-smart_proxy_dynflow{,_core} to 0.1.8
  (ewoud@kohlvanwijngaarden.nl)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Tue Aug 15 2017 Eric D. Helms <ericdhelms@gmail.com> 0.1.7-1
- Update smart_proxy_dynflow to 0.1.7 (inecas@redhat.com)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Wed May 10 2017 Dominic Cleal <dominic@cleal.org> 0.1.6-1
- upgrade smart_proxy_dynflow to 0.1.6 (a.ruzicka@outlook.com)
- Remove EL version conditionals (dominic@cleal.org)

* Tue Sep 20 2016 Dominic Cleal <dominic@cleal.org> 0.1.5-1
- Update smart_proxy_dynflow to 0.1.5 (inecas@redhat.com)

* Fri Jun 24 2016 Dominic Cleal <dominic@cleal.org> 0.1.3-1
- Release smart_proxy_dynflow 0.1.3 (stephen@redhat.com)

* Wed Feb 17 2016 Dominic Cleal <dominic@cleal.org> 0.0.7-1
- Release smart_proxy_dynflow 0.0.7 (stbenjam@redhat.com)

* Thu Feb 04 2016 Dominic Cleal <dcleal@redhat.com> 0.0.6-1
- Release smart_proxy_dynflow 0.0.6 (stbenjam@redhat.com)

* Mon Jan 25 2016 Dominic Cleal <dcleal@redhat.com> 0.0.5-1
- Release smart_proxy_dynflow 0.0.5 (stbenjam@redhat.com)

* Tue Oct 06 2015 Dominic Cleal <dcleal@redhat.com> 0.0.4-1
- Release smart_proxy_dynflow 0.0.4 (RPM) (stbenjam@redhat.com)

* Mon Aug 10 2015 Stephen Benjamin <stephen@redhat.com> 0.0.3-1
- Initial release of 0.0.3
