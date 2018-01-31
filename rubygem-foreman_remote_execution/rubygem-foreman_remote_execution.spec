# This package contains macros that provide functionality relating to
# Software Collections. These macros are not used in default
# Fedora builds, and should not be blindly copied or enabled.
# Specifically, the "scl" macro must not be defined in official Fedora
# builds. For more information, see:
# http://docs.fedoraproject.org/en-US/Fedora_Contributor_Documentation
# /1/html/Software_Collections_Guide/index.html

%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_remote_execution

Summary:    Plugin that brings remote execution capabilities to Foreman
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    1.4.5
Release:    1%{?foremandist}%{?dist}
Group:      Applications/System
License:    GPLv3
URL:        https://github.com/theforeman/foreman_remote_execution
Source0:    https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires:   foreman >= 1.15.0

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}rubygems
Requires: %{?scl_prefix}rubygem(dynflow) >= 0.8.10
Requires: %{?scl_prefix}rubygem(dynflow) < 0.9.0
Requires: %{?scl_prefix}rubygem(foreman-tasks) >= 0.9
Requires: %{?scl_prefix}rubygem(foreman_remote_execution_core)
Requires: %{?scl_prefix}rubygem(deface)

BuildRequires: foreman-plugin >= 1.15.0
BuildRequires: foreman-assets
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems
BuildRequires: %{?scl_prefix}rubygem(dynflow) >= 0.8.10
BuildRequires: %{?scl_prefix}rubygem(dynflow) < 0.9.0
BuildRequires: %{?scl_prefix}rubygem(foreman-tasks) >= 0.9
BuildRequires: %{?scl_prefix}rubygem(foreman_remote_execution_core)
BuildRequires: %{?scl_prefix}rubygem(deface)

BuildArch: noarch

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-remote_execution
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
A plugin bringing remote execution to the Foreman, completing the config
management functionality with remote management functionality

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

%{foreman_bundlerd_file}
%foreman_precompile_plugin -a -s

%posttrans
%{foreman_db_migrate}
%{foreman_db_seed}
%{foreman_apipie_cache}
%{foreman_restart}
exit 0

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/%{gem_name}.gemspec
%exclude %{gem_instdir}/Gemfile
%{gem_instdir}/app
%{gem_instdir}/config
%{gem_instdir}/db
%{gem_instdir}/locale
%{gem_instdir}/lib
%{gem_instdir}/public
%{gem_spec}
%{foreman_bundlerd_plugin}
%{foreman_apipie_cache_foreman}
%{foreman_apipie_cache_plugin}
%{foreman_assets_plugin}
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/LICENSE
%exclude %{gem_cache}
%exclude %{gem_instdir}/test

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/doc
%doc %{gem_instdir}/README.md

%changelog
* Wed Jul 26 2017 Eric D. Helms <ericdhelms@gmail.com> 1.3.3-1
- Bump foreman_remote_execution to 1.3.3 (inecas@redhat.com)

* Mon Jul 17 2017 Eric D. Helms <ericdhelms@gmail.com> 1.3.2-1
- Update foreman_remote_execution to 1.3.2 (inecas@redhat.com)

* Wed May 31 2017 Dominic Cleal <dominic@cleal.org> 1.3.1-1
- Update foreman_remote_execution to 1.3.1 (inecas@redhat.com)

* Tue Apr 11 2017 Dominic Cleal <dominic@cleal.org> 1.3.0-1
- Update foreman_remote_execution to 1.3.0 (aruzicka@redhat.com)

* Fri Jan 27 2017 Dominic Cleal <dominic@cleal.org> 1.2.2-1
- Update foreman_remote_execution to 1.2.2 (inecas@redhat.com)

* Tue Sep 20 2016 Dominic Cleal <dominic@cleal.org> 1.2.1-1
- Update foreman_remote_execution to 1.2.1 (inecas@redhat.com)

* Tue Aug 23 2016 Dominic Cleal <dominic@cleal.org> 1.1.0-1
- Update foreman_remote_execution to 1.1.0 (inecas@redhat.com)

* Tue Jul 19 2016 Dominic Cleal <dominic@cleal.org> 1.0.0-1
- Release foreman_remote_execution 1.0 (stephen@redhat.com)

* Wed May 04 2016 Dominic Cleal <dominic@cleal.org> 0.3.2-2
- Use gem_install macro (dominic@cleal.org)

* Thu Apr 28 2016 Dominic Cleal <dominic@cleal.org> 0.3.2-1
- Release foreman_remote_execution 0.3.2 (RPM) (stephen@redhat.com)

* Wed Feb 17 2016 Dominic Cleal <dominic@cleal.org> 0.3.0-1
- Release foreman_remote_execution 0.3.0 (stbenjam@redhat.com)

* Fri Feb 12 2016 Dominic Cleal <dcleal@redhat.com> 0.2.3-1
- Release foreman_remote_execution 0.2.3 (stbenjam@redhat.com)

* Mon Jan 25 2016 Dominic Cleal <dcleal@redhat.com> 0.2.2-1
- Release foreman_remote_execution 0.2.2 (stbenjam@redhat.com)

* Mon Jan 25 2016 Dominic Cleal <dcleal@redhat.com> 0.2.1-1
- Release foreman_remote_execution 0.2.1 (stbenjam@redhat.com)
- Update dependencies to ror SCL (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Fri Nov 13 2015 Dominic Cleal <dcleal@redhat.com> 0.1.1-1
- Update foreman_remote_execution to 0.1.1 (stbenjam@redhat.com)

* Mon Oct 12 2015 Dominic Cleal <dcleal@redhat.com> 0.0.10-1
- Update foreman_remote_execution to 0.0.10 (inecas@redhat.com)

* Tue Oct 06 2015 Dominic Cleal <dcleal@redhat.com> 0.0.7-1
- Release foreman_remote_execution 0.0.7 (stbenjam@redhat.com)

* Mon Sep 14 2015 Dominic Cleal <dcleal@redhat.com> 0.0.6-1
- Release foreman_remote_execution 0.0.6 (stbenjam@redhat.com)

* Wed Sep 02 2015 Dominic Cleal <dcleal@redhat.com> 0.0.5-1
- Release Remote Execution Plugins 0.0.5 (stbenjam@redhat.com)

* Thu Aug 27 2015 Dominic Cleal <dcleal@redhat.com> 0.0.4-1
- Release foreman_remote_execution 0.0.4 (stbenjam@redhat.com)

* Thu Aug 27 2015 Dominic Cleal <dcleal@redhat.com> 0.0.3-2
- Converted to tfm SCL (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 0.0.3-1
- Release foreman_remote_execution 0.0.3 (stbenjam@redhat.com)

* Tue Aug 18 2015 Stephen Benjamin <stephen@redhat.com> 0.0.2-1
- Initial release of 0.0.2
