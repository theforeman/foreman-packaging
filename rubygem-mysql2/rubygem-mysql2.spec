%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}

%define gem_name mysql2

%define version 0.4.5

%if 0%{?scl:1}
%{!?gem_extdir_mri:%global gem_extdir_mri %{gem_extdir}}
%global gem_extdir_mri_lib %{gem_extdir_mri}
%else
%if 0%{?el6}
%{!?gem_extdir_mri:%global gem_extdir_mri %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")}
%global gem_extdir_mri_lib %{gem_extdir_mri}
%else # el7
%{!?gem_extdir_mri:%global gem_extdir_mri %{gem_extdir}}
%global gem_extdir_mri_lib %{gem_extdir_mri}/lib
%endif
%endif

Summary: A simple, fast Mysql library for Ruby, binding to libmysql
Name: %{?scl_prefix}rubygem-%{gem_name}

Version: %{version}
Release: 2%{?dist}
Group: Development/Ruby
License: MIT
URL: https://github.com/brianmario/mysql2
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}ruby >= 1.8.6
Requires: %{?scl_prefix_ruby}rubygems

BuildRequires: %{?scl_prefix_ruby}ruby >= 1.8.6
BuildRequires: %{?scl_prefix_ruby}rubygems
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby-devel
BuildRequires: mysql-devel

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}


%description
This is the MySQL API module for Ruby. It provides the same functions for Ruby
programs that the MySQL C API provides for C programs.
This is a conversion of tmtm's original extension into a proper RubyGems.

%package doc
Summary: Documentation for rubygem-%{gem_name}
Group: Documentation
Requires: %{?scl_prefix}rubygem-%{gem_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
BuildArch: noarch

%description doc
This package contains documentation for rubygem-%{gem_name}.


%prep
%{?scl:scl enable %{scl} - <<EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} - <<EOF}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:EOF}

%build
# Create the gem as gem install only works on a gem file
%{?scl:scl enable %{scl} - <<EOF}
gem build %{gem_name}.gemspec
%{?scl:EOF}

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%{?scl:scl enable %{scl} - <<EOF}
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

find .
mkdir -p %{buildroot}%{gem_extdir_mri_lib}/mysql2/

cp -a .%{gem_instdir}/ext/mysql2/mysql2.so %{buildroot}%{gem_extdir_mri_lib}/mysql2/
%{?scl:cp -a .%{gem_extdir_mri}/gem.build_complete %{buildroot}%{gem_extdir_mri_lib}/}

# Prevent dangling symlink in -debuginfo.
rm -rf %{buildroot}%{gem_instdir}/ext


# Remove some droppings
rm -f %{buildroot}%{gem_instdir}/{.gitignore,.rspec,.rvmrc,.travis.yml}
rm -rf %{buildroot}%{gem_instdir}/spec
rm -f %{buildroot}%{gem_libdir}/mysql2/*.so

%files
%defattr(-, root, root)
%doc %{gem_instdir}/LICENSE
%{gem_libdir}
%{?scl:%{gem_extdir_mri}/gem.build_complete}
%{gem_extdir_mri_lib}/mysql2
%exclude %{gem_cache}
%{gem_spec}
%exclude %{gem_instdir}/support

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/examples

%changelog
* Tue Oct 25 2016 Dominic Cleal <dominic@cleal.org> 0.4.5-1
- Update mysql2 to 0.4.5 (dominic@cleal.org)

* Thu Feb 04 2016 Dominic Cleal <dcleal@redhat.com> 0.3.19-5
- fix missing mysql2.so and gem.build_complete (#13296)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 0.3.19-4
- Rebuild for rh-ruby22 (dcleal@redhat.com)

* Tue Nov 10 2015 Dominic Cleal <dcleal@redhat.com> 0.3.19-3
- Remove version dependency on rubygems (ewoud@kohlvanwijngaarden.nl)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 0.3.19-2
- Converted to tfm SCL (dcleal@redhat.com)

* Wed Aug 05 2015 Dominic Cleal <dcleal@redhat.com> 0.3.19-1
- Update mysql2 to 0.3.19 (dcleal@redhat.com)

* Mon Jun 01 2015 Dominic Cleal <dcleal@redhat.com> 0.3.18-1
- Update mysql2 to 0.3.18 (dcleal@redhat.com)

* Wed Nov 27 2013 Lukas Zapletal <lzap+git@redhat.com> 0.3.11-4
- Removing extra object files from rubygem-mysql2 - fix (lzap+git@redhat.com)

* Wed Nov 27 2013 Lukas Zapletal <lzap+git@redhat.com> 0.3.11-3
- Removing extra object files from rubygem-mysql2 (lzap+git@redhat.com)

* Mon Jul 08 2013 Dominic Cleal <dcleal@redhat.com> 0.3.11-2
- Remove stray untracked files, ruby/rubygems bugs (dcleal@redhat.com)

* Thu Jun 20 2013 Dominic Cleal <dcleal@redhat.com> 0.3.11-1
- Rebase to mysql2 0.3.11 (dcleal@redhat.com)

* Thu Jun 06 2013 Dominic Cleal <dcleal@redhat.com> 0.2.18-5
- Provide mysql2, not mysql (dcleal@redhat.com)

* Tue Jun 04 2013 Dominic Cleal <dcleal@redhat.com> 0.2.18-4
- Add gem_spec to rubygem-mysql* to fix loading, exclude gem_cache
  (dcleal@redhat.com)

* Fri May 24 2013 Martin Bačovský <mbacovsk@redhat.com> 0.2.18-3
- new package built with tito
- added support for SCL


* Tue May 08 2012 jmontleo@redhat.com - 0.2.18-2
- Cleaned up spec file
