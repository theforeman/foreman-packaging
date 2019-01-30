# template: foreman_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_discovery
%global plugin_name discovery
%global foreman_min_version 1.20.0

%global mainver 14.0.1
%global release 1
%{?prever:
%global gem_instdir %{gem_dir}/gems/%{gem_name}-%{mainver}%{?prever}
%global gem_docdir %{gem_dir}/doc/%{gem_name}-%{mainver}%{?prever}
%global gem_cache %{gem_dir}/cache/%{gem_name}-%{mainver}%{?prever}.gem
%global gem_spec %{gem_dir}/specifications/%{gem_name}-%{mainver}%{?prever}.gemspec
}

Summary:    MaaS Discovery Plugin for Foreman
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    %{mainver}
Release:    %{?prever:0.}%{release}%{?prever}%{?foremandist}%{?dist}
Group:      Applications/Systems
License:    GPLv3
URL:        https://github.com/theforeman/foreman_discovery
Source0:    https://rubygems.org/gems/%{gem_name}-%{version}%{?prever}.gem

# start generated dependencies
Requires: foreman >= %{foreman_min_version}
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: foreman-plugin >= %{foreman_min_version}
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-%{plugin_name}
# end generated dependencies
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
MaaS Discovery Plugin engine for Foreman.


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
%foreman_precompile_plugin -a

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_instdir}/app
%{gem_instdir}/config
%{gem_instdir}/db
%{gem_instdir}/extra
%{gem_libdir}
%{gem_instdir}/locale
%exclude %{gem_cache}
%{gem_spec}
%{foreman_bundlerd_plugin}
%{foreman_apipie_cache_foreman}
%{foreman_apipie_cache_plugin}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/test

%posttrans
%{foreman_db_migrate}
%{foreman_db_seed}
%{foreman_apipie_cache}
%{foreman_restart}
exit 0

%changelog
* Wed Jan 30 2019 Lukas Zapletal <lzap+rpm@redhat.com> 14.0.1-1
- Update to version 14.0.1

* Mon Nov 05 2018 Lukas Zapletal <lzap+rpm@redhat.com> 14.0.0-1
- Update to version 14.0.0

* Fri Sep 07 2018 Eric D. Helms <ericdhelms@gmail.com> - 13.0.1-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Tue Aug 07 2018 Lukas Zapletal <lzap+rpm@redhat.com> 13.0.1-1
- Update to version 13.0.1

* Fri Jul 13 2018 Lukas Zapletal <lzap+rpm@redhat.com> 12.0.2-1
- Update to version 12.0.2 - rule problems solved

* Tue Jun 26 2018 Lukas Zapletal <lzap+rpm@redhat.com> 12.0.1-1
- Update to version 12.0.1

* Fri Jun 22 2018 Lukas Zapletal <lzap+rpm@redhat.com> 12.0.0-1
- Update to version 12.0.0

* Sun May 27 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 11.0.0-2
- Regenerate spec file based on the current template

* Tue Jan 30 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 11.0.0-1
- Updated to foreman_discovery-11.0.0 (lzap+git@redhat.com)

* Fri Oct 27 2017 Daniel Lobato Garcia <me@daniellobato.me> 10.0.0-1
- Update discovery to 10.0.0 (lzap@redhat.com)

* Wed Oct 04 2017 Daniel Lobato Garcia <me@daniellobato.me> 9.1.3-1
- Updated to foreman_discovery-9.1.3.gem (lzap@redhat.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Mon Jun 19 2017 Eric D. Helms <ericdhelms@gmail.com> 9.1.1-1
- Bumped foreman_discovery to 9.1.1 (lzap+git@redhat.com)

* Mon Jun 19 2017 Eric D. Helms <ericdhelms@gmail.com> 9.1.0-1
- Update foreman_discovery to 9.1.0 (RPM) (lzap+git@redhat.com)

* Fri Apr 07 2017 Dominic Cleal <dominic@cleal.org> 9.0.0-1
- Discovery 9.0.0 (lzap+git@redhat.com)

* Mon Mar 27 2017 Dominic Cleal <dominic@cleal.org> 8.0.1-1
- Updated foreman_discovery to 8.0.1 (lzap+git@redhat.com)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Fri Jan 06 2017 Dominic Cleal <dominic@cleal.org> 8.0.0-1
- Discovery 8.0.0 (lzap+git@redhat.com)

* Fri Dec 23 2016 Dominic Cleal <dominic@cleal.org> 7.0.1-1
- Updated foreman_discovery to 7.0.1 (lzap+git@redhat.com)

* Wed Aug 31 2016 Dominic Cleal <dominic@cleal.org> 7.0.0-1
- Updated foreman_discovery to 7.0.0 (lzap+git@redhat.com)

* Fri Mar 11 2016 Dominic Cleal <dominic@cleal.org> 5.0.2-1
- Updated discovery to 5.0.2 (lzap+git@redhat.com)

* Fri Feb 26 2016 Dominic Cleal <dominic@cleal.org> 5.0.1-1
- Updated foreman_discovery to 5.0.1 (lzap+git@redhat.com)

* Tue Jan 26 2016 Dominic Cleal <dcleal@redhat.com> 5.0.0-1
- Update foreman_discovery to 5.0.0 (RPM) (lzap+git@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Mon Oct 26 2015 Dominic Cleal <dcleal@redhat.com> 4.1.2-1
- Updated foreman_discovery to 4.1.2 (lzap+git@redhat.com)

* Tue Oct 20 2015 Dominic Cleal <dcleal@redhat.com> 4.1.1-1
- Updated foreman_discovery to 4.1.1 (RPM) (lzap+git@redhat.com)

* Tue Sep 22 2015 Dominic Cleal <dcleal@redhat.com> 4.1.0-1
- Discovery 4.1.0 (lzap+git@redhat.com)

* Thu Aug 27 2015 Dominic Cleal <dcleal@redhat.com> 4.0.0-2
- Converted to tfm SCL (dcleal@redhat.com)
- Fix BRs to match runtime requirements (dcleal@redhat.com)

* Thu Aug 13 2015 Dominic Cleal <dcleal@redhat.com> 4.0.0-1
- Updated foreman_discovery to 4.0.0 (lzap+git@redhat.com)
- Better branched builds with Foreman version macro (dcleal@redhat.com)

* Tue Mar 10 2015 Dominic Cleal <dcleal@redhat.com> 3.0.0-1
- Version 3.0.0 for Foreman 1.8 (lzap+git@redhat.com)
- Refs #4478 - prebuild apipie cache for rubygem-foreman_discovery
  (martin.bacovsky@gmail.com)

* Mon Feb 09 2015 Dominic Cleal <dcleal@redhat.com> 2.0.0-1
- Version bump to discovery 2.0.0 (lzap+git@redhat.com)

* Sun Feb 01 2015 Dominic Cleal <dcleal@redhat.com> 2.0.0-0.1.rc2
- Update foreman_discovery to 2.0.0.rc2 (lzap+git@redhat.com)

* Tue Jan 20 2015 Lukas Zapletal <lzap+rpm@redhat.com> - 2.0.0-0.1.rc1
- Dropped extra/ directory and TCL building dependencies
- Update to foreman_discovery 2.0.0.rc1

* Tue Nov 25 2014 Lukas Zapletal <lzap+rpm@redhat.com> - 1.4.1-1
- Update to foreman_discovery 1.4.1

* Thu Oct 30 2014 Lukas Zapletal <lzap+git@redhat.com> 1.4.0-2
- Update to foreman_discovery 1.4.0-2

* Thu Oct 30 2014 Lukas Zapletal <lzap+git@redhat.com> 1.4.0-1
- Updated foreman_discovery to 1.4.0 (lzap+git@redhat.com)

* Wed Oct 01 2014 Lukas Zapletal <lzap+git@redhat.com> 1.4.0-0.1.rc4
- Update rubygem-foreman_discovery to 1.4.0.rc4 (lzap+git@redhat.com)

* Wed Oct 01 2014 Lukas Zapletal <lzap+rpm@redhat.com> - 1.4.0-0.1.rc4
- Update foreman_discovery to 1.4.0.rc4

* Tue Sep 23 2014 Dominic Cleal <dcleal@redhat.com> 1.4.0-0.1.rc3
- Update foreman_discovery to 1.4.0.rc3 (dcleal@redhat.com)

* Mon Sep 22 2014 Dominic Cleal <dcleal@redhat.com> 1.4.0-0.1.rc2
- Update foreman_discovery to 1.4.0.rc2 (dcleal@redhat.com)

* Thu Aug 28 2014 Dominic Cleal <dcleal@redhat.com> 1.4.0-0.1.rc1
- Update foreman_discovery to 1.4.0.rc1 (dcleal@redhat.com)

* Fri Jun 06 2014 Lukas Zapletal <lzap+git@redhat.com> 1.3.0-1
- Updated foreman_discovery to 1.3.0 final version (lzap+git@redhat.com)

* Wed May 21 2014 Dominic Cleal <dcleal@redhat.com> 1.3.0-0.1.rc3
- Update foreman_discovery to 1.3.0.rc3 (dcleal@redhat.com)

* Fri Apr 18 2014 Lukas Zapletal <lzap+git@redhat.com> 1.3.0-0.1.rc2
- foreman_discovery-1.3.0.rc2 bump (lzap+git@redhat.com)
- Set minimum Foreman version of 1.5 (dcleal@redhat.com)

* Wed Apr 09 2014 Marek Hulan <mhulan@redhat.com> 1.3.0-0.1.rc1
- Update foreman discovery (mhulan@redhat.com)

* Wed Apr 02 2014 Dominic Cleal <dcleal@redhat.com> 1.2.0-1
- Update to 1.2.0 (dcleal@redhat.com)

* Fri Jan 24 2014 Lukas Zapletal <lzap+git@redhat.com> 1.2.0-0.1.rc2
- Bump foreman_discovery to 1.2.0.rc2 (lzap+git@redhat.com)
- Bump foreman_discovery to 1.2.0.rc1 (lzap+git@redhat.com)

* Sat Oct 19 2013 Dominic Cleal <dcleal@redhat.com> 1.1.1-1
- Update to 1.1.1 (dcleal@redhat.com)

* Fri Oct 18 2013 Dominic Cleal <dcleal@redhat.com> 1.1.0-1
- Update to 1.1.0 (dcleal@redhat.com)

* Thu Aug 22 2013 Dominic Cleal <dcleal@redhat.com> 1.0.2-7
- Create ~foreman/discovery_dir for image building (dcleal@redhat.com)
- Add patch for #2949, don't use bundler to find build_iso.sh
  (dcleal@redhat.com)
- Add dependencies and sudoers file for image building (dcleal@redhat.com)
- Remove SCL prefix from foreman-plugin-* provide (dcleal@redhat.com)

* Tue Aug 13 2013 Lukas Zapletal <lzap+git@redhat.com> 1.0.2-6
- adding SCL prefix to the provides statement (lzap+git@redhat.com)
- fixing dependency name (lzap+git@redhat.com)

* Tue Aug 13 2013 Lukas Zapletal <lzap+git@redhat.com> 1.0.2-5
- adding provides statement (lzap+git@redhat.com)

* Mon Aug 12 2013 Lukas Zapletal <lzap+git@redhat.com> 1.0.2-4
- adding missing source file (lzap+git@redhat.com)

* Mon Aug 12 2013 Lukas Zapletal <lzap+git@redhat.com> 1.0.2-3
- removing alpha tags (lzap+git@redhat.com)

* Thu Aug 01 2013 Lukas Zapletal <lzap+rpm[@]redhat.com> - 1.0.2-1
- bump to 1.0.2 release

* Wed Jun 26 2013 Dominic Cleal <dcleal@redhat.com> 1.0.0-0.1.rc4
- initial package build
