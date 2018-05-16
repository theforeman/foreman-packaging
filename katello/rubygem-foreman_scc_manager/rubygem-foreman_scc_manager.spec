%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_scc_manager
%global plugin_name scc_manager

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.3.1
Release: 1%{?foremandist}%{?dist}
Summary: Suse Customer Center plugin for Foreman
Group: Applications/Systems
License: GPL-3.0
URL: https://www.orcharhino.com/
Source0: https://rubygems.org/downloads/%{gem_name}-%{version}.gem
Requires: foreman >= 1.17.0
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(foreman-tasks)
Requires: %{?scl_prefix}rubygem(katello) >= 3.6
BuildRequires: foreman-assets
BuildRequires: foreman-plugin >= 1.17
BuildRequires: %{?scl_prefix}rubygem(katello) >= 3.6
BuildRequires: %{?scl_prefix}rubygem(foreman-tasks)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-%{plugin_name}

%description
Foreman plugin to sync SUSE Customer Center products and repositories into
Katello.


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

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%posttrans
%{foreman_db_migrate}
%{foreman_restart}
/usr/bin/systemctl restart foreman-tasks
exit 0

%changelog
* Wed May 16 2018 Matthias Dellweg <dellweg@atix.de> 1.3.1-1
- Migration to rails 5 by evgeni
- Fix issue with productless account
* Tue May 15 2018 Matthias Dellweg <dellweg@atix.de> 1.3.0-1
- Prevent exception in case no further products were selected
- Show proper sync status
* Mon Mar 19 2018 Matthias Dellweg <dellweg@atix.de> 1.2.0-1
- Change Edit/Action behaviour to be more user-friendly
- Do not use transaction to create Products and Repositories
- Update some dependencies
- Bump requirement to Katello 3.5
- Issue #7 by prokhorovva: Fast fix
- Catch RecordNotFound when assigning extensions
- disable submit if account was not synced
- Bump requirement to foreman 1.16
* Tue Sep 26 2017 Matthias Dellweg <dellweg@atix.de> 1.1.0-1
- Set default download policy
- Force katello to load before scc_manager
- restart foreman-tasks after installation
- Added note to use Organization credentials
- Select organization landing page
* Wed Aug 16 2017 Matthias Dellweg <dellweg@atix.de> 1.0.1-1
- specfile from gem2spec
- fix asset compilation
- encrypted passwords
- use katello_proxy

* Thu Apr 27 2017 Matthias Dellweg <dellweg@atix.de> 1.0.0-3
- Add dependency foreman-tasks

* Mon Apr 03 2017 Bernhard Suttner <suttner@atix.de> 1.0.0-2
- Set correct ruby build requirements

* Tue Mar 21 2017 Matthias Dellweg <dellweg@atix.de> 1.0.0-1
- First release
