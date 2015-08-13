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

%define rubyabi 1.9.1

Summary:    Plugin for Salt integration with Foreman
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    3.0.1
Release:    1%{?foremandist}%{?dist}
Group:      Applications/System
License:    GPLv3
URL:        http://github.com/theforeman/foreman_salt
Source0:    http://rubygems.org/downloads/%{gem_name}-%{version}.gem

Requires:   foreman >= 1.9.0
Requires:   %{?scl_prefix}rubygem(deface)

%if 0%{?fedora} > 18
Requires: %{?scl_prefix}ruby(release)
%else
Requires: %{?scl_prefix}ruby(abi) >= %{rubyabi}
%endif
Requires: %{?scl_prefix}rubygems
Requires: %{?scl_prefix}rubygem-foreman-tasks >= 0.7.1
Requires: %{?scl_prefix}rubygem-foreman-tasks < 0.8.0

%if 0%{?fedora} > 18
BuildRequires: %{?scl_prefix}ruby(release)
%else
BuildRequires: %{?scl_prefix}ruby(abi) >= %{rubyabi}
%endif
BuildRequires: foreman-plugin >= 1.8.0
BuildRequires: foreman-assets
BuildRequires: %{?scl_prefix}rubygem(deface)
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygems
BuildRequires: %{?scl_prefix}rubygem-foreman-tasks >= 0.7.1
BuildRequires: %{?scl_prefix}rubygem-foreman-tasks < 0.8.0

BuildArch: noarch

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-salt

%description
Foreman extensions that provide Salt support

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
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile

%changelog
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
