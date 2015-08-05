%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}

%define gem_name mysql2

%define version 0.3.19

Summary: A simple, fast Mysql library for Ruby, binding to libmysql
Name: %{?scl_prefix}rubygem-%{gem_name}

Version: %{version}
Release: 1%{?dist}
Group: Development/Ruby
License: MIT
URL: http://mysql-win.rubyforge.org
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix}ruby >= 1.8.6
Requires: %{?scl_prefix}rubygems >= 1.8.10

BuildRequires: %{?scl_prefix}ruby >= 1.8.6
BuildRequires: %{?scl_prefix}rubygems >= 1.8.10
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}ruby-devel
BuildRequires: mysql-devel

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}


%define gem_builddir %{buildroot}%{gem_dir}

%description
This is the MySQL API module for Ruby. It provides the same functions for Ruby
programs that the MySQL C API provides for C programs.
This is a conversion of tmtm's original extension into a proper RubyGems.

%package doc
Summary: Documentation for rubygem-%{gem_name}
Group: Documentation
Requires: %{?scl_prefix}rubygem-%{gem_name} = %{version}-%{release}
BuildArch: noarch

%description doc
This package contains documentation for rubygem-%{gem_name}.


%prep
%setup -T -c -q

%build
%{__rm} -rf %{buildroot}
mkdir -p ./%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir ./%{gem_dir} -V --force %{SOURCE0}
%{?scl:"}


%install
%{__rm} -rf %{buildroot}
mkdir -p %{gem_builddir}
cp -a ./%{gem_dir}/* %{buildroot}/%{gem_dir}
rm -rf %{gem_builddir}/gems/%{gem_name}-%{version}/ext/%{gem_name}/%{gem_name}.so

# ruby 2.0.0 mkmf issue, fixed by r40280
rm -rf %{gem_builddir}/gems/%{gem_name}-%{version}/ext/%{gem_name}/.RUBYARCHDIR.time
# rubygems 2.0.3 stray temp file issue, PR #587
rm -rf %{gem_builddir}/gems/%{gem_name}-%{version}/ext/%{gem_name}/siteconf*.rb

# remove non-stripped object files
find %{buildroot} -type f -name *.o -exec rm -f {} +

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%doc %{gem_instdir}/LICENSE
%{gem_instdir}/ext/mysql2
%{gem_libdir}
%{gem_instdir}/support
%exclude %{gem_cache}
%{gem_spec}

%files doc
%{gem_docdir}
%{gem_instdir}/README.md
%{gem_instdir}/examples
%{gem_instdir}/spec

%changelog
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
