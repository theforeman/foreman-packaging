%global gem_name hammer_cli_foreman_salt
%global confdir hammer

Summary: Foreman Salt-related commands for Hammer CLI
Name: rubygem-%{gem_name}
Version: 0.0.4
Release: 1%{?dist}
Group: Applications/System
License: GPLv3
URL: http://github.com/theforeman/hammer_cli_foreman_salt
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem

%if 0%{?rhel} == 6
Requires: ruby(abi)
%else
Requires: ruby(release)
%endif

Requires: ruby(rubygems)
Requires: rubygem(hammer_cli_foreman) >= 0.1.2
BuildRequires: ruby(rubygems)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
This Hammer CLI plugin contains set of commands for foreman_salt, a plugin
that provides Salt integration in Foreman.

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
%gem_install -n %{SOURCE0}

%install
mkdir -p %{buildroot}%{_sysconfdir}/%{confdir}/cli.modules.d
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* %{buildroot}%{gem_dir}/
cp -pa .%{gem_instdir}/config/foreman_salt.yml %{buildroot}%{_sysconfdir}/%{confdir}/cli.modules.d/foreman_salt.yml


%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%{gem_instdir}/config
%config(noreplace) %{_sysconfdir}/%{confdir}/cli.modules.d/foreman_salt.yml
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Tue Mar 03 2015 Stephen Benjamin <stephen@redhat.com> 0.0.3-1
- Release 0.0.3

* Thu Jan 15 2015 Stephen Benjamin <stephen@redhat.com> 0.0.1-1
- Initial release
