%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name runcible

Name:           %{?scl_prefix}rubygem-%{gem_name}
Version:        2.13.1
Release:        2%{?dist}
Summary:        A gem exposing Pulp's juiciest parts
Group:          Applications/System
License:        MIT
URL:            https://github.com/Katello/runcible
Source0:        https://rubygems.org/downloads/%{gem_name}-%{version}.gem

BuildArch:  noarch
Provides:   %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

Requires:  %{?scl_prefix}rubygem(rest-client) < 3.0.0
Requires:  %{?scl_prefix}rubygem(oauth)
Requires:  %{?scl_prefix}rubygem(i18n) >= 0.5.0
Requires:  %{?scl_prefix}rubygem(activesupport) >= 3.0.10
Requires:  %{?scl_prefix_ruby}rubygem(json)
Requires:  %{?scl_prefix_ruby}ruby(release)
Requires:  %{?scl_prefix_ruby}ruby(rubygems)

BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems

%description
A gem to expose Pulp's juiciest parts.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Summary:    Documentation for rubygem-%{gem_name}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}

%description doc
This package contains documentation for rubygem-%{gem_name}

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
mkdir -p %{buildroot}%{gem_docdir}

%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%{gem_instdir}/Rakefile
%{gem_instdir}/Gemfile
%exclude %{gem_cache}
%{gem_spec}
%license %{gem_instdir}/LICENSE

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/CONTRIBUTING.md

%changelog
* Mon Mar 15 2021 Eric D. Helms <ericdhelms@gmail.com> - 2.13.1-2
- Rebuild for Ruby 2.7

* Thu Apr 30 2020 Justin Sherrill <jsherril@redhat.com> 2.13.1-1
- Update to 2.13.1

* Fri Feb 21 2020 Partha Aji <paji@redhat.com> 2.13.0-1
- Update to 2.13.0

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.12.1-2
- Update spec to remove the ror scl

* Thu Sep 05 2019 Eric D. Helms <ericdhelms@gmail.com> - 2.12.1-1
- Release rubygem-runcible 2.12.1

* Fri Aug 30 2019  Justin Sherrill 2.12.0-1
- Update to 2.12.0

* Tue Mar 19 2019 Justin Sherrill 2.11.1-1
- Update to 2.11.1

* Mon Jan 21 2019 Evgeni Golov 2.11.0-1
- Update to 2.11.0

* Tue Nov 27 2018 Justin Sherrill <jsherril@redhat.com> - 2.10.1-1
- 2.10.1 release

* Mon Nov 26 2018 Justin Sherrill <jsherril@redhat.com> - 2.10.0-1
- 2.10.0 release

* Fri Sep 07 2018 Eric D. Helms <ericdhelms@gmail.com> - 2.9.0-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Tue Sep 04 2018 Justin Sherrill <jsherril@redhat.com> 2.9.0-1
- Update to 2.9.0

* Mon May 21 2018 Justin Sherrill <jsherril@redhat.com> 2.8.1-1
- Update package to 2.8.1

* Wed Jan 10 2018 Eric D. Helms <ericdhelms@gmail.com> 2.6.0-2
- Update katello packages for Rails 5.1 (ericdhelms@gmail.com)

* Mon Dec 11 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 2.6.0-1
- rubygem-runcible 2.6.0 build (jsherril@redhat.com)

* Mon Nov 20 2017 Justin Sherrill <jsherril@redhat.com> 2.5.0-1
- Runcible 2.5.0 (jsherril@redhat.com)

* Tue Nov 14 2017 Justin Sherrill <jsherril@redhat.com> 2.4.0-1
- runcible 2.4.0

* Mon Oct 30 2017 Eric D. Helms <ericdhelms@gmail.com> 2.3.0-1
- rubygem-runcible 2.3.0 build (jsherril@redhat.com)

* Fri Oct 13 2017 Eric D. Helms <ericdhelms@gmail.com> 2.2.0-1
- Runcible 2.2.0 (jsherril@redhat.com)

* Mon Aug 07 2017 Justin Sherrill <jsherril@redhat.com> 2.1.0-1
- runcible 2.1.0 build (jsherril@redhat.com)

* Tue Apr 25 2017 Justin Sherrill <jsherril@redhat.com> 2.0.0-1
- Update rest client requirement for runcible (jsherril@redhat.com)
- Upgrade to runcible 2.0 (jsherril@redhat.com)

* Wed Mar 29 2017 Eric D. Helms <ericdhelms@gmail.com> 1.11.0-1
- Update rubygem-runcible to 1.11.0 (ericdhelms@gmail.com)

* Thu Mar 23 2017 Justin Sherrill <jsherril@redhat.com> 1.10.0-1
- Runcible 1.10.0 (jsherril@redhat.com)
- Use gem_install macro (ericdhelms@gmail.com)

* Wed Mar 01 2017 Eric D Helms <ericdhelms@gmail.com> 1.9.3-1
- rubygem-runcible 1.9.3 (jsherril@redhat.com)

* Wed Feb 22 2017 Eric D Helms <ericdhelms@gmail.com> 1.9.2-1
- runcible 1.9.2 (jsherril@redhat.com)

* Mon Nov 21 2016 Justin Sherrill <jsherril@redhat.com> 1.9.1-1
- runcible-1.9.1 build (jsherril@redhat.com)

* Wed Sep 07 2016 Justin Sherrill <jsherril@redhat.com> 1.9.0-1
- build runcible 1.9.0 (jsherril@redhat.com)

* Tue Jul 26 2016 Eric D Helms <ericdhelms@gmail.com> 1.8.0-1
- Update Runcible to 1.8.0 (#258) (eric.d.helms@gmail.com)

* Tue Apr 26 2016 Justin Sherrill <jsherril@redhat.com> 1.7.2-3
- more ror42 builds (jsherril@redhat.com)

* Tue Apr 26 2016 Justin Sherrill <jsherril@redhat.com> 1.7.2-2
- rebuilding for ruby on rails 4.2 (jsherril@redhat.com)

* Mon Apr 18 2016 Justin Sherrill <jsherril@redhat.com> 1.7.2-1
- runcible 1.7.2 build (jsherril@redhat.com)

* Thu Apr 14 2016 Justin Sherrill <jsherril@redhat.com> 1.7.1-1
- Runcible 1.7.1 build (jsherril@redhat.com)

* Fri Mar 11 2016 Eric D Helms <ericdhelms@gmail.com> 1.7.0-1
- Update runcible to 1.7.0 (paji@redhat.com)

* Thu Feb 04 2016 Eric D Helms <ericdhelms@gmail.com> 1.6.0-1
- Update runcible to 1.6.0 (paji@redhat.com)

* Mon Feb 01 2016 Eric D Helms <ericdhelms@gmail.com> 1.5.0-1
- Update runcible to 1.5.0 (paji@redhat.com)

* Wed Jan 06 2016 Eric D. Helms <ericdhelms@gmail.com> 1.4.0-3
- rubygem-runcible requires referenced wrong SCL (ericdhelms@gmail.com)

* Wed Jan 06 2016 Eric D. Helms <ericdhelms@gmail.com> 1.4.0-2
- Build rubygem-runcible for rh22 SCL (ericdhelms@gmail.com)

* Thu Oct 29 2015 Eric D. Helms <ericdhelms@gmail.com> 1.4.0-1
- Update runcible to 1.4.0 (paji@redhat.com)

* Thu Aug 27 2015 Eric D. Helms <ericdhelms@gmail.com> 1.3.5-3
- Update rubygem-runcible to tfm SCL (ericdhelms@gmail.com)

* Wed Jul 29 2015 Eric D. Helms <ericdhelms@gmail.com> 1.3.5-2
- new package built with tito

* Fri Mar 27 2015 Justin Sherrill <jsherril@redhat.com> 1.3.3-1
- bumping version to 1.3.3 (jsherril@redhat.com)

* Fri Mar 27 2015 Justin Sherrill <jsherril@redhat.com> 1.3.2-1
- locking to rest-client less than 1.8 (jsherril@redhat.com)

* Tue Feb 03 2015 Justin Sherrill <jsherril@redhat.com> 1.3.1-1
- addresses #9179 - fix tests for Pulp 2.6 (mmccune@redhat.com)
- Refs #7617 - Fixed a docker distributor issue (paji@redhat.com)
- Refs #8759 - Running runcible against pulp 2.5.1 (daviddavis@redhat.com)
- Merge pull request #92 from jlsherrill/build_script (jlsherrill@gmail.com)
- adding release script (jsherril@redhat.com)

* Wed Nov 05 2014 Justin Sherrill <jsherril@redhat.com> 1.3.0-1
- Fixes #8079 - Can update docker tags in repository (paji@redhat.com)
- only support debugger on ruby 1.9.3 (jsherril@redhat.com)
- fixing runcible errors caused by rubocop changes (jsherril@redhat.com)
- Fixes #7880 - Rubocop enabled the runcible tests (paji@redhat.com)
- Ref #7880: Rubocop fixes update (paji@redhat.com)
- Fixes #7880 - Add rubocop to runcible (daviddavis@redhat.com)

* Wed Oct 08 2014 Justin Sherrill <jsherril@redhat.com> 1.2.0-1
- Fixes #7765 - Add docker methods to repo (daviddavis@redhat.com)
- Fixes #7617 - CRUD docker repo bindings (paji@redhat.com)
* Thu May 15 2014 Justin Sherrill <jsherril@redhat.com> 1.1.0-1
- Bumping runcible version to 1.1.0 (jsherril@redhat.com)
- adding support for pulp 2.4.0-0.14 (jsherril@redhat.com)
- adding consumer(group) support for pulp2.4 (jsherril@redhat.com)
- Updating runcible to use one cassette per test (jsherril@redhat.com)
- 2.4 support and some cleanup for all most remaining items
  (jsherril@redhat.com)
- Worked on splitting up user and role cassettes (daviddavis@redhat.com)
- Created a cassette_name method for test classes (daviddavis@redhat.com)

* Thu Jan 16 2014 Justin Sherrill <jsherril@redhat.com> 1.0.8-1
- adding a config method for retrieving current configuration
  (jsherril@redhat.com)

* Fri Sep 20 2013 Justin Sherrill <jsherril@redhat.com> 1.0.7-1
- adding new applicabilty features from pulp 2.3 (jsherril@redhat.com)
- Upgrading pulp to 2.3 (daviddavis@redhat.com)
- adding puppet_install_distributor and running the model tests
  (mmccune@redhat.com)
- adding orphan file listing and deleting (jsherril@redhat.com)

* Wed Sep 11 2013 Justin Sherrill <jsherril@redhat.com> 1.0.6-1
- Runcible: Fix upload_bits method (daviddavis@redhat.com)
- allowing hash to be passed for package actions, instead of only name
  (jsherril@redhat.com)

* Wed Aug 21 2013 Partha Aji <paji@redhat.com> 1.0.5-1
- Version bump (paji@redhat.com)
- Added some mods to get copy call accept filters (paji@redhat.com)

* Thu Aug 15 2013 Justin Sherrill <jsherril@redhat.com> 1.0.4-1
- Removing duplicate distributor method (daviddavis@redhat.com)
- Puppet: Adding in missing method to distributor (daviddavis@redhat.com)
- Adding support for f19 in rel-eng (daviddavis@redhat.com)
- Puppet: Fixing a bug and writing a test for it (daviddavis@redhat.com)
- initial node support (jsherril@redhat.com)

* Mon Aug 12 2013 David Davis <daviddavis@redhat.com> 1.0.3-1
- Bump to 1.0.3 (daviddavis@redhat.com)
- Updating cassettes (daviddavis@redhat.com)
- Fixing and reorganizing puppet repo tests (daviddavis@redhat.com)
- Puppet: Wrote some tests and fixed repo methods (daviddavis@redhat.com)
- Merge pull request #95 from mptap/package_uploads (jlsherrill@gmail.com)
- Add Package Upload Pulp API support to runcible (mtapaswi@redhat.com)
- Puppet: Adding distributor and importer tests (daviddavis@redhat.com)
- Puppet: Using new 1.0 architecture for puppet classes (daviddavis@redhat.com)
- Merge branch 'master' into puppet (daviddavis@redhat.com)
- Fixing repository importer code (daviddavis@redhat.com)
- Merge commit '54f9d7bc4655f0a783b5aeacc580b8db2b09935d' into puppet-merge
  (daviddavis@redhat.com)
- puppet: initial support for puppet repositories (bbuckingham@redhat.com)

* Sun Aug 04 2013 Justin Sherrill <jsherril@redhat.com> 1.0.2-1
- bumping gem version (jsherril@redhat.com)

* Sun Aug 04 2013 Justin Sherrill <jsherril@redhat.com> 1.0.1-1
- renamed lazy_config= parameter (dmitri@appliedlogic.ca)
- a tiny fix in README (dmitri@appliedlogic.ca)
- added IoC way of configuring of  runcible (dmitri@appliedlogic.ca)
- adding requirement documentation for pulp-katello-plugin related items
  (jsherril@redhat.com)
- attempting full request of rpmids as it is much faster (jsherril@redhat.com)
- fixing broken test (jsherril@redhat.com)
- Merge pull request #83 from jlsherrill/multi (jlsherrill@gmail.com)
- Merge pull request #84 from parthaa/filter-clauses (parthaa@gmail.com)
- Added code make unit copy accept custom filters (paji@redhat.com)
- removing untested rake task as its no longer reliable (jsherril@redhat.com)
- Changing runcible to support multiple pulp servers. (jsherril@redhat.com)
- adding support for yum_clone_distributor (jsherril@redhat.com)
- Fixing cassette clearing and test update (daviddavis@redhat.com)
- Improving some of the tests for pulp 2.2 and regenerating cassettes
  (jsherril@redhat.com)
- automatically clear cassettes when running in all mode (jsherril@redhat.com)
- Pulp v2.2: Fixing individual tests for Pulp 2.2 (daviddavis@redhat.com)
- Updating Readme to include steps for an official release. (ehelms@redhat.com)

* Tue Jul 30 2013 Justin Sherrill <jsherril@redhat.com> 0.4.12-1
- adding support for yum_clone_distributor (jsherril@redhat.com)
- Improving some of the tests for pulp 2.2 and regenerating cassettes
  (jsherril@redhat.com)
- Pulp v2.2: Fixing individual tests for Pulp 2.2 (daviddavis@redhat.com)
- Updating Readme to include steps for an official release. (ehelms@redhat.com)

* Tue Jul 02 2013 Brad Buckingham <bbuckingham@redhat.com> 0.4.11-1
- bumping release to 0.4.11 (bbuckingham@redhat.com)
- consumer/group - update to allow for update all (bbuckingham@redhat.com)

* Thu Jun 13 2013 Justin Sherrill <jsherril@redhat.com> 0.4.10-1
- adding yum_repo_metadata_file unit type (jsherril@redhat.com)
- adds timeout config values and pass to rest client (jsherril@redhat.com)
- 969457: Do not timeout on getting all #rpm_ids (git@pitr.ch)
- 955706 - update vcr_cassettes for pulp-server-2.1.2-0.1.beta
  (bbuckingham@redhat.com)
- 955706 - consumer_groups - add passing of additional options
  (bbuckingham@redhat.com)
- 955706 - update runcible to support pulp-server-2.1.2-0.1.beta
  (bbuckingham@redhat.com)

* Tue Jun 04 2013 Justin Sherrill <jsherril@redhat.com> 0.4.9-1
- adding more options for various actions (jsherril@redhat.com)
- Docs - Updating how to build and deploy documentation. (ehelms@redhat.com)
- Showing a better config error message (daviddavis@redhat.com)

* Wed May 22 2013 Justin Sherrill <jsherril@redhat.com> 0.4.8-1
- adding additional importer/distributor options (jsherril@redhat.com)
- requiring older minitest (jsherril@redhat.com)
- adding readme and contributing to gemspec (jsherril@redhat.com)
- adding new files to gemfile, and bumping for new release
  (jsherril@redhat.com)
- adding method to easily check the status of a publish (mmccune@redhat.com)
- adding export distributor so we can initiate ISO exports (mmccune@redhat.com)

* Wed May 15 2013 Justin Sherrill <jsherril@redhat.com> 0.4.7-1
- new package built with tito

* Mon May 13 2013 Miroslav Suchý <msuchy@redhat.com> 0.4.5-1
- enable SCL builds

* Fri May 03 2013 Justin Sherrill <jsherril@redhat.com> 0.4.4-2
- consumer - specify different unit key based on content type
  (bbuckingham@redhat.com)

* Fri May 03 2013 Justin Sherrill <jsherril@redhat.com> 0.4.4-1
- consumer - specify different unit key based on content type
  (bbuckingham@redhat.com)

* Tue Apr 23 2013 Justin Sherrill <jsherril@redhat.com> 0.4.3-1
- fixing gem version (jsherril@redhat.com)

* Tue Apr 23 2013 Justin Sherrill <jsherril@redhat.com> 0.4.2-1
- unit copy - updates for pulp improvements in unit associate/copy
  (bbuckingham@redhat.com)
- consumer - updates to support applicable errata (bbuckingham@redhat.com)
- Adding ISO repo support (jsherril@redhat.com)

* Mon Mar 25 2013 Justin Sherrill <jsherril@redhat.com> 0.4.1-1
- removing 1.8.7 support (jsherril@redhat.com)
- adding repo group support (jsherril@redhat.com)
- Pulp 2.1 - Adding fixes to support the previous errors around package group
  unit copy.  This commit is against a beta build of 2.1 (ericdhelms@gmail.com)
- Pulp2.1 - Adding note with link to current stable Runcible branch.
  (ericdhelms@gmail.com)
- Pulp 2.1 - Adding two API calls to handle content applicability for
  consumers. (ericdhelms@gmail.com)
- Pulp2.1 - Updates to how consumer group content tests are handled to test
  them properly. (ericdhelms@gmail.com)
- comply with Fedora Guidelines (msuchy@redhat.com)
- Fixes logging=true option during testing based off the previous changes to
  requiring the logger to be based off the Ruby standard logger API.
  (ericdhelms@gmail.com)
- only request ids of errata and rpms for errata_id/rpm_id functions
  (jsherril@redhat.com)
- allowing running of single test by filename (jsherril@redhat.com)

* Thu Feb 28 2013 Miroslav Suchý <msuchy@redhat.com> 0.3.3-4
- use scl_prefix for setup macro (msuchy@redhat.com)
- use upstream builder (msuchy@redhat.com)

* Thu Feb 28 2013 Miroslav Suchý <msuchy@redhat.com> 0.3.3-3
- tar.gz is created form package name, address this for SC (msuchy@redhat.com)

* Thu Feb 28 2013 Miroslav Suchý <msuchy@redhat.com> 0.3.3-2
- convert spec file using spec2scl to support SC (msuchy@redhat.com)

* Tue Feb 05 2013 Justin Sherrill <jsherril@redhat.com> 0.3.3-1
- dropping version requirement for runcible (jsherril@redhat.com)
- Changes license reference from Eric to Red Hat for consistency.
  (ehelms@redhat.com)

* Mon Feb 04 2013 Justin Sherrill <jsherril@redhat.com> 0.3.2-1
- Logging - Test update. (ehelms@redhat.com)
- Logging - Updates to prevent logging twice in the event an exception is
  thrown when the log level is at debug. (ehelms@redhat.com)
- Gemspec cleanup by moving dependencies into the gemspec file.
  (ehelms@redhat.com)
- Updates logging code to allow logging of all requests (debug mode) and a
  special exceptions mode for only logging to a provided logger calls that
  generate exceptions. (ehelms@redhat.com)
- Updates readme to include new test option. (ehelms@redhat.com)
- Moves primary tests into top level test directory and re-factors the test
  commands to account for the changes. Resources and extension suites may now
  be run separately now. (ehelms@redhat.com)
- Adds environment variable to allow running full test suite against a live
  Pulp without recording new cassettes. (ehelms@redhat.com)
- Updates README to include a section on building and releasin gem or RPM.
  (ehelms@redhat.com)
- being less restrictive on activesupport version in Gemfile
  (jsherril@redhat.com)
- being less restrictive on activesupport version (jsherril@redhat.com)
- Renamed test methods to quiten travis (paji@redhat.com)
- Redid the tests to make em more explicit (paji@redhat.com)
- Fixed a test (paji@redhat.com)
- Accidental blooper where I missed a method name (paji@redhat.com)
- Added some cosmetic changes for clarity (paji@redhat.com)
- Updated unit tests to make travis happy (paji@redhat.com)
- Removed accidental space (paji@redhat.com)
- Updated content unassociate calls to be based of unit_id or content_id
  (paji@redhat.com)
- Moved the copy and unassociate logic to a more centralized location
  (paji@redhat.com)

* Wed Jan 16 2013 Justin Sherrill <jsherril@redhat.com> 0.3.1-1
- version bump to 0.3.1 (jsherril@redhat.com)
- fixes #35 - correctly default to include repos info in unit finds
  (jsherril@redhat.com)

* Fri Jan 11 2013 Eric D Helms <ehelms@redhat.com> 0.3.0-1
- Version bump. (ehelms@redhat.com)
- Adds tests for content_type. (ehelms@redhat.com)
- Updates to how the content type is declared for extensions. Test updates.
  (ehelms@redhat.com)
- Series of documentation updates for extensions that include the addition of a
  base Unit extension that all content types inherit from. (ehelms@redhat.com)
- Updating to first Pulp V2.0 stable build. (ehelms@redhat.com)
- minor version bump (jsherril@redhat.com)
- cassette update (jsherril@redhat.com)
- fixing package category test
- adding package group copy (jsherril@redhat.com)
- Automatic commit of package [rubygem-runcible] release [0.2.0-1].
  (ehelms@redhat.com)
- Spec file updates to remove redundant directory declarations.
  (ehelms@redhat.com)

* Mon Nov 19 2012 Eric D Helms <ehelms@redhat.com> 0.2.0-1
- Spec file updates to remove redundant directory declarations.
  (ehelms@redhat.com)
- Version bump. (ehelms@redhat.com)
- cassette updates (jsherril@redhat.com)
- sleep longer for fewer waiting tasks (jsherril@redhat.com)
- fixing errata copy by unit id (jsherril@redhat.com)
- cassette updates (jsherril@redhat.com)
- fixing typo in rakefile (jsherril@redhat.com)
- adding errata test (jsherril@redhat.com)
- cassette updates (jsherril@redhat.com)
- do not sleep if were running as none (jsherril@redhat.com)
- switching to primarily use unit ids for errata (jsherril@redhat.com)
- Assert - Cleans up copy/paste fail on a test name and associated tests.
  (ehelms@redhat.com)
- Asserts - Cleans up the asserts in extensions. (ehelms@redhat.com)
- Asserts - Cleans up the asserts to use more minitest asserts in resources to
  provide more friendly output. (ehelms@redhat.com)
- Updates readme with link to github pages. (ehelms@redhat.com)
- Doc - Adds references to the latest Pulp doc location for each entity.
  (ehelms@redhat.com)
- Fixes broken reference. (ehelms@redhat.com)
- DOC - Adds documentation for all resources. (ehelms@redhat.com)
- Fixes for none mode test runs. (ehelms@redhat.com)
- Pulp Beta - Updates to handle Repository deletion and consumer unbind as
  tasks to remove chance for race condition. (ehelms@redhat.com)
- Pulp Beta - Adds missing cassettes and updates test data. (ehelms@redhat.com)
- Updates to the latest pulp beta and fixes all associated tests.
  (ehelms@redhat.com)
- Docs - Adds yard doc for repository. (ehelms@redhat.com)
- Updates to fix missing cassette and switches each content type to extend Unit
  resource. (ehelms@redhat.com)
- Version bump. (ehelms@redhat.com)
- Merge branch 'master' of github.com:Katello/runcible (ehelms@redhat.com)
- Updates test data to reflect added tests. (ehelms@redhat.com)
- Adds and cleans-up functions that having missing or mis-named tests.
  (ehelms@redhat.com)
- Updates Travis to fail if there are untested functions. (ehelms@redhat.com)
- Adds rake task to find functions without corresponding test functions.
  (ehelms@redhat.com)
- cassette update (jsherril@redhat.com)
- do not use sorting for unit search, as mongo may fail (jsherril@redhat.com)
- Updating pulp version (paji@redhat.com)

* Mon Nov 19 2012 Eric D Helms <ehelms@redhat.com> 0.2.0-1
- Version bump. (ehelms@redhat.com)
- cassette updates (jsherril@redhat.com)
- sleep longer for fewer waiting tasks (jsherril@redhat.com)
- fixing errata copy by unit id (jsherril@redhat.com)
- cassette updates (jsherril@redhat.com)
- fixing typo in rakefile (jsherril@redhat.com)
- adding errata test (jsherril@redhat.com)
- cassette updates (jsherril@redhat.com)
- do not sleep if were running as none (jsherril@redhat.com)
- switching to primarily use unit ids for errata (jsherril@redhat.com)
- Assert - Cleans up copy/paste fail on a test name and associated tests.
  (ehelms@redhat.com)
- Asserts - Cleans up the asserts in extensions. (ehelms@redhat.com)
- Asserts - Cleans up the asserts to use more minitest asserts in resources to
  provide more friendly output. (ehelms@redhat.com)
- Updates readme with link to github pages. (ehelms@redhat.com)
- Doc - Adds references to the latest Pulp doc location for each entity.
  (ehelms@redhat.com)
- Fixes broken reference. (ehelms@redhat.com)
- DOC - Adds documentation for all resources. (ehelms@redhat.com)
- Fixes for none mode test runs. (ehelms@redhat.com)
- Pulp Beta - Updates to handle Repository deletion and consumer unbind as
  tasks to remove chance for race condition. (ehelms@redhat.com)
- Pulp Beta - Adds missing cassettes and updates test data. (ehelms@redhat.com)
- Updates to the latest pulp beta and fixes all associated tests.
  (ehelms@redhat.com)
- Docs - Adds yard doc for repository. (ehelms@redhat.com)
- Updates to fix missing cassette and switches each content type to extend Unit
  resource. (ehelms@redhat.com)
- Version bump. (ehelms@redhat.com)
- Merge branch 'master' of github.com:Katello/runcible (ehelms@redhat.com)
- Updates test data to reflect added tests. (ehelms@redhat.com)
- Adds and cleans-up functions that having missing or mis-named tests.
  (ehelms@redhat.com)
- Updates Travis to fail if there are untested functions. (ehelms@redhat.com)
- Adds rake task to find functions without corresponding test functions.
  (ehelms@redhat.com)
- cassette update (jsherril@redhat.com)
- do not use sorting for unit search, as mongo may fail (jsherril@redhat.com)
- Updating pulp version (paji@redhat.com)

* Fri Nov 02 2012 Eric D. Helms <ehelms@redhat.com> 0.1.3-1
- Version bump. (ehelms@redhat.com)
- Cassette updates for tests. (ehelms@redhat.com)
- Fixes broken publish_all call and adds tests for publish and publish_all.
  (ehelms@redhat.com)
- Adding files to make travis happy in theory (paji@redhat.com)
- Changed the 'options' parameter to be  empty hash instead of a string since
  pulp expects that (paji@redhat.com)
- Changed the check for 'logging' suite name as suggested (paji@redhat.com)
- Replaced all the GPL licenses with MIT as requested by eric (paji@redhat.com)
- Fixed merge conflicts and regenerated yml cassettes (paji@redhat.com)
- Updated the required yml to make the runcible tests run (paji@redhat.com)
- Fixed a few consumer group tests (paji@redhat.com)
- Travis - Adds testing against 1.9.3 (ehelms@redhat.com)
- Merge branch 'master' of github.com:Katello/runcible (ehelms@redhat.com)
- Ruby 1.9.3 - Updates to get code and tests passing on both Ruby 1.8.7 and
  Ruby 1.9.3 (ehelms@redhat.com)
- Added calls in extensions to simplify adding and removing consumers from
  consumer groups (paji@redhat.com)
- Added consumer group associate and unassociate calls (paji@redhat.com)
- cassette update (jsherril@redhat.com)
- adding support for repository ids as part of repository unit listing
  (jsherril@redhat.com)
- fixing issue with sync cancel not working properly (jsherril@redhat.com)

* Thu Oct 25 2012 Eric D. Helms <ehelms@redhat.com> 0.1.2-1
- Version bump. (ehelms@redhat.com)
- Updates README indentation for code blocks and moves all Copyrights to Red
  Hat. (ehelms@redhat.com)
- Updates README to include configuration and examples. (ehelms@redhat.com)
- Updates to add bold emphasis to pulp version in README. (ehelms@redhat.com)
- Adds Rake task to grab pulp version and input to the README.
  (ehelms@redhat.com)
- Adds missing errata test and cassette. (ehelms@redhat.com)
- Moves helpers to be under test/support. (ehelms@redhat.com)
- Adds missing cassette file. (ehelms@redhat.com)
- Merge branch 'master' of github.com:Katello/runcible (ehelms@redhat.com)
- Merge pull request #13 from parthaa/consumer-groups (ericdhelms@gmail.com)
- Initial set of runcible consumer group bindings (paji@redhat.com)
- Added  consumer tests for content install/update/uninstall (paji@redhat.com)
- Moves fixtures to be under test/fixtures instead of test/integration.
  (ehelms@redhat.com)
- Fixed repo sync schedule based tests (paji@redhat.com)
- Adding back previously deleted test files. (ehelms@redhat.com)
- Misc Fixes to get pulp artifacts running (paji@redhat.com)
- Patch to get all tests running right in live mode (paji@redhat.com)
- Tweaked the tests to pass in the 'none' mode (paji@redhat.com)
- Split up the extension/resources tests in  different files (paji@redhat.com)
- Fixed consumer unit tests based on comments offered in the pull
  (paji@redhat.com)
- Moved the binding methods to follow the runcible convention of separate calls
  (paji@redhat.com)
- Reverting a previous change on this file (paji@redhat.com)
- Merge branch 'master' into pulp-consumer-changes (paji@redhat.com)
- Added tests for consumer API (paji@redhat.com)
- Changes to deal with pulp-server-0.0.331-1.fc16.noarch (paji@redhat.com)
- Fixed notifications to work with the new pulp (paji@redhat.com)

* Tue Oct 16 2012 Eric D. Helms <ehelms@redhat.com> 0.1.1-1
- Version bump. (ehelms@redhat.com)

* Tue Oct 09 2012 Eric D. Helms <ehelms@redhat.com> 0.1.0-1
- Version bump. (ehelms@redhat.com)
- Updates README with Travis status and new test options. (ehelms@redhat.com)
- Removing puts in helper that are not quite helpful. (ehelms@redhat.com)
- Adds i18n for activesupport. (ehelms@redhat.com)
- Typo in Gemfile. (ehelms@redhat.com)
- Adds missing active_support requirement. (ehelms@redhat.com)
- Updates to testing to allow recorded and none modes to be run on a system
  without pulp installed.  Adds option to turn logging during testing off or
  on. (ehelms@redhat.com)
- Removes references to ruby-debug. (ehelms@redhat.com)
- Adds rake to Gemfile. (ehelms@redhat.com)
- Removes ruby-debug from Gemfile, adds none as the default test mode and adds
  a basic travis config file. (ehelms@redhat.com)
- merge conflicts (jsherril@redhat.com)
- cassette updates (jsherril@redhat.com)
- uncommenting some repo test code (jsherril@redhat.com)
- cassette updates (jsherril@redhat.com)
- Merge remote-tracking branch 'upstream-runcible/master' into fork-runcible-
  pulpv2 (bbuckingham@redhat.com)
- fixing broken test (jsherril@redhat.com)
- cleaning up search tests (jsherril@redhat.com)
- pulpv2 - consumer - adding apis for repo binding and content actions
  (bbuckingham@redhat.com)
- moving repository test (jsherril@redhat.com)
- cassette updates (jsherril@redhat.com)
- cassette updates (jsherril@redhat.com)
- adding distributions and other unit tests (jsherril@redhat.com)
- adding new ignore (jsherril@redhat.com)
- pulpv2 - adding retrieve all for users and re-organizing
  (jsherril@redhat.com)
- Merge pull request #5 from jlsherrill/pulpv2 (ericdhelms@gmail.com)
- cassette updates (jsherril@redhat.com)
- adding testing for rpm/errata/category/group (jsherril@redhat.com)
- Revert "removing generate_metadata as it is not a valid option"
  (jsherril@redhat.com)
- adding units (jsherril@redhat.com)
- removing spaces (jsherril@redhat.com)
- removing generate_metadata as it is not a valid option (jsherril@redhat.com)
- Merge remote-tracking branch 'upstream-runcible/master' into fork-runcible-
  pulpv2 (bbuckingham@redhat.com)
- Merge pull request #4 from jlsherrill/pulpv2 (ericdhelms@gmail.com)
- cassette updates (jsherril@redhat.com)
- pull request comment (jsherril@redhat.com)
- addressing pull request comments (jsherril@redhat.com)
- fixing return on publish_all extension (jsherril@redhat.com)
- new cassettes (jsherril@redhat.com)
- adding event notifiers to runcible (jsherril@redhat.com)
- cassette update (jsherril@redhat.com)
- adding extension test (jsherril@redhat.com)
- Merge remote-tracking branch 'upstream-runcible/master' into fork-runcible-
  pulpv2 (bbuckingham@redhat.com)
- cassette updates (jsherril@redhat.com)
- cassette updates (jsherril@redhat.com)
- moving some tests to their own vcr cassettes for isolation, also
  consolidating setups into before_suites (jsherril@redhat.com)
- reducing sleep time (jsherril@redhat.com)
- really adding None record type (jsherril@redhat.com)
- Small fix to get pulp repo test running (paji@redhat.com)
- addressing previous commits comments (jsherril@redhat.com)
- fixes #2 - fixing typo in gemspec (jsherril@redhat.com)
- Adding missing license (jsherril@redhat.com)
- updating readme to point to none mode (jsherril@redhat.com)
- updating vcr cassettes (jsherril@redhat.com)
- Moving with_indifferent_access to base (jsherril@redhat.com)
- removing unintentionally commented out section (jsherril@redhat.com)
- adding unit unassociation methods (jsherril@redhat.com)
- allowing None for record mode (jsherril@redhat.com)
- fixes for pull request (jsherril@redhat.com)
- Update to support proper get params with multiple values
  (jsherril@redhat.com)
- pulp v2 - consumer - initial changes for
  create/review/update/delete/profile/profile upload (bbuckingham@redhat.com)
- moving importers and distributors to their own files (jsherril@redhat.com)
- adding schedule extension and moviing requires (jsherril@redhat.com)
- adding new vcr data (jsherril@redhat.com)
- adding tests for repoistory schedules (jsherril@redhat.com)
- moving unit repo listing to runcible (jsherril@redhat.com)
- some task changes, properly implementing sync_status (jsherril@redhat.com)
- updated vcr data (jsherril@redhat.com)
- moving all unit_copy items to runcible (jsherril@redhat.com)
- new vcr data (jsherril@redhat.com)
- adding importer/distributor extensions and tests (jsherril@redhat.com)
- README update for tests (jsherril@redhat.com)
- adding importer and exporter objects (jsherril@redhat.com)
- Updates to re-scope from Pulp to Resources and from Pulp to Extensions and
  fit in line more with the directory structure. (ehelms@redhat.com)
- Version bump. (ehelms@redhat.com)

* Tue Oct 09 2012 Eric D. Helms <ehelms@redhat.com> 0.1.0-1
- Updates README with Travis status and new test options. (ehelms@redhat.com)
- Removing puts in helper that are not quite helpful. (ehelms@redhat.com)
- Adds i18n for activesupport. (ehelms@redhat.com)
- Typo in Gemfile. (ehelms@redhat.com)
- Adds missing active_support requirement. (ehelms@redhat.com)
- Updates to testing to allow recorded and none modes to be run on a system
  without pulp installed.  Adds option to turn logging during testing off or
  on. (ehelms@redhat.com)
- Removes references to ruby-debug. (ehelms@redhat.com)
- Adds rake to Gemfile. (ehelms@redhat.com)
- Removes ruby-debug from Gemfile, adds none as the default test mode and adds
  a basic travis config file. (ehelms@redhat.com)
- merge conflicts (jsherril@redhat.com)
- cassette updates (jsherril@redhat.com)
- uncommenting some repo test code (jsherril@redhat.com)
- cassette updates (jsherril@redhat.com)
- Merge remote-tracking branch 'upstream-runcible/master' into fork-runcible-
  pulpv2 (bbuckingham@redhat.com)
- fixing broken test (jsherril@redhat.com)
- cleaning up search tests (jsherril@redhat.com)
- pulpv2 - consumer - adding apis for repo binding and content actions
  (bbuckingham@redhat.com)
- moving repository test (jsherril@redhat.com)
- cassette updates (jsherril@redhat.com)
- cassette updates (jsherril@redhat.com)
- adding distributions and other unit tests (jsherril@redhat.com)
- adding new ignore (jsherril@redhat.com)
- pulpv2 - adding retrieve all for users and re-organizing
  (jsherril@redhat.com)
- Merge pull request #5 from jlsherrill/pulpv2 (ericdhelms@gmail.com)
- cassette updates (jsherril@redhat.com)
- adding testing for rpm/errata/category/group (jsherril@redhat.com)
- Revert "removing generate_metadata as it is not a valid option"
  (jsherril@redhat.com)
- adding units (jsherril@redhat.com)
- removing spaces (jsherril@redhat.com)
- removing generate_metadata as it is not a valid option (jsherril@redhat.com)
- Merge remote-tracking branch 'upstream-runcible/master' into fork-runcible-
  pulpv2 (bbuckingham@redhat.com)
- Merge pull request #4 from jlsherrill/pulpv2 (ericdhelms@gmail.com)
- cassette updates (jsherril@redhat.com)
- pull request comment (jsherril@redhat.com)
- addressing pull request comments (jsherril@redhat.com)
- fixing return on publish_all extension (jsherril@redhat.com)
- new cassettes (jsherril@redhat.com)
- adding event notifiers to runcible (jsherril@redhat.com)
- cassette update (jsherril@redhat.com)
- adding extension test (jsherril@redhat.com)
- Merge remote-tracking branch 'upstream-runcible/master' into fork-runcible-
  pulpv2 (bbuckingham@redhat.com)
- cassette updates (jsherril@redhat.com)
- cassette updates (jsherril@redhat.com)
- moving some tests to their own vcr cassettes for isolation, also
  consolidating setups into before_suites (jsherril@redhat.com)
- reducing sleep time (jsherril@redhat.com)
- really adding None record type (jsherril@redhat.com)
- Small fix to get pulp repo test running (paji@redhat.com)
- addressing previous commits comments (jsherril@redhat.com)
- fixes #2 - fixing typo in gemspec (jsherril@redhat.com)
- Adding missing license (jsherril@redhat.com)
- updating readme to point to none mode (jsherril@redhat.com)
- updating vcr cassettes (jsherril@redhat.com)
- Moving with_indifferent_access to base (jsherril@redhat.com)
- removing unintentionally commented out section (jsherril@redhat.com)
- adding unit unassociation methods (jsherril@redhat.com)
- allowing None for record mode (jsherril@redhat.com)
- fixes for pull request (jsherril@redhat.com)
- Update to support proper get params with multiple values
  (jsherril@redhat.com)
- pulp v2 - consumer - initial changes for
  create/review/update/delete/profile/profile upload (bbuckingham@redhat.com)
- moving importers and distributors to their own files (jsherril@redhat.com)
- adding schedule extension and moviing requires (jsherril@redhat.com)
- adding new vcr data (jsherril@redhat.com)
- adding tests for repoistory schedules (jsherril@redhat.com)
- moving unit repo listing to runcible (jsherril@redhat.com)
- some task changes, properly implementing sync_status (jsherril@redhat.com)
- updated vcr data (jsherril@redhat.com)
- moving all unit_copy items to runcible (jsherril@redhat.com)
- new vcr data (jsherril@redhat.com)
- adding importer/distributor extensions and tests (jsherril@redhat.com)
- README update for tests (jsherril@redhat.com)
- adding importer and exporter objects (jsherril@redhat.com)
- Updates to re-scope from Pulp to Resources and from Pulp to Extensions and
  fit in line more with the directory structure. (ehelms@redhat.com)
- Version bump. (ehelms@redhat.com)

* Tue Oct 09 2012 Eric D. Helms <ehelms@redhat.com> 0.1.0-1
- Version bump to 0.1 (ehelms@redhat.com)
- Removing puts in helper that are not quite helpful. (ehelms@redhat.com)
- Adds i18n for activesupport. (ehelms@redhat.com)
- Typo in Gemfile. (ehelms@redhat.com)
- Adds missing active_support requirement. (ehelms@redhat.com)
- Updates to testing to allow recorded and none modes to be run on a system
  without pulp installed.  Adds option to turn logging during testing off or
  on. (ehelms@redhat.com)
- Removes references to ruby-debug. (ehelms@redhat.com)
- Adds rake to Gemfile. (ehelms@redhat.com)
- Removes ruby-debug from Gemfile, adds none as the default test mode and adds
  a basic travis config file. (ehelms@redhat.com)
- merge conflicts (jsherril@redhat.com)
- cassette updates (jsherril@redhat.com)
- uncommenting some repo test code (jsherril@redhat.com)
- cassette updates (jsherril@redhat.com)
- Merge remote-tracking branch 'upstream-runcible/master' into fork-runcible-
  pulpv2 (bbuckingham@redhat.com)
- fixing broken test (jsherril@redhat.com)
- cleaning up search tests (jsherril@redhat.com)
- pulpv2 - consumer - adding apis for repo binding and content actions
  (bbuckingham@redhat.com)
- moving repository test (jsherril@redhat.com)
- cassette updates (jsherril@redhat.com)
- cassette updates (jsherril@redhat.com)
- adding distributions and other unit tests (jsherril@redhat.com)
- adding new ignore (jsherril@redhat.com)
- pulpv2 - adding retrieve all for users and re-organizing
  (jsherril@redhat.com)
- Merge pull request #5 from jlsherrill/pulpv2 (ericdhelms@gmail.com)
- cassette updates (jsherril@redhat.com)
- adding testing for rpm/errata/category/group (jsherril@redhat.com)
- Revert "removing generate_metadata as it is not a valid option"
  (jsherril@redhat.com)
- adding units (jsherril@redhat.com)
- removing spaces (jsherril@redhat.com)
- removing generate_metadata as it is not a valid option (jsherril@redhat.com)
- Merge remote-tracking branch 'upstream-runcible/master' into fork-runcible-
  pulpv2 (bbuckingham@redhat.com)
- Merge pull request #4 from jlsherrill/pulpv2 (ericdhelms@gmail.com)
- cassette updates (jsherril@redhat.com)
- pull request comment (jsherril@redhat.com)
- addressing pull request comments (jsherril@redhat.com)
- fixing return on publish_all extension (jsherril@redhat.com)
- new cassettes (jsherril@redhat.com)
- adding event notifiers to runcible (jsherril@redhat.com)
- cassette update (jsherril@redhat.com)
- adding extension test (jsherril@redhat.com)
- Merge remote-tracking branch 'upstream-runcible/master' into fork-runcible-
  pulpv2 (bbuckingham@redhat.com)
- cassette updates (jsherril@redhat.com)
- cassette updates (jsherril@redhat.com)
- moving some tests to their own vcr cassettes for isolation, also
  consolidating setups into before_suites (jsherril@redhat.com)
- reducing sleep time (jsherril@redhat.com)
- really adding None record type (jsherril@redhat.com)
- Small fix to get pulp repo test running (paji@redhat.com)
- addressing previous commits comments (jsherril@redhat.com)
- fixes #2 - fixing typo in gemspec (jsherril@redhat.com)
- Adding missing license (jsherril@redhat.com)
- updating readme to point to none mode (jsherril@redhat.com)
- updating vcr cassettes (jsherril@redhat.com)
- Moving with_indifferent_access to base (jsherril@redhat.com)
- removing unintentionally commented out section (jsherril@redhat.com)
- adding unit unassociation methods (jsherril@redhat.com)
- allowing None for record mode (jsherril@redhat.com)
- fixes for pull request (jsherril@redhat.com)
- Update to support proper get params with multiple values
  (jsherril@redhat.com)
- pulp v2 - consumer - initial changes for
  create/review/update/delete/profile/profile upload (bbuckingham@redhat.com)
- moving importers and distributors to their own files (jsherril@redhat.com)
- adding schedule extension and moviing requires (jsherril@redhat.com)
- adding new vcr data (jsherril@redhat.com)
- adding tests for repoistory schedules (jsherril@redhat.com)
- moving unit repo listing to runcible (jsherril@redhat.com)
- some task changes, properly implementing sync_status (jsherril@redhat.com)
- updated vcr data (jsherril@redhat.com)
- moving all unit_copy items to runcible (jsherril@redhat.com)
- new vcr data (jsherril@redhat.com)
- adding importer/distributor extensions and tests (jsherril@redhat.com)
- README update for tests (jsherril@redhat.com)
- adding importer and exporter objects (jsherril@redhat.com)
- Updates to re-scope from Pulp to Resources and from Pulp to Extensions and
  fit in line more with the directory structure. (ehelms@redhat.com)
- Version bump. (ehelms@redhat.com)

* Tue Oct 09 2012 Eric D. Helms <ehelms@redhat.com>
- Version bump to 0.1 (ehelms@redhat.com)
- Removing puts in helper that are not quite helpful. (ehelms@redhat.com)
- Adds i18n for activesupport. (ehelms@redhat.com)
- Typo in Gemfile. (ehelms@redhat.com)
- Adds missing active_support requirement. (ehelms@redhat.com)
- Updates to testing to allow recorded and none modes to be run on a system
  without pulp installed.  Adds option to turn logging during testing off or
  on. (ehelms@redhat.com)
- Removes references to ruby-debug. (ehelms@redhat.com)
- Adds rake to Gemfile. (ehelms@redhat.com)
- Removes ruby-debug from Gemfile, adds none as the default test mode and adds
  a basic travis config file. (ehelms@redhat.com)
- merge conflicts (jsherril@redhat.com)
- cassette updates (jsherril@redhat.com)
- uncommenting some repo test code (jsherril@redhat.com)
- cassette updates (jsherril@redhat.com)
- Merge remote-tracking branch 'upstream-runcible/master' into fork-runcible-
  pulpv2 (bbuckingham@redhat.com)
- fixing broken test (jsherril@redhat.com)
- cleaning up search tests (jsherril@redhat.com)
- pulpv2 - consumer - adding apis for repo binding and content actions
  (bbuckingham@redhat.com)
- moving repository test (jsherril@redhat.com)
- cassette updates (jsherril@redhat.com)
- cassette updates (jsherril@redhat.com)
- adding distributions and other unit tests (jsherril@redhat.com)
- adding new ignore (jsherril@redhat.com)
- pulpv2 - adding retrieve all for users and re-organizing
  (jsherril@redhat.com)
- Merge pull request #5 from jlsherrill/pulpv2 (ericdhelms@gmail.com)
- cassette updates (jsherril@redhat.com)
- adding testing for rpm/errata/category/group (jsherril@redhat.com)
- Revert "removing generate_metadata as it is not a valid option"
  (jsherril@redhat.com)
- adding units (jsherril@redhat.com)
- removing spaces (jsherril@redhat.com)
- removing generate_metadata as it is not a valid option (jsherril@redhat.com)
- Merge remote-tracking branch 'upstream-runcible/master' into fork-runcible-
  pulpv2 (bbuckingham@redhat.com)
- Merge pull request #4 from jlsherrill/pulpv2 (ericdhelms@gmail.com)
- cassette updates (jsherril@redhat.com)
- pull request comment (jsherril@redhat.com)
- addressing pull request comments (jsherril@redhat.com)
- fixing return on publish_all extension (jsherril@redhat.com)
- new cassettes (jsherril@redhat.com)
- adding event notifiers to runcible (jsherril@redhat.com)
- cassette update (jsherril@redhat.com)
- adding extension test (jsherril@redhat.com)
- Merge remote-tracking branch 'upstream-runcible/master' into fork-runcible-
  pulpv2 (bbuckingham@redhat.com)
- cassette updates (jsherril@redhat.com)
- cassette updates (jsherril@redhat.com)
- moving some tests to their own vcr cassettes for isolation, also
  consolidating setups into before_suites (jsherril@redhat.com)
- reducing sleep time (jsherril@redhat.com)
- really adding None record type (jsherril@redhat.com)
- Small fix to get pulp repo test running (paji@redhat.com)
- addressing previous commits comments (jsherril@redhat.com)
- fixes #2 - fixing typo in gemspec (jsherril@redhat.com)
- Adding missing license (jsherril@redhat.com)
- updating readme to point to none mode (jsherril@redhat.com)
- updating vcr cassettes (jsherril@redhat.com)
- Moving with_indifferent_access to base (jsherril@redhat.com)
- removing unintentionally commented out section (jsherril@redhat.com)
- adding unit unassociation methods (jsherril@redhat.com)
- allowing None for record mode (jsherril@redhat.com)
- fixes for pull request (jsherril@redhat.com)
- Update to support proper get params with multiple values
  (jsherril@redhat.com)
- pulp v2 - consumer - initial changes for
  create/review/update/delete/profile/profile upload (bbuckingham@redhat.com)
- moving importers and distributors to their own files (jsherril@redhat.com)
- adding schedule extension and moviing requires (jsherril@redhat.com)
- adding new vcr data (jsherril@redhat.com)
- adding tests for repoistory schedules (jsherril@redhat.com)
- moving unit repo listing to runcible (jsherril@redhat.com)
- some task changes, properly implementing sync_status (jsherril@redhat.com)
- updated vcr data (jsherril@redhat.com)
- moving all unit_copy items to runcible (jsherril@redhat.com)
- new vcr data (jsherril@redhat.com)
- adding importer/distributor extensions and tests (jsherril@redhat.com)
- README update for tests (jsherril@redhat.com)
- adding importer and exporter objects (jsherril@redhat.com)
- Updates to re-scope from Pulp to Resources and from Pulp to Extensions and
  fit in line more with the directory structure. (ehelms@redhat.com)
- Version bump. (ehelms@redhat.com)

* Tue Oct 09 2012 Eric D. Helms <ehelms@redhat.com> 0.1.0-1
- Removing puts in helper that are not quite helpful. (ehelms@redhat.com)
- Adds i18n for activesupport. (ehelms@redhat.com)
- Typo in Gemfile. (ehelms@redhat.com)
- Adds missing active_support requirement. (ehelms@redhat.com)
- Updates to testing to allow recorded and none modes to be run on a system
  without pulp installed.  Adds option to turn logging during testing off or
  on. (ehelms@redhat.com)
- Removes references to ruby-debug. (ehelms@redhat.com)
- Adds rake to Gemfile. (ehelms@redhat.com)
- Removes ruby-debug from Gemfile, adds none as the default test mode and adds
  a basic travis config file. (ehelms@redhat.com)
- merge conflicts (jsherril@redhat.com)
- cassette updates (jsherril@redhat.com)
- uncommenting some repo test code (jsherril@redhat.com)
- cassette updates (jsherril@redhat.com)
- Merge remote-tracking branch 'upstream-runcible/master' into fork-runcible-
  pulpv2 (bbuckingham@redhat.com)
- fixing broken test (jsherril@redhat.com)
- cleaning up search tests (jsherril@redhat.com)
- pulpv2 - consumer - adding apis for repo binding and content actions
  (bbuckingham@redhat.com)
- moving repository test (jsherril@redhat.com)
- cassette updates (jsherril@redhat.com)
- cassette updates (jsherril@redhat.com)
- adding distributions and other unit tests (jsherril@redhat.com)
- adding new ignore (jsherril@redhat.com)
- pulpv2 - adding retrieve all for users and re-organizing
  (jsherril@redhat.com)
- Merge pull request #5 from jlsherrill/pulpv2 (ericdhelms@gmail.com)
- cassette updates (jsherril@redhat.com)
- adding testing for rpm/errata/category/group (jsherril@redhat.com)
- Revert "removing generate_metadata as it is not a valid option"
  (jsherril@redhat.com)
- adding units (jsherril@redhat.com)
- removing spaces (jsherril@redhat.com)
- removing generate_metadata as it is not a valid option (jsherril@redhat.com)
- Merge remote-tracking branch 'upstream-runcible/master' into fork-runcible-
  pulpv2 (bbuckingham@redhat.com)
- Merge pull request #4 from jlsherrill/pulpv2 (ericdhelms@gmail.com)
- cassette updates (jsherril@redhat.com)
- pull request comment (jsherril@redhat.com)
- addressing pull request comments (jsherril@redhat.com)
- fixing return on publish_all extension (jsherril@redhat.com)
- new cassettes (jsherril@redhat.com)
- adding event notifiers to runcible (jsherril@redhat.com)
- cassette update (jsherril@redhat.com)
- adding extension test (jsherril@redhat.com)
- Merge remote-tracking branch 'upstream-runcible/master' into fork-runcible-
  pulpv2 (bbuckingham@redhat.com)
- cassette updates (jsherril@redhat.com)
- cassette updates (jsherril@redhat.com)
- moving some tests to their own vcr cassettes for isolation, also
  consolidating setups into before_suites (jsherril@redhat.com)
- reducing sleep time (jsherril@redhat.com)
- really adding None record type (jsherril@redhat.com)
- Small fix to get pulp repo test running (paji@redhat.com)
- addressing previous commits comments (jsherril@redhat.com)
- fixes #2 - fixing typo in gemspec (jsherril@redhat.com)
- Adding missing license (jsherril@redhat.com)
- updating readme to point to none mode (jsherril@redhat.com)
- updating vcr cassettes (jsherril@redhat.com)
- Moving with_indifferent_access to base (jsherril@redhat.com)
- removing unintentionally commented out section (jsherril@redhat.com)
- adding unit unassociation methods (jsherril@redhat.com)
- allowing None for record mode (jsherril@redhat.com)
- fixes for pull request (jsherril@redhat.com)
- Update to support proper get params with multiple values
  (jsherril@redhat.com)
- pulp v2 - consumer - initial changes for
  create/review/update/delete/profile/profile upload (bbuckingham@redhat.com)
- moving importers and distributors to their own files (jsherril@redhat.com)
- adding schedule extension and moviing requires (jsherril@redhat.com)
- adding new vcr data (jsherril@redhat.com)
- adding tests for repoistory schedules (jsherril@redhat.com)
- moving unit repo listing to runcible (jsherril@redhat.com)
- some task changes, properly implementing sync_status (jsherril@redhat.com)
- updated vcr data (jsherril@redhat.com)
- moving all unit_copy items to runcible (jsherril@redhat.com)
- new vcr data (jsherril@redhat.com)
- adding importer/distributor extensions and tests (jsherril@redhat.com)
- README update for tests (jsherril@redhat.com)
- adding importer and exporter objects (jsherril@redhat.com)
- Updates to re-scope from Pulp to Resources and from Pulp to Extensions and
  fit in line more with the directory structure. (ehelms@redhat.com)
- Version bump. (ehelms@redhat.com)

* Tue Oct 09 2012 Eric D. Helms <ehelms@redhat.com> 0.1.1-1
- Removing puts in helper that are not quite helpful. (ehelms@redhat.com)
- Adds i18n for activesupport. (ehelms@redhat.com)
- Typo in Gemfile. (ehelms@redhat.com)
- Adds missing active_support requirement. (ehelms@redhat.com)
- Updates to testing to allow recorded and none modes to be run on a system
  without pulp installed.  Adds option to turn logging during testing off or
  on. (ehelms@redhat.com)
- Removes references to ruby-debug. (ehelms@redhat.com)
- Adds rake to Gemfile. (ehelms@redhat.com)
- Removes ruby-debug from Gemfile, adds none as the default test mode and adds
  a basic travis config file. (ehelms@redhat.com)
- merge conflicts (jsherril@redhat.com)
- cassette updates (jsherril@redhat.com)
- uncommenting some repo test code (jsherril@redhat.com)
- cassette updates (jsherril@redhat.com)
- Merge remote-tracking branch 'upstream-runcible/master' into fork-runcible-
  pulpv2 (bbuckingham@redhat.com)
- fixing broken test (jsherril@redhat.com)
- cleaning up search tests (jsherril@redhat.com)
- pulpv2 - consumer - adding apis for repo binding and content actions
  (bbuckingham@redhat.com)
- moving repository test (jsherril@redhat.com)
- cassette updates (jsherril@redhat.com)
- cassette updates (jsherril@redhat.com)
- adding distributions and other unit tests (jsherril@redhat.com)
- adding new ignore (jsherril@redhat.com)
- pulpv2 - adding retrieve all for users and re-organizing
  (jsherril@redhat.com)
- Merge pull request #5 from jlsherrill/pulpv2 (ericdhelms@gmail.com)
- cassette updates (jsherril@redhat.com)
- adding testing for rpm/errata/category/group (jsherril@redhat.com)
- Revert "removing generate_metadata as it is not a valid option"
  (jsherril@redhat.com)
- adding units (jsherril@redhat.com)
- removing spaces (jsherril@redhat.com)
- removing generate_metadata as it is not a valid option (jsherril@redhat.com)
- Merge remote-tracking branch 'upstream-runcible/master' into fork-runcible-
  pulpv2 (bbuckingham@redhat.com)
- Merge pull request #4 from jlsherrill/pulpv2 (ericdhelms@gmail.com)
- cassette updates (jsherril@redhat.com)
- pull request comment (jsherril@redhat.com)
- addressing pull request comments (jsherril@redhat.com)
- fixing return on publish_all extension (jsherril@redhat.com)
- new cassettes (jsherril@redhat.com)
- adding event notifiers to runcible (jsherril@redhat.com)
- cassette update (jsherril@redhat.com)
- adding extension test (jsherril@redhat.com)
- Merge remote-tracking branch 'upstream-runcible/master' into fork-runcible-
  pulpv2 (bbuckingham@redhat.com)
- cassette updates (jsherril@redhat.com)
- cassette updates (jsherril@redhat.com)
- moving some tests to their own vcr cassettes for isolation, also
  consolidating setups into before_suites (jsherril@redhat.com)
- reducing sleep time (jsherril@redhat.com)
- really adding None record type (jsherril@redhat.com)
- Small fix to get pulp repo test running (paji@redhat.com)
- addressing previous commits comments (jsherril@redhat.com)
- fixes #2 - fixing typo in gemspec (jsherril@redhat.com)
- Adding missing license (jsherril@redhat.com)
- updating readme to point to none mode (jsherril@redhat.com)
- updating vcr cassettes (jsherril@redhat.com)
- Moving with_indifferent_access to base (jsherril@redhat.com)
- removing unintentionally commented out section (jsherril@redhat.com)
- adding unit unassociation methods (jsherril@redhat.com)
- allowing None for record mode (jsherril@redhat.com)
- fixes for pull request (jsherril@redhat.com)
- Update to support proper get params with multiple values
  (jsherril@redhat.com)
- pulp v2 - consumer - initial changes for
  create/review/update/delete/profile/profile upload (bbuckingham@redhat.com)
- moving importers and distributors to their own files (jsherril@redhat.com)
- adding schedule extension and moviing requires (jsherril@redhat.com)
- adding new vcr data (jsherril@redhat.com)
- adding tests for repoistory schedules (jsherril@redhat.com)
- moving unit repo listing to runcible (jsherril@redhat.com)
- some task changes, properly implementing sync_status (jsherril@redhat.com)
- updated vcr data (jsherril@redhat.com)
- moving all unit_copy items to runcible (jsherril@redhat.com)
- new vcr data (jsherril@redhat.com)
- adding importer/distributor extensions and tests (jsherril@redhat.com)
- README update for tests (jsherril@redhat.com)
- adding importer and exporter objects (jsherril@redhat.com)
- Updates to re-scope from Pulp to Resources and from Pulp to Extensions and
  fit in line more with the directory structure. (ehelms@redhat.com)
- Version bump. (ehelms@redhat.com)

* Tue Oct 09 2012 Eric D. Helms <ehelms@redhat.com>
- Removing puts in helper that are not quite helpful. (ehelms@redhat.com)
- Adds i18n for activesupport. (ehelms@redhat.com)
- Typo in Gemfile. (ehelms@redhat.com)
- Adds missing active_support requirement. (ehelms@redhat.com)
- Updates to testing to allow recorded and none modes to be run on a system
  without pulp installed.  Adds option to turn logging during testing off or
  on. (ehelms@redhat.com)
- Removes references to ruby-debug. (ehelms@redhat.com)
- Adds rake to Gemfile. (ehelms@redhat.com)
- Removes ruby-debug from Gemfile, adds none as the default test mode and adds
  a basic travis config file. (ehelms@redhat.com)
- merge conflicts (jsherril@redhat.com)
- cassette updates (jsherril@redhat.com)
- uncommenting some repo test code (jsherril@redhat.com)
- cassette updates (jsherril@redhat.com)
- Merge remote-tracking branch 'upstream-runcible/master' into fork-runcible-
  pulpv2 (bbuckingham@redhat.com)
- fixing broken test (jsherril@redhat.com)
- cleaning up search tests (jsherril@redhat.com)
- pulpv2 - consumer - adding apis for repo binding and content actions
  (bbuckingham@redhat.com)
- moving repository test (jsherril@redhat.com)
- cassette updates (jsherril@redhat.com)
- cassette updates (jsherril@redhat.com)
- adding distributions and other unit tests (jsherril@redhat.com)
- adding new ignore (jsherril@redhat.com)
- pulpv2 - adding retrieve all for users and re-organizing
  (jsherril@redhat.com)
- Merge pull request #5 from jlsherrill/pulpv2 (ericdhelms@gmail.com)
- cassette updates (jsherril@redhat.com)
- adding testing for rpm/errata/category/group (jsherril@redhat.com)
- Revert "removing generate_metadata as it is not a valid option"
  (jsherril@redhat.com)
- adding units (jsherril@redhat.com)
- removing spaces (jsherril@redhat.com)
- removing generate_metadata as it is not a valid option (jsherril@redhat.com)
- Merge remote-tracking branch 'upstream-runcible/master' into fork-runcible-
  pulpv2 (bbuckingham@redhat.com)
- Merge pull request #4 from jlsherrill/pulpv2 (ericdhelms@gmail.com)
- cassette updates (jsherril@redhat.com)
- pull request comment (jsherril@redhat.com)
- addressing pull request comments (jsherril@redhat.com)
- fixing return on publish_all extension (jsherril@redhat.com)
- new cassettes (jsherril@redhat.com)
- adding event notifiers to runcible (jsherril@redhat.com)
- cassette update (jsherril@redhat.com)
- adding extension test (jsherril@redhat.com)
- Merge remote-tracking branch 'upstream-runcible/master' into fork-runcible-
  pulpv2 (bbuckingham@redhat.com)
- cassette updates (jsherril@redhat.com)
- cassette updates (jsherril@redhat.com)
- moving some tests to their own vcr cassettes for isolation, also
  consolidating setups into before_suites (jsherril@redhat.com)
- reducing sleep time (jsherril@redhat.com)
- really adding None record type (jsherril@redhat.com)
- Small fix to get pulp repo test running (paji@redhat.com)
- addressing previous commits comments (jsherril@redhat.com)
- fixes #2 - fixing typo in gemspec (jsherril@redhat.com)
- Adding missing license (jsherril@redhat.com)
- updating readme to point to none mode (jsherril@redhat.com)
- updating vcr cassettes (jsherril@redhat.com)
- Moving with_indifferent_access to base (jsherril@redhat.com)
- removing unintentionally commented out section (jsherril@redhat.com)
- adding unit unassociation methods (jsherril@redhat.com)
- allowing None for record mode (jsherril@redhat.com)
- fixes for pull request (jsherril@redhat.com)
- Update to support proper get params with multiple values
  (jsherril@redhat.com)
- pulp v2 - consumer - initial changes for
  create/review/update/delete/profile/profile upload (bbuckingham@redhat.com)
- moving importers and distributors to their own files (jsherril@redhat.com)
- adding schedule extension and moviing requires (jsherril@redhat.com)
- adding new vcr data (jsherril@redhat.com)
- adding tests for repoistory schedules (jsherril@redhat.com)
- moving unit repo listing to runcible (jsherril@redhat.com)
- some task changes, properly implementing sync_status (jsherril@redhat.com)
- updated vcr data (jsherril@redhat.com)
- moving all unit_copy items to runcible (jsherril@redhat.com)
- new vcr data (jsherril@redhat.com)
- adding importer/distributor extensions and tests (jsherril@redhat.com)
- README update for tests (jsherril@redhat.com)
- adding importer and exporter objects (jsherril@redhat.com)
- Updates to re-scope from Pulp to Resources and from Pulp to Extensions and
  fit in line more with the directory structure. (ehelms@redhat.com)
- Version bump. (ehelms@redhat.com)

* Tue Oct 09 2012 Eric D. Helms <ehelms@redhat.com> 0.1.1-1
- Removing puts in helper that are not quite helpful. (ehelms@redhat.com)
- Adds i18n for activesupport. (ehelms@redhat.com)
- Typo in Gemfile. (ehelms@redhat.com)
- Adds missing active_support requirement. (ehelms@redhat.com)
- Updates to testing to allow recorded and none modes to be run on a system
  without pulp installed.  Adds option to turn logging during testing off or
  on. (ehelms@redhat.com)
- Removes references to ruby-debug. (ehelms@redhat.com)
- Adds rake to Gemfile. (ehelms@redhat.com)
- Removes ruby-debug from Gemfile, adds none as the default test mode and adds
  a basic travis config file. (ehelms@redhat.com)
- merge conflicts (jsherril@redhat.com)
- cassette updates (jsherril@redhat.com)
- uncommenting some repo test code (jsherril@redhat.com)
- cassette updates (jsherril@redhat.com)
- Merge remote-tracking branch 'upstream-runcible/master' into fork-runcible-
  pulpv2 (bbuckingham@redhat.com)
- fixing broken test (jsherril@redhat.com)
- cleaning up search tests (jsherril@redhat.com)
- pulpv2 - consumer - adding apis for repo binding and content actions
  (bbuckingham@redhat.com)
- moving repository test (jsherril@redhat.com)
- cassette updates (jsherril@redhat.com)
- cassette updates (jsherril@redhat.com)
- adding distributions and other unit tests (jsherril@redhat.com)
- adding new ignore (jsherril@redhat.com)
- pulpv2 - adding retrieve all for users and re-organizing
  (jsherril@redhat.com)
- Merge pull request #5 from jlsherrill/pulpv2 (ericdhelms@gmail.com)
- cassette updates (jsherril@redhat.com)
- adding testing for rpm/errata/category/group (jsherril@redhat.com)
- Revert "removing generate_metadata as it is not a valid option"
  (jsherril@redhat.com)
- adding units (jsherril@redhat.com)
- removing spaces (jsherril@redhat.com)
- removing generate_metadata as it is not a valid option (jsherril@redhat.com)
- Merge remote-tracking branch 'upstream-runcible/master' into fork-runcible-
  pulpv2 (bbuckingham@redhat.com)
- Merge pull request #4 from jlsherrill/pulpv2 (ericdhelms@gmail.com)
- cassette updates (jsherril@redhat.com)
- pull request comment (jsherril@redhat.com)
- addressing pull request comments (jsherril@redhat.com)
- fixing return on publish_all extension (jsherril@redhat.com)
- new cassettes (jsherril@redhat.com)
- adding event notifiers to runcible (jsherril@redhat.com)
- cassette update (jsherril@redhat.com)
- adding extension test (jsherril@redhat.com)
- Merge remote-tracking branch 'upstream-runcible/master' into fork-runcible-
  pulpv2 (bbuckingham@redhat.com)
- cassette updates (jsherril@redhat.com)
- cassette updates (jsherril@redhat.com)
- moving some tests to their own vcr cassettes for isolation, also
  consolidating setups into before_suites (jsherril@redhat.com)
- reducing sleep time (jsherril@redhat.com)
- really adding None record type (jsherril@redhat.com)
- Small fix to get pulp repo test running (paji@redhat.com)
- addressing previous commits comments (jsherril@redhat.com)
- fixes #2 - fixing typo in gemspec (jsherril@redhat.com)
- Adding missing license (jsherril@redhat.com)
- updating readme to point to none mode (jsherril@redhat.com)
- updating vcr cassettes (jsherril@redhat.com)
- Moving with_indifferent_access to base (jsherril@redhat.com)
- removing unintentionally commented out section (jsherril@redhat.com)
- adding unit unassociation methods (jsherril@redhat.com)
- allowing None for record mode (jsherril@redhat.com)
- fixes for pull request (jsherril@redhat.com)
- Update to support proper get params with multiple values
  (jsherril@redhat.com)
- pulp v2 - consumer - initial changes for
  create/review/update/delete/profile/profile upload (bbuckingham@redhat.com)
- moving importers and distributors to their own files (jsherril@redhat.com)
- adding schedule extension and moviing requires (jsherril@redhat.com)
- adding new vcr data (jsherril@redhat.com)
- adding tests for repoistory schedules (jsherril@redhat.com)
- moving unit repo listing to runcible (jsherril@redhat.com)
- some task changes, properly implementing sync_status (jsherril@redhat.com)
- updated vcr data (jsherril@redhat.com)
- moving all unit_copy items to runcible (jsherril@redhat.com)
- new vcr data (jsherril@redhat.com)
- adding importer/distributor extensions and tests (jsherril@redhat.com)
- README update for tests (jsherril@redhat.com)
- adding importer and exporter objects (jsherril@redhat.com)
- Updates to re-scope from Pulp to Resources and from Pulp to Extensions and
  fit in line more with the directory structure. (ehelms@redhat.com)
- Version bump. (ehelms@redhat.com)

* Fri Sep 14 2012 Eric D. Helms <ehelms@redhat.com> 0.0.9-1
- Updates verison. (ehelms@redhat.com)
- Minor updates to spec file. (ehelms@redhat.com)
- Automatic commit of package [rubygem-runcible] release [0.0.7-1].
  (ehelms@redhat.com)

* Fri Sep 14 2012 Eric D. Helms <ehelms@redhat.com>
- Automatic commit of package [rubygem-runcible] release [0.0.8-1].
  (ehelms@redhat.com)

* Fri Sep 14 2012 Eric D. Helms <ehelms@redhat.com> 0.0.8-1
- Minor updates to spec file. (ehelms@redhat.com)
- Automatic commit of package [rubygem-runcible] release [0.0.7-1].
  (ehelms@redhat.com)

* Fri Sep 14 2012 Eric D. Helms <ehelms@redhat.com>
- Minor updates to spec file. (ehelms@redhat.com)
- Automatic commit of package [rubygem-runcible] release [0.0.7-1].
  (ehelms@redhat.com)

* Fri Sep 14 2012 Eric D. Helms <ehelms@redhat.com>
- Minor updates to spec file. (ehelms@redhat.com)
- Automatic commit of package [rubygem-runcible] release [0.0.7-1].
  (ehelms@redhat.com)

* Fri Sep 14 2012 Eric D. Helms <ehelms@redhat.com> 0.0.7-1
- Updates to spec file. (ehelms@redhat.com)
- Moves install directive into prep section. (ehelms@redhat.com)
- Flipping order of prep steps. (ehelms@redhat.com)
- Fixing typo in source declaration in spec file. (ehelms@redhat.com)
- Updates to spec file variables. (ehelms@redhat.com)
- Adds documentation subpackage and cleans up spec file to handle tar.gz
  source. (ehelms@redhat.com)

* Fri Sep 14 2012 Eric D. Helms <ehelms@redhat.com> 0.0.6-1
- new package built with tito
