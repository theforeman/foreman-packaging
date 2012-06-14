%define rbname excon
%define version 0.13.3
%define release 1

Summary: speed, persistence, http(s)
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: https://github.com/geemus/excon
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.8.10
BuildRequires: ruby 
BuildRequires: rubygems >= 1.8.10
BuildArch: noarch
Provides: rubygem(excon) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
EXtended http(s) CONnections


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
%{gemdir}/gems/excon-0.13.3/Gemfile
%doc %{gemdir}/gems/excon-0.13.3/README.md
%{gemdir}/gems/excon-0.13.3/Rakefile
%{gemdir}/gems/excon-0.13.3/benchmarks
%{gemdir}/gems/excon-0.13.3/changelog.txt
%{gemdir}/gems/excon-0.13.3/data/cacert.pem
%{gemdir}/gems/excon-0.13.3/excon.gemspec
%{gemdir}/gems/excon-0.13.3/lib/excon.rb
%{gemdir}/gems/excon-0.13.3/lib/excon/connection.rb
%{gemdir}/gems/excon-0.13.3/lib/excon/constants.rb
%{gemdir}/gems/excon-0.13.3/lib/excon/errors.rb
%{gemdir}/gems/excon-0.13.3/lib/excon/response.rb
%{gemdir}/gems/excon-0.13.3/lib/excon/socket.rb
%{gemdir}/gems/excon-0.13.3/lib/excon/ssl_socket.rb
%{gemdir}/gems/excon-0.13.3/tests/bad_tests.rb
%{gemdir}/gems/excon-0.13.3/tests/basic_tests.rb
%{gemdir}/gems/excon-0.13.3/tests/header_tests.rb
%{gemdir}/gems/excon-0.13.3/tests/idempotent_tests.rb
%{gemdir}/gems/excon-0.13.3/tests/instrumentation_tests.rb
%{gemdir}/gems/excon-0.13.3/tests/proxy_tests.rb
%{gemdir}/gems/excon-0.13.3/tests/query_string_tests.rb
%{gemdir}/gems/excon-0.13.3/tests/rackups/basic.rb
%{gemdir}/gems/excon-0.13.3/tests/rackups/basic.ru
%{gemdir}/gems/excon-0.13.3/tests/rackups/basic_auth.ru
%{gemdir}/gems/excon-0.13.3/tests/rackups/proxy.ru
%{gemdir}/gems/excon-0.13.3/tests/rackups/query_string.ru
%{gemdir}/gems/excon-0.13.3/tests/rackups/request_methods.ru
%{gemdir}/gems/excon-0.13.3/tests/rackups/response_header.ru
%{gemdir}/gems/excon-0.13.3/tests/rackups/ssl.ru
%{gemdir}/gems/excon-0.13.3/tests/rackups/thread_safety.ru
%{gemdir}/gems/excon-0.13.3/tests/request_method_tests.rb
%{gemdir}/gems/excon-0.13.3/tests/servers/bad.rb
%{gemdir}/gems/excon-0.13.3/tests/stub_tests.rb
%{gemdir}/gems/excon-0.13.3/tests/test_helper.rb
%{gemdir}/gems/excon-0.13.3/tests/thread_safety_tests.rb

%doc %{gemdir}/doc/excon-0.13.3
%{gemdir}/cache/excon-0.13.3.gem
%{gemdir}/specifications/excon-0.13.3.gemspec

%changelog
