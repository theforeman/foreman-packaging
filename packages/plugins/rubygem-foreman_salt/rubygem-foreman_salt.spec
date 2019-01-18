# template: foreman_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_salt
%global plugin_name salt
%global foreman_min_version 1.17.0

Summary:    Foreman Plug-in for Salt
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    10.1.0
Release:    2%{?foremandist}%{?dist}
Group:      Applications/Systems
License:    GPLv3
URL:        https://github.com/theforeman/foreman_salt
Source0:    https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: foreman >= %{foreman_min_version}
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(deface) < 2.0
Requires: %{?scl_prefix}rubygem(foreman-tasks) >= 0.8
Requires: %{?scl_prefix}rubygem(foreman-tasks) < 1
BuildRequires: foreman-assets >= %{foreman_min_version}
BuildRequires: foreman-plugin >= %{foreman_min_version}
BuildRequires: %{?scl_prefix}rubygem(deface) < 2.0
BuildRequires: %{?scl_prefix}rubygem(foreman-tasks) >= 0.8
BuildRequires: %{?scl_prefix}rubygem(foreman-tasks) < 1
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-%{plugin_name}
# end specfile generated dependencies
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Foreman Plug-in for Salt.


%package doc
BuildArch:  noarch
Group:      Documentation
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
Summary:    Documentation for %{pkg_name}

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

%foreman_bundlerd_file
%foreman_precompile_plugin -a -s

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_instdir}/app
%{gem_instdir}/config
%{gem_instdir}/db
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%{foreman_bundlerd_plugin}
%{foreman_apipie_cache_foreman}
%{foreman_apipie_cache_plugin}
%{foreman_assets_plugin}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%posttrans
%{foreman_db_migrate}
%{foreman_db_seed}
%{foreman_apipie_cache}
%{foreman_restart}
exit 0

%changelog
* Mon Sep 10 2018 Eric D. Helms <ericdhelms@gmail.com> - 10.1.0-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jul 20 2018 Greg Sutcliffe <greg.sutcliffe@gmail.com> 10.1.0-1
- Update to 10.1.0

* Mon May 28 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 10.0.0-2
- Regenerate spec file based on the current template

* Tue May 08 2018 Michael Moll <kvedulv@kvedulv.de> 10.0.0-1
- update foreman_salt to 10.0.0 (kvedulv@kvedulv.de)

* Wed Dec 13 2017 Daniel Lobato Garcia <me@daniellobato.me> 9.0.0-1
- update foreman_salt to 9.0.0 (kvedulv@kvedulv.de)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Thu Mar 30 2017 Dominic Cleal <dominic@cleal.org> 8.0.2-1
- update foreman_salt to 8.0.2 (kvedulv@kvedulv.de)

* Mon Mar 13 2017 Eric D Helms <ericdhelms@gmail.com> 8.0.1-1
- update foreman_salt to 8.0.1 (kvedulv@kvedulv.de)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Wed Nov 23 2016 Dominic Cleal <dominic@cleal.org> 8.0.0-1
- update foreman_salt to 8.0.0 (kvedulv@kvedulv.de)

* Tue Nov 22 2016 Dominic Cleal <dominic@cleal.org> 7.0.1-1
- update foreman_salt to 7.0.1 (kvedulv@kvedulv.de)

* Mon Aug 22 2016 Dominic Cleal <dominic@cleal.org> 7.0.0-1
- Release foreman_salt 7.0.0 (stephen@redhat.com)

* Thu Jul 28 2016 Dominic Cleal <dominic@cleal.org> 6.0.0-1
- Release foreman_salt 6.0.0 (stephen@redhat.com)

* Tue May 31 2016 Dominic Cleal <dominic@cleal.org> 5.0.1-1
- update foreman_salt to 5.0.1 (kvedulv@kvedulv.de)

* Wed Jan 27 2016 Dominic Cleal <dcleal@redhat.com> 5.0.0-1
- Release foreman_salt 5.0.0 (stbenjam@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Mon Oct 26 2015 Dominic Cleal <dcleal@redhat.com> 4.0.1-1
- Small foreman_salt update (stbenjam@redhat.com)

* Tue Oct 13 2015 Dominic Cleal <dcleal@redhat.com> 4.0.0-1
- Release foreman_salt 4.0.0 (RPM) (stbenjam@redhat.com)

* Thu Aug 27 2015 Dominic Cleal <dcleal@redhat.com> 3.0.2-1
- Release foreman_salt 3.0.2 (stbenjam@redhat.com)

* Thu Aug 27 2015 Dominic Cleal <dcleal@redhat.com> 3.0.1-2
- Converted to tfm SCL (dcleal@redhat.com)

* Thu Aug 13 2015 Stephen Benjamin <stephen@redhat.com> 3.0.1-1
- Update to 3.0.1

* Mon Jul 06 2015 Stephen Benjamin <stephen@redhat.com> 3.0.0-1
- Update to 3.0.0

* Sat May 09 2015 Stephen Benjamin <stephen@redhat.com> 2.1.0-1
- Update to 2.1.0

* Tue Mar 17 2015 Stephen Benjamin <stephen@redhat.com> 2.0.2-1
- Update to 2.0.2

* Tue Mar 03 2015 Stephen Benjamin <stephen@redhat.com> 2.0.1-1
- Update to 2.0.1

* Wed Jan 14 2015 Stephen Benjamin <stephen@redhat.com> 1.1.1-1
- Update to 1.1.1

* Tue Dec 30 2014 Michael Moll <mmoll@mmoll.at> 1.1.0-2
- Add dependency on rubygem-deface

* Wed Nov 19 2014 Stephen Benjamin <stephen@redhat.com> 1.1.0-1
- Update to 1.1.0

* Tue Nov 11 2014 Stephen Benjamin <stephen@redhat.com> 1.0.0-1
- Update to 1.0.0

* Wed Oct 08 2014 Stephen Benjamin <stephen@redhat.com> 0.0.4-1
- Update to 0.0.4

* Tue Oct 07 2014 Michael Moll <mmoll@mmoll.at> 0.0.3-1
- Update to 0.0.3

* Thu Aug 28 2014 Stephen Benjamin <stephen@redhat.com> 0.0.2-1
- Initial version
