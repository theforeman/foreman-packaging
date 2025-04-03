# template: foreman_plugin
%global gem_name foreman_bootdisk
%global plugin_name bootdisk
%global foreman_min_version 3.15

Name: rubygem-%{gem_name}
Version: 23.0.0
Release: 1%{?foremandist}%{?dist}
Summary: Create boot disks to provision hosts with Foreman
License: GPLv3
URL: https://github.com/theforeman/foreman_bootdisk
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# used in app/services/foreman_bootdisk/iso_generator.rb
Requires:   dosfstools
Requires:   grub2-efi-x64
Requires:   ipxe-bootimgs
Requires:   /usr/bin/isohybrid
Requires:   /usr/bin/genisoimage

# start specfile generated dependencies
Requires: foreman >= %{foreman_min_version}
BuildRequires: foreman-assets >= %{foreman_min_version}
BuildRequires: foreman-plugin >= %{foreman_min_version}
Requires: ruby >= 2.7
Requires: ruby < 4
BuildRequires: ruby >= 2.7
BuildRequires: ruby < 4
BuildRequires: rubygems-devel
BuildArch: noarch
Provides: foreman-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

# start package.json devDependencies BuildRequires
BuildRequires: (npm(@babel/core) >= 7.7.0 with npm(@babel/core) < 8.0.0)
BuildRequires: npm(@theforeman/builder) >= 8.15.0
BuildRequires: (npm(jed) >= 1.1.1 with npm(jed) < 2.0.0)
# end package.json devDependencies BuildRequires

# start package.json dependencies BuildRequires
# end package.json dependencies BuildRequires

%description
Plugin for Foreman that creates iPXE-based boot disks to provision hosts
without the need for PXE infrastructure.


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
%doc %{gem_instdir}/CHANGES.md
%doc %{gem_instdir}/README.md

%posttrans
%{foreman_plugin_log}

%changelog
* Thu Apr 03 2025 Foreman Packaging Automation <packaging@theforeman.org> - 23.0.0-1
- Update to 23.0.0

* Thu Feb 20 2025 Foreman Packaging Automation <packaging@theforeman.org> - 22.0.3-1
- Update to 22.0.3

* Sun Oct 13 2024 Foreman Packaging Automation <packaging@theforeman.org> - 22.0.2-1
- Update to 22.0.2

* Wed Oct 02 2024 Foreman Packaging Automation <packaging@theforeman.org> - 22.0.1-1
- Update to 22.0.1

* Thu Sep 12 2024 Foreman Packaging Automation <packaging@theforeman.org> - 22.0.0-1
- Update to 22.0.0

* Tue May 07 2024 Evgeni Golov - 21.2.3-2
- Rebuild for Webpack asset compression

* Tue Apr 02 2024 Foreman Packaging Automation <packaging@theforeman.org> - 21.2.3-1
- Update to 21.2.3

* Sun Mar 10 2024 Foreman Packaging Automation <packaging@theforeman.org> - 21.2.2-1
- Update to 21.2.2

* Wed Jan 31 2024 Evgeni Golov - 21.2.1-2
- Rebuild for Webpack 5

* Tue Dec 05 2023 Evgeni Golov 21.2.1-1
- Update to 21.2.1

* Tue Aug 29 2023 Leos Stejskal <lstejska@redhat.com> 21.1.0-1
- Update to 21.1.0

* Thu Jun 22 2023 Leos Stejskal <lstejska@redhat.com> 21.0.4-3
- Regenerate RPM spec from latest template

* Thu Mar 23 2023 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 21.0.4-2
- Depend on grub2-efi-x64

* Tue Feb 21 2023 Foreman Packaging Automation <packaging@theforeman.org> 21.0.4-1
- Update to 21.0.4

* Wed Jan 04 2023 Foreman Packaging Automation <packaging@theforeman.org> 21.0.3-1
- Update to 21.0.3

* Thu Nov 03 2022 Leos Stejskal <lstejska@redhat.com> 21.0.2-1
- Update to 21.0.2

* Mon Sep 26 2022 Leos Stejskal <lstejska@redhat.com> 21.0.0-1
- Update to 21.0.0

* Wed Aug 24 2022 Evgeni Golov - 19.0.5-3
- Refs #35409 - Include sprockets assets

* Mon May 09 2022 Evgeni Golov - 19.0.5-2
- log plugin installation in posttrans

* Thu Apr 28 2022 Ron Lavi <1ronlavi@gmail.com> 19.0.5-1
- Update to 19.0.5

* Fri Apr 22 2022 Eric D. Helms <ericdhelms@gmail.com> - 19.0.4-2
- Stop generaing apipie cache

* Fri Mar 11 2022 Foreman Packaging Automation <packaging@theforeman.org> 19.0.4-1
- Update to 19.0.4

* Wed Jan 19 2022 Lukas Zapletal <lzap+rpm@redhat.com> 19.0.3-1
- Update to 19.0.3

* Fri Jan 14 2022 Lukas Zapletal <lzap+rpm@redhat.com> 19.0.2-1
- Update to 19.0.2

* Wed Jan 12 2022 Lukas Zapletal <lzap+rpm@redhat.com> 19.0.1-1
- Update to 19.0.1

* Thu Dec 09 2021 Evgeni Golov 19.0.0-1
- Update to 19.0.0-1

* Fri Sep 24 2021 Lukas Zapletal <lzap+rpm@redhat.com> 18.0.0-1
- Update to 18.0.0

* Tue Apr 27 2021 Lukas Zapletal <lzap+rpm@redhat.com> 17.1.0-1
- Update to 17.1.0

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 17.0.2-3
- Rebuild plugins for Ruby 2.7

* Wed Jul 15 2020 Adam Ruzicka <aruzicka@redhat.com> 17.0.2-2
- Add missing dependency on dosfstools

* Mon Jun 15 2020 Lukas Zapletal <lzap+rpm@redhat.com> 17.0.2-1
- Update to 17.0.2

* Thu Mar 12 2020 Lukas Zapletal <lzap+rpm@redhat.com> 16.1.0-1
- Update to 16.1.0

* Tue Jan 07 2020 Eric D. Helms <ericdhelms@gmail.com> - 16.0.0-2
- Drop migrate, seed and restart posttans

* Tue Nov 05 2019 Marek Hulan <mhulan@redhat.com> 16.0.0-1
- Update to 16.0.0

* Mon Aug 12 2019 Lukas Zapletal <lzap+rpm@redhat.com> 15.1.0-1
- Update to 15.1.0

* Mon May 13 2019 Lukas Zapletal <lzap+rpm@redhat.com> 15.0.0-1
- Update to 15.0.0

* Tue Nov 06 2018 Lukas Zapletal <lzap+rpm@redhat.com> 14.0.0-1
- Update to 14.0.0

* Thu Oct 04 2018 Lukas Zapletal <lzap+rpm@redhat.com> 13.0.0-1
- Update to 13.0.0

* Fri Sep 07 2018 Eric D. Helms <ericdhelms@gmail.com> - 12.0.0-3
- Rebuild for Rails 5.2 and Ruby 2.5

* Wed May 30 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 12.0.0-2
- Regenerate spec file based on the current template

* Tue May 29 2018 Lukas Zapletal <lzap+git@redhat.com> 12.0.0-1
- Update foreman_bootdisk to 12.0.0

* Tue Jan 16 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 11.0.0-1
- Update foreman_bootdisk to 11.0.0 (mail@timogoebel.name)

* Mon Dec 11 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 10.0.1-1
- Update foreman_bootdisk to 10.0.1 (mail@timogoebel.name)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
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
