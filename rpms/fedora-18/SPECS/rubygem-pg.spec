# Generated from pg-0.13.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name pg
%global rubyabi 1.9.1

Summary: Pg is the Ruby interface to the {PostgreSQL RDBMS}[http://www.postgresql.org/]
Name: rubygem-%{gem_name}
Version: 0.13.2
Release: 1%{?dist}
Group: Development/Languages
License: BSD and Ruby and GPL
URL: https://bitbucket.org/ged/ruby-pg
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems)
Requires: ruby >= 1.8.7

BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: rubygems-devel
BuildRequires: ruby >= 1.8.7
BuildRequires: ruby-devel
BuildRequires: postgresql-devel

Provides: rubygem(%{gem_name}) = %{version}

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


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
%setup -q -c -T
mkdir -p .%{gem_dir}
export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
gem install --local --install-dir .%{gem_dir} \
	    -V \
	    --force %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir}/lib
# TODO: move the extensions
##mv %{buildroot}%{gem_instdir}/lib/shared_object.so %{buildroot}%{gem_extdir}/lib/



# Remove the binary extension sources and build leftovers.
rm -rf %{buildroot}%{geminstdir}/ext

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_extdir}
%exclude %{gem_cache}
%{gem_spec}
/usr/share/gems/gems/pg-0.13.2/
%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/Manifest.txt
%doc %{gem_instdir}/Contributors.rdoc
%doc %{gem_instdir}/History.rdoc
%doc %{gem_instdir}/README-OS_X.rdoc
%doc %{gem_instdir}/README-Windows.rdoc
%doc %{gem_instdir}/README.ja.rdoc
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/POSTGRES
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/ext/pg.c
%doc %{gem_instdir}/ext/pg_connection.c
%doc %{gem_instdir}/ext/pg_result.c

%changelog
* Thu Jun 14 2012 jason - 0.13.2-1
- Initial package
