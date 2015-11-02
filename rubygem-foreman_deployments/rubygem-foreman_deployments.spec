# This package contains macros that provide functionality relating to
# Software Collections. These macros are not used in default
# Fedora builds, and should not be blindly copied or enabled.
# Specifically, the "scl" macro must not be defined in official Fedora
# builds. For more information, see:
# http://docs.fedoraproject.org/en-US/Fedora_Contributor_Documentation/1/html/Software_Collections_Guide/index.html

%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_deployments

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.0.1
Release: 1%{?foremandist}%{?dist}
Summary: A plugin adding Multi-Host Deployment support into the Foreman
Group: Applications/System
License: GPLv3
URL: https://github.com/theforeman/foreman_deployments
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem

Requires: foreman >= 1.8.0
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}rubygems
Requires: %{?scl_prefix}rubygem(foreman-tasks) >= 0.7.3
Requires: %{?scl_prefix}rubygem(foreman-tasks) < 0.8.0
Requires: %{?scl_prefix}rubygem(safe_yaml) >= 1.0.0

BuildRequires: foreman-plugin >= 1.8.0
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems
BuildRequires: %{?scl_prefix}rubygem(foreman-tasks) >= 0.7.3
BuildRequires: %{?scl_prefix}rubygem(foreman-tasks) < 0.8.0
BuildRequires: %{?scl_prefix}rubygem(safe_yaml) >= 1.0.0

BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-deployments

%description
A plugin adding Foreman Multi-Host Deployment support.

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%{?scl:scl enable %{scl} "}
gem unpack %{SOURCE0}
%{?scl:"}

%setup -q -D -T -n  %{gem_name}-%{version}
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
%foreman_precompile_plugin -a

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_instdir}/app
%{gem_instdir}/db
%{gem_instdir}/config
%{gem_instdir}/locale
%exclude %{gem_cache}
%{gem_spec}
%{foreman_bundlerd_plugin}
%doc %{gem_instdir}/LICENSE
%{foreman_apipie_cache_foreman}
%{gem_instdir}/Rakefile

%exclude %{gem_instdir}/test
%exclude %{gem_instdir}/.*

%files doc
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/doc

%posttrans
# We need to run the db:migrate
%foreman_db_migrate
%foreman_db_seed
%foreman_apipie_cache
%foreman_restart
exit 0

%changelog
* Tue Nov 03 2015 Ondrej Prazak <oprazak@redhat.com> - 0.0.1-1
- Initial package
