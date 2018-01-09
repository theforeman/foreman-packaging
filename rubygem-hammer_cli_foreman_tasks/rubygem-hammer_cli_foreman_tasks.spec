%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%{!?_root_sysconfdir:%global _root_sysconfdir %{_sysconfdir}}

%global gem_name hammer_cli_foreman_tasks
%global confdir hammer

Summary: Foreman CLI plugin for showing task information for resources and users
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.0.12
Release: 2%{?foremandist}%{?dist}
Group: Applications/Systems
License: GPLv3+
URL: https://github.com/theforeman/hammer-cli-foreman-tasks
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(hammer_cli_foreman) > 0.1.1
Requires: %{?scl_prefix}rubygem(hammer_cli_foreman) < 1.0.0
Requires: %{?scl_prefix}rubygem(powerbar) >= 1.0.11
Requires: %{?scl_prefix}rubygem(powerbar) < 1.1.0
BuildRequires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}
%if 0%{?scl:1}
Obsoletes: rubygem-%{gem_name} < 0.0.7-2
%endif

%description
Foreman CLI plugin for showing task information for resources and users

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
BuildArch: noarch
%if 0%{?scl:1}
Obsoletes: rubygem-%{gem_name}-doc < 0.0.7-2
%endif

%description doc
Documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_root_sysconfdir}/%{confdir}/cli.modules.d
install -m 755 .%{gem_instdir}/config/foreman_tasks.yml \
               %{buildroot}%{_root_sysconfdir}/%{confdir}/cli.modules.d/foreman_tasks.yml

%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%{gem_instdir}/locale
%config(noreplace) %{_root_sysconfdir}/%{confdir}/cli.modules.d/foreman_tasks.yml
%{gem_spec}
%exclude %{gem_cache}
%doc %{gem_instdir}/LICENSE

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/config
%doc %{gem_instdir}/README.md

%changelog
* Tue Jan 09 2018 Eric D. Helms <ericdhelms@gmail.com> 0.0.12-2
- Bump releases for base foreman plugins packages (ericdhelms@gmail.com)

* Wed Oct 25 2017 Eric D. Helms <ericdhelms@gmail.com> 0.0.12-1
- Update hammer-cli-foreman-tasks 0.0.12 (inecas@redhat.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Wed May 04 2016 Dominic Cleal <dominic@cleal.org> 0.0.10-2
- Use gem_install macro (dominic@cleal.org)

* Fri Feb 19 2016 Dominic Cleal <dominic@cleal.org> 0.0.10-1
- Release hammer_cli_foreman_tasks 0.0.10 (stbenjam@redhat.com)

* Mon Jan 25 2016 Dominic Cleal <dcleal@redhat.com> 0.0.9-2
- Add foremandist to hammer_cli_foreman_tasks (stbenjam@redhat.com)

* Mon Jan 25 2016 Dominic Cleal <dcleal@redhat.com> 0.0.9-1
- Release hammer_cli_foreman_tasks 0.0.9 (stbenjam@redhat.com)

* Thu Dec 24 2015 Dominic Cleal <dcleal@redhat.com> 0.0.8-2
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Mon Sep 28 2015 Dominic Cleal <dcleal@redhat.com> 0.0.8-1
- update hammer_cli_foreman_tasks to 0.0.8 (RPM) (jsherril@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 0.0.7-3
- Converted to tfm SCL (dcleal@redhat.com)

* Thu Aug 20 2015 Dominic Cleal <dcleal@redhat.com> 0.0.7-2
- Increase range of non-SCL obsoletes to cover 1.9 versions (dcleal@redhat.com)

* Tue Aug 04 2015 Dominic Cleal <dcleal@redhat.com> 0.0.7-1
- Update rubygem-hammer_cli_foreman_tasks to 0.0.7 (ericdhelms@gmail.com)

* Tue Jul 28 2015 Dominic Cleal <dcleal@redhat.com> 0.0.6-2
- fixes #8979 - convert hammer packages to SCL (dcleal@redhat.com)

* Mon Apr 27 2015 Dominic Cleal <dcleal@redhat.com> 0.0.6-1
- Update hammer_cli_foreman_tasks to 0.0.6 (dcleal@redhat.com)

* Mon Mar 23 2015 Dominic Cleal <dcleal@redhat.com> 0.0.5-1
- new package built with tito
