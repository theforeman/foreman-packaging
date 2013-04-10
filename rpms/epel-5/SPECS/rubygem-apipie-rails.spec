%define rbname apipie-rails
%define version 0.0.13
%define release 1

Summary: Rails REST API documentation tool
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://github.com/Pajk/apipie-rails
Source0: http://rubygems.org/downloads/%{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.8.10
BuildRequires: ruby 
BuildRequires: rubygems >= 1.8.10
BuildArch: noarch
Provides: rubygem(apipie-rails) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
Maintain your API documentation up to date!


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
%{gemdir}/gems/apipie-rails-%{version}/.gitignore
%{gemdir}/gems/apipie-rails-%{version}/.rspec
%{gemdir}/gems/apipie-rails-%{version}/.rvmrc
%{gemdir}/gems/apipie-rails-%{version}/.travis.yml
%{gemdir}/gems/apipie-rails-%{version}/APACHE-LICENSE-2.0
%{gemdir}/gems/apipie-rails-%{version}/Gemfile
%{gemdir}/gems/apipie-rails-%{version}/Gemfile.lock
%{gemdir}/gems/apipie-rails-%{version}/MIT-LICENSE
%{gemdir}/gems/apipie-rails-%{version}/NOTICE
%{gemdir}/gems/apipie-rails-%{version}/README.rdoc
%{gemdir}/gems/apipie-rails-%{version}/Rakefile
%{gemdir}/gems/apipie-rails-%{version}/apipie-rails.gemspec
%{gemdir}/gems/apipie-rails-%{version}/app/
%{gemdir}/gems/apipie-rails-%{version}/lib/
%{gemdir}/gems/apipie-rails-%{version}/rel-eng/packages/.readme
%{gemdir}/gems/apipie-rails-%{version}/rel-eng/packages/rubygem-apipie-rails
%{gemdir}/gems/apipie-rails-%{version}/rel-eng/tito.props
%{gemdir}/gems/apipie-rails-%{version}/rubygem-apipie-rails.spec
%{gemdir}/gems/apipie-rails-%{version}/spec/

%doc %{gemdir}/doc/apipie-rails-%{version}
%{gemdir}/cache/apipie-rails-%{version}.gem
%{gemdir}/specifications/apipie-rails-%{version}.gemspec

%changelog

