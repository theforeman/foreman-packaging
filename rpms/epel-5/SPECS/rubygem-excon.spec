%define rbname excon
%define version 0.14.0
%define release 1

Summary: speed, persistence, http(s)
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: https://github.com/geemus/excon
Source0: http://rubygems.org/downloads/%{rbname}-%{version}.gem
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
%{gemdir}/gems/excon-0.14.0/Gemfile
%doc %{gemdir}/gems/excon-0.14.0/README.md
%{gemdir}/gems/excon-0.14.0/Rakefile
%{gemdir}/gems/excon-0.14.0/benchmarks
%{gemdir}/gems/excon-0.14.0/changelog.txt
%{gemdir}/gems/excon-0.14.0/data/cacert.pem
%{gemdir}/gems/excon-0.14.0/excon.gemspec
%{gemdir}/gems/excon-0.14.0/lib/
%{gemdir}/gems/excon-0.14.0/tests

%doc %{gemdir}/doc/excon-0.14.0
%{gemdir}/cache/excon-0.14.0.gem
%{gemdir}/specifications/excon-0.14.0.gemspec

%changelog
