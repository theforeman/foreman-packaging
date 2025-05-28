# template: foreman_plugin
%global gem_name foreman_salt
%global plugin_name salt
%global foreman_min_version 3.13

Name: rubygem-%{gem_name}
Version: 17.0.2
Release: 1%{?foremandist}%{?dist}
Summary: Foreman Plug-in for Salt
License: GPLv3
URL: https://github.com/theforeman/foreman_salt
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: foreman >= %{foreman_min_version}
BuildRequires: foreman-assets >= %{foreman_min_version}
BuildRequires: foreman-plugin >= %{foreman_min_version}
Requires: ruby
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildRequires: rubygem(deface) < 2.0
BuildRequires: (rubygem(foreman_remote_execution) >= 14.0 with rubygem(foreman_remote_execution) < 17)
BuildRequires: (rubygem(foreman-tasks) >= 10.0 with rubygem(foreman-tasks) < 12)
BuildArch: noarch
Provides: foreman-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

%description
Foreman Plug-in for Salt.


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
%{gem_instdir}/test

%posttrans
%{foreman_plugin_log}

%changelog
* Thu Mar 27 2025 Foreman Packaging Automation <packaging@theforeman.org> - 17.0.2-1
- Update to 17.0.2

* Thu Jan 30 2025 Foreman Packaging Automation <packaging@theforeman.org> - 17.0.1-1
- Update to 17.0.1

* Thu Sep 12 2024 Foreman Packaging Automation <packaging@theforeman.org> - 17.0.0-1
- Update to 17.0.0

* Thu Sep 05 2024 Evgeni Golov - 16.0.3-2
- Rebuild against Foreman nightly

* Fri Jun 21 2024 Foreman Packaging Automation <packaging@theforeman.org> - 16.0.3-1
- Update to 16.0.3

* Sun Apr 14 2024 Foreman Packaging Automation <packaging@theforeman.org> - 16.0.2-1
- Update to 16.0.2

* Mon Mar 18 2024 Foreman Packaging Automation <packaging@theforeman.org> - 16.0.1-1
- Update to 16.0.1

* Thu Dec 07 2023 Foreman Packaging Automation <packaging@theforeman.org> 16.0.0-1
- Update to 16.0.0

* Tue Nov 28 2023 Bernhard Suttner <suttner@atix.de> 15.2.3-1
- Update to 15.2.3

* Thu Sep 07 2023 Foreman Packaging Automation <packaging@theforeman.org> 15.2.2-1
- Update to 15.2.2

* Thu Aug 03 2023 Nadja Heitmann <nadjah@atix.de> 15.2.1-1
- Update to 15.2.1

* Thu Jun 29 2023 Nadja Heitmann <nadjah@atix.de> 15.1.0-5
- Regenerate RPM spec based on latest template

* Wed Aug 24 2022 Evgeni Golov - 15.1.0-4
- Refs #35409 - Include sprockets assets

* Mon May 09 2022 Evgeni Golov - 15.1.0-3
- log plugin installation in posttrans

* Fri Apr 22 2022 Eric D. Helms <ericdhelms@gmail.com> - 15.1.0-2
- Stop generaing apipie cache

* Fri Apr 08 2022 Bernhard Suttner <suttner@atix.de> 15.1.0-1
- Update to 15.1.0

* Mon Feb 14 2022 Bernhard Suttner <suttner@atix.de> 15.0.0-1
- Update to 15.0.0

* Mon Jan 17 2022 Foreman Packaging Automation <packaging@theforeman.org> 14.1.0-1
- Update to 14.1.0

* Mon Aug 02 2021 Bastian Schmidt <schmidt@atix.de> 14.0.0-1
- Update to 14.0.0
- Implement Salt Autosign via Grains

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 13.2.4-2
- Rebuild plugins for Ruby 2.7

* Tue Jun 09 2020 Bernhard Suttner <suttner@atix.de> 13.2.4-1
- Update to 13.2.4
- Drop migrate, seed and restart posttans

* Thu Jan 23 2020 Bernhard Suttner <suttner@atix.de> 13.2.3-1
- Update to 13.2.3

* Tue Jan 21 2020 Bernhard Suttner <suttner@atix.de> 13.2.2-1
- Update to 13.2.2

* Tue Jan 21 2020 Bernhard Suttner <suttner@atix.de> 13.2.1-1
- Update to 13.2.1

* Tue Nov 19 2019 Bernhard Suttner <suttner@atix.de> 13.2.0-1
- Update to 13.2.0

* Thu Oct 31 2019 Bernhard Suttner <suttner@atix.de> 13.1.0-1
- Update to 13.1.0

* Fri Aug 02 2019 Adam Ruzicka <aruzicka@redhat.com> 12.0.0-1
- Update to 12.0.0

* Mon Jul 22 2019 Bernhard Suttner <suttner@atix.de> 11.0.1-1
- Update to 11.0.1

* Mon May 20 2019 Bernhard Suttner <suttner@atix.de> 11.0.0-1
- Update to 11.0.0

* Mon May 06 2019 Bernhard Suttner <suttner@atix.de> 10.3.1-1
- Update to 10.3.1

* Sun May 05 2019 Bernhard Suttner <suttner@atix.de> 10.3.0-1
- Update to 10.3.0

* Thu Apr 25 2019 Bernhard Suttner <suttner@atix.de> 10.2.0-1
- Update to 10.2.0

* Mon Sep 10 2018 Eric D. Helms <ericdhelms@gmail.com> - 10.1.0-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jul 20 2018 Greg Sutcliffe <greg.sutcliffe@gmail.com> 10.1.0-1
- Update to 10.1.0

* Mon May 28 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 10.0.0-2
- Regenerate spec file based on the current template

* Tue May 08 2018 Michael Moll <kvedulv@kvedulv.de> 10.0.0-1
- update foreman_salt to 10.0.0 (kvedulv@kvedulv.de)

* Wed Dec 13 2017 Daniel Lobato Garcia <me@daniellobato.me> 9.0.0-1
- update foreman_salt to 9.0.0 (kvedulv@kvedulv.de)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Thu Mar 30 2017 Dominic Cleal <dominic@cleal.org> 8.0.2-1
- update foreman_salt to 8.0.2 (kvedulv@kvedulv.de)

* Mon Mar 13 2017 Eric D Helms <ericdhelms@gmail.com> 8.0.1-1
- update foreman_salt to 8.0.1 (kvedulv@kvedulv.de)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Wed Nov 23 2016 Dominic Cleal <dominic@cleal.org> 8.0.0-1
- update foreman_salt to 8.0.0 (kvedulv@kvedulv.de)

* Tue Nov 22 2016 Dominic Cleal <dominic@cleal.org> 7.0.1-1
- update foreman_salt to 7.0.1 (kvedulv@kvedulv.de)

* Mon Aug 22 2016 Dominic Cleal <dominic@cleal.org> 7.0.0-1
- Release foreman_salt 7.0.0 (stephen@redhat.com)

* Thu Jul 28 2016 Dominic Cleal <dominic@cleal.org> 6.0.0-1
- Release foreman_salt 6.0.0 (stephen@redhat.com)

* Tue May 31 2016 Dominic Cleal <dominic@cleal.org> 5.0.1-1
- update foreman_salt to 5.0.1 (kvedulv@kvedulv.de)

* Wed Jan 27 2016 Dominic Cleal <dcleal@redhat.com> 5.0.0-1
- Release foreman_salt 5.0.0 (stbenjam@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Mon Oct 26 2015 Dominic Cleal <dcleal@redhat.com> 4.0.1-1
- Small foreman_salt update (stbenjam@redhat.com)

* Tue Oct 13 2015 Dominic Cleal <dcleal@redhat.com> 4.0.0-1
- Release foreman_salt 4.0.0 (RPM) (stbenjam@redhat.com)

* Thu Aug 27 2015 Dominic Cleal <dcleal@redhat.com> 3.0.2-1
- Release foreman_salt 3.0.2 (stbenjam@redhat.com)

* Thu Aug 27 2015 Dominic Cleal <dcleal@redhat.com> 3.0.1-2
- Converted to tfm SCL (dcleal@redhat.com)

* Thu Aug 13 2015 Stephen Benjamin <stephen@redhat.com> 3.0.1-1
- Update to 3.0.1

* Mon Jul 06 2015 Stephen Benjamin <stephen@redhat.com> 3.0.0-1
- Update to 3.0.0

* Sat May 09 2015 Stephen Benjamin <stephen@redhat.com> 2.1.0-1
- Update to 2.1.0

* Tue Mar 17 2015 Stephen Benjamin <stephen@redhat.com> 2.0.2-1
- Update to 2.0.2

* Tue Mar 03 2015 Stephen Benjamin <stephen@redhat.com> 2.0.1-1
- Update to 2.0.1

* Wed Jan 14 2015 Stephen Benjamin <stephen@redhat.com> 1.1.1-1
- Update to 1.1.1

* Tue Dec 30 2014 Michael Moll <mmoll@mmoll.at> 1.1.0-2
- Add dependency on rubygem-deface

* Wed Nov 19 2014 Stephen Benjamin <stephen@redhat.com> 1.1.0-1
- Update to 1.1.0

* Tue Nov 11 2014 Stephen Benjamin <stephen@redhat.com> 1.0.0-1
- Update to 1.0.0

* Wed Oct 08 2014 Stephen Benjamin <stephen@redhat.com> 0.0.4-1
- Update to 0.0.4

* Tue Oct 07 2014 Michael Moll <mmoll@mmoll.at> 0.0.3-1
- Update to 0.0.3

* Thu Aug 28 2014 Stephen Benjamin <stephen@redhat.com> 0.0.2-1
- Initial version
