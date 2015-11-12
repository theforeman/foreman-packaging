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

%define rubyabi 1.9.1

Summary:    A Foreman plugin that cooperates with Jenkins
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    0.0.1
Release:    1%{?foremandist}%{?dist}
Group:      Applications/System
License:    GPLv3
URL:        http://github.com/theforeman/foreman_pipeline
Source0:    http://rubygems.org/downloads/%{gem_name}-%{version}.gem

Requires:   %{?scl_prefix}rubygem(jenkins_api_client) < 2.0.0
Requires:   %{?scl_prefix}rubygem(foreman_deployments) < 1.0.0
Requires:   %{?scl_prefix}rubygem(net-ssh) <= 2.9.2
Requires:   %{?scl_prefix}rubygem(net-scp)
Requires:   %{?scl_prefix}rubygem(bastion) < 3.0.0

BuildRequires: foreman-plugin >= 1.8.0
BuildRequires: %{?scl_prefix}rubygem(jenkins_api_client) < 2.0.0
BuildRequires: %{?scl_prefix}rubygem(foreman_deployments) < 1.0.0
BuildRequires: %{?scl_prefix}rubygem(net-ssh) <= 2.9.2
BuildRequires: %{?scl_prefix}rubygem(net-scp)
BuildRequires: %{?scl_prefix}rubygem(bastion) < 3.0.0

%if 0%{?fedora} > 18
Requires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
%else
Requires: %{?scl_prefix_ruby}ruby(abi) >= %{rubyabi}
BuildRequires: %{?scl_prefix_ruby}ruby(abi) >= %{rubyabi}
%endif

Requires: %{?scl_prefix_ruby}rubygems
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems
BuildRequires: foreman-assets

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
%foreman_precompile_plugin -a -s

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
%{foreman_assets_plugin}
%doc %{gem_instdir}/LICENSE

%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/test
%exclude %{gem_cache}

%files doc
%doc %{gem_instdir}/README.md

%posttrans
# We need to run the db:migrate after the install transaction
%foreman_db_migrate
%foreman_db_seed
%foreman_apipie_cache
%foreman_restart
exit 0

%changelog
* Thu Nov 12 2015 Ondrej Prazak <oprazak@redhat.com> 0.0.1-1
- initial build
