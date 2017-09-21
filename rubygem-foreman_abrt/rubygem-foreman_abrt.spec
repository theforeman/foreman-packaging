# This package contains macros that provide functionality relating to
# Software Collections. These macros are not used in default
# Fedora builds, and should not be blindly copied or enabled.
# Specifically, the "scl" macro must not be defined in official Fedora
# builds. For more information, see:
# http://docs.fedoraproject.org/en-US/Fedora_Contributor_Documentation
# /1/html/Software_Collections_Guide/index.html

%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_abrt

%global foreman_dir /usr/share/foreman
%global foreman_bundlerd_dir %{foreman_dir}/bundler.d
%global foreman_pluginconf_dir %{foreman_dir}/config/settings.plugins.d

Summary:    Display reports from Automatic Bug Reporting Tool in Foreman
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    0.0.7
Release:    1%{?foremandist}%{?dist}
Group:      Applications/System
License:    GPLv3
URL:        https://github.com/theforeman/foreman_abrt
Source0:    https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires:   foreman >= 1.8.0

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}rubygems

BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems

BuildArch: noarch

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-abrt
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
This plugin allows you to see bug reports submitted by Automatic Bug Reporting
Tool.

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
%{gem_instdir}/db
%{gem_instdir}/lib
%exclude %{gem_cache}
%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/test
%{gem_spec}
%{foreman_bundlerd_dir}/%{gem_name}.rb
%doc %{gem_instdir}/LICENSE

%exclude %{gem_dir}/cache/%{gem_name}-%{version}.gem

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.md

%posttrans
# We need to run the db:migrate after the install transaction
/usr/sbin/foreman-rake db:migrate  >/dev/null 2>&1 || :
/usr/sbin/foreman-rake db:seed  >/dev/null 2>&1 || :
(/sbin/service foreman status && /sbin/service foreman restart) >/dev/null 2>&1
exit 0

%changelog
* Tue May 17 2016 Dominic Cleal <dominic@cleal.org> 0.0.7-1
- Updated foreman_abrt to 0.0.7 (lzap+git@redhat.com)

* Thu Dec 24 2015 Dominic Cleal <dcleal@redhat.com> 0.0.6-4
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)
- Add foremandist to more plugins (dcleal@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 0.0.6-3
- Converted to tfm SCL (dcleal@redhat.com)

* Mon Mar 23 2015 Dominic Cleal <dcleal@redhat.com> 0.0.6-2
- Remove unused apipie:cache call (dcleal@redhat.com)

* Thu Jan 15 2015 Martin Milata <mmilata@redhat.com> 0.0.6-1
- Update to foreman_abrt-0.0.6

* Fri Jan 09 2015 Martin Milata <mmilata@redhat.com> 0.0.5-1
- Update to foreman_abrt-0.0.5

* Fri Nov 14 2014 Martin Milata <mmilata@redhat.com> 0.0.4-1
- Update to foreman_abrt-0.0.4

* Tue Sep 30 2014 Martin Milata <mmilata@redhat.com> 0.0.3-1
- Update to foreman_abrt-0.0.3

* Tue Aug 26 2014 Martin Milata <mmilata@redhat.com> 0.0.2-1
- Update to foreman_abrt-0.0.2

* Mon Aug 11 2014 Martin Milata <mmilata@redhat.com> 0.0.1-1
- new package
