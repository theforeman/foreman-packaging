# template: foreman_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}
%{!?_root_sysconfdir:%global _root_sysconfdir %{_sysconfdir}}

%global gem_name foreman_rh_cloud
%global plugin_name rh_cloud
%global foreman_min_version 2.5

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 5.0.31
Release: 1%{?foremandist}%{?dist}
Summary: Connects Foreman with Red Hat Cloud services
Group: Applications/Systems
License: GPLv3
URL: https://github.com/theforeman/foreman_rh_cloud
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Autoreq: 0

Obsoletes: %{?scl_prefix}rubygem-redhat_access
Obsoletes: %{?scl_prefix}rubygem-redhat_access_lib

Obsoletes: %{?scl_prefix}rubygem-foreman_inventory_upload
Obsoletes: %{?scl_prefix}rubygem-foreman_inventory_upload-doc

# start specfile generated dependencies
Requires: foreman >= %{foreman_min_version}
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(katello)
Requires: %{?scl_prefix}rubygem(foreman_ansible)
Requires: %{?scl_prefix}rubygem(foreman-tasks)
BuildRequires: foreman-assets >= %{foreman_min_version}
BuildRequires: foreman-plugin >= %{foreman_min_version}
BuildRequires: %{?scl_prefix}rubygem(katello)
BuildRequires: %{?scl_prefix}rubygem(foreman_ansible)
BuildRequires: %{?scl_prefix}rubygem(foreman-tasks)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

# start package.json devDependencies BuildRequires
BuildRequires: %{?scl_prefix}npm(@babel/core) >= 7.7.0
BuildRequires: %{?scl_prefix}npm(@babel/core) < 7.8.0
BuildRequires: %{?scl_prefix}npm(@redhat-cloud-services/frontend-components) >= 2.5.0
BuildRequires: %{?scl_prefix}npm(@redhat-cloud-services/frontend-components) < 3.0.0
BuildRequires: %{?scl_prefix}npm(@theforeman/builder) >= 8.16.0
BuildRequires: %{?scl_prefix}npm(jed) >= 1.1.1
BuildRequires: %{?scl_prefix}npm(jed) < 1.2.0
# end package.json devDependencies BuildRequires

# start package.json dependencies BuildRequires
# end package.json dependencies BuildRequires

%description
Foreman plugin that process & upload data to Red Hat Cloud.


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}.

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
%exclude %{gem_instdir}/package.json
%exclude %{gem_instdir}/webpack
%exclude %{gem_cache}
%{gem_spec}
%{foreman_bundlerd_plugin}
%{foreman_apipie_cache_foreman}
%{foreman_apipie_cache_plugin}
%{foreman_webpack_plugin}
%{foreman_webpack_foreman}
%{foreman_assets_plugin}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
* Thu Jan 27 2022 Shimon Shtein <sshtein@redhat.com> 5.0.31-1
- Update to 5.0.31-1

* Sun Jan 16 2022 Shimon Shtein <sshtein@redhat.com> 5.0.30-1
- Update to 5.0.30-1

* Mon Nov 29 2021 Shimon Shtein <sshtein@redhat.com> 5.0.29-1
- Update to 5.0.29-1

* Thu Nov 04 2021 Shimon Shtein <sshtein@redhat.com> 5.0.28-1
- Update to 5.0.28-1

* Mon Aug 23 2021 Shimon Shtein <sshtein@redhat.com> 4.0.26-1
- Update to 4.0.26-1

* Wed Aug 18 2021 Evgeni Golov - 4.0.25.1-2
- Obsolete redhat_access plugin

* Thu Aug 05 2021 Shimon Shtein <sshtein@redhat.com> 4.0.25.1-1
- Update to 4.0.25.1-1

* Sun Aug 01 2021 Shimon Shtein <sshtein@redhat.com> 4.0.25-1
- Update to 4.0.25-1

* Wed Jul 21 2021 Shimon Shtein <sshtein@redhat.com> 4.0.24.1-1
- Update to 4.0.24.1-1

* Tue Jul 20 2021 Shimon Shtein <sshtein@redhat.com> 4.0.24-1
- Update to 4.0.24-1

* Wed Jun 30 2021 Shimon Shtein <sshtein@redhat.com> 4.0.23-1
- Update to 4.0.23-1

* Tue Jun 15 2021 Ron Lavi <1ronlavi@gmail.com> 4.0.22-1
- Update to 4.0.22-1

* Sun Jun 06 2021 Ron Lavi <1ronlavi@gmail.com> 4.0.21.1-1
- Update to 4.0.21.1-1

* Fri Jun 04 2021 Evgeni Golov 3.0.21.1-1
- Update to 3.0.21.1

* Mon May 31 2021 Ron Lavi <1ronlavi@gmail.com> 3.0.21-1
- Update to 3.0.21-1

* Mon Apr 26 2021 Ron Lavi <1ronlavi@gmail.com> 3.0.20-1
- Update to 3.0.20-1

* Thu Apr 01 2021 Ron Lavi <1ronlavi@gmail.com> 3.0.19-1
- Update to 3.0.19-1

* Wed Mar 17 2021 Ron Lavi <1ronlavi@gmail.com> 3.0.18.1-1
- Update to 3.0.18.1-1

* Mon Feb 22 2021 Ron Lavi <1ronlavi@gmail.com> 3.0.17-1
- Update to 3.0.17-1

* Tue Feb 09 2021 Shimon Shtein <sshtein@redhat.com> 3.0.16-1
- Update to 3.0.16-1

* Tue Feb 02 2021 Ron Lavi <1ronlavi@gmail.com> 3.0.15-1
- Update to 3.0.15

* Thu Nov 26 2020 Ron Lavi <1ronlavi@gmail.com> 3.0.14-1
- Update to 3.0.14-1

* Tue Oct 20 2020 laviro <1ronlavi@gmail.com> 2.0.13.1-1
- Update to 2.0.13.1-1

* Wed Sep 23 2020 Shimon Shtein <sshtein@redhat.com> 2.0.12-1
- Update to 2.0.12-1

* Wed Sep 16 2020 laviro <1ronlavi@gmail.com> 2.0.11-1
- Update to 2.0.11-1

* Tue Aug 04 2020 Shimon Shtein <sshtein@redhat.com> 2.0.10-1
- Update to 2.0.10-1

* Tue Jul 14 2020 Shimon Shtein <sshtein@redhat.com> 2.0.9-1
- Update to 2.0.9-1

* Tue Jun 30 2020 Shimon Shtein <sshtein@redhat.com> 2.0.8-1
- Update to 2.0.8-1

* Mon May 25 2020 Shimon Shtein <sshtein@redhat.com> 2.0.7-1
- Update to 2.0.7-1

* Wed Apr 22 2020 Shimon Shtein <sshtein@redhat.com> 2.0.6-1
- Update to 2.0.6-1

* Tue Apr 07 2020 Shimon Shtein <sshtein@redhat.com> 2.0.5-1
- Update to 2.0.5-1

* Mon Mar 09 2020 Shimon Shtein <sshtein@redhat.com> 2.0.4-1
- Add rubygem-foreman_rh_cloud generated by gem2rpm using the foreman_plugin template

