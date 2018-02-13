# This package contains macros that provide functionality relating to
# Software Collections. These macros are not used in default
# Fedora builds, and should not be blindly copied or enabled.
# Specifically, the "scl" macro must not be defined in official Fedora
# builds. For more information, see:
# http://docs.fedoraproject.org/en-US/Fedora_Contributor_Documentation
# /1/html/Software_Collections_Guide/index.html

%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_chef

%global foreman_dir /usr/share/foreman
%global foreman_bundlerd_dir %{foreman_dir}/bundler.d

Summary:    Plugin for Chef integration with Foreman
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    0.6.0
Release:    1%{?foremandist}%{?dist}
Group:      Applications/System
License:    GPLv3
URL:        https://github.com/theforeman/foreman_chef
Source0:    https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires:   foreman >= 1.15.0

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}rubygems
Requires: %{?scl_prefix}rubygem(deface)
Requires: %{?scl_prefix}rubygem(foreman-tasks) >= 0.8.0

BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems
BuildRequires: %{?scl_prefix}rubygem(deface)
BuildRequires: %{?scl_prefix}rubygem(foreman-tasks) >= 0.8.0
BuildRequires: foreman-plugin >= 1.15.0
BuildRequires: foreman-assets

BuildArch: noarch

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-chef
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Foreman extensions that are required for better Chef integration.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
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


%foreman_bundlerd_file
%foreman_precompile_plugin -s

%files
%dir %{gem_instdir}
%{gem_instdir}/app
%{gem_instdir}/db
%{gem_instdir}/lib
%{gem_instdir}/config
%{foreman_bundlerd_plugin}
%exclude %{gem_cache}
%{foreman_assets_plugin}
%{gem_spec}
%doc %{gem_instdir}/LICENSE

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile

%posttrans
%foreman_db_migrate
%foreman_db_seed
%foreman_restart
exit 0

%changelog
* Tue Dec 26 2017 Daniel Lobato Garcia <me@daniellobato.me> 0.6.0-1
- Update foreman_chef to 0.6.0 (ares@users.noreply.github.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Fri Feb 03 2017 Dominic Cleal <dominic@cleal.org> 0.5.0-1
- Update foreman_chef to 0.5.0 (mhulan@redhat.com)

* Wed Jan 18 2017 Dominic Cleal <dominic@cleal.org> 0.4.2-1
- Update foreman_chef to 0.4.2 (mhulan@redhat.com)

* Mon Aug 22 2016 Dominic Cleal <dominic@cleal.org> 0.4.0-1
- Updates foreman_chef to 0.4.0 (mhulan@redhat.com)

* Mon Mar 07 2016 Dominic Cleal <dominic@cleal.org> 0.3.1-1
- Update foreman_chef to 0.3.1 (mhulan@redhat.com)

* Fri Mar 04 2016 Dominic Cleal <dominic@cleal.org> 0.3.0-1
- Update foreman_chef to 0.3.0 (mhulan@redhat.com)

* Thu Dec 24 2015 Dominic Cleal <dcleal@redhat.com> 0.2.0-3
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Oct 06 2015 Dominic Cleal <dcleal@redhat.com> 0.2.0-2
- Add foremandist for branched builds (dcleal@redhat.com)

* Tue Oct 06 2015 Dominic Cleal <dcleal@redhat.com> 0.2.0-1
- Update foreman_chef to 0.2.0 (mhulan@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 0.1.7-2
- Converted to tfm SCL (dcleal@redhat.com)

* Mon Aug 17 2015 Dominic Cleal <dcleal@redhat.com> 0.1.7-1
- Update foreman_chef to 0.1.7 (mhulan@redhat.com)

* Wed Jul 15 2015 Marek Hulan <mhulan@redhat.com> 0.1.6-1
- Update foreman_chef to 0.1.6 (mhulan@redhat.com)

* Wed Jul 08 2015 Dominic Cleal <dcleal@redhat.com> 0.1.5-1
- Update foreman_chef to 0.1.5 (mhulan@redhat.com)

* Mon Jun 22 2015 Marek Hulan <mhulan@redhat.com> 0.1.4-1
- Update foreman_chef to 0.1.4 (mhulan@redhat.com)

* Mon Mar 23 2015 Dominic Cleal <dcleal@redhat.com> 0.1.3-2
- Add db:migrate/seed postinstall steps (dcleal@redhat.com)

* Sun Mar 22 2015 Marek Hulan <mhulan@redhat.com> 0.1.3-1
- Update foreman_chef to 0.1.3 (mhulan@redhat.com)

* Tue Feb 24 2015 Marek Hulan <mhulan@redhat.com> 0.1.2-1
- Update foreman_chef to 0.1.2 (mhulan@redhat.com)

* Thu Jan 29 2015 Marek Hulan <mhulan@redhat.com> 0.1.1-1
- Update foreman_chef to 0.1.1 (mhulan@redhat.com)
- Fix RPM deps to match gemspec (dcleal@redhat.com)

* Wed Jan 14 2015 Marek Hulan <mhulan@redhat.com> 0.1.0-1
- Update foreman_chef to 0.1.0 (mhulan@redhat.com)

* Wed Jan 22 2014 Marek Hulan <mhulan@redhat.com> 0.0.4-1
- Update foreman_chef (mhulan@redhat.com)

* Mon Jan 20 2014 Marek Hulan <mhulan@redhat.com> 0.0.3-1
- new package built with tito
