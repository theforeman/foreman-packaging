%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_virt_who_configure
%global plugin_name virt_who_configure

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.2.1
Release: 1%{?foremandist}%{?dist}
Summary: A plugin to make virt-who configuration easy
Group: Applications/Systems
License: GPLv3
URL: https://github.com/theforeman/foreman_virt_who_configure

Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: foreman >= 1.11
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(katello) >= 3.0
BuildRequires: foreman-assets
BuildRequires: foreman-plugin >= 1.11
BuildRequires: %{?scl_prefix}rubygem(katello) >= 3.0
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-%{plugin_name}

%description
A plugin to make virt-who configuration easy.


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

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
%{gem_instdir}/db
%{gem_libdir}
%{gem_instdir}/locale
%foreman_apipie_cache_foreman
%foreman_apipie_cache_plugin
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
%{foreman_db_seed}
%{foreman_restart}
exit 0

%changelog
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

