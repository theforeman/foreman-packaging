# Generated from foreman_ansible_core-3.0.0.gem by gem2rpm -*- rpm-spec -*-
# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_ansible_core

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 4.0.0
Release: 2%{?foremandist}%{?dist}
Summary: Ansible integration with Foreman (theforeman.org): core bits
Group: Development/Languages
License: GPLv3
URL: https://github.com/theforeman/foreman_ansible
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(foreman_remote_execution_core) >= 1.1
Requires: %{?scl_prefix}rubygem(foreman_remote_execution_core) < 2
Requires: %{?scl_prefix}rubygem(foreman-tasks-core) >= 0.3.2
Requires: %{?scl_prefix}rubygem(foreman-tasks-core) < 0.4
Requires: %{?scl_prefix}rubygem(net-ssh)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

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

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}


%changelog
* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 4.0.0-2
- Rebuild plugins for Ruby 2.7

* Thu Dec 10 2020 Ondrej Prazak <oprazak@redhat.com> 4.0.0-1
- Update to 4.0.0

* Tue Sep 22 2020 Marek Hulan <mhulan@redhat.com> 3.0.4-1
- Update to 3.0.4

* Thu Mar 12 2020 Adam Ruzicka <aruzicka@redhat.com> 3.0.3-1
- Update to 3.0.3

* Tue Nov 26 2019 Ondrej Prazak <oprazak@redhat.com> 3.0.2-1
- Update to 3.0.2

* Fri Sep 06 2019 Adam Ruzicka <aruzicka@redhat.com> 3.0.1-1
- Update to 3.0.1

* Thu Apr 18 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 3.0.0-1
- Update to 3.0.0-1

* Fri Jan 25 2019 Marek Hulan <mhulan@redhat.com> 2.2.1-1
- Update to 2.2.1

* Thu Nov 22 2018 Marek Hulan <mhulan@redhat.com> 2.2.0-1
- Update to 2.2.0

* Mon Sep 10 2018 Eric D. Helms <ericdhelms@gmail.com> - 2.1.2-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Wed Aug 15 2018 Sebastian Gräßl <mail@bastilian.me> 2.1.2-1
- Update to 2.1.2

* Thu Jul 19 2018 Marek Hulan <mhulan@redhat.com> 2.1.1-1
- Update to 2.1.1

* Fri Jun 15 2018 Daniel Lobato Garcia <me@daniellobato.me> 2.1.0-1
- Update to 2.1.0

* Fri Feb 02 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 2.0.2-1
- Bump foreman_ansible_core to 2.0.2 (me@daniellobato.me)

* Wed Jan 10 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.1.1-2
- Bump Foreman plugins release (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

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
