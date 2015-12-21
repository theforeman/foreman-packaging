# This package contains macros that provide functionality relating to
# Software Collections. These macros are not used in default
# Fedora builds, and should not be blindly copied or enabled.
# Specifically, the "scl" macro must not be defined in official Fedora
# builds. For more information, see:
# http://docs.fedoraproject.org/en-US/Fedora_Contributor_Documentation
# /1/html/Software_Collections_Guide/index.html

%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_cockpit

Summary:    Integration of Cockpit in Foreman
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    1.0.3
Release:    1%{?foremandist}%{?dist}
Group:      Applications/System
License:    GPLv3
URL:        http://github.com/theforeman/foreman_cockpit
Source0:    http://rubygems.org/downloads/%{gem_name}-%{version}.gem

Requires:   foreman >= 1.7.0
Requires:   %{?scl_prefix}rubygem(deface) < 2.0

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}rubygems

BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems
BuildRequires: %{?scl_prefix}rubygem(deface) < 2.0
BuildRequires: foreman-plugin >= 1.7.0
BuildRequires: foreman-assets

BuildArch: noarch

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-cockpit
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
This plugin enables integration with Cockpit in Foreman.

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
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0} --no-rdoc --no-ri
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%foreman_bundlerd_file
%foreman_precompile_plugin -s

%files
%dir %{gem_instdir}
%{gem_instdir}/app
%{gem_instdir}/config
%{gem_instdir}/lib
%{gem_instdir}/locale
%exclude %{gem_cache}
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/test
%{gem_spec}
%{foreman_bundlerd_plugin}
%{foreman_assets_plugin}
%doc %{gem_instdir}/LICENSE

%files doc
%doc %{gem_instdir}/README.md

%posttrans
%foreman_restart
exit 0

%changelog
* Thu Nov 05 2015 Dominic Cleal <dcleal@redhat.com> 1.0.3-1
- plugins:foreman_cockpit - Release 1.0.3 (elobatocs@gmail.com)

* Thu Oct 29 2015 Dominic Cleal <dcleal@redhat.com> 1.0.2-2
- Obsolete ruby193 package variant (dcleal@redhat.com)

* Tue Oct 27 2015 Dominic Cleal <dcleal@redhat.com> 1.0.2-1
- new package built with tito

