%define rbname ruby2ruby
%define version 1.3.1
%define release 1

Summary: ruby2ruby provides a means of generating pure ruby code easily from RubyParser compatible Sexps
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: https://github.com/seattlerb/ruby2ruby
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.8.10

Requires: rubygem-sexp_processor => 3.0
Requires: rubygem-sexp_processor < 4

Requires: rubygem-ruby_parser => 2.0
Requires: rubygem-ruby_parser < 3
BuildRequires: ruby 
BuildRequires: rubygems >= 1.8.10
BuildArch: noarch
Provides: rubygem(ruby2ruby) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
ruby2ruby provides a means of generating pure ruby code easily from
RubyParser compatible Sexps. This makes making dynamic language
processors in ruby easier than ever!


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
%{_bindir}/r2r_show
%{gemdir}/gems/ruby2ruby-1.3.1/.autotest
%doc %{gemdir}/gems/ruby2ruby-1.3.1/History.txt
%doc %{gemdir}/gems/ruby2ruby-1.3.1/Manifest.txt
%doc %{gemdir}/gems/ruby2ruby-1.3.1/README.txt
%{gemdir}/gems/ruby2ruby-1.3.1/Rakefile
%{gemdir}/gems/ruby2ruby-1.3.1/bin/r2r_show
%{gemdir}/gems/ruby2ruby-1.3.1/lib/ruby2ruby.rb
%{gemdir}/gems/ruby2ruby-1.3.1/test/test_ruby2ruby.rb
%{gemdir}/gems/ruby2ruby-1.3.1/.gemtest


%doc %{gemdir}/doc/ruby2ruby-1.3.1
%{gemdir}/cache/ruby2ruby-1.3.1.gem
%{gemdir}/specifications/ruby2ruby-1.3.1.gemspec

%changelog
