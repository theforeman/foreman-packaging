# This package contains macros that provide functionality relating to
# Software Collections. These macros are not used in default
# Fedora builds, and should not be blindly copied or enabled.
# Specifically, the "scl" macro must not be defined in official Fedora
# builds. For more information, see:
# http://docs.fedoraproject.org/en-US/Fedora_Contributor_Documentation
# /1/html/Software_Collections_Guide/index.html

%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_bootdisk

Summary:    Create boot disks to provision hosts with Foreman
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    10.0.2
Release:    1%{?foremandist}%{?dist}
Group:      Applications/System
License:    GPLv3
URL:        http://github.com/theforeman/foreman_bootdisk
Source0:    http://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires:   foreman >= 1.15.0
Requires:   ipxe-bootimgs
Requires:   /usr/bin/isohybrid
Requires:   /usr/bin/genisoimage

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}rubygems

BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: foreman-plugin >= 1.13.0
BuildRequires: foreman-assets
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems

BuildArch: noarch

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-bootdisk
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Plugin for Foreman that creates iPXE-based boot disks to provision hosts
without the need for PXE infrastructure.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%foreman_bundlerd_file
%foreman_precompile_plugin -a -s

%files
%dir %{gem_instdir}
%{gem_instdir}/app
%{gem_instdir}/config
%{gem_instdir}/db
%{gem_instdir}/public
%{gem_libdir}
%{gem_instdir}/locale
%{gem_spec}
%{foreman_bundlerd_plugin}
%{foreman_assets_plugin}
%license %{gem_instdir}/LICENSE
%foreman_apipie_cache_foreman

%exclude %{gem_cache}
%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/test

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGES.md
%doc %{gem_instdir}/README.md

%posttrans
%foreman_db_migrate
%foreman_db_seed
%foreman_apipie_cache
%foreman_restart
exit 0

%changelog
* Thu Jan 11 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 10.0.2-1
- Update foreman_bootdisk to 10.0.2 (mail@timogoebel.name)

* Mon Dec 11 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 10.0.1-1
- Update foreman_bootdisk to 10.0.1 (mail@timogoebel.name)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Wed Mar 22 2017 Dominic Cleal <dominic@cleal.org> 9.0.0-1
- Update foreman_bootdisk to 9.0.0 (dominic@cleal.org)

* Wed Dec 14 2016 Dominic Cleal <dominic@cleal.org> 8.1.0-1
- Update foreman_bootdisk to 8.1.0 (dominic@cleal.org)

* Mon Sep 12 2016 Dominic Cleal <dominic@cleal.org> 8.0.2-1
- Update foreman_bootdisk to 8.0.2 (dominic@cleal.org)

* Tue Jun 07 2016 Dominic Cleal <dominic@cleal.org> 8.0.1-1
- Update foreman_bootdisk to 8.0.1 (dominic@cleal.org)

* Mon Apr 18 2016 Dominic Cleal <dominic@cleal.org> 8.0.0-2
- Include precompiled assets in rpm (timo.goebel@dm.de)

* Tue Apr 12 2016 Dominic Cleal <dominic@cleal.org> 8.0.0-1
- Update foreman_bootdisk to 8.0.0 (dominic@cleal.org)

* Wed Apr 06 2016 Dominic Cleal <dominic@cleal.org> 7.0.0-1
- Update foreman_bootdisk to 7.0.0 (dominic@cleal.org)

* Thu Jan 21 2016 Dominic Cleal <dcleal@redhat.com> 6.1.0-1
- Update foreman_bootdisk to 6.1.0 (dcleal@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Thu Aug 27 2015 Dominic Cleal <dcleal@redhat.com> 6.0.0-2
- Converted to tfm SCL (dcleal@redhat.com)
- Better branched builds with Foreman version macro (dcleal@redhat.com)

* Mon Jun 15 2015 Dominic Cleal <dcleal@redhat.com> 6.0.0-1
- Update foreman_bootdisk to 6.0.0 (dcleal@redhat.com)

* Mon Feb 23 2015 Dominic Cleal <dcleal@redhat.com> 5.0.0-1
- Update foreman_bootdisk to 5.0.0 (dcleal@redhat.com)
- Refs #8921 - prebuild localized apipie cache in rubygem-foreman_bootdisk
  (martin.bacovsky@gmail.com)

* Tue Nov 18 2014 Dominic Cleal <dcleal@redhat.com> 4.0.2-1
- Update to foreman_bootdisk 4.0.2 (dcleal@redhat.com)

* Mon Nov 17 2014 Dominic Cleal <dcleal@redhat.com> 4.0.1-1
- Update to foreman_bootdisk 4.0.1 (dcleal@redhat.com)

* Thu Oct 02 2014 Dominic Cleal <dcleal@redhat.com> 4.0.0-1
- Update to foreman_bootdisk 4.0.0 (dcleal@redhat.com)

* Thu Oct 02 2014 Dominic Cleal <dcleal@redhat.com> 3.2.0-1
- Update to foreman_bootdisk 3.2.0 (dcleal@redhat.com)

* Wed Sep 03 2014 Dominic Cleal <dcleal@redhat.com> 3.1.2-1
- Update to foreman_bootdisk 3.1.2 (dcleal@redhat.com)

* Wed Aug 20 2014 Dominic Cleal <dcleal@redhat.com> 3.1.1-1
- Update to foreman_bootdisk 3.1.1 (dcleal@redhat.com)

* Fri Aug 08 2014 Dominic Cleal <dcleal@redhat.com> 3.1.0-2
- Recache API documentation on install (dcleal@redhat.com)

* Fri Aug 08 2014 Dominic Cleal <dcleal@redhat.com> 3.1.0-1
- Update to foreman_bootdisk 3.1.0 (dcleal@redhat.com)

* Tue Aug 05 2014 Dominic Cleal <dcleal@redhat.com> 3.0.0-1
- Update to foreman_bootdisk 3.0.0 (dcleal@redhat.com)

* Thu May 29 2014 Dominic Cleal <dcleal@redhat.com> 2.0.8-1
- Update to foreman_bootdisk 2.0.8 (dcleal@redhat.com)

* Fri May 23 2014 Dominic Cleal <dcleal@redhat.com> 2.0.7-1
- Update to foreman_bootdisk 2.0.7 (dcleal@redhat.com)

* Fri May 16 2014 Dominic Cleal <dcleal@redhat.com> 2.0.6-1
- Update to foreman_bootdisk 2.0.6 (dcleal@redhat.com)

* Tue May 06 2014 Dominic Cleal <dcleal@redhat.com> 2.0.5-1
- Update to foreman_bootdisk 2.0.5 (dcleal@redhat.com)

* Wed Apr 09 2014 Dominic Cleal <dcleal@redhat.com> 2.0.4-1
- Update to foreman_bootdisk 2.0.4 (dcleal@redhat.com)

* Thu Mar 27 2014 Dominic Cleal <dcleal@redhat.com> 2.0.3-1
- Update to foreman_bootdisk 2.0.3 (dcleal@redhat.com)

* Thu Feb 13 2014 Dominic Cleal <dcleal@redhat.com> 2.0.2-1
- Update to foreman_bootdisk 2.0.2 (dcleal@redhat.com)

* Thu Feb 13 2014 Dominic Cleal <dcleal@redhat.com> 2.0.1-1
- Update to foreman_bootdisk 2.0.1 (dcleal@redhat.com)

* Wed Jan 22 2014 Dominic Cleal <dcleal@redhat.com> 2.0.0-1
- Update to foreman_bootdisk 2.0.0 (dcleal@redhat.com)

* Fri Nov 01 2013 Dominic Cleal <dcleal@redhat.com> 1.2.3-2
- Update to foreman_bootdisk 1.2.3 (dcleal@redhat.com)

* Tue Oct 15 2013 Dominic Cleal <dcleal@redhat.com> 1.2.2-2
- Add isohybrid and mkisofs dependencies (dcleal@redhat.com)

* Mon Oct 07 2013 Dominic Cleal <dcleal@redhat.com> 1.2.2-1
- Update to foreman_bootdisk 1.2.2 (dcleal@redhat.com)

* Tue Sep 24 2013 Dominic Cleal <dcleal@redhat.com> 1.2.1-1
- Update to foreman_bootdisk 1.2.1 (dcleal@redhat.com)

* Tue Sep 17 2013 Dominic Cleal <dcleal@redhat.com> 1.2.0-1
- new package built with tito
