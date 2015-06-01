%global gem_name hammer_cli_foreman_bootdisk
%global confdir hammer

Summary: Foreman boot disk commands for Hammer CLI
Name: rubygem-%{gem_name}
Version: 0.1.3
Release: 1%{?dist}
Group: Applications/System
License: GPLv3
URL: http://github.com/theforeman/hammer_cli_foreman_bootdisk
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
This Hammer CLI plugin contains set of commands for foreman_bootdisk, a plugin
to Foreman for ISO/USB booting support.

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
install -m 755 .%{gem_instdir}/config/foreman_bootdisk.yml \
               %{buildroot}%{_sysconfdir}/%{confdir}/cli.modules.d/foreman_bootdisk.yml
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%{gem_instdir}/locale
%doc %{gem_instdir}/LICENSE
%config(noreplace) %{_sysconfdir}/%{confdir}/cli.modules.d/foreman_bootdisk.yml
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/config
%doc %{gem_instdir}/README.md

%changelog
* Mon Jun 01 2015 Dominic Cleal <dcleal@redhat.com> 0.1.3-1
- Update hammer_cli_foreman_bootdisk to 0.1.3 (dcleal@redhat.com)

* Wed Nov 05 2014 Dominic Cleal <dcleal@redhat.com> 0.1.2-1
- new package built with tito

