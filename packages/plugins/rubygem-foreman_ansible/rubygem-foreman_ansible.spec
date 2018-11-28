%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_ansible
%global plugin_name ansible

Summary: Ansible integration with Foreman (theforeman.org)
Name:    %{?scl_prefix}rubygem-%{gem_name}
Version: 2.2.11
Release: 2%{?foremandist}%{?dist}
Group:   Applications/System
License: GPLv3
URL:     https://github.com/theforeman/foreman_ansible
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: foreman >= 1.17.0

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}rubygems
Requires: %{?scl_prefix}rubygem(deface) < 2.0
Requires: %{?scl_prefix}rubygem(foreman-tasks) >= 0.8
Requires: %{?scl_prefix}rubygem(foreman-tasks) < 1.0
Requires: %{?scl_prefix}rubygem(foreman_ansible_core) >= 2.0.2
Requires: %{?scl_prefix}rubygem(foreman_ansible_core) < 3.0
Requires: %{?scl_prefix}rubygem(foreman_remote_execution) >= 1.5.6
Requires: %{?scl_prefix}rubygem(foreman_remote_execution) < 2.0
Requires: %{?scl_prefix}rubygem(ipaddress) >= 0.8.0
Requires: %{?scl_prefix}rubygem(ipaddress) < 1.0
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems
BuildRequires: %{?scl_prefix}rubygem(deface) < 2.0
BuildRequires: %{?scl_prefix}rubygem(foreman-tasks) >= 0.8
BuildRequires: %{?scl_prefix}rubygem(foreman-tasks) < 1.0
BuildRequires: %{?scl_prefix}rubygem(foreman_ansible_core) >= 2.0.2
BuildRequires: %{?scl_prefix}rubygem(foreman_ansible_core) < 3.0
BuildRequires: %{?scl_prefix}rubygem(foreman_remote_execution) >= 1.4.4
BuildRequires: %{?scl_prefix}rubygem(foreman_remote_execution) < 2.0
BuildRequires: %{?scl_prefix}rubygem(ipaddress) >= 0.8.0
BuildRequires: %{?scl_prefix}rubygem(ipaddress) < 1.0
BuildRequires: npm(react-json-tree) >= 0.1.1
BuildRequires: npm(react-json-tree) < 1.0
BuildRequires: foreman-plugin >= 1.17.0
BuildRequires: foreman-assets >= 1.17.0

BuildArch: noarch

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-%{plugin_name} = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Ansible integration with Foreman.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%{?scl:scl enable %{scl} - << \EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

%foreman_bundlerd_file
%foreman_precompile_plugin -a -s

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_instdir}/app
%{gem_instdir}/config
%{gem_instdir}/db
%{gem_libdir}
%{gem_instdir}/locale
%exclude %{gem_cache}
%{gem_spec}
%{foreman_bundlerd_plugin}
%{foreman_apipie_cache_foreman}
%{foreman_apipie_cache_plugin}
%{foreman_assets_plugin}
%{foreman_webpack_plugin}
%{foreman_webpack_foreman}
%exclude %{gem_instdir}/package.json
%exclude %{gem_instdir}/webpack
%exclude %{gem_instdir}/test

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile

%posttrans
%foreman_db_migrate
%foreman_db_seed
%foreman_apipie_cache
%foreman_restart
exit 0


%changelog
* Wed Nov 28 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.2.11-2
- Rebuild for changed Foreman's vendor.js

* Mon Nov 19 2018 Marek Hulan <mhulan@redhat.com> 2.2.11-1
- Update to 2.2.11

* Wed Oct 31 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.2.9-3
- Revbump to correct source map handling

* Wed Oct 31 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.2.9-2
- Use the license macro
- Remove rpmlint warnings

* Tue Sep 25 2018 Marek Hulan <mhulan@redhat.com> 2.2.9-1
- Update to 2.2.9

* Thu Sep 13 2018 Marek Hulan <mhulan@redhat.com> 2.2.7-1
- Update to 2.2.7

* Mon Sep 10 2018 Eric D. Helms <ericdhelms@gmail.com> - 2.2.6-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Wed Aug 15 2018 Sebastian Gräßl <mail@bastilian.me> 2.2.6-1
- Update to 2.2.6

* Wed Jul 25 2018 Marek Hulan <mhulan@redhat.com> 2.2.5-1
- Update to 2.2.5

* Fri Jul 13 2018 Marek Hulan <mhulan@redhat.com> 2.2.3-1
- Update to 2.2.3

* Thu Jul 12 2018 Marek Hulan <mhulan@redhat.com> 2.2.2-1
- Update to 2.2.2

* Wed Jul 04 2018 Marek Hulan <mhulan@redhat.com> 2.2.1-1
- Update to 2.2.1

* Mon Jul 02 2018 Daniel Lobato Garcia <me@daniellobato.me> 2.2.0-1
- Update to 2.2.0

* Wed Jun 27 2018 Ondrej Prazak <oprazak@redhat.com> 2.1.2-2
- Plugin rebuild

* Fri Apr 06 2018 Daniel Lobato Garcia <me@daniellobato.me> 2.0.4-1
- Update to 2.0.4

* Fri Apr 06 2018 Daniel Lobato Garcia <me@daniellobato.me> 2.0.2-1
- Update to 2.0.2

* Fri Feb 02 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 2.0.1-1
- Bump foreman_ansible to 2.0.1 (me@daniellobato.me)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Fri Apr 07 2017 Dominic Cleal <dominic@cleal.org> 1.4.5-1
- Update foreman_ansible to 1.4.5 (me@daniellobato.me)

* Tue Feb 14 2017 Dominic Cleal <dominic@cleal.org> 1.4.4-1
- Update foreman_ansible to 1.4.4 (me@daniellobato.me)

* Mon Jan 30 2017 Dominic Cleal <dominic@cleal.org> 1.4.2-1
- Update foreman-ansible to 1.4.2 (me@daniellobato.me)

* Fri Jan 20 2017 Dominic Cleal <dominic@cleal.org> 1.4.1-1
- Release foreman_ansible 1.4.1 (me@daniellobato.me)

* Wed Dec 21 2016 Dominic Cleal <dominic@cleal.org> 1.3.1-1
- Update foreman_ansible to 1.3.1 (me@daniellobato.me)

* Mon Dec 05 2016 Dominic Cleal <dominic@cleal.org> 1.3.0-1
- Update foreman-ansible to 1.3.0 (me@daniellobato.me)

* Mon Oct 03 2016 Dominic Cleal <dominic@cleal.org> 1.2.1-1
- Update foreman-ansible to 1.2.1 (me@daniellobato.me)

* Fri Jul 08 2016 Dominic Cleal <dominic@cleal.org> 1.0-1
- plugins:foreman_ansible - 1.0.0 (elobatocs@gmail.com)

* Thu Feb 11 2016 Dominic Cleal <dcleal@redhat.com> 0.3-1
- plugins:foreman_ansible - Release 0.3 (elobatocs@gmail.com)

* Mon Feb 08 2016 Dominic Cleal <dcleal@redhat.com> 0.2.2-2
- Obsolete ruby193 variant from 1.8/1.9 (dcleal@redhat.com)

* Mon Feb 08 2016 Dominic Cleal <dcleal@redhat.com> 0.2.2-1
- Release 0.2.2 (elobatocs@gmail.com)

* Sat Jan 02 2016 Daniel Lobato <elobatocs@gmail.com> 0.2.1-1
- Initial package
