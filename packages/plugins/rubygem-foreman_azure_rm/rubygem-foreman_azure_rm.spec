# template: foreman_plugin
%global gem_name foreman_azure_rm
%global plugin_name azure_rm
%global foreman_min_version 3.13

Name: rubygem-%{gem_name}
Version: 3.0.4
Release: 1%{?foremandist}%{?dist}
Summary: Azure Resource Manager as a compute resource for The Foreman
License: GPLv3
URL: https://github.com/theforeman/foreman_azure_rm
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: foreman >= %{foreman_min_version}
BuildRequires: foreman-assets >= %{foreman_min_version}
BuildRequires: foreman-plugin >= %{foreman_min_version}
Requires: ruby
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildRequires: (rubygem(azure_mgmt_resources) >= 0.18.1 with rubygem(azure_mgmt_resources) < 0.19)
BuildRequires: (rubygem(azure_mgmt_network) >= 0.26.1 with rubygem(azure_mgmt_network) < 0.27)
BuildRequires: (rubygem(azure_mgmt_storage) >= 0.23.0 with rubygem(azure_mgmt_storage) < 0.24)
BuildRequires: (rubygem(azure_mgmt_compute) >= 0.22.0 with rubygem(azure_mgmt_compute) < 0.23)
BuildRequires: (rubygem(azure_mgmt_subscriptions) >= 0.18.5 with rubygem(azure_mgmt_subscriptions) < 0.19)
BuildArch: noarch
Provides: foreman-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

%description
This gem provides Azure Resource Manager as a compute resource for The
Foreman.


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
%exclude %{gem_cache}
%{gem_spec}
%{foreman_bundlerd_plugin}
%{foreman_assets_plugin}
%{foreman_assets_foreman}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile

%posttrans
%{foreman_plugin_log}

%changelog
* Wed May 28 2025 Chris Roberts <chrobert@redhat.com> - 3.0.4-1
- Update to 3.0.4

* Thu Feb 20 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.0.3-1
- Update to 3.0.3

* Wed Dec 11 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.0.2-1
- Update to 3.0.2

* Fri Sep 20 2024 Chris Roberts <chrobert@redhat.com> - 3.0.1-1
- Update to 3.0.1

* Fri Sep 13 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.0.0-1
- Update to 3.0.0

* Sun Apr 07 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.3.0-1
- Update to 2.3.0

* Sun Mar 10 2024 nofaralfasi <nalfassi@redhat.com> 2.2.11-2
- Regenerate spec file based on the latest template

* Mon Jan 08 2024 Leos Stejskal <lstejska@redhat.com> - 2.2.11-1
- Update to 2.2.11

* Tue Aug 08 2023 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.2.10-2
- Precompile assets

* Mon Jun 05 2023 Chris Roberts <chrobert@redhat.com> 2.2.10-1
- Update to 2.2.10

* Wed Jan 04 2023 Chris Roberts <chrobert@redhat.com> - 2.2.9-1
- Release rubygem-foreman_azure_rm 2.2.9

* Wed Nov 30 2022 Chris Roberts <chrobert@redhat.com> - 2.2.8-1
- Release rubygem-foreman_azure_rm 2.2.8

* Mon Sep 12 2022 Odilon Sousa <osousa@redhat.com> - 2.2.7-1
- Release rubygem-foreman_azure_rm 2.2.7

* Mon May 09 2022 Evgeni Golov - 2.2.6-3
- log plugin installation in posttrans

* Fri Apr 22 2022 Eric D. Helms <ericdhelms@gmail.com> - 2.2.6-2
- Stop generaing apipie cache

* Thu Nov 11 2021 Chris Roberts <chrobert@redhat.com> 2.2.6-1
- Update to 2.2.6

* Wed Jun 09 2021 Amit Upadhye <upadhyeammit@gmail.com> 2.2.5-1
- Update to 2.2.5

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

