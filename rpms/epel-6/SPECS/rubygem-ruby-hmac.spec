%define rbname ruby-hmac
%define version 0.4.0
%define release 1

Summary: This module provides common interface to HMAC functionality
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://ruby-hmac.rubyforge.org
Source0: http://rubygems.org/downloads/%{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.8.10
BuildRequires: ruby 
BuildRequires: rubygems >= 1.8.10
BuildArch: noarch
Provides: rubygem(ruby-hmac) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
This module provides common interface to HMAC functionality. HMAC is a kind of
"Message Authentication Code" (MAC) algorithm whose standard is documented in
RFC2104. Namely, a MAC provides a way to check the integrity of information
transmitted over or stored in an unreliable medium, based on a secret key.
Originally written by Daiki Ueno. Converted to a RubyGem by Geoffrey
Grosenbach


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
%doc %{gemdir}/gems/ruby-hmac-0.4.0/History.txt
%doc %{gemdir}/gems/ruby-hmac-0.4.0/Manifest.txt
%doc %{gemdir}/gems/ruby-hmac-0.4.0/README.txt
%{gemdir}/gems/ruby-hmac-0.4.0/Rakefile
%{gemdir}/gems/ruby-hmac-0.4.0/lib/hmac-md5.rb
%{gemdir}/gems/ruby-hmac-0.4.0/lib/hmac-rmd160.rb
%{gemdir}/gems/ruby-hmac-0.4.0/lib/hmac-sha1.rb
%{gemdir}/gems/ruby-hmac-0.4.0/lib/hmac-sha2.rb
%{gemdir}/gems/ruby-hmac-0.4.0/lib/hmac.rb
%{gemdir}/gems/ruby-hmac-0.4.0/lib/ruby_hmac.rb
%{gemdir}/gems/ruby-hmac-0.4.0/test/test_hmac.rb


%doc %{gemdir}/doc/ruby-hmac-0.4.0
%{gemdir}/cache/ruby-hmac-0.4.0.gem
%{gemdir}/specifications/ruby-hmac-0.4.0.gemspec

%changelog
