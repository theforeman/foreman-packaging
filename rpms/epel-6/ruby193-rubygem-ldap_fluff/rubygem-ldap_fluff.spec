%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name ldap_fluff

Summary: LDAP integration for Active Directory, Free IPA and posix  
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.1.3
Release: 3%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: https://github.com/jsomara/ldap_fluff
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}rubygems
Requires: %{?scl_prefix}rubygem(net-ldap)
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygem(rake)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Requires: %{?scl_prefix}ruby(abi) = 1.9.1

%description
Provides multiple implementations of LDAP queries for various backends.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%{?scl:scl enable %{scl} "}
gem unpack %{SOURCE0}
%{?scl:"}
%setup -q -D -T -n  %{gem_name}-%{version}
%{?scl:scl enable %{scl} "}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:"}

%build
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem build %{gem_name}.gemspec
%{?scl:"}
#rake ldap_fluff:gem

%{?scl:scl enable %{scl} "}
gem install -V \
        --local \
        --install-dir ./%{gem_dir} \
        --force \
        --rdoc \
        %{gem_name}-%{version}.gem
%{?scl:"}


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_sysconfdir}
cp -a ./%{_root_sysconfdir}/ldap_fluff.yml %{buildroot}%{_sysconfdir}/

rm -rf %{buildroot}%{gem_instdir}/{.yardoc,etc}

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%config(noreplace) %{_sysconfdir}/ldap_fluff.yml

%files doc
%doc %{gem_docdir}
%{gem_instdir}/test

%changelog
* Wed Feb 27 2013 Miroslav Suchý <msuchy@redhat.com> 0.1.3-3
- correct build directory in SC env

* Wed Feb 27 2013 Miroslav Suchý <msuchy@redhat.com> 0.1.3-2
- new package built with tito

* Thu Nov 01 2012 Miroslav Suchý <msuchy@redhat.com> 0.1.3-1
- update to ldap_fluff-0.1.3.gem and polish the spec (msuchy@redhat.com)

* Mon Jul 16 2012 Miroslav Suchý <msuchy@redhat.com> 0.1.1-2
- cleanup spec file (msuchy@redhat.com)

* Tue Jul 10 2012 Jordan OMara <jomara@redhat.com> 0.1.1-1
- new package built with tito

* Fri Jul 06 2012 Jordan OMara <jomara@redhat.com> 0.1.1-1
- A few minor IPA bugs (jomara@redhat.com)
- Adding .rvmrc; unit tests only support 1.9.3 (jomara@redhat.com)

* Fri Jul 06 2012 Jordan OMara <jomara@redhat.com> 0.1.0-1
- Adding the rest of free ipa support - testing, configuration
  (jomara@redhat.com)
- Adding FreeIPA support (jomara@redhat.com)
- Fix for empty set return for missing ldap user (jomara@redhat.com)
- Removing files that shouldnt have been committed (jomara@redhat.com)

* Fri Jun 29 2012 Jordan OMara <jomara@redhat.com> 0.0.6-1
- Adding some heavy recursive tests (jomara@redhat.com)
- Updating README to fix formatting (jsomara@gmail.com)
- Adding anon_queries to AD config; Fixing AD recursive group walk
  (jomara@redhat.com)
- Fixing a posix merge_filter bug. NEEDS SOME TESTS (jomara@redhat.com)
- Fixing a few minor bugs (jomara@redhat.com)

* Tue Jun 26 2012 Jordan OMara <jomara@redhat.com> 0.0.5-1
- Forgot to remove obsolete files from lib (jomara@redhat.com)

* Tue Jun 26 2012 Jordan OMara <jomara@redhat.com> 0.0.4-1
- rdoc/task -> rake/rdoctask for older rpm support (jomara@redhat.com)
- Updating readme (jomara@redhat.com)

* Tue Jun 26 2012 Jordan OMara <jomara@redhat.com> 0.0.3-1
- Automatic commit of package [rubygem-ldap_fluff] release [0.0.2-1].
  (jomara@redhat.com)

* Tue Jun 26 2012 Jordan OMara <jomara@redhat.com> 0.0.2-1
- new package built with tito

