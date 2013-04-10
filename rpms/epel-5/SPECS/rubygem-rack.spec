%define rbname rack
%define version 1.2.5
%define release 4

Summary: a modular Ruby webserver interface
Name: rubygem-%{rbname}

Epoch: 1
Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://rack.rubyforge.org
Source0: http://rubygems.org/downloads/%{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.8.10
BuildRequires: ruby 
BuildRequires: rubygems >= 1.8.10
BuildArch: noarch
Provides: rubygem(rack) = %{version}
Provides: %{name} = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
Rack provides minimal, modular and adaptable interface for developing
web applications in Ruby.  By wrapping HTTP requests and responses in
the simplest way possible, it unifies and distills the API for web
servers, web frameworks, and software in between (the so-called
middleware) into a single method call.
Also see http://rack.rubyforge.org.


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
%{_bindir}/rackup
%{gemdir}/gems/rack-1.2.5/bin/rackup
%{gemdir}/gems/rack-1.2.5/contrib/rack_logo.svg
%{gemdir}/gems/rack-1.2.5/example/lobster.ru
%{gemdir}/gems/rack-1.2.5/example/protectedlobster.rb
%{gemdir}/gems/rack-1.2.5/example/protectedlobster.ru
%{gemdir}/gems/rack-1.2.5/lib/rack/auth/abstract/handler.rb
%{gemdir}/gems/rack-1.2.5/lib/rack/auth/abstract/request.rb
%{gemdir}/gems/rack-1.2.5/lib/rack/auth/basic.rb
%{gemdir}/gems/rack-1.2.5/lib/rack/auth/digest/md5.rb
%{gemdir}/gems/rack-1.2.5/lib/rack/auth/digest/nonce.rb
%{gemdir}/gems/rack-1.2.5/lib/rack/auth/digest/params.rb
%{gemdir}/gems/rack-1.2.5/lib/rack/auth/digest/request.rb
%{gemdir}/gems/rack-1.2.5/lib/rack/builder.rb
%{gemdir}/gems/rack-1.2.5/lib/rack/cascade.rb
%{gemdir}/gems/rack-1.2.5/lib/rack/chunked.rb
%{gemdir}/gems/rack-1.2.5/lib/rack/commonlogger.rb
%{gemdir}/gems/rack-1.2.5/lib/rack/conditionalget.rb
%{gemdir}/gems/rack-1.2.5/lib/rack/config.rb
%{gemdir}/gems/rack-1.2.5/lib/rack/content_length.rb
%{gemdir}/gems/rack-1.2.5/lib/rack/content_type.rb
%{gemdir}/gems/rack-1.2.5/lib/rack/deflater.rb
%{gemdir}/gems/rack-1.2.5/lib/rack/directory.rb
%{gemdir}/gems/rack-1.2.5/lib/rack/etag.rb
%{gemdir}/gems/rack-1.2.5/lib/rack/file.rb
%{gemdir}/gems/rack-1.2.5/lib/rack/handler/cgi.rb
%{gemdir}/gems/rack-1.2.5/lib/rack/handler/evented_mongrel.rb
%{gemdir}/gems/rack-1.2.5/lib/rack/handler/fastcgi.rb
%{gemdir}/gems/rack-1.2.5/lib/rack/handler/lsws.rb
%{gemdir}/gems/rack-1.2.5/lib/rack/handler/mongrel.rb
%{gemdir}/gems/rack-1.2.5/lib/rack/handler/scgi.rb
%{gemdir}/gems/rack-1.2.5/lib/rack/handler/swiftiplied_mongrel.rb
%{gemdir}/gems/rack-1.2.5/lib/rack/handler/thin.rb
%{gemdir}/gems/rack-1.2.5/lib/rack/handler/webrick.rb
%{gemdir}/gems/rack-1.2.5/lib/rack/handler.rb
%{gemdir}/gems/rack-1.2.5/lib/rack/head.rb
%{gemdir}/gems/rack-1.2.5/lib/rack/lint.rb
%{gemdir}/gems/rack-1.2.5/lib/rack/lobster.rb
%{gemdir}/gems/rack-1.2.5/lib/rack/lock.rb
%{gemdir}/gems/rack-1.2.5/lib/rack/logger.rb
%{gemdir}/gems/rack-1.2.5/lib/rack/methodoverride.rb
%{gemdir}/gems/rack-1.2.5/lib/rack/mime.rb
%{gemdir}/gems/rack-1.2.5/lib/rack/mock.rb
%{gemdir}/gems/rack-1.2.5/lib/rack/nulllogger.rb
%{gemdir}/gems/rack-1.2.5/lib/rack/recursive.rb
%{gemdir}/gems/rack-1.2.5/lib/rack/reloader.rb
%{gemdir}/gems/rack-1.2.5/lib/rack/request.rb
%{gemdir}/gems/rack-1.2.5/lib/rack/response.rb
%{gemdir}/gems/rack-1.2.5/lib/rack/rewindable_input.rb
%{gemdir}/gems/rack-1.2.5/lib/rack/runtime.rb
%{gemdir}/gems/rack-1.2.5/lib/rack/sendfile.rb
%{gemdir}/gems/rack-1.2.5/lib/rack/server.rb
%{gemdir}/gems/rack-1.2.5/lib/rack/session/abstract/id.rb
%{gemdir}/gems/rack-1.2.5/lib/rack/session/cookie.rb
%{gemdir}/gems/rack-1.2.5/lib/rack/session/memcache.rb
%{gemdir}/gems/rack-1.2.5/lib/rack/session/pool.rb
%{gemdir}/gems/rack-1.2.5/lib/rack/showexceptions.rb
%{gemdir}/gems/rack-1.2.5/lib/rack/showstatus.rb
%{gemdir}/gems/rack-1.2.5/lib/rack/static.rb
%{gemdir}/gems/rack-1.2.5/lib/rack/urlmap.rb
%{gemdir}/gems/rack-1.2.5/lib/rack/utils.rb
%{gemdir}/gems/rack-1.2.5/lib/rack.rb
%{gemdir}/gems/rack-1.2.5/test/cgi/lighttpd.conf
%{gemdir}/gems/rack-1.2.5/test/cgi/rackup_stub.rb
%{gemdir}/gems/rack-1.2.5/test/cgi/sample_rackup.ru
%{gemdir}/gems/rack-1.2.5/test/cgi/test
%{gemdir}/gems/rack-1.2.5/test/cgi/test.fcgi
%{gemdir}/gems/rack-1.2.5/test/cgi/test.ru
%{gemdir}/gems/rack-1.2.5/test/gemloader.rb
%{gemdir}/gems/rack-1.2.5/test/multipart/bad_robots
%{gemdir}/gems/rack-1.2.5/test/multipart/binary
%{gemdir}/gems/rack-1.2.5/test/multipart/empty
%{gemdir}/gems/rack-1.2.5/test/multipart/fail_16384_nofile
%{gemdir}/gems/rack-1.2.5/test/multipart/file1.txt
%{gemdir}/gems/rack-1.2.5/test/multipart/filename_and_modification_param
%{gemdir}/gems/rack-1.2.5/test/multipart/filename_with_escaped_quotes
%{gemdir}/gems/rack-1.2.5/test/multipart/filename_with_escaped_quotes_and_modification_param
%{gemdir}/gems/rack-1.2.5/test/multipart/filename_with_percent_escaped_quotes
%{gemdir}/gems/rack-1.2.5/test/multipart/filename_with_unescaped_quotes
%{gemdir}/gems/rack-1.2.5/test/multipart/ie
%{gemdir}/gems/rack-1.2.5/test/multipart/nested
%{gemdir}/gems/rack-1.2.5/test/multipart/none
%{gemdir}/gems/rack-1.2.5/test/multipart/semicolon
%{gemdir}/gems/rack-1.2.5/test/multipart/text
%{gemdir}/gems/rack-1.2.5/test/rackup/config.ru
%{gemdir}/gems/rack-1.2.5/test/spec_auth_basic.rb
%{gemdir}/gems/rack-1.2.5/test/spec_auth_digest.rb
%{gemdir}/gems/rack-1.2.5/test/spec_builder.rb
%{gemdir}/gems/rack-1.2.5/test/spec_cascade.rb
%{gemdir}/gems/rack-1.2.5/test/spec_cgi.rb
%{gemdir}/gems/rack-1.2.5/test/spec_chunked.rb
%{gemdir}/gems/rack-1.2.5/test/spec_commonlogger.rb
%{gemdir}/gems/rack-1.2.5/test/spec_conditionalget.rb
%{gemdir}/gems/rack-1.2.5/test/spec_config.rb
%{gemdir}/gems/rack-1.2.5/test/spec_content_length.rb
%{gemdir}/gems/rack-1.2.5/test/spec_content_type.rb
%{gemdir}/gems/rack-1.2.5/test/spec_deflater.rb
%{gemdir}/gems/rack-1.2.5/test/spec_directory.rb
%{gemdir}/gems/rack-1.2.5/test/spec_etag.rb
%{gemdir}/gems/rack-1.2.5/test/spec_fastcgi.rb
%{gemdir}/gems/rack-1.2.5/test/spec_file.rb
%{gemdir}/gems/rack-1.2.5/test/spec_handler.rb
%{gemdir}/gems/rack-1.2.5/test/spec_head.rb
%{gemdir}/gems/rack-1.2.5/test/spec_lint.rb
%{gemdir}/gems/rack-1.2.5/test/spec_lobster.rb
%{gemdir}/gems/rack-1.2.5/test/spec_lock.rb
%{gemdir}/gems/rack-1.2.5/test/spec_logger.rb
%{gemdir}/gems/rack-1.2.5/test/spec_methodoverride.rb
%{gemdir}/gems/rack-1.2.5/test/spec_mock.rb
%{gemdir}/gems/rack-1.2.5/test/spec_mongrel.rb
%{gemdir}/gems/rack-1.2.5/test/spec_nulllogger.rb
%{gemdir}/gems/rack-1.2.5/test/spec_recursive.rb
%{gemdir}/gems/rack-1.2.5/test/spec_request.rb
%{gemdir}/gems/rack-1.2.5/test/spec_response.rb
%{gemdir}/gems/rack-1.2.5/test/spec_rewindable_input.rb
%{gemdir}/gems/rack-1.2.5/test/spec_runtime.rb
%{gemdir}/gems/rack-1.2.5/test/spec_sendfile.rb
%{gemdir}/gems/rack-1.2.5/test/spec_session_cookie.rb
%{gemdir}/gems/rack-1.2.5/test/spec_session_memcache.rb
%{gemdir}/gems/rack-1.2.5/test/spec_session_pool.rb
%{gemdir}/gems/rack-1.2.5/test/spec_showexceptions.rb
%{gemdir}/gems/rack-1.2.5/test/spec_showstatus.rb
%{gemdir}/gems/rack-1.2.5/test/spec_static.rb
%{gemdir}/gems/rack-1.2.5/test/spec_thin.rb
%{gemdir}/gems/rack-1.2.5/test/spec_urlmap.rb
%{gemdir}/gems/rack-1.2.5/test/spec_utils.rb
%{gemdir}/gems/rack-1.2.5/test/spec_webrick.rb
%{gemdir}/gems/rack-1.2.5/test/testrequest.rb
%{gemdir}/gems/rack-1.2.5/test/unregistered_handler/rack/handler/unregistered.rb
%{gemdir}/gems/rack-1.2.5/test/unregistered_handler/rack/handler/unregistered_long_one.rb
%{gemdir}/gems/rack-1.2.5/COPYING
%doc %{gemdir}/gems/rack-1.2.5/KNOWN-ISSUES
%{gemdir}/gems/rack-1.2.5/rack.gemspec
%{gemdir}/gems/rack-1.2.5/Rakefile
%doc %{gemdir}/gems/rack-1.2.5/README
%doc %{gemdir}/gems/rack-1.2.5/SPEC
%doc %{gemdir}/doc/rack-1.2.5
%{gemdir}/cache/rack-1.2.5.gem
%{gemdir}/specifications/rack-1.2.5.gemspec

%changelog
* Tue May 08 2012 jmontleo@redhat.com - 1.2.5-4
- Cleaned up spec file
