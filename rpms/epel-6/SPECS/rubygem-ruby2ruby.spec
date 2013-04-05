%define rbname ruby2ruby
%define version 2.0.1
%define release 1

Summary: ruby2ruby provides a means of generating pure ruby code easily from RubyParser compatible Sexps
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: https://github.com/seattlerb/ruby2ruby
Source0: http://rubygems.org/downloads/%{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.8.10

Requires: rubygem-sexp_processor => 4.1.2

Requires: rubygem-ruby_parser => 3.0.1
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
%{gemdir}/gems/ruby2ruby-%{version}/.autotest
%doc %{gemdir}/gems/ruby2ruby-%{version}/History.txt
%doc %{gemdir}/gems/ruby2ruby-%{version}/Manifest.txt
%doc %{gemdir}/gems/ruby2ruby-%{version}/README.txt
%{gemdir}/gems/ruby2ruby-%{version}/Rakefile
%{gemdir}/gems/ruby2ruby-%{version}/bin/r2r_show
%{gemdir}/gems/ruby2ruby-%{version}/lib/ruby2ruby.rb
%{gemdir}/gems/ruby2ruby-%{version}/test/test_ruby2ruby.rb
%{gemdir}/gems/ruby2ruby-%{version}/.gemtest


%doc %{gemdir}/doc/ruby2ruby-%{version}
%{gemdir}/cache/ruby2ruby-%{version}.gem
%{gemdir}/specifications/ruby2ruby-%{version}.gemspec

%changelog
