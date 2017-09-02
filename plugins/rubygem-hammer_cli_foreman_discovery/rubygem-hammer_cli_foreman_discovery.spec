%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%{!?_root_sysconfdir:%global _root_sysconfdir %{_sysconfdir}}

%global gem_name hammer_cli_foreman_discovery
%global confdir hammer

Summary: Foreman discovery commands for Hammer CLI
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.0.0
Release: 1%{?dist}
Group: Applications/System
License: GPLv3
URL: https://github.com/theforeman/hammer-cli-foreman-discovery
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem

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
Obsoletes: rubygem-%{gem_name} < 0.0.2-2
%endif

%description
This Hammer CLI plugin contains set of commands for foreman_discovery, a plugin
to Foreman for bare-metal hardware discovery.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
BuildArch: noarch
%if 0%{?scl:1}
Obsoletes: rubygem-%{gem_name}-doc < 0.0.2-2
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
install -m 755 .%{gem_instdir}/config/foreman_discovery.yml \
               %{buildroot}%{_root_sysconfdir}/%{confdir}/cli.modules.d/foreman_discovery.yml

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%{gem_instdir}/locale
%config(noreplace) %{_root_sysconfdir}/%{confdir}/cli.modules.d/foreman_discovery.yml
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/LICENSE

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/config
%doc %{gem_instdir}/README.md

%changelog
* Mon Jun 19 2017 Eric D. Helms <ericdhelms@gmail.com> 1.0.0-1
- Updated hammer_cli_foreman_discovery-1.0.0 (lzap+git@redhat.com)

* Wed May 04 2016 Dominic Cleal <dominic@cleal.org> 0.0.3-2
- Use gem_install macro (dominic@cleal.org)

* Thu Apr 14 2016 Dominic Cleal <dominic@cleal.org> 0.0.3-1
- Update hammer_cli_foreman_discovery to 0.0.3 (orabin@redhat.com)

* Thu Dec 24 2015 Dominic Cleal <dcleal@redhat.com> 0.0.2-4
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 0.0.2-3
- Converted to tfm SCL (dcleal@redhat.com)

* Tue Jul 28 2015 Dominic Cleal <dcleal@redhat.com> 0.0.2-2
- fixes #8979 - convert hammer packages to SCL (dcleal@redhat.com)

* Thu Mar 19 2015 Dominic Cleal <dcleal@redhat.com> 0.0.2-1
- Update hammer_cli_foreman_discovery to 0.0.2 (dcleal@redhat.com)

* Tue Feb 10 2015 Lukas Zapletal <lzap+rpm@redhat.com>
- new package built with tito
