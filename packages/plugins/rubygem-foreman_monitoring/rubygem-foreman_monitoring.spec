# template: foreman_plugin
%global gem_name foreman_monitoring
%global plugin_name monitoring
%global foreman_min_version 3.13

Name: rubygem-%{gem_name}
Version: 3.4.0
Release: 1%{?foremandist}%{?dist}
Summary: Foreman plugin for monitoring system integration
License: GPLv3
URL: https://github.com/theforeman/foreman_monitoring
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: foreman >= %{foreman_min_version}
BuildRequires: foreman-plugin >= %{foreman_min_version}
Requires: ruby >= 2.7
Requires: ruby < 4
BuildRequires: ruby >= 2.7
BuildRequires: ruby < 4
BuildRequires: rubygems-devel
BuildArch: noarch
Provides: foreman-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

%description
Foreman plugin for monitoring system integration.


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

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%posttrans
%{foreman_plugin_log}

%changelog
* Tue Aug 19 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.4.0-1
- Update to 3.4.0

* Thu May 08 2025 Foreman Packaging Automation <packaging@theforeman.org> - 3.3.0-1
- Update to 3.3.0

* Thu Sep 05 2024 Evgeni Golov - 3.2.0-2
- Rebuild against Foreman nightly

* Sun Jun 02 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.2.0-1
- Update to 3.2.0

* Tue May 28 2024 Foreman Packaging Automation <packaging@theforeman.org> - 3.1.0-1
- Update to 3.1.0

* Wed Nov 02 2022 Dirk Goetz 3.0.0-1
- Update to 3.0.0

* Mon May 09 2022 Evgeni Golov - 2.1.0-4
- log plugin installation in posttrans

* Fri Apr 22 2022 Eric D. Helms <ericdhelms@gmail.com> - 2.1.0-3
- Stop generaing apipie cache

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 2.1.0-2
- Rebuild plugins for Ruby 2.7

* Tue Dec 01 2020 Dirk Goetz 2.1.0-1
- Update to 2.1.0

* Tue Aug 11 2020 Manuel Laug <manuel.laug@dm.de> - 2.0.0-1
- Update foreman_monitoring to 2.0.0

* Tue Jan 07 2020 Eric D. Helms <ericdhelms@gmail.com> - 1.0.1-4
- Drop migrate, seed and restart posttans

* Fri Sep 07 2018 Eric D. Helms <ericdhelms@gmail.com> - 1.0.1-3
- Rebuild for Rails 5.2 and Ruby 2.5

* Mon May 28 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.0.1-2
- Regenerate spec file based on the current template

* Mon Jan 15 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.0.0-2
- Update foreman_monitoring to 1.0.0 (mail@timogoebel.name)

* Wed Jan 10 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.1.1-2
- Bump Foreman plugins release (ericdhelms@gmail.com)

* Tue Oct 24 2017 Daniel Lobato Garcia <me@daniellobato.me> 0.1.1-1
- Update foreman_monitoring to 0.1.1 (mail@timogoebel.name)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)

* Thu Apr 13 2017 Dirk Goetz <dirk.goetz> - 0.1.0-1
- updated upstream

* Fri Aug 19 2016 Dirk Goetz <dirk.goetz> - 0.0.3-1
- initial build
