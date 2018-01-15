# This package contains macros that provide functionality relating to
# Software Collections. These macros are not used in default
# Fedora builds, and should not be blindly copied or enabled.
# Specifically, the "scl" macro must not be defined in official Fedora
# builds. For more information, see:
# http://docs.fedoraproject.org/en-US/Fedora_Contributor_Documentation
# /1/html/Software_Collections_Guide/index.html

%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name puppetdb_foreman

%global foreman_dir /usr/share/foreman
%global foreman_bundlerd_dir %{foreman_dir}/bundler.d

Summary:    Foreman plugin to interact with PuppetDB
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    4.0.0
Release:    1%{?foremandist}%{?dist}
Group:      Applications/System
License:    GPLv3
URL:        https://github.com/theforeman/puppetdb_foreman
Source0:    https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires:   foreman >= 1.17.0

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}rubygems

BuildRequires: foreman-plugin >= 1.17.0
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel

BuildArch: noarch

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-puppetdb
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
This is a foreman plugin to interact with PuppetDB through callbacks
and proxy the performance dashboard to Foreman.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

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

%foreman_bundlerd_file
%foreman_precompile_plugin -a

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
%{foreman_apipie_cache_foreman}
%{foreman_apipie_cache_plugin}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%posttrans
%{foreman_db_migrate}
%{foreman_apipie_cache}
%{foreman_restart}
exit 0

%changelog
* Wed Sep 06 2017 Daniel Lobato Garcia <me@daniellobato.me> 3.1.2-1
- Update puppetdb_foreman to 3.1.2 (mail@timogoebel.name)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Fri Apr 28 2017 Dominic Cleal <dominic@cleal.org> 3.0.2-1
- Update puppetdb_foreman to 3.0.2 (mail@timogoebel.name)

* Wed Apr 26 2017 Dominic Cleal <dominic@cleal.org> 3.0.1-1
- Update puppetdb_foreman to 3.0.1 (mail@timogoebel.name)

* Fri Jan 13 2017 Dominic Cleal <dominic@cleal.org> 2.0.0-1
- Release puppetdb_foreman 2.0 (me@daniellobato.me)
- Use gem_install to build rubygem (dominic@cleal.org)

* Fri Sep 30 2016 Dominic Cleal <dominic@cleal.org> 1.0.4-1
- Update puppetdb_foreman 1.0.4 (me@daniellobato.me)

* Tue Apr 19 2016 Dominic Cleal <dominic@cleal.org> 1.0.3-1
- plugins:puppetdb_foreman - Release 1.0.3 (elobatocs@gmail.com)

* Thu Mar 03 2016 Dominic Cleal <dominic@cleal.org> 1.0.2-1
- plugins:puppetdb_foreman - Release 1.0.2 (elobatocs@gmail.com)

* Thu Dec 24 2015 Dominic Cleal <dcleal@redhat.com> 0.2.0-2
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Fri Nov 13 2015 Dominic Cleal <dcleal@redhat.com> 0.2.0-1
- plugins:puppetdb_foreman - Release 0.2.0 (elobatocs@gmail.com)

* Mon Oct 26 2015 Dominic Cleal <dcleal@redhat.com> 0.1.3-1
- plugins:puppetdb_foreman - Release 0.1.3 (elobatocs@gmail.com)
- Add foremandist macro (dcleal@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 0.1.2-2
- Converted to tfm SCL (dcleal@redhat.com)

* Tue Nov 11 2014 Daniel Lobato <dlobatog@redhat.com> 0.1.2-1
- Update to v0.1.2 (dlobatog@redhat.com)
- Better error handling for dashboard

* Sat Oct 11 2014 Daniel Lobato <dlobatog@redhat.com> 0.1.1-1
- Update to v0.1.1 (dlobatog@redhat.com)
- Proxy PuppetDB dashboard

* Fri Oct 03 2014 Daniel Lobato <dlobatog@redhat.com> 0.0.9-1
- Update to v0.0.9 (dlobatog@redhat.com)
- Deactivate host after build

* Fri Sep 19 2014 Daniel Lobato <dlobatog@redhat.com> 0.0.8-1
- Update to v0.0.8 (dlobatog@redhat.com)
- Setting puppetdb_enabled is now a boolean

* Mon Jul 21 2014 Dominic Cleal <dcleal@redhat.com> 0.0.7-1
- Update to v0.0.7 (dcleal@redhat.com)

* Mon Jul 21 2014 Dominic Cleal <dcleal@redhat.com> 0.0.6-1
- Update to v0.0.6
- Config file removed and replaced with in-app settings

* Thu Jan 30 2014 Dominic Cleal <dcleal@redhat.com> 0.0.5-1
- Update to v0.0.5 (dcleal@redhat.com)

* Tue Nov 05 2013 Dominic Cleal <dcleal@redhat.com> 0.0.4-2
- Install disabled config file by default (dcleal@redhat.com)

* Tue Sep 10 2013 Dominic Cleal <dcleal@redhat.com> 0.0.4-1
- new package built with tito
