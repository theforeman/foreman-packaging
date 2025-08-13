# template: foreman_plugin
%global gem_name foreman_scc_manager
%global plugin_name scc_manager
%global foreman_min_version 3.13

Name: rubygem-%{gem_name}
Version: 5.0.1
Release: 1%{?foremandist}%{?dist}
Summary: Suse Customer Center plugin for Foreman
License: GPLv3
URL: https://www.orcharhino.com/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: foreman >= %{foreman_min_version}
BuildRequires: foreman-assets >= %{foreman_min_version}
BuildRequires: foreman-plugin >= %{foreman_min_version}
Requires: ruby
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildRequires: (rubygem(coffee-rails) >= 5.0.0 with rubygem(coffee-rails) < 5.1)
BuildRequires: rubygem(katello) >= 3.16
BuildArch: noarch
Provides: foreman-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

# start package.json devDependencies BuildRequires
BuildRequires: (npm(@babel/core) >= 7.7.0 with npm(@babel/core) < 8.0.0)
BuildRequires: (npm(@theforeman/builder) >= 15.0.0 with npm(@theforeman/builder) < 16.0.0)
# end package.json devDependencies BuildRequires

# start package.json dependencies BuildRequires
# end package.json dependencies BuildRequires

%description
Foreman plugin to sync SUSE Customer Center products and repositories into
Katello.


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
* Wed Aug 13 2025 Foreman Packaging Automation <packaging@theforeman.org> - 5.0.1-1
- Update to 5.0.1

* Wed Aug 13 2025 Foreman Packaging Automation <packaging@theforeman.org> - 5.0.0-1
- Update to 5.0.0

* Tue Jul 15 2025 Evgeni Golov - 4.0.1-2
- Rebuild for removal of theforeman/vendor

* Thu May 08 2025 Foreman Packaging Automation <packaging@theforeman.org> - 4.0.1-1
- Update to 4.0.1

* Mon Oct 14 2024 Foreman Packaging Automation <packaging@theforeman.org> - 4.0.0-1
- Update to 4.0.0

* Fri Aug 02 2024 Nadja Heitmann <nadjah@atix.de> - 3.1.0-1
- Update to 3.1.0

* Tue May 07 2024 Evgeni Golov - 3.0.0-3
- Rebuild for Webpack asset compression

* Wed Jan 31 2024 Evgeni Golov - 3.0.0-2
- Rebuild for Webpack 5

* Fri Jan 05 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.0.0-1
- Update to 3.0.0

* Tue Jun 27 2023 Evgeni Golov 2.3.0-2
- Regenerate RPM spec based on latest template

* Tue Jun 06 2023 Nadja Heitmann <nadjah@atix.de> 2.3.0-1
- Update to 2.3.0
- Major bug fixes for product selection page

* Tue May 16 2023 Nadja Heitmann <nadjah@atix.de> 2.2.3-1
- Update to 2.2.3
- Open up Foreman build dependencies

* Wed Jan 11 2023 Nadja Heitmann <nadjah@atix.de> 2.2.0-1
- Update to 2.2.0
- Fix permission issue for new installations

* Mon Nov 14 2022 Bernhard Suttner <suttner@atix.de> 2.1.0-1
- Update to 2.1.0

* Mon Oct 31 2022 Markus Bucher <bucher@atix.de> 2.0.0-1
- Update to 2.0.0
- Introducing new SCC product selection page

* Wed Aug 24 2022 Evgeni Golov - 1.8.20-2
- Refs #35409 - Include sprockets assets

* Thu Jun 02 2022 Nadja Heitmann <nadjah@atix.de> 1.8.20-1
- Update to 1.8.20
- Support upstream_authentication_token for Katello > 4.3

* Fri Apr 29 2022 Nadja Heitmann <nadjah@atix.de> 1.8.19-1
- Update to 1.8.19
- Use default_download_policy for scc repositories

* Fri Apr 22 2022 Nadja Heitmann <nadjah@atix.de> 1.8.18-1
- Update to 1.8.18
- Bug fix: Update all Katello repositories originating from one SCC repository

* Fri Apr 22 2022 Eric D. Helms <ericdhelms@gmail.com> - 1.8.17-2
- Stop generaing apipie cache

* Tue Feb 01 2022 Nadja Heitmann <heitmann@atix.de> 1.8.17-1
- Update to 1.8.17
- Allow for new mirroring_policy setting in Katello >= 4.3

* Wed Dec 08 2021 Nadja Heitmann <heitmann@atix.de> 1.8.16-1
- Update to 1.8.16
- Fix migration bug for Katello >= 4.2

* Mon Dec 06 2021 Nadja Heitmann <heitmann@atix.de> 1.8.15-1
- Update to 1.8.15
- Katello 4.2 compliance

* Tue Sep 21 2021 Nadja Heitmann <heitmann@atix.de> 1.8.12-1
- Update to 1.8.12
- Minor bug fixes

* Wed Jul 14 2021 Nadja Heitmann <heitmann@atix.de> 1.8.10-1
- Update to 1.8.10
- Bug fixes

* Thu Apr 29 2021 Nadja Heitmann <heitmann@atix.de> 1.8.9-1
- Update to 1.8.9
- Update to work with Katello 3.18 and Foreman 2.3

* Mon Mar 15 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.8.8-2
- Rebuild for Ruby 2.7

* Wed Mar 10 2021 Nadja Heitmann <heitmann@atix.de> 1.8.8-1
- Update to 1.8.8
- Fix migrations bug

* Tue Mar 02 2021 Nadja Heitmann <heitmann@atix.de> 1.8.7-1
- Update to 1.8.7
- Prevent SCC manager to delete subscribed SCC products if subscription expires
- Fix dynflow output for failed SCC account sync tasks
- Shorten automatically created Katello root repository labels

* Thu Dec 10 2020 Nadja Heitmann <heitmann@atix.de> 1.8.6-1
- Update to 1.8.6
- Add automatic GPG key support for SCC accounts
- Make titles and descriptions of SCC products more readable
- Minor beautifications and bug fixes

* Wed Nov 04 2020 Markus Bucher <bucher@atix.de> 1.8.5-1
- Update to 1.8.5
- Fix display of product list for foreman >=2.0
- Remove products without repositories from product-selection

* Mon May 04 2020 ATIX AG <info@atix.de> 1.8.4-1
- looser gem dependency on rails
- Update to 1.8.4

* Wed Mar 25 2020 Markus Bucher <bucher@atix.de> 1.8.3-1
- Update to 1.8.3
- Fix test-connection in http-proxy-scenario
- Improve logging

* Tue Mar 17 2020 Markus Bucher <bucher@atix.de> 1.8.2-1
- Update to 1.8.2
- Encrypt password in foreman-tasks

* Mon Mar 16 2020 Markus Bucher <bucher@atix.de> 1.8.1-1
- Update to 1.8.1
- Fix test-connection button
- Add role descriptions

* Fri Feb 07 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.8.0-3
- Update spec to remove missed ror scl

* Wed Jan 22 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.8.0-2
- Update spec to remove the ror scl

* Wed Jan 22 2020 Markus Bucher <bucher@atix.de> 1.8.0-1
- Update to 1.8.0

* Fri Jan 17 2020 Eric D. Helms <ericdhelms@gmail.com> - 1.7.0-3
- Drop posttrans macros

* Tue Nov 19 2019 Markus Bucher <bucher@atix.de> - 1.7.0-2
- Add apipie-cache generation

* Tue Nov 12 2019 Markus Bucher <bucher@atix.de> 1.7.0-1
- Update to 1.7.0
- Add API

* Thu Sep 19 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.6.3-2
- Regenerate spec based on the latest foreman_plugin gem2rpm template

* Wed Aug 07 2019 Markus Bucher <bucher@atix.de> 1.6.3-1
- Update to 1.6.3
- Fix update non-existing repositories

* Mon May 06 2019 Markus Bucher <bucher@atix.de> 1.6.2-1
- Update to 1.6.2
- Add recurring-sync of repositories

* Wed Mar 06 2019 Markus Bucher <bucher@atix.de> 1.6.1-1
- Update to 1.6.1
- Fix product delete issue

* Mon Jan 14 2019 Markus Bucher <bucher@atix.de> 1.6.0-1
- Update to 1.6.0
- Improve Foreman 1.20 support

* Thu Dec 13 2018 Markus Bucher <bucher@atix.de> 1.5.1-1
- Update to 1.5.1
- Fix for Foreman 1.20

* Wed Sep 12 2018 Bryan Kearney <bryan.kearney@gmail.com> - 1.4.0-3
- Move licenes which are GPL-* to GPLv3

* Tue Sep 11 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.4.0-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Tue Aug 07 2018 Matthias Dellweg <dellweg@atix.de> 1.4.0-1
- Raise compatibility to foreman 1.18
* Wed May 16 2018 Matthias Dellweg <dellweg@atix.de> 1.3.1-1
- Migration to rails 5 by evgeni
- Fix issue with productless account
* Tue May 15 2018 Matthias Dellweg <dellweg@atix.de> 1.3.0-1
- Prevent exception in case no further products were selected
- Show proper sync status
* Mon Mar 19 2018 Matthias Dellweg <dellweg@atix.de> 1.2.0-1
- Change Edit/Action behaviour to be more user-friendly
- Do not use transaction to create Products and Repositories
- Update some dependencies
- Bump requirement to Katello 3.5
- Issue #7 by prokhorovva: Fast fix
- Catch RecordNotFound when assigning extensions
- disable submit if account was not synced
- Bump requirement to foreman 1.16
* Tue Sep 26 2017 Matthias Dellweg <dellweg@atix.de> 1.1.0-1
- Set default download policy
- Force katello to load before scc_manager
- restart foreman-tasks after installation
- Added note to use Organization credentials
- Select organization landing page
* Wed Aug 16 2017 Matthias Dellweg <dellweg@atix.de> 1.0.1-1
- specfile from gem2spec
- fix asset compilation
- encrypted passwords
- use katello_proxy

* Thu Apr 27 2017 Matthias Dellweg <dellweg@atix.de> 1.0.0-3
- Add dependency foreman-tasks

* Mon Apr 03 2017 Bernhard Suttner <suttner@atix.de> 1.0.0-2
- Set correct ruby build requirements

* Tue Mar 21 2017 Matthias Dellweg <dellweg@atix.de> 1.0.0-1
- First release
