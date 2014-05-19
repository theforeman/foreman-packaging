# This package contains macros that provide functionality relating to
# Software Collections. These macros are not used in default
# Fedora builds, and should not be blindly copied or enabled.
# Specifically, the "scl" macro must not be defined in official Fedora
# builds. For more information, see:
# http://docs.fedoraproject.org/en-US/Fedora_Contributor_Documentation
# /1/html/Software_Collections_Guide/index.html
%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}

%{!?_pkgdocdir:%global _pkgdocdir %{_docdir}/%{name}}

%if 0%{?rhel} == 6 && 0%{!?scl:1}
%{!?gem_extdir_mri:%global gem_extdir_mri %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")}
%global gem_extdir_mri_lib %{gem_extdir_mri}
%else
%{!?gem_extdir_mri:%global gem_extdir_mri %{gem_extdir}}
%global gem_extdir_mri_lib %{gem_extdir_mri}/lib
%endif


%global gem_name rkerberos

Summary: A Ruby interface for the the Kerberos library
Name: %{?scl_prefix}rubygem-%{gem_name}

Version: 0.1.3
Release: 2%{?dist}
Group: Development/Languages
License: Artistic 2.0
URL: http://github.com/domcleal/rkerberos
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix}ruby
Requires: %{?scl_prefix}rubygems

BuildRequires: %{?scl_prefix}ruby
BuildRequires: %{?scl_prefix}rubygems
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}ruby-devel
BuildRequires: krb5-devel
#BuildRequires: %{?scl_prefix}rubygem-rake-compiler

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

#test
#BuildRequires: %{?scl_prefix}rubygem(test-unit)
#not yet in Fedora
#BuildRequires: %{?scl_prefix}rubygem(dbi-dbrc)

%description
The rkerberos library is an interface for the Kerberos 5 network
authentication protocol. It wraps the Kerberos C API.

%package doc
Summary: Documentation for rubygem-%{gem_name}
Group: Documentation
BuildArch: noarch

%description doc
This package contains documentation for rubygem-%{gem_name}.



%prep
%{?scl:scl enable %{scl} "}
gem unpack %{SOURCE0}
%{?scl:"}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} "}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:"}

%build
# Create the gem as gem install only works on a gem file
%{?scl:scl enable %{scl} "}
gem build %{gem_name}.gemspec
%{?scl:"}

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri_lib}
mv %{buildroot}%{gem_instdir}/lib/rkerberos.so %{buildroot}%{gem_extdir_mri_lib}

rm -rf %{buildroot}%{gem_dir}/gems/%{gem_name}-%{version}/{ext,tmp}
rm -rf %{buildroot}%{gem_dir}/gems/%{gem_name}-%{version}/.yardoc
rm -rf %{buildroot}%{gem_dir}/gems/%{gem_name}-%{version}/Gemfile*
# rake-compiler isn't needed on the system itself
sed -i '/rake-compiler/ s/runtime/development/' %{buildroot}/%{gem_spec}

mkdir -p %{buildroot}%{_pkgdocdir}
for docfile in LICENSE README.md CHANGES MANIFEST; do
     mv %{buildroot}%{gem_instdir}/$docfile %{buildroot}%{_pkgdocdir}
     ln -s %{_pkgdocdir}/$docfile %{buildroot}%{gem_instdir}
done

%check
pushd ./%{gem_instdir}
# test do not work and many of them need functional keytab
# this need some work in upstream first
#testrb -v -Ilib -Itest test/test_*.rb
popd

%files
%doc %{_pkgdocdir}/README.md
%doc %{gem_instdir}/README.md
%doc %{_pkgdocdir}/LICENSE
%doc %{gem_instdir}/LICENSE
%{gem_extdir_mri}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{_pkgdocdir}/README.md
%doc %{gem_instdir}/README.md
%doc %{_pkgdocdir}/LICENSE
%doc %{gem_instdir}/LICENSE

%doc %{_pkgdocdir}/CHANGES
%doc %{gem_instdir}/CHANGES
%doc %{_pkgdocdir}/MANIFEST
%doc %{gem_instdir}/MANIFEST
%doc %{gem_docdir}
%{gem_instdir}/rkerberos.gemspec
%{gem_instdir}/test
%{gem_instdir}/Rakefile


%changelog
* Mon Oct 21 2013 Miroslav Suchý <msuchy@redhat.com> 0.1.3-2
- 1001728 - remove deps of -doc subpackage on main package

* Sun Sep 08 2013 Miroslav Suchý <msuchy@redhat.com> 0.1.3-1
- rebase to 0.1.3 and move doc files to pkgdocdir
- 1001728 - use dist tag with question mark

* Tue Aug 27 2013 Miroslav Suchý <msuchy@redhat.com> 0.1.2-3
- fix files section

* Tue Aug 27 2013 Miroslav Suchý <msuchy@redhat.com> 0.1.2-2
- initial package

* Tue Jun 25 2013 Dominic Cleal <dcleal@redhat.com> 0.1.2-1
- Rebase to rkerberos 0.1.2 (dcleal@redhat.com)

* Thu May 23 2013 Dominic Cleal <dcleal@redhat.com> 0.1.1-4
- Remove rubygems version requirement (dcleal@redhat.com)

* Wed May 22 2013 Dominic Cleal <dcleal@redhat.com> 0.1.1-3
- Support building in non-SCL Ruby (dcleal@redhat.com)

* Tue May 21 2013 Martin Bačovský <mbacovsk@redhat.com> 0.1.1-2
- new package built with tito
- added support for SCL


* Wed May 08 2013 Dominic Cleal <dcleal@redhat.com> 0.1.1-1
- Update to 0.1.1 release
- Remove patch 103cea7d

* Wed May 08 2013 Dominic Cleal <dcleal@redhat.com> 0.1.0-1
- Initial 0.1.0 release
- Add patch 103cea7d (Add credential cache argument to get_init_creds_keytab)

