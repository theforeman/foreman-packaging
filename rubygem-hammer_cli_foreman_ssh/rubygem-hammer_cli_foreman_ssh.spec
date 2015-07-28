%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%{!?_root_sysconfdir:%global _root_sysconfdir %{_sysconfdir}}

%global gem_name hammer_cli_foreman_ssh
%global confdir hammer

Summary: Adds remote SSH support to Hammer Foreman CLI
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.0.2
Release: 2%{?dist}
Group: Applications/System
License: GPLv3+
URL: http://github.com/theforeman/hammer-cli-foreman-ssh
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: foreman_ssh.yml

%if 0%{?fedora} > 18
Requires: %{?scl_prefix}ruby(release)
%else
Requires: %{?scl_prefix}ruby(abi)
%endif

Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(hammer_cli) >= 0.0.6
Requires: %{?scl_prefix}rubygem(hammer_cli_foreman)
Requires: %{?scl_prefix}rubygem(net-ssh-multi)
BuildRequires: %{?scl_prefix}ruby(rubygems)
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%if 0%{?scl:1}
Obsoletes: rubygem-%{gem_name} < 0.0.2-2
%endif

%description
Adds remote SSH support to Hammer Foreman CLI.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch
%if 0%{?scl:1}
Obsoletes: rubygem-%{gem_name}-doc < 0.0.2-2
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
install -m 755 %{SOURCE1} %{buildroot}%{_root_sysconfdir}/%{confdir}/cli.modules.d/foreman_ssh.yml
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_libdir}
%config(noreplace) %{_root_sysconfdir}/%{confdir}/cli.modules.d/foreman_ssh.yml
%doc %{gem_instdir}/LICENSE
%{gem_spec}
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Tue Jul 28 2015 Dominic Cleal <dcleal@redhat.com> 0.0.2-2
- fixes #8979 - convert hammer packages to SCL (dcleal@redhat.com)

* Wed Nov 05 2014 Dominic Cleal <dcleal@redhat.com> 0.0.2-1
- new package built with tito
