# template: foreman_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_webhooks
%global plugin_name webhooks
%global foreman_min_version 2.3

Summary:    Plugin for Foreman that allows to configure Webhooks
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    3.0.5
Release:    1%{?foremandist}%{?dist}
Group:      Applications/Systems
License:    GPLv3
URL:        https://github.com/theforeman/foreman_webhooks
Source0:    https://rubygems.org/gems/%{gem_name}-%{version}%{?prever}.gem

# start specfile generated dependencies
Requires: foreman >= %{foreman_min_version}
Requires: ruby >= 2.5.0
BuildRequires: foreman-assets >= %{foreman_min_version}
BuildRequires: foreman-plugin >= %{foreman_min_version}
Requires: ruby >= 2.5.0
BuildRequires: ruby >= 2.5.0
BuildRequires: rubygems-devel
BuildArch: noarch
Provides: foreman-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

# start package.json devDependencies BuildRequires
BuildRequires: npm(@babel/core) >= 7.7.0
BuildRequires: npm(@babel/core) < 8.0.0
BuildRequires: npm(@theforeman/builder) >= 0
BuildRequires: npm(jed) >= 1.1.1
BuildRequires: npm(jed) < 2.0.0
# end package.json devDependencies BuildRequires

%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Plugin for Foreman that allows to configure Webhooks.


%package doc
BuildArch:  noarch
Group:      Documentation
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
Summary:    Documentation for %{pkg_name}

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
%exclude %{gem_cache}
%exclude %{gem_instdir}/package.json
%exclude %{gem_instdir}/webpack
%exclude %{gem_instdir}/Rakefile
%{gem_spec}
%{foreman_bundlerd_plugin}
%{foreman_assets_plugin}
%{foreman_assets_foreman}
%{foreman_webpack_plugin}
%{foreman_webpack_foreman}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/test

%posttrans
%{foreman_plugin_log}

%changelog
* Sun Sep 11 2022 Foreman Packaging Automation <packaging@theforeman.org> 3.0.5-1
- Update to 3.0.5

* Wed Aug 24 2022 Evgeni Golov - 3.0.4-2
- Refs #35409 - Include sprockets assets

* Wed Aug 17 2022 Oleh Fedorenko <ofedoren@redhat.com> 3.0.4-1
- Update to 3.0.4

* Fri Jun 03 2022 Oleh Fedorenko <ofedoren@redhat.com> 3.0.3-1
- Update to 3.0.3

* Mon May 09 2022 Evgeni Golov - 3.0.1-3
- log plugin installation in posttrans

* Fri Apr 22 2022 Eric D. Helms <ericdhelms@gmail.com> - 3.0.1-2
- Stop generaing apipie cache

* Mon Mar 07 2022 Ron Lavi <1ronlavi@gmail.com> 3.0.1-1
- Update to 3.0.1

* Wed Sep 01 2021 Lukas Zapletal <lzap+rpm@redhat.com> 3.0.0-1
- Update to 3.0.0

* Mon May 24 2021 Lukas Zapletal <lzap+rpm@redhat.com> 2.0.0-1
- Update to 2.0.0

* Fri Apr 23 2021 Lukas Zapletal <lzap+rpm@redhat.com> 1.0.0-1
- Update to 1.0.0

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.0.3-2
- Rebuild plugins for Ruby 2.7

* Mon Mar 29 2021 Lukas Zapletal <lzap+rpm@redhat.com> 0.0.3-1
- Update to 0.0.3

* Mon Mar 08 2021 Lukas Zapletal <lzap+rpm@redhat.com> 0.0.2-1
- Update to 0.0.2

* Mon Jan 25 2021 Lukas Zapletal <lzap+rpm@redhat.com> 0.0.1-1
- Initial version
