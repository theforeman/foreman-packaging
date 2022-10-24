# template: foreman_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}
%{!?_root_sysconfdir:%global _root_sysconfdir %{_sysconfdir}}

%global gem_name foreman_leapp
%global plugin_name leapp
%global foreman_min_version 2.1

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.1.11
Release: 1%{?foremandist}%{?dist}
Summary: A Foreman plugin for Leapp utility
Group: Applications/Systems
License: GPLv3
URL: https://github.com/oamg/foreman_leapp
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: foreman >= %{foreman_min_version}
Requires: ruby
BuildRequires: foreman-assets >= %{foreman_min_version}
BuildRequires: foreman-plugin >= %{foreman_min_version}
Requires: ruby
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildArch: noarch
Provides: foreman-plugin-%{plugin_name} = %{version}
BuildRequires: rubygem(foreman_remote_execution) >= 3.2
BuildRequires: rubygem(foreman_ansible) >= 5.0
# end specfile generated dependencies

# start package.json devDependencies BuildRequires
BuildRequires: npm(@babel/core) >= 7.7.0
BuildRequires: npm(@babel/core) < 8.0.0
BuildRequires: npm(@theforeman/builder) >= 8.3.3
BuildRequires: npm(@theforeman/builder) < 9.0.0
# end package.json devDependencies BuildRequires

# start package.json dependencies BuildRequires
BuildRequires: npm(react-ellipsis-with-tooltip) >= 1.0.8
BuildRequires: npm(react-ellipsis-with-tooltip) < 2.0.0
# end package.json dependencies BuildRequires

%description
A Foreman plugin to support inplace RHEL 7 -> RHEL 8 upgrades with Leapp
utility.

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
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%foreman_bundlerd_file
%foreman_precompile_plugin -s

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
%{foreman_assets_plugin}
%{foreman_assets_foreman}
%{foreman_webpack_plugin}
%{foreman_webpack_foreman}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%posttrans
%{foreman_plugin_log}

%changelog
* Mon Oct 24 2022 Leos Stejskal <lstejska@redhat.com> 0.1.11-1
- Update to 0.1.11

* Wed Aug 24 2022 Evgeni Golov - 0.1.10-3
- Refs #35409 - Include sprockets assets

* Mon May 09 2022 Evgeni Golov - 0.1.10-2
- log plugin installation in posttrans

* Thu Apr 28 2022 Evgeni Golov 0.1.10-1
- Update to 0.1.10
- Stop generaing apipie cache

* Thu Dec 09 2021 Leos Stejskal <lstejska@redhat.com> 0.1.9-1
- Update to 0.1.9

* Thu Dec 09 2021 Leos Stejskal <lstejska@redhat.com> 0.1.8-1
- Update to 0.1.8

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.1.7-2
- Rebuild plugins for Ruby 2.7

* Tue Mar 30 2021 Leos Stejskal <lstejska@redhat.com> 0.1.7-1
- Update to 0.1.7

* Fri Sep 25 2020 Leos Stejskal <lstejska@redhat.com> 0.1.6-1
- Update to 0.1.6

* Thu Sep 10 2020 Leos Stejskal <lstejska@redhat.com> 0.1.5-1
- Update to 0.1.5

* Mon Aug 24 2020 Marek Hulan <mhulan@redhat.com> 0.1.4-1
- Update to 0.1.4

* Tue Jun 09 2020 Leos Stejskal <lstejska@redhat.com> 0.1.3-1
- Update to 0.1.3

* Tue May 12 2020 Leos Stejskal <lstejska@redhat.com> 0.1.2-1
- Update to 0.1.2

* Mon May 11 2020 Leos Stejskal <lstejska@redhat.com> 0.1.1-1
- Update to 0.1.1

* Fri May 08 2020 Leos Stejskal <lstejska@redhat.com> 0.1.0-1
- Update to 0.1.0

* Tue Apr 21 2020 Leos Stejskal <lstejska@redhat.com> 0.0.6-1
- Update to 0.0.6

* Thu Apr 16 2020 Leos Stejskal <lstejska@redhat.com> 0.0.5-1
- Update to 0.0.5

* Thu Apr 16 2020 Leos Stejskal <lstejska@redhat.com> 0.0.4-1
- Update to 0.0.4

* Thu Apr 16 2020 Leos Stejskal <lstejska@redhat.com> 0.0.3-1
- Update to 0.0.3

* Tue Apr 14 2020 Leos Stejskal <lstejska@redhat.com> 0.0.2-1
- Update to 0.0.2

* Wed Apr 08 2020 Leos Stejskal <lstejska@redhat.com> 0.0.1-1
- Add rubygem-foreman_leapp generated by gem2rpm using the foreman_plugin template

