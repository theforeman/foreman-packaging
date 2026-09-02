# template: foreman_plugin
%global gem_name foreman_omaha
%global plugin_name omaha
%global foreman_min_version 3.0

Name: rubygem-%{gem_name}
Version: 5.1.0
Release: 1%{?foremandist}%{?dist}
Summary: This plug-in adds support for the Omaha procotol to The Foreman
License: GPL-3
URL: https://github.com/theforeman/foreman_omaha
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: foreman >= %{foreman_min_version}
BuildRequires: foreman-assets >= %{foreman_min_version}
BuildRequires: foreman-plugin >= %{foreman_min_version}
Requires: ruby >= 3.0
BuildRequires: ruby >= 3.0
BuildRequires: rubygems-devel
BuildRequires: rubygem(jquery-matchheight-rails)
BuildArch: noarch
Provides: foreman-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

%description
This plug-in adds support for the Omaha procotol to The Foreman. It allows you
to better manage and update your CoreOS servers.


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
* Wed Sep  2 04:26:43 UTC 2026 Foreman Packaging Automation <packaging@theforeman.org> - 5.1.0-1
- Update to 5.1.0

* Wed Aug 24 2022 Evgeni Golov - 5.0.1-2
- Refs #35409 - Include sprockets assets

* Thu May 26 2022 Foreman Packaging Automation <packaging@theforeman.org> 5.0.1-1
- Update to 5.0.1

* Mon May 09 2022 Evgeni Golov - 4.0.1-4
- log plugin installation in posttrans

* Fri Apr 22 2022 Eric D. Helms <ericdhelms@gmail.com> - 4.0.1-3
- Stop generaing apipie cache

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 4.0.1-2
- Rebuild plugins for Ruby 2.7

* Thu Apr 09 2020 Timo Goebel <mail@timogoebel.name> - 4.0.1-1
- Update foreman_omaha to 4.0.1

* Tue Jan 07 2020 Eric D. Helms <ericdhelms@gmail.com> - 3.0.0-2
- Drop migrate, seed and restart posttans

* Thu Nov 29 2018 Timo Goebel <mail@timogoebel.name> - 3.0.0-1
- Update foreman_omaha to 3.0.0

* Fri Sep 07 2018 Eric D. Helms <ericdhelms@gmail.com> - 2.0.0-2
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jun 29 2018 Timo Goebel <mail@timogoebel.name> - 2.0.0-1
- Update foreman_omaha to 2.0.0

* Mon May 28 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.0.0-2
- Regenerate spec file based on the current template

* Tue Jan 16 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.0.0-1
- Update foreman_omaha to 1.0.0 (mail@timogoebel.name)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Wed Sep 06 2017 Daniel Lobato Garcia <me@daniellobato.me> 0.0.3-1
- Update foreman_omaha to 0.0.3 (mail@timogoebel.name)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Mon Oct 24 2016 Dominic Cleal <dominic@cleal.org> 0.0.2-1
- Update foreman_omaha to 0.0.2 (timo.goebel@dm.de)

* Mon Oct 17 2016 Dominic Cleal <dominic@cleal.org> 0.0.1-1
- new package built with tito

