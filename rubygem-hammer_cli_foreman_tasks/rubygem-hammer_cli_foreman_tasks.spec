%global gem_name hammer_cli_foreman_tasks
%global confdir hammer

Summary: Foreman CLI plugin for showing task information for resources and users
Name: rubygem-%{gem_name}
Version: 0.0.6
Release: 1%{?dist}
Group: Applications/Systems
License: GPLv3+
URL: http://github.com/theforeman/hammer-cli-foreman-tasks
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem

%if 0%{?rhel} == 6
Requires: ruby(abi)
%else
Requires: ruby(release)
%endif

Requires: ruby(rubygems)
Requires: rubygem(hammer_cli_foreman) > 0.1.1
Requires: rubygem(hammer_cli_foreman) < 0.3.0
Requires: rubygem(powerbar) >= 1.0.11
Requires: rubygem(powerbar) < 1.1.0
BuildRequires: ruby(rubygems)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Foreman CLI plugin for showing task information for resources and users

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
%setup -q -c -T
mkdir -p .%{gem_dir}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_sysconfdir}/%{confdir}/cli.modules.d
install -m 755 .%{gem_instdir}/config/foreman_tasks.yml \
               %{buildroot}%{_sysconfdir}/%{confdir}/cli.modules.d/foreman_tasks.yml

%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%config(noreplace) %{_sysconfdir}/%{confdir}/cli.modules.d/foreman_tasks.yml
%{gem_spec}
%exclude %{gem_cache}
%doc %{gem_instdir}/LICENSE

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/config
%doc %{gem_instdir}/README.md

%changelog
* Mon Apr 27 2015 Dominic Cleal <dcleal@redhat.com> 0.0.6-1
- Update hammer_cli_foreman_tasks to 0.0.6 (dcleal@redhat.com)

* Mon Mar 23 2015 Dominic Cleal <dcleal@redhat.com> 0.0.5-1
- new package built with tito

