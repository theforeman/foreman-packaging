%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_remote_execution_core

Summary: Foreman remote execution - core bits
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.1.0
Release: 1%{?foremandist}%{?dist}
Group: Development/Libraries
License: GPLv3
URL: https://github.com/theforeman/foreman_remote_execution
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix}rubygem(net-scp)
Requires: %{?scl_prefix}rubygem(net-ssh)
Requires: %{?scl_prefix}rubygem(foreman-tasks-core) >= 0.1.5

BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems
BuildRequires: %{?scl_prefix_ruby}rubygems-devel

BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Ssh remote execution provider code sharable between Foreman and Foreman-Proxy

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%exclude %{gem_cache}
%exclude %{gem_instdir}/.*
%doc %{gem_instdir}/LICENSE
%{gem_libdir}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/LICENSE

%changelog
* Mon Mar 12 2018 Daniel Lobato Garcia <me@daniellobato.me> 1.1.0-1
- Update rubygem-foreman_remote_execution_core to 1.1.0
  (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Mon Jul 17 2017 Eric D. Helms <ericdhelms@gmail.com> 1.0.5-1
- Update foreman_remote_execution_core to 1.0.5 (inecas@redhat.com)

* Wed May 31 2017 Dominic Cleal <dominic@cleal.org> 1.0.4-1
- Update foreman_remote_execution_core to 1.0.4 (inecas@redhat.com)

* Tue Apr 11 2017 Dominic Cleal <dominic@cleal.org> 1.0.3-1
- Update foreman_remote_execution_core to 1.0.3 (aruzicka@redhat.com)

* Fri Jan 27 2017 Dominic Cleal <dominic@cleal.org> 1.0.2-1
- Update foreman_remote_execution_core to 1.0.2 (inecas@redhat.com)

* Mon Sep 19 2016 Dominic Cleal <dominic@cleal.org> 1.0.1-1
- new package built with tito

