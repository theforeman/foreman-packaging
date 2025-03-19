# template: foreman_plugin
%global gem_name foreman_virt_who_configure
%global plugin_name virt_who_configure
%global foreman_min_version 3.13

Name: rubygem-%{gem_name}
Version: 0.5.26
Release: 1%{?foremandist}%{?dist}
Summary: A plugin to make virt-who configuration easy
License: GPLv3
URL: https://github.com/theforeman/foreman_virt_who_configure
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: foreman >= %{foreman_min_version}
BuildRequires: foreman-assets >= %{foreman_min_version}
BuildRequires: foreman-plugin >= %{foreman_min_version}
Requires: ruby
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildRequires: rubygem(katello)
BuildArch: noarch
Provides: foreman-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

%description
A plugin to make virt-who configuration easy.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%foreman_bundlerd_file
%foreman_precompile_plugin -s

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_instdir}/app
%{gem_instdir}/config
%{gem_instdir}/db
%{gem_libdir}
%{gem_instdir}/locale
%exclude %{gem_cache}
%{gem_spec}
%{foreman_bundlerd_plugin}
%{foreman_assets_plugin}
%{foreman_assets_foreman}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%posttrans
%{foreman_plugin_log}

%changelog
* Wed Mar 19 2025 Foreman Packaging Automation <packaging@theforeman.org> - 0.5.26-1
- Update to 0.5.26

* Tue Nov 05 2024 Chris Roberts <chrobert@redhat.com> - 0.5.25-1
- Update to 0.5.25

* Fri Sep 20 2024 Foreman Packaging Automation <packaging@theforeman.org> - 0.5.24-1
- Update to 0.5.24

* Tue Aug 20 2024 Chris Roberts <chrobert@redhat.com> - 0.5.23-1
- Update to 0.5.23

* Wed May 22 2024 Chris Roberts <chrobert@redhat.com> - 0.5.22-1
- Update to 0.5.22

* Tue Feb 27 2024 Chris Roberts <chrobert@redhat.com> - 0.5.21-1
- Update to 0.5.21

* Thu Jan 18 2024 Chris Roberts <chrobert@redhat.com> - 0.5.20-1
- Update to 0.5.20

* Sun Dec 03 2023 Foreman Packaging Automation <packaging@theforeman.org> 0.5.19-1
- Update to 0.5.19

* Wed Sep 27 2023 Chris Roberts <chrobert@redhat.com> 0.5.18-1
- Update to 0.5.18

* Wed Sep 06 2023 Foreman Packaging Automation <packaging@theforeman.org> 0.5.17-1
- Update to 0.5.17

* Sun Aug 06 2023 Foreman Packaging Automation <packaging@theforeman.org> 0.5.16-1
- Update to 0.5.16

* Sun Jun 18 2023 Foreman Packaging Automation <packaging@theforeman.org> 0.5.15-1
- Update to 0.5.15

* Wed May 24 2023 William Bradford Clark <wclark@redhat.com> 0.5.14-1
- Update to 0.5.14

* Thu Feb 23 2023 Chris Roberts <chrobert@redhat.com> 0.5.13-1
- Update to 0.5.13

* Wed Jan 04 2023 Chris Roberts <chrobert@redhat.com> 0.5.12-1
- Update to 0.5.12

* Fri Dec 02 2022 Chris Roberts <chrobert@redhat.com> 0.5.11-1
- Update to 0.5.11

* Thu Nov 10 2022 Foreman Packaging Automation <packaging@theforeman.org> 0.5.10-1
- Update to 0.5.10

* Wed Aug 24 2022 Evgeni Golov - 0.5.9-2
- Refs #35409 - Include sprockets assets

* Wed Jul 13 2022 Chris Roberts <chrobert@redhat.com> 0.5.9-1
- Update to 0.5.9

* Fri Apr 22 2022 Eric D. Helms <ericdhelms@gmail.com> - 0.5.8-2
- Stop generaing apipie cache

* Wed Nov 10 2021 Jonathon Turel <jturel@gmail.com> 0.5.8-1
- Update to 0.5.8

* Wed Jul 28 2021 Jonathon Turel <jturel@gmail.com> 0.5.7-1
- Update to 0.5.7

* Mon May 10 2021 Jonathon Turel <jturel@gmail.com> - 0.5.6-1
- Update to 0.5.6

* Mon Mar 15 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.5.5-2
- Rebuild for Ruby 2.7

* Mon Dec 14 2020 Jonathon Turel <jturel@gmail.com> 0.5.5-1
- Update to 0.5.5

* Mon Nov 30 2020 Jonathon Turel <jturel@gmail.com> 0.5.4-1
- Update to 0.5.4

* Thu Sep 10 2020 Jonathon Turel <jturel@gmail.com> 0.5.3-1
- Update to 0.5.3

* Mon Mar 02 2020 Marek Hulan <mhulan@redhat.com> 0.5.2-1
- Update to 0.5.2

* Tue Feb 25 2020 Marek Hulan <mhulan@redhat.com> 0.5.1-1
- Update to 0.5.1

* Tue Jan 07 2020 Eric D. Helms <ericdhelms@gmail.com> - 0.5.0-2
- Drop migrate, seed and restart posttans

* Tue Nov 19 2019 Marek Hulan <mhulan@redhat.com> 0.5.0-1
- Update to 0.5.0

* Tue Oct 22 2019 Marek Hulan <mhulan@redhat.com> 0.4.5-1
- Update to 0.4.5

* Thu Sep 19 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.4.4-2
- Regenerate the spec file based on the latest foreman_plugin template

* Mon Sep 09 2019 Marek Hulan <mhulan@redhat.com> 0.4.4-1
- Update to 0.4.4

* Tue Aug 20 2019 Marek Hulan <mhulan@redhat.com> 0.4.3-1
- Update to 0.4.3

* Thu May 23 2019 Marek Hulan <mhulan@redhat.com> 0.4.1-1
- Update to 0.4.1

* Wed Feb 27 2019 Marek Hulan <mhulan@redhat.com> 0.4.0-1
- Update to 0.4.0

* Tue Jan 15 2019 Marek Hulan <mhulan@redhat.com> 0.3.2-1
- Update to 0.3.2

* Fri Nov 23 2018 Marek Hulan <mhulan@redhat.com> 0.3.0-1
- Update to 0.3.0

* Tue Sep 11 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.2.2-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jun 15 2018 Marek Hulan <mhulan@redhat.com> 0.2.2-1
- Update to 0.2.2

* Wed May 30 2018 Marek Hulan <mhulan@redhat.com> 0.2.1-1
- Update to 0.2.1

* Tue Apr 10 2018 Marek Hulan <mhulan@redhat.com> 0.2.0-1
- Update to 0.2.0

* Thu Dec 28 2017 Daniel Lobato Garcia <me@daniellobato.me> 0.1.9-1
- new package built with tito

* Thu Oct 26 2017 Eric D. Helms <ericdhelms@gmail.com> 0.1.8-2
- Fixes #21455 - generate apipie cache during build (mhulan@redhat.com)

* Thu Oct 12 2017 Eric D. Helms <ericdhelms@gmail.com> 0.1.8-1
- Update foreman_virt_who_configure to 0.1.8 (mhulan@redhat.com)

* Tue Sep 26 2017 Justin Sherrill <jsherril@redhat.com> 0.1.7-1
- Update foreman_virt_who_configure to 0.1.7 (mhulan@redhat.com)

* Thu Aug 24 2017 Eric D. Helms <ericdhelms@gmail.com> 0.1.5-1
- Update foreman_virt_who_configure to 0.1.5 (mhulan@redhat.com)
- Update foreman_virt_who_configure to 0.1.4 (mhulan@redhat.com)

* Mon Jun 26 2017 Eric D. Helms <ericdhelms@gmail.com> 0.1.3-1
- Update foreman_virt_who_configure to 0.1.3 (mhulan@redhat.com)

* Tue Jun 13 2017 Eric D. Helms <ericdhelms@gmail.com> 0.1.2-1
- Update foreman_virt_who_configure to 0.1.2 (mhulan@redhat.com)

* Fri May 26 2017 Eric D. Helms <ericdhelms@gmail.com> 0.1.1-1
- Update foreman_virt_who_configure to 0.1.1 (mhulan@redhat.com)

* Thu May 18 2017 Justin Sherrill <jsherril@redhat.com> 0.1.0-1
- Update foreman_virt_who_configure to 0.1.0 (mhulan@redhat.com)

* Wed May 03 2017 Justin Sherrill <jsherril@redhat.com> 0.0.2-2
- Rebuild virt_who_configure for proper tagging (jsherril@redhat.com)

* Wed May 03 2017 Justin Sherrill <jsherril@redhat.com> 0.0.2-1
- Update foreman_virt_who_configure to 0.0.2 (mhulan@redhat.com)

* Thu Apr 06 2017 Eric D. Helms <ericdhelms@gmail.com> 0.0.1-2
-

* Thu Apr 06 2017 Eric D. Helms <ericdhelms@gmail.com> 0.0.1-1
- new package built with tito

