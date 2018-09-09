# template: foreman_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_column_view
%global plugin_name column_view
%global foreman_min_version 1.17.0

Summary:    Column View Plugin for Foreman
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    0.4.0
Release:    3%{?foremandist}%{?dist}
Group:      Applications/Systems
License:    GPLv3
URL:        https://github.com/theforeman/foreman_column_view
Source0:    https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start generated dependencies
Requires: foreman >= %{foreman_min_version}
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(deface) < 2.0
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
Displays an additional column in the Foreman Hosts view
and/or additional entries in the Host show page.


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
cat <<CONFIG > %{buildroot}%{foreman_pluginconf_dir}/%{gem_name}.yaml.example
# Copy this file to %{gem_name}.yaml to enable, then restart Foreman
#
# See %{name}-doc and %{gem_instdir}/README.md for more information
:column_view:
  :architecture:
    :title: Architecture
    :after: last_report
    :content: facts_hash['architecture']
  :uptime:
    :title: Uptime
    :after: architecture
    :content: facts_hash['uptime']
CONFIG

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_instdir}/app
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%{foreman_bundlerd_plugin}
%doc %{foreman_pluginconf_dir}/%{gem_name}.yaml.example

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile

%posttrans
%{foreman_restart}
exit 0

%changelog
* Sat Sep 08 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.4.0-3
- Rebuild for Rails 5.2 and Ruby 2.5

* Sun May 27 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 0.4.0-2
- Regenerate spec file based on the current template

* Thu May 17 2018 Greg Sutcliffe <greg.sutcliffe@gmail.com> 0.4.0-1
- Update to 0.4.0
-   * 1.17 / Rails 5 - Module#prepend compatibility

* Wed Jan 10 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.3.0-2
- Bump Foreman plugins release (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Wed Oct 05 2016 Dominic Cleal <dominic@cleal.org> 0.3.0-1
- column_view: 0.3.0 release (greg.sutcliffe@gmail.com)
- Use gem_install macro, tidy up (dominic@cleal.org)

* Thu Dec 24 2015 Dominic Cleal <dcleal@redhat.com> 0.2.1-3
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)
- Add foremandist to more plugins (dcleal@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 0.2.1-2
- Converted to tfm SCL (dcleal@redhat.com)

* Mon Aug 03 2015 Dominic Cleal <dcleal@redhat.com> 0.2.1-1
- Update foreman_column_view to 0.2.1 (dcleal@redhat.com)

* Wed Feb 26 2014 Dominic Cleal <dcleal@redhat.com> 0.2.0-1
- Update to v0.2.0 (dcleal@redhat.com)
- Remove SCL prefix from foreman-plugin-* provide (dcleal@redhat.com)

* Tue Aug 20 2013 Dominic Cleal <dcleal@redhat.com> 0.1.2-1
- new package built with tito
