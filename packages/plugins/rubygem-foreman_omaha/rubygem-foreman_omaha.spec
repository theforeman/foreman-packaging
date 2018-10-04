# template: foreman_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_omaha
%global plugin_name omaha
%global foreman_min_version 1.18.0

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 2.0.0
Release: 2%{?foremandist}%{?dist}
Summary: This plug-in adds support for the Omaha procotol to The Foreman
Group: Applications/Systems
License: GPLv3
URL: https://github.com/theforeman/foreman_omaha
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start generated dependencies
Requires: foreman >= %{foreman_min_version}
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(jquery-matchheight-rails)
BuildRequires: foreman-assets >= %{foreman_min_version}
BuildRequires: foreman-plugin >= %{foreman_min_version}
BuildRequires: %{?scl_prefix}rubygem(jquery-matchheight-rails)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-%{plugin_name}
# end generated dependencies
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
This plug-in adds support for the Omaha procotol to The Foreman. It allows you
to better manage and update your CoreOS servers.


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
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%foreman_bundlerd_file
%foreman_precompile_plugin -a -s

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
%{foreman_apipie_cache_foreman}
%{foreman_apipie_cache_plugin}
%{foreman_assets_plugin}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%posttrans
%{foreman_db_migrate}
%{foreman_db_seed}
%{foreman_apipie_cache}
%{foreman_restart}
exit 0

%changelog
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

