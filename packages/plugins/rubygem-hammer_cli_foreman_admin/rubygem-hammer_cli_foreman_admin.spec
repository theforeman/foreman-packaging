%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%{!?_root_sysconfdir:%global _root_sysconfdir %{_sysconfdir}}

%global gem_name hammer_cli_foreman_admin
%global confdir hammer

Summary: Foreman admin commands for Hammer CLI
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.0.8
Release: 1%{?dist}
Group: Applications/System
License: GPLv3
URL: https://github.com/theforeman/hammer-cli-foreman-admin
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(hammer_cli_foreman) >= 0.1.2
BuildRequires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
This Hammer CLI plugin contains set of administrative Foreman server commands.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%install
install -m 755 -d %{buildroot}%{_root_sysconfdir}/%{confdir}/cli.modules.d
install -m 644 .%{gem_instdir}/config/foreman_admin.yml \
  .%{gem_instdir}/config/cli.modules.d/foreman_admin_*.yml \
  %{buildroot}%{_root_sysconfdir}/%{confdir}/cli.modules.d/

install -m 755 -d %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%{gem_instdir}/locale
%config(noreplace) %{_root_sysconfdir}/%{confdir}/cli.modules.d/foreman_admin.yml
%config %{_root_sysconfdir}/%{confdir}/cli.modules.d/foreman_admin_logging_core.yml
%config %{_root_sysconfdir}/%{confdir}/cli.modules.d/foreman_admin_logging_katello.yml
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/LICENSE

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/config
%doc %{gem_instdir}/README.md

%changelog
* Tue Jan 30 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.0.8-1
- Updated hammer_cli_foreman_admin to 0.0.8 (lzap+git@redhat.com)

* Tue Jan 09 2018 Eric D. Helms <ericdhelms@gmail.com> 0.0.7-2
- Bump releases for base foreman plugins packages (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Thu Sep 21 2017 Eric D. Helms <ericdhelms@gmail.com> 0.0.7-1
- Updated rubygem-hammer_cli_foreman_admin to 0.0.7 (lzap+git@redhat.com)

* Mon Dec 12 2016 Dominic Cleal <dominic@cleal.org> 0.0.6-1
- Update hammer_cli_foreman_admin to 0.0.6 (lzap+git@redhat.com)

* Wed Aug 10 2016 Dominic Cleal <dominic@cleal.org> 0.0.5-1
- Update hammer_cli_foreman_admin to 0.0.5 (lzap+git@redhat.com)

* Fri Jun 10 2016 Dominic Cleal <dominic@cleal.org> 0.0.4-1
- new package built with tito

