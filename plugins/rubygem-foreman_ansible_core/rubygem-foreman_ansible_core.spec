%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_ansible_core

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.1.1
Release: 1%{?foremandist}%{?dist}
Summary: Ansible integration with Foreman (theforeman.org): core bits
Group: Development/Languages
License: GPLv3
URL: https://github.com/theforeman/foreman_ansible
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(foreman-tasks-core) >= 0.1
Requires: %{?scl_prefix}rubygem(foreman-tasks-core) < 1.0
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Ansible integration with Foreman - core parts for dealing with Ansible
concepts, usable by foreman_ansible or smart_proxy_ansible to delegate
the execution.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}.

%prep
%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} - << \EOF}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:EOF}

%build
# Create the gem as gem install only works on a gem file
%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%{?scl:EOF}

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%{?scl:scl enable %{scl} - << \EOF}
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/LICENSE
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}

%changelog
* Thu Mar 30 2017 Dominic Cleal <dominic@cleal.org> 1.1.1-1
- Update foreman_ansible_core to 1.1.1 (me@daniellobato.me)

* Mon Feb 13 2017 Dominic Cleal <dominic@cleal.org> 1.1.0-1
- Update foreman_ansible_core to 1.1.0 (me@daniellobato.me)

* Fri Jan 20 2017 Dominic Cleal <dominic@cleal.org> 1.0.0-1
- Release foreman_ansible_core 1.0.0 (me@daniellobato.me)

* Mon Oct 03 2016 Dominic Cleal <dominic@cleal.org> 0.0.1-2
- Add foremandist to release field (dominic@cleal.org)

* Fri Sep 23 2016 Dominic Cleal <dominic@cleal.org> 0.0.1-1
- new package built with tito

