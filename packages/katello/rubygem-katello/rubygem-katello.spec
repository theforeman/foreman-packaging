# template: foreman_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global foreman_min_version 3.6
%global foreman_max_version 3.7
%global plugin_name katello
%global gem_name katello
%global prereleasesource rc2
%global prerelease %{?prereleasesource:.}%{?prereleasesource}
%global mainver 4.8.0
%global release 2

Name:    %{?scl_prefix}rubygem-%{gem_name}
Summary: Content and Subscription Management plugin for Foreman

Version: %{mainver}
Release: %{?prerelease:0.}%{release}%{?prerelease}%{?nightly}%{?dist}
Group:   Applications/Systems
License: GPLv2
URL:     https://theforeman.org/plugins/katello
Source0: https://rubygems.org/downloads/%{gem_name}-%{version}%{?prerelease}.gem

Requires: foreman-postgresql
Requires: foreman < %{foreman_max_version}
# start specfile generated dependencies
Requires: foreman >= %{foreman_min_version}
Requires: ruby >= 2.5
Requires: ruby < 3
BuildRequires: foreman-assets >= %{foreman_min_version}
BuildRequires: foreman-plugin >= %{foreman_min_version}
Requires: ruby >= 2.5
Requires: ruby < 3
BuildRequires: ruby >= 2.5
BuildRequires: ruby < 3
BuildRequires: rubygems-devel > 1.3.1
BuildArch: noarch
Provides: foreman-plugin-%{plugin_name} = %{version}
BuildRequires: rubygem(rails)
BuildRequires: rubygem(json)
BuildRequires: rubygem(oauth)
BuildRequires: rubygem(rest-client)
BuildRequires: rubygem(rabl)
BuildRequires: rubygem(foreman-tasks) >= 5.0
BuildRequires: rubygem(foreman_remote_execution) >= 7.1.0
BuildRequires: rubygem(dynflow) >= 1.6.1
BuildRequires: rubygem(activerecord-import)
BuildRequires: rubygem(qpid_proton)
BuildRequires: rubygem(stomp)
BuildRequires: rubygem(scoped_search) >= 4.1.9
BuildRequires: rubygem(gettext_i18n_rails)
BuildRequires: rubygem(apipie-rails) >= 0.5.14
BuildRequires: rubygem(fx) < 1.0
BuildRequires: rubygem(pg)
BuildRequires: rubygem(runcible) >= 2.13.0
BuildRequires: rubygem(runcible) < 3.0.0
BuildRequires: rubygem(anemone)
BuildRequires: rubygem(pulpcore_client) >= 3.22.0
BuildRequires: rubygem(pulpcore_client) < 3.23.0
BuildRequires: rubygem(pulp_file_client) >= 1.12.0
BuildRequires: rubygem(pulp_file_client) < 1.13
BuildRequires: rubygem(pulp_ansible_client) >= 0.16.0
BuildRequires: rubygem(pulp_ansible_client) < 0.17
BuildRequires: rubygem(pulp_container_client) >= 2.14.0
BuildRequires: rubygem(pulp_container_client) < 2.15.0
BuildRequires: rubygem(pulp_deb_client) >= 2.20.0
BuildRequires: rubygem(pulp_deb_client) < 2.21
BuildRequires: rubygem(pulp_rpm_client) >= 3.19.0
BuildRequires: rubygem(pulp_rpm_client) < 3.20.0
BuildRequires: rubygem(pulp_certguard_client) < 2.0
BuildRequires: rubygem(pulp_python_client) >= 3.8.0
BuildRequires: rubygem(pulp_python_client) < 3.9
BuildRequires: rubygem(pulp_ostree_client)
BuildRequires: rubygem(deface) >= 1.0.2
BuildRequires: rubygem(deface) < 2.0.0
BuildRequires: rubygem(angular-rails-templates) >= 1.1.0
BuildRequires: rubygem(angular-rails-templates) < 1.2
# end specfile generated dependencies
Obsoletes: %{?scl_prefix}rubygem-%{gem_name}_ostree
Obsoletes: %{?scl_prefix}rubygem-pulp_2to3_migration_client
Obsoletes: %{?scl_prefix}rubygem-bastion
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

# start package.json devDependencies BuildRequires
BuildRequires: npm(@theforeman/builder) >= 6.0.0
# end package.json devDependencies BuildRequires
# start package.json dependencies BuildRequires
BuildRequires: npm(angular) = 1.8.2
BuildRequires: npm(bootstrap-select) = 1.13.18
BuildRequires: npm(downshift) >= 5.4.2
BuildRequires: npm(downshift) < 6.0.0
BuildRequires: npm(ngreact) >= 0.5.0
BuildRequires: npm(ngreact) < 1.0.0
BuildRequires: npm(query-string) >= 6.1.0
BuildRequires: npm(query-string) < 7.0.0
BuildRequires: npm(react-bootstrap) >= 0.32.1
BuildRequires: npm(react-bootstrap) < 1.0.0
BuildRequires: npm(use-deep-compare-effect) >= 1.6.1
BuildRequires: npm(use-deep-compare-effect) < 2.0.0
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
Requires: npm(@theforeman/builder) >= 6.0.0
# end package.json devDependencies Requires
# start package.json dependencies Requires
Requires: npm(angular) = 1.8.2
Requires: npm(bootstrap-select) = 1.13.18
Requires: npm(downshift) >= 5.4.2
Requires: npm(downshift) < 6.0.0
Requires: npm(ngreact) >= 0.5.0
Requires: npm(ngreact) < 1.0.0
Requires: npm(query-string) >= 6.1.0
Requires: npm(query-string) < 7.0.0
Requires: npm(react-bootstrap) >= 0.32.1
Requires: npm(react-bootstrap) < 1.0.0
Requires: npm(use-deep-compare-effect) >= 1.6.1
Requires: npm(use-deep-compare-effect) < 2.0.0
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
%foreman_precompile_plugin -s

for asset in bastion bastion_katello
do
  ln -s %{gem_instdir}/public/assets/${asset} %{buildroot}%{foreman_dir}/public/assets/${asset}
done

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
%exclude %{gem_instdir}/vendor
%exclude %{gem_cache}
%{gem_spec}
%{foreman_bundlerd_plugin}
%{foreman_assets_plugin}
%{foreman_assets_foreman}
%{foreman_dir}/public/assets/bastion
%{foreman_dir}/public/assets/bastion_katello
%{foreman_webpack_foreman}
%{foreman_webpack_plugin}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%files assets
%{gem_instdir}/package.json
%{gem_instdir}/webpack

%changelog
* Mon Apr 03 2023 Odilon Sousa <osousa@redhat.com> - 4.8.0-0.2.rc2
- Release rubygem-katello 4.8.0rc2

* Tue Feb 28 2023 Odilon Sousa <osousa@redhat.com> - 4.8.0-0.2.rc1
- Release rubygem-katello 4.8.0rc1

* Wed Feb 15 2023 Ian Ballou <ianballou67@gmail.com> - 4.8.0-0.2.pre.master
- Update Pulp bindings for Pulpcore 3.22

* Thu Nov 10 2022 Evgeni Golov - 4.8.0-0.1.pre.master
- Bump version to 4.8.0

* Wed Oct 26 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 4.7.0-0.6.pre.master
- Update Gem and NPM dependencies

* Mon Oct 3 2022 Ian Ballou <ianballou67@gmail.com> 4.7.0-0.5.pre.master
- Bump pulp_python_client requirement to be higher than 3.7.1 but lower then 3.8.0

* Wed Aug 31 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 4.7.0-0.4.pre.master
- Update Gem and NPM dependencies

* Fri Aug 26 2022 Evgeni Golov - 4.7.0-0.3.pre.master
- Don't ship the vendor dir, it's only need during build

* Mon Aug 22 2022 Evgeni Golov - 4.7.0-0.2.pre.master
- Fixes #35409 - symlink legacy katello assets from foreman assets

* Mon Aug 15 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 4.7.0-0.1.pre.master
- Update to version 4.7

* Thu Jun 16 2022 Ian Ballou <ianballou67@gmail.com> 4.6.0-0.3.pre.master
- Bump pulp_ansible_client requirement to at least 0.13.1 but not more than 0.14

* Wed May 18 2022 Ian Ballou <ianballou67@gmail.com> 4.6.0-0.2.pre.master
- Bump pulpcore_client requirement to 3.18

* Thu May 12 2022 Partha Aji <paji@redhat.com> 4.6.0-0.1.pre.master
- bump to 4.6

* Mon May 02 2022 Quirin Pamp - 4.5.0-0.5.pre.master
- Update katello's pulp_deb GEM dependency

* Thu Apr 28 2022 Evgeni Golov - 4.5.0-0.4.pre.master
- Update katello GEM dependencies

* Fri Apr 22 2022 Eric D. Helms <ericdhelms@gmail.com> - 4.5.0-0.3.pre.master
- Stop generaing apipie cache

* Mon Feb 28 2022 Justin Sherrill <jsherril@redhat.com> 4.5.0-0.2.pre.master
- update to pulp-rpm 3.17

* Wed Feb 16 2022 Justin Sherrill <jsherril@redhat.com> 4.5.0-0.1.pre.master
- bump for 4.5

* Thu Nov 18 2021 Ian Ballou <ianballou67@gmail.com> 4.4.0-0.2.pre.master
- updates to pulpcore 3.16 client bindings

* Wed Nov 17 2021 Chris Roberts <chrobert@redhat.com> 4.4.0-0.1.pre.master
- 4.4.0 version bump

* Tue Oct 19 2021 Justin Sherrill <jsherril@redhat.com> 4.3.0-0.5.pre.master
- updates to pulpcore 3.15 client bindings

* Tue Sep 28 2021 Justin Sherrill <jsherril@redhat.com> 4.3.0-0.4.pre.master
- match dynflow requires at 1.6.1, add pulp_ostree_client

* Mon Sep 27 2021 Justin Sherrill <jsherril@redhat.com> 4.3.0-0.3.pre.master
- bump bootstrap-select requires

* Thu Sep 02 2021 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 4.3.0-0.2.pre.master
- Update Gem and NPM dependencies

* Mon Aug 09 2021 Justin Sherrill <jsherril@redhat.com> 4.3.0-0.1.pre.master
- 4.3.0 version bump

* Fri Jul 23 2021 Evgeni Golov - 4.2.0-0.4.pre.master
- Update Foreman version

* Thu Jul 08 2021 Evgeni Golov - 4.2.0-0.3.pre.master
- Update gem dependencies

* Mon Jul 05 2021 Evgeni Golov - 4.2.0-0.2.pre.master
- Update gem and npm dependencies

* Thu May 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 4.2.0-0.1.pre.master
- Update to 4.2.0

* Tue Apr 27 2021 Quirin Pamp <pamp@atix.de> 4.1.0-0.9.pre.master
- Update Katello's pulp_deb_client requirement to 2.11

* Mon Apr 12 2021 ianballou <ianballou67@gmail.com> 4.1.0-0.8.pre.master
- Update Katello's pulp_rpm_client requirement to 3.10.0

* Thu Apr 08 2021 Justin Sherrill <jsherril@redhat.com> 4.1.0-0.7.pre.master
- pulpcore 3.11 upgrade

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
