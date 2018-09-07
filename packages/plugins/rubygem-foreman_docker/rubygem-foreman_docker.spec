# template: foreman_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_docker
%global plugin_name docker
%global foreman_min_version 1.17.0

Summary:    Provision and manage Docker containers and images from Foreman
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    4.1.0
Release:    2%{?foremandist}%{?dist}
Group:      Applications/Systems
License:    GPLv3
URL:        https://github.com/theforeman/foreman_docker
Source0:    https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: foreman-compute >= %{foreman_min_version}
BuildRequires: foreman-compute >= %{foreman_min_version}
# start generated dependencies
Requires: foreman >= %{foreman_min_version}
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(docker-api) >= 1.18
Requires: %{?scl_prefix}rubygem(docker-api) < 2
Requires: %{?scl_prefix}rubygem(excon) >= 0.46
Requires: %{?scl_prefix}rubygem(excon) < 1
Requires: %{?scl_prefix}rubygem(deface) < 2.0
Requires: %{?scl_prefix}rubygem(wicked) >= 1.1
Requires: %{?scl_prefix}rubygem(wicked) < 2
BuildRequires: foreman-assets >= %{foreman_min_version}
BuildRequires: foreman-plugin >= %{foreman_min_version}
BuildRequires: %{?scl_prefix}rubygem(docker-api) >= 1.18
BuildRequires: %{?scl_prefix}rubygem(docker-api) < 2
BuildRequires: %{?scl_prefix}rubygem(excon) >= 0.46
BuildRequires: %{?scl_prefix}rubygem(excon) < 1
BuildRequires: %{?scl_prefix}rubygem(deface) < 2.0
BuildRequires: %{?scl_prefix}rubygem(wicked) >= 1.1
BuildRequires: %{?scl_prefix}rubygem(wicked) < 2
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-%{plugin_name}
# end generated dependencies
Provides: foreman-docker
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Provision and manage Docker containers and images from Foreman.


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
%exclude %{gem_instdir}/.rubocop.yml
%license %{gem_instdir}/LICENSE
%{gem_instdir}/app
%{gem_instdir}/config
%{gem_instdir}/db
%{gem_libdir}
%{gem_instdir}/locale
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
%{foreman_apipie_cache}
%{foreman_restart}
exit 0

%changelog
* Fri Sep 07 2018 Eric D. Helms <ericdhelms@gmail.com> - 4.1.0-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Sun May 27 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 4.1.0-1
- Update to 4.1.0
- Regenerate spec file based on the current template

* Thu Jan 11 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 4.0.0-1
- Release foreman_docker 4.0.0 (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Wed Jun 28 2017 Eric D. Helms <ericdhelms@gmail.com> 3.2.1-1
- plugins:foreman_docker - Release 3.2.1 (mail@bastilian.me)

* Mon Jun 19 2017 Eric D. Helms <ericdhelms@gmail.com> 3.1.0-1
- Updated foreman_docker to 3.1.0 (me@daniellobato.me)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Mon Aug 01 2016 Eric D Helms <ericdhelms@gmail.com> 3.0.0-1
- plugins: foreman-docker 3.0.0 (elobatocs@gmail.com)

* Fri Apr 15 2016 Dominic Cleal <dominic@cleal.org> 2.1.1-1
- plugins:foreman_docker - 2.1.1 (elobatocs@gmail.com)

* Mon Jan 18 2016 Dominic Cleal <dcleal@redhat.com> 2.0.1-1
- plugins:foreman_docker - Release 2.0.1 (elobatocs@gmail.com)

* Wed Jan 06 2016 Dominic Cleal <dcleal@redhat.com> 2.0.0-2
- Fix docker-api dependency version number in gemspec (dcleal@redhat.com)

* Wed Jan 06 2016 Dominic Cleal <dcleal@redhat.com> 2.0.0-1
- plugins:foreman_docker - Release 2.0.0 (elobatocs@gmail.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Thu Aug 27 2015 Dominic Cleal <dcleal@redhat.com> 1.4.1-2
- Converted to tfm SCL (dcleal@redhat.com)

* Wed Aug 19 2015 Dominic Cleal <dcleal@redhat.com> 1.4.1-1
- plugins:foreman_docker - Release 1.4.1 (elobatocs@gmail.com)

* Tue Jul 28 2015 Dominic Cleal <dcleal@redhat.com> 1.4.0-2
- Use foremandist macro in release (dcleal@redhat.com)

* Fri Jul 24 2015 Dominic Cleal <dcleal@redhat.com> 1.4.0-1.fm1_10
- Update foreman_docker to 1.4.0 (dcleal@redhat.com)

* Wed Apr 29 2015 Dominic Cleal <dcleal@redhat.com> 1.3.1-1.fm1_9
- plugins:foreman_docker - Release 1.3.1 (elobatocs@gmail.com)

* Wed Apr 29 2015 Dominic Cleal <dcleal@redhat.com> 1.3.0-1.fm1_9
- plugins:foreman_docker - Release 1.3.0 (elobatocs@gmail.com)
- Partially revert "Better branched builds with Foreman version macro"
  (dcleal@redhat.com)

* Thu Apr 23 2015 Dominic Cleal <dcleal@redhat.com> 1.2.4-2
- Use foremandist macro in release (dcleal@redhat.com)

* Wed Mar 25 2015 Dominic Cleal <dcleal@redhat.com> 1.2.4-1.fm1_9
- plugins:foreman_docker - Release 1.2.4 (elobatocs@gmail.com)
- Min of foreman 1.8.0 due to post-install scriptlet (dcleal@redhat.com)

* Fri Mar 20 2015 Dominic Cleal <dcleal@redhat.com> 1.2.3-1.fm1_9
- Update foreman_docker to 1.2.3 (dcleal@redhat.com)

* Wed Mar 11 2015 Daniel Lobato Garcia <dlobatog@redhat.com> 1.2.2-1.fm1_8
- Updating the version of foreman_docker to 1.2.2

* Wed Mar 04 2015 Dominic Cleal <dcleal@redhat.com> 1.2.1-2.fm1_8
- Precompile foreman_docker API docs (dcleal@redhat.com)

* Tue Mar 03 2015 Daniel Lobato Garcia <dlobatog@redhat.com> 1.2.1-1
- Updating the version of foreman_docker to 1.2.1

* Tue Feb 24 2015 Daniel Lobato Garcia <dlobatog@redhat.com> 1.2.0-1
- Updating the version of foreman_docker to 1.2.0
- docker-api dependency listed to 1.17 minimum

* Mon Feb 23 2015 Dominic Cleal <dcleal@redhat.com> 1.1.0-2
- Default options in foreman_precompile_plugin changed (rubygem-foreman_docker)
  (martin.bacovsky@gmail.com)

* Tue Feb 10 2015 Daniel Lobato Garcia <dlobatog@redhat.com> 1.1.0-1
- Support katello content views to create containers

* Thu Feb 5 2015 Daniel Lobato Garcia <dlobatog@redhat.com> 1.0.1-1
- Fixes for 1.7 compatibility
- Do not list the assets directory twice. (slukasik@redhat.com)

* Mon Jan 12 2015 Daniel Lobato Garcia <dlobatog@redhat.com> 1.0.0-1
- Updating the version of foreman_docker to 1.0.0

* Wed Nov 05 2014 Dominic Cleal <dcleal@redhat.com> 0.2.0-2
- Precompile foreman_docker assets (dcleal@redhat.com)

* Mon Nov 3 2014 Daniel Lobato Garcia <dlobatog@redhat.com> 0.2.0-1
- Updating the version of foreman_docker to 0.2.0

* Tue Oct 21 2014 David Davis <daviddavis@redhat.com> 0.1.0-1
- Updating the version of foreman_docker to 0.1.0

* Tue Apr 29 2014 Dominic Cleal <dcleal@redhat.com> 0.0.3-1
- new package built with tito
