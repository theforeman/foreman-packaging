# template: foreman_plugin
%global gem_name foreman_puppet
%global plugin_name puppet
%global foreman_min_version 3.13

Name: rubygem-%{gem_name}
Version: 9.0.0
Release: 1%{?foremandist}%{?dist}
Summary: Add Puppet features to Foreman
License: GPLv3
URL: https://github.com/theforeman/foreman_puppet
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: foreman >= %{foreman_min_version}
BuildRequires: foreman-assets >= %{foreman_min_version}
BuildRequires: foreman-plugin >= %{foreman_min_version}
Requires: ruby >= 2.7
Requires: ruby < 4
BuildRequires: ruby >= 2.7
BuildRequires: ruby < 4
BuildRequires: rubygems-devel
BuildArch: noarch
Provides: foreman-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

# start package.json devDependencies BuildRequires
BuildRequires: (npm(@babel/core) >= 7.7.0 with npm(@babel/core) < 8.0.0)
BuildRequires: npm(@theforeman/builder) >= 10.1.0
BuildRequires: (npm(jed) >= 1.1.1 with npm(jed) < 2.0.0)
# end package.json devDependencies BuildRequires

# start package.json dependencies BuildRequires
# end package.json dependencies BuildRequires

%description
Allow assigning Puppet environments and classes to the Foreman Hosts.


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
* Wed Jul 23 2025 Foreman Packaging Automation <packaging@theforeman.org> - 9.0.0-1
- Update to 9.0.0

* Tue Jul 15 2025 Evgeni Golov - 8.1.2-3
- Rebuild for removal of theforeman/vendor

* Tue Jul 15 2025 Evgeni Golov - 8.1.2-2
- Rebuild for removal of theforeman/vendor

* Sun Jul 13 2025 Foreman Packaging Automation <packaging@theforeman.org> - 8.1.2-1
- Update to 8.1.2

* Thu Feb 20 2025 Foreman Packaging Automation <packaging@theforeman.org> - 8.1.1-1
- Update to 8.1.1

* Tue Dec 10 2024 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 8.1.0-1
- Update to 8.1.0

* Thu Sep 12 2024 Foreman Packaging Automation <packaging@theforeman.org> - 8.0.0-1
- Update to 8.0.0

* Thu Sep 05 2024 Evgeni Golov - 7.0.0-2
- Rebuild against Foreman nightly

* Sun Aug 11 2024 Foreman Packaging Automation <packaging@theforeman.org> - 7.0.0-1
- Update to 7.0.0

* Tue May 07 2024 Evgeni Golov - 6.3.0-2
- Rebuild for Webpack asset compression

* Sun Apr 07 2024 Foreman Packaging Automation <packaging@theforeman.org> - 6.3.0-1
- Update to 6.3.0

* Sun Feb 04 2024 Foreman Packaging Automation <packaging@theforeman.org> - 6.2.0-1
- Update to 6.2.0

* Fri Jan 26 2024 Evgeni Golov - 6.1.1-2
- Rebuild for Webpack 5

* Sun Dec 03 2023 Foreman Packaging Automation <packaging@theforeman.org> 6.1.1-1
- Update to 6.1.1

* Sun Sep 17 2023 Foreman Packaging Automation <packaging@theforeman.org> 6.1.0-1
- Update to 6.1.0

* Thu Aug 10 2023 Leos Stejskal <lstejska@redhat.com> 6.0.1-1
- Update to 6.0.1

* Thu Jun 22 2023 Leos Stejskal <lstejska@redhat.com> 6.0.0-2
- Update spec file from latest template

* Mon Jun 12 2023 Leos Stejskal <lstejska@redhat.com> 6.0.0-1
- Update to 6.0.0

* Tue May 16 2023 Nadja Heitmann <nadjah@atix.de> 5.1.2-1
- Update to 5.1.2

* Sun Feb 26 2023 Foreman Packaging Automation <packaging@theforeman.org> 5.1.1-1
- Update to 5.1.1

* Thu Feb 23 2023 Foreman Packaging Automation <packaging@theforeman.org> 5.1.0-1
- Update to 5.1.0

* Tue Nov 22 2022 Ron Lavi <1ronlavi@gmail.com> 5.0.0-1
- Update to 5.0.0

* Thu Sep 01 2022 Ron Lavi <1ronlavi@gmail.com> 4.0.3-1
- Update to 4.0.3

* Wed Aug 24 2022 Evgeni Golov - 4.0.2-2
- Refs #35409 - Include sprockets assets

* Tue Aug 16 2022 Foreman Packaging Automation <packaging@theforeman.org> 4.0.2-1
- Update to 4.0.2

* Fri Jun 03 2022 Nadja Heitmann <nadjah@atix.de> 4.0.1-1
- Update to 4.0.1
- Add ENC preview tab for Host details

* Wed May 25 2022 Nadja Heitmann <nadjah@atix.de> 4.0.0-1
- Add reports tab to Host details
- Update to 4.0.0

* Mon May 09 2022 Evgeni Golov - 3.0.6-2
- log plugin installation in posttrans

* Thu Apr 28 2022 Nadja Heitmann <nadjah@atix.de> 3.0.6-1
- Update to 3.0.6

* Fri Apr 22 2022 Eric D. Helms <ericdhelms@gmail.com> - 3.0.5-2
- Stop generaing apipie cache

* Fri Mar 11 2022 Foreman Packaging Automation <packaging@theforeman.org> 3.0.5-1
- Update to 3.0.5

* Mon Feb 28 2022 Ondřej Ezr <oezr@redhat.com> 3.0.3-1
- Update to 3.0.3

* Fri Nov 26 2021 Ondřej Ezr <oezr@redhat.com> 3.0.0-1
- Update to 3.0.0

* Mon Nov 15 2021 Ondřej Ezr <oezr@redhat.com> 2.0.0-1
- Update to 2.0.0

* Thu Oct 14 2021 Ondřej Ezr <oezr@redhat.com> 2.0.0-0.1.alpha.2
- Update to 2.0.0.alpha.2

* Fri Sep 17 2021 Ondřej Ezr <oezr@redhat.com> 1.0.3-1
- Update to 1.0.3

* Mon Sep 13 2021 Ondřej Ezr <oezr@redhat.com> 1.0.1-1
- Update to 1.0.1

* Fri Sep 10 2021 Ondřej Ezr <oezr@redhat.com> 1.0.0-1
- Update to 1.0.0

* Mon Aug 16 2021 Ondřej Ezr <oezr@redhat.com> 1.0.0.rc.2-1
- Update to 1.0.0.rc.2

* Thu Jul 15 2021 Ondřej Ezr <oezr@redhat.com> 1.0.0.rc.1-1
- Update to 1.0.0.rc.1

* Thu May 20 2021 Manuel Laug <manuel.laug@dm.de> 0.1.0-1
- Update to 0.1.0

* Fri Apr 16 2021 Evgeni Golov - 0.0.2-2
- Drop theforeman/builder upper bound from BuildRequires
- Rebuild for Ruby 2.7

* Tue Feb 02 2021 Ondřej Ezr <oezr@redhat.com> 0.0.2-1
- Add rubygem-foreman_puppet generated by gem2rpm using the foreman_plugin template

