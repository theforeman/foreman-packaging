# Generated from foreman_git_templates-1.0.4.gem by gem2rpm -*- rpm-spec -*-
# template: foreman_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}
%{!?_root_sysconfdir:%global _root_sysconfdir %{_sysconfdir}}

%global gem_name foreman_git_templates
%global plugin_name git_templates
%global foreman_min_version 1.20

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 2.0.0
Release: 1%{?foremandist}%{?dist}
Summary: Adds support for using templates from Git repositories
Group: Applications/Systems
License: GPLv3
URL: https://github.com/dm-drogeriemarkt/foreman_git_templates
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: foreman >= %{foreman_min_version}
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(down) >= 4.5
Requires: %{?scl_prefix}rubygem(down) < 5
Requires: %{?scl_prefix}rubygem(rest-client) >= 2
Requires: %{?scl_prefix}rubygem(rest-client) < 3
BuildRequires: foreman-plugin >= %{foreman_min_version}
BuildRequires: %{?scl_prefix}rubygem(down) >= 4.5
BuildRequires: %{?scl_prefix}rubygem(down) < 5
BuildRequires: %{?scl_prefix}rubygem(rest-client) >= 2
BuildRequires: %{?scl_prefix}rubygem(rest-client) < 3
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

%description
Adds support for using templates from Git repositories.


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

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_instdir}/app
%{gem_instdir}/config
%{gem_instdir}/db
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%{foreman_bundlerd_plugin}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%posttrans
%{foreman_plugin_log}

%changelog
* Tue May 14 2024 Manuel Laug <laugmanuel@gmail.com> - 2.0.0-1
- Update foreman_git_templates to 2.0.0

* Mon May 09 2022 Evgeni Golov - 1.0.6-3
- log plugin installation in posttrans

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 1.0.6-2
- Rebuild plugins for Ruby 2.7

* Thu Aug 13 2020 Manuel Laug <manuel.laug@dm.de> - 1.0.6-1
- Update foreman_git_templates to 1.0.6

* Wed Jun 10 2020 Manuel Laug <manuel.laug@dm.de> - 1.0.5-1
- Update foreman_git_templates to 1.0.5

* Mon Feb 10 2020 Manuel Laug <manuel.laug@dm.de> - 1.0.4-1
- Update foreman_git_templates to 1.0.4

* Fri Jan 17 2020 Eric D. Helms <ericdhelms@gmail.com> - 1.0.3-2
- Drop posttrans macros

* Tue Dec 10 2019 Timo Goebel <mail@timogoebel.name> - 1.0.3-1
- Update foreman_git_templates to 1.0.3

* Wed Sep 18 2019 Eric D. Helms <ericdhelms@gmail.com> - 1.0.2-2
- Corrected the license format

* Thu Aug 29 2019 Timo Goebel <mail@timogoebel.name> - 1.0.2-1
- Update foreman_git_templates to 1.0.2

* Wed Apr 17 2019 Timo Goebel <mail@timogoebel.name> - 1.0.1-1
- Update foreman_git_templates to 1.0.1

* Mon Mar 04 2019 Timo Goebel <mail@timogoebel.name> - 1.0.0-1
- Add foreman_git_templates plugin
