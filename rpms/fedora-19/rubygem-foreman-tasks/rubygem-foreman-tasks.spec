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
%global jobs_name foreman-tasks

Summary: Tasks support for Foreman with Dynflow integration
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.5.3
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

Requires: %{?scl_prefix}rubygem(dynflow) >= 0.6.0
Requires: %{?scl_prefix}rubygem(sequel)
Requires: %{?scl_prefix}rubygem(sinatra)
Requires: %{?scl_prefix}rubygem(daemons)
Requires: %{?scl_prefix}rubygems
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
sed -ri '1sX(/usr/bin/ruby|/usr/bin/env ruby)X%{scl_ruby}X' %{_builddir}/%{pkg_name}-%{version}/%{gem_instdir}/bin/%{jobs_name}

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
install -Dp -m0644 %{buildroot}%{gem_dir}/gems/%{gem_name}-%{version}/%{confdir}/%{jobs_name}.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/%{jobs_name}
install -Dp -m0755 %{buildroot}%{gem_dir}/gems/%{gem_name}-%{version}/%{confdir}/%{jobs_name}.service %{buildroot}%{_libdir}/systemd/system/%{jobs_name}.service
mkdir -p %{buildroot}%{_bindir}
ln -sv %{gem_instdir}/bin/%{jobs_name} %{buildroot}%{_bindir}/%{jobs_name}
%else
install -Dp -m0644 %{buildroot}%{gem_dir}/gems/%{gem_name}-%{version}/%{confdir}/%{jobs_name}.sysconfig %{buildroot}%{_root_sysconfdir}/sysconfig/%{jobs_name}
mkdir -p %{buildroot}%{_root_bindir}
ln -sv %{gem_instdir}/bin/%{jobs_name} %{buildroot}%{_root_bindir}/%{jobs_name}
%if 0%{?rhel} == 6
install -Dp -m0755 %{buildroot}%{gem_dir}/gems/%{gem_name}-%{version}/%{confdir}/%{jobs_name}.init %{buildroot}%{_root_initddir}/%{jobs_name}
%else
install -Dp -m0755 %{buildroot}%{gem_dir}/gems/%{gem_name}-%{version}/%{confdir}/%{jobs_name}.service %{buildroot}%{_root_libdir}/systemd/system/%{jobs_name}.service
%endif
%endif

%preun
if [ $1 -eq 0 ] ; then
    /sbin/service %{jobs_name} stop >/dev/null 2>&1
    /sbin/chkconfig --del %{jobs_name}
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
%{_libdir}/systemd/system/%{jobs_name}.service
%{_sysconfdir}/sysconfig/%{jobs_name}
%{_bindir}/%{jobs_name}
%else
%{_root_bindir}/%{jobs_name}
%if 0%{?rhel} == 6
%{_root_sysconfdir}/rc.d/init.d/%{jobs_name}
%else
%{_root_libdir}/systemd/system/%{jobs_name}.service
%endif
%{_root_sysconfdir}/sysconfig/%{jobs_name}
%endif


%exclude %{gem_instdir}/deploy
%exclude %{gem_instdir}/test
%exclude %{gem_dir}/cache/%{gem_name}-%{version}.gem

%files doc
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.md

%changelog
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

