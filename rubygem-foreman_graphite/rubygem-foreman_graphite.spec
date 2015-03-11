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

%define rubyabi 1.9.1
%global foreman_dir /usr/share/foreman
%global foreman_bundlerd_dir %{foreman_dir}/bundler.d
%global foreman_pluginconf_dir /etc/foreman/plugins

Summary:    Adds graphite integration to Foreman
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    0.0.3
Release:    1%{?dist}
Group:      Applications/System
License:    GPLv3
URL:        http://github.com/theforeman/foreman_graphite
Source0:    http://rubygems.org/downloads/%{gem_name}-%{version}.gem

Requires:   foreman >= 1.7.0

%if 0%{?fedora} > 18
Requires: %{?scl_prefix}ruby(release)
%else
Requires: %{?scl_prefix}ruby(abi) >= %{rubyabi}
%endif
Requires: %{?scl_prefix}rubygems
Requires: %{?scl_prefix}rubygem(graphite-api)

%if 0%{?fedora} > 18
BuildRequires: %{?scl_prefix}ruby(release)
%else
BuildRequires: %{?scl_prefix}ruby(abi) >= %{rubyabi}
%endif
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygems

BuildArch: noarch

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-graphite

%description
Adds graphite support for Foreman.

This Foreman plugin allows to use graphite to track performance metrics of
your Foreman instances.

You will need to install a graphite instance to use this plugin.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

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
%doc %{gem_instdir}/README.md

%posttrans
(/sbin/service foreman status && /sbin/service foreman restart) >/dev/null 2>&1
exit 0

%changelog
* Wed Jan 14 2015 Dominic Cleal <dcleal@redhat.com> 0.0.2-1
- new package built with tito

