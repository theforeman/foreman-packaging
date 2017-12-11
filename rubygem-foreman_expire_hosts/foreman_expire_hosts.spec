%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_expire_hosts

Summary:    A Foreman plugin to allow hosts to expire.
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    4.0.0
Release:    1%{?foremandist}%{?dist}
Group:      Applications/System
License:    GPLv3
URL:        https://github.com/theforeman/foreman_expire_hosts
Source0:    https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:    %{gem_name}.cron.d

Requires:   foreman >= 1.16.0
Requires:   %{?scl_prefix_ruby}ruby(release)
Requires:   %{?scl_prefix_ruby}rubygems
Requires:   %{?scl_prefix}rubygem(deface)
Requires:   /etc/cron.d
Requires:   %{?scl_prefix}rubygem(bootstrap-datepicker-rails)

BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems
BuildRequires: foreman-assets
BuildRequires: foreman-plugin >= 1.16.0
BuildRequires: %{?scl_prefix}rubygem(deface)
BuildRequires: %{?scl_prefix}rubygem(bootstrap-datepicker-rails)

BuildArch: noarch

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-expire_hosts

%description
A Foreman plugin that allows hosts to expire at a configurable date.
Hosts will be shut down and automatically deleted after a grace
period.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

install -Dp -m0644 %{SOURCE1} %{buildroot}%{?scl:%_root_sysconfdir}%{!?scl:%_sysconfdir}/cron.d/%{gem_name}

%{foreman_bundlerd_file}
%foreman_precompile_plugin -s

%posttrans
%{foreman_db_migrate}
%{foreman_db_seed}
%{foreman_restart}
exit 0

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%{gem_instdir}/app
%{gem_instdir}/lib
%{gem_instdir}/config
%{gem_instdir}/db
%exclude %{gem_cache}
%{foreman_bundlerd_plugin}
%{foreman_assets_plugin}
%{gem_spec}
%config %{?scl:%_root_sysconfdir}%{!?scl:%_sysconfdir}/cron.d/%{gem_name}
%doc %{gem_instdir}/LICENSE
%exclude %{gem_instdir}/test

%files doc
%{gem_instdir}/%{gem_name}.gemspec
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/Gemfile
%{gem_docdir}

%changelog
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
