# template: foreman_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_azure_rm
%global plugin_name azure_rm
%global foreman_min_version 1.17

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 2.2.4
Release: 1%{?foremandist}%{?dist}
Summary: Azure Resource Manager as a compute resource for The Foreman
Group: Applications/Systems
License: GPLv3
URL: https://github.com/theforeman/foreman_azure_rm
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: foreman >= %{foreman_min_version}
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(azure_mgmt_resources) >= 0.18.1
Requires: %{?scl_prefix}rubygem(azure_mgmt_resources) < 0.19
Requires: %{?scl_prefix}rubygem(azure_mgmt_network) >= 0.26.1
Requires: %{?scl_prefix}rubygem(azure_mgmt_network) < 0.27
Requires: %{?scl_prefix}rubygem(azure_mgmt_storage) >= 0.23.0
Requires: %{?scl_prefix}rubygem(azure_mgmt_storage) < 0.24
Requires: %{?scl_prefix}rubygem(azure_mgmt_compute) >= 0.22.0
Requires: %{?scl_prefix}rubygem(azure_mgmt_compute) < 0.23
Requires: %{?scl_prefix}rubygem(azure_mgmt_subscriptions) >= 0.18.5
Requires: %{?scl_prefix}rubygem(azure_mgmt_subscriptions) < 0.19
BuildRequires: foreman-plugin >= %{foreman_min_version}
BuildRequires: %{?scl_prefix}rubygem(azure_mgmt_resources) >= 0.18.1
BuildRequires: %{?scl_prefix}rubygem(azure_mgmt_resources) < 0.19
BuildRequires: %{?scl_prefix}rubygem(azure_mgmt_network) >= 0.26.1
BuildRequires: %{?scl_prefix}rubygem(azure_mgmt_network) < 0.27
BuildRequires: %{?scl_prefix}rubygem(azure_mgmt_storage) >= 0.23.0
BuildRequires: %{?scl_prefix}rubygem(azure_mgmt_storage) < 0.24
BuildRequires: %{?scl_prefix}rubygem(azure_mgmt_compute) >= 0.22.0
BuildRequires: %{?scl_prefix}rubygem(azure_mgmt_compute) < 0.23
BuildRequires: %{?scl_prefix}rubygem(azure_mgmt_subscriptions) >= 0.18.5
BuildRequires: %{?scl_prefix}rubygem(azure_mgmt_subscriptions) < 0.19
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

%description
This gem provides Azure Resource Manager as a compute resource for The
Foreman.


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
%foreman_precompile_plugin -a

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

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile

%changelog
* Fri May 14 2021 Evgeni Golov 2.2.4-1
- Update to 2.2.4

* Tue May 04 2021 Evgeni Golov 2.2.3-1
- Update to 2.2.3

* Tue Apr 13 2021 Evgeni Golov 2.2.2-1
- Update to 2.2.2

* Thu Apr 08 2021 Amit Upadhye <upadhyeammit@gmail.com> 2.2.1-1
- Update to 2.2.1

* Mon Jul 13 2020 Aditi Puntambekar <apuntamb@redhat.com> 2.1.2-1
- Update to 2.1.2

* Tue Jun 09 2020 Aditi Puntambekar <apuntamb@redhat.com> 2.1.1-1
- Update to 2.1.1

* Fri May 15 2020 Aditi Puntambekar <apuntamb@redhat.com> 2.1.0-1
- Update to 2.1.0

* Wed Feb 26 2020 Aditi Puntambekar <apuntamb@redhat.com> 2.0.8-1
- Update to 2.0.8

* Mon Feb 17 2020 Aditi Puntambekar <apuntamb@redhat.com> 2.0.7-1
- Update to 2.0.7

* Thu Jan 23 2020 Aditi Puntambekar <apuntamb@redhat.com> 2.0.6-1
- Update to 2.0.6

* Fri Jan 17 2020 Eric D. Helms <ericdhelms@gmail.com> - 2.0.5-2
- Drop posttrans macros

* Thu Jan 09 2020 Aditi Puntambekar <apuntamb@redhat.com> 2.0.5-1
- Update to 2.0.5

* Thu Dec 12 2019 Aditi Puntambekar <apuntamb@redhat.com> 2.0.4-1
- Update to 2.0.4

* Tue Dec 10 2019 Aditi Puntambekar <apuntamb@redhat.com> 2.0.3-1
- Update to 2.0.3

* Tue Nov 26 2019 Aditi Puntambekar <apuntamb@redhat.com> 2.0.2-1
- Update to 2.0.2

* Thu Oct 31 2019 Aditi Puntambekar <apuntamb@redhat.com> 2.0.1-1
- Add rubygem-foreman_azure_rm generated by gem2rpm using the foreman_plugin template

