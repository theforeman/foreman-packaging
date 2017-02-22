%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%{!?_root_sysconfdir:%global _root_sysconfdir %{_sysconfdir}}

%global gem_name hammer_cli_import
%global confdir hammer

Summary: Sat5-import command plugin for the Hammer CLI
Name:    %{?scl_prefix}rubygem-%{gem_name}
Version: 0.11.3
Release: 1%{?dist}
Group:   Development/Languages
License: GPLv3
URL:     https://github.com/Katello/hammer-cli-import
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%if 0%{?scl:1}
Obsoletes: rubygem-%{gem_name} < 0.10.21-3
%endif
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(hammer_cli)
Requires: %{?scl_prefix}rubygem(hammer_cli_foreman) > 0.1.1
Requires: %{?scl_prefix}rubygem(hammer_cli_katello) < 1.0.0

BuildRequires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel

%description
Sat5-import plugin for the Hammer CLI

%package doc
Summary:   Documentation for %{pkg_name}
Group:     Documentation
Requires:  %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description doc
Documentation for %{pkg_name}

%prep
%setup -q -c -T -n %{pkg_name}-%{version}
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} - << \EOF}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{_root_sysconfdir}/%{confdir}/cli.modules.d/import
install -m 755 .%{gem_instdir}/config/import.yml %{buildroot}%{_root_sysconfdir}/%{confdir}/cli.modules.d/import.yml
install -m 644 .%{gem_instdir}/config/import/role_map.yml %{buildroot}%{_root_sysconfdir}/%{confdir}/cli.modules.d/import/role_map.yml
install -m 644 .%{gem_instdir}/config/import/config_macros.yml %{buildroot}%{_root_sysconfdir}/%{confdir}/cli.modules.d/import/config_macros.yml
install -m 644 .%{gem_instdir}/config/import/interview_answers.yml %{buildroot}%{_root_sysconfdir}/%{confdir}/cli.modules.d/import/interview_answers.yml
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%{gem_instdir}/channel_data_pretty.json
%doc %{gem_instdir}/LICENSE
%config(noreplace) %{_root_sysconfdir}/%{confdir}/cli.modules.d/import.yml
%config(noreplace) %{_root_sysconfdir}/%{confdir}/cli.modules.d/import/role_map.yml
%config(noreplace) %{_root_sysconfdir}/%{confdir}/cli.modules.d/import/config_macros.yml
%config(noreplace) %{_root_sysconfdir}/%{confdir}/cli.modules.d/import/interview_answers.yml
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/config
%doc %{gem_instdir}/README.md

%changelog
* Thu Sep 22 2016 Eric D Helms <ericdhelms@gmail.com> 0.11.3-1
- Update rubygem-hammer_cli_import to 0.11.3 (#287) (eric.d.helms@gmail.com)

* Tue Jul 26 2016 Eric D Helms <ericdhelms@gmail.com> 0.11.2-1
- Update rubygem-hammer_cli_import to 0.11.1 (#251) (eric.d.helms@gmail.com)
- updating hammer_cli_import (jsherril@redhat.com)

* Wed Jan 06 2016 Eric D. Helms <ericdhelms@gmail.com> 0.10.22-2
- Build rubygem-hammer_cli_import for RH22 SCL (ericdhelms@gmail.com)

* Thu Sep 17 2015 Justin Sherrill <jsherril@redhat.com> 0.10.22-1
- Updating rubygem-hammer_cli_import to 0.10.22 (jsherril@redhat.com)

* Thu Aug 27 2015 Eric D. Helms <ericdhelms@gmail.com> 0.10.21-4
- Update rubygem-hammer_cli_import to tfm SCL (ericdhelms@gmail.com)

* Fri Jul 31 2015 Eric D. Helms <ericdhelms@gmail.com> 0.10.21-3
- Add missing scl_prefix to package name. (ericdhelms@gmail.com)

* Fri Jul 31 2015 Eric D. Helms <ericdhelms@gmail.com> 0.10.21-2
- Fixes #11259: Move hammer packages to SCL (ericdhelms@gmail.com)

* Wed Jul 29 2015 Eric D. Helms <ericdhelms@gmail.com> 0.10.21-1
- new package built with tito

* Wed Jul 08 2015 Tomas Lestach <tlestach@redhat.com> 0.10.20-1
- 1231956 - do not set basearch/releasever if not present in substitutions for
  repository enablement (tlestach@redhat.com)
- 1231956 - recover even if sat6 reports untrue repository information
  (tlestach@redhat.com)
- Remove obsoleted file (mkollar@redhat.com)
- Enhance README (mkollar@redhat.com)

* Tue Jun 16 2015 Tomas Lestach <tlestach@redhat.com> 0.10.19-1
- 1231956 - some of the available repos do not substitute $releasever
  (tlestach@redhat.com)
- 1231956 - $releasever needs to be substituted for some repository-sets
  (tlestach@redhat.com)

* Fri Jun 05 2015 Tomas Lestach <tlestach@redhat.com> 0.10.18-1
- 1224268 - allow caching of non-persistent entity lists (tlestach@redhat.com)
- 1222039 - use File.expand_path instead of File.absolute_path
  (tlestach@redhat.com)
- fix information message (wrong entity listed) (tlestach@redhat.com)
- 1228194 - before deleting a content view, we first need to delete it from
  associated environments (tlestach@redhat.com)

* Wed Jun 03 2015 Tomas Lestach <tlestach@redhat.com> 0.10.17-1
- 1222448 - do not try to associate activation keys with content views that are
  not ready yet (tlestach@redhat.com)

* Tue Jun 02 2015 Tomas Lestach <tlestach@redhat.com> 0.10.16-1
- 1215199 - support different repository architectures within one repository
  set (tlestach@redhat.com)

* Fri May 29 2015 Tomas Lestach <tlestach@redhat.com> 0.10.14-1
- addressing the rest of rubocop 0.31.0 issues (tlestach@redhat.com)
- rubocop: addressing various offenses (lpramuk@redhat.com)
- 1224268 - adapt repository enablement for Sat 6.1 API changes
  (tlestach@redhat.com)
- since rubocop 0.27 a new cop got hired (lpramuk@redhat.com)
- Detect broken CSV (mkollar@redhat.com)

* Mon May 11 2015 Justin Sherrill <jsherril@redhat.com> 0.10.13-1
- Update hammer_cli_import.gemspec (zleite@gmail.com)

* Mon Apr 13 2015 Tomas Lestach <tlestach@redhat.com> 0.10.12-1
- use absolute export directory path for the rpmbuild instructions
  (tlestach@redhat.com)

* Fri Apr 10 2015 Tomas Lestach <tlestach@redhat.com> 0.10.11-1
- 1165825 - use only the latest content view version (tlestach@redhat.com)
- detect a synced repository (tlestach@redhat.com)
- prevent nil exception addressing: Caught TypeError:no implicit conversion of
  nil into String while processing CSV line: ... /usr/share/gems/gems/hammer_cl
  i_import-0.10.6.3/lib/hammer_cli_import/templatesnippet.rb:41:in `+' /usr/sha
  re/gems/gems/hammer_cli_import-0.10.6.3/lib/hammer_cli_import/templatesnippet
  .rb:41:in `mk_snippet_hash' /usr/share/gems/gems/hammer_cli_import-0.10.6.3/l
  ib/hammer_cli_import/templatesnippet.rb:57:in `import_single_row' /usr/share/
  gems/gems/hammer_cli_import-0.10.6.3/lib/hammer_cli_import/base.rb:511:in
  `call' /usr/share/gems/gems/hammer_cli_import-0.10.6.3/lib/hammer_cli_import/
  base.rb:511:in `block (2 levels) in cvs_iterate' /usr/share/gems/gems/hammer_
  cli_import-0.10.6.3/lib/hammer_cli_import/importtools.rb:302:in `call' /usr/s
  hare/gems/gems/hammer_cli_import-0.10.6.3/lib/hammer_cli_import/importtools.r
  b:302:in `handle_missing_and_supress' /usr/share/gems/gems/hammer_cli_import-
  0.10.6.3/lib/hammer_cli_import/base.rb:510:in `block in cvs_iterate' ...
  (tlestach@redhat.com)
- 1136361 - add 'logtrace <exception>' logging-method (ggainey@redhat.com)
- 1136899 - with_synced_repo will always issue action if repo is already sync'd
  (ggainey@redhat.com)
- 1136841 - give a better error-msg when repo-enable fails (ggainey@redhat.com)

* Tue Feb 24 2015 Grant Gainey 0.10.10-1
- 1195329 - Fix AK-update call and some warning-verbiage (ggainey@redhat.com)

* Wed Feb 18 2015 Grant Gainey 0.10.9-1
- 1192581 - Made prev commit more reliable/safer (ggainey@redhat.com)

* Wed Feb 18 2015 Grant Gainey 0.10.8-1
- 1192581 - special-case org-create call (ggainey@redhat.com)

* Tue Feb 17 2015 Grant Gainey 0.10.7-1
- 1192556 - Remove need to dig out auth-credentials * Remove api_usr and
  api_pwd * Teach config-file to call Repository::UploadContentCommand directly
  (ggainey@redhat.com)
- 1192556 - The way to dig out apipie-binding auth changed in 0.11
  (ggainey@redhat.com)

* Fri Dec 05 2014 Grant Gainey 0.10.6-1
- 1160847 - interface-macros are special. (ggainey@redhat.com)
- 1165151 - Integer(nil) behavior chgd between 1.8.7 and 2.0
  (ggainey@redhat.com)

* Thu Oct 09 2014 Grant Gainey 0.10.5-1
- 1140256 - system-profile-transition rpm should avoid using advanced rpmlib
  capabilities (lpramuk+github@redhat.com)
- 1138696 - propagate --synchronize and --wait options to the import content-
  view sub-command (tlestach@redhat.com)

* Wed Sep 03 2014 Tomas Lestach <tlestach@redhat.com> 0.10.4-1
- 1136530 - remove dist tag from release in the rpmbuild instructions
  (tlestach@redhat.com)
- 1136463 - do not create composite content view, if no there're no associated
  channels (tlestach@redhat.com)
- do not print the rpmbuild instructions if no system profiles were
  transitioned (tlestach@redhat.com)

* Tue Sep 02 2014 Tomas Lestach <tlestach@redhat.com> 0.10.3-1
- fix exception message (tlestach@redhat.com)
- import the test config-file into the 100 org as all the other entities
  (tlestach@redhat.com)
- Fix tests (mkollar@redhat.com)
- catch exception when publishing of content view fails (tlestach@redhat.com)
- Simple test enriched for configuration thingies... (mkollar@redhat.com)
- Field last_sync id not always set (mkollar@redhat.com)
- 1136011 - require rubygem(hammer_cli_foreman) (tlestach@redhat.com)
- as delete_content_view does not throw exception at failure
  (tlestach@redhat.com)
- catch sat6 delete excetion for content view versions removal
  (tlestach@redhat.com)
- fix typo in the test (tlestach@redhat.com)
- catch sat6 delete exception and count them into summary (tlestach@redhat.com)
- do not count unavailable entities as :found when deleting
  (tlestach@redhat.com)
- add the innocent line lost by refactoring (tlestach@redhat.com)
- 1133846 - Teach config-file the diff between 'created' and 'wrote'   -
  Summary now recognizes :wrote and :failed   - configfile summarizes
  filesystem ops as :wrote   - configfile.rb checks for hammer-invocation-
  failure   - tripped over/fixed a bug in rcop fix from prev commit
  (ggainey@redhat.com)
- rubocop: lib/hammer_cli_import/base.rb:345:5: C: Cyclomatic complexity for
  create_entity is too high. [20/11]  - Broke out the error-checking in
  create_entity into bite-sized pieces (ggainey@redhat.com)
- 1135588 - Teach config-file to reuse credentials from @api
  (ggainey@redhat.com)
- add template snippet import to simple test (tlestach@redhat.com)
- catch exceptions when deleting system content views (tlestach@redhat.com)
- extent recognizing of already existing objects (tlestach@redhat.com)
- return object if mapped as create_entity does (tlestach@redhat.com)
- 1134576 - do not call methods on nil, ruby does not like it
  (tlestach@redhat.com)
- do not export_files in case @modules weren't even initialized
  (tlestach@redhat.com)
- Change the way of obtaining @api (mkollar@redhat.com)
- 1133972 - adapt code to actual sat6 exception (tlestach@redhat.com)
- Address state without initialized var (mkollar@redhat.com)
- delete orgs as it should work now (tlestach@redhat.com)
- Rewording (mkollar@redhat.com)
- when searching for a content view, first check redhat cvs
  (tlestach@redhat.com)
- 1133547 - Fix missing module name... (mkollar@redhat.com)

* Mon Aug 25 2014 Tomas Lestach <tlestach@redhat.com> 0.10.2-1
- adding el7 tito support (jsherril@redhat.com)
- This actually can be useful (mkollar@redhat.com)
- 1132481 - rename ~/data directory to ~/.transition_data (tlestach@redhat.com)
- replace ak with "activation key" (tlestach@redhat.com)
- Apply abstracted code for suppressing exceptions (mkollar@redhat.com)
- Abstract often used exception handling (mkollar@redhat.com)
- 1132644 - Pass along --no-async if specified (ggainey@redhat.com)
- 1132642 - put back --macro-mapping to 'all' (ggainey@redhat.com)
- 1132553 - Fix config-files descr (ggainey@redhat.com)
- Handle exceptions in post import (mkollar@redhat.com)
- Colors for simple test (mkollar@redhat.com)
- New rubocop: rubocop-0.25.0 (mkollar@redhat.com)
- 1130558 - do not check 'updated_at', it is unreliable (mkollar@redhat.com)

* Tue Aug 19 2014 Tomas Lestach <tlestach@redhat.com> 0.10.1-1
- fix content host and host collection association (tlestach@redhat.com)
- enhance exception message (tlestach@redhat.com)
- use set instead of an array (tlestach@redhat.com)
- generate 1 server rpm instead of client rpm per org (tlestach@redhat.com)
- 1130183 - Use extends (so needed methods will be added) (mkollar@redhat.com)
- Use existing logging capabilities (mkollar@redhat.com)
- 1130183 - Add possibility to things in one thread (mkollar@redhat.com)
- Typo (mkollar@redhat.com)
- 1130508 - add --delete to 'all' (ggainey@redhat.com)
- 1127800 - let's work with uuid as content host id (tlestach@redhat.com)
- 1120839 - Backtrace log level finetuning (mkollar@redhat.com)
- replace all underscore characters with spaces (tlestach@redhat.com)
- Handle MissingObjectError in appropriate way (mkollar@redhat.com)
- allow deleting content views without any versions published
  (tlestach@redhat.com)
- enhance to_singular method (tlestach@redhat.com)
- replace all unallowed characters from content view names
  (tlestach@redhat.com)
- add one more sytem profile to simple test (tlestach@redhat.com)
- 1125035 - Removed some more no-longer-relevant TODO comments
  (ggainey@redhat.com)
- 1125035 - Remove ancient TODO comment, because it was to-did
  (ggainey@redhat.com)
- Associate ak with environment (mkollar@redhat.com)
- Enhance readme (mkollar@redhat.com)

* Mon Aug 11 2014 Grant Gainey 0.10.0-1
- allow content view --delete to be executed multiple times
  (tlestach@redhat.com)
- move initialization of @map earlier (tlestach@redhat.com)
- introduce --delete option for simple test (tlestach@redhat.com)
- Rubocop doesn't like some of out more-complicated things.
  (ggainey@redhat.com)
- Fix our attempt to publish RH-content-view. Spit out a useful error when it
  fails (ggainey@redhat.com)
- do not delete orgs, since it's disabled (tlestach@redhat.com)
- introduce post_delete (tlestach@redhat.com)
- include persistent map (tlestach@redhat.com)
- add content-host import to the simple test (tlestach@redhat.com)
- system_content_views persistant map (tlestach@redhat.com)
- sort persistent maps alphabetically (tlestach@redhat.com)
- associate content views with content hosts (tlestach@redhat.com)
- check among redhat content view, if id not found among the custom content
  views (tlestach@redhat.com)
- start creating composite content views for content hosts
  (tlestach@redhat.com)
- let's use Spacewalk 2.2 client as 2nd repository (tlestach@redhat.com)
- fix bracket for better substitution (tlestach@redhat.com)
- add activation keys to simple test (tlestach@redhat.com)
- move composite content view creation to importtools (tlestach@redhat.com)
- Skip activation-keys with 'Satellite default' (mkollar@redhat.com)
- 1126239 - Add content-host to Things Import-All Knows (ggainey@redhat.com)
- 1126882 - move default-cfgs to cli.modules.d/import (ggainey@redhat.com)
- 1127263 - Add info about files and puppet-modules to summary
  (ggainey@redhat.com)
- 1126618 - false != :false, was causing upload to *always* be skipped
  (ggainey@redhat.com)
- Use preferred way to map existing entities (mkollar@redhat.com)
- 1126155 - slightly better (mkollar@redhat.com)
- 1126155 - hide potentially confusing messages (mkollar@redhat.com)
- --export-directory option not required with combination of --delete option
  (tlestach@redhat.com)
- No really, fixing args for import-all for *sure* this time
  (ggainey@redhat.com)
- Fix arg-breakage in import-all (ggainey@redhat.com)
- Be consistent in plural for report_summary (mkollar@redhat.com)
- 1126618 - Add --generate-only to config-file (ggainey@redhat.com)
- Report sipping of content-view (mkollar@redhat.com)
- 1126842 - Need to quote the values in config_macros.yml (ggainey@redhat.com)
- Fix logging so that --debug actually works (ggainey@redhat.com)
- 1126493 - Set 'description' for cfg-chan puppet module. Fix it so
  #{module_name} actually works as well (ggainey@redhat.com)
- 1126027 - create product/repo for local stuff only when needed
  (mkollar@redhat.com)
- Handle empty summary nicely (mkollar@redhat.com)
- configfile - hide unsilence-able puppet output (ggainey@redhat.com)

* Sun Aug 03 2014 Grant Gainey 0.9.1-1
- Minor comment cleanup (ggainey@redhat.com)
- Rubocop: Prefer single-quoted strings when you don't need string
  interpolation or special symbols. (ggainey@redhat.com)
- Don't override execute just to do something once (ggainey@redhat.com)
- 1126103 - config-file needs its own persistence-type, :puppet_repositories
  (ggainey@redhat.com)
- Add correct missing interview_answers.yml (ggainey@redhat.com)
- missing interview_answers.yml prevents RPM from building (lpramuk@redhat.com)
- 1126063 - Teach import config-file to find/use interview_answers.yml
  (ggainey@redhat.com)
- Report repository skipping (mkollar@redhat.com)
- Report manifest uploading (mkollar@redhat.com)
- Summary reporting (mkollar@redhat.com)
- add another repo to the test (tlestach@redhat.com)
- update sync repo message (tlestach@redhat.com)
- work with absolute path (tlestach@redhat.com)
- create simple content views within the test (tlestach@redhat.com)
- do not count the entities in the test (tlestach@redhat.com)
- print the issued import command (tlestach@redhat.com)
- run the tests in verbose mode (tlestach@redhat.com)
- just notify about unexpected entity count instead of dying
  (tlestach@redhat.com)
- change tests org_id to 100 (tlestach@redhat.com)
- enhance test (tlestach@redhat.com)
- Rubocop: lib/hammer_cli_import/user.rb:85:77: C: Do not use semicolons to
  terminate expressions. lib/hammer_cli_import/all.rb:135:7: C: Cyclomatic
  complexity for build_args is too high. [12/11] (ggainey@redhat.com)
- 1124967 - teach upload-manifest to wait for task to finish
  (ggainey@redhat.com)
- 1125034 - teach --verbose to only emit if >= current-log-level
  (ggainey@redhat.com)
- 1125266 - Turn on using Sat6-API to get role-list (ggainey@redhat.com)
- configfile - add macro-mapping to RPM (ggainey@redhat.com)
- configfile - add to 'all' command (ggainey@redhat.com)
- configfiles - Everything works now (including --delete) (ggainey@redhat.com)
- create rpmbuild structure (tlestach@redhat.com)
- export system-id_to_uuid files (tlestach@redhat.com)
- enhance debug message (tlestach@redhat.com)
- fix content host deletion (tlestach@redhat.com)
- content host change (tlestach@redhat.com)
- change type (tlestach@redhat.com)
- Rubocop: Style/Blocks (mkollar@redhat.com)
- Rubocop: Style/LineLength (mkollar@redhat.com)
- Rubocop: Style/PerlBackrefs (mkollar@redhat.com)
- Rubocop: Style/NegatedWhile (mkollar@redhat.com)
- Rubocop: Style/MethodCallParentheses (mkollar@redhat.com)
- Rubocop: Style/EmptyLinesAroundBody (mkollar@redhat.com)
- Rubocop: Style/WhileUntilDo (mkollar@redhat.com)
- Rubocop: Style/SpaceInsideParens (mkollar@redhat.com)
- Rubocop: Style/DeprecatedHashMethods (mkollar@redhat.com)
- Rubocop: Lint/UnusedMethodArgument (mkollar@redhat.com)
- Rubocop: Lint/UnusedBlockArgument (mkollar@redhat.com)
- Rubocop: Style/StringLiterals (mkollar@redhat.com)
- configfiles - DRAFT, main path generally working (ggainey@redhat.com)

* Mon Jul 28 2014 Grant Gainey 0.9.0-1
- 1123837 - Allow hosts with no dot (only tld) (mkollar@redhat.com)
- Check CSV file headers sooner (mkollar@redhat.com)
- 1121131 - Add reportname attr to commands to describe which sw-report they
  understand (ggainey@redhat.com)
- 1122169 - Add someexplanantion to --upload-manifests-from
  (ggainey@redhat.com)
- 1121986 - setup logging at init, not at execute (ggainey@redhat.com)
- Do not discard content of log file (prefer append) (mkollar@redhat.com)
- Activation keys with contentviews with rh cotent (mkollar@redhat.com)
- sat6-latest appears to no longer wrap orgs (ggainey@redhat.com)
- Add support for clones of Red Hat Channels (mkollar@redhat.com)
- Do not mix translated and untranslated ids (mkollar@redhat.com)

* Tue Jul 15 2014 Grant Gainey 0.8.0-1
- rubocop, where is thy sting? (ggainey@redhat.com)
- Sprint-7 demo response: standardize logging * Added calls for
  debug/info/progress/wanbr/error/fatal * Added quiet/verbose/debug/logfile
  switches * Changed instances of 'puts' and 'p' to use the new options
  (ggainey@redhat.com)
- Fiddle with asyntaskscreactor statuses... (mkollar@redhat.com)
- Use ID instead of label (mkollar@redhat.com)
- More suitable message (mkollar@redhat.com)
- Protect persistent map (mkollar@redhat.com)
- Teach all about wait/sync (ggainey@redhat.com)
- Teach 'all' about manifest-directory (ggainey@redhat.com)
- fixed: WARN Legacy configuration of modules detected. (lpramuk@redhat.com)
- specfile: on rhel7 gems live elsewhere (lpramuk@redhat.com)
- O(n log n) -> O(n) (mkollar@redhat.com)
- Removing debugging-rescue (ggainey@redhat.com)
- RuboCop (mkollar@redhat.com)
- Last synced field might not be parsable (mkollar@redhat.com)
- Look for and upload manifests as we import organizations (ggainey@redhat.com)
- Integrate reactor into repository-enable (mkollar@redhat.com)
- Just a little note for the future generations (mkollar@redhat.com)
- Handle non-mapped channels (mkollar@redhat.com)
- Move check for existence of file to the right place (mkollar@redhat.com)
- Fix capitalization (mkollar@redhat.com)
- Better debugging message (mkollar@redhat.com)
- Consistency (mkollar@redhat.com)
- One TODO down... (mkollar@redhat.com)
- Detect sync in progress (mkollar@redhat.com)
- Allow user to do Ctrl-C (mkollar@redhat.com)
- Update README (mkollar@redhat.com)
- RuboCop ... almost (mkollar@redhat.com)
- Fix me! 87 (mkollar@redhat.com)
- Be more specific about exception caught (mkollar@redhat.com)
- Whoops... (mkollar@redhat.com)
- Unnecessary proc re-creaction (mkollar@redhat.com)
- Check whether we are deleting compatible entity (mkollar@redhat.com)
- RuboCop: SignalException (mkollar@redhat.com)
- Make raising/failing consistent (mkollar@redhat.com)
- Run tasks with no prerequisites in main thread (mkollar@redhat.com)
- Cleanup (mkollar@redhat.com)
- move content view deletion to a separate module, so we can re-use it from
  multiple subcommands (tlestach@redhat.com)
- create a common composite_rhcv_id (tlestach@redhat.com)
- delete Red Hat content views (tlestach@redhat.com)
- some repos do not have 'url' (tlestach@redhat.com)
- create content views from Red Hat channels (tlestach@redhat.com)
- Use new repository synchronization (mkollar@redhat.com)
- New methods for repository syncing (mkollar@redhat.com)
- Be more verbose when main thread finished (mkollar@redhat.com)
- Catch exceptions in asynchronous tasks... (mkollar@redhat.com)
- Start using AsyncTasksReactor (mkollar@redhat.com)
- Determine state of multiple asynchronous tasks (mkollar@redhat.com)
- Meanwhile in the real world... (mkollar@redhat.com)
- Alternate status messages (mkollar@redhat.com)
- AsyncTasksReactor playground (mkollar@redhat.com)
- Reactor for asynchronous tasks (mkollar@redhat.com)
- move read_channel_map to a separate file in 'scripts' directory
  (tlestach@redhat.com)
- enhance error message (tlestach@redhat.com)
- sort persistent map definitions (tlestach@redhat.com)
- sat6 system uuid is actually a String ... (tlestach@redhat.com)
- associate virtual guests for virtual hosts (tlestach@redhat.com)
- introduce migrating of system profiles to content hosts (tlestach@redhat.com)
- We can iterate over users directly (mkollar@redhat.com)
- fix commas (tlestach@redhat.com)
- more universal transcript (tlestach@redhat.com)
- sort the @prerequisite keys (tlestach@redhat.com)
- inserting one key=>value into a hash multiple times does not make any
  difference (tlestach@redhat.com)
- RuboCop (mkollar@redhat.com)
- Avoid problems in the future (mkollar@redhat.com)
- Avoid problems (mkollar@redhat.com)
- Describe args using args.join() instead of args.inspect (ggainey@redhat.com)
- Teach 'all' about new entities and new options (ggainey@redhat.com)
- 1114103 - Don't assume @prereqs quite so much (ggainey@redhat.com)
- Method api_init actually can be called multiple times (mkollar@redhat.com)
- :users needs :orgs as prereq (ggainey@redhat.com)
- organization simplification (tlestach@redhat.com)
- extend cache search and detect already enabled/unknown repos
  (tlestach@redhat.com)
- store repo to cache (tlestach@redhat.com)
- allow to disable repository_sets (tlestach@redhat.com)
- introduce prerequisities for server entities (tlestach@redhat.com)
- map redhat repositories (tlestach@redhat.com)
- move per row work to import_single_row (tlestach@redhat.com)
- Reproducers HOW TO (mkollar@redhat.com)
- rubocop-0.24.0 issue (tlestach@redhat.com)
- Revert back to get_cache so we only enable repos for orgs that the tool knows
  about. Add some messaging to avoid user-confusion. (ggainey@redhat.com)
- Nicer message (mkollar@redhat.com)

* Tue Jun 24 2014 Grant Gainey 0.7.2-1
- Subcommand and option name-chgs in response to comments (ggainey@redhat.com)

* Mon Jun 23 2014 Grant Gainey 0.7.1-1
- Update to 0.7.0 (ggainey@redhat.com)

* Mon Jun 23 2014 Grant Gainey 0.6.2-1
- Add some more documentation (mkollar@redhat.com)
- Some sanity checking (mkollar@redhat.com)
- Added some documentation (mkollar@redhat.com)
- let's build rubygem-hammer_cli_import to katello-nightly-rhel6 tag
  (tlestach@redhat.com)

* Thu Jun 19 2014 Grant Gainey 0.6.1-1
- * Look for the default repository-map where the gem puts it * Clarify the
  output when we decide to enable a repo (ggainey@redhat.com)
- let git ignore .swp files (tlestach@redhat.com)

* Thu Jun 19 2014 Tomas Lestach <tlestach@redhat.com> 0.6.0-1
- initial hammer-cli-import tag


