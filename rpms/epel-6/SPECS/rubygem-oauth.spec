%define rbname oauth
%define version 0.4.6
%define release 1

Summary: OAuth Core Ruby implementation
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
Source0: http://rubygems.org/downloads/%{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.8.10
BuildRequires: ruby 
BuildRequires: rubygems >= 1.8.10
BuildArch: noarch
Provides: rubygem(oauth) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
OAuth Core Ruby implementation


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
%{_bindir}/oauth
%{gemdir}/gems/oauth-0.4.6/.gemtest
%{gemdir}/gems/oauth-0.4.6/Gemfile
%{gemdir}/gems/oauth-0.4.6/Gemfile.lock
%{gemdir}/gems/oauth-0.4.6/HISTORY
%doc %{gemdir}/gems/oauth-0.4.6/LICENSE
%doc %{gemdir}/gems/oauth-0.4.6/README.rdoc
%{gemdir}/gems/oauth-0.4.6/Rakefile
%doc %{gemdir}/gems/oauth-0.4.6/TODO
%{gemdir}/gems/oauth-0.4.6/bin/oauth
%{gemdir}/gems/oauth-0.4.6/examples/yql.rb
%{gemdir}/gems/oauth-0.4.6/lib/digest/hmac.rb
%{gemdir}/gems/oauth-0.4.6/lib/oauth.rb
%{gemdir}/gems/oauth-0.4.6/lib/oauth/cli.rb
%{gemdir}/gems/oauth-0.4.6/lib/oauth/client.rb
%{gemdir}/gems/oauth-0.4.6/lib/oauth/client/action_controller_request.rb
%{gemdir}/gems/oauth-0.4.6/lib/oauth/client/em_http.rb
%{gemdir}/gems/oauth-0.4.6/lib/oauth/client/helper.rb
%{gemdir}/gems/oauth-0.4.6/lib/oauth/client/net_http.rb
%{gemdir}/gems/oauth-0.4.6/lib/oauth/consumer.rb
%{gemdir}/gems/oauth-0.4.6/lib/oauth/core_ext.rb
%{gemdir}/gems/oauth-0.4.6/lib/oauth/errors.rb
%{gemdir}/gems/oauth-0.4.6/lib/oauth/errors/error.rb
%{gemdir}/gems/oauth-0.4.6/lib/oauth/errors/problem.rb
%{gemdir}/gems/oauth-0.4.6/lib/oauth/errors/unauthorized.rb
%{gemdir}/gems/oauth-0.4.6/lib/oauth/helper.rb
%{gemdir}/gems/oauth-0.4.6/lib/oauth/oauth.rb
%{gemdir}/gems/oauth-0.4.6/lib/oauth/oauth_test_helper.rb
%{gemdir}/gems/oauth-0.4.6/lib/oauth/request_proxy.rb
%{gemdir}/gems/oauth-0.4.6/lib/oauth/request_proxy/action_controller_request.rb
%{gemdir}/gems/oauth-0.4.6/lib/oauth/request_proxy/base.rb
%{gemdir}/gems/oauth-0.4.6/lib/oauth/request_proxy/curb_request.rb
%{gemdir}/gems/oauth-0.4.6/lib/oauth/request_proxy/em_http_request.rb
%{gemdir}/gems/oauth-0.4.6/lib/oauth/request_proxy/jabber_request.rb
%{gemdir}/gems/oauth-0.4.6/lib/oauth/request_proxy/mock_request.rb
%{gemdir}/gems/oauth-0.4.6/lib/oauth/request_proxy/net_http.rb
%{gemdir}/gems/oauth-0.4.6/lib/oauth/request_proxy/rack_request.rb
%{gemdir}/gems/oauth-0.4.6/lib/oauth/request_proxy/typhoeus_request.rb
%{gemdir}/gems/oauth-0.4.6/lib/oauth/server.rb
%{gemdir}/gems/oauth-0.4.6/lib/oauth/signature.rb
%{gemdir}/gems/oauth-0.4.6/lib/oauth/signature/base.rb
%{gemdir}/gems/oauth-0.4.6/lib/oauth/signature/hmac/base.rb
%{gemdir}/gems/oauth-0.4.6/lib/oauth/signature/hmac/md5.rb
%{gemdir}/gems/oauth-0.4.6/lib/oauth/signature/hmac/rmd160.rb
%{gemdir}/gems/oauth-0.4.6/lib/oauth/signature/hmac/sha1.rb
%{gemdir}/gems/oauth-0.4.6/lib/oauth/signature/hmac/sha2.rb
%{gemdir}/gems/oauth-0.4.6/lib/oauth/signature/md5.rb
%{gemdir}/gems/oauth-0.4.6/lib/oauth/signature/plaintext.rb
%{gemdir}/gems/oauth-0.4.6/lib/oauth/signature/rsa/sha1.rb
%{gemdir}/gems/oauth-0.4.6/lib/oauth/signature/sha1.rb
%{gemdir}/gems/oauth-0.4.6/lib/oauth/token.rb
%{gemdir}/gems/oauth-0.4.6/lib/oauth/tokens/access_token.rb
%{gemdir}/gems/oauth-0.4.6/lib/oauth/tokens/consumer_token.rb
%{gemdir}/gems/oauth-0.4.6/lib/oauth/tokens/request_token.rb
%{gemdir}/gems/oauth-0.4.6/lib/oauth/tokens/server_token.rb
%{gemdir}/gems/oauth-0.4.6/lib/oauth/tokens/token.rb
%{gemdir}/gems/oauth-0.4.6/oauth.gemspec
%{gemdir}/gems/oauth-0.4.6/tasks/deployment.rake
%{gemdir}/gems/oauth-0.4.6/tasks/environment.rake
%{gemdir}/gems/oauth-0.4.6/tasks/website.rake
%{gemdir}/gems/oauth-0.4.6/test/cases/oauth_case.rb
%{gemdir}/gems/oauth-0.4.6/test/cases/spec/1_0-final/test_construct_request_url.rb
%{gemdir}/gems/oauth-0.4.6/test/cases/spec/1_0-final/test_normalize_request_parameters.rb
%{gemdir}/gems/oauth-0.4.6/test/cases/spec/1_0-final/test_parameter_encodings.rb
%{gemdir}/gems/oauth-0.4.6/test/cases/spec/1_0-final/test_signature_base_strings.rb
%{gemdir}/gems/oauth-0.4.6/test/integration/consumer_test.rb
%{gemdir}/gems/oauth-0.4.6/test/keys/rsa.cert
%{gemdir}/gems/oauth-0.4.6/test/keys/rsa.pem
%{gemdir}/gems/oauth-0.4.6/test/test_access_token.rb
%{gemdir}/gems/oauth-0.4.6/test/test_action_controller_request_proxy.rb
%{gemdir}/gems/oauth-0.4.6/test/test_consumer.rb
%{gemdir}/gems/oauth-0.4.6/test/test_curb_request_proxy.rb
%{gemdir}/gems/oauth-0.4.6/test/test_em_http_client.rb
%{gemdir}/gems/oauth-0.4.6/test/test_em_http_request_proxy.rb
%{gemdir}/gems/oauth-0.4.6/test/test_helper.rb
%{gemdir}/gems/oauth-0.4.6/test/test_hmac_sha1.rb
%{gemdir}/gems/oauth-0.4.6/test/test_net_http_client.rb
%{gemdir}/gems/oauth-0.4.6/test/test_net_http_request_proxy.rb
%{gemdir}/gems/oauth-0.4.6/test/test_oauth_helper.rb
%{gemdir}/gems/oauth-0.4.6/test/test_rack_request_proxy.rb
%{gemdir}/gems/oauth-0.4.6/test/test_request_token.rb
%{gemdir}/gems/oauth-0.4.6/test/test_rsa_sha1.rb
%{gemdir}/gems/oauth-0.4.6/test/test_server.rb
%{gemdir}/gems/oauth-0.4.6/test/test_signature.rb
%{gemdir}/gems/oauth-0.4.6/test/test_signature_base.rb
%{gemdir}/gems/oauth-0.4.6/test/test_signature_plain_text.rb
%{gemdir}/gems/oauth-0.4.6/test/test_token.rb
%{gemdir}/gems/oauth-0.4.6/test/test_typhoeus_request_proxy.rb


%doc %{gemdir}/doc/oauth-0.4.6
%{gemdir}/cache/oauth-0.4.6.gem
%{gemdir}/specifications/oauth-0.4.6.gemspec

%changelog
