%define rbname sqlite3
%define version 1.3.5
%define release 2

Summary: This module allows Ruby programs to interface with the SQLite3 database engine (http://www.sqlite.org)
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://github.com/luislavena/sqlite3-ruby
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 1.8.7
Requires: rubygems >= 1.8.10
BuildRequires: ruby >= 1.8.7
BuildRequires: rubygems >= 1.8.10
BuildRequires: sqlite-devel
Provides: rubygem(sqlite3) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
This module allows Ruby programs to interface with the SQLite3
database engine (http://www.sqlite.org).  You must have the
SQLite engine installed in order to build this module.
Note that this module is only compatible with SQLite 3.6.16 or newer.


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
%doc %{gemdir}/gems/sqlite3-1.3.5/API_CHANGES.rdoc
%doc %{gemdir}/gems/sqlite3-1.3.5/CHANGELOG.rdoc
%{gemdir}/gems/sqlite3-1.3.5/ChangeLog.cvs
%{gemdir}/gems/sqlite3-1.3.5/LICENSE
%doc %{gemdir}/gems/sqlite3-1.3.5/Manifest.txt
%doc %{gemdir}/gems/sqlite3-1.3.5/README.rdoc
%{gemdir}/gems/sqlite3-1.3.5/Rakefile
%doc %{gemdir}/gems/sqlite3-1.3.5/ext/sqlite3/backup.c
%{gemdir}/gems/sqlite3-1.3.5/ext/sqlite3/backup.h
%doc %{gemdir}/gems/sqlite3-1.3.5/ext/sqlite3/database.c
%{gemdir}/gems/sqlite3-1.3.5/ext/sqlite3/database.h
%doc %{gemdir}/gems/sqlite3-1.3.5/ext/sqlite3/exception.c
%{gemdir}/gems/sqlite3-1.3.5/ext/sqlite3/exception.h
%{gemdir}/gems/sqlite3-1.3.5/ext/sqlite3/extconf.rb
%doc %{gemdir}/gems/sqlite3-1.3.5/ext/sqlite3/sqlite3.c
%{gemdir}/gems/sqlite3-1.3.5/ext/sqlite3/sqlite3_ruby.h
%doc %{gemdir}/gems/sqlite3-1.3.5/ext/sqlite3/statement.c
%{gemdir}/gems/sqlite3-1.3.5/ext/sqlite3/statement.h
%{gemdir}/gems/sqlite3-1.3.5/faq/faq.rb
%{gemdir}/gems/sqlite3-1.3.5/faq/faq.yml
%{gemdir}/gems/sqlite3-1.3.5/lib/sqlite3.rb
%{gemdir}/gems/sqlite3-1.3.5/lib/sqlite3/constants.rb
%{gemdir}/gems/sqlite3-1.3.5/lib/sqlite3/database.rb
%{gemdir}/gems/sqlite3-1.3.5/lib/sqlite3/errors.rb
%{gemdir}/gems/sqlite3-1.3.5/lib/sqlite3/pragmas.rb
%{gemdir}/gems/sqlite3-1.3.5/lib/sqlite3/resultset.rb
%{gemdir}/gems/sqlite3-1.3.5/lib/sqlite3/statement.rb
%{gemdir}/gems/sqlite3-1.3.5/lib/sqlite3/translator.rb
%{gemdir}/gems/sqlite3-1.3.5/lib/sqlite3/value.rb
%{gemdir}/gems/sqlite3-1.3.5/lib/sqlite3/version.rb
%{gemdir}/gems/sqlite3-1.3.5/setup.rb
%{gemdir}/gems/sqlite3-1.3.5/tasks/faq.rake
%{gemdir}/gems/sqlite3-1.3.5/tasks/gem.rake
%{gemdir}/gems/sqlite3-1.3.5/tasks/native.rake
%{gemdir}/gems/sqlite3-1.3.5/tasks/vendor_sqlite3.rake
%{gemdir}/gems/sqlite3-1.3.5/test/helper.rb
%{gemdir}/gems/sqlite3-1.3.5/test/test_backup.rb
%{gemdir}/gems/sqlite3-1.3.5/test/test_collation.rb
%{gemdir}/gems/sqlite3-1.3.5/test/test_database.rb
%{gemdir}/gems/sqlite3-1.3.5/test/test_database_readonly.rb
%{gemdir}/gems/sqlite3-1.3.5/test/test_deprecated.rb
%{gemdir}/gems/sqlite3-1.3.5/test/test_encoding.rb
%{gemdir}/gems/sqlite3-1.3.5/test/test_integration.rb
%{gemdir}/gems/sqlite3-1.3.5/test/test_integration_open_close.rb
%{gemdir}/gems/sqlite3-1.3.5/test/test_integration_pending.rb
%{gemdir}/gems/sqlite3-1.3.5/test/test_integration_resultset.rb
%{gemdir}/gems/sqlite3-1.3.5/test/test_integration_statement.rb
%{gemdir}/gems/sqlite3-1.3.5/test/test_sqlite3.rb
%{gemdir}/gems/sqlite3-1.3.5/test/test_statement.rb
%{gemdir}/gems/sqlite3-1.3.5/test/test_statement_execute.rb
%{gemdir}/gems/sqlite3-1.3.5/.gemtest
%{gemdir}/gems/sqlite3-1.3.5/ext/sqlite3/Makefile
%{gemdir}/gems/sqlite3-1.3.5/ext/sqlite3/backup.o
%{gemdir}/gems/sqlite3-1.3.5/ext/sqlite3/database.o
%{gemdir}/gems/sqlite3-1.3.5/ext/sqlite3/exception.o
%{gemdir}/gems/sqlite3-1.3.5/ext/sqlite3/mkmf.log
%{gemdir}/gems/sqlite3-1.3.5/ext/sqlite3/sqlite3.o
%{gemdir}/gems/sqlite3-1.3.5/ext/sqlite3/sqlite3_native.so
%{gemdir}/gems/sqlite3-1.3.5/ext/sqlite3/statement.o
%{gemdir}/gems/sqlite3-1.3.5/lib/sqlite3/sqlite3_native.so
%doc %{gemdir}/doc/sqlite3-1.3.5
%{gemdir}/cache/sqlite3-1.3.5.gem
%{gemdir}/specifications/sqlite3-1.3.5.gemspec

%changelog
* Tue May 08 2012 jmontleo@redhat.com - 1.3.5-2
- Cleaned up spec file

