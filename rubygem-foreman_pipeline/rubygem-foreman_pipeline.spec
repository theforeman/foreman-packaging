# This package contains macros that provide functionality relating to
# Software Collections. These macros are not used in default
# Fedora builds, and should not be blindly copied or enabled.
# Specifically, the "scl" macro must not be defined in official Fedora
# builds. For more information, see:
# http://docs.fedoraproject.org/en-US/Fedora_Contributor_Documentation
# /1/html/Software_Collections_Guide/index.html

%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_pipeline
%global foreman_dir /usr/share/foreman

Summary:    A Foreman plugin that cooperates with Jenkins
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    0.1.0
Release:    1%{?foremandist}%{?dist}
Group:      Applications/System
License:    GPLv3
URL:        http://github.com/theforeman/foreman_pipeline
Source0:    http://rubygems.org/downloads/%{gem_name}-%{version}.gem

Requires:   foreman >= 1.13.0
Requires:   %{?scl_prefix}rubygem(jenkins_api_client) < 2.0.0
Requires:   %{?scl_prefix}rubygem-katello >= 3.0.0
Requires:   %{?scl_prefix}rubygem-katello < 4.0.0
Requires:   %{?scl_prefix}rubygem(bastion) >= 3.0.0
Requires:   %{?scl_prefix}rubygem(bastion) < 4.0.0
Requires:   %{?scl_prefix_ruby}ruby(release)
Requires:   %{?scl_prefix_ruby}ruby(rubygems)

BuildRequires: foreman-assets
BuildRequires: foreman-plugin >= 1.13.0
BuildRequires: %{?scl_prefix}rubygem(jenkins_api_client) < 2.0.0
BuildRequires: %{?scl_prefix}rubygem-katello >= 3.0.0
BuildRequires: %{?scl_prefix}rubygem-katello < 4.0.0
BuildRequires: %{?scl_prefix}rubygem(bastion) >= 3.0.0
BuildRequires: %{?scl_prefix}rubygem(bastion) < 4.0.0
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}ruby(release)

BuildArch: noarch

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-pipeline

%description
This plugin allows Jenkins to deploy artifacts onto newly 
provisioned host by Foreman.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%setup -q -c -T -n %{pkg_name}-%{version}
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
%foreman_precompile_plugin -s -a

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_instdir}/app
%{gem_instdir}/config
%{gem_instdir}/db
%{gem_instdir}/script
%{gem_spec}
%{foreman_bundlerd_plugin}
%{foreman_apipie_cache_foreman}
%{foreman_apipie_cache_plugin}
%{foreman_assets_plugin}

%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/test
%exclude %{gem_cache}

%files doc
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/LICENSE

%changelog
* Tue Dec 20 2016 Justin Sherrill <jsherril@redhat.com> 0.1.0-1
- Update foreman_pipeline to 0.1.0 (oprazak@redhat.com)

* Mon May 09 2016 Eric D Helms <ericdhelms@gmail.com> 0.0.11-1
- Update foreman_pipeline to 0.0.11 (#214) (xprazak2@users.noreply.github.com)

* Thu Dec 17 2015 Eric D. Helms <ericdhelms@gmail.com> 0.0.8-2
- 

* Thu Dec 17 2015 Eric D. Helms <ericdhelms@gmail.com> 0.0.8-1
- new package built with tito

* Thu Nov 12 2015 Ondrej Prazak <oprazak@redhat.com> 0.0.8-1
- initial build
