%define rbname rails
%define version 3.2.13
%define release 1

Summary: Full-stack web application framework.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://www.rubyonrails.org
Source0: http://rubygems.org/downloads/%{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root

Requires: ruby >= 1.8.7
Requires: rubygems >= 1.8.10
Requires: rubygem-activesupport = %{version}
Requires: rubygem-actionpack = %{version}
Requires: rubygem-activerecord = %{version}
Requires: rubygem-activeresource = %{version}
Requires: rubygem-actionmailer = %{version}
Requires: rubygem-railties = %{version}
Requires: rubygem-bundler => 1.0
Requires: rubygem-bundler < 2

BuildRequires: ruby >= 1.8.7
BuildRequires: rubygems >= 1.8.10
BuildRequireS: rubygem-rdoc
BuildArch: noarch

Provides: rubygem(rails) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
Ruby on Rails is a full-stack web framework optimized for programmer happiness
and sustainable productivity. It encourages beautiful code by favoring
convention over configuration.


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


%doc %{gemdir}/doc/rails-%{version}
%{gemdir}/cache/rails-%{version}.gem
%{gemdir}/specifications/rails-%{version}.gemspec

%changelog
* Fri Apr 12 2013 shk@redhat.com 3.2.13-1
- Updated to 3.2.13
* Mon Feb 4 2013 shk@redhat.com 3.0.20-1
- Updated to 3.0.20
* Fri Jan 25 2013 shk@redhat.com 3.0.19-1
- Updated to 3.0.19
