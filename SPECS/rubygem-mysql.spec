%define rbname mysql
%define version 2.8.1
%define release 2

Summary: This is the MySQL API module for Ruby
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://mysql-win.rubyforge.org
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 1.8.6
Requires: rubygems >= 1.8.10
BuildRequires: ruby >= 1.8.6
BuildRequires: rubygems >= 1.8.10
BuildRequires: mysql-devel
Provides: rubygem(mysql) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
This is the MySQL API module for Ruby. It provides the same functions for Ruby
programs that the MySQL C API provides for C programs.
This is a conversion of tmtm's original extension into a proper RubyGems.


%prep
%setup -T -c

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{gembuilddir}
gem install --local --install-dir %{gembuilddir} --force %{SOURCE0}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%{gemdir}/gems/mysql-2.8.1/COPYING
%{gemdir}/gems/mysql-2.8.1/COPYING.ja
%doc %{gemdir}/gems/mysql-2.8.1/History.txt
%doc %{gemdir}/gems/mysql-2.8.1/Manifest.txt
%doc %{gemdir}/gems/mysql-2.8.1/README.txt
%{gemdir}/gems/mysql-2.8.1/Rakefile
%{gemdir}/gems/mysql-2.8.1/ext/mysql_api/extconf.rb
%{gemdir}/gems/mysql-2.8.1/ext/mysql_api/mysql.c
%{gemdir}/gems/mysql-2.8.1/extra/README.html
%{gemdir}/gems/mysql-2.8.1/extra/README_ja.html
%{gemdir}/gems/mysql-2.8.1/extra/tommy.css
%{gemdir}/gems/mysql-2.8.1/lib/mysql.rb
%{gemdir}/gems/mysql-2.8.1/tasks/gem.rake
%{gemdir}/gems/mysql-2.8.1/tasks/native.rake
%{gemdir}/gems/mysql-2.8.1/tasks/vendor_mysql.rake
%{gemdir}/gems/mysql-2.8.1/test/test_mysql.rb
   /usr/lib/ruby/gems/1.8/gems/mysql-2.8.1/ext/mysql_api/Makefile
   /usr/lib/ruby/gems/1.8/gems/mysql-2.8.1/ext/mysql_api/error_const.h
   /usr/lib/ruby/gems/1.8/gems/mysql-2.8.1/ext/mysql_api/mkmf.log
   /usr/lib/ruby/gems/1.8/gems/mysql-2.8.1/ext/mysql_api/mysql.o
   /usr/lib/ruby/gems/1.8/gems/mysql-2.8.1/ext/mysql_api/mysql_api.so
   /usr/lib/ruby/gems/1.8/gems/mysql-2.8.1/lib/mysql_api.so


%doc %{gemdir}/doc/mysql-2.8.1
%{gemdir}/cache/mysql-2.8.1.gem
%{gemdir}/specifications/mysql-2.8.1.gemspec

%changelog
* Tue May 08 2012 jmontleo@redhat.com - 2.8.1-2
- Cleaned up spec file
