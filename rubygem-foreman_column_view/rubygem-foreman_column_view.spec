# This package contains macros that provide functionality relating to
# Software Collections. These macros are not used in default
# Fedora builds, and should not be blindly copied or enabled.
# Specifically, the "scl" macro must not be defined in official Fedora
# builds. For more information, see:
# http://docs.fedoraproject.org/en-US/Fedora_Contributor_Documentation
# /1/html/Software_Collections_Guide/index.html

%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_column_view

%global foreman_dir /usr/share/foreman
%global foreman_bundlerd_dir %{foreman_dir}/bundler.d
%global foreman_pluginconf_dir /etc/foreman/plugins

Summary:    Column View Plugin for Foreman
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    0.4.0
Release:    1%{?foremandist}%{?dist}
Group:      Applications/System
License:    GPLv3
URL:        https://github.com/theforeman/foreman_column_view
Source0:    https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires:   foreman >= 1.17.0
Requires:   %{?scl_prefix}rubygem(deface) < 2.0

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}rubygems

BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems

BuildArch: noarch

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-column_view
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Displays an additional column in the Foreman Hosts view and/or additional
entries in the Host show page.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{foreman_bundlerd_dir}
cat <<GEMFILE > %{buildroot}%{foreman_bundlerd_dir}/%{gem_name}.rb
gem '%{gem_name}'
GEMFILE

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
%{gem_instdir}/app
%{gem_instdir}/lib
%exclude %{gem_cache}
%{gem_spec}
%{foreman_bundlerd_dir}/%{gem_name}.rb
%doc %{foreman_pluginconf_dir}/%{gem_name}.yaml.example
%doc %{gem_instdir}/LICENSE

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile

%changelog
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
