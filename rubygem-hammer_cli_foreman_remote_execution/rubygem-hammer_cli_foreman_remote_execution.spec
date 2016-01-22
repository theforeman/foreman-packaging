%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%{!?_root_sysconfdir:%global _root_sysconfdir %{_sysconfdir}}

%global gem_name hammer_cli_foreman_remote_execution
%global confdir hammer

Summary: Foreman Remote Execution commands for Hammer CLI
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.0.4
Release: 1%{?foremandist}%{?dist}
Group: Applications/System
License: GPLv3
URL: http://github.com/theforeman/hammer_cli_foreman_remote_execution
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(hammer_cli_foreman) >= 0.1.3
Requires: %{?scl_prefix}rubygem(hammer_cli_foreman) < 1.0.0
Requires: %{?scl_prefix}rubygem(hammer_cli_foreman_tasks) >= 0.0.3
Requires: %{?scl_prefix}rubygem(hammer_cli_foreman_tasks) < 0.1.0
BuildRequires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
This Hammer CLI plugin contains set of commands for foreman_remote_execution

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

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
mkdir -p %{buildroot}%{_root_sysconfdir}/%{confdir}/cli.modules.d
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* %{buildroot}%{gem_dir}/
cp -pa .%{gem_instdir}/config/foreman_remote_execution.yml %{buildroot}%{_root_sysconfdir}/%{confdir}/cli.modules.d/foreman_remote_execution.yml

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/%{gem_name}.gemspec
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/test
%{gem_instdir}/Rakefile
%{gem_instdir}/lib
%{gem_instdir}/config
%config(noreplace) %{_root_sysconfdir}/%{confdir}/cli.modules.d/foreman_remote_execution.yml
%doc %{gem_instdir}/LICENSE
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Wed Jan 06 2016 Dominic Cleal <dcleal@redhat.com> 0.0.2-2
- Add foremandist to plugin (dcleal@redhat.com)
- Fix spec filename to match RPM (dcleal@redhat.com)

* Fri Dec 11 2015 Stephen Benjamin <stephen@redhat.com> 0.0.2-1
- Initial release
