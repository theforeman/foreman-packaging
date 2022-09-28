# template: hammer_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name hammer_cli_katello
%global plugin_name katello

%global release 1

%{!?_root_sysconfdir:%global _root_sysconfdir %{_sysconfdir}}
%global hammer_confdir %{_root_sysconfdir}/hammer

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.5.3
Release: %{?prerelease:0.}%{release}%{?prerelease}%{?nightly}%{?dist}
Summary: Katello commands for Hammer
Group: Development/Languages
License: GPLv3
URL: https://github.com/Katello/hammer-cli-katello
Source0: https://rubygems.org/gems/%{gem_name}-%{version}%{?prerelease}.gem

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(hammer_cli_foreman)
Requires: %{?scl_prefix}rubygem(hammer_cli_foreman_tasks)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

Obsoletes: %{?scl_prefix}rubygem-hammer_cli_foreman_docker < 0.0.7-2

%description
Hammer-CLI-Katello is a plugin for Hammer to provide connectivity to a Katello
server.


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
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{hammer_confdir}/cli.modules.d
install -m 0644 .%{gem_instdir}/config/%{plugin_name}.yml \
                %{buildroot}%{hammer_confdir}/cli.modules.d/%{plugin_name}.yml

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_instdir}/locale
%exclude %{gem_cache}
%{gem_spec}
%config %{hammer_confdir}/cli.modules.d/%{plugin_name}.yml

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/config
%{gem_instdir}/test

%changelog
* Wed Sep 28 2022 Chris Roberts <chrobert@redhat.com> 1.5.3-1
- Update to 1.5.3

* Thu Jun 30 2022 Chris Roberts - 1.5.2-1
* Bump version to 1.5.2

* Fri Mar 11 2022 Evgeni Golov - 1.5.0-0.1.pre.master
- Bump version to 1.5.0

* Fri Mar 04 2022 Zach Huntington-Meath <zhunting@redhat.com> - 1.4.1-0.1.pre.master
- Bump version to 1.4.1

* Thu Nov 11 2021 Chris Roberts <chrobert@redhat.com> - 1.4.0-0.1.pre.master
- Bump version to 1.4.0

* Fri Oct 22 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.3.0-0.1.pre.master
- Bump version to 1.3.0

* Fri May 07 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.1.1-0.1.pre.master
- Update version to 1.1.1

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.0.1-0.4.pre.master
- Rebuild for Ruby 2.7

* Wed Mar 24 2021 Evgeni Golov - 1.0.1-0.3.pre.master
- Obsolete hammer_cli_foreman_docker as we ship conflicting commands

* Mon Mar 15 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.0.1-0.2.pre.master
- Drop hammer_cli_docker and hammer_cli_bootdisk requires

* Thu Feb 18 2021 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.0.1-0.1.pre.master
- Bump to 1.0.1

* Mon Nov 02 2020 Chris Roberts - 0.25-0.1.pre.master
- Update version to 0.25

* Wed Sep 02 2020 Chris Roberts - 0.24-0.1.pre.master
- Update version to 0.24

* Wed Jun 03 2020 Evgeni Golov - 0.23-0.1.pre.master
- Update version to 0.23
- Regenerate spec file based on recent template

* Mon Feb 24 2020 Eric D. Helms <ericdhelms@gmail.com> - 0.22-0.3.pre.master
- Update version to 0.22

* Thu Feb 13 2020 Zach Huntington-Meath - 0.21-0.3.pre.master
- Remove hammer_cli_foreman version requirement

* Mon Nov 18 2019 Evgeni Golov - 0.21-0.2.pre.master
- Unify prerelease macro handling

* Thu Nov 07 2019 Jonathon Turel <jturel@gmail.com> 0.21-0.1.pre.master
- Bump to 0.21 to match git

* Fri Aug 09 2019 Evgeni Golov 0.20-0.1.pre.master
- Bump to 0.20 to match git
- Regenerate spec based on template

* Wed May 15 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 0.19-0.1.pre.master
- Bump to 0.19-master to match git

* Mon Jan 21 2019 Jonathon Turel <jturel@gmail.com> - 0.18-0.1.pre.master
- Bump to 0.18 to match git master

* Fri Dec 14 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 0.17-0.1.pre.master
- Bump to 0.17 to match git master

* Thu Oct 25 2018 Adam Price <komidore64@gmail.com> - 0.16-0.2.pre.master
- add nightly macro

* Thu Oct 25 2018 Adam Price <komidore64@gmail.com> - 0.16-0.1.pre.master
- bump version to 0.16

* Wed Sep 12 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.15-0.3.pre.master
- Change hammer_cli_foreman requirement to match version

* Wed Sep 12 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.15-0.2.pre.master
- Add prerelease support

* Wed Sep 12 2018 Andrew Kofink <akofink@redhat.com> 0.15.0-1
- Bump to 0.15.0

* Wed Aug 29 2018 Andrew Kofink <akofink@redhat.com> 0.14.1-1
- Bump to 0.14.1

* Tue Aug 07 2018 Adam Price <komidore64@gmail.com> 0.13.4-2
- bump release due to spec change

* Thu Jul 19 2018 Andrew Kofink <akofink@redhat.com> 0.13.4-1
- Update to 0.13.4

* Thu Jun 28 2018 Andrew Kofink <akofink@redhat.com> 0.13.3-1
- Update to 0.13.3

* Wed Jun 06 2018 Jonathon Turel <jturel@redhat.com> 0.13.2-1
- Update to 0.13.2

* Tue May 15 2018 Andrew Kofink <akofink@redhat.com> 0.13.1-1
- Update to 0.13.1

* Fri Feb 02 2018 Eric D. Helms <ericdhelms@gmail.com> 0.12.0-1
- Update Hammer-Cli-Katello to 0.12.0 (zhunting@redhat.com)

* Wed Jan 10 2018 Eric D. Helms <ericdhelms@gmail.com> 0.11.0-2
- new package built with tito

* Mon Aug 28 2017 Eric D. Helms <ericdhelms@gmail.com> 0.11.0-1
- Update hammer_cli_katello to 0.11.0 (akofink@redhat.com)

* Thu Mar 30 2017 Eric D. Helms <ericdhelms@gmail.com> 0.10.0-1
- Update hammer_cli_katello to 0.10.0 (akofink@redhat.com)
- Use gem_install macro (ericdhelms@gmail.com)

* Wed Dec 21 2016 Justin Sherrill <jsherril@redhat.com> 0.3.0-1
- Build hammer_cli_katello 0.3.0 (jsherril@redhat.com)

* Fri Sep 09 2016 Eric D Helms <ericdhelms@gmail.com> 0.1.0-1
- Update hammer-cli-katello to 0.1.0 (#283) (eric.d.helms@gmail.com)
- Fixes #15271: Obsolete removed gutterball gems (#232)
  (eric.d.helms@gmail.com)

* Tue May 17 2016 Justin Sherrill <jsherril@redhat.com> 0.0.26-1
- Update rubygem-hammer_cli_katello to 0.0.26 (komidore64@gmail.com)

* Mon May 16 2016 Justin Sherrill <jsherril@redhat.com> 0.0.25-1
- Update rubygem-hammer_cli_katello to 0.0.25 (komidore64@gmail.com)

* Mon Mar 28 2016 Justin Sherrill <jsherril@redhat.com> 0.0.24-1
- build hammer-cli-katello 0.0.24 (jsherril@redhat.com)

* Thu Feb 25 2016 Eric D Helms <ericdhelms@gmail.com> 0.0.23-1
- Update rubygem-hammer_cli_katello to 0.0.23 (ericdhelms@gmail.com)

* Thu Feb 18 2016 Eric D Helms <ericdhelms@gmail.com> 0.0.22-1
- Update rubygem-hammer_cli_katello to 0.0.22 (komidore64@gmail.com)

* Fri Feb 12 2016 Eric D Helms <ericdhelms@gmail.com> 0.0.21-1
- Update rubygem-hammer_cli_katello to 0.0.21 (komidore64@gmail.com)

* Fri Jan 22 2016 Eric D Helms <ericdhelms@gmail.com> 0.0.20-1
- Update rubygem-hammer_cli_katello to 0.0.20 (ericdhelms@gmail.com)

* Wed Jan 06 2016 Eric D. Helms <ericdhelms@gmail.com> 0.0.19-2
- Build rubygem-hammer_cli_katello for RH22 SCL (ericdhelms@gmail.com)

* Wed Dec 16 2015 Eric D. Helms <ericdhelms@gmail.com> 0.0.19-1
- Refs #12846: bump hammer_cli_katello to 0.0.19 (ericdhelms@gmail.com)

* Fri Sep 25 2015 Justin Sherrill <jsherril@redhat.com> 0.0.18-3
- updating hammer_cli_katello to match gem deps (jsherril@redhat.com)

* Wed Sep 23 2015 Eric D. Helms <ericdhelms@gmail.com> 0.0.18-1
- Update rubygem-hammer_cli_katello to 0.0.18 (ericdhelms@gmail.com)

* Fri Aug 28 2015 Eric D. Helms <ericdhelms@gmail.com> 0.0.17-4
- Update rubygem-hammer_cli_katello to tfm SCl (ericdhelms@gmail.com)

* Thu Aug 06 2015 Eric D. Helms <ericdhelms@gmail.com> 0.0.17-1
- Update rubygem-hammer_cli_katello to 0.0.17 (ericdhelms@gmail.com)

* Fri Jul 31 2015 Eric D. Helms <ericdhelms@gmail.com> 0.0.16-2
- Fixes #11259: Move hammer packages to SCL (ericdhelms@gmail.com)

* Wed Jul 29 2015 Eric D. Helms <ericdhelms@gmail.com> 0.0.16-1
- new package built with tito

* Tue Jul 07 2015 Stephen Benjamin <stbenjam@redhat.com> 0.0.15-1
- Version bump to 0.0.15 (stbenjam@redhat.com)
- fixes #10948 - fix text for Limit field, BZ 1214675 (komidore64@gmail.com)
- Merge pull request #295 from ehelms/fixes-10600 (eric.d.helms@gmail.com)
- Merge pull request #298 from adamruzicka/10561-repository_upload
  (eric.d.helms@gmail.com)
- Fixes #10561,BZ1206734 - repository content-upload opens files one by one
  (aruzicka@redhat.com)
- refs #10628 - add org back to content-view version commands, bz 1223086
  (komidore64@gmail.com)
- refs #10628 - add orgs and CVs back to puppet_module list, bz 1223086
  (komidore64@gmail.com)
- refs #10628 - adding back organization for puppet-module info, bz 1223086
  (komidore64@gmail.com)
- refs #10628 - adding back content-view[-id], BZ 1223086
  (komidore64@gmail.com)
- Fixes #10600: Cleanup incremental update options. (ericdhelms@gmail.com)

* Tue May 26 2015 Adam Price <komidore64@gmail.com> 0.0.14-1
- fixes #10499 - switch content-host errata list to use correct resource
  (jsherril@redhat.com)
- fixes #10473 - do not support prior id on environment update
  (jsherril@redhat.com)
- Fixes #10456: Set composite to false if user does not specify it.
  (ericdhelms@gmail.com)

* Fri Apr 24 2015 Adam Price <komidore64@gmail.com> 0.0.13-1
- bump to version 0.0.13 (komidore64@gmail.com)

* Fri Apr 17 2015 Eric D. Helms <ericdhelms@gmail.com> 0.0.12-1
- bump to version 0.0.12 (komidore64@gmail.com)
- Merge pull request #291 from ehelms/fixes-9849 (eric.d.helms@gmail.com)
- Merge pull request #289 from cfouant/cv-cli (cfouant@redhat.com)
- Fixes #9849: Prevent users from clearing content host facts unknowingly.
  (ericdhelms@gmail.com)
- fixes #9736 - fixes content-view-version param interfering with erratum
  commands, BZ1201352 (cfouant@redhat.com)
- Fixes #9995: Only send content IDs that user passes during incremental
  update. (ericdhelms@gmail.com)
- Add releasers for tito. (ericdhelms@gmail.com)

* Fri Mar 27 2015 Eric D. Helms <ericdhelms@gmail.com> 0.0.11-1
- bump to version 0.0.11 (komidore64@gmail.com)
- refs #9628 - need to use params instead of options (komidore64@gmail.com)

* Tue Mar 24 2015 Eric D. Helms <ericdhelms@gmail.com> 0.0.10-1
- bump to version 0.0.10 (komidore64@gmail.com)
- Merge pull request #287 from komidore64/bz1189478 (komidore64@gmail.com)
- Merge pull request #284 from stbenjam/9679 (stephen@bitbin.de)
- Merge pull request #282 from komidore64/new-version (komidore64@gmail.com)
- Merge pull request #280 from omaciel/master (komidore64@gmail.com)
- Fixes #9819 - No default values for Sync Plans. (omaciel@ogmaciel.com)
- Merge pull request #285 from daviddavis/temp/20150312110618
  (david@memorious.net)
- fixes #9628 - hcli-katello now accepts --prior or --prior-id, BZ1189478
  (komidore64@gmail.com)
- Merge pull request #281 from parthaa/containers (parthaa@gmail.com)
- Fixes #9732: Update incremental update based on server API changes.
  (ericdhelms@gmail.com)
- Fixes #9728 - Adding dependencies for hammer_cli_foreman_docker
  (daviddavis@redhat.com)
- fixes #9679 - fix host collection erratum install (stbenjam@redhat.com)
- Fixes #9666 - hammer content-host info having blank "Release Version" every
  time (pmoravec@redhat.com)
- Refs #9518, #9310 - Show container repo image name (paji@redhat.com)

* Thu Mar 05 2015 Adam Price <komidore64@gmail.com> 0.0.9-1
- Merge pull request #279 from parthaa/cdn-enablement (parthaa@gmail.com)
- Merge pull request #272 from eLobato/patch-1 (david@memorious.net)
- Refs #7796 - Shows docker registry names for CDN enablement (paji@redhat.com)
- Merge pull request #276 from mbacovsky/8227_docker_moved
  (david@memorious.net)
- Merge pull request #278 from Katello/9537 (walden@redhat.com)
- Fixes #9537: update help text for host collection erratum, BZ1179473.
  (walden@redhat.com)
- Refs #8227 - docker commands moved to separate plugin
  (martin.bacovsky@gmail.com)
- Fixes #9183 - Remove duplicate key for content_view (elobatocs@gmail.com)

* Tue Feb 24 2015 Eric D. Helms <ericdhelms@gmail.com> 0.0.8-1
- Version bump to 0.0.8 (ericdhelms@gmail.com)
- fixes #9504 - rename available to installable (stbenjam@redhat.com)
- Merge pull request #271 from daviddavis/temp/20150127110109
  (david@memorious.net)
- Fixes #8203, #9226 - Docker counts displayed on repo info (paji@redhat.com)
- Merge pull request #274 from ehelms/fixes-8190 (eric.d.helms@gmail.com)
- Fixes #8190: Show incremental updates for given content host.
  (ericdhelms@gmail.com)
- Fixes #8179,#8193: Add ability to incrementally update a content view
  version. (ericdhelms@gmail.com)
- Fixes #9133 - Fixing docker tag name field in CLI (daviddavis@redhat.com)
- Merge pull request #267 from cfouant/auto-attach (cfouant@redhat.com)
- fixes #9008 - fixing content-view puppet-module add (jsherril@redhat.com)
- Merge pull request #258 from daviddavis/temp/20141202134530
  (daviddavis@redhat.com)
- Merge pull request #260 from daviddavis/temp/20141204105103
  (daviddavis@redhat.com)
- Merge pull request #266 from daviddavis/temp/20150106162616
  (daviddavis@redhat.com)
- fixes #8913 - add back content view options for content view version promote
  (jsherril@redhat.com)
- fixes #8891 - adds auto-attach to cli output, BZ1180285 (cfouant@redhat.com)
- Refs #8632 - Updating docker attributes (daviddavis@redhat.com)
- Fixes #8583 - Renaming id attribute to avoid lookup (daviddavis@redhat.com)
- Fixes #8547 - Showing error when no env params (daviddavis@redhat.com)

* Fri Dec 19 2014 Adam Price <komidore64@gmail.com> 0.0.7-1
- new package built with tito

* Wed Jun 11 2014 Jason Montleon <jmontleo@redhat.com> 0.0.4-6
- Fixes #6096 - override sub --system-id description (dtsang@redhat.com)
- Fixes #6071 - override CH --id desc (dtsang@redhat.com)
- Fixes #6056 - HC override desc create/update sysid (dtsang@redhat.com)
- Fixes #6055 - HC add/remove-content-host take uuid (dtsang@redhat.com)
- Fixes #5794 : Improve how Async commands are done in katello-cli.
  (bkearney@redhat.com)
- Fixes #6101 - lfenv conditional resolv prior (dtsang@redhat.com)
- Fixes #6079, bz 1103958 - Display org name of a capsule env (paji@redhat.com)

* Tue Jun 03 2014 Jason Montleon <jmontleo@redhat.com> 0.0.4-5
- Fixes #5802 HC update/create using system uuids (dtsang@redhat.com)

* Wed May 28 2014 Jason Montleon <jmontleo@redhat.com> 0.0.4-4
- correct hammer_cli_foreman_tasks dependency version (jmontleo@redhat.com)

* Wed May 28 2014 Jason Montleon <jmontleo@redhat.com> 0.0.4-3
- update dependencies in rpm spec for 0.1.1 (jmontleo@redhat.com)

* Wed May 28 2014 Jason Montleon <jmontleo@redhat.com> 0.0.4-2
- Merge remote-tracking branch 'upstream/master' into SATELLITE-6.0.3
  (jmontleo@redhat.com)
- Merge pull request #175 from komidore64/version-bump (komidore64@gmail.com)
- Merge pull request #176 from dustint-rh/product_info_content
  (dtsang@redhat.com)
- Fixes #5893 - Fixes product info's content (dtsang@redhat.com)
- bump to version 0.0.4 (komidore64@gmail.com)

* Wed May 28 2014 Jason Montleon <jmontleo@redhat.com> 0.0.4-1
- update version to 0.0.4 (jmontleo@redhat.com)

* Thu May 22 2014 Jason Montleon <jmontleo@redhat.com> 0.0.3-26
- Merge remote-tracking branch 'upstream/master' into SATELLITE-6.0.3
  (jmontleo@redhat.com)
- Merge pull request #173 from iNecas/capsule (jlsherrill@gmail.com)
- Refs #5821 - address PR issues (inecas@redhat.com)
- Refs #5821 - initial CLI support for the capsule commands (inecas@redhat.com)

* Thu May 22 2014 Jason Montleon <jmontleo@redhat.com> 0.0.3-25
- Merge remote-tracking branch 'upstream/master' into SATELLITE-6.0.3
  (jmontleo@redhat.com)
- Merge pull request #172 from bbuckingham/issue-5771 (bbuckingham@redhat.com)
- Merge pull request #168 from dustint-
  rh/985393_searchables_resolve_by_uuid_only_uuid (dtsang@redhat.com)
- update releasers (jmontleo@redhat.com)
- Fixes #5111 - product info did list options (dtsang@redhat.com)
- Merge pull request #164 from bkearney/bkearney/string_extract
  (komidore64@gmail.com)
- fixes #5771 - lifecycle-environment - fix the behavir of prior environment
  (bbuckingham@redhat.com)
- Fixes #5729 - content-host lookup by uuid (dtsang@redhat.com)
- Fixes #5658 - Latest String Extract (bkearney@redhat.com)

* Sat May 17 2014 Jason Montleon <jmontleo@redhat.com> 0.0.3-24
- Merge remote-tracking branch 'upstream/master' into SATELLITE-6.0.3
  (jmontleo@redhat.com)
- fixes #5598 - hammer cannot list repositories, BZ1094493
  (komidore64@gmail.com)
- Merge pull request #159 from bkearney/bkearney/5597 (bryan.kearney@gmail.com)
- Fixes #5613 - Content Hosts outputs uuid bz1084722 (dtsang@redhat.com)
- Merge pull request #163 from bbuckingham/issue-5601 (bbuckingham@redhat.com)
- Merge pull request #162 from bbuckingham/issue-5602 (bbuckingham@redhat.com)
- fixes #5601, #5603 - host-collections: add support for update and add/remove-
  content-host (bbuckingham@redhat.com)
- Merge pull request #155 from komidore64/rmi5028 (komidore64@gmail.com)
- Merge pull request #161 from bbuckingham/issue-5600 (bbuckingham@redhat.com)
- Merge pull request #160 from dustint-rh/update_readme_with_tasks
  (dtsang@redhat.com)
- fixes #5602 - host-collections: add command to list content-hosts
  (bbuckingham@redhat.com)
- fixes #5600 - fix host-collection copy command (bbuckingham@redhat.com)
- update README to also pull down hammer-cli-foreman-tasks (dtsang@redhat.com)
- Fixes #5597 - Exposes new data in the repository-set info command
  (bkearney@redhat.com)
- refs #5028 - organizations aren't a special case anymore
  (komidore64@gmail.com)

* Wed May 14 2014 Jason Montleon <jmontleo@redhat.com> 0.0.3-23
- fixes #5600 - fix host-collection copy command (bbuckingham@redhat.com)
- refs #5028 - organizations aren't a special case anymore
  (komidore64@gmail.com)

* Thu May 08 2014 Jason Montleon <jmontleo@redhat.com> 0.0.3-22
- Merge remote-tracking branch 'upstream/master' into SATELLITE-6.0.3
  (jmontleo@redhat.com)
- Merge pull request #158 from bbuckingham/issue-5192 (bbuckingham@redhat.com)
- fixes #5192 - rename system-group to host-collection (bbuckingham@redhat.com)

* Wed May 07 2014 Jason Montleon <jmontleo@redhat.com> 0.0.3-21
- Merge remote-tracking branch 'upstream/master' into SATELLITE-6.0.3
  (jmontleo@redhat.com)
- Merge pull request #157 from iNecas/repository-set-available
  (inecas@redhat.com)
- Merge pull request #152 from dustint-
  rh/bz1077893_redmine_5008_add_manifest_history (dtsang@redhat.com)
- Fixes #5569 - support --name for repository-set available-repositories
  (inecas@redhat.com)
- Refs #5008 adds manifest history to subscriptions and organization
  (dtsang@redhat.com)

* Tue May 06 2014 Jason Montleon <jmontleo@redhat.com> 0.0.3-20
- Merge remote-tracking branch 'upstream/master' into SATELLITE-6.0.3
  (jmontleo@redhat.com)
- Merge pull request #156 from dustint-
  rh/bz985393_redmine5432_add_system_group_delete_command (dtsang@redhat.com)
- Fixed #5546 system_group info missing Total System (dtsang@redhat.com)
- Fixes #5432 adding system group delete command (dtsang@redhat.com)
- Merge pull request #153 from komidore64/rmi4919 (komidore64@gmail.com)
- Fixes #5199 - Add env and cv to output columns to Activation Key list command
  (dtsang@redhat.com)
- fixes #4919 - hammer systemgroup info has NO params, BZ1080475
  (komidore64@gmail.com)
- Refs #4311 - removing old scoped names functionality (tstrachota@redhat.com)
- refs #4311 - including `label` for organization lookup (komidore64@gmail.com)
- refs #4311 - making rubocop happy (komidore64@gmail.com)
- removed log_api_calls setting (tstrachota@redhat.com)
- fix in String#format (tstrachota@redhat.com)
- Refs #4311 - read and write commands merged (tstrachota@redhat.com)
- exception handler - process foreman style messages (tstrachota@redhat.com)
- Refs #4311 - searchables, id resolver and option builders
  (tstrachota@redhat.com)

* Mon May 05 2014 Jason Montleon <jmontleo@redhat.com> 0.0.3-19
- fix macros to work with RHEL 7 (jmontleo@redhat.com)

* Wed Apr 30 2014 Jason Montleon <jmontleo@redhat.com> 0.0.3-18
- Merge remote-tracking branch 'upstream/master' into SATELLITE-6.0.3
  (jmontleo@redhat.com)
- Merge pull request #150 from komidore64/rubocop (komidore64@gmail.com)
- fixes #5462 - adding some rubocop directives (komidore64@gmail.com)
- Merge pull request #105 from bkearney/bkearney/zanata
  (bryan.kearney@gmail.com)
- Merge pull request #143 from iNecas/reposet-enable (inecas@redhat.com)
- Merge pull request #147 from daviddavis/temp/20140423175044
  (daviddavis@redhat.com)
- Fixes #5433 - Display redhat repo url (paji@redhat.com)
- Fixes #5420 - Fixes bad grammar message (daviddavis@redhat.com)
- Fixes #5415 - Fixed problems with cv destroy commands (daviddavis@redhat.com)
- Refs #4826 - Update cli to support new reposet approach (inecas@redhat.com)
- Add zanata translation information (bkearney@redhat.com)

* Wed Apr 23 2014 Jason Montleon <jmontleo@redhat.com> 0.0.3-17
- Merge remote-tracking branch 'upstream/master' into SATELLITE-6.0.3
  (jmontleo@redhat.com)
- fixes #5182 - Rename Systems to Content Hosts (bbuckingham@redhat.com)

* Thu Apr 17 2014 Jason Montleon <jmontleo@redhat.com> 0.0.3-16
- Merge remote-tracking branch 'upstream/master' into SATELLITE-6.0.3
  (jmontleo@redhat.com)
- Merge pull request #141 from daviddavis/cvv_deletion (daviddavis@redhat.com)
- Refs #4811 - Allow users to delete content views from CLI
  (daviddavis@redhat.com)
- Merge pull request #134 from komidore64/bz1078866 (komidore64@gmail.com)
- Fixes #5135 BZ 1085541; removed duplicate output. (omaciel@ogmaciel.com)
- Refs #4957 - Allow users to delete content view versions
  (daviddavis@redhat.com)
- Merge pull request #132 from daviddavis/temp/20140402123025
  (daviddavis@redhat.com)
- Merge pull request #140 from daviddavis/cve-deletion (daviddavis@redhat.com)
- Merge pull request #136 from daviddavis/temp/20140405071614
  (daviddavis@redhat.com)
- Fixes #5048 - Fixing help text for composite option (daviddavis@redhat.com)
- Fixes #5092 - Updating README with new config structure
  (daviddavis@redhat.com)
- Refs #4818 - Allow users to remove a content view from environment
  (daviddavis@redhat.com)
- Fixes #5070 - Disabling name for associate commands (daviddavis@redhat.com)
- Fixes #5032 - hammer organization <info,list> --help types information
  doubled, 1078866 (komidore64@gmail.com)

* Thu Apr 03 2014 Jason Montleon <jmontleo@redhat.com> 0.0.3-15
- Merge remote-tracking branch 'upstream/master' into SATELLITE-6.0.3
  (jmontleo@redhat.com)
- Fixes #4984, #5001, #5010 - Repo enable/disable (paji@redhat.com)

* Wed Apr 02 2014 Jason Montleon <jmontleo@redhat.com> 0.0.3-14
- Merge remote-tracking branch 'upstream/master' into SATELLITE-6.0.3
  (jmontleo@redhat.com)
- Merge pull request #122 from bkearney/bkearney/more-product-changes
  (komidore64@gmail.com)
- Merge pull request #128 from parthaa/good-bye-provider (komidore64@gmail.com)
- Fixes #4295 - Removing provider subcommands (paji@redhat.com)
- Fixes #4908 - Address provider and reposet usage testing
  (bkearney@redhat.com)

* Tue Apr 01 2014 Jason Montleon <jmontleo@redhat.com> 0.0.3-13
- Merge remote-tracking branch 'upstream/master' (jmontleo@redhat.com)
- Merge pull request #129 from parthaa/repo-crud (daviddavis@redhat.com)
- Fixes #4798 - Subscriptions and system groups for activation keys
  (thomasmckay@redhat.com)
- Fixes #4936 - Added repo info, update, delete ops (paji@redhat.com)

* Mon Mar 31 2014 Jason Montleon <jmontleo@redhat.com> 0.0.3-12
- Merge remote-tracking branch 'upstream/master' (jmontleo@redhat.com)
- Fixes #4953 - Show sync plan description (daviddavis@redhat.com)
- Merge pull request #127 from bkearney/bkearney/sync-plan-changes
  (bryan.kearney@gmail.com)
- Changes to sync plan based on usage. (bkearney@redhat.com)

* Thu Mar 27 2014 Jason Montleon <jmontleo@redhat.com> 0.0.3-11
- update confdir (jmontleo@redhat.com)

* Thu Mar 27 2014 Jason Montleon <jmontleo@redhat.com> 0.0.3-10
- update yml config location (jmontleo@redhat.com)

* Wed Mar 26 2014 Jason Montleon <jmontleo@redhat.com> 0.0.3-9
- Merge remote-tracking branch 'upstream/master' (jmontleo@redhat.com)
- Merge pull request #123 from daviddavis/temp/20140325083248
  (daviddavis@redhat.com)
- Merge remote-tracking branch 'upstream/master' (jmontleo@redhat.com)
- fixes #4885 - updated hammer-cli-katello deps (komidore64@gmail.com)
- Fixes #4837 - Adding i18n to strings (daviddavis@redhat.com)

* Wed Mar 26 2014 Jason Montleon <jmontleo@redhat.com> 0.0.3-8
- update rpm spec file to match upstream and add katello.yml config
  (jmontleo@redhat.com)
- update hammer_cli_foreman dependency (jmontleo@redhat.com)

* Wed Mar 26 2014 Jason Montleon <jmontleo@redhat.com>
- update rpm spec file to match upstream and add katello.yml config
  (jmontleo@redhat.com)
- update hammer_cli_foreman dependency (jmontleo@redhat.com)

* Wed Mar 26 2014 Jason Montleon <jmontleo@redhat.com>
- update rpm spec file to match upstream and add katello.yml config
  (jmontleo@redhat.com)
- update hammer_cli_foreman dependency (jmontleo@redhat.com)

* Wed Mar 26 2014 Jason Montleon <jmontleo@redhat.com>
- update rpm spec file to match upstream and add katello.yml config
  (jmontleo@redhat.com)
- update hammer_cli_foreman dependency (jmontleo@redhat.com)

* Wed Mar 26 2014 Jason Montleon <jmontleo@redhat.com>
- update rpm spec file to match upstream and add katello.yml config
  (jmontleo@redhat.com)
- update hammer_cli_foreman dependency (jmontleo@redhat.com)

* Wed Mar 26 2014 Jason Montleon <jmontleo@redhat.com>
- update rpm spec file to match upstream and add katello.yml config
  (jmontleo@redhat.com)
- update hammer_cli_foreman dependency (jmontleo@redhat.com)

* Wed Mar 26 2014 Jason Montleon <jmontleo@redhat.com>
- update rpm spec file to match upstream and add katello.yml config
  (jmontleo@redhat.com)
- update hammer_cli_foreman dependency (jmontleo@redhat.com)

* Tue Feb 04 2014 Jason Montleon <jmontleo@redhat.com> 0.0.3-1
- update hammer_cli_katello to 0.0.3 (jmontleo@redhat.com)

* Thu Jan 30 2014 Jason Montleon <jmontleo@redhat.com> 0.0.2-4
- add missing katello_api dependency (jmontleo@redhat.com)

* Mon Jan 27 2014 Jason Montleon <jmontleo@redhat.com> 0.0.2-3
- fix packaging error (jmontleo@redhat.com)

* Mon Jan 27 2014 Jason Montleon <jmontleo@redhat.com> 0.0.2-2
- new package built with tito

