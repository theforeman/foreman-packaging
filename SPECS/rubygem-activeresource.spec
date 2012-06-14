%define rbname activeresource
%define version 3.0.14
%define release 1

Summary: REST modeling framework (part of Rails).
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://www.rubyonrails.org
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 1.8.7
Requires: rubygems >= 1.8.10

Requires: rubygem-activesupport = 3.0.14

Requires: rubygem-activemodel = 3.0.14
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
%{gemdir}/gems/activeresource-3.0.14/CHANGELOG
%doc %{gemdir}/gems/activeresource-3.0.14/README.rdoc
%{gemdir}/gems/activeresource-3.0.14/examples/simple.rb
%{gemdir}/gems/activeresource-3.0.14/lib/active_resource/base.rb
%{gemdir}/gems/activeresource-3.0.14/lib/active_resource/connection.rb
%{gemdir}/gems/activeresource-3.0.14/lib/active_resource/custom_methods.rb
%{gemdir}/gems/activeresource-3.0.14/lib/active_resource/exceptions.rb
%{gemdir}/gems/activeresource-3.0.14/lib/active_resource/formats/json_format.rb
%{gemdir}/gems/activeresource-3.0.14/lib/active_resource/formats/xml_format.rb
%{gemdir}/gems/activeresource-3.0.14/lib/active_resource/formats.rb
%{gemdir}/gems/activeresource-3.0.14/lib/active_resource/http_mock.rb
%{gemdir}/gems/activeresource-3.0.14/lib/active_resource/log_subscriber.rb
%{gemdir}/gems/activeresource-3.0.14/lib/active_resource/observing.rb
%{gemdir}/gems/activeresource-3.0.14/lib/active_resource/railtie.rb
%{gemdir}/gems/activeresource-3.0.14/lib/active_resource/schema.rb
%{gemdir}/gems/activeresource-3.0.14/lib/active_resource/validations.rb
%{gemdir}/gems/activeresource-3.0.14/lib/active_resource/version.rb
%{gemdir}/gems/activeresource-3.0.14/lib/active_resource.rb


%doc %{gemdir}/doc/activeresource-3.0.14
%{gemdir}/cache/activeresource-3.0.14.gem
%{gemdir}/specifications/activeresource-3.0.14.gemspec

%changelog
