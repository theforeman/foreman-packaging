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
%{gemdir}/gems/apipie-rails-0.0.12/app/controllers/apipie/apipies_controller.rb
%{gemdir}/gems/apipie-rails-0.0.12/app/public/apipie/javascripts/apipie.js
%{gemdir}/gems/apipie-rails-0.0.12/app/public/apipie/javascripts/bundled/bootstrap-collapse.js
%{gemdir}/gems/apipie-rails-0.0.12/app/public/apipie/javascripts/bundled/bootstrap.js
%{gemdir}/gems/apipie-rails-0.0.12/app/public/apipie/javascripts/bundled/jquery-1.7.2.js
%{gemdir}/gems/apipie-rails-0.0.12/app/public/apipie/javascripts/bundled/prettify.js
%{gemdir}/gems/apipie-rails-0.0.12/app/public/apipie/stylesheets/application.css
%{gemdir}/gems/apipie-rails-0.0.12/app/public/apipie/stylesheets/bundled/bootstrap-responsive.min.css
%{gemdir}/gems/apipie-rails-0.0.12/app/public/apipie/stylesheets/bundled/bootstrap.min.css
%{gemdir}/gems/apipie-rails-0.0.12/app/public/apipie/stylesheets/bundled/prettify.css
%{gemdir}/gems/apipie-rails-0.0.12/app/views/apipie/apipies/_params.html.erb
%{gemdir}/gems/apipie-rails-0.0.12/app/views/apipie/apipies/_params_plain.html.erb
%{gemdir}/gems/apipie-rails-0.0.12/app/views/apipie/apipies/index.html.erb
%{gemdir}/gems/apipie-rails-0.0.12/app/views/apipie/apipies/method.html.erb
%{gemdir}/gems/apipie-rails-0.0.12/app/views/apipie/apipies/plain.html.erb
%{gemdir}/gems/apipie-rails-0.0.12/app/views/apipie/apipies/resource.html.erb
%{gemdir}/gems/apipie-rails-0.0.12/app/views/apipie/apipies/static.html.erb
%{gemdir}/gems/apipie-rails-0.0.12/app/views/layouts/apipie/apipie.html.erb
%{gemdir}/gems/apipie-rails-0.0.12/lib/apipie-rails.rb
%{gemdir}/gems/apipie-rails-0.0.12/lib/apipie/apipie_module.rb
%{gemdir}/gems/apipie-rails-0.0.12/lib/apipie/application.rb
%{gemdir}/gems/apipie-rails-0.0.12/lib/apipie/client/generator.rb
%{gemdir}/gems/apipie-rails-0.0.12/lib/apipie/client/template/Gemfile.tt
%{gemdir}/gems/apipie-rails-0.0.12/lib/apipie/client/template/README.tt
%{gemdir}/gems/apipie-rails-0.0.12/lib/apipie/client/template/Rakefile.tt
%{gemdir}/gems/apipie-rails-0.0.12/lib/apipie/client/template/base.rb.tt
%{gemdir}/gems/apipie-rails-0.0.12/lib/apipie/client/template/bin.rb.tt
%{gemdir}/gems/apipie-rails-0.0.12/lib/apipie/client/template/cli.rb.tt
%{gemdir}/gems/apipie-rails-0.0.12/lib/apipie/client/template/cli_command.rb.tt
%{gemdir}/gems/apipie-rails-0.0.12/lib/apipie/client/template/client.gemspec.tt
%{gemdir}/gems/apipie-rails-0.0.12/lib/apipie/client/template/client.rb.tt
%{gemdir}/gems/apipie-rails-0.0.12/lib/apipie/client/template/resource.rb.tt
%{gemdir}/gems/apipie-rails-0.0.12/lib/apipie/client/template/rest_client_oauth.rb.tt
%{gemdir}/gems/apipie-rails-0.0.12/lib/apipie/client/template/version.rb.tt
%{gemdir}/gems/apipie-rails-0.0.12/lib/apipie/dsl_definition.rb
%{gemdir}/gems/apipie-rails-0.0.12/lib/apipie/error_description.rb
%{gemdir}/gems/apipie-rails-0.0.12/lib/apipie/extractor.rb
%{gemdir}/gems/apipie-rails-0.0.12/lib/apipie/extractor/collector.rb
%{gemdir}/gems/apipie-rails-0.0.12/lib/apipie/extractor/recorder.rb
%{gemdir}/gems/apipie-rails-0.0.12/lib/apipie/extractor/writer.rb
%{gemdir}/gems/apipie-rails-0.0.12/lib/apipie/helpers.rb
%{gemdir}/gems/apipie-rails-0.0.12/lib/apipie/markup.rb
%{gemdir}/gems/apipie-rails-0.0.12/lib/apipie/method_description.rb
%{gemdir}/gems/apipie-rails-0.0.12/lib/apipie/param_description.rb
%{gemdir}/gems/apipie-rails-0.0.12/lib/apipie/railtie.rb
%{gemdir}/gems/apipie-rails-0.0.12/lib/apipie/resource_description.rb
%{gemdir}/gems/apipie-rails-0.0.12/lib/apipie/routing.rb
%{gemdir}/gems/apipie-rails-0.0.12/lib/apipie/static_dispatcher.rb
%{gemdir}/gems/apipie-rails-0.0.12/lib/apipie/validator.rb
%{gemdir}/gems/apipie-rails-0.0.12/lib/apipie/version.rb
%{gemdir}/gems/apipie-rails-0.0.12/lib/tasks/apipie.rake
%{gemdir}/gems/apipie-rails-0.0.12/rel-eng/packages/.readme
%{gemdir}/gems/apipie-rails-0.0.12/rel-eng/packages/rubygem-apipie-rails
%{gemdir}/gems/apipie-rails-0.0.12/rel-eng/tito.props
%{gemdir}/gems/apipie-rails-0.0.12/rubygem-apipie-rails.spec
%{gemdir}/gems/apipie-rails-0.0.12/spec/controllers/apipies_controller_spec.rb
%{gemdir}/gems/apipie-rails-0.0.12/spec/controllers/users_controller_spec.rb
%{gemdir}/gems/apipie-rails-0.0.12/spec/dummy/Rakefile
%{gemdir}/gems/apipie-rails-0.0.12/spec/dummy/app/controllers/application_controller.rb
%{gemdir}/gems/apipie-rails-0.0.12/spec/dummy/app/controllers/twitter_example_controller.rb
%{gemdir}/gems/apipie-rails-0.0.12/spec/dummy/app/controllers/users_controller.rb
%{gemdir}/gems/apipie-rails-0.0.12/spec/dummy/app/views/layouts/application.html.erb
%{gemdir}/gems/apipie-rails-0.0.12/spec/dummy/config.ru
%{gemdir}/gems/apipie-rails-0.0.12/spec/dummy/config/application.rb
%{gemdir}/gems/apipie-rails-0.0.12/spec/dummy/config/boot.rb
%{gemdir}/gems/apipie-rails-0.0.12/spec/dummy/config/database.yml
%{gemdir}/gems/apipie-rails-0.0.12/spec/dummy/config/environment.rb
%{gemdir}/gems/apipie-rails-0.0.12/spec/dummy/config/environments/development.rb
%{gemdir}/gems/apipie-rails-0.0.12/spec/dummy/config/environments/production.rb
%{gemdir}/gems/apipie-rails-0.0.12/spec/dummy/config/environments/test.rb
%{gemdir}/gems/apipie-rails-0.0.12/spec/dummy/config/initializers/apipie.rb
%{gemdir}/gems/apipie-rails-0.0.12/spec/dummy/config/initializers/backtrace_silencers.rb
%{gemdir}/gems/apipie-rails-0.0.12/spec/dummy/config/initializers/inflections.rb
%{gemdir}/gems/apipie-rails-0.0.12/spec/dummy/config/initializers/mime_types.rb
%{gemdir}/gems/apipie-rails-0.0.12/spec/dummy/config/initializers/secret_token.rb
%{gemdir}/gems/apipie-rails-0.0.12/spec/dummy/config/initializers/session_store.rb
%{gemdir}/gems/apipie-rails-0.0.12/spec/dummy/config/locales/en.yml
%{gemdir}/gems/apipie-rails-0.0.12/spec/dummy/config/routes.rb
%{gemdir}/gems/apipie-rails-0.0.12/spec/dummy/db/.gitkeep
%{gemdir}/gems/apipie-rails-0.0.12/spec/dummy/doc/apipie_examples.yml
%{gemdir}/gems/apipie-rails-0.0.12/spec/dummy/public/404.html
%{gemdir}/gems/apipie-rails-0.0.12/spec/dummy/public/422.html
%{gemdir}/gems/apipie-rails-0.0.12/spec/dummy/public/500.html
%{gemdir}/gems/apipie-rails-0.0.12/spec/dummy/public/favicon.ico
%{gemdir}/gems/apipie-rails-0.0.12/spec/dummy/public/javascripts/application.js
%{gemdir}/gems/apipie-rails-0.0.12/spec/dummy/public/javascripts/controls.js
%{gemdir}/gems/apipie-rails-0.0.12/spec/dummy/public/javascripts/dragdrop.js
%{gemdir}/gems/apipie-rails-0.0.12/spec/dummy/public/javascripts/effects.js
%{gemdir}/gems/apipie-rails-0.0.12/spec/dummy/public/javascripts/prototype.js
%{gemdir}/gems/apipie-rails-0.0.12/spec/dummy/public/javascripts/rails.js
%{gemdir}/gems/apipie-rails-0.0.12/spec/dummy/public/stylesheets/.gitkeep
%{gemdir}/gems/apipie-rails-0.0.12/spec/dummy/script/rails
%{gemdir}/gems/apipie-rails-0.0.12/spec/spec_helper.rb


%doc %{gemdir}/doc/apipie-rails-0.0.12
%{gemdir}/cache/apipie-rails-0.0.12.gem
%{gemdir}/specifications/apipie-rails-0.0.12.gemspec

%changelog

