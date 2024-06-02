# template: foreman_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}
%{!?_root_sysconfdir:%global _root_sysconfdir %{_sysconfdir}}

%global gem_name foreman_expire_hosts
%global plugin_name expire_hosts
%global foreman_min_version 3.0.0

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 8.2.0
Release: 1%{?foremandist}%{?dist}
Summary: Foreman plugin for limiting host lifetime
Group: Applications/Systems
License: GPLv3
URL: https://github.com/theforeman/foreman_expire_hosts
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: %{gem_name}.cron.d

# start specfile generated dependencies
Requires: foreman >= %{foreman_min_version}
BuildRequires: foreman-plugin >= %{foreman_min_version}
Requires: ruby
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildArch: noarch
Provides: foreman-plugin-%{plugin_name} = %{version}
# end specfile generated dependencies

%description
This Plugin will add new column expired_on to hosts to limit the lifetime of a
host.


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

mkdir -p %{buildroot}%{_root_sysconfdir}/cron.d/
mv %{buildroot}%{gem_instdir}/extra/*.cron %{buildroot}%{_root_sysconfdir}/cron.d/%{gem_name}
%foreman_bundlerd_file

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_instdir}/app
%{gem_instdir}/config
%{gem_instdir}/db
%{gem_instdir}/extra
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%{foreman_bundlerd_plugin}
%config(noreplace) %{_root_sysconfdir}/cron.d/%{gem_name}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/test

%posttrans
%{foreman_plugin_log}

%changelog
* Sun Jun 02 2024 Foreman Packaging Automation <packaging@theforeman.org> - 8.2.0-1
- Update to 8.2.0

* Mon Mar 06 2023 Foreman Packaging Automation <packaging@theforeman.org> 8.1.0-1
- Update to 8.1.0

* Mon Oct 24 2022 Marek Hulan <mhulan@redhat.com> 8.0.0-1
- Update to 8.0.0

* Mon May 09 2022 Evgeni Golov - 7.0.4-4
- log plugin installation in posttrans

* Fri Apr 22 2022 Eric D. Helms <ericdhelms@gmail.com> - 7.0.4-3
- Stop generaing apipie cache

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 7.0.4-2
- Rebuild plugins for Ruby 2.7

* Tue Feb 02 2021 Manuel Laug <laugmanuel@gmail.com> - 7.0.4-1
- Update foreman_expire_hosts to 7.0.4

* Mon Mar 16 2020 Timo Goebel <mail@timogoebel.name> - 7.0.1-1
- Update foreman_expire_hosts to 7.0.1

* Tue Jan 07 2020 Eric D. Helms <ericdhelms@gmail.com> - 7.0.0-2
- Drop migrate, seed and restart posttans

* Tue Dec 10 2019 Timo Goebel <mail@timogoebel.name> - 7.0.0-1
- Update foreman_expire_hosts to 7.0.0

* Fri Aug 30 2019 Timo Goebel <mail@timogoebel.name> - 6.0.2-1
- Update foreman_expire_hosts to 6.0.2

* Mon Jul 01 2019 Timo Goebel <mail@timogoebel.name> - 6.0.1-1
- Update foreman_expire_hosts to 6.0.1

* Fri Mar 08 2019 Timo Goebel <mail@timogoebel.name> - 6.0.0-1
- Update foreman_expire_hosts to 6.0.0

* Fri Sep 07 2018 Eric D. Helms <ericdhelms@gmail.com> - 5.1.0-4
- Rebuild for Rails 5.2 and Ruby 2.5

* Wed May 30 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 5.1.0-3
- Correct cron.d location

* Sun May 27 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 5.1.0-2
- Regenerate spec file based on the current template

* Thu Apr 26 2018 Timo Goebel <mail@timogoebel.name> - 5.1.0-1
 - Update foreman_expire_hosts to 5.1.0

* Mon Jan 22 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 5.0.0-1
- Update foreman_expire_hosts to 5.0.0 (mail@timogoebel.name)
- Correct non-existing date (ewoud@kohlvanwijngaarden.nl)

* Mon Dec 11 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 4.0.0-1
- Update foreman_expire_hosts to 4.0.0 (mail@timogoebel.name)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Mon Apr 24 2017 Dominic Cleal <dominic@cleal.org> 3.0.0-1
- Update foreman_expire_hosts to 3.0.0 (mail@timogoebel.name)

* Wed Feb 22 2017 Dominic Cleal <dominic@cleal.org> 2.2.0-1
- Update foreman_expire_hosts to 2.2.0 (mail@timogoebel.name)

* Wed Dec 21 2016 Dominic Cleal <dominic@cleal.org> 2.1.2-1
- Update foreman_expire_hosts to 2.1.2 (timo.goebel@dm.de)

* Mon Oct 24 2016 Dominic Cleal <dominic@cleal.org> 2.1.1-1
- Update foreman_expire_hosts to 2.1.1 (timo.goebel@dm.de)

* Thu Oct 20 2016 Dominic Cleal <dominic@cleal.org> 2.1.0-1
- Update foreman_expire_hosts to 2.1.0 (timo.goebel@dm.de)

* Thu Jul 07 2016 Timo Goebel <mail@timogoebel.name> 2.0.2-1
- release v2.0.2

* Fri Jun 17 2016 Timo Goebel <mail@timogoebel.name> 2.0.1-1
- release v2.0.1

* Tue Jun 07 2016 Timo Goebel <mail@timogoebel.name> 2.0.0-1
- initial packaging
