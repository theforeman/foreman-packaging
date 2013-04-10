%define rbname ffi
%define version 1.0.11
%define release 1

Summary: Ruby-FFI is a ruby extension for programmatically loading dynamic libraries, binding functions within them, and calling those functions from Ruby code
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://wiki.github.com/ffi/ffi
Source0: http://rubygems.org/downloads/%{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.8.10
BuildRequires: ruby 
BuildRequires: rubygems >= 1.8.10
BuildRequires: libffi-devel
BuildRequires: ruby-devel
BuildRequires: gcc
Provides: rubygem(ffi) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
Ruby-FFI is a ruby extension for programmatically loading dynamic
libraries, binding functions within them, and calling those functions
from Ruby code. Moreover, a Ruby-FFI extension works without changes
on Ruby and JRuby. Discover why should you write your next extension
using Ruby-FFI here[http://wiki.github.com/ffi/ffi/why-use-ffi].


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
%doc %{gemdir}/gems/ffi-1.0.11/History.txt
%{gemdir}/gems/ffi-1.0.11/LICENSE
%doc %{gemdir}/gems/ffi-1.0.11/README.rdoc
%{gemdir}/gems/ffi-1.0.11/Rakefile
%{gemdir}/gems/ffi-1.0.11/ext/
%{gemdir}/gems/ffi-1.0.11/gen/Rakefile
%{gemdir}/gems/ffi-1.0.11/lib/
%{gemdir}/gems/ffi-1.0.11/spec/
%{gemdir}/gems/ffi-1.0.11/tasks/
%doc %{gemdir}/doc/ffi-1.0.11/
%{gemdir}/specifications/ffi-1.0.11.gemspec
%{gemdir}/cache/ffi-1.0.11.gem
%changelog
