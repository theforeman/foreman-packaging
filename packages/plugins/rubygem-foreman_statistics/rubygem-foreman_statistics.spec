# template: foreman_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}
%{!?_root_sysconfdir:%global _root_sysconfdir %{_sysconfdir}}

%global gem_name foreman_statistics
%global plugin_name statistics
%global foreman_min_version 3.1.0

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 2.0.1
Release: 3%{?foremandist}%{?dist}
Summary: Add Statistics and Trends
Group: Applications/Systems
License: GPLv3
URL: https://theforeman.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Autoreq: 0

# start specfile generated dependencies
Requires: foreman >= %{foreman_min_version}
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: foreman-assets >= %{foreman_min_version}
BuildRequires: foreman-plugin >= %{foreman_min_version}
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

# start package.json devDependencies BuildRequires
BuildRequires: %{?scl_prefix}npm(@babel/core) >= 7.7.0
BuildRequires: %{?scl_prefix}npm(@babel/core) < 8.0.0
BuildRequires: %{?scl_prefix}npm(@theforeman/builder) >= 8.4.1
BuildRequires: %{?scl_prefix}npm(@theforeman/builder) < 11.0.0
# end package.json devDependencies BuildRequires

# start package.json dependencies BuildRequires
BuildRequires: %{?scl_prefix}npm(react-intl) >= 2.8.0
BuildRequires: %{?scl_prefix}npm(react-intl) < 3.0.0
# end package.json dependencies BuildRequires

%description
Statistics and Trends for Foreman gives users overview of their
infrastructure.


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
* Mon May 09 2022 Evgeni Golov - 2.0.1-3
- log plugin installation in posttrans

* Fri Apr 22 2022 Eric D. Helms <ericdhelms@gmail.com> - 2.0.1-2
- Stop generaing apipie cache

* Mon Feb 14 2022 Ondřej Ezr <oezr@redhat.com> 2.0.1-1
- Update to 2.0.1

* Sun Oct 31 2021 Ondřej Ezr <oezr@redhat.com> 2.0.0-1
- Update to 2.0.0

* Mon Aug 16 2021 Ondřej Ezr <oezr@redhat.com> 1.2.0-1
- Update to 1.2.0

* Fri Apr 16 2021 Evgeni Golov - 1.1.1-2
- Drop theforeman/builder upper bound from BuildRequires
- Rebuild for Ruby 2.7

* Thu Feb 04 2021 Ondřej Ezr <oezr@redhat.com> 1.1.1-1
- Update to 1.1.1

* Mon Aug 10 2020 Ondřej Ezr <oezr@redhat.com> 1.0.0-1
- Update to 1.0.0

* Wed Jul 22 2020 Ondřej Ezr <oezr@redhat.com> 0.1.3-1
- Update to 0.1.3-1

* Thu Jun 18 2020 Ondřej Ezr <oezr@redhat.com> 0.1.1-1
- Add rubygem-foreman_statistics generated by gem2rpm using the foreman_plugin template

