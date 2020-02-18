%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%{!?_root_sysconfdir:%global _root_sysconfdir %{_sysconfdir}}

%global gem_name hammer_cli_foreman_openscap
%global confdir hammer

Summary: Foreman OpenSCAP commands for Hammer CLI
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.1.9
Release: 1%{?foremandist}%{?dist}
Group: Applications/System
License: GPLv3
URL: https://github.com/theforeman/hammer_cli_foreman_openscap
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(hammer_cli_foreman) >= 0.6.0
Requires: %{?scl_prefix}rubygem(hammer_cli_foreman) < 3.0.0
BuildRequires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
This Hammer CLI plugin contains set of commands for foreman_openscap

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
mkdir -p %{buildroot}%{_root_sysconfdir}/%{confdir}/cli.modules.d
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* %{buildroot}%{gem_dir}/
cp -pa .%{gem_instdir}/config/foreman_openscap.yml %{buildroot}%{_root_sysconfdir}/%{confdir}/cli.modules.d/foreman_openscap.yml

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/test
%{gem_instdir}/config
%{gem_instdir}/lib
%{gem_instdir}/locale
%config(noreplace) %{_root_sysconfdir}/%{confdir}/cli.modules.d/foreman_openscap.yml
%doc %{gem_instdir}/LICENSE
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Tue Feb 18 2020 Ondrej Prazak <oprazak@redhat.com> 0.1.9-1
- Update to 0.1.9

* Thu May 23 2019 Ondrej Prazak <oprazak@redhat.com> 0.1.8-1
- Update to 0.1.8

* Tue Mar 19 2019 Marek Hulan <mhulan@redhat.com> 0.1.7-1
- Update to 0.1.7

* Fri Sep 07 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.1.6-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Apr 06 2018 Marek Hulan <mhulan@redhat.com> 0.1.6-1
- Update to 0.1.6

* Tue Jan 09 2018 Eric D. Helms <ericdhelms@gmail.com> 0.1.5-2
- Bump releases for base foreman plugins packages (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Thu Sep 14 2017 Eric D. Helms <ericdhelms@gmail.com> 0.1.5-1
- Update hammer_cli_foreman_openscap to 0.1.5 (mhulan@redhat.com)

* Wed Jul 26 2017 Eric D. Helms <ericdhelms@gmail.com> 0.1.4-1
- Update hammer_cli_foreman_openscap to 0.1.4 (mhulan@redhat.com)

* Wed Mar 15 2017 Dominic Cleal <dominic@cleal.org> 0.1.3-1
- Update hammer_cli_foreman_openscap to 0.1.3 (mhulan@redhat.com)

* Wed Oct 19 2016 Dominic Cleal <dominic@cleal.org> 0.1.2-1
- Update hammer_cli_foreman_openscap to 0.1.2 (oprazak@redhat.com)

* Wed Sep 07 2016 Dominic Cleal <dominic@cleal.org> 0.1.1-1
- new package built with tito

