# template: smart_proxy_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%{!?_root_datadir:%global _root_datadir %{_datadir}}
%{!?_root_localstatedir:%global _root_localstatedir %{_localstatedir}}
%{!?_root_sysconfdir:%global _root_sysconfdir %{_sysconfdir}}

%global gem_name smart_proxy_dynflow
%global plugin_name dynflow

%global foreman_proxy_min_version 1.25
%global foreman_proxy_dir %{_root_datadir}/foreman-proxy
%global foreman_proxy_statedir %{_root_localstatedir}/foreman-proxy
%global foreman_proxy_bundlerd_dir %{foreman_proxy_dir}/bundler.d
%global foreman_proxy_settingsd_dir %{_root_sysconfdir}/foreman-proxy/settings.d
%global smart_proxy_dynflow_bundlerd_dir %{!?scl:/opt/theforeman/tfm/root}%{_datadir}/smart_proxy_dynflow_core/bundler.d

Summary: Dynflow runtime for Foreman smart proxy
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.2.4
Release: 2%{?foremandist}%{?dist}
Group: Applications/System
License: GPLv3
URL: https://github.com/theforeman/smart_proxy_dynflow
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

%if 0%{?rhel} == 7
Requires: tfm-rubygem(smart_proxy_dynflow_core) >= 0.2.0
Requires: tfm-rubygem(smart_proxy_dynflow_core) < 0.3.0
%else
Requires: rubygem(smart_proxy_dynflow_core) >= 0.2.0
Requires: rubygem(smart_proxy_dynflow_core) < 0.3.0
%endif

# start specfile generated dependencies
Requires: foreman-proxy >= %{foreman_proxy_min_version}
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-proxy-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

%description
Use the Dynflow inside Foreman smart proxy.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

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
mv %{buildroot}%{gem_instdir}/bundler.plugins.d/%{plugin_name}.rb \
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
%exclude %{gem_instdir}/bundler.plugins.d
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile

%changelog
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
