# template: foreman_plugin
%global gem_name foreman_ansible
%global plugin_name ansible
%global foreman_min_version 3.16.0

Name: rubygem-%{gem_name}
Version: 17.0.0
Release: 1%{?foremandist}%{?dist}
Summary: Ansible integration with Foreman (theforeman.org)
License: GPLv3
URL: https://github.com/theforeman/foreman_ansible
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: foreman >= %{foreman_min_version}
BuildRequires: foreman-assets >= %{foreman_min_version}
BuildRequires: foreman-plugin >= %{foreman_min_version}
Requires: ruby
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildRequires: (rubygem(acts_as_list) >= 1.2 with rubygem(acts_as_list) < 2)
BuildRequires: rubygem(deface) < 2.0
BuildRequires: (rubygem(foreman_remote_execution) >= 14.0 with rubygem(foreman_remote_execution) < 17)
BuildRequires: (rubygem(foreman-tasks) >= 10.0 with rubygem(foreman-tasks) < 12)
BuildArch: noarch
Provides: foreman-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

# start package.json devDependencies BuildRequires
BuildRequires: (npm(@babel/core) >= 7.7.0 with npm(@babel/core) < 8.0.0)
BuildRequires: npm(@theforeman/builder) >= 12.0.1
# end package.json devDependencies BuildRequires

# start package.json dependencies BuildRequires
BuildRequires: (npm(react-json-tree) >= 0.11.0 with npm(react-json-tree) < 1.0.0)
# end package.json dependencies BuildRequires

%description
Ansible integration with Foreman.


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

%posttrans
%{foreman_plugin_log}

%changelog
* Thu Jul 17 2025 Foreman Packaging Automation <packaging@theforeman.org> - 17.0.0-1
- Update to 17.0.0

* Tue Jul 15 2025 Evgeni Golov - 16.0.1-2
- Rebuild for removal of theforeman/vendor

* Wed Jun 04 2025 Foreman Packaging Automation <packaging@theforeman.org> - 16.0.1-1
- Update to 16.0.1

* Thu Mar 27 2025 Foreman Packaging Automation <packaging@theforeman.org> - 16.0.0-1
- Update to 16.0.0

* Wed Mar 05 2025 Foreman Packaging Automation <packaging@theforeman.org> - 15.0.6-1
- Update to 15.0.6

* Thu Jan 30 2025 Foreman Packaging Automation <packaging@theforeman.org> - 15.0.5-1
- Update to 15.0.5

* Sun Jan 26 2025 Foreman Packaging Automation <packaging@theforeman.org> - 15.0.4-1
- Update to 15.0.4

* Tue Dec 03 2024 Foreman Packaging Automation <packaging@theforeman.org> - 15.0.3-1
- Update to 15.0.3

* Wed Nov 20 2024 Foreman Packaging Automation <packaging@theforeman.org> - 15.0.2-1
- Update to 15.0.2

* Wed Sep 25 2024 Foreman Packaging Automation <packaging@theforeman.org> - 15.0.1-1
- Update to 15.0.1

* Wed Sep 11 2024 Foreman Packaging Automation <packaging@theforeman.org> - 15.0.0-1
- Update to 15.0.0

* Wed Sep 11 2024 Foreman Packaging Automation <packaging@theforeman.org> - 14.2.2-1
- Update to 14.2.2

* Sun Aug 11 2024 Foreman Packaging Automation <packaging@theforeman.org> - 14.2.1-1
- Update to 14.2.1

* Thu Aug 01 2024 Leos Stejskal <lstejska@redhat.com> - 14.2.0-1
- Update to 14.2.0

* Wed Jul 31 2024 Leos Stejskal <lstejska@redhat.com> - 14.1.1-1
- Update to 14.1.1

* Fri Jun 21 2024 Foreman Packaging Automation <packaging@theforeman.org> - 14.1.0-1
- Update to 14.1.0

* Tue May 07 2024 Evgeni Golov - 14.0.0-2
- Rebuild for Webpack asset compression

* Tue Mar 26 2024 Foreman Packaging Automation <packaging@theforeman.org> - 14.0.0-1
- Update to 14.0.0

* Wed Mar 13 2024 Foreman Packaging Automation <packaging@theforeman.org> - 13.0.4-1
- Update to 13.0.4

* Fri Jan 26 2024 Evgeni Golov - 13.0.3-2
- Rebuild for Webpack 5

* Fri Jan 19 2024 nofaralfasi <nalfassi@redhat.com> - 13.0.3-1
- Update to 13.0.3

* Sun Dec 03 2023 nofaralfasi <nalfassi@redhat.com> 13.0.2-1
- Update to 13.0.2

* Thu Nov 30 2023 nofaralfasi <nalfassi@redhat.com> 13.0.1-1
- Update to 13.0.1

* Tue Nov 21 2023 nofaralfasi <nalfassi@redhat.com> 13.0.0-1
- Update to 13.0.0

* Wed Sep 06 2023 Foreman Packaging Automation <packaging@theforeman.org> 12.0.7-1
- Update to 12.0.7

* Sun Aug 06 2023 nofaralfasi <nalfassi@redhat.com> 12.0.6-1
- Update to 12.0.6

* Wed Jul 26 2023 nofaralfasi <nalfassi@redhat.com> 12.0.5-1
- Update to 12.0.5

* Thu Jun 22 2023 Foreman Packaging Automation <packaging@theforeman.org> 12.0.4-1
- Update to 12.0.4

* Mon May 22 2023 nofaralfasi <nalfassi@redhat.com> 12.0.3-1
- Update to 12.0.3

* Mon May 22 2023 Foreman Packaging Automation <packaging@theforeman.org> 12.0.2-1
- Update to 12.0.2

* Fri May 19 2023 Foreman Packaging Automation <packaging@theforeman.org> 12.0.1-1
- Update to 12.0.1

* Tue May 16 2023 nofaralfasi <nalfassi@redhat.com> 12.0.0-1
- Update to 12.0.0

* Wed May 10 2023 nofaralfasi <nalfassi@redhat.com> 11.2.1-1
- Update to 11.2.1

* Thu May 04 2023 Evgeni Golov 11.2.0-2
- Regenerate RPM spec from latest template

* Sun Apr 30 2023 Foreman Packaging Automation <packaging@theforeman.org> 11.2.0-1
- Update to 11.2.0

* Tue Mar 21 2023 nofaralfasi <nalfassi@redhat.com> 11.1.2-1
- Update to 11.1.2

* Tue Mar 07 2023 Leos Stejskal <lstejska@redhat.com> 11.1.1-1
- Update to 11.1.1

* Tue Feb 14 2023 nofaralfasi <nalfassi@redhat.com> 11.1.0-1
- Update to 11.1.0

* Mon Jan 09 2023 Foreman Packaging Automation <packaging@theforeman.org> 11.0.0-1
- Update to 11.0.0

* Wed Jan 04 2023 Foreman Packaging Automation <packaging@theforeman.org> 10.2.0-1
- Update to 10.2.0

* Wed Nov 09 2022 nofaralfasi <nalfassi@redhat.com> 10.1.0-1
- Update to 10.1.0

* Mon Oct 03 2022 Leos Stejskal <lstejska@redhat.com> 10.0.1-1
- Update to 10.0.1

* Mon Sep 05 2022 Leos Stejskal <lstejska@redhat.com> 9.0.1-1
- Update to 9.0.1

* Mon Aug 29 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 9.0.0-1
- Update to 9.0.0

* Wed Aug 24 2022 Evgeni Golov - 8.0.1-2
- Refs #35409 - Include sprockets assets

* Sun Jul 24 2022 Foreman Packaging Automation <packaging@theforeman.org> 8.0.1-1
- Update to 8.0.1

* Mon May 16 2022 Leos Stejskal <lstejska@redhat.com> 8.0.0-1
- Update to 8.0.0

* Mon May 09 2022 Evgeni Golov - 7.1.0-3
- log plugin installation in posttrans

* Fri Apr 22 2022 Eric D. Helms <ericdhelms@gmail.com> - 7.1.0-2
- Stop generaing apipie cache

* Mon Mar 14 2022 Ondřej Ezr <oezr@redhat.com> 7.1.0-1
- Update to 7.1.0

* Thu Feb 24 2022 Leos Stejskal <lstejska@redhat.com> 7.0.3-1
- Update to 7.0.3

* Thu Jan 20 2022 Ondřej Ezr <oezr@redhat.com> 7.0.2-1
- Update to 7.0.2

* Tue Dec 07 2021 Ondřej Ezr <oezr@redhat.com> 7.0.1-1
- Update to 7.0.1

* Fri Jun 25 2021 Adam Ruzicka <aruzicka@redhat.com> 6.4.1-1
- Update to 6.4.1

* Mon May 17 2021 Ondrej Prazak <oprazak@redhat.com> 6.3.0-1
- Update to 6.3.0

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 6.2.0-2
- Rebuild plugins for Ruby 2.7

* Wed Feb 24 2021 Ondrej Prazak <oprazak@redhat.com> 6.2.0-1
- Update to 6.2.0

* Fri Jan 22 2021 Adam Ruzicka <aruzicka@redhat.com> 6.1.1-1
- Update to 6.1.1

* Mon Jan 18 2021 Adam Ruzicka <aruzicka@redhat.com> 6.1.0-1
- Update to 6.1.0

* Thu Dec 03 2020 Ondrej Prazak <oprazak@redhat.com> 6.0.1-1
- Update to 6.0.1

* Tue Sep 01 2020 Adam Ruzicka <aruzicka@redhat.com> 6.0.0-1
- Update to 6.0.0

* Fri Jun 05 2020 Adam Ruzicka <aruzicka@redhat.com> 5.1.1-1
- Update to 5.1.1

* Tue Jun 02 2020 Adam Ruzicka <aruzicka@redhat.com> 5.1.0-1
- Update to 5.1.0

* Mon Mar 09 2020 Marek Hulan <mhulan@redhat.com> 5.0.1-1
- Update to 5.0.1

* Tue Jan 28 2020 Tomer Brisker <tbrisker@gmail.com> - 5.0.0-3
- rebuild for webpack change

* Wed Jan 15 2020 Eric D. Helms <ericdhelms@gmail.com> - 5.0.0-2
- Drop migrate, seed and restart posttans

* Wed Jan 15 2020 Marek Hulan <mhulan@redhat.com> 5.0.0-1
- Update to 5.0.0

* Fri Oct 25 2019 Ondrej Prazak <oprazak@redhat.com> - 4.0.0-1
- Update to 4.0.0

* Tue Oct 22 2019 Eric D. Helms <ericdhelms@gmail.com> - 3.0.7-2
- Rebuild for SCL nodejs

* Mon Sep 09 2019 Marek Hulan <mhulan@redhat.com> 3.0.7-1
- Update to 3.0.7

* Thu Aug 08 2019 Marek Hulan <mhulan@redhat.com> 3.0.6-1
- Update to 3.0.6

* Thu Jul 18 2019 Ondrej Prazak <oprazak@redhat.com> 3.0.5-1
- Update to 3.0.5

* Wed Jul 17 2019 Evgeni Golov - 3.0.3-2
- Rebuild to use @theforeman/vendor

* Thu Jun 27 2019 Marek Hulan <mhulan@redhat.com> 3.0.3-1
- Update to 3.0.3

* Thu May 16 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 3.0.2-2
- Rebuild rubygem-foreman_ansible to drop the generated webpack vendor.js
  dependency

* Fri May 10 2019 Marek Hulan <mhulan@redhat.com> 3.0.2-1
- Update to 3.0.2

* Thu May 09 2019 Marek Hulan - 2.3.3-5
- Rebuild Ansible for webpack

* Mon May 06 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.3.3-4
- Rebuild rubygem-foreman_ansible for webpack

* Tue Apr 30 2019 Evgeni Golov - 2.3.3-3
- Rebuild Ansible for webpack

* Fri Apr 12 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.3.3-2
- Rebuild rubygem-foreman_ansible for webpack

* Thu Apr 11 2019 Marek Hulan <mhulan@redhat.com> 2.3.3-1
- Update to 2.3.3

* Thu Apr 04 2019 Marek Hulan - 2.3.2-4
- Rebuild Ansible for webpack

* Thu Mar 28 2019 Evgeni Golov - 2.3.2-3
- Rebuild Ansible for webpack

* Tue Mar 26 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.3.2-2
- Rebuild rubygem-foreman_ansible for webpack

* Thu Mar 07 2019 Marek Hulan <mhulan@redhat.com> 2.3.2-1
- Update to 2.3.2

* Mon Feb 25 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.3.1-4
- Rebuild rubygem-foreman_ansible for webpack

* Tue Feb 19 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.3.1-3
- Rebuild rubygem-foreman_ansible for webpack

* Thu Feb 14 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.3.1-2
- Rebuild rubygem-foreman_ansible for webpack

* Fri Jan 25 2019 Marek Hulan <mhulan@redhat.com> 2.3.1-1
- Update to 2.3.1

* Thu Jan 24 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.3.0-5
- Rebuild rubygem-foreman_ansible for webpack

* Mon Jan 21 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.3.0-4
- Rebuild for webpack

* Wed Jan 09 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.3.0-3
- Rebuild for webpack

* Tue Jan 08 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.3.0-2
- Rebuild for webpack

* Thu Nov 22 2018 Marek Hulan <mhulan@redhat.com> 2.3.0-1
- Update to 2.3.0

* Mon Nov 19 2018 Marek Hulan <mhulan@redhat.com> 2.2.11-1
- Update to 2.2.11

* Wed Oct 31 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.2.9-3
- Revbump to correct source map handling

* Wed Oct 31 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.2.9-2
- Use the license macro
- Remove rpmlint warnings

* Tue Sep 25 2018 Marek Hulan <mhulan@redhat.com> 2.2.9-1
- Update to 2.2.9

* Thu Sep 13 2018 Marek Hulan <mhulan@redhat.com> 2.2.7-1
- Update to 2.2.7

* Mon Sep 10 2018 Eric D. Helms <ericdhelms@gmail.com> - 2.2.6-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Wed Aug 15 2018 Sebastian Gräßl <mail@bastilian.me> 2.2.6-1
- Update to 2.2.6

* Wed Jul 25 2018 Marek Hulan <mhulan@redhat.com> 2.2.5-1
- Update to 2.2.5

* Fri Jul 13 2018 Marek Hulan <mhulan@redhat.com> 2.2.3-1
- Update to 2.2.3

* Thu Jul 12 2018 Marek Hulan <mhulan@redhat.com> 2.2.2-1
- Update to 2.2.2

* Wed Jul 04 2018 Marek Hulan <mhulan@redhat.com> 2.2.1-1
- Update to 2.2.1

* Mon Jul 02 2018 Daniel Lobato Garcia <me@daniellobato.me> 2.2.0-1
- Update to 2.2.0

* Wed Jun 27 2018 Ondrej Prazak <oprazak@redhat.com> 2.1.2-2
- Plugin rebuild

* Fri Apr 06 2018 Daniel Lobato Garcia <me@daniellobato.me> 2.0.4-1
- Update to 2.0.4

* Fri Apr 06 2018 Daniel Lobato Garcia <me@daniellobato.me> 2.0.2-1
- Update to 2.0.2

* Fri Feb 02 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 2.0.1-1
- Bump foreman_ansible to 2.0.1 (me@daniellobato.me)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Fri Apr 07 2017 Dominic Cleal <dominic@cleal.org> 1.4.5-1
- Update foreman_ansible to 1.4.5 (me@daniellobato.me)

* Tue Feb 14 2017 Dominic Cleal <dominic@cleal.org> 1.4.4-1
- Update foreman_ansible to 1.4.4 (me@daniellobato.me)

* Mon Jan 30 2017 Dominic Cleal <dominic@cleal.org> 1.4.2-1
- Update foreman-ansible to 1.4.2 (me@daniellobato.me)

* Fri Jan 20 2017 Dominic Cleal <dominic@cleal.org> 1.4.1-1
- Release foreman_ansible 1.4.1 (me@daniellobato.me)

* Wed Dec 21 2016 Dominic Cleal <dominic@cleal.org> 1.3.1-1
- Update foreman_ansible to 1.3.1 (me@daniellobato.me)

* Mon Dec 05 2016 Dominic Cleal <dominic@cleal.org> 1.3.0-1
- Update foreman-ansible to 1.3.0 (me@daniellobato.me)

* Mon Oct 03 2016 Dominic Cleal <dominic@cleal.org> 1.2.1-1
- Update foreman-ansible to 1.2.1 (me@daniellobato.me)

* Fri Jul 08 2016 Dominic Cleal <dominic@cleal.org> 1.0-1
- plugins:foreman_ansible - 1.0.0 (elobatocs@gmail.com)

* Thu Feb 11 2016 Dominic Cleal <dcleal@redhat.com> 0.3-1
- plugins:foreman_ansible - Release 0.3 (elobatocs@gmail.com)

* Mon Feb 08 2016 Dominic Cleal <dcleal@redhat.com> 0.2.2-2
- Obsolete ruby193 variant from 1.8/1.9 (dcleal@redhat.com)

* Mon Feb 08 2016 Dominic Cleal <dcleal@redhat.com> 0.2.2-1
- Release 0.2.2 (elobatocs@gmail.com)

* Sat Jan 02 2016 Daniel Lobato <elobatocs@gmail.com> 0.2.1-1
- Initial package
