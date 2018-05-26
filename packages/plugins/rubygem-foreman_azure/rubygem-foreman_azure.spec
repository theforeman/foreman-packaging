# template: foreman_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_azure
%global plugin_name azure
%global foreman_min_version 1.11.0

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.3.1
Release: 2%{?foremandist}%{?dist}
Summary: Azure as a Compute Resource of Foreman (theforeman.org)
Group: Applications/Systems
License: GPLv3
URL: https://github.com/theforeman/foreman_azure
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start generated dependencies
Requires: foreman >= %{foreman_min_version}
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(fog-azure) = 0.0.2
Requires: %{?scl_prefix}rubygem(deface) < 2.0
BuildRequires: foreman-assets >= %{foreman_min_version}
BuildRequires: foreman-plugin >= %{foreman_min_version}
BuildRequires: %{?scl_prefix}rubygem(fog-azure) = 0.0.2
BuildRequires: %{?scl_prefix}rubygem(deface) < 2.0
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-%{plugin_name}
Provides: foreman-%{plugin_name}
# end generated dependencies

%description
Azure as a Compute Resource of Foreman.


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

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile

%posttrans
%{foreman_db_seed}
%{foreman_restart}
exit 0

%changelog
* Sat May 26 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.3.1-2
- Regenerate spec file based on the current template

* Fri Mar 24 2017 Dominic Cleal <dominic@cleal.org> 1.3.1-1
- Update foreman_azure to 1.3.1 (me@daniellobato.me)

* Wed Dec 21 2016 Dominic Cleal <dominic@cleal.org> 1.3.0-1
- Update foreman_azure to 1.3.0 (me@daniellobato.me)

* Fri Nov 18 2016 Dominic Cleal <dominic@cleal.org> 1.2.0-1
- Update foreman_azure to 1.2.0 (me@daniellobato.me)

* Tue Nov 15 2016 Dominic Cleal <dominic@cleal.org> 1.1.1-1
- Update foreman_azure to 1.1.1 (me@daniellobato.me)

* Tue Oct 04 2016 Dominic Cleal <dominic@cleal.org> 1.0.2-1
- Update foreman_azure to 1.0.2 (me@daniellobato.me)

* Tue Jun 14 2016 Dominic Cleal <dominic@cleal.org> 1.0.1-1
- new package built with tito

