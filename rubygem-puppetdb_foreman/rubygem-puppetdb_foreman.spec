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

%define rubyabi 1.9.1
%global foreman_dir /usr/share/foreman
%global foreman_bundlerd_dir %{foreman_dir}/bundler.d

Summary:    Foreman plugin to interact with PuppetDB
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    0.1.2
Release:    1%{?dist}
Group:      Applications/System
License:    GPLv3
URL:        https://github.com/cernops/puppetdb_foreman
Source0:    http://rubygems.org/downloads/%{gem_name}-%{version}.gem

Requires:   foreman >= 1.4.0

%if 0%{?fedora} > 18
Requires: %{?scl_prefix_ruby}ruby(release)
%else
Requires: %{?scl_prefix_ruby}ruby(abi) >= %{rubyabi}
%endif
Requires: %{?scl_prefix_ruby}rubygems

%if 0%{?fedora} > 18
BuildRequires: %{?scl_prefix_ruby}ruby(release)
%else
BuildRequires: %{?scl_prefix_ruby}ruby(abi) >= %{rubyabi}
%endif
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems

BuildArch: noarch

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-puppetdb
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
This is a foreman plugin to interact with PuppetDB through callbacks
and proxy the performance dashboard to Foreman.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0} --no-rdoc --no-ri
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{foreman_bundlerd_dir}
cat <<GEMFILE > %{buildroot}%{foreman_bundlerd_dir}/%{gem_name}.rb
gem '%{gem_name}'
GEMFILE

%files
%dir %{gem_instdir}
%{gem_instdir}/app
%{gem_instdir}/config
%{gem_instdir}/lib
%exclude %{gem_cache}
%{gem_spec}
%{foreman_bundlerd_dir}/%{gem_name}.rb

%exclude %{gem_dir}/cache/%{gem_name}-%{version}.gem

%changelog
* Tue Nov 11 2014 Daniel Lobato <dlobatog@redhat.com> 0.1.2-1
- Update to v0.1.2 (dlobatog@redhat.com)
- Better error handling for dashboard

* Fri Oct 11 2014 Daniel Lobato <dlobatog@redhat.com> 0.1.1-1
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
