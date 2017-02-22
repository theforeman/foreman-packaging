%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name katello
# %%global prever .rc1
%global mainver 3.4.0
%global release 1.nightly

%global foreman_dir /usr/share/foreman
%global foreman_bundlerd_dir %{foreman_dir}/bundler.d

%global scl_ruby_bin /usr/bin/%{?scl:%{scl_prefix}}ruby
%global scl_rake /usr/bin/%{?scl:%{scl_prefix}}rake

%global gem_instdir %{gem_dir}/gems/%{gem_name}-%{mainver}%{?prever}
%global gem_docdir %{gem_dir}/doc/%{gem_name}-%{mainver}%{?prever}
%global gem_cache %{gem_dir}/cache/%{gem_name}-%{mainver}%{?prever}.gem
%global gem_spec %{gem_dir}/specifications/%{gem_name}-%{mainver}%{?prever}.gemspec

%define katello_ostree %{?scl_prefix}rubygem-%{gem_name}_ostree

Name:    %{?scl_prefix}rubygem-%{gem_name}
Summary: Katello

Version: %{mainver}
Release: %{?prever:0.}%{release}%{?prever}%{?dist}
Group:   Development/Ruby
License: Distributable
URL:     http://www.katello.org
Source0: https://rubygems.org/downloads/%{gem_name}-%{version}%{?prever}.gem

Requires: katello-selinux
Requires: foreman >= 1.11.0
Requires: foreman-postgresql
Requires: %{?scl_prefix}rubygem(angular-rails-templates) >= 0.0.4
Requires: %{?scl_prefix}rubygem(bastion) >= 4.0.0
Requires: %{?scl_prefix}rubygem(bastion) < 5.0.0
Requires: %{?scl_prefix}rubygem(oauth)
Requires: %{?scl_prefix}rubygem(rest-client)
Requires: %{?scl_prefix}rubygem(rabl)
Requires: %{?scl_prefix}rubygem(foreman_docker) >= 0.2.0
Requires: %{?scl_prefix}rubygem(foreman-tasks) >= 0.8.0
Requires: %{?scl_prefix}rubygem(foreman-tasks) < 0.9.0
Requires: %{?scl_prefix}rubygem(gettext_i18n_rails)
Requires: %{?scl_prefix}rubygem(apipie-rails) >= 0.1.1
Requires: %{?scl_prefix}rubygem(runcible) >= 1.3.0
Requires: %{?scl_prefix}rubygem(anemone)
Requires: %{?scl_prefix}rubygem(jquery-ui-rails)
Requires: %{?scl_prefix}rubygem(deface) >= 1.0.0
Requires: %{?scl_prefix}rubygem(deface) < 2.0.0
Requires: %{?scl_prefix}rubygem(qpid_messaging)
Requires: %{?scl_prefix_ruby}rubygem(json)
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)

BuildRequires: foreman-assets
BuildRequires: foreman-plugin >= 1.11.0
BuildRequires: %{?scl_prefix}rubygem(foreman_docker) >= 0.2.0
BuildRequires: %{?scl_prefix}rubygem(angular-rails-templates) >= 0.0.4
BuildRequires: %{?scl_prefix}rubygem(bastion) >= 4.0.0
BuildRequires: %{?scl_prefix}rubygem(bastion) < 5.0.0
BuildRequires: %{?scl_prefix}rubygem(foreman-tasks) >= 0.8.0
BuildRequires: %{?scl_prefix}rubygem(foreman-tasks) < 0.9.0
BuildRequires: %{?scl_prefix}rubygem(gettext_i18n_rails)
BuildRequires: %{?scl_prefix}rubygem(apipie-rails) >= 0.1.1
BuildRequires: %{?scl_prefix}rubygem(runcible) >= 1.3.0
BuildRequires: %{?scl_prefix}rubygem(anemone)
BuildRequires: %{?scl_prefix}rubygem(jquery-ui-rails)
BuildRequires: %{?scl_prefix}rubygem(deface) >= 1.0.0
BuildRequires: %{?scl_prefix}rubygem(deface) < 2.0.0
BuildRequires: %{?scl_prefix}rubygem(qpid_messaging)
BuildRequires: %{?scl_prefix_ror}rubygem(rails)
BuildRequires: %{?scl_prefix_ruby}rubygem(json)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}ruby(release)

#old dependencies that are no longer needed, remove in katello 2.6
Obsoletes: ruby193-rubygem-haml
Obsoletes: ruby193-rubygem-haml-rails
Obsoletes: ruby193-rubygem-hpricot
Obsoletes: ruby193-rubygem-strong_parameters
Obsoletes: ruby193-rubygem-tire
Obsoletes: ruby193-rubygem-less
Obsoletes: ruby193-rubygem-hashr
Obsoletes: ruby193-rubygem-foreman_gutterball

BuildArch: noarch
Provides: %{?scl_prefix}rubygem(katello) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Katello

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Summary:    Documentation for rubygem-%{gem_name}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%package -n %{katello_ostree}
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Summary:    Katello Ostree Plugin

%description -n %{katello_ostree}
This package provides the ostree plugin for rubygem-%{gem_name}.

%prep
%setup -q -c -T -n %{pkg_name}-%{version}
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0} --no-rdoc --no-ri
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%foreman_bundlerd_file
%foreman_precompile_plugin -s -a

%files
%dir %{gem_instdir}/
%{gem_libdir}
%{gem_instdir}/app
%{gem_instdir}/config
%{gem_instdir}/db
%{gem_instdir}/locale
%{gem_instdir}/engines
%{gem_instdir}/ca
%{gem_instdir}/vendor
%{gem_spec}
%{foreman_bundlerd_plugin}
%{foreman_apipie_cache_foreman}
%{foreman_apipie_cache_plugin}
%{foreman_assets_plugin}
%{gem_instdir}/public/assets/bastion_katello

%exclude %{gem_cache}
%exclude %{gem_instdir}/lib/katello/repository_types/ostree.rb

%doc %{gem_instdir}/LICENSE.txt

%files doc
%doc %{gem_instdir}/README.md

%files -n %{katello_ostree}
%{gem_instdir}/lib/katello/repository_types/ostree.rb

%changelog
* Wed Jul 29 2015 Eric D. Helms <ericdhelms@gmail.com> 2.4.0-1.nightly
- new package built with tito

* Mon Jul 06 2015 Stephen Benjamin <stbenjam@redhat.com> 2.4.0-2
- Version bump to 2.4.0 (stbenjam@redhat.com)

* Mon Jul 06 2015 Stephen Benjamin <stbenjam@redhat.com>
- Version bump to 2.4.0 (stbenjam@redhat.com)

* Mon Jul 06 2015 Stephen Benjamin <stbenjam@redhat.com> 2.4.0-1
- Update to Katello 2.4.0
* Mon Jul 06 2015 Stephen Benjamin <stbenjam@redhat.com> 2.3.0-2
- adding myself to contrib (chrobert@redhat.com)
- Refs #10962 - limit foreman tasks in rpm specs to < 0.7.0 (inecas@redhat.com)
- Fixes #10830 - Humanized state description for Pulp and Candlepin async
  actions (inecas@redhat.com)
  (jlsherrill@gmail.com)
- fixes #10934 - per-page/page options for puppet-module list, BZ1202050
  (komidore64@gmail.com)
- Fixes #10904: fix errata CH selection, BZ 1233901. (walden@redhat.com)
- fixes #10903 - remove reference to non-existent methods
  (thomasmckay@redhat.com)
- Fixes #10705: filter out non-installable Systems BZ1228292.
  (walden@redhat.com)
- fixes #10901 - skip all errors on sync tasks (jsherril@redhat.com)
- fixes #8690 - converting repository to scoped search (jsherril@redhat.com)
- fixes #10886 - adding more conditions for readable repos
  (jsherril@redhat.com)
- Fixes #8693: Convert content view puppet module to scoped search.
  (ericdhelms@gmail.com)
- refs #10725 - run ping check as anonymous admin (jsherril@redhat.com)
- fixes #10459,#10435 - do not create a puppet env for cvs with no modules
  (jsherril@redhat.com)
- Fixes #10824 - Refactoring errata index to show available errata using a url
  parameter. This is part of the conversion to scoped search for the
  filter_rules. By using a url parameter, the available errata is shown using
  the index of errata, which will make scoped search easier to implement.
  (jomitsch@redhat.com)
- fixes #10871 - Loads product content tab on content host, BZ1230782
  (cfouant@redhat.com)
- Fixes #10857: Ensure DestroyMedium filename and action name are the same.
  (ericdhelms@gmail.com)
- Fixes #10827: replace usages of deprecated bst-infinite-scroll.
  (walden@redhat.com)
  (david@memorious.net)
- fixes #10536 - changes 404 exceptions from error to info, BZ1136081
  (cfouant@redhat.com)
- Fixes #10822 - Don't clean up env content during CV remove
  (daviddavis@redhat.com)
- fixes #10820 - collect tasks dump with foreman-debug (jsherril@redhat.com)
- refs #7162 - fixing capsule sync timeout (jsherril@redhat.com)
- Fixes #10732: Remove attributes from user and use admin for remote calls.
  (ericdhelms@gmail.com)
- fixes #10735 - remove default and custom info (stbenjam@redhat.com)
- Fixes #10809: Remove unused doc/ directory. (ericdhelms@gmail.com)
- Fixes #10810: Remove unused public/ directory. (ericdhelms@gmail.com)
  (mmccune@gmail.com)
- Fixes #10804 - Fixing full_path for docker repos BZ1230777
  (daviddavis@redhat.com)
- Fixes #10798: fix overlap of CVV repository selector BZ 1228390.
  (walden@redhat.com)
  (jlsherrill@gmail.com)
- Fixes #10790 - Package groups aren't listed in content view package group
  filter rules (jomitsch@redhat.com)
- Fixes #10786: remove content dashboard settings button, BZ 1225949.
  (walden@redhat.com)
- Refs #7096 - rename the model in seeds (mhulan@redhat.com)
- fixes #10725 - adding backend check prior during plan of some actions
  (jsherril@redhat.com)
- Fixes #10775: only show one message for CVV page BZ 1230408.
  (walden@redhat.com)
- Fixes #10774: fix content host errata results BZ 1228316. (walden@redhat.com)
- Fixes #10724 - Peppier katello:reindex (paji@redhat.com)
- Fixes #10640: only show one repo per CVV BZ 1223699. (walden@redhat.com)
  (thomasmckay@redhat.com)
- refs #10655 - fixing a couple more issues with org delete
  (jsherril@redhat.com)
- fixes #8586 - fixing race condition on errata index (jsherril@redhat.com)
- Fixes #7162 - timeout capsule sync task (dtsang@redhat.com)
- Fixes #10671 - Fix upload on gpg_key BZ1204602 (sloranz@xantham.com)
- fixes #10719 - removed extra unused arg to import_products_from_cp
  (thomasmckay@redhat.com)
- fixes #10718 - correctly show repos (thomasmckay@redhat.com)
- Fixes #10681:  show correct installable count BZ 1226997. (walden@redhat.com)
- Fixes #10742: Remove legacy User Notice and Notices. (ericdhelms@gmail.com)
- Fixes #10601: Destroy installation media when repository is destroyed.
  (ericdhelms@gmail.com)
- Fixes #10697 - Improved CP SetContent add/delete logic (paji@redhat.com)
- Fixes #10705: fix errata CH installable filter BZ 1228292.
  (walden@redhat.com)
- Fixes #10704: correct text on errata confirm page, BZ 1228281.
  (walden@redhat.com)
- Fixes #10551 - Add scoped search for content view version by version and
  repository (jomitsch@redhat.com)
- Fixes #10585: Migrate to custom logging now in Foreman core.
  (ericdhelms@gmail.com)
- fixes #10696 - Fixes org creation error from 500 to 422 (cfouant@redhat.com)
- fixes #10690 - fixing possible race condition with creating operatingsystems
  (jsherril@redhat.com)
- Refs #7096 - Fix migration and tests using old model (mhulan@redhat.com)
- Fixes #10734: Remove unused/legacy search history and search favorites.
  (ericdhelms@gmail.com)
- fixes #10572 - send e-mail to all subscribers (stbenjam@redhat.com)
  (walden@redhat.com)
- Fixes #10631: hide errata confirm if no errata IDs BZ 1223963.
  (walden@redhat.com)
- Fixes #10622 - Fixes javascript traceback when removing repositories
  (aruzicka@redhat.com)
- fixes #10669 - Fixes issue with actkey name not updating, BZ1221685
  (cfouant@redhat.com)
- fixes #10655 - fix organization delete (jsherril@redhat.com)
- Fixes #10733: Remove Katello help tips. (ericdhelms@gmail.com)
- Fixes #10381 - reduce #queries on products page (dtsang@redhat.com)
  (thomasmckay@redhat.com)
- fixes #10351 - Fixes issue with CVV restrictive promotion sequence in UI,
  BZ1169876 (cfouant@redhat.com)
- Fixes #10593: Log message instead of failing when no mail recipients.
  (ericdhelms@gmail.com)
  (jlsherrill@gmail.com)
- fixes #10281 - do not display inaccessible red hat repos for enable
  (thomasmckay@redhat.com)
- fixes #10537 - Fixes toggle issue when switching between subscription panes
  on content host, BZ1207488 (cfouant@redhat.com)
- fixes #10569 - convert products to scoped search (jsherril@redhat.com)
- Fixes #10620 - Repos no longer protected by default (paji@redhat.com)
- Fixes #10617: don't use scroll on unpaged tables BZ 1223968.
  (walden@redhat.com)
- fixes 10598 - hammer content-host errata list failed, BZ1223926
  (komidore64@gmail.com)
- fixes #10614 - omit device network option on el5 kickstart
  (jsherril@redhat.com)
  (david@memorious.net)
- Fixes #10590 : The product help message should not reference a repository
  (bkearney@redhat.com)
- Fixes #10588: Fix typo that broke listing puppet modules for a version.
  (ericdhelms@gmail.com)
- Fixes #10575: add available content to AK products index BZ 1223743.
  (walden@redhat.com)
- fixes #10570 - removing provider elasticsearch (jsherril@redhat.com)
- Fixes #9924 - Fixing content view history bug in elasticsearch
  (daviddavis@redhat.com)
- fixes #10428 - katello-service and related scripts shouldn't be symlinks
  (stbenjam@redhat.com)
  (david@memorious.net)
- Fixes #10014 - Move version api to scoped search BZ1192162
  (daviddavis@redhat.com)
- Fixes #10498: Content view comparison wasn't showing repositories.
  (ericdhelms@gmail.com)
- fixes #10489 - adding two timeouts for content tasks (jsherril@redhat.com)
- Fixes #10540: correct product link on errata repo page BZ 1222660.
  (walden@redhat.com)
- fixes #10536 - Removes traceback from successful CH registration, BZ1136081
  (cfouant@redhat.com)
- Fixes #10525: remove unnecessary reference to tipsy, BZ 1222135.
  (walden@redhat.com)
- fixes #10523 - use admin user for facts updating (jsherril@redhat.com)
  (thomasmckay@redhat.com)
- fixes #10514 - handle case where content host no longer exists
  (thomasmckay@redhat.com)
- fixes #10495 - create custom products with metadata_expire set to 1
  (jsherril@redhat.com)
  (david@memorious.net)
  (thomasmckay@redhat.com)
- Fixes #10488: Ensure ID exists when environment details are loaded.
  (ericdhelms@gmail.com)
- Fixes #10381 - reduce #queries on products page (dtsang@redhat.com)
- Fixes #10152 - reduce num querys in sys#index (dtsang@redhat.com)
- fixes #10484 - use virt-who rhsm user for hypervisor checkin
  (thomasmckay@redhat.com)
- Fixes #10388 - Removing license header from remaining files
  (daviddavis@redhat.com)
- Refs #10388 - Removing license header from js test files
  (daviddavis@redhat.com)
- Refs #10388 - Remove license from javascript non-test files
  (daviddavis@redhat.com)
  (thomasmckay@redhat.com)
- Refs #10473 - remove prior option from environment update
  (jsherril@redhat.com)
- Fixes #10455: Validate the presence of the composite field as a boolean.
  (ericdhelms@gmail.com)
- fixes #8698 - migrate content view filters to scoped search
  (jsherril@redhat.com)
- fixes #10428 - katello-service package should actually have katello-service
  (stbenjam@redhat.com)
- fixes #10422 - send hash to capsule sync plan as expected
  (stbenjam@redhat.com)
- Fixes #9327: Update to Bastion 1.X and fix for eslint. (ericdhelms@gmail.com)
- Fixes #8692: Move content views to scoped search. (ericdhelms@gmail.com)
  (eric.d.helms@gmail.com)
- Fixes #10426: Ensure content host exists before updating in migration.
  (ericdhelms@gmail.com)
- fixes #10424 - remove required flag from content host update params
  (thomasmckay@redhat.com)
- Fixes #10308: prevent ISE on errata content hosts page BZ1216200.
  (walden@redhat.com)
- Refs #10388 - Removing license header from test folder
  (daviddavis@redhat.com)
  (david@memorious.net)
- Refs #10388 - Removing license header from other app folders
  (daviddavis@redhat.com)
  (thomasmckay@redhat.com)
  (david@memorious.net)
- Refs #10388 - Removing license header from ruby model files
  (daviddavis@redhat.com)
- Refs #10388 - Removing license header from spec, actions, config, lib
  (daviddavis@redhat.com)
- fixes #10396 - display better errors on repo metadata sync fail
  (jsherril@redhat.com)
- Fixes #10383: change errata issued/updated columns to date, BZ1215756.
  (walden@redhat.com)
- Fixes #10257: Connect capsule and its content host at the DB level.
  (ericdhelms@gmail.com)
- Fixes #10227: remove tipsy to fix tooltip issues, BZ 1213556.
  (walden@redhat.com)
- fixes #10331 - fix assocation from lifecycle environment to hosts
  (stbenjam@redhat.com)
- Refs #10224 - release python-isodate for fedoras (jsherril@redhat.com)
- fixes #6781 - provide a way to restart capsule services (stbenjam@redhat.com)
- Fixes #10309: prevent ISE on CH bulk actions errata BZ1216195.
  (walden@redhat.com)
  (inecas@redhat.com)
- Fixes #10249 - treat canceled tasks as errors (inecas@redhat.com)
- fixes #10229 - centralizing and isolating capsule communication
  (jsherril@redhat.com)
- Fixes #10258: hide "published at" section if puppet BZ 1131940.
  (walden@redhat.com)
- Refs #10224 - updating comps for f20, f21 (jsherril@redhat.com)
- fixes #10246 - hypervisors do not have pulp record (thomasmckay@redhat.com)
- Fixes #5684: cancel repository discovery is now dynflowed
  (oprazak@redhat.com)
- fixes #10225 - handle candlepin events cleanly (thomasmckay@redhat.com)
- fixes #10218 - incorrect usage of subscription guest host uuid
  (thomasmckay@redhat.com)
  (thomasmckay@redhat.com)
- fixes #9655 - reindex content hosts and ignore warnings
  (thomasmckay@redhat.com)
- Fixes #10185: Lock openjdk to less than 1.8.0.45. (ericdhelms@gmail.com)
  (thomasmckay@redhat.com)
- fixes #10144 - pass last-checkin time through to candlepin
  (thomasmckay@redhat.com)
- Fixes #10149: Distribute katello-client-repos RPM in client repos.
  (ericdhelms@gmail.com)
- Fixes #9867: Update katello-remove for latest packages.
  (ericdhelms@gmail.com)
- Fixes #8544: Carry subscription-manager for EL5 in our client repos.
  (ericdhelms@gmail.com)
- Fixes #10140: allow sync plans start date to be editable, BZ 1177901.
  (walden@redhat.com)
- Fixes #10132: Allow viewer role to view content dashboard.
  (ericdhelms@gmail.com)
- fixes #10127 - remove dynflow stacktrace when unregistering, BZ 1208100
  (komidore64@gmail.com)
- Fixes #9818: Properly propogate enabled state for sync plans to Pulp.
  (ericdhelms@gmail.com)
- fixes #9354 - fixing error with import_errata rake task (jsherril@redhat.com)
- Fixes #10006: Host collections can be listed on AK key page again.
  (ericdhelms@gmail.com)
- Fixes #9915: Backend cleanup script handles uebercert and hypervisors.
  (ericdhelms@gmail.com)
- Fixes #9929: Errata parameter was improperly named for repositories.
  (ericdhelms@gmail.com)
- fixes #10028 - Fixes issue with enabling non-yum repos (cfouant@redhat.com)
- fixes #9951 - fixing package update during inc update (jsherril@redhat.com)
- fixes #10012 - properly display conent host tasks (jsherril@redhat.com)
- Fixes #10011: fix long URI error when applying errata BZ 1208678.
  (walden@redhat.com)
- fixes #9984 - remove required flag from DELETE /subscriptions apipie
  (thomasmckay@redhat.com)
- Fixes #9933: use correct param for search BZ1205855. (walden@redhat.com)
- fixes #9786 - fixing searching and adding pagination to hosts errata
  (jsherril@redhat.com)
- Fixes #9992: fix no rows message on errata CH page BZ 1208216.
  (walden@redhat.com)
- Refs #9979: Other tests were not setting User.current when they should.
  (ericdhelms@gmail.com)
- Fixes #9968: Remove unused kill commands and cleanup script.
  (ericdhelms@gmail.com)
- Fixes #9978 - Sets an env content id correctly in cp (paji@redhat.com)
- Fixes #9986: Lock 'logging' gem to 1.X (ericdhelms@gmail.com)
- Fixes #9979: Set User.current in Organization spec tests.
  (ericdhelms@gmail.com)
- fixes #9935 - pass correct id to install errata for inc updates
  (jsherril@redhat.com)
- fixes #9923 - replaced Author column with Description in cv versions
  (thomasmckay@redhat.com)
- Fixes #9934: do not refresh errata on initial load BZ 1206704.
  (walden@redhat.com)
- Fixes #9927:  add missing no row messages, BZ 1206611. (walden@redhat.com)
- fixes #9922 - typo in subscription-products.html (thomasmckay@redhat.com)
- fixes #9889 - hides delete option when values are nil, BZ1186514
  (cfouant@redhat.com)
- fixes #9914 - fixing uninitialized constant error on incremental update
  (jsherril@redhat.com)
- Fixes #9913: ensure unique count on errata CH counts, BZ1206329.
  (walden@redhat.com)
- Fixes #9902 - Updated incorrect cv association (paji@redhat.com)
  (david@memorious.net)
- fixes #9899 - reindex all org subscriptions during manifest destroy
  (jsherril@redhat.com)
- Fixes #9866: Properly remove Pulp sync schedule from products.
  (ericdhelms@gmail.com)
- Fixes #9890 - Add content_view_id to systems API (daviddavis@redhat.com)
- fixes #9898 - Activation Key hint more explicit in registration page,
  BZ1201425 (cfouant@redhat.com)
- fixes #9876 - Adds product content override values to act key API, BZ1180282
  (cfouant@redhat.com)
- refs #8477 - remove defaulting of foreman templates (stbenjam@redhat.com)
  (david@memorious.net)
- Fixes #9887: remove search on activation key show, BZ1204929.
  (walden@redhat.com)
- fixes #9883 - making auto attach run after consumer update
  (jsherril@redhat.com)
- refs #9628 - change prior to prior_id, BZ1189478 (komidore64@gmail.com)
- Fixes #9872: Properly destroy systems that are of type Hypervisor.
  (ericdhelms@gmail.com)
  (david@memorious.net)
- Fixes #9839: show no rows message if table isn't working BZ 1203851.
  (walden@redhat.com)
- fixes #9478 - update system env and cv in candlepin on cv remove
  (jsherril@redhat.com)
- fixes #9802 - convert system bulk errata action to dynflow
  (jsherril@redhat.com)
- Fixes #9838 - additional pkgs for .30 qpid (dtsang@redhat.com)
- Fixes #9423 - Fix updating of docker upstream name (daviddavis@redhat.com)
- Fixes #9755 - Adding docker_images method to cvv (daviddavis@redhat.com)
- fixes #9799 - changing structure of incremental update around composites
  (jsherril@redhat.com)
- Fixes #9069 - support mrg31 (jmontleo@redhat.com)
- Fixes #9796: fix translations for subscription loading screens.
  (walden@redhat.com)
  (eric.d.helms@gmail.com)
- fixes #9798 - don't plan CVPE deletion if this is the default version,
  BZ1076568 (komidore64@gmail.com)
  (eric.d.helms@gmail.com)
- Fixes #9608: correct repository count, BZ 1197836. (walden@redhat.com)
- fixes #9792 - unregister content host UI modal blank (thomasmckay@redhat.com)
- fixes #9790 - Adds tool-tip to actkey UI upon env selection
  (cfouant@redhat.com)
- Fixes #9783:  ensure errata on dashboard are unique, BZ 1187704.
  (walden@redhat.com)
  (thomasmckay@redhat.com)
- Refs #4478 - API localization - Apipie setup moved
  (martin.bacovsky@gmail.com)
- Fixes #9737: fix CH filter for incremental update, BZ 1200441.
  (walden@redhat.com)
- fixes #9750 - always reindex errata packages (jsherril@redhat.com)
- fixes #9722 - recognize and show errors on host content actions
  (jsherril@redhat.com)
- Fixes #9741 - Fixed a puppet module count error in a CVV (paji@redhat.com)
- fixes #9739 - replace reference to delete_products w/ destroy_products
  permission (thomasmckay@redhat.com)
- Fixes #9730: show message when no CV versions exist, BZ1201410.
  (walden@redhat.com)
- Fixes #9658: correct CH count when applying errata, BZ1198815.
  (walden@redhat.com)
- Fixes #9735: Fix package/puppet module incremental update.
  (ericdhelms@gmail.com)
- Fixes #9732: Incorrect apiepie docs for incremental update.
  (ericdhelms@gmail.com)
- Fixes #9731: show success/error messages when updating filter, BZ1201406.
  (walden@redhat.com)
- Fixes #9697: hide confirmation after bulk action or cancel, BZ 1199584.
  (walden@redhat.com)
- Refs #9518, #9310 - Create containers in API using katello repos
  (paji@redhat.com)
- Fixes #9707: Cleanup requirement on rubygems-devel. (ericdhelms@gmail.com)
- fixes #9566 - only destroy repo in finalize for direct repo deletes
  (jsherril@redhat.com)
- Refs #8710 - katello-debug script is no longer a symlink
  (lzap+git@redhat.com)
- Fixes #9698: use correct styling for association tables, BZ 1199626.
  (walden@redhat.com)
  (thomasmckay@redhat.com)
- Fixes #9586: Content view comparison will provide results again.
  (ericdhelms@gmail.com)
- fixes #9681 - simplify presented content override choices
  (thomasmckay@redhat.com)
  (thomasmckay@redhat.com)
- Fixes #9688 - Uses cdn url scheme for docker repo feeds (paji@redhat.com)
- Fixes #9583: improve repository deletion responses BZ 1166365.
  (walden@redhat.com)
- Fixes #9685: Allow searching on capital letters for Packages in CS.
  (ericdhelms@gmail.com)
- Fixes #8570: Show modal dialog before deletion. (ericdhelms@gmail.com)
- Fixes #9580: fix N+1 queries on activation key list, BZ 1196742.
  (walden@redhat.com)
- fixes #7354 - corrected state permission for import manifest
  (thomasmckay@redhat.com)
- Fixes #9670: show applicable errata message on CH errata page, BZ1194773.
  (walden@redhat.com)
- fixes #9664 - Add links to sync errata mail header (stbenjam@redhat.com)
- refs #9637 - add python-amqp to client repos (jsherril@redhat.com)
  (thomasmckay@redhat.com)
- fixes #9647 - speed up puppet class import (jsherril@redhat.com)
- Fixes #8689 - scoped search for host collection (sloranz@xantham.com)
- fixes #9646 - call dynflow to update facts sent via rhsm and virt-who
  (thomasmckay@redhat.com)
- Fixes #9610 - Docker Content now hidden for composite cv (paji@redhat.com)
  (thomasmckay@redhat.com)
  (stephen@bitbin.de)
- fixes #9637 - adding qpid-proton-c to client repos (jsherril@redhat.com)
- fixes #9360 - set feature flag host collection actions
  (thomasmckay@redhat.com)
  (stephen@bitbin.de)
- fixes #9629 - fix env delete, as it no longer needs indexing
  (jsherril@redhat.com)
- Fixes #9511: fix typo on manifest update page. (walden@redhat.com)
- fixes #9626 - sort package names on incremental update task details
  (jsherril@redhat.com)
  (thomasmckay@redhat.com)
  (david@memorious.net)
- fixes #9622 - remove unused product rabl attribute (jsherril@redhat.com)
- refs #8175 - require qpid-dispatch-router (stbenjam@redhat.com)
  (jlsherrill@gmail.com)
- fixes #9587 - remove model reloading from tests (jsherril@redhat.com)
- fixes #9462,#9557,#9556 - various inherited hostgroup issues
  (jsherril@redhat.com)
- Fixes #9608 add repository/puppet module to CV components BZ 1197836.
  (walden@redhat.com)
- Fixes #9582: display content tab after content view is loaded BZ1196720.
  (walden@redhat.com)
- fixes #9577 - fixing host single and bulk delete (jsherril@redhat.com)
- Fixes #9344 - Changing descriptions to text fields BZ1177158
  (daviddavis@redhat.com)
- fixes #9585 - speed up enabling redhat repos (jsherril@redhat.com)
- fixes #9502, #9503 - verify errata exist before application
  (stbenjam@redhat.com)
- Fixes #9579: Limit bastion to less than 1.0.0 (ericdhelms@gmail.com)
- Fixes #7796 - Enable docker repos from the CDN (paji@redhat.com)
- Fixes #8964: Show repository count for composite content views.
  (ericdhelms@gmail.com)
- Fixes #9345: fix content view promotion in IE, BZ1168457. (walden@redhat.com)
- Fixes #9376: Calculate next_sync time properly based on UTC.
  (ericdhelms@gmail.com)
- Fixes #9564: limit components rabl to fix N+1 queries, BZ 1177609.
  (walden@redhat.com)
- fixes #9521 - activate and deactivate pulp nodes (jsherril@redhat.com)
- Fixes #9534: fix N+1 queries on content view index. (walden@redhat.com)
- Fixes #9554: Fix broken package display on content search.
  (ericdhelms@gmail.com)
  (cfouant@redhat.com)
  (cfouant@redhat.com)
- refs #8175 - add new proton/dispatcher packages to comps
  (jsherril@redhat.com)
  (david@memorious.net)
- fixes #8728, #8756 - use capsule RPM for registering a content host
  (stbenjam@redhat.com)
- Automatic commit of package [katello] release [2.3.0-1].
  (ericdhelms@gmail.com)
- Update katello to 2.3.0 (ericdhelms@gmail.com)
- Fixes #9539 - Remove unused erroneous file (daviddavis@redhat.com)
- fixes #9405 - Attaches custom products when registering with activation key
  (cfouant@redhat.com)
- refs #8175 - add qpid dispatch router to services list (stbenjam@redhat.com)
- fixes #8956, #9337 - remove unused scripts and files from specfile
  (mmccune@redhat.com)
- fixes #9422 - limit 24 hour guest subscription visibility
  (thomasmckay@redhat.com)
- fixes #8892, #9340 - Validates content label and override value, BZ1173723,
  BZ1187750 (cfouant@redhat.com)
- Fixes #9400 - configure networking in finish template (mhulan@redhat.com)
- Fixes #9132 - use networking snippet during provisioning (mhulan@redhat.com)
- refs #8861 - adding layout_helper to use trunc with tooltip helper
  (orabin@redhat.com)

* Mon Jul 06 2015 Stephen Benjamin <stbenjam@redhat.com>
- adding myself to contrib (chrobert@redhat.com)
- Refs #10962 - limit foreman tasks in rpm specs to < 0.7.0 (inecas@redhat.com)
- Fixes #10830 - Humanized state description for Pulp and Candlepin async
  actions (inecas@redhat.com)
  (jlsherrill@gmail.com)
- fixes #10934 - per-page/page options for puppet-module list, BZ1202050
  (komidore64@gmail.com)
- Fixes #10904: fix errata CH selection, BZ 1233901. (walden@redhat.com)
- fixes #10903 - remove reference to non-existent methods
  (thomasmckay@redhat.com)
- Fixes #10705: filter out non-installable Systems BZ1228292.
  (walden@redhat.com)
- fixes #10901 - skip all errors on sync tasks (jsherril@redhat.com)
- fixes #8690 - converting repository to scoped search (jsherril@redhat.com)
- fixes #10886 - adding more conditions for readable repos
  (jsherril@redhat.com)
- Fixes #8693: Convert content view puppet module to scoped search.
  (ericdhelms@gmail.com)
- refs #10725 - run ping check as anonymous admin (jsherril@redhat.com)
- fixes #10459,#10435 - do not create a puppet env for cvs with no modules
  (jsherril@redhat.com)
- Fixes #10824 - Refactoring errata index to show available errata using a url
  parameter. This is part of the conversion to scoped search for the
  filter_rules. By using a url parameter, the available errata is shown using
  the index of errata, which will make scoped search easier to implement.
  (jomitsch@redhat.com)
- fixes #10871 - Loads product content tab on content host, BZ1230782
  (cfouant@redhat.com)
- Fixes #10857: Ensure DestroyMedium filename and action name are the same.
  (ericdhelms@gmail.com)
- Fixes #10827: replace usages of deprecated bst-infinite-scroll.
  (walden@redhat.com)
  (david@memorious.net)
- fixes #10536 - changes 404 exceptions from error to info, BZ1136081
  (cfouant@redhat.com)
- Fixes #10822 - Don't clean up env content during CV remove
  (daviddavis@redhat.com)
- fixes #10820 - collect tasks dump with foreman-debug (jsherril@redhat.com)
- refs #7162 - fixing capsule sync timeout (jsherril@redhat.com)
- Fixes #10732: Remove attributes from user and use admin for remote calls.
  (ericdhelms@gmail.com)
- fixes #10735 - remove default and custom info (stbenjam@redhat.com)
- Fixes #10809: Remove unused doc/ directory. (ericdhelms@gmail.com)
- Fixes #10810: Remove unused public/ directory. (ericdhelms@gmail.com)
  (mmccune@gmail.com)
- Fixes #10804 - Fixing full_path for docker repos BZ1230777
  (daviddavis@redhat.com)
- Fixes #10798: fix overlap of CVV repository selector BZ 1228390.
  (walden@redhat.com)
  (jlsherrill@gmail.com)
- Fixes #10790 - Package groups aren't listed in content view package group
  filter rules (jomitsch@redhat.com)
- Fixes #10786: remove content dashboard settings button, BZ 1225949.
  (walden@redhat.com)
- Refs #7096 - rename the model in seeds (mhulan@redhat.com)
- fixes #10725 - adding backend check prior during plan of some actions
  (jsherril@redhat.com)
- Fixes #10775: only show one message for CVV page BZ 1230408.
  (walden@redhat.com)
- Fixes #10774: fix content host errata results BZ 1228316. (walden@redhat.com)
- Fixes #10724 - Peppier katello:reindex (paji@redhat.com)
- Fixes #10640: only show one repo per CVV BZ 1223699. (walden@redhat.com)
  (thomasmckay@redhat.com)
- refs #10655 - fixing a couple more issues with org delete
  (jsherril@redhat.com)
- fixes #8586 - fixing race condition on errata index (jsherril@redhat.com)
- Fixes #7162 - timeout capsule sync task (dtsang@redhat.com)
- Fixes #10671 - Fix upload on gpg_key BZ1204602 (sloranz@xantham.com)
- fixes #10719 - removed extra unused arg to import_products_from_cp
  (thomasmckay@redhat.com)
- fixes #10718 - correctly show repos (thomasmckay@redhat.com)
- Fixes #10681:  show correct installable count BZ 1226997. (walden@redhat.com)
- Fixes #10742: Remove legacy User Notice and Notices. (ericdhelms@gmail.com)
- Fixes #10601: Destroy installation media when repository is destroyed.
  (ericdhelms@gmail.com)
- Fixes #10697 - Improved CP SetContent add/delete logic (paji@redhat.com)
- Fixes #10705: fix errata CH installable filter BZ 1228292.
  (walden@redhat.com)
- Fixes #10704: correct text on errata confirm page, BZ 1228281.
  (walden@redhat.com)
- Fixes #10551 - Add scoped search for content view version by version and
  repository (jomitsch@redhat.com)
- Fixes #10585: Migrate to custom logging now in Foreman core.
  (ericdhelms@gmail.com)
- fixes #10696 - Fixes org creation error from 500 to 422 (cfouant@redhat.com)
- fixes #10690 - fixing possible race condition with creating operatingsystems
  (jsherril@redhat.com)
- Refs #7096 - Fix migration and tests using old model (mhulan@redhat.com)
- Fixes #10734: Remove unused/legacy search history and search favorites.
  (ericdhelms@gmail.com)
- fixes #10572 - send e-mail to all subscribers (stbenjam@redhat.com)
  (walden@redhat.com)
- Fixes #10631: hide errata confirm if no errata IDs BZ 1223963.
  (walden@redhat.com)
- Fixes #10622 - Fixes javascript traceback when removing repositories
  (aruzicka@redhat.com)
- fixes #10669 - Fixes issue with actkey name not updating, BZ1221685
  (cfouant@redhat.com)
- fixes #10655 - fix organization delete (jsherril@redhat.com)
- Fixes #10733: Remove Katello help tips. (ericdhelms@gmail.com)
- Fixes #10381 - reduce #queries on products page (dtsang@redhat.com)
  (thomasmckay@redhat.com)
- fixes #10351 - Fixes issue with CVV restrictive promotion sequence in UI,
  BZ1169876 (cfouant@redhat.com)
- Fixes #10593: Log message instead of failing when no mail recipients.
  (ericdhelms@gmail.com)
  (jlsherrill@gmail.com)
- fixes #10281 - do not display inaccessible red hat repos for enable
  (thomasmckay@redhat.com)
- fixes #10537 - Fixes toggle issue when switching between subscription panes
  on content host, BZ1207488 (cfouant@redhat.com)
- fixes #10569 - convert products to scoped search (jsherril@redhat.com)
- Fixes #10620 - Repos no longer protected by default (paji@redhat.com)
- Fixes #10617: don't use scroll on unpaged tables BZ 1223968.
  (walden@redhat.com)
- fixes 10598 - hammer content-host errata list failed, BZ1223926
  (komidore64@gmail.com)
- fixes #10614 - omit device network option on el5 kickstart
  (jsherril@redhat.com)
  (david@memorious.net)
- Fixes #10590 : The product help message should not reference a repository
  (bkearney@redhat.com)
- Fixes #10588: Fix typo that broke listing puppet modules for a version.
  (ericdhelms@gmail.com)
- Fixes #10575: add available content to AK products index BZ 1223743.
  (walden@redhat.com)
- fixes #10570 - removing provider elasticsearch (jsherril@redhat.com)
- Fixes #9924 - Fixing content view history bug in elasticsearch
  (daviddavis@redhat.com)
- fixes #10428 - katello-service and related scripts shouldn't be symlinks
  (stbenjam@redhat.com)
  (david@memorious.net)
- Fixes #10014 - Move version api to scoped search BZ1192162
  (daviddavis@redhat.com)
- Fixes #10498: Content view comparison wasn't showing repositories.
  (ericdhelms@gmail.com)
- fixes #10489 - adding two timeouts for content tasks (jsherril@redhat.com)
- Fixes #10540: correct product link on errata repo page BZ 1222660.
  (walden@redhat.com)
- fixes #10536 - Removes traceback from successful CH registration, BZ1136081
  (cfouant@redhat.com)
- Fixes #10525: remove unnecessary reference to tipsy, BZ 1222135.
  (walden@redhat.com)
- fixes #10523 - use admin user for facts updating (jsherril@redhat.com)
  (thomasmckay@redhat.com)
- fixes #10514 - handle case where content host no longer exists
  (thomasmckay@redhat.com)
- fixes #10495 - create custom products with metadata_expire set to 1
  (jsherril@redhat.com)
  (david@memorious.net)
  (thomasmckay@redhat.com)
- Fixes #10488: Ensure ID exists when environment details are loaded.
  (ericdhelms@gmail.com)
- Fixes #10381 - reduce #queries on products page (dtsang@redhat.com)
- Fixes #10152 - reduce num querys in sys#index (dtsang@redhat.com)
- fixes #10484 - use virt-who rhsm user for hypervisor checkin
  (thomasmckay@redhat.com)
- Fixes #10388 - Removing license header from remaining files
  (daviddavis@redhat.com)
- Refs #10388 - Removing license header from js test files
  (daviddavis@redhat.com)
- Refs #10388 - Remove license from javascript non-test files
  (daviddavis@redhat.com)
  (thomasmckay@redhat.com)
- Refs #10473 - remove prior option from environment update
  (jsherril@redhat.com)
- Fixes #10455: Validate the presence of the composite field as a boolean.
  (ericdhelms@gmail.com)
- fixes #8698 - migrate content view filters to scoped search
  (jsherril@redhat.com)
- fixes #10428 - katello-service package should actually have katello-service
  (stbenjam@redhat.com)
- fixes #10422 - send hash to capsule sync plan as expected
  (stbenjam@redhat.com)
- Fixes #9327: Update to Bastion 1.X and fix for eslint. (ericdhelms@gmail.com)
- Fixes #8692: Move content views to scoped search. (ericdhelms@gmail.com)
  (eric.d.helms@gmail.com)
- Fixes #10426: Ensure content host exists before updating in migration.
  (ericdhelms@gmail.com)
- fixes #10424 - remove required flag from content host update params
  (thomasmckay@redhat.com)
- Fixes #10308: prevent ISE on errata content hosts page BZ1216200.
  (walden@redhat.com)
- Refs #10388 - Removing license header from test folder
  (daviddavis@redhat.com)
  (david@memorious.net)
- Refs #10388 - Removing license header from other app folders
  (daviddavis@redhat.com)
  (thomasmckay@redhat.com)
  (david@memorious.net)
- Refs #10388 - Removing license header from ruby model files
  (daviddavis@redhat.com)
- Refs #10388 - Removing license header from spec, actions, config, lib
  (daviddavis@redhat.com)
- fixes #10396 - display better errors on repo metadata sync fail
  (jsherril@redhat.com)
- Fixes #10383: change errata issued/updated columns to date, BZ1215756.
  (walden@redhat.com)
- Fixes #10257: Connect capsule and its content host at the DB level.
  (ericdhelms@gmail.com)
- Fixes #10227: remove tipsy to fix tooltip issues, BZ 1213556.
  (walden@redhat.com)
- fixes #10331 - fix assocation from lifecycle environment to hosts
  (stbenjam@redhat.com)
- Refs #10224 - release python-isodate for fedoras (jsherril@redhat.com)
- fixes #6781 - provide a way to restart capsule services (stbenjam@redhat.com)
- Fixes #10309: prevent ISE on CH bulk actions errata BZ1216195.
  (walden@redhat.com)
  (inecas@redhat.com)
- Fixes #10249 - treat canceled tasks as errors (inecas@redhat.com)
- fixes #10229 - centralizing and isolating capsule communication
  (jsherril@redhat.com)
- Fixes #10258: hide "published at" section if puppet BZ 1131940.
  (walden@redhat.com)
- Refs #10224 - updating comps for f20, f21 (jsherril@redhat.com)
- fixes #10246 - hypervisors do not have pulp record (thomasmckay@redhat.com)
- Fixes #5684: cancel repository discovery is now dynflowed
  (oprazak@redhat.com)
- fixes #10225 - handle candlepin events cleanly (thomasmckay@redhat.com)
- fixes #10218 - incorrect usage of subscription guest host uuid
  (thomasmckay@redhat.com)
  (thomasmckay@redhat.com)
- fixes #9655 - reindex content hosts and ignore warnings
  (thomasmckay@redhat.com)
- Fixes #10185: Lock openjdk to less than 1.8.0.45. (ericdhelms@gmail.com)
  (thomasmckay@redhat.com)
- fixes #10144 - pass last-checkin time through to candlepin
  (thomasmckay@redhat.com)
- Fixes #10149: Distribute katello-client-repos RPM in client repos.
  (ericdhelms@gmail.com)
- Fixes #9867: Update katello-remove for latest packages.
  (ericdhelms@gmail.com)
- Fixes #8544: Carry subscription-manager for EL5 in our client repos.
  (ericdhelms@gmail.com)
- Fixes #10140: allow sync plans start date to be editable, BZ 1177901.
  (walden@redhat.com)
- Fixes #10132: Allow viewer role to view content dashboard.
  (ericdhelms@gmail.com)
- fixes #10127 - remove dynflow stacktrace when unregistering, BZ 1208100
  (komidore64@gmail.com)
- Fixes #9818: Properly propogate enabled state for sync plans to Pulp.
  (ericdhelms@gmail.com)
- fixes #9354 - fixing error with import_errata rake task (jsherril@redhat.com)
- Fixes #10006: Host collections can be listed on AK key page again.
  (ericdhelms@gmail.com)
- Fixes #9915: Backend cleanup script handles uebercert and hypervisors.
  (ericdhelms@gmail.com)
- Fixes #9929: Errata parameter was improperly named for repositories.
  (ericdhelms@gmail.com)
- fixes #10028 - Fixes issue with enabling non-yum repos (cfouant@redhat.com)
- fixes #9951 - fixing package update during inc update (jsherril@redhat.com)
- fixes #10012 - properly display conent host tasks (jsherril@redhat.com)
- Fixes #10011: fix long URI error when applying errata BZ 1208678.
  (walden@redhat.com)
- fixes #9984 - remove required flag from DELETE /subscriptions apipie
  (thomasmckay@redhat.com)
- Fixes #9933: use correct param for search BZ1205855. (walden@redhat.com)
- fixes #9786 - fixing searching and adding pagination to hosts errata
  (jsherril@redhat.com)
- Fixes #9992: fix no rows message on errata CH page BZ 1208216.
  (walden@redhat.com)
- Refs #9979: Other tests were not setting User.current when they should.
  (ericdhelms@gmail.com)
- Fixes #9968: Remove unused kill commands and cleanup script.
  (ericdhelms@gmail.com)
- Fixes #9978 - Sets an env content id correctly in cp (paji@redhat.com)
- Fixes #9986: Lock 'logging' gem to 1.X (ericdhelms@gmail.com)
- Fixes #9979: Set User.current in Organization spec tests.
  (ericdhelms@gmail.com)
- fixes #9935 - pass correct id to install errata for inc updates
  (jsherril@redhat.com)
- fixes #9923 - replaced Author column with Description in cv versions
  (thomasmckay@redhat.com)
- Fixes #9934: do not refresh errata on initial load BZ 1206704.
  (walden@redhat.com)
- Fixes #9927:  add missing no row messages, BZ 1206611. (walden@redhat.com)
- fixes #9922 - typo in subscription-products.html (thomasmckay@redhat.com)
- fixes #9889 - hides delete option when values are nil, BZ1186514
  (cfouant@redhat.com)
- fixes #9914 - fixing uninitialized constant error on incremental update
  (jsherril@redhat.com)
- Fixes #9913: ensure unique count on errata CH counts, BZ1206329.
  (walden@redhat.com)
- Fixes #9902 - Updated incorrect cv association (paji@redhat.com)
  (david@memorious.net)
- fixes #9899 - reindex all org subscriptions during manifest destroy
  (jsherril@redhat.com)
- Fixes #9866: Properly remove Pulp sync schedule from products.
  (ericdhelms@gmail.com)
- Fixes #9890 - Add content_view_id to systems API (daviddavis@redhat.com)
- fixes #9898 - Activation Key hint more explicit in registration page,
  BZ1201425 (cfouant@redhat.com)
- fixes #9876 - Adds product content override values to act key API, BZ1180282
  (cfouant@redhat.com)
- refs #8477 - remove defaulting of foreman templates (stbenjam@redhat.com)
  (david@memorious.net)
- Fixes #9887: remove search on activation key show, BZ1204929.
  (walden@redhat.com)
- fixes #9883 - making auto attach run after consumer update
  (jsherril@redhat.com)
- refs #9628 - change prior to prior_id, BZ1189478 (komidore64@gmail.com)
- Fixes #9872: Properly destroy systems that are of type Hypervisor.
  (ericdhelms@gmail.com)
  (david@memorious.net)
- Fixes #9839: show no rows message if table isn't working BZ 1203851.
  (walden@redhat.com)
- fixes #9478 - update system env and cv in candlepin on cv remove
  (jsherril@redhat.com)
- fixes #9802 - convert system bulk errata action to dynflow
  (jsherril@redhat.com)
- Fixes #9838 - additional pkgs for .30 qpid (dtsang@redhat.com)
- Fixes #9423 - Fix updating of docker upstream name (daviddavis@redhat.com)
- Fixes #9755 - Adding docker_images method to cvv (daviddavis@redhat.com)
- fixes #9799 - changing structure of incremental update around composites
  (jsherril@redhat.com)
- Fixes #9069 - support mrg31 (jmontleo@redhat.com)
- Fixes #9796: fix translations for subscription loading screens.
  (walden@redhat.com)
  (eric.d.helms@gmail.com)
- fixes #9798 - don't plan CVPE deletion if this is the default version,
  BZ1076568 (komidore64@gmail.com)
  (eric.d.helms@gmail.com)
- Fixes #9608: correct repository count, BZ 1197836. (walden@redhat.com)
- fixes #9792 - unregister content host UI modal blank (thomasmckay@redhat.com)
- fixes #9790 - Adds tool-tip to actkey UI upon env selection
  (cfouant@redhat.com)
- Fixes #9783:  ensure errata on dashboard are unique, BZ 1187704.
  (walden@redhat.com)
  (thomasmckay@redhat.com)
- Refs #4478 - API localization - Apipie setup moved
  (martin.bacovsky@gmail.com)
- Fixes #9737: fix CH filter for incremental update, BZ 1200441.
  (walden@redhat.com)
- fixes #9750 - always reindex errata packages (jsherril@redhat.com)
- fixes #9722 - recognize and show errors on host content actions
  (jsherril@redhat.com)
- Fixes #9741 - Fixed a puppet module count error in a CVV (paji@redhat.com)
- fixes #9739 - replace reference to delete_products w/ destroy_products
  permission (thomasmckay@redhat.com)
- Fixes #9730: show message when no CV versions exist, BZ1201410.
  (walden@redhat.com)
- Fixes #9658: correct CH count when applying errata, BZ1198815.
  (walden@redhat.com)
- Fixes #9735: Fix package/puppet module incremental update.
  (ericdhelms@gmail.com)
- Fixes #9732: Incorrect apiepie docs for incremental update.
  (ericdhelms@gmail.com)
- Fixes #9731: show success/error messages when updating filter, BZ1201406.
  (walden@redhat.com)
- Fixes #9697: hide confirmation after bulk action or cancel, BZ 1199584.
  (walden@redhat.com)
- Refs #9518, #9310 - Create containers in API using katello repos
  (paji@redhat.com)
- Fixes #9707: Cleanup requirement on rubygems-devel. (ericdhelms@gmail.com)
- fixes #9566 - only destroy repo in finalize for direct repo deletes
  (jsherril@redhat.com)
- Refs #8710 - katello-debug script is no longer a symlink
  (lzap+git@redhat.com)
- Fixes #9698: use correct styling for association tables, BZ 1199626.
  (walden@redhat.com)
  (thomasmckay@redhat.com)
- Fixes #9586: Content view comparison will provide results again.
  (ericdhelms@gmail.com)
- fixes #9681 - simplify presented content override choices
  (thomasmckay@redhat.com)
  (thomasmckay@redhat.com)
- Fixes #9688 - Uses cdn url scheme for docker repo feeds (paji@redhat.com)
- Fixes #9583: improve repository deletion responses BZ 1166365.
  (walden@redhat.com)
- Fixes #9685: Allow searching on capital letters for Packages in CS.
  (ericdhelms@gmail.com)
- Fixes #8570: Show modal dialog before deletion. (ericdhelms@gmail.com)
- Fixes #9580: fix N+1 queries on activation key list, BZ 1196742.
  (walden@redhat.com)
- fixes #7354 - corrected state permission for import manifest
  (thomasmckay@redhat.com)
- Fixes #9670: show applicable errata message on CH errata page, BZ1194773.
  (walden@redhat.com)
- fixes #9664 - Add links to sync errata mail header (stbenjam@redhat.com)
- refs #9637 - add python-amqp to client repos (jsherril@redhat.com)
  (thomasmckay@redhat.com)
- fixes #9647 - speed up puppet class import (jsherril@redhat.com)
- Fixes #8689 - scoped search for host collection (sloranz@xantham.com)
- fixes #9646 - call dynflow to update facts sent via rhsm and virt-who
  (thomasmckay@redhat.com)
- Fixes #9610 - Docker Content now hidden for composite cv (paji@redhat.com)
  (thomasmckay@redhat.com)
  (stephen@bitbin.de)
- fixes #9637 - adding qpid-proton-c to client repos (jsherril@redhat.com)
- fixes #9360 - set feature flag host collection actions
  (thomasmckay@redhat.com)
  (stephen@bitbin.de)
- fixes #9629 - fix env delete, as it no longer needs indexing
  (jsherril@redhat.com)
- Fixes #9511: fix typo on manifest update page. (walden@redhat.com)
- fixes #9626 - sort package names on incremental update task details
  (jsherril@redhat.com)
  (thomasmckay@redhat.com)
  (david@memorious.net)
- fixes #9622 - remove unused product rabl attribute (jsherril@redhat.com)
- refs #8175 - require qpid-dispatch-router (stbenjam@redhat.com)
  (jlsherrill@gmail.com)
- fixes #9587 - remove model reloading from tests (jsherril@redhat.com)
- fixes #9462,#9557,#9556 - various inherited hostgroup issues
  (jsherril@redhat.com)
- Fixes #9608 add repository/puppet module to CV components BZ 1197836.
  (walden@redhat.com)
- Fixes #9582: display content tab after content view is loaded BZ1196720.
  (walden@redhat.com)
- fixes #9577 - fixing host single and bulk delete (jsherril@redhat.com)
- Fixes #9344 - Changing descriptions to text fields BZ1177158
  (daviddavis@redhat.com)
- fixes #9585 - speed up enabling redhat repos (jsherril@redhat.com)
- fixes #9502, #9503 - verify errata exist before application
  (stbenjam@redhat.com)
- Fixes #9579: Limit bastion to less than 1.0.0 (ericdhelms@gmail.com)
- Fixes #7796 - Enable docker repos from the CDN (paji@redhat.com)
- Fixes #8964: Show repository count for composite content views.
  (ericdhelms@gmail.com)
- Fixes #9345: fix content view promotion in IE, BZ1168457. (walden@redhat.com)
- Fixes #9376: Calculate next_sync time properly based on UTC.
  (ericdhelms@gmail.com)
- Fixes #9564: limit components rabl to fix N+1 queries, BZ 1177609.
  (walden@redhat.com)
- fixes #9521 - activate and deactivate pulp nodes (jsherril@redhat.com)
- Fixes #9534: fix N+1 queries on content view index. (walden@redhat.com)
- Fixes #9554: Fix broken package display on content search.
  (ericdhelms@gmail.com)
  (cfouant@redhat.com)
  (cfouant@redhat.com)
- refs #8175 - add new proton/dispatcher packages to comps
  (jsherril@redhat.com)
  (david@memorious.net)
- fixes #8728, #8756 - use capsule RPM for registering a content host
  (stbenjam@redhat.com)
- Automatic commit of package [katello] release [2.3.0-1].
  (ericdhelms@gmail.com)
- Update katello to 2.3.0 (ericdhelms@gmail.com)
- Fixes #9539 - Remove unused erroneous file (daviddavis@redhat.com)
- fixes #9405 - Attaches custom products when registering with activation key
  (cfouant@redhat.com)
- refs #8175 - add qpid dispatch router to services list (stbenjam@redhat.com)
- fixes #8956, #9337 - remove unused scripts and files from specfile
  (mmccune@redhat.com)
- fixes #9422 - limit 24 hour guest subscription visibility
  (thomasmckay@redhat.com)
- fixes #8892, #9340 - Validates content label and override value, BZ1173723,
  BZ1187750 (cfouant@redhat.com)
- Fixes #9400 - configure networking in finish template (mhulan@redhat.com)
- Fixes #9132 - use networking snippet during provisioning (mhulan@redhat.com)
- refs #8861 - adding layout_helper to use trunc with tooltip helper
  (orabin@redhat.com)

* Tue Feb 24 2015 Eric D. Helms <ericdhelms@gmail.com> 2.3.0-1
- Version bump to 2.3.0 (ericdhelms@gmail.com)

* Tue Feb 24 2015 Eric D. Helms <ericdhelms@gmail.com> 2.2.0-2
- Fixes #9511: update manifest upload styling to bootstrap 3, BZ1194531
  (walden@redhat.com)
  (eric.d.helms@gmail.com)
- Fixed #9530 - installer logs are collected again by debug script
  (lzap+git@redhat.com)
- Fixes #8448: Add content tabs to environment details page.
  (ericdhelms@gmail.com)
- Fixes #9528: fix JS error on content host errata table, BZ 1195760.
  (walden@redhat.com)
- fixes #9525 - add array equality assertion methods (stbenjam@redhat.com)
- Fixes #9522: no row-select on tables without bulk actions, BZ 1173765.
  (walden@redhat.com)
- fixes #9467 - fix bulk errata apply list (jsherril@redhat.com)
- fixes #8954 - speeding up product rabl rendering (jsherril@redhat.com)
- katello-remove typo 'permanetly' -> 'permanently' (elobatocs@gmail.com)
- Fixes #8387: Redirect users back to 403 page if no current organization.
  (ericdhelms@gmail.com)
- Fixes #9484: fix bastion katello modal translations, BZ 1194691.
  (walden@redhat.com)
- Fixes #9474: display confirmation when applying errata to CH, BZ1160740.
  (walden@redhat.com)
- fixes #9402 - allow removal of cv version with archive deletion
  (jsherril@redhat.com)
- fixes #9404 - fix sync_plan add/del product action getting stuck
  (jsherril@redhat.com)
- Fixes #9471: fix JS error on content host errata page, BZ1194396
  (walden@redhat.com)
- Fixes #9464: fix typo on content host errata counts display, BZ 1179465.
  (walden@redhat.com)
  (cfouant@redhat.com)
  (jlsherrill@gmail.com)
- fixes #9455 - fixes validation error, BZ1139576 (cfouant@redhat.com)
- refs #9428 - fixing errata loading on the system tests (jsherril@redhat.com)
- fixes #9150 - reindex all distributions on indexing (jsherril@redhat.com)
- Fixes #7088: set filter rule to updated rule on save. (walden@redhat.com)
- Fixes #9431: Clear system_errata when pruning backend objects.
  (ericdhelms@gmail.com)
- fixes #9416 - content view update - dynflow'ize it (bbuckingham@redhat.com)
- fixes #9428 - fixing failing unit test (jsherril@redhat.com)
- fixes #9401 - refresh content view version list after deletion
  (jsherril@redhat.com)
  (david@memorious.net)
- Fixes #9421 - Removing products.json (daviddavis@redhat.com)
- ref #9179 - adding python-mongoengine for EL7 (mmccune@redhat.com)
- Fixes #9166: show message if incremental update in progress, BZ 1193185.
  (walden@redhat.com)
- Fixes #7694: Allow errata to be sorted by updated field.
  (ericdhelms@gmail.com)
- Fixes #8984: Remove sync plan from products when a sync plan is destroyed.
  (ericdhelms@gmail.com)
- fixes #9120 - better feedback around composites for inc updates
  (jsherril@redhat.com)
- fixes #9317 - only call foreman content update when needed
  (jsherril@redhat.com)
  (thomasmckay@redhat.com)
- Fixes #9370: Switch to ASCII 'x' to fix assets precompile.
  (ericdhelms@gmail.com)
- fixes #8251 - keeping track of and showing incremental update content
  (jsherril@redhat.com)
- fixes #9363 - syntax error in hash substitution in errata import task
  (stbenjam@redhat.com)
- fixes #9361 - correct logic to hide content hosts list on collection
  (thomasmckay@redhat.com)
- Refs #8710 - created katello-debug sub-package (lzap+git@redhat.com)
- fixes #9343 - Actkey copies auto-attach preference, BZ1173724
  (cfouant@redhat.com)
- fixes #9330 - validates new name presence prior to dynflow, BZ1187539
  (cfouant@redhat.com)
- fixes #9333 - fix bad action name on lifecycle env delete
  (jsherril@redhat.com)
- fixes #8180 - use dep solving for incremental updates (jsherril@redhat.com)
- fixes #9312 - handle errata import with duplicate packages
  (jsherril@redhat.com)
- Fixes #9298: only apply errata if box is checked, bz 1191214.
  (walden@redhat.com)
- fixes #9309 - fix for NotImplementedError on tasks page (jsherril@redhat.com)
- Ref #9300: destroy ktenv should no longer call dis (dtsang@redhat.com)
- Fixes #9176: display incremental update task in nutupane, bz 1188823.
  (walden@redhat.com)
- Fixes #8834: Prevent empty composite list just after creating content view.
  (ericdhelms@gmail.com)
- Fixes #8938: Publish Red Hat repositories upon enablement.
  (ericdhelms@gmail.com)
- Fixes #9276 - Added some DockerTag tests (daviddavis@redhat.com)
- fixes #9264 - fix for ambiguous col on errata content hosts
  (jsherril@redhat.com)
- Fixes #9238: fix errata icon classes post patternfly upgrade.
  (walden@redhat.com)
  (daviddavis@redhat.com)
- Fixes #8918 - Katello UI to provision docker container (paji@redhat.com)
- Fixes #9224 - Not setting docker upstream name on clones
  (daviddavis@redhat.com)
- Fixes #9220 - fixing incremental update errors and button disable.
  (walden@redhat.com)
- Fixes #9219: close details pane when cancelling content host selection.
  (walden@redhat.com)
- fixes #9221 - fix scoped search call for environment (jsherril@redhat.com)
- fixes #9218 - extend hostgroups controller create/update to include katello
  attrs (bbuckingham@redhat.com)
- Fixes #7127 - Creating a docker tag page (daviddavis@redhat.com)
- Fixes #9209 - Default capsule now checked using Pulp feature
  (paji@redhat.com)
- Fixes #9206: Remove border-radius mixin that was removed in Foreman.
  (ericdhelms@gmail.com)
- fixes #9201 - adds search options for content views index, BZ1188244
  (cfouant@redhat.com)
- Refs #9200: Discovery does not work with Foreman 1.8 currently.
  (ericdhelms@gmail.com)
  (walden@redhat.com)
- Fixes #8192 - allow applying errata to CHs after incremental update.
  (walden@redhat.com)
- Refs #8190: Fix API docs to match intended params. (ericdhelms@gmail.com)
- Fixes #9167: Fix chained scopes when using scoped_search in API
  (ericdhelms@gmail.com)
- Fixes #9181: fix sorting on Errata ID table column. (walden@redhat.com)
- Fixes #8039 - upgrade patternfly to version 1.1.3. (walden@redhat.com)
- Fixes #8178, 8189:  adding UI for incremental update. (walden@redhat.com)
- Fixes 9174 - replace UUIDTools with SecureRandom (inecas@redhat.com)
- fixes #9158 - do not find foreman host by mac (stbenjam@redhat.com)
- Fixes #8959 - Repo create cleanup (paji@redhat.com)
- refs #8683 - adding support for katello-selinux (jsherril@redhat.com)
  (jlsherrill@gmail.com)
- fixes #8612 - Makes output consistent for deleting act key, BZ1171092
  (cfouant@redhat.com)
  (daviddavis@redhat.com)
- fixes #8040 - Product content changes are updated in UI, BZ1112747
  (cfouant@redhat.com)
- Fixes #8958 - Show tag info for docker images (daviddavis@redhat.com)
- fixes #9131 - publish content view was always using latest puppet module
  (jsherril@redhat.com)
- fixes #8191 - adding support for updating systems after an incremental update
  (jsherril@redhat.com)
- fixes #9051 - add errata_ids param to systems index (jsherril@redhat.com)
- Refs #9099 - Update rubocop to 0.28 (daviddavis@redhat.com)
- refs #8213 - add sam-installer to comps (mmccune@redhat.com)
- fixes #9105 - set default org for initial admin user (jsherril@redhat.com)
  (jlsherrill@gmail.com)
- Fixes #8688 - Migrate environment to scoped search (sloranz@xantham.com)
- Fixes #8307 - allow filtering of Errata by available/installable.
  (walden@redhat.com)
- refs 8213 - split out katello package into modular sub-packages
  (mmccune@redhat.com)
- refs #8860 - updating clean backend objects to handle missing pulp entries
  (jsherril@redhat.com)
- Fixes #8951 - add host collection BZ1143029 (sloranz@xantham.com)
- Fixes #9079 - Add /var/lib/mongodb to the foreman-debug collection
  (bkearney@redhat.com)
  (thomasmckay@redhat.com)
- fixes #8941 - dynflow refresh subscriptions (auto-attach)
  (thomasmckay@redhat.com)
- Fixes #7676 - order dashboard errata list by errata updated date.
  (walden@redhat.com)
- Refs #7745: Support checking for custom header from RHSM proxied requests.
  (ericdhelms@gmail.com)
- fixes #8174 - specify capsule-supported gpg key url (jsherril@redhat.com)
- fixes #8194 - adding ability to update composites as part of a content view
  update (jsherril@redhat.com)
- Fixes #8870 - add applicable systems errata count to errata list.
  (walden@redhat.com)
- Fixes #9011 - Skip deleting products during manifest actions
  (daviddavis@redhat.com)
- Fixes #8652: replace errata content search links (walden@redhat.com)
- Fixes #8971: rename "Available" to "Installable" Errata, bz 1182604.
  (walden@redhat.com)
- fixes #8574 - separating host content view & life env from puppet env
  (jsherril@redhat.com)
- fixes #8867 - fixes activation key dynflow update passing in nil variables
  (cfouant@redhat.com)
- Fixes #8895: link to errata page from errata dashboard. (walden@redhat.com)
- Fixes #8960 - Handled ISE on bulk repos sync page (paji@redhat.com)
- Fixes #8962 - CV page shows only non zero content counts in UI
  (paji@redhat.com)
- Fixes #8836 - CV Versions page shows docker info (paji@redhat.com)
  (bryan.kearney@gmail.com)
- Fixes #8974 - HC make name optional on update (dtsang@redhat.com)
- Fixes #8961 - Fixing a typo in the name of an action class (paji@redhat.com)
- Fixes #7755: Use product label to make media unique. (ericdhelms@gmail.com)
- Refs #8934: Set menu links to disable turbo links support.
  (ericdhelms@gmail.com)
- fixes #8943 - do not perform post sync actions until after the sync is
  finished (jsherril@redhat.com)
  (thomasmckay@redhat.com)
- fixes #8353 - require all neccessary pulp packages in RPM
  (stbenjam@redhat.com)
  (daviddavis@redhat.com)
- Fixes #8933 - Turn off content type check for routes (daviddavis@redhat.com)
- fixes #8326 - fixing errata queries due to ambiguous sort
  (jsherril@redhat.com)
- Fixes #8621: Set sync plan on product during repository creation.
  (ericdhelms@gmail.com)
- fixes #8936 - fixes localization to help message, BZ1143859
  (cfouant@redhat.com)
- fixes #8935 - reverts table columns for SAM feature flags
  (cfouant@redhat.com)
- Fixes #8924: add last_sync_words to sync plan rabl, bz 1130300.
  (walden@redhat.com)
  (bryan.kearney@gmail.com)
- fixes #8860 - fixing clean_backend_objects rake task (jsherril@redhat.com)
- Fixes #8931 - Update the text for the filter to address typo
  (bkearney@redhat.com)
- Fixes #8928 : Text on publish screen is not grammatically correct
  (bkearney@redhat.com)
  (jlsherrill@gmail.com)
  (daviddavis@redhat.com)
  (daviddavis@redhat.com)
- Fixes #8632 - Redoing docker tables/fields (daviddavis@redhat.com)
- fixes #8671, #8684 - Hides custom products from SAM users, hides gpg keys
  from red hat products, BZ1173340, BZ1173764 (cfouant@redhat.com)
- refs #8764 - moving organization description to foreman core
  (orabin@redhat.com)
- fixes #8904 - fixing query breaking content view repo list
  (jsherril@redhat.com)
- Fixes #7691: Add repository filter to Errata list page.
  (ericdhelms@gmail.com)
- refs #8635 - add hammer-cli-gutterball to comps (komidore64@gmail.com)
- fixes #8563 - fetch package information in chunks when fetching file lists
  (jsherril@redhat.com)
- fixes #8893 - hide katello-agent info (thomasmckay@redhat.com)
- fixes #8891 - adds auto-attach to api/cli output, BZ1180285
  (cfouant@redhat.com)
  (cfouant@redhat.com)
- Fixes #8887: returning correct CVE structure in rabl. (walden@redhat.com)
- Fixes #8886: show N/A if no CVEs exist for errata. (walden@redhat.com)
- Fixes #6184 - Dynflowizes system update. (aruzicka@redhat.com)
- Fixes #8846 - Have the V2 api controller extend Api::V2::BaseController
  (daviddavis@redhat.com)
- Fixes #8858: Collect candlepin logs on RHEL7 (bkearney@redhat.com)
- Fixes #8594: Fix errata listing for content view filter regression.
  (ericdhelms@gmail.com)
- fixes #8848 - fixing content host errata list (jsherril@redhat.com)
- Fixes #8743 - Repo Index returns promoted repos (paji@redhat.com)
- fixes #8730 - keep track of components of composite content view versions
  (jsherril@redhat.com)
- fixes #8833 - Removes name requirement for act key update, BZ 1178928
  (cfouant@redhat.com)
  dustints/check_config_starting_listen_on_cp_event (dtsang@redhat.com)
- refs #8575 - adding python-qpid-common to comps (jsherril@redhat.com)
- fixes #8775 - ensure available errata are unique (stbenjam@redhat.com)
- fixes #8776 - bumping gem version (jsherril@redhat.com)
- Fixes #8771 - Remove katello_api from comps (daviddavis@redhat.com)
- Automatic commit of package [katello] minor release [2.2.0-1].
  (daviddavis@redhat.com)
- fixes #8731 - sets feature flag for lifecycle environments, BZ1174944
  (cfouant@redhat.com)
- fixes #8729 - Sets feature flag on remote actions, BZ1174932
  (cfouant@redhat.com)
- Fixes #8482: add an environment filter to the errata content hosts page.
  (walden@redhat.com)
- Fixes #8552 - Don't initialize cp task if no qpid config (dtsang@redhat.com)

* Fri Dec 19 2014 David Davis <daviddavis@redhat.com> 2.2.0-1
- fatal: bad revision 'rubygem-katello-2.2.0-1..HEAD'

* Fri Dec 19 2014 David Davis <daviddavis@redhat.com> 2.2.0-1
  (jlsherrill@gmail.com)
  (daviddavis@redhat.com)
- fixes #8768 - fixing pulp glue tests in live mode (jsherril@redhat.com)
- fixes #8598 - fixing repository delete current user was not set during
  finalize phase (jsherril@redhat.com)
- fixes #8770 - delay node metadata sync to 2nd action (jsherril@redhat.com)
- Fixes #8655: Show content view and environment pairings for library
  repositories. (ericdhelms@gmail.com)
- Fixes #8763 - Remove unnecessary ignore blocks (daviddavis@redhat.com)
- fixes #8703 - fix promotion notification mail (stbenjam@redhat.com)
- fixes #8354 - truncate long erratum titles (stbenjam@redhat.com)
- fixes #8687 - rewire sync_plan for scoped search (sloranz@xantham.com)
- Fixes #7953: add product/repositories list for an erratum.
  (walden@redhat.com)
- fixes #8686 - rewire gpg_keys for scoped search (sloranz@xantham.com)
- fixes #8188 - adding api to determine what inc update is needed
  (jsherril@redhat.com)
- fixes #8306,8177,8180 - adding incremnetal update api (jsherril@redhat.com)
- Refs #8679: Update comps for new katello installer breakout.
  (ericdhelms@gmail.com)
- fixes #8681 - removing requirements for maruku (jsherril@redhat.com)
- fixes #6637 - loosening url validation restrictions (jsherril@redhat.com)
- Fixes #8519 - Bonus subs not being reindexed (dtsang@redhat.com)
- fixes #8675 - updating rubocop.yml for bastion_katello (jsherril@redhat.com)
- Fixes #8626: ensure errata icons line up, BZ 1171310. (walden@redhat.com)
  (cfouant@redhat.com)
- Fixes #8668: Hide 'Server' kickstart repositories from enablement.
  (ericdhelms@gmail.com)
- refs #8596 - adding foreman_sam and hammer-cli-sam to comps
  (komidore64@gmail.com)
  (komidore64@gmail.com)
- refs #8584 - foreman-gutterball and gutterball to comps
  (komidore64@gmail.com)
  (daviddavis@redhat.com)
- fixes #7480 - disown foreman templates (stbenjam@redhat.com)
  (jlsherrill@gmail.com)
- fixes #8606 - fixing puppet module index (jsherril@redhat.com)
- Fixes #8615 - relax qpid_messaging dependency (jmontleo@redhat.com)
  (thomasmckay@redhat.com)
- fixes #7176 - display hypervisor/guest info for subscription
  (thomasmckay@redhat.com)
- BuildRequires needs to be updated as well (jmontleo@redhat.com)
- Fixes #8610 - Adding search param to repo content api (daviddavis@redhat.com)
- fixes #7667 - promotion errata mail notification (stbenjam@redhat.com)
- fixes #7666 - sync errata mail notification (stbenjam@redhat.com)
- fixes #7668 - host errata mail notification (stbenjam@redhat.com)
- fixes #8480 - Adds default setting for act key autoattach, BZ 1166889
  (cfouant@redhat.com)
- fixes #8491 - removing puppet modules list from content view version api
  (jsherril@redhat.com)
- fixes #8588 - make repo indexing idempotent (stbenjam@redhat.com)
- Fixes #7603,7792,7789 - Code to promote/publish dockered cv's
  (paji@redhat.com)
  (daviddavis@redhat.com)
- fixes #8549 - Fixes subscription error messages for act key, BZ 1154619
  (cfouant@redhat.com)
- Fixes #7845 - Allows user to delete custom product (aruzicka@redhat.com)
- fixes #7695, #7677 - enable searching errata by issued/updated times
  (stbenjam@redhat.com)
- Fixes #8579 - Enabling EmptyLinesAroundBody cop (daviddavis@redhat.com)
- Fixes #7810 - Remove docker and puppet content from a repository
  (daviddavis@redhat.com)
- Fixes #7688: add content hosts tab to the errata details page.
  (walden@redhat.com)
- Fixes #8553: Fix broken table layouts. (ericdhelms@gmail.com)
- Fixes #8384: Remove dependence on ui-alchemy_rails and compass.
  (ericdhelms@gmail.com)
- fixes #7697 - enable searching by CVE (stbenjam@redhat.com)
- refs #7706 - extend errata rabl in systems API (stbenjam@redhat.com)
- Fixes #8113 - Docker tags count now displayed for Repositories
  (paji@redhat.com)
  (daviddavis@redhat.com)
  (daviddavis@redhat.com)
  (bryan.kearney@gmail.com)
- Fixes #8494 - Re-adding the content view filter line (daviddavis@redhat.com)
- refs #7233 - refactor FactoryGirl methods to after(:action) and use
  assocation for library (shlomi@ben-hanna.com)
- Fixes #8483: Require foreman-assets RPM. (ericdhelms@gmail.com)
  (komidore64@gmail.com)
  (daviddavis@redhat.com)
- Fixes #8404: Re-factor environments UI to show environment counts.
  (ericdhelms@gmail.com)
- fixes #6939 - Sets autoattach flag for act key, BZ 1126924
  (cfouant@redhat.com)
- fixes #7904 - adding autocomplete for errata (jsherril@redhat.com)
- fixes #8454 - display product id (sku) (thomasmckay@redhat.com)
- Fixes #8101 - Show docker pull url for repository details page
  (aruzicka@redhat.com)
- fixes #8451 - add hammer-cli-csv to nightly builds (thomasmckay@redhat.com)
- Fixes #8406: Allow content to be filtered by environment.
  (ericdhelms@gmail.com)
  (daviddavis@redhat.com)
- Fixes #8018 - Performs docker repository name validation on repo create
  (aruzicka@redhat.com)
- Fixes #8441 - Can specify cdn ssl version via config (paji@redhat.com)
- Fixes #8440: Fix broken auto_complete URL in Package Filter UI.
  (ericdhelms@gmail.com)
- fixes #8438 - using correct environments for repository lookup
  (jsherril@redhat.com)
- Fixes #8436 - Fixing broken apidoc route and field (daviddavis@redhat.com)
- Refs #8396: Remove use of 'alchemy' namespace from Bastion re-facotring.
  (ericdhelms@gmail.com)
  (eric.d.helms@gmail.com)
- Refs #7883: Adds repository filter to tabs on content view version details.
  (ericdhelms@gmail.com)
- Fixes #7883: Allow filtering content by a content view version and
  repository. (ericdhelms@gmail.com)
- Fixes #8222 - Prevent duplicate docker tags for repos (daviddavis@redhat.com)
- Fixes #8397: Display errata counts for Library environment counts.
  (ericdhelms@gmail.com)
- Fixes #5059 - Returns error message when sorting by wrong column.
  (aruzicka@redhat.com)
  (bryan.kearney@gmail.com)
- fixes #8355 - remove ambigious column plucks for older rails
  (stbenjam@redhat.com)
- Fixes #8338: add CVE numbers to errata details. (walden@redhat.com)
- Refs #8340 - remove uneeded packages from comps (jsherril@redhat.com)
- Fixes #8322: display black icons if no errata needs to be applied.
  (walden@redhat.com)
- fixes #8318 - make errata indexing idempotent (stbenjam@redhat.com)
  (daviddavis@redhat.com)
- Refs #8242 - Create docker tag API (daviddavis@redhat.com)
  (komidore64@gmail.com)
- refs #8292 - adding org_id param b/c it's required, BZ 1135125
  (komidore64@gmail.com)
- Fixes #8237 : Validate that the user can not set max_content_hosts if
  unlimited_content_hosts is true (bryan.kearney@gmail.com)
- Fixes #8283: Require jquery-ui-rails for the RPM spec and bump Runcible.
  (ericdhelms@gmail.com)
- Fixes #8127: add errata counts to the content host details page.
  (walden@redhat.com)
- Fixes #8273/BZ1138868: fix JS error on content hosts page.
  (walden@redhat.com)
- fixes #8268 - adding progress reporting for puppet sync (jsherril@redhat.com)
- Fixes #8263: Remove usage of to_sym on user input params.
  (ericdhelms@gmail.com)
  (bryan.kearney@gmail.com)
- Fixes #8265/BZ1154380: remove deselect all link from tables.
  (walden@redhat.com)
- fixes #8262 - fixing progress updating on sync status page
  (jsherril@redhat.com)
- fixes #6060 - Fixes activation-key content override, BZ 1104638
  (cfouant@redhat.com)
- fixes #8255 - properly display new version for publish after just publishing
  old version (jsherril@redhat.com)
- fixes #8253 - updating requirements for foreman_docker (jsherril@redhat.com)
- fixes #8220 - Throw error for act key content host limit beyond max, BZ
  1139576 (cfouant@redhat.com)
- Fixes #8235: Add orgzanization_id to the systems json which is generated
  (bryan.kearney@gmail.com)
  (thomasmckay@redhat.com)
- Fixes #8238 : Mark content_type parameter as required, since it is for POSTS
  (bryan.kearney@gmail.com)
- Fixes #8225 - RH Cdn url can now be updated (paji@redhat.com)
- fixes #8232 - fixing db:seed when called twice with seed organization
  (jsherril@redhat.com)
- fixes #8131 - hypervisors forced into content host's org, env, and cv
  (thomasmckay@redhat.com)
  (daviddavis@redhat.com)
- Refs #8138: Removes use of RootURL removed from Bastion.
  (ericdhelms@gmail.com)
- Fixes #7604 - Enable docker image uploads (daviddavis@redhat.com)
  (daviddavis@redhat.com)
  (daviddavis@redhat.com)
- fixes #7711 - adding api errata comparison for content view versions
  (jsherril@redhat.com)
- Fixes #8209 - Hammer repo create doesn't require url (aruzicka@redhat.com)
- Fixes #7554 - Show user friendly error message on 413 (daviddavis@redhat.com)
  (komidore64@gmail.com)
- Fixes #7961: Able to view the Errata in the Library Environment
  (ericdhelms@gmail.com)
- fixes #7885 - adding counts to lifecycle environments (jsherril@redhat.com)
- Fixes #7126 - Upload docker images to the API (daviddavis@redhat.com)
- fixes #7690 - adding errata applicable/available systems api
  (jsherril@redhat.com)
- Fixes #8126:  add color to errata icons based on errata count.
  (walden@redhat.com)
- Fixes #8132: Remove unused styling and import to fix asset compile.
  (ericdhelms@gmail.com)
- fixes #8116 - correcting prior env description in apidoc, BZ 1130258
  (komidore64@gmail.com)
- Fixes #7609: View the details of a Content View Version
  (ericdhelms@gmail.com)
  (daviddavis@redhat.com)
  (daviddavis@redhat.com)
- Fixes #7642 - Added backend/api for docker images (daviddavis@redhat.com)
- Fixes #8119 - Remove tests covered by rubocop (daviddavis@redhat.com)
- Fixes #7951 - Add/Remove Docker repos to Content Views (paji@redhat.com)
  (daviddavis@redhat.com)
- fixes #7680 - filter errata optionally by organization id from api
  (jsherril@redhat.com)
- fixes #8094 - Content Host - fix the host collection capacity
  (bbuckingham@redhat.com)
- fixes #8089 - Content Dashboard - fix the sorting of items in Sync Overview
  (bbuckingham@redhat.com)
- fixes #8087 - Locations - update to allow proper use of nested locations
  (bbuckingham@redhat.com)
- fixes #7754 - Adds cloning of activation key, BZ 531307 (cfouant@redhat.com)
- Fixes #6187,BZ1125358 - Deleting a resource and creation a new one wont lead
  to conflicts (aruzicka@redhat.com)
- fixes #7996 - don't index users in elasticsearch (stbenjam@redhat.com)
  desccriptification-station (komidore64@gmail.com)
- Fixes #8013: Rely on factory_girl_rails and mocha version from Foreman.
  (ericdhelms@gmail.com)
- fixes #7993 - showing available errata and not all applicable
  (jsherril@redhat.com)
- Refs #7733: Remove usage of Host fixtures in favor of Host factories.
  (ericdhelms@gmail.com)
- Refs #7423: Convert to using Bastion core to provide the Katello UI.
  (ericdhelms@gmail.com)
- Fixes #7846 - remove critcal section from cp events task (dtsang@redhat.com)
- fixes #7701,7702,7703 - adding selector for type of applicability view
  (jsherril@redhat.com)
- Fixes #7949: show affected packages of errata on details page.
  (walden@redhat.com)
-  fixes #7979 - adding better error reporting for repo enable ui
  (jsherril@redhat.com)
  (eric.d.helms@gmail.com)
- fixes #7834 - properly process incoming and updated hypervisors
  (thomasmckay@redhat.com)
  (daviddavis@redhat.com)
- Fixes #7796 - Added code to enable docker repos (paji@redhat.com)
- Refs #7156 - Addressing more rubocop cops (daviddavis@redhat.com)
- Fixes #7919/BZ1151633: fix translations of sync plan intervals.
  (walden@redhat.com)
- Fixes #7947 - Validating package checksums when syncing
  (daviddavis@redhat.com)
- refs #6463 - hammer was unable to update the org's desc, BZ 1114136
  (komidore64@gmail.com)
- Fixes #7685: add errata details page. (walden@redhat.com)
- Fixes #7942: redirect to correct place after creating a sync plan.
  (walden@redhat.com)
- fixes #7813 - adds arguments to activation-key functions, BZ 1110475
  (cfouant@redhat.com)
- Fixes #7630 - Creating new product saves its description
  (aruzicka@redhat.com)
  (daviddavis@redhat.com)
  (daviddavis@redhat.com)
- fixes 7927 - fix subscription-manager registration for missing constant
  (jsherril@redhat.com)
- Fixes #7929 - Update the MethodLength namespaces (daviddavis@redhat.com)
  (walden@redhat.com)
- Fixes #7915 - copy uploaded files to shared tmp directory in plan phase
  (inecas@redhat.com)
- Fixes #5015 - Repo discovery display format (oprazak@redhat.com)
- Fixes #7679: add the errata list page and menu item. (walden@redhat.com)
- Fixes #7903 - Remove call to undefined class (daviddavis@redhat.com)
- Fixes #7156 - Fixing up rubocop errors across katello (daviddavis@redhat.com)
  (daviddavis@redhat.com)
- Fixes #7863 - Upgrade rubocop to 0.26.1 (daviddavis@redhat.com)
- Fixes #7900: Bastion pages couldn't load due to unparseable User.to_json
  (ericdhelms@gmail.com)
  (daviddavis@redhat.com)
- Fixes #7816 - Refactor strong_params code (daviddavis@redhat.com)
- Refs #6421 - Turning on rubocop for the test directory
  (daviddavis@redhat.com)
- Refs #7156: Fixing app/lib for Rubocop. (ericdhelms@gmail.com)
  (walden@redhat.com)
- Fixes #7852: Refactor puppet modules controller to use content concern.
  (ericdhelms@gmail.com)
- Refs #6421: Fix spec directory rubocop offenses. (ericdhelms@gmail.com)
  (daviddavis@redhat.com)
- refs #7493 - fixing test that is randomly failing (jsherril@redhat.com)
- Fixes #7704: show applicable Errata count for Content Host list.
  (walden@redhat.com)
- Refs #7156 - Disable some cops (daviddavis@redhat.com)
  (komidore64@gmail.com)
- refs #7156 - test updates for model changes (jsherril@redhat.com)
  (eric.d.helms@gmail.com)
  (eric.d.helms@gmail.com)
- Refs #7156: Fix lib/ Rubocop offenses. (ericdhelms@gmail.com)
- refs #7156 - rubocop - adding to app/views/*.rabl files
  (komidore64@gmail.com)
- refs #7156 - updating rubocop style for migrations (jsherril@redhat.com)
- Refs #7156: fix rubocop offenses in app/controllers. (walden@redhat.com)
- Refs #7156: Removing unneeded files Rubocop was checking.
  (ericdhelms@gmail.com)
- refs #7156 - updating models for new rubocop style (jsherril@redhat.com)
- Refs #7156: Fix config/ Rubocop offenses. (ericdhelms@gmail.com)
- refs #7156 - rubocop fixes for katello/helpers (bbuckingham@redhat.com)
- fixes #7705 - adding errata counts to content host details
  (jsherril@redhat.com)
- Refs #7642 - Back-end code for viewing docker images (daviddavis@redhat.com)
- Fixes #7798 - adding editable redhat registry url (paji@redhat.com)
  (daviddavis@redhat.com)
  (dtsang@redhat.com)
- Fixes #7844 - lockdown qpid_messaging rpms (dtsang@redhat.com)
- Fixes #7526 - Fixing crane dependency (daviddavis@redhat.com)
  (daviddavis@redhat.com)
- Ref# #7124 - Improved a complicated if statement (paji@redhat.com)
- Merge branch 'master' into master-merge (paji@redhat.com)
- Fixes #7844 - lockdown qpid_messaging >= 0.26.1 && (dtsang@redhat.com)
- Fixes #7526 - Add pulp-docker dependencies for pulp 2.5 upgrade
  (daviddavis@redhat.com)
- Merge branch 'master' into master-merge (paji@redhat.com)
- refs #7818 - render permissions to fix oj 2.10.3 error (elobatocs@gmail.com)
- refs #7814 - adding one last client package to comps (jsherril@redhat.com)
- fixes #7814 - adding a few client pages to comps (jsherril@redhat.com)
- refs #7124 - docker - downcase pulp_id when creating docker repository
  (bbuckingham@redhat.com)
- Fixes #7606 - Added code to sync docker repos (paji@redhat.com)
- refs #7124 - docker - fix issue where repo was always created as protected
  (bbuckingham@redhat.com)
  (dtsang@redhat.com)
  (dtsang@redhat.com)
- Fixes #6543 - updt index on cp event bz1115602 (inecas@redhat.com)
- Fixes #7243 - CVV promotion out of sequence (dtsang@redhat.com)
  (eric.d.helms@gmail.com)
- Fixes #7730,BZ1127090 - Activation key max host count can be set from finite
  number to infinite (aruzicka@redhat.com)
- fixes #7627 - handle cases where this codte is ran outside of rails
  (mmccune@redhat.com)
- Fixes #4121: Removes unused configuration values. (ericdhelms@gmail.com)
- Fixes #7493 - Store the description entered during publish
  (daviddavis@redhat.com)
  (daviddavis@redhat.com)
- fixes #4056 - add checksum selection for custom repos (jsherril@redhat.com)
- fixes #7621 - treat a nil minor OS version as empty string
  (jsherril@redhat.com)
- fixes #7598 - Docker - initial ui chgs to support CRUD
  (bbuckingham@redhat.com)
- Fixes #7641: add errata icon tooltips on content view versions page.
  (walden@redhat.com)
- Fixes #7616 - Use validates_lengths_from_database (daviddavis@redhat.com)
- fixes #7155 - ensure displayMessage is present (thomasmckay@redhat.com)
- fixes #7124 - Docker - initial backend/api changes to support repository CRUD
  actions (bbuckingham@redhat.com)
- Fixes #7304 - use dynflow for repository sync bulk actions
  (inecas@redhat.com)
- Fixes #6946: Update organization to disallow modifying label
  (paji@redhat.com)
  (walden@redhat.com)
- Fixes #6912/BZ 1126446 - Sync Plan enabled by default, checkbox to disable on
  edit (oprazak@redhat.com)
- fixes #7542 - add ability to delete a Hypervisor (stbenjam@redhat.com)
  (eric.d.helms@gmail.com)
- Fixes #7527 - don't require less in production unless from rake
  (inecas@redhat.com)
- fixes #7521 - fix import of virt-who subscription information
  (stbenjam@redhat.com)
- Fixes #7446/bz1140653 - Host delete dynflowed (paji@redhat.com)
  (daviddavis@redhat.com)
- fixes #7481 - fix taxonomy association on smart proxy create
  (jsherril@redhat.com)
- Fixes #7428,BZ1120314 - Show user friendly error when no repo name
  (daviddavis@redhat.com)
  (komidore64@gmail.com)
- Fixes #7322 - Fixed handling of empty body (just whitespaces)
  (martin.bacovsky@gmail.com)
- fixes #7422 - documenting the `label` param for env creation, BZ 883170
  (komidore64@gmail.com)
- Fixes #7465: display message when there aren't any subscriptions.
  (walden@redhat.com)
  (walden@redhat.com)
- Fixes #6186 - Dynflowize product update. (aruzicka@redhat.com)
- refs 7207 - fixing comps for el7 candlepin (jsherril@redhat.com)
  (daviddavis@redhat.com)
  (daviddavis@redhat.com)
- fixes #7441 - add candlepin-common to comps (jsherril@redhat.com)
- Fixes #4633 - Select all checkbox deselected after sync (oprazak@redhat.com)
- Refs #7156 - Fixing some small rubocop items (daviddavis@redhat.com)
- Fixes #7362 - Update org create dynflow (paji@redhat.com)
- Fixes #7427 - Avoid use of params local variables (daviddavis@redhat.com)
- fixes #7426 - Adds a spinner to the repository tabs, BZ 1129526
  (cfouant@redhat.com)
- Refs #7242: Add 1.5-2.0 Changelog. (ericdhelms@gmail.com)
- Automatic commit of package [katello] minor release [2.1.0-1].
  (jsherril@redhat.com)
- bumping to katello version to 2.1 (jsherril@redhat.com)
- Fixes #5229 - Messages for empty tables in Bastion (oprazak@redhat.com)
- Fixes #7282: Use apipie packages provided by Foreman repos.
  (ericdhelms@gmail.com)

* Fri Sep 12 2014 Justin Sherrill <jsherril@redhat.com> 2.1.0-1
- bumping to version to 2.1 (jsherril@redhat.com)

* Fri Sep 12 2014 Justin Sherrill <jsherril@redhat.com> 2.0.0-1
- bumping to katello 2.0 (jsherril@redhat.com)
- Automatic commit of package [katello] minor release [2.0.0-0].
  (jsherril@redhat.com)
- fixes #7410 - replaced query_params with params (thomasmckay@redhat.com)
- fixes #7404 - add salt support to katello templates (stbenjam@redhat.com)
- Fixes #7395: Turn off strong params for Candlepin proxies controller.
  (ericdhelms@gmail.com)
- fixes #6488 enable autosearch completion on Katello model filters
  (stbenjam@redhat.com)
- Fixes #7394: Stop blocking plugin routes from being loaded properly.
  (ericdhelms@gmail.com)
- Fixes #3584: Enable all tests to be run. (ericdhelms@gmail.com)
- Fixes #7390: Change global variable $/ to $INPUT_RECORD_SEPARATOR.
  (ericdhelms@gmail.com)
- Fixes #7389: Prevent undefined method error from root controller.
  (ericdhelms@gmail.com)
- Fixes #7358/BZ1138411: correct empty org message logic on dashboard.
  (walden@redhat.com)
- Fixes #6287: Remove V1 API entirely. (ericdhelms@gmail.com)
- refs #6370 - automatically associate OS's with templates
  (stbenjam@redhat.com)
- Fixes #7307 - Refactor errata/package/package group APIs
  (daviddavis@redhat.com)
- Refs #7156 - Fixing a bunch of small rubocop items (daviddavis@redhat.com)
- fixes #7360 / BZ 1120595 - UI: Product: fix Sync Now behavior
  (bbuckingham@redhat.com)
- Fixes #6942,bz1122924 - subscription reindex (inecas@redhat.com)
- Fixes #6821/BZ1117636: fix link to content hosts on CV delete page.
  (walden@redhat.com)
- fixes #7343 / BZ 1132576 - iso sync - fix issue where progress report not
  available yet (bbuckingham@redhat.com)
- fixes #7342 / BZ 1128469 - content view filter - improve behavior when
  clicking calendar icon (bbuckingham@redhat.com)
- Fixes #7341: Adds script to generate contributors with initial list.
  (ericdhelms@gmail.com)
- fixes #7309 / BZ 1093483 - Repo sync status - update UI cross-links and
  status based on dynflow task (bbuckingham@redhat.com)
- fixes #7328 - Adds route for sync-plans, BZ 1132817 (cfouant@redhat.com)
- Fixes #6773 - Host inherits Content Source from Hostgroup
  (elobatocs@gmail.com)
- Fixes #7303 - Added content view version param to errata api
  (daviddavis@redhat.com)
- Fixes #7300 - Adding a content view version parameter for packages
  (daviddavis@redhat.com)
- Fixes #7242: Script to generate formatted changelog. (ericdhelms@gmail.com)
- fixes #7292 - Fixes duplicated sync plan route, BZ 1132914
  (cfouant@redhat.com)
- Fixes #7283: using translate directive in <span> to avoid infinite loop.
  (walden@redhat.com)
- Fixes #7294: replace <th> translate filters with directives.
  (walden@redhat.com)
- Fixes #6993: Ensure repo discovery proxy setup is loaded in production.
  (ericdhelms@gmail.com)
- fixes #7273 - sync puppet and rpm content together (jsherril@redhat.com)
- fixes #7278 - Fixes activation key registration hint, BZ 1128245
  (cfouant@redhat.com)
- Fixes #7028 - fixing api docs for orgs (tstrachota@redhat.com)
- fixes #7271 - validate repositories associated to content views
  (jsherril@redhat.com)
- fixes #6605 - Adds registered by to content host, BZ 1020402
  (cfouant@redhat.com)
- fixes #7162 / BZ 1102763 - capsule - treat task as failed if sync times out
  with capsule (bbuckingham@redhat.com)
- Fixes #7272 - system has extra validation on name (dtsang@redhat.com)
- Fixes #7270/BZ1131661: remove GMT from new sync plan form.
  (walden@redhat.com)
- Fixes #6955: using CSS to mimic a <pre> for multiple line support.
  (walden@redhat.com)
- fixes #7266 - specify time when creating new ulimited subscriptions
  (jsherril@redhat.com)
- Fixes #6990 - No message for admin (oprazak@redhat.com)
- Fixes #7027: Restrict mongodb to version 2.4 or greater.
  (ericdhelms@gmail.com)
- Fixes #7251 - hammer org_id help text missing (dtsang@redhat.com)
- Fixes #7241/bz1132790 - Enable rh common for ks template (paji@redhat.com)
- fixes #7084 - add rubygem-hammer_cli_import dep (jmontleo@redhat.com)
- refs #5271 - update tito for el7 (jsherril@redhat.com)
- Fixes #7120/BZ980113: use BS3 on dashboard to make it responsive.
  (walden@redhat.com)
- Fixes #6726 - sends username in cp-user header. (aruzicka@redhat.com)
