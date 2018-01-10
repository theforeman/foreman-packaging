# This package contains macros that provide functionality relating to
# Software Collections. These macros are not used in default
# Fedora builds, and should not be blindly copied or enabled.
# Specifically, the "scl" macro must not be defined in official Fedora
# builds. For more information, see:
# http://docs.fedoraproject.org/en-US/Fedora_Contributor_Documentation
# /1/html/Software_Collections_Guide/index.html

%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_graphite

%global foreman_dir /usr/share/foreman
%global foreman_bundlerd_dir %{foreman_dir}/bundler.d
%global foreman_pluginconf_dir /etc/foreman/plugins

Summary:    Adds graphite integration to Foreman
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    0.0.3
Release:    4%{?foremandist}%{?dist}
Group:      Applications/System
License:    GPLv3
URL:        https://github.com/theforeman/foreman_graphite
Source0:    https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires:   foreman >= 1.7.0

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}rubygems
Requires: %{?scl_prefix}rubygem(graphite-api)

BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems

BuildArch: noarch

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-graphite
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Adds graphite support for Foreman.

This Foreman plugin allows to use graphite to track performance metrics of
your Foreman instances.

You will need to install a graphite instance to use this plugin.

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

mkdir -p %{buildroot}%{foreman_bundlerd_dir}
cat <<GEMFILE > %{buildroot}%{foreman_bundlerd_dir}/%{gem_name}.rb
gem '%{gem_name}'
GEMFILE

mkdir -p %{buildroot}%{foreman_pluginconf_dir}
mv %{buildroot}%{gem_instdir}/%{gem_name}.yaml.example %{buildroot}%{foreman_pluginconf_dir}

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_spec}
%{foreman_bundlerd_dir}/%{gem_name}.rb
%doc %{gem_instdir}/LICENSE
%doc %{foreman_pluginconf_dir}/%{gem_name}.yaml.example

%exclude %{gem_cache}
%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/Rakefile

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%posttrans
(/sbin/service foreman status && /sbin/service foreman restart) >/dev/null 2>&1
exit 0

%changelog
* Wed Jan 10 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.0.3-4
- Bump Foreman plugins release (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Thu Dec 24 2015 Dominic Cleal <dcleal@redhat.com> 0.0.3-3
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)
- Add foremandist to more plugins (dcleal@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 0.0.3-2
- Converted to tfm SCL (dcleal@redhat.com)

* Wed Mar 11 2015 Dominic Cleal <dcleal@redhat.com> 0.0.3-1
- Update foreman_graphite to 0.0.3 (dcleal@redhat.com)

* Wed Jan 14 2015 Dominic Cleal <dcleal@redhat.com> 0.0.2-1
- new package built with tito
