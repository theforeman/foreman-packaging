# Generated from mysql2-0.2.18.gem by gem2rpm -*- rpm-spec -*-
%global gemname mysql2

%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}
%global rubyabi 1.8

Summary: A simple, fast Mysql library for Ruby, binding to libmysql
Name: rubygem-%{gemname}
Version: 0.2.18
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://github.com/brianmario/mysql2
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
Requires: ruby 
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: ruby(rubygems) 
BuildRequires: ruby 
BuildRequires: ruby-devel
BuildRequires: mysql-devel
Provides: rubygem(%{gemname}) = %{version}

%description



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

%files doc
%doc %{gemdir}/doc/%{gemname}-%{version}
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
%{gemdir}/gems/mysql2-0.2.18/spec/em/em_fiber_spec.rb
%changelog
* Mon Jul 02 2012 jason - 0.2.18-1
- Initial package
