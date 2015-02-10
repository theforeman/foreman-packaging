%global gem_name hammer_cli_foreman_discovery
%global confdir hammer

Summary: Foreman discovery commands for Hammer CLI
Name: rubygem-%{gem_name}
Version: 0.0.1
Release: 1%{?dist}
Group: Applications/System
License: GPLv3
URL: https://github.com/theforeman/hammer-cli-foreman-discovery
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: foreman_discovery.yml

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
This Hammer CLI plugin contains set of commands for foreman_discovery, a plugin
to Foreman for bare-metal hardware discovery.

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
install -m 755 %{SOURCE1} %{buildroot}%{_sysconfdir}/%{confdir}/cli.modules.d/foreman_discovery.yml
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%{gem_instdir}/locale
%config(noreplace) %{_sysconfdir}/%{confdir}/cli.modules.d/foreman_discovery.yml
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Tue Feb 10 2015 Lukas Zapletal <lzap+rpm@redhat.com>
- new package built with tito

