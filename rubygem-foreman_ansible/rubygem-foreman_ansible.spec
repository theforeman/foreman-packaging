%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_ansible

Summary: Ansible integration with Foreman (theforeman.org)
Name:    %{?scl_prefix}rubygem-%{gem_name}
Version: 1.0
Release: 1%{?foremandist}%{?dist}
Group:   Applications/System
License: GPLv3
URL:     https://github.com/theforeman/foreman_ansible
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: foreman >= 1.12.0

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}rubygems
Requires: %{?scl_prefix}rubygem(deface) < 2.0
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems
BuildRequires: %{?scl_prefix}rubygem(deface) < 2.0
BuildRequires: foreman-plugin >= 1.12.0

BuildArch: noarch

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-ansible
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Ansible integration with Foreman.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%{?scl:scl enable %{scl} - << \EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

%{foreman_bundlerd_file}

%posttrans
%{foreman_db_migrate}
%{foreman_db_seed}
%{foreman_restart}
exit 0

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/LICENSE
%{gem_instdir}/app
%{gem_instdir}/config
%{gem_instdir}/db
%{gem_libdir}
%{gem_instdir}/locale
%exclude %{gem_cache}
%{gem_spec}
%{foreman_bundlerd_dir}/%{gem_name}.rb
%exclude %{gem_instdir}/test

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile

%changelog
* Thu Feb 11 2016 Dominic Cleal <dcleal@redhat.com> 0.3-1
- plugins:foreman_ansible - Release 0.3 (elobatocs@gmail.com)

* Mon Feb 08 2016 Dominic Cleal <dcleal@redhat.com> 0.2.2-2
- Obsolete ruby193 variant from 1.8/1.9 (dcleal@redhat.com)

* Mon Feb 08 2016 Dominic Cleal <dcleal@redhat.com> 0.2.2-1
- Release 0.2.2 (elobatocs@gmail.com)

* Sat Jan 02 2016 Daniel Lobato <elobatocs@gmail.com> 0.2.1-1
- Initial package
