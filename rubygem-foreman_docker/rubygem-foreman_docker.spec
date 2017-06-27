# This package contains macros that provide functionality relating to
# Software Collections. These macros are not used in default
# Fedora builds, and should not be blindly copied or enabled.
# Specifically, the "scl" macro must not be defined in official Fedora
# builds. For more information, see:
# http://docs.fedoraproject.org/en-US/Fedora_Contributor_Documentation
# /1/html/Software_Collections_Guide/index.html

%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_docker

%global foreman_dir /usr/share/foreman
%global foreman_bundlerd_dir %{foreman_dir}/bundler.d
%global foreman_pluginconf_dir %{foreman_dir}/config/settings.plugins.d

Summary:    A Foreman plugin for Docker container management
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    3.2.0
Release:    1%{?foremandist}%{?dist}
Group:      Applications/System
License:    GPLv3
URL:        http://github.com/theforeman/foreman-docker
Source0:    http://rubygems.org/downloads/%{gem_name}-%{version}.gem

Requires:   foreman-compute >= 1.15.0
Requires:   %{?scl_prefix}rubygem(docker-api) >= 1.18.0
Requires:   %{?scl_prefix}rubygem(docker-api) < 2.0
Requires:   %{?scl_prefix}rubygem(wicked) >= 1.1
Requires:   %{?scl_prefix}rubygem(wicked) < 2.0
Requires:   %{?scl_prefix}rubygem(deface) < 2.0
Requires:   %{?scl_prefix}rubygem(excon) >= 0.46
Requires:   %{?scl_prefix}rubygem(excon) < 1.0

BuildRequires: foreman-compute >= 1.15.0
BuildRequires: foreman-plugin >= 1.15.0
BuildRequires: %{?scl_prefix}rubygem(docker-api) >= 1.18.0
BuildRequires: %{?scl_prefix}rubygem(docker-api) < 2.0
BuildRequires: %{?scl_prefix}rubygem(wicked) >= 1.1
BuildRequires: %{?scl_prefix}rubygem(wicked) < 2.0
BuildRequires: %{?scl_prefix}rubygem(deface) < 2.0
BuildRequires: %{?scl_prefix}rubygem(excon) >= 0.46
BuildRequires: %{?scl_prefix}rubygem(excon) < 1.0

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}rubygems

BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems
BuildRequires: foreman-assets

BuildArch: noarch

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-docker
Provides: foreman-docker
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
This plugin enables provisioning and managing Docker containers and images in
Foreman.

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
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

# Fix version to match the full docker-api package version, as auto-requires
# generates a dep of "= 1.17" that can't be resolved by yum
sed -i '/docker-api/ s/"= 1\.17"/"= 1.17.0"/' %{buildroot}%{gem_spec}

%foreman_bundlerd_file
%foreman_precompile_plugin -a -s

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_instdir}/app
%{gem_instdir}/config
%{gem_instdir}/db
%{gem_instdir}/locale
%{gem_spec}
%{foreman_bundlerd_plugin}
%{foreman_apipie_cache_foreman}
%{foreman_apipie_cache_plugin}
%{foreman_assets_plugin}
%doc %{gem_instdir}/LICENSE

%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/test
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%posttrans
# We need to run the db:migrate after the install transaction
%foreman_db_migrate
%foreman_apipie_cache
%foreman_restart
exit 0

%changelog
* Mon Jun 19 2017 Eric D. Helms <ericdhelms@gmail.com> 3.1.0-1
- Updated foreman_docker to 3.1.0 (me@daniellobato.me)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Mon Aug 01 2016 Eric D Helms <ericdhelms@gmail.com> 3.0.0-1
- plugins: foreman-docker 3.0.0 (elobatocs@gmail.com)

* Fri Apr 15 2016 Dominic Cleal <dominic@cleal.org> 2.1.1-1
- plugins:foreman_docker - 2.1.1 (elobatocs@gmail.com)

* Mon Jan 18 2016 Dominic Cleal <dcleal@redhat.com> 2.0.1-1
- plugins:foreman_docker - Release 2.0.1 (elobatocs@gmail.com)

* Wed Jan 06 2016 Dominic Cleal <dcleal@redhat.com> 2.0.0-2
- Fix docker-api dependency version number in gemspec (dcleal@redhat.com)

* Wed Jan 06 2016 Dominic Cleal <dcleal@redhat.com> 2.0.0-1
- plugins:foreman_docker - Release 2.0.0 (elobatocs@gmail.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Thu Aug 27 2015 Dominic Cleal <dcleal@redhat.com> 1.4.1-2
- Converted to tfm SCL (dcleal@redhat.com)

* Wed Aug 19 2015 Dominic Cleal <dcleal@redhat.com> 1.4.1-1
- plugins:foreman_docker - Release 1.4.1 (elobatocs@gmail.com)

* Tue Jul 28 2015 Dominic Cleal <dcleal@redhat.com> 1.4.0-2
- Use foremandist macro in release (dcleal@redhat.com)

* Fri Jul 24 2015 Dominic Cleal <dcleal@redhat.com> 1.4.0-1.fm1_10
- Update foreman_docker to 1.4.0 (dcleal@redhat.com)

* Wed Apr 29 2015 Dominic Cleal <dcleal@redhat.com> 1.3.1-1.fm1_9
- plugins:foreman_docker - Release 1.3.1 (elobatocs@gmail.com)

* Wed Apr 29 2015 Dominic Cleal <dcleal@redhat.com> 1.3.0-1.fm1_9
- plugins:foreman_docker - Release 1.3.0 (elobatocs@gmail.com)
- Partially revert "Better branched builds with Foreman version macro"
  (dcleal@redhat.com)

* Thu Apr 23 2015 Dominic Cleal <dcleal@redhat.com> 1.2.4-2
- Use foremandist macro in release (dcleal@redhat.com)

* Wed Mar 25 2015 Dominic Cleal <dcleal@redhat.com> 1.2.4-1.fm1_9
- plugins:foreman_docker - Release 1.2.4 (elobatocs@gmail.com)
- Min of foreman 1.8.0 due to post-install scriptlet (dcleal@redhat.com)

* Fri Mar 20 2015 Dominic Cleal <dcleal@redhat.com> 1.2.3-1.fm1_9
- Update foreman_docker to 1.2.3 (dcleal@redhat.com)

* Wed Mar 11 2015 Daniel Lobato Garcia <dlobatog@redhat.com> 1.2.2-1.fm1_8
- Updating the version of foreman_docker to 1.2.2

* Wed Mar 04 2015 Dominic Cleal <dcleal@redhat.com> 1.2.1-2.fm1_8
- Precompile foreman_docker API docs (dcleal@redhat.com)

* Tue Mar 03 2015 Daniel Lobato Garcia <dlobatog@redhat.com> 1.2.1-1
- Updating the version of foreman_docker to 1.2.1

* Tue Feb 24 2015 Daniel Lobato Garcia <dlobatog@redhat.com> 1.2.0-1
- Updating the version of foreman_docker to 1.2.0
- docker-api dependency listed to 1.17 minimum

* Mon Feb 23 2015 Dominic Cleal <dcleal@redhat.com> 1.1.0-2
- Default options in foreman_precompile_plugin changed (rubygem-foreman_docker)
  (martin.bacovsky@gmail.com)

* Tue Feb 10 2015 Daniel Lobato Garcia <dlobatog@redhat.com> 1.1.0-1
- Support katello content views to create containers

* Thu Feb 5 2015 Daniel Lobato Garcia <dlobatog@redhat.com> 1.0.1-1
- Fixes for 1.7 compatibility
- Do not list the assets directory twice. (slukasik@redhat.com)

* Mon Jan 12 2015 Daniel Lobato Garcia <dlobatog@redhat.com> 1.0.0-1
- Updating the version of foreman_docker to 1.0.0

* Wed Nov 05 2014 Dominic Cleal <dcleal@redhat.com> 0.2.0-2
- Precompile foreman_docker assets (dcleal@redhat.com)

* Mon Nov 3 2014 Daniel Lobato Garcia <dlobatog@redhat.com> 0.2.0-1
- Updating the version of foreman_docker to 0.2.0

* Tue Oct 21 2014 David Davis <daviddavis@redhat.com> 0.1.0-1
- Updating the version of foreman_docker to 0.1.0

* Tue Apr 29 2014 Dominic Cleal <dcleal@redhat.com> 0.0.3-1
- new package built with tito
