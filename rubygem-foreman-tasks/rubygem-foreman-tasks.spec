%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%if "%{?scl}" == "ruby193"
    %global scl_ruby /usr/bin/ruby193-ruby
%else
    %global scl_ruby /usr/bin/ruby
%endif

%global gem_name foreman-tasks

%define rubyabi 1.9.1
%global foreman_bundlerd_dir /usr/share/foreman/bundler.d
%global confdir deploy
%global service_name foreman-tasks

Summary: Tasks support for Foreman with Dynflow integration
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.6.10
Release: 1%{?dist}
Group: Development/Libraries
License: GPLv3
URL: http://github.com/theforeman/foreman-tasks
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem
Requires: foreman

%if 0%{?fedora} > 18
Requires:       %{?scl_prefix}ruby(release)
%else
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
%endif

Requires: %{?scl_prefix}rubygem(dynflow) >= 0.7.2
Requires: %{?scl_prefix}rubygem(sequel)
Requires: %{?scl_prefix}rubygem(sinatra)
Requires: %{?scl_prefix}rubygem(daemons)
Requires: %{?scl_prefix}rubygems
%if 0%{?rhel} == 6
Requires(post): chkconfig
Requires(preun): chkconfig
Requires(preun): initscripts
%else
Requires(post): systemd-sysv
Requires(post): systemd-units
Requires(preun): systemd-units
BuildRequires: systemd-units
%endif
BuildRequires: %{?scl_prefix}rubygems-devel

%if 0%{?fedora} > 18
BuildRequires:       %{?scl_prefix}ruby(release)
%else
BuildRequires: %{?scl_prefix}ruby(abi) = 1.9.1
%endif
BuildRequires: %{?scl_prefix}rubygems
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

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
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0} --no-rdoc --no-ri
%{?scl:"}

%build
sed -ri '1sX(/usr/bin/ruby|/usr/bin/env ruby)X%{scl_ruby}X' %{_builddir}/%{pkg_name}-%{version}/%{gem_instdir}/bin/%{service_name}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{foreman_bundlerd_dir}
cat <<GEMFILE > %{buildroot}%{foreman_bundlerd_dir}/foreman-tasks.rb
gem 'foreman-tasks'
GEMFILE

#copy init scripts and sysconfigs
%if 0%{?fedora} > 18
install -Dp -m0644 %{buildroot}%{gem_dir}/gems/%{gem_name}-%{version}/%{confdir}/%{service_name}.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/%{service_name}
install -Dp -m0755 %{buildroot}%{gem_dir}/gems/%{gem_name}-%{version}/%{confdir}/%{service_name}.service %{buildroot}%{_libdir}/systemd/system/%{service_name}.service
mkdir -p %{buildroot}%{_bindir}
ln -sv %{gem_instdir}/bin/%{service_name} %{buildroot}%{_bindir}/%{service_name}
%else
install -Dp -m0644 %{buildroot}%{gem_dir}/gems/%{gem_name}-%{version}/%{confdir}/%{service_name}.sysconfig %{buildroot}%{_root_sysconfdir}/sysconfig/%{service_name}
mkdir -p %{buildroot}%{_root_bindir}
ln -sv %{gem_instdir}/bin/%{service_name} %{buildroot}%{_root_bindir}/%{service_name}
%if 0%{?rhel} == 6
install -Dp -m0755 %{buildroot}%{gem_dir}/gems/%{gem_name}-%{version}/%{confdir}/%{service_name}.init %{buildroot}%{_root_initddir}/%{service_name}
%else
install -Dp -m0755 %{buildroot}%{gem_dir}/gems/%{gem_name}-%{version}/%{confdir}/%{service_name}.service %{buildroot}%{_root_libdir}/systemd/system/%{service_name}.service
%endif
%endif

%post
type foreman-selinux-relabel >/dev/null 2>&1 && foreman-selinux-relabel 2>&1 >/dev/null || true
%if 0%{?rhel} == 6
  /sbin/chkconfig --add %{service_name}
  exit 0
%else
  if [ $1 -eq 1 ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
  fi
%endif

%preun
if [ $1 -eq 0 ] ; then
  %if 0%{?rhel} == 6
    /sbin/service %{service_name} stop >/dev/null 2>&1
    /sbin/chkconfig --del %{service_name}
  %else
    /bin/systemctl --no-reload disable %{service_name}.service >/dev/null 2>&1 || :
    /bin/systemctl stop %{service_name}.service >/dev/null 2>&1 || :
  %endif
fi

%files
%dir %{gem_instdir}
%{gem_instdir}/app
%{gem_instdir}/bin
%{gem_instdir}/lib
%{gem_instdir}/config
%{gem_instdir}/db
%exclude %{gem_cache}
%{gem_spec}
%{foreman_bundlerd_dir}/foreman-tasks.rb
%doc %{gem_instdir}/LICENSE

%if 0%{?fedora} > 18
%{_libdir}/systemd/system/%{service_name}.service
%{_sysconfdir}/sysconfig/%{service_name}
%{_bindir}/%{service_name}
%else
%{_root_bindir}/%{service_name}
%if 0%{?rhel} == 6
%{_root_sysconfdir}/rc.d/init.d/%{service_name}
%else
%{_root_libdir}/systemd/system/%{service_name}.service
%endif
%{_root_sysconfdir}/sysconfig/%{service_name}
%endif


%exclude %{gem_instdir}/deploy
%exclude %{gem_instdir}/test
%exclude %{gem_dir}/cache/%{gem_name}-%{version}.gem

%files doc
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.md

%changelog
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

