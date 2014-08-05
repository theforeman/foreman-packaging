# This package contains macros that provide functionality relating to
# Software Collections. These macros are not used in default
# Fedora builds, and should not be blindly copied or enabled.
# Specifically, the "scl" macro must not be defined in official Fedora
# builds. For more information, see:
# http://docs.fedoraproject.org/en-US/Fedora_Contributor_Documentation
# /1/html/Software_Collections_Guide/index.html

%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_bootdisk

%define rubyabi 1.9.1
%global foreman_dir /usr/share/foreman
%global foreman_bundlerd_dir %{foreman_dir}/bundler.d
%global foreman_pluginconf_dir %{foreman_dir}/config/settings.plugins.d

Summary:    Create boot disks to provision hosts with Foreman
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    3.0.0
Release:    1%{?dist}
Group:      Applications/System
License:    GPLv3
URL:        http://github.com/theforeman/foreman_bootdisk
Source0:    http://rubygems.org/downloads/%{gem_name}-%{version}.gem

Requires:   foreman >= 1.6.0
Requires:   ipxe-bootimgs
Requires:   /usr/bin/isohybrid
Requires:   /usr/bin/genisoimage

%if 0%{?fedora} > 18
Requires: %{?scl_prefix}ruby(release)
%else
Requires: %{?scl_prefix}ruby(abi) >= %{rubyabi}
%endif
Requires: %{?scl_prefix}rubygems

%if 0%{?fedora} > 18
BuildRequires: %{?scl_prefix}ruby(release)
%else
BuildRequires: %{?scl_prefix}ruby(abi) >= %{rubyabi}
%endif
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygems

BuildArch: noarch

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-bootdisk

%description
Plugin for Foreman that creates iPXE-based boot disks to provision hosts
without the need for PXE infrastructure.

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
%{gem_instdir}/locale
%exclude %{gem_cache}
%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/Rakefile
%{gem_spec}
%{foreman_bundlerd_dir}/%{gem_name}.rb
%doc %{gem_instdir}/LICENSE

%exclude %{gem_dir}/cache/%{gem_name}-%{version}.gem

%files doc
%doc %{gem_instdir}/CHANGES.md
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.md

%posttrans
# We need to run the db:migrate after the install transaction
/usr/sbin/foreman-rake db:migrate  >/dev/null 2>&1 || :
/usr/sbin/foreman-rake db:seed  >/dev/null 2>&1 || :
(/sbin/service foreman status && /sbin/service foreman restart) >/dev/null 2>&1
exit 0

%changelog
* Tue Aug 05 2014 Dominic Cleal <dcleal@redhat.com> 3.0.0-1
- Update to foreman_bootdisk 3.0.0 (dcleal@redhat.com)

* Thu May 29 2014 Dominic Cleal <dcleal@redhat.com> 2.0.8-1
- Update to foreman_bootdisk 2.0.8 (dcleal@redhat.com)

* Fri May 23 2014 Dominic Cleal <dcleal@redhat.com> 2.0.7-1
- Update to foreman_bootdisk 2.0.7 (dcleal@redhat.com)

* Fri May 16 2014 Dominic Cleal <dcleal@redhat.com> 2.0.6-1
- Update to foreman_bootdisk 2.0.6 (dcleal@redhat.com)

* Tue May 06 2014 Dominic Cleal <dcleal@redhat.com> 2.0.5-1
- Update to foreman_bootdisk 2.0.5 (dcleal@redhat.com)

* Wed Apr 09 2014 Dominic Cleal <dcleal@redhat.com> 2.0.4-1
- Update to foreman_bootdisk 2.0.4 (dcleal@redhat.com)

* Thu Mar 27 2014 Dominic Cleal <dcleal@redhat.com> 2.0.3-1
- Update to foreman_bootdisk 2.0.3 (dcleal@redhat.com)

* Thu Feb 13 2014 Dominic Cleal <dcleal@redhat.com> 2.0.2-1
- Update to foreman_bootdisk 2.0.2 (dcleal@redhat.com)

* Thu Feb 13 2014 Dominic Cleal <dcleal@redhat.com> 2.0.1-1
- Update to foreman_bootdisk 2.0.1 (dcleal@redhat.com)

* Wed Jan 22 2014 Dominic Cleal <dcleal@redhat.com> 2.0.0-1
- Update to foreman_bootdisk 2.0.0 (dcleal@redhat.com)

* Fri Nov 01 2013 Dominic Cleal <dcleal@redhat.com> 1.2.3-2
- Update to foreman_bootdisk 1.2.3 (dcleal@redhat.com)

* Tue Oct 15 2013 Dominic Cleal <dcleal@redhat.com> 1.2.2-2
- Add isohybrid and mkisofs dependencies (dcleal@redhat.com)

* Mon Oct 07 2013 Dominic Cleal <dcleal@redhat.com> 1.2.2-1
- Update to foreman_bootdisk 1.2.2 (dcleal@redhat.com)

* Tue Sep 24 2013 Dominic Cleal <dcleal@redhat.com> 1.2.1-1
- Update to foreman_bootdisk 1.2.1 (dcleal@redhat.com)

* Tue Sep 17 2013 Dominic Cleal <dcleal@redhat.com> 1.2.0-1
- new package built with tito

