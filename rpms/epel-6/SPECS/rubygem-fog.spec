%define rbname fog
%define version 1.9.0
%define release 1

Summary: brings clouds to you
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://github.com/fog/fog
Source0: http://rubygems.org/downloads/%{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.8.10
Requires: rubygem-builder 
Requires: rubygem-excon >= 0.14.0
Requires: rubygem-formatador => 0.2.0
Requires: rubygem-formatador < 0.3
Requires: rubygem-multi_json => 1.0
Requires: rubygem-multi_json < 2
Requires: rubygem-mime-types 
Requires: rubygem-net-scp => 1.0.4
Requires: rubygem-net-scp < 1.1
Requires: rubygem-net-ssh >= 2.1.3
Requires: rubygem-nokogiri => 1.5.0
Requires: rubygem-nokogiri < 1.6
Requires: rubygem-ruby-hmac 
BuildRequires: ruby 
BuildRequires: rubygems >= 1.8.10
BuildArch: noarch
Provides: rubygem(fog) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
The Ruby cloud services library. Supports all major cloud providers including
AWS, Rackspace, Linode, Blue Box, StormOnDemand, and many others. Full support
for most AWS services including EC2, S3, CloudWatch, SimpleDB, ELB, and RDS.


%prep
%setup -T -c

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{gembuilddir}
gem install --local --install-dir %{gembuilddir} --force %{SOURCE0} --no-rdoc --no-ri 
mkdir -p %{buildroot}/%{_bindir}
mv %{gembuilddir}/bin/* %{buildroot}/%{_bindir}
rmdir %{gembuilddir}/bin

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%{_bindir}/fog
%{gemdir}/gems/%{rbname}-%{version}/.document
%{gemdir}/gems/%{rbname}-%{version}/.gitignore
%{gemdir}/gems/%{rbname}-%{version}/Gemfile
%{gemdir}/gems/%{rbname}-%{version}/Rakefile
%{gemdir}/gems/%{rbname}-%{version}/benchs/fog_vs.rb
%{gemdir}/gems/%{rbname}-%{version}/benchs/params.rb
%{gemdir}/gems/%{rbname}-%{version}/benchs/parse_vs_push.rb
%{gemdir}/gems/%{rbname}-%{version}/bin/fog
%{gemdir}/gems/%{rbname}-%{version}/changelog.txt
%{gemdir}/gems/%{rbname}-%{version}/docs/
%{gemdir}/gems/%{rbname}-%{version}/fog.gemspec
%{gemdir}/gems/%{rbname}-%{version}/lib/
%{gemdir}/gems/%{rbname}-%{version}/tests/
%{gemdir}/gems/%{rbname}-%{version}/.irbrc
%{gemdir}/gems/%{rbname}-%{version}/.travis.yml
%{gemdir}/gems/%{rbname}-%{version}/README.md
%{gemdir}/gems/%{rbname}-%{version}/RELEASE.md

#%doc %{gemdir}/doc/fog-%{version}
%{gemdir}/cache/./fog-%{version}.gem
%{gemdir}/specifications/./fog-%{version}.gemspec

%changelog
* Fri Jan 25 2013 shk@redhat.com 1.9.0-1
- Updated to 1.9.0
