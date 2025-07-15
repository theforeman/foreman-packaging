# template: foreman_plugin
%global gem_name foreman_acd
%global plugin_name acd
%global foreman_min_version 3.13

Name: rubygem-%{gem_name}
Version: 0.12.0
Release: 2%{?foremandist}%{?dist}
Summary: Foreman plugin to provide application centric deployment and self service portal
License: GPLv3
URL: https://www.orcharhino.com
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: foreman >= %{foreman_min_version}
BuildRequires: foreman-assets >= %{foreman_min_version}
BuildRequires: foreman-plugin >= %{foreman_min_version}
Requires: ruby >= 2.7
Requires: ruby < 4
BuildRequires: ruby >= 2.7
BuildRequires: ruby < 4
BuildRequires: rubygems-devel
BuildRequires: rubygem(foreman_remote_execution) >= 8.0
BuildRequires: rubygem(foreman-tasks) >= 7.0
BuildRequires: rubygem(git)
BuildArch: noarch
Provides: foreman-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

# start package.json devDependencies BuildRequires
BuildRequires: npm(@theforeman/builder) >= 12.0.1
BuildRequires: (npm(babel-plugin-transform-class-properties) >= 6.24.1 with npm(babel-plugin-transform-class-properties) < 7.0.0)
BuildRequires: (npm(babel-preset-env) >= 1.6.0 with npm(babel-preset-env) < 2.0.0)
BuildRequires: (npm(babel-preset-react) >= 6.24.1 with npm(babel-preset-react) < 7.0.0)
BuildRequires: (npm(lodash) >= 4.17.11 with npm(lodash) < 5.0.0)
BuildRequires: (npm(sortabular) >= 1.5.1 with npm(sortabular) < 2.0.0)
BuildRequires: (npm(table-resolver) >= 3.2.0 with npm(table-resolver) < 4.0.0)
# end package.json devDependencies BuildRequires

# start package.json dependencies BuildRequires
# end package.json dependencies BuildRequires

%description
Foreman plugin to provide application centric deployment and self service
portal.


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

mkdir -p %{buildroot}%{_localstatedir}/lib/foreman/%{gem_name}/ansible-playbooks/

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_instdir}/app
%{gem_instdir}/config
%{gem_instdir}/db
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
%attr(-,foreman,foreman) %{_localstatedir}/lib/foreman/%{gem_name}
%attr(-,foreman,foreman) %{_localstatedir}/lib/foreman/%{gem_name}/ansible-playbooks/

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%posttrans
%{foreman_plugin_log}

%changelog
* Tue Jul 15 2025 Evgeni Golov - 0.12.0-2
- Rebuild for removal of theforeman/vendor

* Thu May 08 2025 Foreman Packaging Automation <packaging@theforeman.org> - 0.12.0-1
- Update to 0.12.0

* Mon Oct 14 2024 Foreman Packaging Automation <packaging@theforeman.org> - 0.11.0-1
- Update to 0.11.0

* Thu Sep 26 2024 Nadja Heitmann <nadjah@atix.de> - 0.10.0-1
- Update to 0.10.0

* Sun Apr 14 2024 Foreman Packaging Automation <packaging@theforeman.org> - 0.9.7-1
- Update to 0.9.7

* Sun Mar 31 2024 Foreman Packaging Automation <packaging@theforeman.org> - 0.9.5-1
- Update to 0.9.5

* Wed Jan 31 2024 Evgeni Golov - 0.9.4-3
- Rebuild for Webpack 5

* Thu Jun 29 2023 Nadja Heitmann <nadjah@atix.de> 0.9.4-2
- Regenerate RPM spec based on latest template

* Mon Jan 16 2023 Bernhard Suttner <suttner@atix.de> 0.9.4-1
- Update to 0.9.4

* Wed Aug 24 2022 Evgeni Golov - 0.9.3-2
- Refs #35409 - Include sprockets assets

* Fri Jul 15 2022 Bernhard Suttner <suttner@atix.de> 0.9.3-1
- Update to 0.9.3

* Mon May 09 2022 Evgeni Golov - 0.9.2.3-2
- log plugin installation in posttrans

* Mon May 02 2022 Bernhard Suttner <suttner@atix.de> 0.9.2.3-1
- Update to 0.9.2.3
- Stop generating apipie cache (Thanks Evgeni G.)

* Tue Oct 05 2021 Bernhard Suttner <suttner@atix.de> 0.9.0-1
- Update to 0.9.0

* Mon May 31 2021 Bernhard Suttner <suttner@atix.de> 0.7.0-1
- Update to 0.7.0

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.6.0-2
- Rebuild plugins for Ruby 2.7

* Tue Mar 09 2021 Bernhard Suttner <suttner@atix.de> 0.6.0-1
- Update to 0.6.0

* Tue Jan 19 2021 Bernhard Suttner <suttner@atix.de> 0.5.0-1
- Update to 0.5.0

* Thu Nov 26 2020 Bernhard Suttner <suttner@atix.de> 0.3.0-1
- Update to 0.3.0

* Tue Jul 21 2020 Evgeni Golov - 0.2.1-3
- Drop posttrans macros

* Tue Jun 30 2020 Evgeni Golov - 0.2.1-2
- Rebuild to properly build on EL7 and EL8

* Fri Jun 26 2020 Bernhard Suttner <suttner@atix.de> 0.2.1-1
- Update to 0.2.1

* Tue Feb 11 2020 Bernhard Suttner <suttner@atix.de> 0.1.0-1
- Update to 0.1.0

* Wed Nov 27 2019 Bernhard Suttner <suttner@atix.de> 0.0.6-1
- Update to 0.0.6

* Wed Nov 27 2019 Bernhard Suttner <suttner@atix.de> 0.0.4-1
- Update to 0.0.4

* Mon Nov 25 2019 Bernhard Suttner <suttner@atix.de> 0.0.3-1
- Update to 0.0.3

* Fri Nov 22 2019 Bernhard Suttner <suttner@atix.de> 0.0.2-1
- Update to 0.0.2

* Fri Nov 22 2019 Bernhard Suttner <suttner@atix.de> 0.0.1-1
- Add rubygem-foreman_acd generated by gem2rpm using the foreman_plugin template
