# template: foreman_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_expire_hosts
%global plugin_name expire_hosts
%global foreman_min_version 1.17.0

Summary:    Foreman plugin for limiting host lifetime
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    5.1.0
Release:    4%{?foremandist}%{?dist}
Group:      Applications/Systems
License:    GPLv3
URL:        https://github.com/theforeman/foreman_expire_hosts
Source0:    https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:    %{gem_name}.cron.d

Requires:   %{?scl:%_root_sysconfdir}%{!?scl:%_sysconfdir}/cron.d
# start specfile generated dependencies
Requires: foreman >= %{foreman_min_version}
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(bootstrap-datepicker-rails)
Requires: %{?scl_prefix}rubygem(deface)
BuildRequires: foreman-assets >= %{foreman_min_version}
BuildRequires: foreman-plugin >= %{foreman_min_version}
BuildRequires: %{?scl_prefix}rubygem(bootstrap-datepicker-rails)
BuildRequires: %{?scl_prefix}rubygem(deface)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-%{plugin_name}
# end specfile generated dependencies

%description
A Foreman plugin that allows hosts to expire at a configurable date.
Hosts will be shut down and automatically deleted after a grace
period.

%package doc
BuildArch:  noarch
Group:      Documentation
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Summary:    Documentation for %{pkg_name}

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
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

install -Dp -m0644 %{SOURCE1} %{buildroot}%{?scl:%_root_sysconfdir}%{!?scl:%_sysconfdir}/cron.d/%{gem_name}

%foreman_bundlerd_file
%foreman_precompile_plugin -a -s

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.rubocop.yml
%exclude %{gem_instdir}/.rubocop_todo.yml
%license %{gem_instdir}/LICENSE
%{gem_instdir}/app
%{gem_instdir}/config
%{gem_instdir}/db
%exclude %{gem_instdir}/foreman_expire_hosts.gemspec
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%config(noreplace) %{?scl:%_root_sysconfdir}%{!?scl:%_sysconfdir}/cron.d/%{gem_name}
%{foreman_bundlerd_plugin}
%{foreman_apipie_cache_foreman}
%{foreman_apipie_cache_plugin}
%{foreman_assets_plugin}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/test

%posttrans
%{foreman_db_migrate}
%{foreman_db_seed}
%{foreman_apipie_cache}
%{foreman_restart}
exit 0

%changelog
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
