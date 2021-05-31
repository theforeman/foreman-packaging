# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_remote_execution_core

Summary: Foreman remote execution - core bits
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.4.3
Release: 1%{?dist}
Group: Development/Languages
License: GPLv3
URL: https://github.com/theforeman/foreman_remote_execution
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(bcrypt_pbkdf)
Requires: %{?scl_prefix}rubygem(ed25519)
Requires: %{?scl_prefix}rubygem(foreman-tasks-core) >= 0.3.1
Requires: %{?scl_prefix}rubygem(net-ssh)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

%description
Ssh remote execution provider code sharable between Foreman and
Foreman-Proxy.


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
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}


%changelog
* Mon May 31 2021 Adam Ruzicka <aruzicka@redhat.com> 1.4.3-1
- Update to 1.4.3

* Wed Apr 07 2021 Adam Ruzicka <aruzicka@redhat.com> 1.4.2-1
- Update to 1.4.2

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.4.1-2
- Rebuild plugins for Ruby 2.7

* Fri Mar 26 2021 Adam Ruzicka <aruzicka@redhat.com> 1.4.1-1
- Update to 1.4.1

* Mon Nov 09 2020 Adam Ruzicka <aruzicka@redhat.com> 1.4.0-1
- Update to 1.4.0

* Tue Jul 14 2020 Adam Ruzicka <aruzicka@redhat.com> 1.3.1-1
- Update to 1.3.1

* Fri Oct 04 2019 Adam Ruzicka <aruzicka@redhat.com> 1.3.0-1
- Update to 1.3.0

* Tue May 21 2019 Ivan Nečas <inecas@redhat.com> 1.2.0-1
- Update to 1.2.0

* Mon Jan 14 2019 Ivan Nečas <inecas@redhat.com> 1.1.5-1
- Update to 1.1.5

* Tue Oct 09 2018 Ivan Nečas <inecas@redhat.com> 1.1.4-1
- Update to 1.1.4

* Mon Sep 10 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.1.3-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Thu Jun 14 2018 Ivan Nečas <inecas@redhat.com> 1.1.3-1
- Update to 1.1.3

* Mon May 28 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.1.2-2
- Regenerate spec file based on the current template

* Wed May 16 2018 Ivan Nečas <inecas@redhat.com> 1.1.2-1
- Update to 1.1.2

* Wed Mar 14 2018 Adam Ruzicka <aruzicka@redhat.com> 1.1.1-1
- Update foreman_remote_execution_core to 1.1.1 (aruzicka@redhat.com.com)

* Fri Feb 02 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.1.0-1
- Update rubygem-foreman_remote_execution to 1.4.2 (aruzicka@redhat.com)

* Wed Jan 10 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.0.5-2
- Bump Foreman plugins release (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
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
