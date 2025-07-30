# template: foreman_plugin
%global gem_name foreman_snapshot_management
%global plugin_name snapshot_management
%global foreman_min_version 3.13

Name: rubygem-%{gem_name}
Version: 4.1.0
Release: 1%{?foremandist}%{?dist}
Summary: Snapshot Management for machines on virtualization-platforms
License: GPLv3
URL: https://www.orcharhino.com
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: foreman >= %{foreman_min_version}
BuildRequires: foreman-assets >= %{foreman_min_version}
BuildRequires: foreman-plugin >= %{foreman_min_version}
Requires: ruby >= 2.5
BuildRequires: ruby >= 2.5
BuildRequires: rubygems-devel
BuildArch: noarch
Provides: foreman-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

# start package.json devDependencies BuildRequires
BuildRequires: (npm(@babel/core) >= 7.7.0 with npm(@babel/core) < 8.0.0)
BuildRequires: npm(@theforeman/builder) >= 12.0.1
# end package.json devDependencies BuildRequires

# start package.json dependencies BuildRequires
# end package.json dependencies BuildRequires

%description
Foreman-plugin to manage snapshots in a virtual-hardware environments.


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
%{gem_libdir}
%{gem_instdir}/locale
%exclude %{gem_instdir}/package.json
%exclude %{gem_instdir}/webpack
%exclude %{gem_cache}
%{gem_spec}
%{foreman_bundlerd_plugin}
%{foreman_assets_plugin}
%{foreman_assets_foreman}
%{foreman_webpack_plugin}
%{foreman_webpack_foreman}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%posttrans
%{foreman_plugin_log}

%changelog
* Wed Jul 30 2025 Foreman Packaging Automation <packaging@theforeman.org> - 4.1.0-1
- Update to 4.1.0

* Tue Jul 15 2025 Evgeni Golov - 4.0.0-2
- Rebuild for removal of theforeman/vendor

* Sun Oct 27 2024 Foreman Packaging Automation <packaging@theforeman.org> - 4.0.0-1
- Update to 4.0.0

* Wed Apr 17 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.0.1-1
- Update to 3.0.1

* Wed Mar 27 2024 Evgeni Golov - 3.0.0-2
- Rebuild for Webpack 5

* Mon Jan 08 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.0.0-1
- Update to 3.0.0

* Thu Jun 29 2023 Nadja Heitmann <nadjah@atix.de> 2.0.3-2
- Regenerate RPM spec based on latest template

* Fri Feb 17 2023 Markus Bucher <bucher@atix.de> 2.0.3-1
- Update to 2.0.3

* Mon Oct 31 2022 Markus Bucher <bucher@atix.de> - 2.0.2-2
- Drop apipie:cache generation during build

* Fri Oct 07 2022 Bernhard Suttner <suttner@atix.de> 2.0.2-1
- Update to 2.0.2

* Wed Aug 24 2022 Evgeni Golov - 2.0.1-2
- Refs #35409 - Include sprockets assets

* Thu Jul 15 2021 Markus Bucher <bucher@atix.de> 2.0.1-1
- Update to 2.0.1

* Mon May 10 2021 Markus Bucher <bucher@atix.de> 2.0.0-1
- Update to 2.0.0
- Switch to React-UI

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.7.1-2
- Rebuild plugins for Ruby 2.7

* Mon Mar 02 2020 Markus Bucher <bucher@atix.de> 1.7.1-1
- Update to 1.7.1
- Proxmox support
- Update translations

* Wed Jan 22 2020 Matthias Dellweg <dellweg@atix.de> 1.7.0-1
- Update to 1.7.0
- Remove dependency on deface
- Update translations

* Fri Jan 17 2020 Eric D. Helms <ericdhelms@gmail.com> - 1.6.0-2
- Drop posttrans macros

* Thu Apr 11 2019 Matthias Dellweg <dellweg@atix.de> 1.6.0-1
- Update to 1.6.0
- Add compatibility workaround for foreman-1.22 (timogoebel)

* Fri Oct 19 2018 Matthias Dellweg <dellweg@atix.de> 1.5.1-1
- Update to 1.5.1

* Fri Sep 07 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.5.0-3
- Rebuild for Rails 5.2 and Ruby 2.5

* Mon May 28 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.5.0-2
- Regenerate spec file based on the current template

* Fri May 25 2018 Matthias Dellweg <dellweg@atix.de> 1.5.0-1
- Update to 1.5.0
- Add a bulk action for snapshots

* Thu Apr 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.4.0-1
- Update to 1.4.0

* Wed Jan 10 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.3.0-2
- Bump Foreman plugins release (ericdhelms@gmail.com)

* Fri Dec 15 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.3.0-1
- Update foreman_snapshot_management to 1.3.0 (mail@timogoebel.name)

* Tue Sep 26 2017 Daniel Lobato Garcia <me@daniellobato.me> 1.1.0-1
- Update foreman_snapshot_management to 1.1.0 (mail@timogoebel.name)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Tue Aug 15 2017 Eric D. Helms <ericdhelms@gmail.com> 1.0.0-1
- new package built with tito
