%define rbname rest-client
%define version 1.6.7
%define release 1

Summary: Simple HTTP and REST client for Ruby, inspired by microframework syntax for specifying actions.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://github.com/archiloque/rest-client
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.8.10

Requires: rubygem-mime-types >= 1.16
BuildRequires: ruby 
BuildRequires: rubygems >= 1.8.10
BuildArch: noarch
Provides: rubygem(rest-client) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
A simple HTTP and REST client for Ruby, inspired by the Sinatra microframework
style of specifying actions: get, put, post, delete.


%prep
%setup -T -c

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{gembuilddir}
gem install --local --install-dir %{gembuilddir} --force %{SOURCE0}
mkdir -p %{buildroot}/%{_bindir}
mv %{gembuilddir}/bin/* %{buildroot}/%{_bindir}
rmdir %{gembuilddir}/bin

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%{_bindir}/restclient
%doc %{gemdir}/gems/rest-client-1.6.7/README.rdoc
%{gemdir}/gems/rest-client-1.6.7/Rakefile
%{gemdir}/gems/rest-client-1.6.7/VERSION
%{gemdir}/gems/rest-client-1.6.7/bin/restclient
%{gemdir}/gems/rest-client-1.6.7/lib/rest-client.rb
%{gemdir}/gems/rest-client-1.6.7/lib/rest_client.rb
%{gemdir}/gems/rest-client-1.6.7/lib/restclient.rb
%{gemdir}/gems/rest-client-1.6.7/lib/restclient/abstract_response.rb
%{gemdir}/gems/rest-client-1.6.7/lib/restclient/exceptions.rb
%{gemdir}/gems/rest-client-1.6.7/lib/restclient/net_http_ext.rb
%{gemdir}/gems/rest-client-1.6.7/lib/restclient/payload.rb
%{gemdir}/gems/rest-client-1.6.7/lib/restclient/raw_response.rb
%{gemdir}/gems/rest-client-1.6.7/lib/restclient/request.rb
%{gemdir}/gems/rest-client-1.6.7/lib/restclient/resource.rb
%{gemdir}/gems/rest-client-1.6.7/lib/restclient/response.rb
%{gemdir}/gems/rest-client-1.6.7/spec/abstract_response_spec.rb
%{gemdir}/gems/rest-client-1.6.7/spec/base.rb
%{gemdir}/gems/rest-client-1.6.7/spec/exceptions_spec.rb
%{gemdir}/gems/rest-client-1.6.7/spec/integration/certs/equifax.crt
%{gemdir}/gems/rest-client-1.6.7/spec/integration/certs/verisign.crt
%{gemdir}/gems/rest-client-1.6.7/spec/integration/request_spec.rb
%{gemdir}/gems/rest-client-1.6.7/spec/integration_spec.rb
%{gemdir}/gems/rest-client-1.6.7/spec/master_shake.jpg
%{gemdir}/gems/rest-client-1.6.7/spec/payload_spec.rb
%{gemdir}/gems/rest-client-1.6.7/spec/raw_response_spec.rb
%{gemdir}/gems/rest-client-1.6.7/spec/request2_spec.rb
%{gemdir}/gems/rest-client-1.6.7/spec/request_spec.rb
%{gemdir}/gems/rest-client-1.6.7/spec/resource_spec.rb
%{gemdir}/gems/rest-client-1.6.7/spec/response_spec.rb
%{gemdir}/gems/rest-client-1.6.7/spec/restclient_spec.rb
%doc %{gemdir}/gems/rest-client-1.6.7/history.md


%doc %{gemdir}/doc/rest-client-1.6.7
%{gemdir}/cache/rest-client-1.6.7.gem
%{gemdir}/specifications/rest-client-1.6.7.gemspec

%changelog
