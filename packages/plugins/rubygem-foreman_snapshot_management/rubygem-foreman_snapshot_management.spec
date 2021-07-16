# template: foreman_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_snapshot_management
%global plugin_name snapshot_management
%global foreman_min_version 2.0.0

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 2.0.1
Release: 1%{?foremandist}%{?dist}
Summary: Snapshot Management for VMware vSphere
Group: Applications/Systems
License: GPLv3
URL: https://www.orcharhino.com
Source0: https://rubygems.org/downloads/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: foreman >= %{foreman_min_version}
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby >= 2.5
Requires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: foreman-assets >= %{foreman_min_version}
BuildRequires: foreman-plugin >= %{foreman_min_version}
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby >= 2.5
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

# start package.json devDependencies BuildRequires
BuildRequires: %{?scl_prefix}npm(@babel/core) >= 7.7.0
BuildRequires: %{?scl_prefix}npm(@babel/core) < 8.0.0
BuildRequires: %{?scl_prefix}npm(@theforeman/builder) >= 4.0.0
BuildRequires: %{?scl_prefix}npm(@theforeman/builder) < 9.0.0
# end package.json devDependencies BuildRequires

# start package.json dependencies BuildRequires
BuildRequires: %{?scl_prefix}npm(react-intl) >= 2.8.0
BuildRequires: %{?scl_prefix}npm(react-intl) < 3.0.0
# end package.json dependencies BuildRequires

%description
Foreman-plugin to manage snapshots on hosts on a VMWare or Proxmox compute resource.


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
%foreman_precompile_plugin -a -s

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
%{foreman_apipie_cache_foreman}
%{foreman_apipie_cache_plugin}
%{foreman_assets_plugin}
%{foreman_webpack_plugin}
%{foreman_webpack_foreman}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
* Thu Jul 15 2021 Markus Bucher <bucher@atix.de> 2.0.1-1
- Update to 2.0.1

* Mon May 10 2021 Markus Bucher <bucher@atix.de> 2.0.0-1
- Update to 2.0.0
- Switch to React-UI

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
