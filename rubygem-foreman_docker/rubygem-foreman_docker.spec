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

%define rubyabi 1.9.1
%global foreman_dir /usr/share/foreman
%global foreman_bundlerd_dir %{foreman_dir}/bundler.d
%global foreman_pluginconf_dir %{foreman_dir}/config/settings.plugins.d

Summary:    A Foreman plugin for Docker container management
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    1.2.3
Release:    1.fm1_9%{?dist}
Group:      Applications/System
License:    GPLv3
URL:        http://github.com/theforeman/foreman-docker
Source0:    http://rubygems.org/downloads/%{gem_name}-%{version}.gem

Requires:   foreman-compute >= 1.6.0
Requires:   %{?scl_prefix}rubygem(docker-api) = 1.17.0
Requires:   %{?scl_prefix}rubygem(wicked) >= 1.1
Requires:   %{?scl_prefix}rubygem(wicked) < 2.0

BuildRequires: foreman-compute >= 1.7.0
BuildRequires: foreman-plugin >= 1.8.0
BuildRequires: %{?scl_prefix}rubygem(docker-api) = 1.17.0
BuildRequires: %{?scl_prefix}rubygem(wicked) >= 1.1
BuildRequires: %{?scl_prefix}rubygem(wicked) < 2.0

%if 0%{?fedora} > 18
Requires: %{?scl_prefix}ruby(release)
%else
Requires: %{?scl_prefix}ruby(abi) >= %{rubyabi}
%endif
Requires: %{?scl_prefix}rubygems

%if 0%{?fedora} > 18
BuildRequires: %{?scl_prefix}ruby(release)
%else
BuildRequires: %{?scl_prefix}ruby(abi) >= %{rubyabi}
%endif
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygems
BuildRequires: foreman-assets

BuildArch: noarch

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-docker
Provides: foreman-docker

%description
This plugin enables provisioning and managing Docker containers and images in
Foreman.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0} --no-rdoc --no-ri
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

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
%doc %{gem_instdir}/README.md

%posttrans
# We need to run the db:migrate after the install transaction
%foreman_db_migrate
%foreman_apipie_cache
%foreman_restart
exit 0

%changelog
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

