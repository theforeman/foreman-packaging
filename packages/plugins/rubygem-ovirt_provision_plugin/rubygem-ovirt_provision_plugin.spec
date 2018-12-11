# This package contains macros that provide functionality relating to
# Software Collections. These macros are not used in default
# Fedora builds, and should not be blindly copied or enabled.
# Specifically, the "scl" macro must not be defined in official Fedora
# builds. For more information, see:
# http://docs.fedoraproject.org/en-US/Fedora_Contributor_Documentation
# /1/html/Software_Collections_Guide/index.html

%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name ovirt_provision_plugin

%global foreman_dir /usr/share/foreman
%global foreman_bundlerd_dir %{foreman_dir}/bundler.d
%global foreman_pluginconf_dir %{foreman_dir}/config/settings.plugins.d

Summary:    Foreman plugin to provision new hosts and integrate to oVirt Engine
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    2.0.2
Release:    1%{?foremandist}%{?dist}
Group:      Applications/System
License:    GPLv3
URL:        https://github.com/theforeman/ovirt_provision_plugin
Source0:    https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires:   foreman >= 1.11.0
Requires:   %{?scl_prefix}rubygem(deface)

Requires:   %{?scl_prefix_ruby}ruby(release)
Requires:   %{?scl_prefix_ruby}rubygems

BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems

BuildArch: noarch

Requires: %{?scl_prefix}rubygem(rbovirt) >= 0.0.27

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-ovirt-provision
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
This plugin monitors oVirt provision for new host and perform related API calls
to ovirt-engine.

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

%files
%dir %{gem_instdir}
%{gem_instdir}/app
%{gem_instdir}/config
%{gem_instdir}/lib
%exclude %{gem_cache}
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/test
%{gem_spec}
%{foreman_bundlerd_dir}/%{gem_name}.rb
%doc %{gem_instdir}/LICENSE

%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.md

%changelog
* Wed Dec 12 2018 Moti Asayag <masayag@redhat.com> 2.0.2-1
- Update to 2.0.2

* Tue Jan 09 2018 Eric D. Helms <ericdhelms@gmail.com> 1.0.2-2
- Bump releases for base foreman plugins packages (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Mon Jun 27 2016 Dominic Cleal <dominic@cleal.org> 1.0.2-1
- re-add ovirt_provision_plugin (kvedulv@kvedulv.de)

* Thu Dec 24 2015 Dominic Cleal <dcleal@redhat.com> 1.0.1-3
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)
- More foremandist macros (dcleal@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 1.0.1-2
- Converted to tfm SCL (dcleal@redhat.com)

* Mon Dec 01 2014 Dominic Cleal <dcleal@redhat.com> 1.0.1-1
- Update ovirt_provision_plugin to 1.0.1 (ybronhei@redhat.com)

* Thu Nov 06 2014 Dominic Cleal <dcleal@redhat.com> 1.0.0-1
- Update ovirt_provision_plugin to 1.0.0 (ybronhei@redhat.com)

* Fri Jun 27 2014 Dominic Cleal <dcleal@redhat.com> 0.0.1-1
- new package built with tito
