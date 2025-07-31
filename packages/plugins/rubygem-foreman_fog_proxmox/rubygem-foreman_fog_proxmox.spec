# template: foreman_plugin
%global gem_name foreman_fog_proxmox
%global plugin_name fog_proxmox
%global foreman_min_version 3.15

Name: rubygem-%{gem_name}
Version: 0.19.0
Release: 1%{?foremandist}%{?dist}
Summary: Foreman plugin that adds Proxmox VE compute resource using fog-proxmox
License: GPLv3
URL: https://github.com/theforeman/foreman_fog_proxmox
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: foreman >= %{foreman_min_version}
BuildRequires: foreman-assets >= %{foreman_min_version}
BuildRequires: foreman-plugin >= %{foreman_min_version}
Requires: ruby
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildRequires: rubygem(deface)
BuildRequires: (rubygem(fog-proxmox) >= 0.15.1 with rubygem(fog-proxmox) < 0.16)
BuildArch: noarch
Provides: foreman-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

Requires(post):   policycoreutils-python-utils
Requires(postun): policycoreutils-python-utils

# start package.json devDependencies BuildRequires
BuildRequires: (npm(@babel/core) >= 7.7.0 with npm(@babel/core) < 8.0.0)
BuildRequires: npm(@theforeman/builder) >= 15.0.1
# end package.json devDependencies BuildRequires

# start package.json dependencies BuildRequires
BuildRequires: (npm(react-intl) >= 2.8.0 with npm(react-intl) < 3.0.0)
# end package.json dependencies BuildRequires

%description
Foreman plugin adds Proxmox VE compute resource using fog-proxmox. It is
compatible with Foreman 1.22+.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

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

%post
/sbin/semanage port -a -t http_port_t -p tcp 8006 &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
  /sbin/semanage port -d -t http_port_t -p tcp 8006 &> /dev/null || :
fi

%posttrans
%{foreman_plugin_log}

%changelog
* Thu Jul 31 2025 Foreman Packaging Automation <packaging@theforeman.org> - 0.19.0-1
- Update to 0.19.0

* Tue Jul 15 2025 Evgeni Golov - 0.18.1-2
- Rebuild for removal of theforeman/vendor

* Sun Mar 02 2025 Foreman Packaging Automation <packaging@theforeman.org> - 0.18.1-1
- Update to 0.18.1

* Thu Nov 07 2024 Nadja Heitmann <nadjah@atix.de> - 0.17.1-1
- Update to 0.17.1

* Wed Oct 09 2024 Foreman Packaging Automation <packaging@theforeman.org> - 0.17.0-1
- Update to 0.17.0

* Wed Jul 24 2024 Nadja Heitmann <nadjah@atix.de> 0.16.1-1
- Update to 0.16.1-1
- New enhanced React UI

* Sun Apr 28 2024 Foreman Packaging Automation <packaging@theforeman.org> - 0.15.1-1
- Update to 0.15.1

* Thu Nov 16 2023 Foreman Packaging Automation <packaging@theforeman.org> 0.15.0-1
- Update to 0.15.0

* Sun Aug 27 2023 Foreman Packaging Automation <packaging@theforeman.org> 0.14.3-1
- Update to 0.14.3

* Fri Mar 10 2023 Foreman Packaging Automation <packaging@theforeman.org> 0.14.2-1
- Update to 0.14.2

* Wed Aug 24 2022 Evgeni Golov - 0.14.0-4
- Refs #35409 - Include sprockets assets

* Mon May 09 2022 Evgeni Golov - 0.14.0-3
- log plugin installation in posttrans

* Fri Apr 22 2022 Eric D. Helms <ericdhelms@gmail.com> - 0.14.0-2
- Stop generaing apipie cache

* Fri Jul 23 2021 Tristan Robert <tristan.robert.44@gmail.com> 0.14.0-1
- Update to 0.14.0

* Thu Jul 22 2021 Tristan Robert <tristan.robert.44@gmail.com> 0.13.4-1
- Update to 0.13.4

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.13.3-2
- Rebuild plugins for Ruby 2.7

* Fri Mar 19 2021 Tristan Robert <tristan.robert.44@gmail.com> 0.13.3-1
- Update to 0.13.3

* Tue Aug 25 2020 Tristan Robert <tristan.robert.44@gmail.com> 0.12.4-1
- Update to 0.12.4

* Fri May 15 2020 Tristan Robert <tristan.robert.44@gmail.com> 0.11.1-1
- Update to 0.11.1

* Wed Apr 08 2020 Tristan Robert 0.10.2-1
- Update to 0.10.2

* Thu Jan 30 2020 Tristan Robert <tristan.robert.44@gmail.com> 0.9.4-1
- Update to 0.9.4

* Fri Jan 17 2020 Eric D. Helms <ericdhelms@gmail.com> - 0.9.3-2
- Drop posttrans macros

* Fri Dec 13 2019 Tristan Robert <tristan.robert.44@gmail.com> 0.9.3-1
- Update to 0.9.3

* Tue Jul 23 2019 Matthias Dellweg <dellweg@atix.de> 0.8.0-2
- Manage selinux permissions for proxmox access

* Fri Jul 12 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.8.0-1
- Update to 0.8.0-1

* Thu Jan 03 2019 Tristan Robert <tristan.robert.44@gmail.com> 0.5.5-1
- Update to 0.5.5

* Thu Nov 08 2018 Tristan Robert <tristan.robert.44@gmail.com> 0.5.3-1
- Update to 0.5.3

* Fri Oct 05 2018 Tristan Robert <tristan.robert.44@gmail.com> 0.5.2-1
- Add rubygem-foreman_fog_proxmox generated by gem2rpm using the foreman_plugin template

