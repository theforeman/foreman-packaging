# template: foreman_plugin
%global gem_name foreman_rh_cloud
%global plugin_name rh_cloud
%global foreman_min_version 3.13

Name: rubygem-%{gem_name}
Version: 12.1.5
Release: 1%{?foremandist}%{?dist}
Summary: Connects Foreman with Red Hat Cloud services
License: GPLv3
URL: https://github.com/theforeman/foreman_rh_cloud
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
BuildRequires: rubygem(foreman_ansible) >= 15.0.0
BuildRequires: rubygem(foreman-tasks) >= 10.0.0
BuildRequires: rubygem(katello) >= 4.14.0.rc1.1
BuildArch: noarch
Provides: foreman-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

# start package.json devDependencies BuildRequires
BuildRequires: (npm(@babel/core) >= 7.7.0 with npm(@babel/core) < 8.0.0)
BuildRequires: npm(@theforeman/builder) >= 15.0.1
BuildRequires: (npm(jed) >= 1.1.1 with npm(jed) < 1.2.0)
# end package.json devDependencies BuildRequires

# start package.json dependencies BuildRequires
BuildRequires: (npm(@scalprum/core) >= 0.8.1 with npm(@scalprum/core) < 1.0.0)
BuildRequires: (npm(@scalprum/react-core) >= 0.9.3 with npm(@scalprum/react-core) < 1.0.0)
# end package.json dependencies BuildRequires

%description
Foreman plugin that process & upload data to Red Hat Cloud.


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
* Tue Jul 22 2025 Chris Roberts <chrobert@redhat.com> - 12.1.5-1
- Update to 12.1.5

* Tue Jul 15 2025 Chris Roberts <chrobert@redhat.com> - 12.1.4-1
- Update to 12.1.4

* Tue Jul 15 2025 Evgeni Golov - 12.1.3-2
- Rebuild for removal of theforeman/vendor

* Wed Jul 09 2025 Chris Roberts <chrobert@redhat.com> - 12.1.3-1
- Update to 12.1.3

* Tue Jul 01 2025 Chris Roberts <chrobert@redhat.com> - 12.1.2-1
- Update to 12.1.2

* Tue Jun 03 2025 Chris Roberts <chrobert@redhat.com> - 12.1.1-1
- Update to 12.1.1

* Tue May 20 2025 Odilon Sousa <osousa@redhat.com> - 12.1.0-2
- Drop unversioned obsoletes

* Tue May 06 2025 Chris Roberts <chrobert@redhat.com> - 12.1.0-1
- Update to 12.1.0

* Tue Apr 01 2025 Foreman Packaging Automation <packaging@theforeman.org> - 12.0.0-1
- Update to 12.0.0

* Mon Mar 24 2025 Chris Roberts <chrobert@redhat.com> - 11.3.0-1
- Update to 11.3.0

* Mon Mar 10 2025 Chris Roberts <chrobert@redhat.com> - 11.2.0-1
- Update to 11.2.0

* Mon Feb 03 2025 Chris Roberts <chrobert@redhat.com> - 11.1.0-1
- Update to 11.1.0

* Mon Nov 25 2024 Chris Roberts <chrobert@redhat.com> - 11.0.3-1
- Update to 11.0.3

* Tue Oct 29 2024 Foreman Packaging Automation <packaging@theforeman.org> - 11.0.2-1
- Update to 11.0.2

* Wed Sep 25 2024 Foreman Packaging Automation <packaging@theforeman.org> - 11.0.1-1
- Update to 11.0.1

* Mon Sep 23 2024 Evgeni Golov - 11.0.0-2
- Enable AutoReq for rh_cloud

* Fri Sep 20 2024 Chris Roberts <chrobert@redhat.com> - 11.0.0-1
- Update to 11.0.0

* Mon Sep 09 2024 Chris Roberts <chrobert@redhat.com> - 10.0.2-1
- Update to 10.0.2

* Tue Jun 25 2024 Chris Roberts <chrobert@redhat.com> - 10.0.1-1
- Update to 10.0.1

* Mon Apr 29 2024 Chris Roberts <chrobert@redhat.com> - 9.0.56-1
- Update to 9.0.56

* Wed Jan 31 2024 Evgeni Golov - 9.0.55-2
- Rebuild for Webpack 5

* Tue Jan 16 2024 Chris Roberts <chrobert@redhat.com> - 9.0.55-1
- Update to 9.0.55

* Tue Dec 19 2023 Chris Roberts <chrobert@redhat.com> 9.0.54-1
- Update to 9.0.54

* Tue Dec 12 2023 Chris Roberts <chrobert@redhat.com> 9.0.53-1
- Update to 9.0.53

* Mon Nov 13 2023 Chris Roberts <chrobert@redhat.com> 9.0.52-1
- Update to 9.0.52

* Thu Oct 12 2023 Shimon Shtein <sshtein@redhat.com> 9.0.51-1
- Update to 9.0.51-1

* Wed Aug 02 2023 Shimon Shtein <sshtein@redhat.com> 8.0.48-1
- Update to 8.0.48

* Sun Jun 25 2023 Foreman Packaging Automation <packaging@theforeman.org> 8.0.47-1
- Update to 8.0.47

* Sun Jun 11 2023 Shimon Shtein <sshtein@redhat.com> 8.0.46-1
- Update to 8.0.46

* Sun Mar 19 2023 Foreman Packaging Automation <packaging@theforeman.org> 7.0.46-1
- Update to 7.0.46

* Sun Jan 22 2023 Foreman Packaging Automation <packaging@theforeman.org> 7.0.45-1
- Update to 7.0.45

* Sun Dec 04 2022 Foreman Packaging Automation <packaging@theforeman.org> 6.0.44-1
- Update to 6.0.44

* Thu Sep 15 2022 Shimon Shtein <sshtein@redhat.com> 6.0.43-1
- Update to 6.0.43-1

* Wed Aug 24 2022 Evgeni Golov - 5.0.39-2
- Refs #35409 - Include sprockets assets

* Mon Jun 13 2022 Evgeni Golov 5.0.39-1
- Update to 5.0.39

* Thu May 26 2022 Foreman Packaging Automation <packaging@theforeman.org> 5.0.37-1
- Update to 5.0.37

* Thu May 19 2022 Shimon Shtein <sshtein@redhat.com> 5.0.36-1
- Update to 5.0.36-1

* Wed May 11 2022 Shimon Shtein <sshtein@redhat.com> 5.0.35-1
- Update to 5.0.35-1

* Tue Apr 26 2022 Shimon Shtein <sshtein@redhat.com> 5.0.34-1
- Update to 5.0.34-1

* Tue Apr 26 2022 Shimon Shtein <sshtein@redhat.com> 5.0.34-1
- Update to 5.0.34-1

* Fri Apr 22 2022 Eric D. Helms <ericdhelms@gmail.com> - 5.0.33-2
- Stop generaing apipie cache

* Thu Apr 14 2022 Shimon Shtein <sshtein@redhat.com> 5.0.33-1
- Update to 5.0.33-1

* Thu Mar 10 2022 Shimon Shtein <sshtein@redhat.com> 5.0.32-1
- Update to 5.0.32-1

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

