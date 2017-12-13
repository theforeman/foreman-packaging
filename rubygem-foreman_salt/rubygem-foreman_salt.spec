# This package contains macros that provide functionality relating to
# Software Collections. These macros are not used in default
# Fedora builds, and should not be blindly copied or enabled.
# Specifically, the "scl" macro must not be defined in official Fedora
# builds. For more information, see:
# http://docs.fedoraproject.org/en-US/Fedora_Contributor_Documentation
# /1/html/Software_Collections_Guide/index.html

%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_salt

Summary:    Plugin for Salt integration with Foreman
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    9.0.0
Release:    1%{?foremandist}%{?dist}
Group:      Applications/System
License:    GPLv3
URL:        http://github.com/theforeman/foreman_salt
Source0:    http://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires:   foreman >= 1.14.0
Requires:   %{?scl_prefix}rubygem(deface)

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}rubygems
Requires: %{?scl_prefix}rubygem-foreman-tasks >= 0.8.0
Requires: %{?scl_prefix}rubygem-foreman-tasks < 1.0.0

BuildRequires: foreman-plugin >= 1.14.0
BuildRequires: foreman-assets
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems
BuildRequires: %{?scl_prefix}rubygem(deface)
BuildRequires: %{?scl_prefix}rubygem-foreman-tasks >= 0.8.0
BuildRequires: %{?scl_prefix}rubygem-foreman-tasks < 1.0.0

BuildArch: noarch

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-salt
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Foreman extensions that provide Salt support

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
%foreman_precompile_plugin -a -s

%posttrans
# We need to run the db:migrate after the install transaction
/usr/sbin/foreman-rake db:migrate  >/dev/null 2>&1 || :
/usr/sbin/foreman-rake db:seed  >/dev/null 2>&1 || :
%{foreman_apipie_cache}
(/sbin/service foreman status && /sbin/service foreman restart) >/dev/null 2>&1
exit 0

%files
%dir %{gem_instdir}
%{gem_instdir}/app
%{gem_instdir}/db
%{gem_instdir}/lib
%{gem_instdir}/config
%{gem_instdir}/public
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/LICENSE
%{foreman_bundlerd_plugin}
%foreman_apipie_cache_foreman
%{foreman_apipie_cache_plugin}
%{foreman_assets_plugin}

%exclude %{gem_instdir}/test
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile

%changelog
* Thu Mar 30 2017 Dominic Cleal <dominic@cleal.org> 8.0.2-1
- update foreman_salt to 8.0.2 (kvedulv@kvedulv.de)

* Mon Mar 13 2017 Eric D Helms <ericdhelms@gmail.com> 8.0.1-1
- update foreman_salt to 8.0.1 (kvedulv@kvedulv.de)
- Switch to using gem_install macro (ericdhelms@gmail.com)

* Wed Nov 23 2016 Dominic Cleal <dominic@cleal.org> 8.0.0-1
- update foreman_salt to 8.0.0 (kvedulv@kvedulv.de)

* Tue Nov 22 2016 Dominic Cleal <dominic@cleal.org> 7.0.1-1
- update foreman_salt to 7.0.1 (kvedulv@kvedulv.de)

* Mon Aug 22 2016 Dominic Cleal <dominic@cleal.org> 7.0.0-1
- Release foreman_salt 7.0.0 (stephen@redhat.com)

* Thu Jul 28 2016 Dominic Cleal <dominic@cleal.org> 6.0.0-1
- Release foreman_salt 6.0.0 (stephen@redhat.com)

* Tue May 31 2016 Dominic Cleal <dominic@cleal.org> 5.0.1-1
- update foreman_salt to 5.0.1 (kvedulv@kvedulv.de)

* Wed Jan 27 2016 Dominic Cleal <dcleal@redhat.com> 5.0.0-1
- Release foreman_salt 5.0.0 (stbenjam@redhat.com)
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Mon Oct 26 2015 Dominic Cleal <dcleal@redhat.com> 4.0.1-1
- Small foreman_salt update (stbenjam@redhat.com)

* Tue Oct 13 2015 Dominic Cleal <dcleal@redhat.com> 4.0.0-1
- Release foreman_salt 4.0.0 (RPM) (stbenjam@redhat.com)

* Thu Aug 27 2015 Dominic Cleal <dcleal@redhat.com> 3.0.2-1
- Release foreman_salt 3.0.2 (stbenjam@redhat.com)

* Thu Aug 27 2015 Dominic Cleal <dcleal@redhat.com> 3.0.1-2
- Converted to tfm SCL (dcleal@redhat.com)

* Thu Aug 13 2015 Stephen Benjamin <stephen@redhat.com> 3.0.1-1
- Update to 3.0.1

* Mon Jul 06 2015 Stephen Benjamin <stephen@redhat.com> 3.0.0-1
- Update to 3.0.0

* Sat May 09 2015 Stephen Benjamin <stephen@redhat.com> 2.1.0-1
- Update to 2.1.0

* Tue Mar 17 2015 Stephen Benjamin <stephen@redhat.com> 2.0.2-1
- Update to 2.0.2

* Tue Mar 03 2015 Stephen Benjamin <stephen@redhat.com> 2.0.1-1
- Update to 2.0.1

* Wed Jan 14 2015 Stephen Benjamin <stephen@redhat.com> 1.1.1-1
- Update to 1.1.1

* Tue Dec 30 2014 Michael Moll <mmoll@mmoll.at> 1.1.0-2
- Add dependency on rubygem-deface

* Wed Nov 19 2014 Stephen Benjamin <stephen@redhat.com> 1.1.0-1
- Update to 1.1.0

* Tue Nov 11 2014 Stephen Benjamin <stephen@redhat.com> 1.0.0-1
- Update to 1.0.0

* Wed Oct 08 2014 Stephen Benjamin <stephen@redhat.com> 0.0.4-1
- Update to 0.0.4

* Tue Oct 07 2014 Michael Moll <mmoll@mmoll.at> 0.0.3-1
- Update to 0.0.3

* Thu Aug 28 2014 Stephen Benjamin <stephen@redhat.com> 0.0.2-1
- Initial version
