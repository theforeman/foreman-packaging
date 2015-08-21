%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%{!?_root_sysconfdir:%global _root_sysconfdir %{_sysconfdir}}

%global gem_name hammer_cli_foreman_tasks
%global confdir hammer

Summary: Foreman CLI plugin for showing task information for resources and users
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.0.7
Release: 2%{?dist}
Group: Applications/Systems
License: GPLv3+
URL: http://github.com/theforeman/hammer-cli-foreman-tasks
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem

%if 0%{?fedora} > 18
Requires: %{?scl_prefix_ruby}ruby(release)
%else
Requires: %{?scl_prefix_ruby}ruby(abi)
%endif

Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(hammer_cli_foreman) > 0.1.1
Requires: %{?scl_prefix}rubygem(hammer_cli_foreman) < 0.4.0
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
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} - << \EOF}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}
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
%config(noreplace) %{_root_sysconfdir}/%{confdir}/cli.modules.d/foreman_tasks.yml
%{gem_spec}
%exclude %{gem_cache}
%doc %{gem_instdir}/LICENSE

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/config
%doc %{gem_instdir}/README.md

%changelog
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
