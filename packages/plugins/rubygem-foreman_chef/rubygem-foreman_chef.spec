# template: foreman_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_chef
%global plugin_name chef
%global foreman_min_version 1.17.0

Summary:    Plugin for Chef integration with Foreman
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    0.8.0
Release:    2%{?foremandist}%{?dist}
Group:      Applications/Systems
License:    GPLv3
URL:        https://github.com/theforeman/foreman_chef
Source0:    https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start generated dependencies
Requires: foreman >= %{foreman_min_version}
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(deface)
Requires: %{?scl_prefix}rubygem(foreman-tasks) >= 0.8.0
BuildRequires: foreman-assets >= %{foreman_min_version}
BuildRequires: foreman-plugin >= %{foreman_min_version}
BuildRequires: %{?scl_prefix}rubygem(deface)
BuildRequires: %{?scl_prefix}rubygem(foreman-tasks) >= 0.8.0
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-%{plugin_name}
# end generated dependencies
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Foreman extensions that are required for better Chef integration.

%package doc
BuildArch:  noarch
Group:      Documentation
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
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

%foreman_bundlerd_file
%foreman_precompile_plugin -s

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_instdir}/app
%{gem_instdir}/config
%{gem_instdir}/db
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%{foreman_bundlerd_plugin}
%{foreman_assets_plugin}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile

%posttrans
%{foreman_db_migrate}
%{foreman_restart}
exit 0

%changelog
* Tue Jun 19 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.8.0-2
- Regenerate spec file based on the current template

* Tue Jun 05 2018 Marek Hulan <mhulan@redhat.com> 0.8.0-1
- Update to 0.8.0

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
