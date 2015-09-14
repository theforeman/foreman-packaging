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

%define rubyabi 1.9.1

Summary:    Plugin that brings remote execution capabilities to Foreman
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    0.0.6
Release:    1%{?foremandist}%{?dist}
Group:      Applications/System
License:    GPLv3
URL:        http://github.com/theforeman/foreman_remote_execution
Source0:    http://rubygems.org/downloads/%{gem_name}-%{version}.gem

Requires:   foreman >= 1.9.0

%if 0%{?fedora} > 18
Requires: %{?scl_prefix_ruby}ruby(release)
%else
Requires: %{?scl_prefix_ruby}ruby(abi) >= %{rubyabi}
%endif
Requires: %{?scl_prefix_ruby}rubygems
Requires: %{?scl_prefix}rubygem(foreman-tasks) >= 0.7.3
Requires: %{?scl_prefix}rubygem(foreman-tasks) < 0.8.0
Requires: %{?scl_prefix_ruby}rubygem(rails) >= 3.2.8
Requires: %{?scl_prefix_ruby}rubygem(rails) < 3.3.0

%if 0%{?fedora} > 18
BuildRequires: %{?scl_prefix_ruby}ruby(release)
%else
BuildRequires: %{?scl_prefix_ruby}ruby(abi) >= %{rubyabi}
%endif
BuildRequires: foreman-plugin >= 1.9.0
BuildRequires: foreman-assets
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems
BuildRequires: %{?scl_prefix}rubygem(foreman-tasks) >= 0.7.3
BuildRequires: %{?scl_prefix}rubygem(foreman-tasks) < 0.8.0
BuildRequires: %{?scl_prefix_ruby}rubygem(rails) >= 3.2.8
BuildRequires: %{?scl_prefix_ruby}rubygem(rails) < 3.3.0

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
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0} --rdoc
%{?scl:"}

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
