%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name katello
# %%global prever .rc1
%global mainver 3.7.0
%global release 1.nightly

Name:    %{?scl_prefix}rubygem-%{gem_name}
Summary: Katello

Version: %{mainver}
Release: %{?prever:0.}%{release}%{?prever}%{?dist}
Group:   Development/Ruby
License: GPLv2
URL:     https://theforeman.org/plugins/katello
Source0: https://rubygems.org/downloads/%{gem_name}-%{version}%{?prever}.gem

Requires: katello-selinux
Requires: foreman >= 1.17.0
Requires: foreman-postgresql
Requires: %{?scl_prefix}rubygem(angular-rails-templates) >= 0.0.4
Requires: %{?scl_prefix}rubygem(bastion) >= 6.1.2
Requires: %{?scl_prefix}rubygem(bastion) < 7.0.0
Requires: %{?scl_prefix}rubygem(oauth)
Requires: %{?scl_prefix}rubygem(rest-client)
Requires: %{?scl_prefix}rubygem(rabl)
Requires: %{?scl_prefix}rubygem(foreman_docker) >= 0.2.0
Requires: %{?scl_prefix}rubygem(foreman-tasks) >= 0.12.2
Requires: %{?scl_prefix}rubygem(foreman-tasks) < 1.0.0
Requires: %{?scl_prefix}rubygem(gettext_i18n_rails)
Requires: %{?scl_prefix}rubygem(apipie-rails) >= 0.1.1
Requires: %{?scl_prefix}rubygem(runcible) >= 2.0.0
Requires: %{?scl_prefix}rubygem(anemone)
Requires: %{?scl_prefix}rubygem(deface) >= 1.0.0
Requires: %{?scl_prefix}rubygem(deface) < 2.0.0
Requires: %{?scl_prefix}rubygem(qpid_messaging)
Requires: %{?scl_prefix_ruby}rubygem(json)
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)

BuildRequires: foreman-assets
BuildRequires: foreman-plugin >= 1.17.0
BuildRequires: %{?scl_prefix}rubygem(foreman_docker) >= 0.2.0
BuildRequires: %{?scl_prefix}rubygem(angular-rails-templates) >= 0.0.4
BuildRequires: %{?scl_prefix}rubygem(bastion) >= 6.1.2
BuildRequires: %{?scl_prefix}rubygem(bastion) < 7.0.0
BuildRequires: %{?scl_prefix}rubygem(foreman-tasks) >= 0.12.2
BuildRequires: %{?scl_prefix}rubygem(foreman-tasks) < 1.0.0
BuildRequires: %{?scl_prefix}rubygem(gettext_i18n_rails)
BuildRequires: %{?scl_prefix}rubygem(apipie-rails) >= 0.1.1
BuildRequires: %{?scl_prefix}rubygem(runcible) >= 2.0.0
BuildRequires: %{?scl_prefix}rubygem(anemone)
BuildRequires: %{?scl_prefix}rubygem(deface) >= 1.0.0
BuildRequires: %{?scl_prefix}rubygem(deface) < 2.0.0
BuildRequires: %{?scl_prefix}rubygem(qpid_messaging)
BuildRequires: %{?scl_prefix_ror}rubygem(rails)
BuildRequires: %{?scl_prefix_ruby}rubygem(json)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}ruby(release)

Obsoletes: %{?scl_prefix}rubygem-%{gem_name}_ostree

BuildArch: noarch
Provides: %{?scl_prefix}rubygem(katello) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Katello

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Summary:    Documentation for rubygem-%{gem_name}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}

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

%foreman_bundlerd_file
%foreman_precompile_plugin -s -a

%files
%dir %{gem_instdir}/
%{gem_libdir}
%{gem_instdir}/app
%{gem_instdir}/config
%{gem_instdir}/db
%{gem_instdir}/locale
%{gem_instdir}/engines
%{gem_instdir}/ca
%{gem_instdir}/vendor
%{gem_spec}
%{foreman_bundlerd_plugin}
%{foreman_apipie_cache_foreman}
%{foreman_apipie_cache_plugin}
%{foreman_assets_plugin}
%{gem_instdir}/public/assets/bastion_katello

%exclude %{gem_cache}
%exclude %{gem_instdir}/package.json
%exclude %{gem_instdir}/webpack

%license %{gem_instdir}/LICENSE.txt

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
