# This package contains macros that provide functionality relating to
# Software Collections. These macros are not used in default
# Fedora builds, and should not be blindly copied or enabled.
# Specifically, the "scl" macro must not be defined in official Fedora
# builds. For more information, see:
# http://docs.fedoraproject.org/en-US/Fedora_Contributor_Documentation
# /1/html/Software_Collections_Guide/index.html

%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_discovery

%global mainver 4.1.0
#global prever .rc2
%global release 1
%{?prever:
%global gem_instdir %{gem_dir}/gems/%{gem_name}-%{mainver}%{?prever}
%global gem_docdir %{gem_dir}/doc/%{gem_name}-%{mainver}%{?prever}
%global gem_cache %{gem_dir}/cache/%{gem_name}-%{mainver}%{?prever}.gem
%global gem_spec %{gem_dir}/specifications/%{gem_name}-%{mainver}%{?prever}.gemspec
}

%define rubyabi 1.9.1
%global foreman_dir /usr/share/foreman
%global foreman_bundlerd_dir %{foreman_dir}/bundler.d

Summary:    MaaS Discovery Plugin for Foreman
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    %{mainver}
Release:    %{?prever:0.}%{release}%{?prever}%{?foremandist}%{?dist}
Group:      Applications/System
License:    GPLv3
URL:        http://github.com/theforeman/foreman_discovery
Source0:    http://rubygems.org/downloads/%{gem_name}-%{version}%{?prever}.gem

Requires:   foreman >= 1.9.0
Requires:   %{?scl_prefix}rubygem(deface) < 2.0

%if 0%{?fedora} > 18
Requires: %{?scl_prefix_ruby}ruby(release)
%else
Requires: %{?scl_prefix_ruby}ruby(abi) >= %{rubyabi}
%endif
Requires: %{?scl_prefix_ruby}rubygems

%if 0%{?fedora} > 18
BuildRequires: %{?scl_prefix_ruby}ruby(release)
%else
BuildRequires: %{?scl_prefix_ruby}ruby(abi) >= %{rubyabi}
%endif
BuildRequires: foreman-plugin >= 1.9.0
BuildRequires: %{?scl_prefix}rubygem(deface) < 2.0
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems

BuildArch: noarch

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-discovery
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
MaaS Discovery Plugin engine for Foreman.

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
%foreman_precompile_plugin -a

%files
%dir %{gem_instdir}
%{gem_instdir}/app
%{gem_instdir}/lib
%{gem_instdir}/config
%{gem_instdir}/db
%exclude %{gem_instdir}/extra
%{gem_instdir}/locale
%{gem_instdir}/public
%exclude %{gem_cache}
%{gem_spec}
%{foreman_bundlerd_dir}/%{gem_name}.rb
%doc %{gem_instdir}/LICENSE
%foreman_apipie_cache_foreman

%exclude %{gem_instdir}/test
%exclude %{gem_dir}/cache/%{gem_name}-%{version}%{?prever}.gem

%files doc
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.md

%posttrans
# We need to run the db:migrate after the install transaction
/usr/sbin/foreman-rake db:migrate  >/dev/null 2>&1 || :
/usr/sbin/foreman-rake db:seed  >/dev/null 2>&1 || :
%{foreman_apipie_cache}
(/sbin/service foreman status && /sbin/service foreman restart) >/dev/null 2>&1
exit 0

%changelog
* Thu Aug 27 2015 Dominic Cleal <dcleal@redhat.com> 4.0.0-2
- Converted to tfm SCL (dcleal@redhat.com)
- Fix BRs to match runtime requirements (dcleal@redhat.com)

* Thu Aug 13 2015 Dominic Cleal <dcleal@redhat.com> 4.0.0-1
- Updated foreman_discovery to 4.0.0 (lzap+git@redhat.com)
- Better branched builds with Foreman version macro (dcleal@redhat.com)

* Tue Mar 10 2015 Dominic Cleal <dcleal@redhat.com> 3.0.0-1
- Version 3.0.0 for Foreman 1.8 (lzap+git@redhat.com)
- Refs #4478 - prebuild apipie cache for rubygem-foreman_discovery
  (martin.bacovsky@gmail.com)

* Mon Feb 09 2015 Dominic Cleal <dcleal@redhat.com> 2.0.0-1
- Version bump to discovery 2.0.0 (lzap+git@redhat.com)

* Sun Feb 01 2015 Dominic Cleal <dcleal@redhat.com> 2.0.0-0.1.rc2
- Update foreman_discovery to 2.0.0.rc2 (lzap+git@redhat.com)

* Tue Jan 20 2015 Lukas Zapletal <lzap+rpm@redhat.com> - 2.0.0-0.1.rc1
- Dropped extra/ directory and TCL building dependencies
- Update to foreman_discovery 2.0.0.rc1

* Tue Nov 25 2014 Lukas Zapletal <lzap+rpm@redhat.com> - 1.4.1-1
- Update to foreman_discovery 1.4.1

* Thu Oct 30 2014 Lukas Zapletal <lzap+git@redhat.com> 1.4.0-2
- Update to foreman_discovery 1.4.0-2

* Thu Oct 30 2014 Lukas Zapletal <lzap+git@redhat.com> 1.4.0-1
- Updated foreman_discovery to 1.4.0 (lzap+git@redhat.com)

* Wed Oct 01 2014 Lukas Zapletal <lzap+git@redhat.com> 1.4.0-0.1.rc4
- Update rubygem-foreman_discovery to 1.4.0.rc4 (lzap+git@redhat.com)

* Wed Oct 01 2014 Lukas Zapletal <lzap+rpm@redhat.com> - 1.4.0-0.1.rc4
- Update foreman_discovery to 1.4.0.rc4

* Tue Sep 23 2014 Dominic Cleal <dcleal@redhat.com> 1.4.0-0.1.rc3
- Update foreman_discovery to 1.4.0.rc3 (dcleal@redhat.com)

* Mon Sep 22 2014 Dominic Cleal <dcleal@redhat.com> 1.4.0-0.1.rc2
- Update foreman_discovery to 1.4.0.rc2 (dcleal@redhat.com)

* Thu Aug 28 2014 Dominic Cleal <dcleal@redhat.com> 1.4.0-0.1.rc1
- Update foreman_discovery to 1.4.0.rc1 (dcleal@redhat.com)

* Fri Jun 06 2014 Lukas Zapletal <lzap+git@redhat.com> 1.3.0-1
- Updated foreman_discovery to 1.3.0 final version (lzap+git@redhat.com)

* Wed May 21 2014 Dominic Cleal <dcleal@redhat.com> 1.3.0-0.1.rc3
- Update foreman_discovery to 1.3.0.rc3 (dcleal@redhat.com)

* Fri Apr 18 2014 Lukas Zapletal <lzap+git@redhat.com> 1.3.0-0.1.rc2
- foreman_discovery-1.3.0.rc2 bump (lzap+git@redhat.com)
- Set minimum Foreman version of 1.5 (dcleal@redhat.com)

* Wed Apr 09 2014 Marek Hulan <mhulan@redhat.com> 1.3.0-0.1.rc1
- Update foreman discovery (mhulan@redhat.com)

* Wed Apr 02 2014 Dominic Cleal <dcleal@redhat.com> 1.2.0-1
- Update to 1.2.0 (dcleal@redhat.com)

* Fri Jan 24 2014 Lukas Zapletal <lzap+git@redhat.com> 1.2.0-0.1.rc2
- Bump foreman_discovery to 1.2.0.rc2 (lzap+git@redhat.com)
- Bump foreman_discovery to 1.2.0.rc1 (lzap+git@redhat.com)

* Sat Oct 19 2013 Dominic Cleal <dcleal@redhat.com> 1.1.1-1
- Update to 1.1.1 (dcleal@redhat.com)

* Fri Oct 18 2013 Dominic Cleal <dcleal@redhat.com> 1.1.0-1
- Update to 1.1.0 (dcleal@redhat.com)

* Thu Aug 22 2013 Dominic Cleal <dcleal@redhat.com> 1.0.2-7
- Create ~foreman/discovery_dir for image building (dcleal@redhat.com)
- Add patch for #2949, don't use bundler to find build_iso.sh
  (dcleal@redhat.com)
- Add dependencies and sudoers file for image building (dcleal@redhat.com)
- Remove SCL prefix from foreman-plugin-* provide (dcleal@redhat.com)

* Tue Aug 13 2013 Lukas Zapletal <lzap+git@redhat.com> 1.0.2-6
- adding SCL prefix to the provides statement (lzap+git@redhat.com)
- fixing dependency name (lzap+git@redhat.com)

* Tue Aug 13 2013 Lukas Zapletal <lzap+git@redhat.com> 1.0.2-5
- adding provides statement (lzap+git@redhat.com)

* Mon Aug 12 2013 Lukas Zapletal <lzap+git@redhat.com> 1.0.2-4
- adding missing source file (lzap+git@redhat.com)

* Mon Aug 12 2013 Lukas Zapletal <lzap+git@redhat.com> 1.0.2-3
- removing alpha tags (lzap+git@redhat.com)

* Thu Aug 01 2013 Lukas Zapletal <lzap+rpm[@]redhat.com> - 1.0.2-1
- bump to 1.0.2 release

* Wed Jun 26 2013 Dominic Cleal <dcleal@redhat.com> 1.0.0-0.1.rc4
- initial package build
