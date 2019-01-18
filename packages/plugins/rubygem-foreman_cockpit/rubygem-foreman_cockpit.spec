# template: foreman_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_cockpit
%global plugin_name cockpit
%global foreman_min_version 1.7.0

Summary:    Use your hosts' Cockpit in Foreman
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    2.0.3
Release:    4%{?foremandist}%{?dist}
Group:      Applications/Systems
License:    GPLv3
URL:        https://github.com/theforeman/foreman_cockpit
Source0:    https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: foreman >= %{foreman_min_version}
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(deface) < 2.0
BuildRequires: foreman-assets >= %{foreman_min_version}
BuildRequires: foreman-plugin >= %{foreman_min_version}
BuildRequires: %{?scl_prefix}rubygem(deface) < 2.0
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-%{plugin_name}
# end specfile generated dependencies
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
This plugin adds a tab to see your host's Cockpit components, such as console,
journal, and networking if the host has Cockpit installed.


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
%{gem_instdir}/test

%posttrans
%{foreman_restart}
exit 0

%changelog
* Fri Sep 07 2018 Eric D. Helms <ericdhelms@gmail.com> - 2.0.3-4
- Rebuild for Rails 5.2 and Ruby 2.5

* Sat May 26 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 2.0.3-2
- Regenerate spec file based on the current template

* Wed Jan 10 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 2.0.3-2
- Bump Foreman plugins release (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Wed Jun 07 2017 Dominic Cleal <dominic@cleal.org> 2.0.3-1
- Updated foreman_cockpit to 2.0.3 (me@daniellobato.me)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Thu Aug 04 2016 Dominic Cleal <dominic@cleal.org> 2.0.2-1
- Updated foreman_cockpit to 2.0.2 (elobatocs@gmail.com)

* Mon Apr 11 2016 Dominic Cleal <dominic@cleal.org> 2.0.1-1
- plugins:foreman_cockpit - Release 2.0.1 (elobatocs@gmail.com)

* Thu Dec 24 2015 Dominic Cleal <dcleal@redhat.com> 1.0.3-2
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Thu Nov 05 2015 Dominic Cleal <dcleal@redhat.com> 1.0.3-1
- plugins:foreman_cockpit - Release 1.0.3 (elobatocs@gmail.com)

* Thu Oct 29 2015 Dominic Cleal <dcleal@redhat.com> 1.0.2-2
- Obsolete ruby193 package variant (dcleal@redhat.com)

* Tue Oct 27 2015 Dominic Cleal <dcleal@redhat.com> 1.0.2-1
- new package built with tito

