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
Version:    2.0.3
Release:    2%{?foremandist}%{?dist}
Group:      Applications/System
License:    GPLv3
URL:        https://github.com/theforeman/foreman_cockpit
Source0:    https://rubygems.org/gems/%{gem_name}-%{version}.gem

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
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

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
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%posttrans
%foreman_restart
exit 0

%changelog
* Wed Jun 07 2017 Dominic Cleal <dominic@cleal.org> 2.0.3-1
- Updated foreman_cockpit to 2.0.3 (me@daniellobato.me)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Thu Aug 04 2016 Dominic Cleal <dominic@cleal.org> 2.0.2-1
- Updated foreman_cockpit to 2.0.2 (elobatocs@gmail.com)

* Mon Apr 11 2016 Dominic Cleal <dominic@cleal.org> 2.0.1-1
- plugins:foreman_cockpit - Release 2.0.1 (elobatocs@gmail.com)

* Thu Dec 24 2015 Dominic Cleal <dcleal@redhat.com> 1.0.3-2
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Thu Nov 05 2015 Dominic Cleal <dcleal@redhat.com> 1.0.3-1
- plugins:foreman_cockpit - Release 1.0.3 (elobatocs@gmail.com)

* Thu Oct 29 2015 Dominic Cleal <dcleal@redhat.com> 1.0.2-2
- Obsolete ruby193 package variant (dcleal@redhat.com)

* Tue Oct 27 2015 Dominic Cleal <dcleal@redhat.com> 1.0.2-1
- new package built with tito

