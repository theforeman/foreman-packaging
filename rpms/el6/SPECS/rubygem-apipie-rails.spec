%define rbname apipie-rails
%define version 0.0.12
%define release 1

Summary: Rails REST API documentation tool
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://github.com/Pajk/apipie-rails
Source0: %{rbname}-%{version}.gem
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
%{gemdir}/gems/apipie-rails-0.0.12/.gitignore
%{gemdir}/gems/apipie-rails-0.0.12/.rspec
%{gemdir}/gems/apipie-rails-0.0.12/.rvmrc
%{gemdir}/gems/apipie-rails-0.0.12/.travis.yml
%{gemdir}/gems/apipie-rails-0.0.12/APACHE-LICENSE-2.0
%{gemdir}/gems/apipie-rails-0.0.12/Gemfile
%{gemdir}/gems/apipie-rails-0.0.12/Gemfile.lock
%{gemdir}/gems/apipie-rails-0.0.12/MIT-LICENSE
%{gemdir}/gems/apipie-rails-0.0.12/NOTICE
%{gemdir}/gems/apipie-rails-0.0.12/README.rdoc
%{gemdir}/gems/apipie-rails-0.0.12/Rakefile
%{gemdir}/gems/apipie-rails-0.0.12/apipie-rails.gemspec
%{gemdir}/gems/apipie-rails-0.0.12/app/
%{gemdir}/gems/apipie-rails-0.0.12/lib/
%{gemdir}/gems/apipie-rails-0.0.12/rel-eng/packages/.readme
%{gemdir}/gems/apipie-rails-0.0.12/rel-eng/packages/rubygem-apipie-rails
%{gemdir}/gems/apipie-rails-0.0.12/rel-eng/tito.props
%{gemdir}/gems/apipie-rails-0.0.12/rubygem-apipie-rails.spec
%{gemdir}/gems/apipie-rails-0.0.12/spec/

%doc %{gemdir}/doc/apipie-rails-0.0.12
%{gemdir}/cache/apipie-rails-0.0.12.gem
%{gemdir}/specifications/apipie-rails-0.0.12.gemspec

%changelog

