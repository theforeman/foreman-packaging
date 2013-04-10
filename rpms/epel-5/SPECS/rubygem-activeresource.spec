%define rbname activeresource
%define version 3.0.20
%define release 1

Summary: REST modeling framework (part of Rails).
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
Requires: rubygem-activemodel = %{version}

BuildRequires: ruby >= 1.8.7
BuildRequires: rubygems >= 1.8.10
BuildArch: noarch
Provides: rubygem(activeresource) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
REST on Rails. Wrap your RESTful web app with Ruby classes and work with them
like Active Record models.


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
%{gemdir}/gems/activeresource-%{version}/CHANGELOG
%doc %{gemdir}/gems/activeresource-%{version}/README.rdoc
%{gemdir}/gems/activeresource-%{version}/examples/simple.rb
%{gemdir}/gems/activeresource-%{version}/lib/active_resource/base.rb
%{gemdir}/gems/activeresource-%{version}/lib/active_resource/connection.rb
%{gemdir}/gems/activeresource-%{version}/lib/active_resource/custom_methods.rb
%{gemdir}/gems/activeresource-%{version}/lib/active_resource/exceptions.rb
%{gemdir}/gems/activeresource-%{version}/lib/active_resource/formats/json_format.rb
%{gemdir}/gems/activeresource-%{version}/lib/active_resource/formats/xml_format.rb
%{gemdir}/gems/activeresource-%{version}/lib/active_resource/formats.rb
%{gemdir}/gems/activeresource-%{version}/lib/active_resource/http_mock.rb
%{gemdir}/gems/activeresource-%{version}/lib/active_resource/log_subscriber.rb
%{gemdir}/gems/activeresource-%{version}/lib/active_resource/observing.rb
%{gemdir}/gems/activeresource-%{version}/lib/active_resource/railtie.rb
%{gemdir}/gems/activeresource-%{version}/lib/active_resource/schema.rb
%{gemdir}/gems/activeresource-%{version}/lib/active_resource/validations.rb
%{gemdir}/gems/activeresource-%{version}/lib/active_resource/version.rb
%{gemdir}/gems/activeresource-%{version}/lib/active_resource.rb


%doc %{gemdir}/doc/activeresource-%{version}
%{gemdir}/cache/activeresource-%{version}.gem
%{gemdir}/specifications/activeresource-%{version}.gemspec

%changelog
* Mon Feb 4 2013 shk@redhat.com 3.0.20-1
- Updated to 3.0.20
* Fri Jan 25 2013 shk@redhat.com 3.0.19-1
- Updated to 3.0.19
