# This package contains macros that provide functionality relating to
# Software Collections. These macros are not used in default
# Fedora builds, and should not be blindly copied or enabled.
# Specifically, the "scl" macro must not be defined in official Fedora
# builds. For more information, see:
# http://docs.fedoraproject.org/en-US/Fedora_Contributor_Documentation
# /1/html/Software_Collections_Guide/index.html

%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_dhcp_browser

%global foreman_dir /usr/share/foreman
%global foreman_bundlerd_dir %{foreman_dir}/bundler.d

Summary:    DHCP browser plugin for Foreman
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    0.0.7
Release:    3%{?foremandist}%{?dist}
Group:      Applications/System
License:    GPLv3
URL:        http://github.com/theforeman/foreman_dhcp_browser
Source0:    http://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires:   foreman >= 1.2.0

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}rubygems

Requires: %{?scl_prefix}rubygem(deface) < 2.0.0

BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems

BuildArch: noarch

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-dhcp-browser
Provides: foreman-plugin-dhcp_browser
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Plugin for Foreman to browse and add/edit/delete DHCP leases independent of
Foreman's host creation.

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
%doc %{gem_instdir}/LICENSE
%exclude %{gem_cache}
%{gem_spec}
%{foreman_bundlerd_dir}/%{gem_name}.rb

%exclude %{gem_instdir}/Rakefile
%exclude %{gem_dir}/cache/%{gem_name}-%{version}.gem

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.md

%changelog
* Thu Dec 24 2015 Dominic Cleal <dcleal@redhat.com> 0.0.7-3
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)
- Add foremandist to more plugins (dcleal@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 0.0.7-2
- Converted to tfm SCL (dcleal@redhat.com)

* Thu Aug 20 2015 Dominic Cleal <dcleal@redhat.com> 0.0.7-1
- update foreman_dhcp_browser to 0.0.7 (kvedulv@kvedulv.de)

* Mon Oct 20 2014 Dominic Cleal <dcleal@redhat.com> 0.0.6-1
- update foreman_dhcp_browser to 0.0.6 (kvedulv@kvedulv.de)

* Mon Jul 21 2014 Dominic Cleal <dcleal@redhat.com> 0.0.5-1
- Update to v0.0.5 (dcleal@redhat.com)

* Tue Feb 04 2014 Dominic Cleal <dcleal@redhat.com> 0.0.4-1
- Update to v0.0.4 (dcleal@redhat.com)

* Tue Dec 10 2013 Dominic Cleal <dcleal@redhat.com> 0.0.3-1
- new package built with tito
