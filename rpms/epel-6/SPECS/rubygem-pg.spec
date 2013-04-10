%define rbname pg
%define version 0.13.2
%define release 2

Summary: Pg is the Ruby interface to the {PostgreSQL RDBMS}[http://www.postgresql.org/]
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: https://bitbucket.org/ged/ruby-pg
Source0: http://rubygems.org/downloads/%{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 1.8.7
Requires: rubygems >= 1.8.10
BuildRequires: ruby >= 1.8.7
BuildRequires: rubygems >= 1.8.10
BuildRequires: postgresql-devel
Provides: rubygem(pg) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
Pg is the Ruby interface to the {PostgreSQL
RDBMS}[http://www.postgresql.org/].
It works with {PostgreSQL 8.3 and later}[http://bit.ly/6AfPhm].
A small example usage:
#!/usr/bin/env ruby
require 'pg'
# Output a table of current connections to the DB
conn = PG.connect( dbname: 'sales' )
conn.exec( "SELECT * FROM pg_stat_activity" ) do |result|
puts "     PID | User             | Query"
result.each do |row|
puts " %7d | %-16s | %s " %
row.values_at('procpid', 'usename', 'current_query')
end
end


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
%{gemdir}/gems/pg-0.13.2/.gemtest
%{gemdir}/gems/pg-0.13.2/BSDL
%{gemdir}/gems/pg-0.13.2/ChangeLog
%doc %{gemdir}/gems/pg-0.13.2/Contributors.rdoc
%doc %{gemdir}/gems/pg-0.13.2/History.rdoc
%doc %{gemdir}/gems/pg-0.13.2/LICENSE
%doc %{gemdir}/gems/pg-0.13.2/Manifest.txt
%doc %{gemdir}/gems/pg-0.13.2/POSTGRES
%doc %{gemdir}/gems/pg-0.13.2/README-OS_X.rdoc
%doc %{gemdir}/gems/pg-0.13.2/README-Windows.rdoc
%doc %{gemdir}/gems/pg-0.13.2/README.ja.rdoc
%doc %{gemdir}/gems/pg-0.13.2/README.rdoc
%{gemdir}/gems/pg-0.13.2/Rakefile
%{gemdir}/gems/pg-0.13.2/Rakefile.cross
%{gemdir}/gems/pg-0.13.2/ext/extconf.rb
%doc %{gemdir}/gems/pg-0.13.2/ext/pg.c
%{gemdir}/gems/pg-0.13.2/ext/pg.h
%doc %{gemdir}/gems/pg-0.13.2/ext/pg_connection.c
%doc %{gemdir}/gems/pg-0.13.2/ext/pg_result.c
%{gemdir}/gems/pg-0.13.2/ext/vc/pg.sln
%{gemdir}/gems/pg-0.13.2/ext/vc/pg_18/pg.vcproj
%{gemdir}/gems/pg-0.13.2/ext/vc/pg_19/pg_19.vcproj
%{gemdir}/gems/pg-0.13.2/lib/pg.rb
%{gemdir}/gems/pg-0.13.2/lib/pg/connection.rb
%{gemdir}/gems/pg-0.13.2/lib/pg/constants.rb
%{gemdir}/gems/pg-0.13.2/lib/pg/exceptions.rb
%{gemdir}/gems/pg-0.13.2/lib/pg/result.rb
%{gemdir}/gems/pg-0.13.2/sample/async_api.rb
%{gemdir}/gems/pg-0.13.2/sample/async_copyto.rb
%{gemdir}/gems/pg-0.13.2/sample/async_mixed.rb
%{gemdir}/gems/pg-0.13.2/sample/copyfrom.rb
%{gemdir}/gems/pg-0.13.2/sample/copyto.rb
%{gemdir}/gems/pg-0.13.2/sample/cursor.rb
%{gemdir}/gems/pg-0.13.2/sample/losample.rb
%{gemdir}/gems/pg-0.13.2/sample/notify_wait.rb
%{gemdir}/gems/pg-0.13.2/sample/test_binary_values.rb
%{gemdir}/gems/pg-0.13.2/spec/data/expected_trace.out
%{gemdir}/gems/pg-0.13.2/spec/data/random_binary_data
%{gemdir}/gems/pg-0.13.2/spec/lib/helpers.rb
%{gemdir}/gems/pg-0.13.2/spec/pg/connection_spec.rb
%{gemdir}/gems/pg-0.13.2/spec/pg/result_spec.rb
%{gemdir}/gems/pg-0.13.2/spec/pg_spec.rb
%{gemdir}/gems/pg-0.13.2/ext/Makefile
%{gemdir}/gems/pg-0.13.2/ext/extconf.h
%{gemdir}/gems/pg-0.13.2/ext/mkmf.log
%{gemdir}/gems/pg-0.13.2/ext/pg.o
%{gemdir}/gems/pg-0.13.2/ext/pg_connection.o
%{gemdir}/gems/pg-0.13.2/ext/pg_ext.so
%{gemdir}/gems/pg-0.13.2/ext/pg_result.o
%{gemdir}/gems/pg-0.13.2/lib/pg_ext.so

%doc %{gemdir}/doc/pg-0.13.2
%{gemdir}/cache/pg-0.13.2.gem
%{gemdir}/specifications/pg-0.13.2.gemspec

%changelog
* Tue May 08 2012 jmontleo@redhat.com - 0.13.2-2
- Cleaned up spec file
