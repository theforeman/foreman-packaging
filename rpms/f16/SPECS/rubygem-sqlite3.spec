# Generated from sqlite3-1.3.5.gem by gem2rpm -*- rpm-spec -*-
%global gemname sqlite3

%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}
%global rubyabi 1.8

Summary: This module allows Ruby programs to interface with the SQLite3 database engine (http://www.sqlite.org)
Name: rubygem-%{gemname}
Version: 1.3.5
Release: 2%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://github.com/luislavena/sqlite3-ruby
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) >= 1.3.5
Requires: ruby >= 1.8.7
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: ruby(rubygems) >= 1.3.5
BuildRequires: ruby >= 1.8.7
Provides: rubygem(%{gemname}) = %{version}

%description
This module allows Ruby programs to interface with the SQLite3
database engine (http://www.sqlite.org).  You must have the
SQLite engine installed in order to build this module.
Note that this module is only compatible with SQLite 3.6.16 or newer.


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
%{gemdir}/gems/sqlite3-1.3.5/.gemtest
%{gemdir}/gems/sqlite3-1.3.5/ChangeLog.cvs
%{gemdir}/gems/sqlite3-1.3.5/LICENSE
%{gemdir}/gems/sqlite3-1.3.5/Rakefile
%{gemdir}/gems/sqlite3-1.3.5/faq/faq.rb
%{gemdir}/gems/sqlite3-1.3.5/faq/faq.yml
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

%files doc
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/Manifest.txt
%doc %{geminstdir}/README.rdoc
%doc %{geminstdir}/CHANGELOG.rdoc
%doc %{geminstdir}/API_CHANGES.rdoc


%changelog
* Tue May 08 2012 jmontleo@redhat.com - 1.3.5-2
- Cleaned up spec file
* Tue Apr 10 2012 jason - 1.3.5-1
- Initial package
