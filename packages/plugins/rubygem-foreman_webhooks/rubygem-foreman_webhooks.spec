# template: foreman_plugin
%global gem_name foreman_webhooks
%global plugin_name webhooks
%global foreman_min_version 3.13

Name: rubygem-%{gem_name}
Version: 4.0.1
Release: 2%{?foremandist}%{?dist}
Summary: Configure webhooks for Foreman
License: GPLv3
URL: https://github.com/theforeman/foreman_webhooks
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: foreman >= %{foreman_min_version}
BuildRequires: foreman-assets >= %{foreman_min_version}
BuildRequires: foreman-plugin >= %{foreman_min_version}
Requires: ruby >= 2.7.0
BuildRequires: ruby >= 2.7.0
BuildRequires: rubygems-devel
BuildArch: noarch
Provides: foreman-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

# start package.json devDependencies BuildRequires
BuildRequires: (npm(@babel/core) >= 7.7.0 with npm(@babel/core) < 8.0.0)
BuildRequires: npm(@theforeman/builder) >= 0
BuildRequires: (npm(jed) >= 1.1.1 with npm(jed) < 2.0.0)
# end package.json devDependencies BuildRequires

# start package.json dependencies BuildRequires
# end package.json dependencies BuildRequires

%description
Plugin for Foreman that allows to configure Webhooks.


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
* Tue Jul 15 2025 Evgeni Golov - 4.0.1-2
- Rebuild for removal of theforeman/vendor

* Wed Feb 19 2025 Foreman Packaging Automation <packaging@theforeman.org> - 4.0.1-1
- Update to 4.0.1

* Fri Sep 13 2024 Foreman Packaging Automation <packaging@theforeman.org> - 4.0.0-1
- Update to 4.0.0

* Wed Jul 24 2024 Adam Ruzicka <aruzicka@redhat.com> - 3.2.3-1
- Update to 3.2.3

* Tue May 07 2024 Evgeni Golov - 3.2.2-3
- Rebuild for Webpack asset compression

* Wed Jan 31 2024 Evgeni Golov - 3.2.2-2
- Rebuild for Webpack 5

* Wed Nov 15 2023 Adam Ruzicka <aruzicka@redhat.com> 3.2.2-1
- Update to 3.2.2

* Wed Aug 09 2023 Oleh Fedorenko <ofedoren@redhat.com> 3.2.1-1
- Update to 3.2.1

* Tue Jun 27 2023 Oleh Fedorenko <ofedoren@redhat.com> 3.2.0-1
- Update to 3.2.0

* Thu May 25 2023 Oleh Fedorenko <ofedoren@redhat.com> 3.1.0-2
- Remove SCL macros

* Tue Mar 21 2023 Oleh Fedorenko <ofedoren@redhat.com> 3.1.0-1
- Update to 3.1.0

* Sun Sep 11 2022 Foreman Packaging Automation <packaging@theforeman.org> 3.0.5-1
- Update to 3.0.5

* Wed Aug 24 2022 Evgeni Golov - 3.0.4-2
- Refs #35409 - Include sprockets assets

* Wed Aug 17 2022 Oleh Fedorenko <ofedoren@redhat.com> 3.0.4-1
- Update to 3.0.4

* Fri Jun 03 2022 Oleh Fedorenko <ofedoren@redhat.com> 3.0.3-1
- Update to 3.0.3

* Mon May 09 2022 Evgeni Golov - 3.0.1-3
- log plugin installation in posttrans

* Fri Apr 22 2022 Eric D. Helms <ericdhelms@gmail.com> - 3.0.1-2
- Stop generaing apipie cache

* Mon Mar 07 2022 Ron Lavi <1ronlavi@gmail.com> 3.0.1-1
- Update to 3.0.1

* Wed Sep 01 2021 Lukas Zapletal <lzap+rpm@redhat.com> 3.0.0-1
- Update to 3.0.0

* Mon May 24 2021 Lukas Zapletal <lzap+rpm@redhat.com> 2.0.0-1
- Update to 2.0.0

* Fri Apr 23 2021 Lukas Zapletal <lzap+rpm@redhat.com> 1.0.0-1
- Update to 1.0.0

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.0.3-2
- Rebuild plugins for Ruby 2.7

* Mon Mar 29 2021 Lukas Zapletal <lzap+rpm@redhat.com> 0.0.3-1
- Update to 0.0.3

* Mon Mar 08 2021 Lukas Zapletal <lzap+rpm@redhat.com> 0.0.2-1
- Update to 0.0.2

* Mon Jan 25 2021 Lukas Zapletal <lzap+rpm@redhat.com> 0.0.1-1
- Initial version
