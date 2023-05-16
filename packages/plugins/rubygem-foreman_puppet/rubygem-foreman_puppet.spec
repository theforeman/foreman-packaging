# template: foreman_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}
%{!?_root_sysconfdir:%global _root_sysconfdir %{_sysconfdir}}

%global gem_name foreman_puppet
%global plugin_name puppet
%global foreman_min_version 3.5.0
%global release 1

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 5.1.2
Release: %{?prerelease:0.}%{release}%{?prerelease}%{?foremandist}%{?dist}
Summary: Adds puppet ENC features
Group: Applications/Systems
License: GPLv3
URL: https://theforeman.org
Source0: https://rubygems.org/downloads/%{gem_name}-%{version}%{?prerelease}.gem

Autoreq: 0

# start specfile generated dependencies
Requires: foreman >= %{foreman_min_version}
Requires: ruby
BuildRequires: foreman-assets >= %{foreman_min_version}
BuildRequires: foreman-plugin >= %{foreman_min_version}
Requires: ruby
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildArch: noarch
Provides: foreman-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

# start package.json devDependencies BuildRequires
BuildRequires: npm(@babel/core) >= 7.7.0
BuildRequires: npm(@babel/core) < 8.0.0
BuildRequires: npm(@theforeman/builder) >= 10.1.0
BuildRequires: npm(jed) >= 1.1.1
BuildRequires: npm(jed) < 2.0.0
# end package.json devDependencies BuildRequires

%description
Allow assigning Puppet environmets and classes to the Foreman Hosts.


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
* Tue May 16 2023 Nadja Heitmann <nadjah@atix.de> 5.1.2-1
- Update to 5.1.2

* Sun Feb 26 2023 Foreman Packaging Automation <packaging@theforeman.org> 5.1.1-1
- Update to 5.1.1

* Thu Feb 23 2023 Foreman Packaging Automation <packaging@theforeman.org> 5.1.0-1
- Update to 5.1.0

* Tue Nov 22 2022 Ron Lavi <1ronlavi@gmail.com> 5.0.0-1
- Update to 5.0.0

* Thu Sep 01 2022 Ron Lavi <1ronlavi@gmail.com> 4.0.3-1
- Update to 4.0.3

* Wed Aug 24 2022 Evgeni Golov - 4.0.2-2
- Refs #35409 - Include sprockets assets

* Tue Aug 16 2022 Foreman Packaging Automation <packaging@theforeman.org> 4.0.2-1
- Update to 4.0.2

* Fri Jun 03 2022 Nadja Heitmann <nadjah@atix.de> 4.0.1-1
- Update to 4.0.1
- Add ENC preview tab for Host details

* Wed May 25 2022 Nadja Heitmann <nadjah@atix.de> 4.0.0-1
- Add reports tab to Host details
- Update to 4.0.0

* Mon May 09 2022 Evgeni Golov - 3.0.6-2
- log plugin installation in posttrans

* Thu Apr 28 2022 Nadja Heitmann <nadjah@atix.de> 3.0.6-1
- Update to 3.0.6

* Fri Apr 22 2022 Eric D. Helms <ericdhelms@gmail.com> - 3.0.5-2
- Stop generaing apipie cache

* Fri Mar 11 2022 Foreman Packaging Automation <packaging@theforeman.org> 3.0.5-1
- Update to 3.0.5

* Mon Feb 28 2022 Ondřej Ezr <oezr@redhat.com> 3.0.3-1
- Update to 3.0.3

* Fri Nov 26 2021 Ondřej Ezr <oezr@redhat.com> 3.0.0-1
- Update to 3.0.0

* Mon Nov 15 2021 Ondřej Ezr <oezr@redhat.com> 2.0.0-1
- Update to 2.0.0

* Thu Oct 14 2021 Ondřej Ezr <oezr@redhat.com> 2.0.0-0.1.alpha.2
- Update to 2.0.0.alpha.2

* Fri Sep 17 2021 Ondřej Ezr <oezr@redhat.com> 1.0.3-1
- Update to 1.0.3

* Mon Sep 13 2021 Ondřej Ezr <oezr@redhat.com> 1.0.1-1
- Update to 1.0.1

* Fri Sep 10 2021 Ondřej Ezr <oezr@redhat.com> 1.0.0-1
- Update to 1.0.0

* Mon Aug 16 2021 Ondřej Ezr <oezr@redhat.com> 1.0.0.rc.2-1
- Update to 1.0.0.rc.2

* Thu Jul 15 2021 Ondřej Ezr <oezr@redhat.com> 1.0.0.rc.1-1
- Update to 1.0.0.rc.1

* Thu May 20 2021 Manuel Laug <manuel.laug@dm.de> 0.1.0-1
- Update to 0.1.0

* Fri Apr 16 2021 Evgeni Golov - 0.0.2-2
- Drop theforeman/builder upper bound from BuildRequires
- Rebuild for Ruby 2.7

* Tue Feb 02 2021 Ondřej Ezr <oezr@redhat.com> 0.0.2-1
- Add rubygem-foreman_puppet generated by gem2rpm using the foreman_plugin template

