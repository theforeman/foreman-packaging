%define rbname rack-test
%define version 0.5.7
%define release 2

Summary: Simple testing API built on Rack
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://github.com/brynary/rack-test
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.8.10

Requires: rubygem-rack >= 1.0
BuildRequires: ruby 
BuildRequires: rubygems >= 1.8.10
BuildArch: noarch
Provides: rubygem(rack-test) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
Rack::Test is a small, simple testing API for Rack apps. It can be used on its
own or as a reusable starting point for Web frameworks and testing libraries
to build on. Most of its initial functionality is an extraction of Merb 1.0's
request helpers feature.


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
%{gemdir}/gems/rack-test-0.5.7/.document
%{gemdir}/gems/rack-test-0.5.7/.gitignore
%{gemdir}/gems/rack-test-0.5.7/Gemfile
%{gemdir}/gems/rack-test-0.5.7/Gemfile.lock
%{gemdir}/gems/rack-test-0.5.7/History.txt
%doc %{gemdir}/gems/rack-test-0.5.7/MIT-LICENSE.txt
%doc %{gemdir}/gems/rack-test-0.5.7/README.rdoc
%{gemdir}/gems/rack-test-0.5.7/Rakefile
%{gemdir}/gems/rack-test-0.5.7/Thorfile
%{gemdir}/gems/rack-test-0.5.7/lib/rack/mock_session.rb
%{gemdir}/gems/rack-test-0.5.7/lib/rack/test.rb
%{gemdir}/gems/rack-test-0.5.7/lib/rack/test/cookie_jar.rb
%{gemdir}/gems/rack-test-0.5.7/lib/rack/test/methods.rb
%{gemdir}/gems/rack-test-0.5.7/lib/rack/test/mock_digest_request.rb
%{gemdir}/gems/rack-test-0.5.7/lib/rack/test/uploaded_file.rb
%{gemdir}/gems/rack-test-0.5.7/lib/rack/test/utils.rb
%{gemdir}/gems/rack-test-0.5.7/rack-test.gemspec
%{gemdir}/gems/rack-test-0.5.7/spec/fixtures/bar.txt
%{gemdir}/gems/rack-test-0.5.7/spec/fixtures/config.ru
%{gemdir}/gems/rack-test-0.5.7/spec/fixtures/fake_app.rb
%{gemdir}/gems/rack-test-0.5.7/spec/fixtures/foo.txt
%{gemdir}/gems/rack-test-0.5.7/spec/rack/test/cookie_spec.rb
%{gemdir}/gems/rack-test-0.5.7/spec/rack/test/digest_auth_spec.rb
%{gemdir}/gems/rack-test-0.5.7/spec/rack/test/multipart_spec.rb
%{gemdir}/gems/rack-test-0.5.7/spec/rack/test/utils_spec.rb
%{gemdir}/gems/rack-test-0.5.7/spec/rack/test_spec.rb
%{gemdir}/gems/rack-test-0.5.7/spec/spec_helper.rb
%{gemdir}/gems/rack-test-0.5.7/spec/support/matchers/body.rb
%{gemdir}/gems/rack-test-0.5.7/spec/support/matchers/challenge.rb
%doc %{gemdir}/doc/rack-test-0.5.7
%{gemdir}/cache/rack-test-0.5.7.gem
%{gemdir}/specifications/rack-test-0.5.7.gemspec

%changelog
* Tue May 08 2012 jmontleo@redhat.com - 0.5.7-2
- Cleaned up spec file
