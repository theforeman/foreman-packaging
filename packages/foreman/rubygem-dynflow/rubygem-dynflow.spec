# Generated from dynflow-1.3.0.gem by gem2rpm -*- rpm-spec -*-
# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name dynflow

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.4.7
Release: 2%{?foremandist}%{?dist}
Summary: DYNamic workFLOW engine
Group: Development/Languages
License: MIT
URL: https://github.com/Dynflow/dynflow
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby >= 2.3.0
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(multi_json)
Requires: %{?scl_prefix}rubygem(apipie-params)
Requires: %{?scl_prefix}rubygem(algebrick) >= 0.7.0
Requires: %{?scl_prefix}rubygem(algebrick) < 0.8
Requires: %{?scl_prefix}rubygem(concurrent-ruby) >= 1.1.3
Requires: %{?scl_prefix}rubygem(concurrent-ruby) < 1.2
Requires: %{?scl_prefix}rubygem(concurrent-ruby-edge) >= 0.6.0
Requires: %{?scl_prefix}rubygem(concurrent-ruby-edge) < 0.7
Requires: %{?scl_prefix}rubygem(sequel) >= 4.0.0
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby >= 2.3.0
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

# Optional dependency that we always pull in
Requires: %{?scl_prefix}rubygem(statsd-instrument)

%description
Ruby workflow/orchestration engine.


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
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.rubocop.yml
%exclude %{gem_instdir}/.rubocop_todo.yml
%exclude %{gem_instdir}/.travis.yml
%exclude %{gem_instdir}/Dockerfile
%exclude %{gem_instdir}/docker-compose.yml
%license %{gem_instdir}/MIT-LICENSE
%{gem_instdir}/extras
%{gem_libdir}
%{gem_instdir}/web
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/doc
%{gem_instdir}/dynflow.gemspec
%{gem_instdir}/examples
%{gem_instdir}/test

%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.4.7-2
- Rebuild against rh-ruby27

* Sat Aug 29 2020 Adam Ruzicka <aruzicka@redhat.com> 1.4.7-1
- Update to 1.4.7

* Tue Jun 23 2020 Adam Ruzicka <aruzicka@redhat.com> 1.4.6-1
- Update to 1.4.6

* Wed Jun 17 2020 Adam Ruzicka <aruzicka@redhat.com> 1.4.5-1
- Update to 1.4.5

* Wed May 06 2020 Adam Ruzicka <aruzicka@redhat.com> 1.4.4-1
- Update to 1.4.4

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.4.3-2
- Bump to release for EL8

* Wed Mar 04 2020 Adam Ruzicka <aruzicka@redhat.com> 1.4.3-1
- Update to 1.4.3

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.4.2-2
- Update spec to remove the ror scl

* Tue Dec 17 2019 Adam Ruzicka <aruzicka@redhat.com> 1.4.2-1
- Update to 1.4.2

* Mon Nov 04 2019 Patrick Creech <pcreech@redhat.com> - 1.4.1-2
- Remove sidekiq

* Fri Oct 25 2019 Adam Ruzicka <aruzicka@redhat.com> 1.4.1-1
- Update to 1.4.1

* Tue Oct 22 2019 Adam Ruzicka <aruzicka@redhat.com> 1.4.0-1
- Update to 1.4.0

* Wed Aug 21 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.3.0-1
- Update to 1.3.0-1

* Fri May 03 2019 Ivan Nečas <inecas@redhat.com> 1.2.3-1
- Update to 1.2.3

* Wed Feb 27 2019 Ivan Nečas <inecas@redhat.com> 1.2.2-1
- Update to 1.2.2

* Thu Jan 24 2019 Ivan Nečas <inecas@redhat.com> 1.2.1-1
- Update to 1.2.1

* Fri Jan 04 2019 Ivan Nečas <inecas@redhat.com> 1.2.0-1
- Update to 1.2.0

* Thu Dec 13 2018 Ivan Nečas <inecas@redhat.com> 1.1.6-1
- Update to 1.1.6

* Tue Dec 11 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.1.5-1
- Release rubygem-dynflow 1.1.5

* Mon Dec 03 2018 Ivan Nečas <inecas@redhat.com> 1.1.4-1
- Update to 1.1.4

* Thu Nov 15 2018 Evgeni Golov - 1.1.2-1
- Release rubygem-dynflow 1.1.2

* Fri Oct 05 2018 Ivan Nečas <inecas@redhat.com> 1.1.1-1
- Update to 1.1.1

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.1.0-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Mon Jul 09 2018 Adam Ruzicka <aruzicka@redhat.com> 1.1.0-1
- Update to 1.1.0

* Wed Jun 13 2018 Adam Ruzicka <aruzicka@redhat.com> 1.0.5-1
- Update to 1.0.5

* Mon Jun 11 2018 Adam Ruzicka <aruzicka@redhat.com> 1.0.4-1
- Update to 1.0.4

* Wed May 16 2018 Ivan Nečas <inecas@redhat.com> 1.0.3-1
- Update to 1.0.3

* Thu Mar 29 2018 Adam Ruzicka <aruzicka@redhat.com> 1.0.0-1
- Update to 1.0.0

* Tue Mar 06 2018 Adam Ruzicka <aruzicka@redhat.com> 0.8.36-1
- Update Dynflow to 0.8.36 (aruzicka@redhat.com)

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.8.34-2
- Rebuild packages for Rails 5.1 (ericdhelms@gmail.com)

* Thu Jan 04 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.8.34-1
- Update Dynflow to 0.8.34 (inecas@redhat.com)

* Mon Nov 13 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.8.32-1
- Update dynflow to 0.8.32 (aruzicka@redhat.com)

* Mon Oct 16 2017 Eric D. Helms <ericdhelms@gmail.com> 0.8.31-1
- Update dynflow to 0.8.31 (aruzicka@redhat.com)

* Tue Sep 26 2017 Daniel Lobato Garcia <me@daniellobato.me> 0.8.30-1
- Update Dynflow to 0.8.30 (inecas@redhat.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Mon Aug 07 2017 Eric D. Helms <ericdhelms@gmail.com> 0.8.26-1
- Update rubygem-dynflow to 0.8.26 (me@daniellobato.me)

* Thu May 04 2017 Dominic Cleal <dominic@cleal.org> 0.8.24-1
- upgrade dynflow to 0.8.24 (jsherril@redhat.com)

* Tue Mar 28 2017 Dominic Cleal <dominic@cleal.org> 0.8.23-1
- Update dynflow to 0.8.23 (aruzicka@redhat.com)

* Tue Mar 21 2017 Dominic Cleal <dominic@cleal.org> 0.8.21-1
- Update dynflow to 0.8.21 (me@daniellobato.me)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Wed Nov 23 2016 Dominic Cleal <dominic@cleal.org> 0.8.17-1
- Bump version to 0.8.17 (inecas@redhat.com)

* Tue Sep 13 2016 Dominic Cleal <dominic@cleal.org> 0.8.15-1
- Update dynflow to 0.8.15 (inecas@redhat.com)

* Tue Aug 16 2016 Dominic Cleal <dominic@cleal.org> 0.8.13-1
- Update dynflow to 0.8.13 (daviddavis@redhat.com)

* Tue Jun 21 2016 Dominic Cleal <dominic@cleal.org> 0.8.11-1
- Update dynflow to 0.8.11 (RPM) (inecas@redhat.com)

* Thu Apr 21 2016 Dominic Cleal <dominic@cleal.org> 0.8.10-2
- Rebuild tfm against sclo-ror42 (dominic@cleal.org)

* Tue Feb 16 2016 Dominic Cleal <dcleal@redhat.com> 0.8.10-1
- Update dynflow to 0.8.10 (stbenjam@redhat.com)

* Thu Dec 24 2015 Dominic Cleal <dcleal@redhat.com> 0.8.9-1
- Update dynflow to 0.8.9 (stbenjam@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)
- Add foremandist to more plugins (dcleal@redhat.com)

* Mon Oct 12 2015 Dominic Cleal <dcleal@redhat.com> 0.8.7-1
- Update dynflow to 0.8.7 (inecas@redhat.com)

* Tue Oct 06 2015 Dominic Cleal <dcleal@redhat.com> 0.8.6-1
- Release dynflow 0.8.6 (stbenjam@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 0.8.5-3
- Fix checks against scl name, optimise rhel/empty SCL conditional
  (dcleal@redhat.com)
- Converted to tfm SCL (dcleal@redhat.com)

* Thu Aug 20 2015 Dominic Cleal <dcleal@redhat.com> 0.8.5-2
- Package dynflow for non-SCL on el7 (stbenjam@redhat.com)

* Mon Aug 17 2015 Dominic Cleal <dcleal@redhat.com> 0.8.5-1
- Release dynflow 0.8.5 (stbenjam@redhat.com)

* Mon Aug 03 2015 Ivan Nečas <inecas@redhat.com> 0.8.2-1
- Update dynflow to 0.8.2 (inecas@redhat.com)
- Automatic commit of package [rubygem-dynflow] minor release [0.8.1-1].
  (dcleal@redhat.com)
- Update dynflow to 0.8.1 (inecas@redhat.com)

* Thu Jul 02 2015 Dominic Cleal <dcleal@redhat.com> 0.8.1-1
- Update dynflow to 0.8.1 (inecas@redhat.com)

* Fri Jun 19 2015 Ivan Nečas <inecas@redhat.com> 0.7.9-1
- Update dynflow to 0.7.9 (inecas@redhat.com)

* Mon May 18 2015 Dominic Cleal <dcleal@redhat.com> 0.7.8-1
- Update dynflow to 0.7.8 (inecas@redhat.com)

* Tue Mar 17 2015 Dominic Cleal <dcleal@redhat.com> 0.7.7-1
- Update dynflow to 0.7.7 (inecas@redhat.com)

* Wed Jan 28 2015 Dominic Cleal <dcleal@redhat.com> 0.7.6-1
- Update to dynflow 0.7.6 (inecas@redhat.com)

* Fri Dec 05 2014 Dominic Cleal <dcleal@redhat.com> 0.7.5-1
- Update to dynflow 0.7.5 (brad@redhat.com)

* Tue Aug 12 2014 Ivan Nečas <inecas@redhat.com> 0.7.3-1
- Bump version (inecas@redhat.com)

* Mon Jul 14 2014 Ivan Nečas <inecas@redhat.com> 0.7.2-1
- Bump version (inecas@redhat.com)

* Fri Jun 13 2014 Ivan Nečas <inecas@redhat.com> 0.7.1-1
- Bump version (inecas@redhat.com)

* Tue Jun 10 2014 Ivan Nečas <inecas@redhat.com> 0.7.0-1
- Bump version (inecas@redhat.com)

* Mon Apr 07 2014 Ivan Nečas <inecas@redhat.com> 0.6.1-1
- Bump version (inecas@redhat.com)

* Tue Mar 25 2014 Ivan Nečas <inecas@redhat.com> 0.6.0-1
- Bump version (inecas@redhat.com)

* Tue Mar 18 2014 Ivan Nečas <inecas@redhat.com> 0.5.1-1
- Bump version (inecas@redhat.com)

* Tue Feb 25 2014 Ivan Nečas <inecas@redhat.com> 0.5.0-1
- Bump to version 0.5.0 (inecas@redhat.com)

* Wed Aug 28 2013 Partha Aji <paji@redhat.com> 0.1.0-2
- F19 Changes - made ruby abi conditional (paji@redhat.com)

* Tue May 07 2013 Ivan Necas <inecas@redhat.com> 0.1.0-1
- new package built with tito
