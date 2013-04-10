%define rbname jquery-rails
%define version 1.0.19
%define release 1

Summary: Use jQuery with Rails 3
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://rubygems.org/gems/jquery-rails
Source0: http://rubygems.org/downloads/%{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.8.10

Requires: rubygem-railties => 3.0
Requires: rubygem-railties < 4

Requires: rubygem-thor => 0.14
Requires: rubygem-thor < 1
BuildRequires: ruby 
BuildRequires: rubygems >= 1.8.10
BuildArch: noarch
Provides: rubygem(jquery-rails) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
This gem provides jQuery and the jQuery-ujs driver for your Rails 3
application.


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
%{gemdir}/gems/jquery-rails-1.0.19/.gitignore
%{gemdir}/gems/jquery-rails-1.0.19/CHANGELOG.md
%{gemdir}/gems/jquery-rails-1.0.19/Gemfile
%{gemdir}/gems/jquery-rails-1.0.19/Gemfile.lock
%{gemdir}/gems/jquery-rails-1.0.19/LICENSE
%{gemdir}/gems/jquery-rails-1.0.19/README.md
%{gemdir}/gems/jquery-rails-1.0.19/Rakefile
%{gemdir}/gems/jquery-rails-1.0.19/jquery-rails.gemspec
%{gemdir}/gems/jquery-rails-1.0.19/lib/generators/jquery/install/install_generator.rb
%{gemdir}/gems/jquery-rails-1.0.19/lib/jquery-rails.rb
%{gemdir}/gems/jquery-rails-1.0.19/lib/jquery/assert_select.rb
%{gemdir}/gems/jquery-rails-1.0.19/lib/jquery/rails.rb
%{gemdir}/gems/jquery-rails-1.0.19/lib/jquery/rails/engine.rb
%{gemdir}/gems/jquery-rails-1.0.19/lib/jquery/rails/railtie.rb
%{gemdir}/gems/jquery-rails-1.0.19/lib/jquery/rails/version.rb
%{gemdir}/gems/jquery-rails-1.0.19/spec/lib/jquery-rails_spec.rb
%{gemdir}/gems/jquery-rails-1.0.19/spec/spec_helper.rb
%{gemdir}/gems/jquery-rails-1.0.19/vendor/assets/javascripts/jquery-ui.js
%{gemdir}/gems/jquery-rails-1.0.19/vendor/assets/javascripts/jquery-ui.min.js
%{gemdir}/gems/jquery-rails-1.0.19/vendor/assets/javascripts/jquery.js
%{gemdir}/gems/jquery-rails-1.0.19/vendor/assets/javascripts/jquery.min.js
%{gemdir}/gems/jquery-rails-1.0.19/vendor/assets/javascripts/jquery_ujs.js


%doc %{gemdir}/doc/jquery-rails-1.0.19
%{gemdir}/cache/jquery-rails-1.0.19.gem
%{gemdir}/specifications/jquery-rails-1.0.19.gemspec

%changelog
