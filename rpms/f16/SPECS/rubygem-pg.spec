# Generated from pg-0.13.2.gem by gem2rpm -*- rpm-spec -*-
%global gemname pg

%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}
%global rubyabi 1.8

Summary: Pg is the Ruby interface to the {PostgreSQL RDBMS}[http://www.postgresql.org/]
Name: rubygem-%{gemname}
Version: 0.13.2
Release: 2%{?dist}
Group: Development/Languages
License: BSD and Ruby and GPL
URL: https://bitbucket.org/ged/ruby-pg
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
Requires: ruby >= 1.8.7
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: ruby(rubygems) 
BuildRequires: ruby >= 1.8.7
Provides: rubygem(%{gemname}) = %{version}

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
puts "  PID | User | Query"
result.each do |row|
puts " %7d | %-16s | %s " %
row.values_at('procpid', 'usename', 'current_query')
end
end


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}


%prep
%setup -q -c -T
mkdir -p .%{gemdir}
export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
gem install --local --install-dir .%{gemdir} \
-V \
--force %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gemdir}
cp -a .%{gemdir}/* \
  %{buildroot}%{gemdir}/

# Remove the binary extension sources and build leftovers.
rm -rf %{buildroot}%{geminstdir}/ext

%files
%dir %{geminstdir}
%{geminstdir}/lib
%exclude %{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec
%{gemdir}/gems/pg-0.13.2/.gemtest
%{gemdir}/gems/pg-0.13.2/BSDL
%{gemdir}/gems/pg-0.13.2/ChangeLog
%{gemdir}/gems/pg-0.13.2/Rakefile
%{gemdir}/gems/pg-0.13.2/Rakefile.cross
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

%files doc
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/Manifest.txt
%doc %{geminstdir}/Contributors.rdoc
%doc %{geminstdir}/History.rdoc
%doc %{geminstdir}/README-OS_X.rdoc
%doc %{geminstdir}/README-Windows.rdoc
%doc %{geminstdir}/README.ja.rdoc
%doc %{geminstdir}/README.rdoc
%doc %{geminstdir}/POSTGRES
%doc %{geminstdir}/LICENSE


%changelog
* Tue May 08 2012 jmontleo@redhat.com - 0.13.2-2
- Cleaned up spec file
* Tue Apr 10 2012 jason - 0.13.2-1
- Initial package
