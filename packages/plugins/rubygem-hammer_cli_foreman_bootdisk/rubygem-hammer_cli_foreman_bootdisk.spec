%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%{!?_root_sysconfdir:%global _root_sysconfdir %{_sysconfdir}}

%global gem_name hammer_cli_foreman_bootdisk
%global confdir hammer

Summary: Foreman boot disk commands for Hammer CLI
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.1.3
Release: 7%{?dist}
Group: Applications/System
License: GPLv3
URL: https://github.com/theforeman/hammer_cli_foreman_bootdisk
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(hammer_cli_foreman) >= 0.1.2
BuildRequires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}
%if 0%{?scl:1}
Obsoletes: rubygem-%{gem_name} < 0.1.3-2
%endif

%description
This Hammer CLI plugin contains set of commands for foreman_bootdisk, a plugin
to Foreman for ISO/USB booting support.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
BuildArch: noarch
%if 0%{?scl:1}
Obsoletes: rubygem-%{gem_name}-doc < 0.1.3-2
%endif

%description doc
Documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{_root_sysconfdir}/%{confdir}/cli.modules.d
install -m 755 .%{gem_instdir}/config/foreman_bootdisk.yml \
               %{buildroot}%{_root_sysconfdir}/%{confdir}/cli.modules.d/foreman_bootdisk.yml
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%{gem_instdir}/locale
%doc %{gem_instdir}/LICENSE
%config(noreplace) %{_root_sysconfdir}/%{confdir}/cli.modules.d/foreman_bootdisk.yml
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/config
%doc %{gem_instdir}/README.md

%changelog
* Fri Sep 07 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.1.3-7
- Rebuild for Rails 5.2 and Ruby 2.5

* Tue Jan 09 2018 Eric D. Helms <ericdhelms@gmail.com> 0.1.3-6
- Bump releases for base foreman plugins packages (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Wed May 04 2016 Dominic Cleal <dominic@cleal.org> 0.1.3-5
- Use gem_install macro (dominic@cleal.org)

* Thu Dec 24 2015 Dominic Cleal <dcleal@redhat.com> 0.1.3-4
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 0.1.3-3
- Converted to tfm SCL (dcleal@redhat.com)

* Tue Jul 28 2015 Dominic Cleal <dcleal@redhat.com> 0.1.3-2
- fixes #8979 - convert hammer packages to SCL (dcleal@redhat.com)

* Mon Jun 01 2015 Dominic Cleal <dcleal@redhat.com> 0.1.3-1
- Update hammer_cli_foreman_bootdisk to 0.1.3 (dcleal@redhat.com)

* Wed Nov 05 2014 Dominic Cleal <dcleal@redhat.com> 0.1.2-1
- new package built with tito
