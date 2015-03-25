# This package contains macros that provide functionality relating to
# Software Collections. These macros are not used in default
# Fedora builds, and should not be blindly copied or enabled.
# Specifically, the "scl" macro must not be defined in official Fedora
# builds. For more information, see:
# http://docs.fedoraproject.org/en-US/Fedora_Contributor_Documentation/1/html/Software_Collections_Guide/index.html

%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_openscap

%define rubyabi 1.9.1
%global foreman_dir /usr/share/foreman
%global foreman_bundlerd_dir %{foreman_dir}/bundler.d

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.4.0
Release: 1%{?dist}
Summary: Foreman plug-in for displaying OpenSCAP audit reports
Group: Applications/System
License: GPLv3
URL: https://github.com/OpenSCAP/foreman_openscap
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem

Requires: foreman >= 1.5.0

Requires: %{?scl_prefix}rubygem(deface)
Requires: %{?scl_prefix}rubygem(scaptimony) >= 0.3.0
Requires: %{?scl_prefix}rubygem(scaptimony) < 0.4.0
%if 0%{?fedora} > 18
Requires: %{?scl_prefix}ruby(release)
Requires: %{?scl_prefix}ruby(rubygems)
BuildRequires: %{?scl_prefix}ruby(release)
%else
Requires: %{?scl_prefix}ruby(abi) >= %{rubyabi}
Requires: %{?scl_prefix}rubygems
BuildRequires: %{?scl_prefix}ruby(abi) >= %{rubyabi}
%endif
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygems
BuildRequires: foreman-assets >= 1.7.0
BuildRequires: foreman-plugin >= 1.8.0
BuildRequires: %{?scl_prefix}rubygem(deface)
BuildRequires: %{?scl_prefix}rubygem(scaptimony) >= 0.3.0
BuildRequires: %{?scl_prefix}rubygem(scaptimony) < 0.4.0

BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-openscap

%description
Foreman plug-in for managing security compliance reports.


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

mkdir -p %{buildroot}%{foreman_bundlerd_dir}

%foreman_bundlerd_file
%foreman_precompile_plugin -s

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_instdir}/app
%{gem_instdir}/db
%{gem_instdir}/config
%exclude %{gem_cache}
%{gem_spec}
%{foreman_bundlerd_plugin}
%doc %{gem_instdir}/LICENSE
%{foreman_assets_plugin}

%exclude %{gem_instdir}/test

%files doc
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.md

%posttrans
# We need to run the db:migrate (because of SCAPtimony) after the install transaction
%foreman_db_migrate
/usr/sbin/foreman-rake db:seed  >/dev/null 2>&1 || :
/usr/sbin/foreman-rake apipie:cache  >/dev/null 2>&1 || :
%foreman_restart
exit 0

%changelog
* Wed Mar 25 2015 Šimon Lukašík <slukasik@redhat.com> - 0.4.0-1
- new upstream release

* Thu Mar 19 2015 Šimon Lukašík <slukasik@redhat.com> - 0.3.3-1
- new upstream release

* Mon Mar 02 2015 Šimon Lukašík <slukasik@redhat.com> - 0.3.2-1
- new upstream release
- fix FTBFS, missing foreman-plugins dep for build macros (dcleal@redhat.com)

* Thu Feb 12 2015 Šimon Lukašík <slukasik@redhat.com> - 0.3.1-1
- new upstream release

* Wed Jan 28 2015 Šimon Lukašík <slukasik@redhat.com> - 0.3.0-1
- new upstream release

* Fri Jan 23 2015 Marek Hulán <mhulan@redhat.com> - 0.2.1-1
- new upstream release

* Thu Dec 04 2014 Šimon Lukašík <slukasik@redhat.com> - 0.2.0-1
- new upstream release

* Thu Oct 23 2014 Šimon Lukašík <slukasik@redhat.com> - 0.1.0-1
- rebuilt

* Mon Jul 28 2014 Šimon Lukašík <slukasik@redhat.com> - 0.0.1-1
- Initial package
