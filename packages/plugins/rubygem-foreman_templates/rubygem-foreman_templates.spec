# template: foreman_plugin
%global gem_name foreman_templates
%global plugin_name templates
%global foreman_min_version 3.7

Name: rubygem-%{gem_name}
Version: 9.5.1
Release: 2%{?foremandist}%{?dist}
Summary: Template-syncing engine for Foreman
License: GPLv3
URL: https://github.com/theforeman/foreman_templates
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# Duplicates the autogenerated one so we can ensure git-core is pulled in
Requires: rubygem(git) >= 1.18.0

# start specfile generated dependencies
Requires: foreman >= %{foreman_min_version}
BuildRequires: foreman-assets >= %{foreman_min_version}
BuildRequires: foreman-plugin >= %{foreman_min_version}
Requires: ruby
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildRequires: rubygem(diffy)
BuildRequires: rubygem(git)
BuildArch: noarch
Provides: foreman-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

# start package.json devDependencies BuildRequires
BuildRequires: (npm(@babel/core) >= 7.7.0 with npm(@babel/core) < 8.0.0)
BuildRequires: npm(@theforeman/builder) >= 12.0.1
BuildRequires: (npm(identity-obj-proxy) >= 3.0.0 with npm(identity-obj-proxy) < 4.0.0)
# end package.json devDependencies BuildRequires

# start package.json dependencies BuildRequires
# end package.json dependencies BuildRequires

%description
Engine to synchronise provisioning templates from GitHub.


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

# Ensure a git config file exists
mkdir -p %{buildroot}%{foreman_dir}/.config/git
touch %{buildroot}%{foreman_dir}/.config/git/config

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
%attr(-, foreman, foreman) %dir %{foreman_dir}/.config
%attr(-, foreman, foreman) %dir %{foreman_dir}/.config/git
%attr(0600, foreman, foreman) %config(noreplace) %{foreman_dir}/.config/git/config

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile

%posttrans
%{foreman_plugin_log}

%changelog
* Wed Aug 28 2024 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 9.5.1-2
- Add ownership of the git configuration file

* Sun Aug 11 2024 Foreman Packaging Automation <packaging@theforeman.org> - 9.5.1-1
- Update to 9.5.1

* Wed Jul 10 2024 Oleh Fedorenko <ofedoren@redhat.com> - 9.5.0-1
- Update to 9.5.0

* Tue May 07 2024 Evgeni Golov - 9.4.0-3
- Rebuild for Webpack asset compression

* Wed Jan 31 2024 Evgeni Golov - 9.4.0-2
- Rebuild for Webpack 5

* Thu May 25 2023 Oleh Fedorenko <ofedoren@redhat.com> 9.4.0-1
- Update to 9.4.0-1

* Wed Aug 24 2022 Evgeni Golov - 9.3.0-2
- Refs #35409 - Include sprockets assets

* Mon May 16 2022 Oleh Fedorenko <ofedoren@redhat.com> 9.3.0-1
- Update to 9.3.0

* Mon May 09 2022 Evgeni Golov - 9.2.0-3
- log plugin installation in posttrans

* Fri Apr 22 2022 Eric D. Helms <ericdhelms@gmail.com> - 9.2.0-2
- Stop generaing apipie cache

* Thu Feb 10 2022 Oleh Fedorenko <ofedoren@redhat.com> 9.2.0-1
- Update to 9.2.0

* Tue May 25 2021 Ondrej Prazak <oprazak@redhat.com> 9.1.0-1
- Update to 9.1.0

* Fri Apr 23 2021 Evgeni Golov 9.0.2-1
- Update to 9.0.2

* Thu Jul 30 2020 Ondrej Prazak <oprazak@redhat.com> 9.0.1-1
- Update to 9.0.1

* Tue Jul 21 2020 Evgeni Golov - 9.0.0-2
- Drop posttrans macros

* Mon May 18 2020 Ondrej Prazak <oprazak@redhat.com> 9.0.0-1
- Update to 9.0.0

* Thu Feb 20 2020 Ondrej Prazak <oprazak@redhat.com> 8.0.0-1
- Update to 8.0.0

* Tue Oct 15 2019 Ondrej Prazak <oprazak@redhat.com> 7.0.4-1
- Update to 7.0.4

* Fri Sep 07 2018 Eric D. Helms <ericdhelms@gmail.com> - 6.0.3-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Wed Jul 11 2018 Marek Hulan <mhulan@redhat.com> 6.0.3-1
- Update to 6.0.3

* Wed Jul 04 2018 Marek Hulan <mhulan@redhat.com> 6.0.2-1
- Update to 6.0.2

* Mon May 28 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 6.0.1-2
- Regenerate spec file based on the current template

* Thu May 17 2018 Marek Hulan <mhulan@redhat.com> 6.0.1-1
- Update to 6.0.1

* Tue Apr 10 2018 Marek Hulan <mhulan@redhat.com> 6.0.0-1
- Update to 6.0.0

* Wed Jan 10 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 5.0.1-2
- Bump Foreman plugins release (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Wed May 31 2017 Dominic Cleal <dominic@cleal.org> 5.0.1-1
- Update foreman_templates to 5.0.1 (mhulan@redhat.com)

* Wed Apr 26 2017 Dominic Cleal <dominic@cleal.org> 5.0.0-1
- Update foreman_templates to 5.0.0 (mhulan@redhat.com)

* Fri Apr 21 2017 Dominic Cleal <dominic@cleal.org> 4.0.2-1
- Update foreman_templates to 4.0.2 (mhulan@redhat.com)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Fri Feb 03 2017 Dominic Cleal <dominic@cleal.org> 4.0.1-1
- templates: 4.0.1 release (greg.sutcliffe@gmail.com)

* Tue Oct 04 2016 Dominic Cleal <dominic@cleal.org> 3.1.0-1
- templates: 3.1.0 release (greg.sutcliffe@gmail.com)

* Thu Sep 08 2016 Dominic Cleal <dominic@cleal.org> 3.0.0-1
- templates: 3.0.0 release (greg.sutcliffe@gmail.com)

* Thu May 12 2016 Dominic Cleal <dominic@cleal.org> 2.1.0-1
- Update foreman_templates to 2.1.0 (gsutclif@redhat.com)

* Wed Jan 06 2016 Dominic Cleal <dcleal@redhat.com> 2.0.3-1
- Update foreman_templates to 2.0.3 (dcleal@redhat.com)

* Thu Dec 24 2015 Dominic Cleal <dcleal@redhat.com> 2.0.1-2
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Wed Dec 02 2015 Dominic Cleal <dcleal@redhat.com> 2.0.1-1
- Update foreman_templates to 2.0.1 (dcleal@redhat.com)
- Add foremandist macro (dcleal@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 2.0.0-2
- Converted to tfm SCL (dcleal@redhat.com)

* Mon Jul 06 2015 Dominic Cleal <dcleal@redhat.com> 2.0.0-1
- Update foreman_templates to 2.0.0 (dcleal@redhat.com)

* Wed Mar 18 2015 Dominic Cleal <dcleal@redhat.com> 1.5.0-1
- Update foreman_templates to 1.5.0 (dcleal@redhat.com)

* Wed Feb 26 2014 Dominic Cleal <dcleal@redhat.com> 1.4.0-2
- Add git dependency (dcleal@redhat.com)

* Thu Jan 30 2014 Dominic Cleal <dcleal@redhat.com> 1.4.0-1
- Update to foreman_templates 1.4.0 (dcleal@redhat.com)

* Fri Dec 06 2013 Dominic Cleal <dcleal@redhat.com> 1.3.2-1
- Update to foreman_templates 1.3.2 (dcleal@redhat.com)

* Fri Dec 06 2013 Dominic Cleal <dcleal@redhat.com> 1.3.1-1
- Update to foreman_templates 1.3.1 (dcleal@redhat.com)

* Thu Dec 05 2013 Dominic Cleal <dcleal@redhat.com> 1.3.0-1
- Update to foreman_templates 1.3.0 (dcleal@redhat.com)

* Wed Nov 20 2013 Dominic Cleal <dcleal@redhat.com> 1.2.0-1
- new package built with tito
