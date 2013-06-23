%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}

%define gem_name mysql

%define version 2.8.1

Summary: This is the MySQL API module for Ruby
Name: %{?scl_prefix}rubygem-%{gem_name}

Version: %{version}
Release: 4%{?dist}
Group: Development/Ruby
License: Distributable
URL: http://mysql-win.rubyforge.org
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem
BuildRoot: %{_tmppath}/%{pkg_name}-%{version}-root

Requires: %{?scl_prefix}ruby >= 1.8.6
Requires: %{?scl_prefix}rubygems >= 1.8.10

BuildRequires: %{?scl_prefix}ruby >= 1.8.6
BuildRequires: %{?scl_prefix}rubygems >= 1.8.10
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}ruby-devel
BuildRequires: mysql-devel

Provides: %{?scl_prefix}rubygem(mysql) = %{version}


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
rm -rf %{gem_builddir}/gems/%{gem_name}-%{version}/ext/mysql_api/mysql_api.so
rm -rf %{buildroot}%{gem_dir}/gems/%{gem_name}-%{version}/.yardoc
rm -rf %{buildroot}%{gem_docdir}/rdoc/ext

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%{gem_instdir}/COPYING
%{gem_instdir}/COPYING.ja
%doc %{gem_instdir}/History.txt
%doc %{gem_instdir}/Manifest.txt
%doc %{gem_instdir}/README.txt
%{gem_instdir}/ext/mysql_api/extconf.rb
%{gem_instdir}/ext/mysql_api/mysql.c
%{gem_instdir}/lib/mysql.rb
%{gem_instdir}/tasks/gem.rake
%{gem_instdir}/tasks/native.rake
%{gem_instdir}/tasks/vendor_mysql.rake
%{gem_instdir}/ext/mysql_api/Makefile
%{gem_instdir}/ext/mysql_api/error_const.h
%{gem_instdir}/ext/mysql_api/mkmf.log
%{gem_instdir}/ext/mysql_api/mysql.o
%{gem_instdir}/lib/mysql_api.so
%exclude %{gem_cache}
%{gem_spec}

%files doc
%{gem_instdir}/test/test_mysql.rb
%{gem_docdir}
%{gem_instdir}/extra/README.html
%{gem_instdir}/extra/README_ja.html
%{gem_instdir}/extra/tommy.css
%{gem_instdir}/Rakefile

%changelog
* Tue Jun 04 2013 Dominic Cleal <dcleal@redhat.com> 2.8.1-4
- Add gem_spec to rubygem-mysql* to fix loading, exclude gem_cache
  (dcleal@redhat.com)

* Fri May 24 2013 Martin Bačovský <mbacovsk@redhat.com> 2.8.1-3
- new package built with tito
- added support for SCL


* Tue May 08 2012 jmontleo@redhat.com - 2.8.1-2
- Cleaned up spec file
