# template: foreman_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global foreman_min_version 2.5
%global foreman_max_version 2.6
%global plugin_name katello
%global gem_name katello
%global prereleasesource pre.master
%global prerelease %{?prereleasesource:.}%{?prereleasesource}
%global mainver 4.1.0
%global release 6

Name:    %{?scl_prefix}rubygem-%{gem_name}
Summary: Content and Subscription Management plugin for Foreman

Version: %{mainver}
Release: %{?prerelease:0.}%{release}%{?prerelease}%{?nightly}%{?dist}
Group:   Applications/Systems
License: GPLv2
URL:     https://theforeman.org/plugins/katello
Source0: https://rubygems.org/downloads/%{gem_name}-%{version}%{?prerelease}.gem

Autoreq: 0

Requires: foreman-postgresql
Requires: foreman < %{foreman_max_version}
# start specfile generated dependencies
Requires: foreman >= %{foreman_min_version}
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}rubygems
Requires: %{?scl_prefix}rubygem(rails)
Requires: %{?scl_prefix_ruby}rubygem(json)
Requires: %{?scl_prefix}rubygem(oauth)
Requires: %{?scl_prefix}rubygem(rest-client)
Requires: %{?scl_prefix}rubygem(rabl)
Requires: %{?scl_prefix}rubygem(foreman-tasks) >= 0.14.1
Requires: %{?scl_prefix}rubygem(foreman_remote_execution) >= 3.0
Requires: %{?scl_prefix}rubygem(dynflow) >= 1.2.0
Requires: %{?scl_prefix}rubygem(activerecord-import)
Requires: %{?scl_prefix}rubygem(qpid_proton)
Requires: %{?scl_prefix}rubygem(stomp)
Requires: %{?scl_prefix}rubygem(scoped_search) >= 4.1.9
Requires: %{?scl_prefix}rubygem(gettext_i18n_rails)
Requires: %{?scl_prefix}rubygem(apipie-rails) >= 0.5.14
Requires: %{?scl_prefix}rubygem(fx) < 1.0
Requires: %{?scl_prefix}rubygem(pg)
Requires: %{?scl_prefix}rubygem(runcible) >= 2.13.0
Requires: %{?scl_prefix}rubygem(runcible) < 3.0.0
Requires: %{?scl_prefix}rubygem(anemone)
Requires: %{?scl_prefix}rubygem(pulpcore_client) >= 3.6.0
Requires: %{?scl_prefix}rubygem(pulpcore_client) < 3.10.0
Requires: %{?scl_prefix}rubygem(pulp_file_client) >= 1.2.0
Requires: %{?scl_prefix}rubygem(pulp_file_client) < 1.6.0
Requires: %{?scl_prefix}rubygem(pulp_ansible_client) >= 0.2
Requires: %{?scl_prefix}rubygem(pulp_ansible_client) < 0.7
Requires: %{?scl_prefix}rubygem(pulp_container_client) >= 2.0.0
Requires: %{?scl_prefix}rubygem(pulp_container_client) < 2.3.0
Requires: %{?scl_prefix}rubygem(pulp_deb_client) >= 2.6.0
Requires: %{?scl_prefix}rubygem(pulp_deb_client) < 2.9.0
Requires: %{?scl_prefix}rubygem(pulp_rpm_client) >= 3.9.0
Requires: %{?scl_prefix}rubygem(pulp_rpm_client) < 3.10.0
Requires: %{?scl_prefix}rubygem(pulp_2to3_migration_client) >= 0.7.0
Requires: %{?scl_prefix}rubygem(pulp_2to3_migration_client) < 0.8.0
Requires: %{?scl_prefix}rubygem(pulp_certguard_client) < 2.0
Requires: %{?scl_prefix}rubygem(deface) >= 1.0.2
Requires: %{?scl_prefix}rubygem(deface) < 2.0.0
Requires: %{?scl_prefix}rubygem(angular-rails-templates) >= 1.1.0
Requires: %{?scl_prefix}rubygem(angular-rails-templates) < 1.2
BuildRequires: foreman-assets >= %{foreman_min_version}
BuildRequires: foreman-plugin >= %{foreman_min_version}
BuildRequires: %{?scl_prefix}rubygem(rails)
BuildRequires: %{?scl_prefix_ruby}rubygem(json)
BuildRequires: %{?scl_prefix}rubygem(oauth)
BuildRequires: %{?scl_prefix}rubygem(rest-client)
BuildRequires: %{?scl_prefix}rubygem(rabl)
BuildRequires: %{?scl_prefix}rubygem(foreman-tasks) >= 0.14.1
BuildRequires: %{?scl_prefix}rubygem(foreman_remote_execution) >= 3.0
BuildRequires: %{?scl_prefix}rubygem(dynflow) >= 1.2.0
BuildRequires: %{?scl_prefix}rubygem(activerecord-import)
BuildRequires: %{?scl_prefix}rubygem(qpid_proton)
BuildRequires: %{?scl_prefix}rubygem(stomp)
BuildRequires: %{?scl_prefix}rubygem(scoped_search) >= 4.1.9
BuildRequires: %{?scl_prefix}rubygem(gettext_i18n_rails)
BuildRequires: %{?scl_prefix}rubygem(apipie-rails) >= 0.5.14
BuildRequires: %{?scl_prefix}rubygem(fx) < 1.0
BuildRequires: %{?scl_prefix}rubygem(pg)
BuildRequires: %{?scl_prefix}rubygem(runcible) >= 2.13.0
BuildRequires: %{?scl_prefix}rubygem(runcible) < 3.0.0
BuildRequires: %{?scl_prefix}rubygem(anemone)
BuildRequires: %{?scl_prefix}rubygem(pulpcore_client) >= 3.6.0
BuildRequires: %{?scl_prefix}rubygem(pulpcore_client) < 3.10.0
BuildRequires: %{?scl_prefix}rubygem(pulp_file_client) >= 1.2.0
BuildRequires: %{?scl_prefix}rubygem(pulp_file_client) < 1.6.0
BuildRequires: %{?scl_prefix}rubygem(pulp_ansible_client) >= 0.2
BuildRequires: %{?scl_prefix}rubygem(pulp_ansible_client) < 0.7
BuildRequires: %{?scl_prefix}rubygem(pulp_container_client) >= 2.0.0
BuildRequires: %{?scl_prefix}rubygem(pulp_container_client) < 2.3.0
BuildRequires: %{?scl_prefix}rubygem(pulp_deb_client) >= 2.6.0
BuildRequires: %{?scl_prefix}rubygem(pulp_deb_client) < 2.9.0
BuildRequires: %{?scl_prefix}rubygem(pulp_rpm_client) >= 3.9.0
BuildRequires: %{?scl_prefix}rubygem(pulp_rpm_client) < 3.10.0
BuildRequires: %{?scl_prefix}rubygem(pulp_2to3_migration_client) >= 0.7.0
BuildRequires: %{?scl_prefix}rubygem(pulp_2to3_migration_client) < 0.8.0
BuildRequires: %{?scl_prefix}rubygem(pulp_certguard_client) < 2.0
BuildRequires: %{?scl_prefix}rubygem(deface) >= 1.0.2
BuildRequires: %{?scl_prefix}rubygem(deface) < 2.0.0
BuildRequires: %{?scl_prefix}rubygem(angular-rails-templates) >= 1.1.0
BuildRequires: %{?scl_prefix}rubygem(angular-rails-templates) < 1.2
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies
Obsoletes: %{?scl_prefix}rubygem-%{gem_name}_ostree
Obsoletes: %{?scl_prefix}rubygem-bastion
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

# start package.json devDependencies BuildRequires
BuildRequires: %{?scl_prefix}npm(@theforeman/builder) >= 6.0.0
# end package.json devDependencies BuildRequires
# start package.json dependencies BuildRequires
BuildRequires: %{?scl_prefix}npm(angular) = 1.8.2
BuildRequires: %{?scl_prefix}npm(bootstrap-select) = 1.13.6
BuildRequires: %{?scl_prefix}npm(downshift) >= 5.4.2
BuildRequires: %{?scl_prefix}npm(downshift) < 6.0.0
BuildRequires: %{?scl_prefix}npm(ngreact) >= 0.5.0
BuildRequires: %{?scl_prefix}npm(ngreact) < 1.0.0
BuildRequires: %{?scl_prefix}npm(query-string) >= 6.1.0
BuildRequires: %{?scl_prefix}npm(query-string) < 7.0.0
BuildRequires: %{?scl_prefix}npm(react-bootstrap) >= 0.32.1
BuildRequires: %{?scl_prefix}npm(react-bootstrap) < 1.0.0
# end package.json dependencies BuildRequires

%description
Content and Subscription Management plugin for Foreman.


%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Summary:    Documentation for %{pkg_name}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}

%description doc
Documentation for %{pkg_name}.

%package assets
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Summary:    Rebuild the assets for %{pkg_name}

Requires: foreman-assets >= %{foreman_min_version}
# start package.json devDependencies Requires
Requires: %{?scl_prefix}npm(@theforeman/builder) >= 6.0.0
# end package.json devDependencies Requires
# start package.json dependencies Requires
Requires: %{?scl_prefix}npm(angular) = 1.8.2
Requires: %{?scl_prefix}npm(bootstrap-select) = 1.13.6
Requires: %{?scl_prefix}npm(downshift) >= 5.4.2
Requires: %{?scl_prefix}npm(downshift) < 6.0.0
Requires: %{?scl_prefix}npm(ngreact) >= 0.5.0
Requires: %{?scl_prefix}npm(ngreact) < 1.0.0
Requires: %{?scl_prefix}npm(query-string) >= 6.1.0
Requires: %{?scl_prefix}npm(query-string) < 7.0.0
Requires: %{?scl_prefix}npm(react-bootstrap) >= 0.32.1
Requires: %{?scl_prefix}npm(react-bootstrap) < 1.0.0
# end package.json dependencies Requires

%description assets
This package can be used to rebuild the assets for %{pkg_name}.

%prep
%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}

%setup -q -D -T -n  %{gem_name}-%{version}%{?prerelease}

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
%license %{gem_instdir}/LICENSE.txt
%{gem_instdir}/app
%{gem_instdir}/ca
%{gem_instdir}/config
%{gem_instdir}/db
%{gem_instdir}/engines
%{gem_libdir}
%{gem_instdir}/locale
%{gem_instdir}/public/assets/bastion
%{gem_instdir}/public/assets/bastion_katello
%{gem_instdir}/vendor
%exclude %{gem_cache}
%{gem_spec}
%{foreman_bundlerd_plugin}
%{foreman_apipie_cache_foreman}
%{foreman_apipie_cache_plugin}
%{foreman_assets_plugin}
%{foreman_webpack_foreman}
%{foreman_webpack_plugin}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%files assets
%{gem_instdir}/package.json
%{gem_instdir}/webpack

%changelog
* Mon Mar 15 2021 Eric D. Helms <ericdhelms@gmail.com> - 4.1.0-0.6.pre.master
- Rebuild for Ruby 2.7

* Fri Mar 12 2021 Eric D. Helms <ericdhelms@gmail.com> - 4.1.0-0.5.pre.master
- Relax Ruby requirements

* Wed Feb 24 2021 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 4.1.0-0.4.pre.master
- Update Gem and NPM dependencies

* Mon Feb 15 2021 Justin Sherrill <jsherril@redhat.com> 4.1.0-0.3.pre.master
- upgrade to newer migration client gem

* Thu Feb 4 2021 Jonathon Turel - 4.1.0-0.2.pre.master
- Add qpid_proton dependency

* Thu Feb 04 2021 Eric D. Helms <ericdhelms@gmail.com> - 4.1.0-0.1.pre.master
- Bump version to 4.1.0

* Mon Jan 11 2021 Ian Ballou <ianballou67@gmail.com> - 4.0.0-0.3.pre.master
- Update Pulp 3 client bindings requirements

* Mon Nov 23 2020 Evgeni Golov - 4.0.0-0.2.pre.master
- Update @theforeman/builder dependency

* Wed Nov 04 2020 Jonathon Turel <jturel@gmail.com> 4.0.0-0.1.pre.master
- Add pulp_deb_client dependencies
- Bump version to 4.0.0

* Thu Oct 15 2020 Ian Ballou <ianballou67@gmail.com> 3.18.0-0.5.pre.master
- update pulp 3 client requires

* Fri Sep 11 2020 Justin Sherrill <jsherril@redhat.com> 3.18.0-0.4.pre.master
- update pulp_ansible_client requires

* Wed Sep 09 2020 Evgeni Golov - 3.18.0-0.3.pre.master
- Update GEM dependencies

* Tue Sep 01 2020 Evgeni Golov - 3.18.0-0.2.pre.master
- Update GEM dependencies

* Tue Aug 11 2020 Eric D. Helms <ericdhelms@gmail.com> - 3.18.0-0.1.pre.master
- Bump to 3.18.0

* Tue Aug 04 2020 Justin Sherrill <jsherril@redhat.com> 3.17.0-0.1.pre.master
- update version to 3.17.0
- pulp_rpm 3.5 support
- add remote_execution dep
- Disable autorequires to prevent rich dependency auto-creation on EL8
- Add pulp_certguard_client
- Drop Requires on katello-selinux

* Wed May 06 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.16.0-0.13.pre.master
- Update foreman version bounds

* Mon May 04 2020 Justin Sherrill <jsherril@redhat.com> 3.16.0-0.12.pre.master
- Update to pulp 3.3 bindings

* Fri May 01 2020 Eric D. Helms <ericdhelms@gmail.com> - 3.16.0-0.11.pre.master
- Add fx to build requires

* Fri Apr 17 2020 Jonathon Turel <jturel@gmail.com> 3.16.0-0.10.pre.master
- Replace qpid_messaging with stomp

* Thu Apr 16 2020 Jonathon Turel <jturel@gmail.com> 3.16.0-0.9.pre.master
- Adjust angular-rails-templates version

* Mon Apr 13 2020 ianballou <ianballou67@gmail.com> 3.16.0-0.8.pre.master
- Add fx gem as a dependency

* Tue Apr 07 2020 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 3.16.0-0.7.pre.master
- Update Gem and NPM dependencies

* Wed Apr 01 2020 Justin Sherrill <jsherril@redhat.com> 3.16.0-0.6.pre.master
- Update angular dep

* Wed Apr 01 2020 Evgeni Golov - 3.16.0-0.5.pre.master
- correct BuildRequires for new pulp gems

* Thu Mar 26 2020 Samir Jha <sajha@redhat.com> 3.16.0-0.4.pre.master
- Update pulp gem requirements

* Thu Feb 20 2020 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 3.16.0-0.3.pre.master
- Update Gem and NPM dependencies

* Wed Feb 19 2020 Justin Sherrill <jsherril@redhat.com> 3.16.0-0.2.pre.master
- Update pulp_2to3_migration requirement

* Thu Feb 13 2020 James Jeffers <jjeffers@redhat.com> - 3.16.0-0.1.pre.master
- Bump version to 3.16

* Wed Jan 29 2020 Justin Sherrill <jlsherrill@gmail.com> - 3.15.0-0.6.pre.master
- Restrict pulp client gems

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.15.0-0.5.pre.master
- Update spec to remove the ror scl

* Wed Dec 18 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 3.15.0-0.4.pre.master
- Update Gem and NPM dependencies

* Wed Nov 27 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 3.15.0-0.3.pre.master
- Update Gem and NPM dependencies

* Mon Nov 18 2019 Evgeni Golov - 3.15.0-0.2.pre.master
- Unify prerelease macro handling

* Fri Nov 01 2019 Jonathon Turel <jturel@gmail.com> - 3.15.0-0.1.pre.master
- Bump to 3.15.0

* Tue Oct 22 2019 Eric D. Helms <ericdhelms@gmail.com> - 3.14.0-0.4.pre.master
- Update requires on nodejs packages

* Sun Oct 06 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 3.14.0-0.3.pre.master
- Update Gem and NPM dependencies

* Mon Aug 26 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 3.14.0-0.2.pre.master
- Update Gem and NPM dependencies

* Wed Aug 07 2019 Evgeni Golov - 3.14.0-0.1.pre.master
- Bump version to 3.14

* Tue Jul 23 2019 Evgeni Golov - 3.13.0-0.7.pre.master
- Update katello packaging to @theforeman/vendor bundle

* Thu Jul 11 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 3.13.0-0.6.pre.master
- Update Gem and NPM dependencies

* Mon Jul 01 2019 Justin Sherrill <jlsherrill@gmail.com> 3.13.0-0.5.pre.master
- add pulp_ansible_client requirement

* Wed Jun 12 2019 Justin Sherrill <jlsherrill@gmail.com> - 3.13.0-0.4.pre.master
- update pulp_file_client requirement

* Mon Jun 10 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 3.13.0-0.3.pre.master
- Update gem and NPM dependencies

* Tue May 14 2019 Justin Sherrill <jlsherrill@gmail.com> - 3.13.0-0.2.pre.master
- pull in new pulp3 gem dependencies

* Thu Apr 25 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 3.13.0-0.1.pre.master
- Bump version to 3.13

* Mon Apr 15 2019 Ondrej Prazak <oprazak@redhat.com> - 3.12.0-0.8.pre.master
- Remove foreman_docker as a dependency

* Tue Apr 02 2019 Eric D. Helms <ericdhelms@gmail.com> - 3.12.0-0.7.pre.master
- Properly obsolete bastion

* Tue Apr 2 2019 Tomer Brisker- 3.12.0-0.6.pre.master
- Add zest dependency

* Fri Mar 29 2019 Justin Sherrill - 3.12.0-0.5.pre.master
- Remove bastion

* Fri Mar 15 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 3.12.0-0.4.pre.master
- Update gem and NPM dependencies

* Thu Feb 7 2019 Justin Sherrill <jlsherrill@gmail.com> - 3.12.0-0.3.pre.master
- Require activerecord-import

* Wed Jan 23 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 3.12.0-0.2.pre.master
- Update gem dependencies

* Wed Jan 16 2019 Eric D. Helms <ericdhelms@gmail.com> - 3.12.0-0.1.pre.master
- Bump version to 3.12

* Wed Jan 09 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 3.11.0-0.2.pre.master
- Update NPM dependencies

* Fri Nov 30 2018 Eric D. Helms <ericdhelms@gmail.com> - 3.11.0-0.1.pre.master
- Bump version to 3.11

* Wed Oct 31 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 3.10.0-0.4.pre.master
- Stop removing JS source maps

* Thu Oct 25 2018 Adam Price <komidore64@gmail.com> - 3.10.0-0.3.pre.master
- add nightly macro

* Wed Oct 24 2018 Adam Price <komidore64@gmail.com> - 3.10.0-0.2.pre.master
- set prerelease to .pre.master

* Thu Oct 18 2018 Eric D. Helms <ericdhelms@gmail.com> - 3.10.0-1
- Bump version to 3.10

* Thu Oct 11 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 3.9.0-6
- Update NPM dependencies
- Exclude Javascript source maps

* Mon Sep 17 2018 Eric D. Helms <ericdhelms@gmail.com> - 3.9.0-5
- Add nodejs-query-string as a dependency

* Thu Sep 13 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 3.9.0-4
- Update NPM dependencies

* Tue Sep 11 2018 Eric D. Helms <ericdhelms@gmail.com> - 3.9.0-3
- Update dependencies

* Tue Jul 24 2018 Eric D. Helms <ericdhelms@gmail.com> - 3.9.0-2
- Add prerelease macro support

* Wed Jul 18 2018 Eric D. Helms <ericdhelms@gmail.com> 3.9.0-1.nightly
- Bump to 3.9

* Wed Jun 6 2018 Eric D. Helms <ericdhelms@gmail.com> 3.8.0-1.nightly
- Switch Katello to 3.8
