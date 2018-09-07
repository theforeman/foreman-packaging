# template: foreman_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_default_hostgroup
%global plugin_name default_hostgroup
%global foreman_min_version 1.17.0

Summary:    Default Hostgroup Plugin for Foreman
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    5.0.0
Release:    3%{?foremandist}%{?dist}
Group:      Applications/Systems
License:    GPLv3
URL:        https://github.com/theforeman/foreman_default_hostgroup
Source0:    https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start generated dependencies
Requires: foreman >= %{foreman_min_version}
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
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
Adds the option to specify a default hostgroup for new hosts created from
facts/reports.


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

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_instdir}/app
%doc %{gem_instdir}/default_hostgroup.yaml.example
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%{foreman_bundlerd_plugin}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/test

%posttrans
%{foreman_restart}
exit 0

%changelog
* Fri Sep 07 2018 Eric D. Helms <ericdhelms@gmail.com> - 5.0.0-3
- Rebuild for Rails 5.2 and Ruby 2.5

* Sun May 27 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 5.0.0-2
- Regenerate spec file based on the current template

* Mon May 21 2018 Greg Sutcliffe <greg.sutcliffe@gmail.com> 5.0.0-1
- Update to 5.0.0
- 1.17 / Rails 5 - Module#prepend compatibility
- Fix source URL

* Mon Jan 15 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 4.0.1-1
- update foreman_default_hostgroup to 4.0.1 (kvedulv@kvedulv.de)

* Wed Jan 10 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 4.0.0-2
- Bump Foreman plugins release (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Wed Jul 06 2016 Dominic Cleal <dominic@cleal.org> 4.0.0-1
- Update foreman_default_hostgroup to 4.0.0 (gsutclif@redhat.com)

* Thu Dec 24 2015 Dominic Cleal <dcleal@redhat.com> 3.0.0-3
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)
- Add foremandist to more plugins (dcleal@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 3.0.0-2
- Converted to tfm SCL (dcleal@redhat.com)

* Mon Dec 15 2014 Dominic Cleal <dcleal@redhat.com> 3.0.0-1
- Update foreman_default_hostgroup to 3.0.0 (dcleal@redhat.com)

* Wed Apr 30 2014 Dominic Cleal <dcleal@redhat.com> 2.0.1-1
- Update to v2.0.1, add example config file (dcleal@redhat.com)

* Tue Apr 29 2014 Dominic Cleal <dcleal@redhat.com> 2.0.0-1
- Update to v2.0.0 (dcleal@redhat.com)

* Mon Feb 10 2014 Dominic Cleal <dcleal@redhat.com> 1.1.0-1
- Update to v1.1.0 (dcleal@redhat.com)

* Fri Oct 04 2013 Dominic Cleal <dcleal@redhat.com> 1.0.0-1
- new package built with tito
