%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%{!?_root_sysconfdir:%global _root_sysconfdir %{_sysconfdir}}

%global gem_name hammer_cli_foreman_salt
%global confdir hammer

Summary: Foreman Salt-related commands for Hammer CLI
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.0.4
Release: 3%{?dist}
Group: Applications/System
License: GPLv3
URL: http://github.com/theforeman/hammer_cli_foreman_salt
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem

%if 0%{?fedora} > 18
Requires: %{?scl_prefix_ruby}ruby(release)
%else
Requires: %{?scl_prefix_ruby}ruby(abi)
%endif

Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(hammer_cli_foreman) >= 0.1.2
BuildRequires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}
%if 0%{?scl:1}
Obsoletes: rubygem-%{gem_name} < 0.0.4-2
%endif

%description
This Hammer CLI plugin contains set of commands for foreman_salt, a plugin
that provides Salt integration in Foreman.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
BuildArch: noarch
%if 0%{?scl:1}
Obsoletes: rubygem-%{gem_name}-doc < 0.0.4-2
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
mkdir -p %{buildroot}%{_root_sysconfdir}/%{confdir}/cli.modules.d
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* %{buildroot}%{gem_dir}/
cp -pa .%{gem_instdir}/config/foreman_salt.yml %{buildroot}%{_root_sysconfdir}/%{confdir}/cli.modules.d/foreman_salt.yml

%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%{gem_instdir}/config
%config(noreplace) %{_root_sysconfdir}/%{confdir}/cli.modules.d/foreman_salt.yml
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 0.0.4-3
- Converted to tfm SCL (dcleal@redhat.com)

* Tue Jul 28 2015 Dominic Cleal <dcleal@redhat.com> 0.0.4-2
- fixes #8979 - convert hammer packages to SCL (dcleal@redhat.com)

* Wed Mar 04 2015 Dominic Cleal <dcleal@redhat.com> 0.0.4-1
- Update hammer_cli_foreman_salt to 0.0.4 (dcleal@redhat.com)

* Tue Mar 03 2015 Stephen Benjamin <stephen@redhat.com> 0.0.3-1
- Release 0.0.3

* Thu Jan 15 2015 Stephen Benjamin <stephen@redhat.com> 0.0.1-1
- Initial release
