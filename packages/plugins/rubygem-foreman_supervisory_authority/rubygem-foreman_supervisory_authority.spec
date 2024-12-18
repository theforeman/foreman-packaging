# Generated from foreman_supervisory_authority-0.0.1.gem by gem2rpm -*- rpm-spec -*-
# template: foreman_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_supervisory_authority
%global plugin_name supervisory_authority
%global foreman_min_version 3.10

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.2.0
Release: 1%{?foremandist}%{?dist}
Summary: This Foreman plug-in integrates with Elastic APM
Group: Applications/Systems
License: GPLv3+
URL: https://github.com/timogoebel/foreman_supervisory_authority
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: foreman >= %{foreman_min_version}
BuildRequires: foreman-plugin >= %{foreman_min_version}
Requires: ruby >= 2.5
Requires: ruby < 4
BuildRequires: ruby >= 2.5
BuildRequires: ruby < 4
BuildRequires: rubygems-devel
BuildArch: noarch
Provides: foreman-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

%description
This plug-in for Foreman sends data to Elastic APM.


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

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_instdir}/app
%{gem_instdir}/config
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
* Wed Dec 18 2024 Foreman Packaging Automation <packaging@theforeman.org> - 0.2.0-1
- Update to 0.2.0

* Mon May 09 2022 Evgeni Golov - 0.0.2-4
- log plugin installation in posttrans

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.0.2-3
- Rebuild plugins for Ruby 2.7

* Fri Jan 17 2020 Eric D. Helms <ericdhelms@gmail.com> - 0.0.2-2
- Drop posttrans macros

* Thu Aug 29 2019 Timo Goebel <mail@timogoebel.name> - 0.0.2-1
- Update foreman_supervisory_authority to 0.0.2

* Fri Jul 19 2019 Timo Goebel <mail@timogoebel.name> 0.0.1-1
- Add rubygem-foreman_supervisory_authority
