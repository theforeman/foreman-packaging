%define rbname mysql2
%define version 0.2.18
%define release 1

Summary: A simple, fast Mysql library for Ruby, binding to libmysql
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://github.com/brianmario/mysql2
Source0: http://rubygems.org/downloads/%{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.8.10
BuildRequires: ruby 
BuildRequires: rubygems >= 1.8.10
BuildRequires: mysql-devel
Provides: rubygem(mysql2) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description



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
%{gemdir}/gems/mysql2-0.2.18/.gitignore
%{gemdir}/gems/mysql2-0.2.18/.rspec
%{gemdir}/gems/mysql2-0.2.18/.rvmrc
%{gemdir}/gems/mysql2-0.2.18/.travis.yml
%{gemdir}/gems/mysql2-0.2.18/CHANGELOG.md
%{gemdir}/gems/mysql2-0.2.18/Gemfile
%{gemdir}/gems/mysql2-0.2.18/MIT-LICENSE
%{gemdir}/gems/mysql2-0.2.18/README.md
%{gemdir}/gems/mysql2-0.2.18/Rakefile
%{gemdir}/gems/mysql2-0.2.18/benchmark/active_record.rb
%{gemdir}/gems/mysql2-0.2.18/benchmark/active_record_threaded.rb
%{gemdir}/gems/mysql2-0.2.18/benchmark/allocations.rb
%{gemdir}/gems/mysql2-0.2.18/benchmark/escape.rb
%{gemdir}/gems/mysql2-0.2.18/benchmark/query_with_mysql_casting.rb
%{gemdir}/gems/mysql2-0.2.18/benchmark/query_without_mysql_casting.rb
%{gemdir}/gems/mysql2-0.2.18/benchmark/sequel.rb
%{gemdir}/gems/mysql2-0.2.18/benchmark/setup_db.rb
%{gemdir}/gems/mysql2-0.2.18/benchmark/threaded.rb
%{gemdir}/gems/mysql2-0.2.18/examples/eventmachine.rb
%{gemdir}/gems/mysql2-0.2.18/examples/threaded.rb
%{gemdir}/gems/mysql2-0.2.18/ext/mysql2/client.c
%{gemdir}/gems/mysql2-0.2.18/ext/mysql2/client.h
%{gemdir}/gems/mysql2-0.2.18/ext/mysql2/extconf.rb
%{gemdir}/gems/mysql2-0.2.18/ext/mysql2/mysql2_ext.c
%{gemdir}/gems/mysql2-0.2.18/ext/mysql2/mysql2_ext.h
%{gemdir}/gems/mysql2-0.2.18/ext/mysql2/result.c
%{gemdir}/gems/mysql2-0.2.18/ext/mysql2/result.h
%{gemdir}/gems/mysql2-0.2.18/ext/mysql2/wait_for_single_fd.h
%{gemdir}/gems/mysql2-0.2.18/lib/mysql2.rb
%{gemdir}/gems/mysql2-0.2.18/lib/mysql2/client.rb
%{gemdir}/gems/mysql2-0.2.18/lib/mysql2/em.rb
%{gemdir}/gems/mysql2-0.2.18/lib/mysql2/error.rb
%{gemdir}/gems/mysql2-0.2.18/lib/mysql2/result.rb
%{gemdir}/gems/mysql2-0.2.18/lib/mysql2/version.rb
%{gemdir}/gems/mysql2-0.2.18/mysql2.gemspec
%{gemdir}/gems/mysql2-0.2.18/spec/em/em_spec.rb
%{gemdir}/gems/mysql2-0.2.18/spec/mysql2/client_spec.rb
%{gemdir}/gems/mysql2-0.2.18/spec/mysql2/error_spec.rb
%{gemdir}/gems/mysql2-0.2.18/spec/mysql2/result_spec.rb
%{gemdir}/gems/mysql2-0.2.18/spec/rcov.opts
%{gemdir}/gems/mysql2-0.2.18/spec/spec_helper.rb
%{gemdir}/gems/mysql2-0.2.18/tasks/benchmarks.rake
%{gemdir}/gems/mysql2-0.2.18/tasks/compile.rake
%{gemdir}/gems/mysql2-0.2.18/tasks/rspec.rake
%{gemdir}/gems/mysql2-0.2.18/tasks/vendor_mysql.rake
%{gemdir}/gems/mysql2-0.2.18/ext/mysql2/Makefile
%{gemdir}/gems/mysql2-0.2.18/ext/mysql2/client.o
%{gemdir}/gems/mysql2-0.2.18/ext/mysql2/mkmf.log
%{gemdir}/gems/mysql2-0.2.18/ext/mysql2/mysql2.so
%{gemdir}/gems/mysql2-0.2.18/ext/mysql2/mysql2_ext.o
%{gemdir}/gems/mysql2-0.2.18/ext/mysql2/result.o
%{gemdir}/gems/mysql2-0.2.18/lib/mysql2/mysql2.so
%{gemdir}/gems/mysql2-0.2.18/lib/active_record/connection_adapters/em_mysql2_adapter.rb
%{gemdir}/gems/mysql2-0.2.18/lib/active_record/connection_adapters/mysql2_adapter.rb
%{gemdir}/gems/mysql2-0.2.18/lib/active_record/fiber_patches.rb
%{gemdir}/gems/mysql2-0.2.18/lib/arel/engines/sql/compilers/mysql2_compiler.rb
%{gemdir}/gems/mysql2-0.2.18/lib/mysql2/em_fiber.rb
%{gemdir}/gems/mysql2-0.2.18/spec/em/em_fiber_spec.rb
%doc %{gemdir}/doc/mysql2-0.2.18
%{gemdir}/cache/mysql2-0.2.18.gem
%{gemdir}/specifications/mysql2-0.2.18.gemspec

%changelog
* Tue May 08 2012 jmontleo@redhat.com - 0.2.18-2
- Cleaned up spec file
