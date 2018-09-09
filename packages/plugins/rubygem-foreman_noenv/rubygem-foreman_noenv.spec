# template: foreman_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_noenv
%global plugin_name noenv
%global foreman_min_version 1.8.0

Summary:    Agent-specified Environment Plugin for Foreman
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    0.0.7
Release:    4%{?foremandist}%{?dist}
Group:      Applications/Systems
License:    GPLv3
URL:        https://github.com/joshuabaird/foreman_noenv
Source0:    https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start generated dependencies
Requires: foreman >= %{foreman_min_version}
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(deface)
BuildRequires: foreman-plugin >= %{foreman_min_version}
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-%{plugin_name}
# end generated dependencies
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
The foreman_noenv plugin allows a hosts Puppet agent to specify a local
environment.


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

mkdir -p %{buildroot}%{foreman_pluginconf_dir}
mv %{buildroot}%{gem_instdir}/config/%{gem_name}.yaml \
   %{buildroot}%{foreman_pluginconf_dir}/%{gem_name}.yaml

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
%config %{foreman_pluginconf_dir}/%{gem_name}.yaml
%{foreman_bundlerd_plugin}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%posttrans
%{foreman_db_migrate}
%{foreman_restart}
exit 0

%changelog
* Sat Sep 08 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.0.7-4
- Rebuild for Rails 5.2 and Ruby 2.5

* Mon May 28 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 0.0.7-3
- Regenerate spec file based on the current template

* Wed Jan 10 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.0.7-2
- Bump Foreman plugins release (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Mon Nov 07 2016 Josh Baird <jbaird@follett.com> 0.0.7-1
- Support for Foreman 1.13.x

* Mon Aug 08 2016 Josh Baird <jbaird@follett.com> 0.0.6-1
- Fix whitelisting problem for noenv attribute

* Tue Apr 05 2016 Josh Baird <jbaird@follett.com> 0.0.5-1
- Support for Foreman 1.11.0/Ruby 2.2.4

* Thu Dec 24 2015 Dominic Cleal <dcleal@redhat.com> 0.0.4-3
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)
- Add foremandist to more plugins (dcleal@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 0.0.4-2
- Converted to tfm SCL (dcleal@redhat.com)

* Thu Aug 13 2015 Josh Baird <jbaird@follett.com> 0.0.4-1
- Run db:migrate in %posttrans

* Wed Aug 12 2015 Josh Baird <jbaird@follett.com> 0.0.3-1
- Fix typos and cleanup spec

* Tue Aug 11 2015 Josh Baird <jbaird@follett.com> 0.0.2-1
- Initial build of foreman_noenv 0.0.2-1
