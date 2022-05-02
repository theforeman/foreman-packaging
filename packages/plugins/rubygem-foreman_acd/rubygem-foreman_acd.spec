# template: foreman_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}
%{!?_root_localstatedir:%global _root_localstatedir %{_localstatedir}}

%global gem_name foreman_acd
%global plugin_name acd
%global foreman_min_version 2.1

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.9.2.3
Release: 1%{?foremandist}%{?dist}
Summary: Foreman plugin to provide application centric deployment and self service portal
Group: Applications/Systems
License: GPLv3
URL: https://www.orcharhino.com
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: foreman >= %{foreman_min_version}
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby >= 2.5
Requires: %{?scl_prefix_ruby}ruby < 3
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(foreman_remote_execution) >= 3.3.0
Requires: %{?scl_prefix}rubygem(foreman-tasks) >= 0.10
Requires: %{?scl_prefix}rubygem(git)
BuildRequires: foreman-assets >= %{foreman_min_version}
BuildRequires: foreman-plugin >= %{foreman_min_version}
BuildRequires: %{?scl_prefix}rubygem(foreman_remote_execution) >= 3.3.0
BuildRequires: %{?scl_prefix}rubygem(foreman-tasks) >= 0.10
BuildRequires: %{?scl_prefix}rubygem(git)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby >= 2.5
BuildRequires: %{?scl_prefix_ruby}ruby < 3
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

# start package.json devDependencies BuildRequires
BuildRequires: %{?scl_prefix}npm(@theforeman/builder) >= 10.1.0
BuildRequires: %{?scl_prefix}npm(@theforeman/builder) < 11.0.0
BuildRequires: %{?scl_prefix}npm(babel-plugin-transform-class-properties) >= 6.24.1
BuildRequires: %{?scl_prefix}npm(babel-plugin-transform-class-properties) < 7.0.0
BuildRequires: %{?scl_prefix}npm(babel-preset-env) >= 1.6.0
BuildRequires: %{?scl_prefix}npm(babel-preset-env) < 2.0.0
BuildRequires: %{?scl_prefix}npm(babel-preset-react) >= 6.24.1
BuildRequires: %{?scl_prefix}npm(babel-preset-react) < 7.0.0
BuildRequires: %{?scl_prefix}npm(lodash) >= 4.17.11
BuildRequires: %{?scl_prefix}npm(lodash) < 5.0.0
BuildRequires: %{?scl_prefix}npm(sortabular) >= 1.5.1
BuildRequires: %{?scl_prefix}npm(sortabular) < 2.0.0
BuildRequires: %{?scl_prefix}npm(table-resolver) >= 3.2.0
BuildRequires: %{?scl_prefix}npm(table-resolver) < 4.0.0
# end package.json devDependencies BuildRequires

# start package.json dependencies BuildRequires
# end package.json dependencies BuildRequires

%description
A plugin to bring an user self service portal and application centric deployment to Foreman.

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
%foreman_precompile_plugin -s

mkdir -p %{buildroot}%{_root_localstatedir}/lib/foreman/%{gem_name}/ansible-playbooks/

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
%{foreman_webpack_plugin}
%{foreman_webpack_foreman}
%attr(-,foreman,foreman) %{_root_localstatedir}/lib/foreman/%{gem_name}
%attr(-,foreman,foreman) %{_root_localstatedir}/lib/foreman/%{gem_name}/ansible-playbooks/

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
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
