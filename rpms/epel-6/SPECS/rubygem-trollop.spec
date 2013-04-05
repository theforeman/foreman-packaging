%define rbname trollop
%define version 1.16.2
%define release 1

Summary: Trollop is a commandline option parser for Ruby that just gets out of your way.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://trollop.rubyforge.org
Source0: http://rubygems.org/downloads/%{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.8.10
BuildRequires: ruby 
BuildRequires: rubygems >= 1.8.10
BuildArch: noarch
Provides: rubygem(trollop) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
Trollop is a commandline option parser for Ruby that just
gets out of your way. One line of code per option is all you need to write.
For that, you get a nice automatically-generated help page, robust option
parsing, command subcompletion, and sensible defaults for everything you don't
specify.


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
%{gemdir}/gems/trollop-1.16.2/lib/trollop.rb
%{gemdir}/gems/trollop-1.16.2/test/test_trollop.rb
%{gemdir}/gems/trollop-1.16.2/README.txt
%{gemdir}/gems/trollop-1.16.2/release-script.txt
%{gemdir}/gems/trollop-1.16.2/FAQ.txt
%{gemdir}/gems/trollop-1.16.2/History.txt


%doc %{gemdir}/doc/trollop-1.16.2
%{gemdir}/cache/trollop-1.16.2.gem
%{gemdir}/specifications/trollop-1.16.2.gemspec

%changelog
