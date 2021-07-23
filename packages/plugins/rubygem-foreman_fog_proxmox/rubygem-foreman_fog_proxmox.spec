# template: foreman_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_fog_proxmox
%global plugin_name fog_proxmox
%global foreman_min_version 1.22

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.14.0
Release: 1%{?foremandist}%{?dist}
Summary: Foreman plugin that adds Proxmox VE compute resource using fog-proxmox
Group: Applications/Systems
License: GPLv3
URL: https://github.com/theforeman/foreman_fog_proxmox
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: foreman >= %{foreman_min_version}
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(deface)
Requires: %{?scl_prefix}rubygem(fog-proxmox) >= 0.14
Requires: %{?scl_prefix}rubygem(fog-proxmox) < 1
BuildRequires: foreman-assets >= %{foreman_min_version}
BuildRequires: foreman-plugin >= %{foreman_min_version}
BuildRequires: %{?scl_prefix}rubygem(deface)
BuildRequires: %{?scl_prefix}rubygem(fog-proxmox) >= 0.14
BuildRequires: %{?scl_prefix}rubygem(fog-proxmox) < 1
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires(post):   policycoreutils-python-utils
Requires(postun): policycoreutils-python-utils
%else
Requires(post):   policycoreutils-python
Requires(postun): policycoreutils-python
%endif

%description
Foreman plugin adds Proxmox VE compute resource using fog-proxmox. It is
compatible with Foreman 1.22+.


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
%{gem_instdir}/db
%{gem_libdir}
%{gem_instdir}/locale
%exclude %{gem_cache}
%{gem_spec}
%{foreman_bundlerd_plugin}
%{foreman_apipie_cache_foreman}
%{foreman_apipie_cache_plugin}
%{foreman_assets_plugin}

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

%changelog
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

