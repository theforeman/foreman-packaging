# template: foreman_plugin
%global gem_name foreman_leapp
%global plugin_name leapp
%global foreman_min_version 3.16

Name: rubygem-%{gem_name}
Version: 3.0.0
Release: 1%{?foremandist}%{?dist}
Summary: A Foreman plugin for Leapp utility
License: GPLv3
URL: https://github.com/theforeman/foreman_leapp
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: foreman >= %{foreman_min_version}
BuildRequires: foreman-assets >= %{foreman_min_version}
BuildRequires: foreman-plugin >= %{foreman_min_version}
Requires: ruby
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildRequires: rubygem(foreman_remote_execution) >= 8.1.1
BuildRequires: rubygem(foreman_ansible) >= 5.0
BuildArch: noarch
Provides: foreman-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

# start package.json devDependencies BuildRequires
BuildRequires: (npm(@babel/core) >= 7.7.0 with npm(@babel/core) < 8.0.0)
BuildRequires: npm(@theforeman/builder) >= 12.0.1
# end package.json devDependencies BuildRequires

# start package.json dependencies BuildRequires
# end package.json dependencies BuildRequires

%description
A Foreman plugin to support inplace RHEL upgrades with Leapp utility.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
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
* Mon Jul 28 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.0.0-1
- Update to 3.0.0

* Tue Jul 15 2025 Evgeni Golov - 2.0.5-2
- Rebuild for removal of theforeman/vendor

* Sun Jul 06 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2.0.5-1
- Update to 2.0.5

* Thu Feb 20 2025 Foreman Packaging Automation <packaging@theforeman.org> - 2.0.4-1
- Update to 2.0.4

* Wed Dec 18 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.0.3-1
- Update to 2.0.3

* Wed Dec 11 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.0.2-1
- Update to 2.0.2

* Wed Oct 09 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.0.1-1
- Update to 2.0.1

* Thu Sep 12 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.0.0-1
- Update to 2.0.0

* Tue May 07 2024 Evgeni Golov - 1.2.1-2
- Rebuild for Webpack asset compression

* Sun Apr 07 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.2.1-1
- Update to 1.2.1

* Wed Feb 14 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.2.0-1
- Update to 1.2.0

* Wed Jan 31 2024 Evgeni Golov - 1.1.1-2
- Rebuild for Webpack 5

* Sun Dec 03 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.1.1-1
- Update to 1.1.1

* Sun Oct 29 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.1.0-1
- Update to 1.1.0

* Tue Jun 27 2023 Leos Stejskal <lstejska@redhat.com> 1.0.0-2
- Regenerate RPM spec based on latest template

* Thu Jun 22 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.0.0-1
- Update to 1.0.0

* Wed May 10 2023 Foreman Packaging Automation <packaging@theforeman.org> 0.1.14-1
- Update to 0.1.14

* Thu Feb 09 2023 Leos Stejskal <lstejska@redhat.com> 0.1.13-1
- Update to 0.1.13

* Mon Jan 23 2023 Leos Stejskal <lstejska@redhat.com> 0.1.12-1
- Update to 0.1.12

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

