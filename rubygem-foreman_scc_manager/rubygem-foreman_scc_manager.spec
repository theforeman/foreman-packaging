%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_scc_manager
%global plugin_name scc_manager

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.0.1
Release: 1%{?foremandist}%{?dist}
Summary: Suse Customer Center plugin for Foreman
Group: Applications/Systems
License: GPL-3.0
URL: https://www.orcharhino.com/
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem
Requires: foreman >= 1.13.0
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(foreman-tasks)
Requires: %{?scl_prefix}rubygem(katello) >= 3.2
BuildRequires: foreman-assets
BuildRequires: foreman-plugin >= 1.13
BuildRequires: %{?scl_prefix}rubygem(katello) >= 3.2
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
%setup -n %{gem_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

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
