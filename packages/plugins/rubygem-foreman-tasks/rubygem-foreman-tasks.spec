%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman-tasks

%global foreman_bundlerd_dir /usr/share/foreman/bundler.d

Summary: Tasks support for Foreman with Dynflow integration
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.14.4
Release: 1%{?foremandist}%{?dist}
Group: Development/Libraries
License: GPLv3
URL: https://github.com/theforeman/foreman-tasks
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: foreman >= 1.17.0

Requires: %{?scl_prefix}rubygem(foreman-tasks-core)
Requires: %{?scl_prefix}rubygem(dynflow) >= 1.1.5
Requires: %{?scl_prefix}rubygem(dynflow) < 2.0
Requires: %{?scl_prefix}rubygem(get_process_mem)
Requires: %{?scl_prefix}rubygem(parse-cron) >= 0.1.4
Requires: %{?scl_prefix}rubygem(parse-cron) < 0.2.0
Requires: %{?scl_prefix_ror}rubygem(sinatra)
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}rubygems

BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix}rubygem(foreman-tasks-core)
BuildRequires: %{?scl_prefix}rubygem(dynflow) >= 1.1.1
BuildRequires: %{?scl_prefix}rubygem(dynflow) < 2.0
BuildRequires: %{?scl_prefix}rubygem(get_process_mem)
BuildRequires: %{?scl_prefix}rubygem(parse-cron) >= 0.1.4
BuildRequires: %{?scl_prefix}rubygem(parse-cron) < 0.2.0
BuildRequires: %{?scl_prefix_ror}rubygem(sinatra)
BuildRequires: foreman-plugin >= 1.17.0
BuildRequires: foreman-assets

BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
The goal of this plugin is to unify the way of showing task statuses across
the Foreman instance.  It defines Task model for keeping the information
about the tasks and Lock for assigning the tasks to resources. The locking
allows dealing with preventing multiple colliding tasks to be run on the
same resource. It also optionally provides Dynflow infrastructure for using
it for managing the tasks.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

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

%foreman_bundlerd_file
%foreman_precompile_plugin -a -s

mkdir -p %{buildroot}%{foreman_pluginconf_dir}
mv %{buildroot}/%{gem_instdir}/config/%{gem_name}.yaml.example \
  %{buildroot}%{foreman_pluginconf_dir}/%{gem_name}.yaml

#link dynflow-debug.sh to be called from foreman-debug
chmod +x %{buildroot}%{gem_instdir}/extra/dynflow-debug.sh
%{__mkdir_p} %{buildroot}%{foreman_dir}/script/foreman-debug.d
ln -s %{gem_instdir}/extra/dynflow-debug.sh %{buildroot}%{foreman_dir}/script/foreman-debug.d/60-dynflow_debug

%post
type foreman-selinux-relabel >/dev/null 2>&1 && foreman-selinux-relabel 2>&1 >/dev/null || true

%posttrans
# We need to run the db:migrate after the install transaction
%foreman_db_migrate
%foreman_db_seed
%foreman_apipie_cache
%foreman_restart
exit 0

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/script
%exclude %{gem_instdir}/%{gem_name}.gemspec
%exclude %{gem_instdir}/Gemfile
%{gem_instdir}/app
%{gem_instdir}/bin
%{gem_libdir}
%{gem_instdir}/config
%{gem_instdir}/db
%{gem_instdir}/deploy
%{gem_instdir}/locale
%{gem_instdir}/extra
%exclude %{gem_cache}
%{gem_spec}
%{foreman_bundlerd_plugin}
%{gem_instdir}/public
%config %{foreman_pluginconf_dir}/%{gem_name}.yaml
%{foreman_apipie_cache_foreman}
%{foreman_apipie_cache_plugin}
%{foreman_dir}/script/foreman-debug.d/60-dynflow_debug
%doc %{gem_instdir}/LICENSE

%exclude %{gem_instdir}/test

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/extra/dynflow-executor.example

%changelog
* Tue Dec 11 2018 Adam Ruzicka <aruzicka@redhat.com> 0.14.4-1
- Update to 0.14.4

* Thu Nov 22 2018 Ivan Nečas <inecas@redhat.com> 0.14.3-1
- Update to 0.14.3

* Tue Nov 06 2018 Ivan Nečas <inecas@redhat.com> 0.14.2-1
- Update to 0.14.2

* Wed Oct 10 2018 Ivan Nečas <inecas@redhat.com> 0.14.1-1
- Update to 0.14.1

* Fri Sep 07 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.14.0-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Tue Jul 31 2018 Ivan Nečas <inecas@redhat.com> 0.14.0-1
- Update to 0.14.0

* Fri Jun 29 2018 Andrew Kofink <akofink@redhat.com> 0.13.3-1
- Update to 0.13.3

* Thu Jun 14 2018 Ivan Nečas <inecas@redhat.com> 0.13.2-1
- Update to 0.13.2

* Wed May 16 2018 Ivan Nečas <inecas@redhat.com> 0.13.1-1
- Update to 0.13.1

* Thu Apr 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.13.0-1
- Update to 0.13.0

* Fri Mar 02 2018 Eric D. Helms <ericdhelms@gmail.com> 0.12.0-1
- Release rubygem-foreman-tasks 0.12.0

* Tue Feb 20 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.11.1-1
- update foreman-tasks to 0.11.1 (kvedulv@kvedulv.de)
- Restructure plugin packages to prepare for obal (pcreech@redhat.com)

* Tue Jan 16 2018 Eric D. Helms <ericdhelms@gmail.com> 0.11.0-2
- Deploy dynflow-executor service via Foreman package (me@daniellobato.me)

* Tue Jan 09 2018 Eric D. Helms <ericdhelms@gmail.com> 0.11.0-1
- Bump foreman-tasks to 0.11.0 (zhunting@redhat.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Tue Aug 15 2017 Eric D. Helms <ericdhelms@gmail.com> 0.10.0-2
- Update foreman-tasks use of foreman_precompile_plugin macro
  (ericdhelms@gmail.com)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Mon Aug 14 2017 Eric D. Helms <ericdhelms@gmail.com> 0.10.0-1
- Update foreman-tasks to 0.10.0 (inecas@redhat.com)

* Wed Jul 12 2017 Eric D. Helms <ericdhelms@gmail.com> 0.9.4-1
-  Update foreman-tasks to 0.9.4 (inecas@redhat.com)

* Wed Jun 28 2017 Eric D. Helms <ericdhelms@gmail.com> 0.9.3-1
- Update foreman-tasks to 0.9.3 (inecas@redhat.com)

* Mon Jun 19 2017 Eric D. Helms <ericdhelms@gmail.com> 0.9.2-1
- Update foreman-tasks to 0.9.2 (inecas@redhat.com)

* Mon Apr 10 2017 Dominic Cleal <dominic@cleal.org> 0.9.1-1
- Update foreman-tasks to 0.9.1 (aruzicka@redhat.com)
- Remove EL6 conditionals (dominic@cleal.org)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Thu Nov 24 2016 Dominic Cleal <dominic@cleal.org> 0.8.6-1
- Update foreman-tasks to 0.8.6 (inecas@redhat.com)

* Fri Sep 16 2016 Dominic Cleal <dominic@cleal.org> 0.8.2-1
- Update foreman-tasks to 0.8.2 (#1347) (inecas@redhat.com)

* Mon Aug 22 2016 Dominic Cleal <dominic@cleal.org> 0.8.0-1
- Update foreman-tasks to 0.8.0 (daviddavis@redhat.com)

* Wed Jun 29 2016 Dominic Cleal <dominic@cleal.org> 0.7.19-1
- Update foreman-tasks to 0.7.19 (inecas@redhat.com)

* Fri Jun 03 2016 Dominic Cleal <dominic@cleal.org> 0.7.18-1
- Build foreman-tasks 0.7.18 (jsherril@redhat.com)

* Tue Apr 26 2016 Dominic Cleal <dominic@cleal.org> 0.7.17-1
- Update foreman-tasks to 0.7.17 (mhulan@redhat.com)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 0.7.16-2
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Mon Apr 11 2016 Dominic Cleal <dominic@cleal.org> 0.7.16-1
- Update foreman-tasks to 0.7.16 (mhulan@redhat.com)

* Tue Mar 15 2016 Dominic Cleal <dominic@cleal.org> 0.7.15-1
- Release foreman-tasks 0.7.15 (RPM) (stbenjam@redhat.com)

* Wed Feb 17 2016 Dominic Cleal <dominic@cleal.org> 0.7.14-1
- Release foreman-tasks 0.7.14 (stbenjam@redhat.com)

* Thu Jan 21 2016 Dominic Cleal <dcleal@redhat.com> 0.7.11-1
- Release foreman-tasks 0.7.11 (RPM) (stbenjam@redhat.com)

* Mon Jan 11 2016 Dominic Cleal <dcleal@redhat.com> 0.7.10-2
- Handle assets, require foreman 1.9 (stbenjam@redhat.com)

* Fri Jan 08 2016 Dominic Cleal <dcleal@redhat.com> 0.7.10-1
- Release foreman-tasks 0.7.10 (RPM) (stbenjam@redhat.com)

* Thu Dec 24 2015 Dominic Cleal <dcleal@redhat.com> 0.7.8-1
- Release foreman-tasks 0.7.8 (stbenjam@redhat.com)
- Update dependencies to ror SCL (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)
- Fixes #12886 - Unnecessary executable bits on service unit file
  (seanokeeffe797@gmail.com)

* Tue Oct 06 2015 Dominic Cleal <dcleal@redhat.com> 0.7.6-1
- Release foreman-tasks 0.7.6 (RPM) (stbenjam@redhat.com)

* Thu Aug 27 2015 Dominic Cleal <dcleal@redhat.com> 0.7.3-2
- Rename scl_ruby variables to scl_ruby_bin, use tfm-ruby (dcleal@redhat.com)
- Converted to tfm SCL (dcleal@redhat.com)

* Mon Aug 17 2015 Dominic Cleal <dcleal@redhat.com> 0.7.3-1
- Update foreman-tasks to 0.7.3 (stbenjam@redhat.com)

* Mon Aug 03 2015 Ivan Nečas <inecas@redhat.com> 0.7.2-1
- Update foreman-tasks to 0.7.2 (inecas@redhat.com)
- Better branched builds with Foreman version macro (dcleal@redhat.com)

* Tue Jul 07 2015 Dominic Cleal <dcleal@redhat.com> 0.7.1-1
- Update foreman-tasks to 0.7.1 (inecas@redhat.com)

* Tue Jun 30 2015 Dominic Cleal <dcleal@redhat.com> 0.6.14-1
- Update foreman-tasks to 0.6.14 (inecas@redhat.com)

* Mon Mar 23 2015 Dominic Cleal <dcleal@redhat.com> 0.6.13-2
- Convert to build apipie resource docs (dcleal@redhat.com)

* Tue Mar 17 2015 Dominic Cleal <dcleal@redhat.com> 0.6.13-1
- Update foreman-tasks to 0.6.13 (inecas@redhat.com)

* Sun Feb 01 2015 Dominic Cleal <dcleal@redhat.com> 0.6.12-2
- Add db:seed to post install (dcleal@redhat.com)

* Fri Jan 30 2015 Ivan Nečas <inecas@redhat.com> 0.6.12-1
- Update foreman-tasks to 0.6.12 (inecas@redhat.com)

* Wed Jan 28 2015 Ivan Nečas <inecas@redhat.com> 0.6.11-1
- Update foreman tasks to 0.6.11 (inecas@redhat.com)

* Mon Dec 15 2014 Dominic Cleal <dcleal@redhat.com> 0.6.10-3
- Replace rubygem(sequel) due to Fedora BZ#1174138 (dcleal@redhat.com)

* Mon Dec 08 2014 Dominic Cleal <dcleal@redhat.com> 0.6.10-2
- Cleanup of spec file (brad@redhat.com)

* Thu Sep 11 2014 Ivan Nečas <inecas@redhat.com> 0.6.10-1
- Fixes #7301 - infrastructure for bulk actions via dynflow (inecas@redhat.com)
- updating for el7 builds (jsherril@redhat.com)

* Wed Aug 20 2014 Ivan Nečas <inecas@redhat.com> 0.6.9-1
- Refs #6297 - fix systemd script (inecas@redhat.com)

* Tue Aug 19 2014 Ivan Nečas <inecas@redhat.com> 0.6.8-1
- Fixes BZ1108645 - Dynflow is available only to admin user
  (aruzicka@redhat.com)
- Fixes #6822/bz1117554 - Tasks search breaks for defualt searches
  (paji@redhat.com)
- Foreman facts import method change (mhulan@redhat.com)

* Wed Aug 06 2014 Ivan Nečas <inecas@redhat.com> 0.6.7-1
- do not attempt to show error information when there are no errors
  (jsherril@redhat.com)
- Added activation key humanizer (aruzicka@redhat.com)

* Thu Jul 24 2014 Ivan Nečas <inecas@redhat.com> 0.6.6-1
- Fix typo (kontakt@pitr.ch)
- Ref #6656 - allow actions to determine if task is already running
  (dtsang@redhat.com)

* Mon Jul 14 2014 Ivan Nečas <inecas@redhat.com> 0.6.5-1
- Bump required dynflow version (inecas@redhat.com)
- Refs #6180 - make sure the task label is set before the planning starts
  (inecas@redhat.com)
- Merge pull request #73 from iNecas/issue/6310 (inecas@redhat.com)
- Merge pull request #75 from iNecas/issue/6296 (inecas@redhat.com)
- Support sub-uri deployments (mhulan@redhat.com)
- Refs #6296 - support for searching for subset of action types
  (inecas@redhat.com)
- Refs #6296 - return humanized task errors in separate field
  (inecas@redhat.com)
- Fixes #6310 - Fix typo and make the lock error message localized
  (inecas@redhat.com)

* Fri Jun 20 2014 Ivan Nečas <inecas@redhat.com> 0.6.4-1
- UX improvements (git@pitr.ch)

* Tue Jun 17 2014 Ivan Nečas <inecas@redhat.com> 0.6.3-1
- Fixes #6193 - increase the db poll size only for executor (inecas@redhat.com)
- Merge pull request #69 from iNecas/issue/5719 (inecas@redhat.com)
- Fixes #6193 - make sure we increase the AR db pool soon enough
  (inecas@redhat.com)
- Refs #5719 - wait for the cancel event being processed (inecas@redhat.com)

* Mon Jun 16 2014 Ivan Nečas <inecas@redhat.com> 0.6.2-1
- Fixes #6224: Prevent increasing db pool size in test environment.
  (ericdhelms@gmail.com)

* Fri Jun 13 2014 Ivan Nečas <inecas@redhat.com> 0.6.1-1
- Refs #6193 - execute planned actions in case the execution was not picked up
  for some reason (inecas@redhat.com)
- Fixes #6193 - increase the database pool to avoid connection timeouts
  (inecas@redhat.com)
- Fixes #6166 - ensure we don't execute the same execution plan twice in a row
  (inecas@redhat.com)

* Tue Jun 10 2014 Ivan Nečas <inecas@redhat.com> 0.6.0-1
- Update dependencies (inecas@redhat.com)
- Fixes #5719 - show the currently running steps and allow canceling when
  possible (inecas@redhat.com)
- Refs #6072 - use unlock words instead of stop to don't give false assumptions
  (inecas@redhat.com)
- Refs #6072 - allow to resume after stopping the task (inecas@redhat.com)
- Refs #6072 - provide more debug information for the task (inecas@redhat.com)
- Refs #4748 - Include error details in humanized output (inecas@redhat.com)

* Wed May 28 2014 Ivan Nečas <inecas@redhat.com> 0.5.7-1
- Refs #5961 - dynflow world init hooks (inecas@redhat.com)
- Fixes #5950 - don't show empty output as {} in humanized form
  (inecas@redhat.com)
- Fixes #5961 - Call SELinux relabel only when present (lzap+git@redhat.com)

* Tue May 27 2014 Ivan Nečas <inecas@redhat.com> 0.5.6-1
- better LockConflict message (git@pitr.ch)
- Add Start/stop auto-refresh button (git@pitr.ch)

* Thu May 22 2014 Ivan Nečas <inecas@redhat.com> 0.5.5-1
- File contexts relabelled after installation (lzap+git@redhat.com)
- Fixes #5778 - make sure that we always execute the planned tasks
  (inecas@redhat.com)

* Thu May 15 2014 Ivan Nečas <inecas@redhat.com> 0.5.4-1
- Add Resume, Stop, Unlock action buttons to Task detail (git@pitr.ch)
- Support linking of entry action to task without locking (inecas@redhat.com)

* Tue Apr 15 2014 Ivan Nečas <inecas@redhat.com> 0.5.3-1
- stupid-simple auto-reloading task show page (git@pitr.ch)
- fix path to setting definition (git@pitr.ch)
- Ensure that it works when task_id nil (git@pitr.ch)
- Add class method .coliding_locks (git@pitr.ch)
- rename .lock? to .lockable? and add .locked? (git@pitr.ch)
- Remove automatic chkconfig after installation (mhulan@redhat.com)
- Fixes #4449, add setting to enable/disable dynflow console.
  (walden@redhat.com)

* Fri Apr 04 2014 Ivan Nečas <inecas@redhat.com> 0.5.2-1
- Add init scripts and foreman-tasks daemon controller (mhulan@redhat.com)

* Tue Apr 01 2014 Ivan Nečas <inecas@redhat.com> 0.5.1-1
- Fix issue if rake is not explicitly in Gemfile (mhulan@redhat.com)

* Tue Mar 25 2014 Ivan Nečas <inecas@redhat.com> 0.5.0-1
- Update dependencies (inecas@redhat.com)
- Merge pull request #41 from iNecas/apipie-bindings (inecas@redhat.com)
- Set up Apipie documentation (inecas@redhat.com)
- Merge pull request #40 from iNecas/limit-rake-executor (inecas@redhat.com)
- Merge pull request #39 from pitr-ch/master (inecas@redhat.com)
- Run separate executor just for selected rake tasks (inecas@redhat.com)
- Better message for LockConflict error (git@pitr.ch)
- Fix update_attributes to work with ActionTriggering (git@pitr.ch)
- Add variable names to be able to debug it (git@pitr.ch)
- Do not propagate error from humanized methods (git@pitr.ch)
- Do not raise when Rake::Task['gettext:find'] is missing (git@pitr.ch)
- Don't precalculate the progress in persistence (inecas@redhat.com)
- Modularize the humanizer (inecas@redhat.com)

* Wed Mar 12 2014 Ivan Nečas <inecas@redhat.com> 0.4.0-1
- Update progress bar to use bootstrap 3.0 (git@pitr.ch)
- Extracting ActionTriggering form ActionSubject module (git@pitr.ch)

* Mon Mar 10 2014 Ivan Nečas <inecas@redhat.com> 0.3.6-1
- Additional scopes for searching getting tasks for actions and resources
  (inecas@redhat.com)

* Thu Mar 06 2014 Ivan Nečas <inecas@redhat.com> 0.3.5-1
- The ActionSubject#sync_action! has not caused waiting for the task
  (inecas@redhat.com)

* Tue Mar 04 2014 Ivan Nečas <inecas@redhat.com> 0.3.4-1
- Extract transaction checking (inecas@redhat.com)

* Mon Mar 03 2014 Ivan Nečas <inecas@redhat.com> 0.3.3-1
- Make sure `require_dependency` is called only once for every action
  (inecas@redhat.com)

* Thu Feb 27 2014 Ivan Nečas <inecas@redhat.com> 0.3.2-1
- Fix adding links to related resources (inecas@redhat.com)

* Tue Feb 25 2014 Ivan Nečas <inecas@redhat.com> 0.3.1-1
- Require dynflow >= 0.5.0 (inecas@redhat.com)

* Tue Feb 25 2014 Ivan Nečas <inecas@redhat.com> 0.3.0-1
- Update license (inecas@redhat.com)
- Use class names for translated humanized_name (git@pitr.ch)
- Do not call #plan_self in #action_subject (git@pitr.ch)
- use new step#action API to retrieve actions in Present phase (git@pitr.ch)
- Do not override hash method, other minor improvements (git@pitr.ch)
- Use active support inflections instead of ad-hoc implementations
  (git@pitr.ch)

* Fri Feb 21 2014 Ivan Nečas <inecas@redhat.com> 0.2.2-1
- Make sure the action hooked into ActiveRecord is not run inside other
  transaction (inecas@redhat.com)
- Raise errors for sync tasks (inecas@redhat.com)

* Wed Feb 19 2014 Ivan Nečas <inecas@redhat.com> 0.2.1-1
- Postpone the initialization of persistence (inecas@redhat.com)
- Update the links to products and repositories (inecas@redhat.com)

* Mon Feb 17 2014 Ivan Nečas <inecas@redhat.com> 0.2.0-1
- Extract the hammer plugin to separate repo. (inecas@redhat.com)
- Fix ArgsSerialization and Lock to use new unified Action phases (git@pitr.ch)
- Update ForemanTasks.trigger to new World#trigger API (git@pitr.ch)
- Support references in action_subject (inecas@redhat.com)
- update to dynflow with unified actions (git@pitr.ch)
- Fix Triggers module to only delegate to ForemanTasks (git@pitr.ch)

* Tue Feb 11 2014 Ivan Nečas <inecas@redhat.com> 0.1.5-1
- Make sure the pid and socket directories exist (inecas@redhat.com)

* Tue Feb 11 2014 Ivan Nečas <inecas@redhat.com> 0.1.4-1
- Fix action triggering (inecas@redhat.com)
- Support sync actions when hooking into Foreman model with Dynflow
  (inecas@redhat.com)
- Fix eager loading with lazy world initialization (inecas@redhat.com)
- Add ForemanTasks::Triggers module to include trigger methods where needed
  (git@pitr.ch)

* Wed Jan 29 2014 Ivan Nečas <inecas@redhat.com> 0.1.3-1
- enforce local executor in rake tasks (inecas@redhat.com)

* Wed Jan 29 2014 Ivan Nečas <inecas@redhat.com> 0.1.2-1
- Delay world initialization when using PhusionPassenger (inecas@redhat.com)
* Mon Jan 27 2014 Ivan Nečas <inecas@redhat.com> 0.1.1-1
- Use separate database when running on sqlite3 (inecas@redhat.com)

* Thu Jan 23 2014 Ivan Nečas <inecas@redhat.com> 0.1.0-1
- new package built with tito
