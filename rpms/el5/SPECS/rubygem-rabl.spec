%define rbname rabl
%define version 0.7.0
%define release 1

Summary: General ruby templating with json, bson, xml and msgpack support
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: https://github.com/nesquena/rabl
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.8.10

Requires: rubygem-activesupport >= 2.3.14

Requires: rubygem-multi_json => 1.0
Requires: rubygem-multi_json < 2
BuildRequires: ruby 
BuildRequires: rubygems >= 1.8.10
BuildArch: noarch
Provides: rubygem(rabl) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
General ruby templating with json, bson, xml and msgpack support


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
%{gemdir}/gems/rabl-0.7.0/.gitignore
%{gemdir}/gems/rabl-0.7.0/.travis.yml
%{gemdir}/gems/rabl-0.7.0/CHANGELOG.md
%{gemdir}/gems/rabl-0.7.0/Gemfile
%{gemdir}/gems/rabl-0.7.0/Gemfile.ci
%{gemdir}/gems/rabl-0.7.0/MIT-LICENSE
%{gemdir}/gems/rabl-0.7.0/README.md
%{gemdir}/gems/rabl-0.7.0/Rakefile
%{gemdir}/gems/rabl-0.7.0/TODO
%{gemdir}/gems/rabl-0.7.0/examples/base.json.rabl
%{gemdir}/gems/rabl-0.7.0/examples/demo.json.rabl
%{gemdir}/gems/rabl-0.7.0/examples/inherited.json.rabl
%{gemdir}/gems/rabl-0.7.0/fixtures/ashared/NOTES
%{gemdir}/gems/rabl-0.7.0/fixtures/ashared/README
%{gemdir}/gems/rabl-0.7.0/fixtures/ashared/migrate/20111002092016_create_users.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/ashared/migrate/20111002092019_create_posts.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/ashared/migrate/20111002092024_create_phone_numbers.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/ashared/models/phone_number.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/ashared/models/post.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/ashared/models/user.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/ashared/views/layouts/application.html.erb
%{gemdir}/gems/rabl-0.7.0/fixtures/ashared/views/posts/_show_footer_script.js.erb
%{gemdir}/gems/rabl-0.7.0/fixtures/ashared/views/posts/date.rabl
%{gemdir}/gems/rabl-0.7.0/fixtures/ashared/views/posts/index.rabl
%{gemdir}/gems/rabl-0.7.0/fixtures/ashared/views/posts/show.rabl
%{gemdir}/gems/rabl-0.7.0/fixtures/ashared/views/users/index.json.rabl
%{gemdir}/gems/rabl-0.7.0/fixtures/ashared/views/users/phone_number.json.rabl
%{gemdir}/gems/rabl-0.7.0/fixtures/ashared/views/users/show.json.rabl
%{gemdir}/gems/rabl-0.7.0/fixtures/ashared/views_rails_3/layouts/application.html.erb
%{gemdir}/gems/rabl-0.7.0/fixtures/ashared/views_rails_3/posts/_show_footer_script.js.erb
%{gemdir}/gems/rabl-0.7.0/fixtures/ashared/views_rails_3/posts/date.rabl
%{gemdir}/gems/rabl-0.7.0/fixtures/ashared/views_rails_3/posts/index.html.erb
%{gemdir}/gems/rabl-0.7.0/fixtures/ashared/views_rails_3/posts/index.rabl
%{gemdir}/gems/rabl-0.7.0/fixtures/ashared/views_rails_3/posts/show.html.erb
%{gemdir}/gems/rabl-0.7.0/fixtures/ashared/views_rails_3/posts/show.rabl
%{gemdir}/gems/rabl-0.7.0/fixtures/ashared/views_rails_3/posts/show.rabl_test_v1.rabl
%{gemdir}/gems/rabl-0.7.0/fixtures/ashared/views_rails_3/users/index.json.rabl
%{gemdir}/gems/rabl-0.7.0/fixtures/ashared/views_rails_3/users/phone_number.json.rabl
%{gemdir}/gems/rabl-0.7.0/fixtures/ashared/views_rails_3/users/phone_number.xml.rabl
%{gemdir}/gems/rabl-0.7.0/fixtures/ashared/views_rails_3/users/show.json.rabl
%{gemdir}/gems/rabl-0.7.0/fixtures/ashared/views_rails_3/users/show.rabl_test_v1.rabl
%{gemdir}/gems/rabl-0.7.0/fixtures/padrino_test/.components
%{gemdir}/gems/rabl-0.7.0/fixtures/padrino_test/.gitignore
%{gemdir}/gems/rabl-0.7.0/fixtures/padrino_test/Gemfile
%{gemdir}/gems/rabl-0.7.0/fixtures/padrino_test/Rakefile
%{gemdir}/gems/rabl-0.7.0/fixtures/padrino_test/app/app.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/padrino_test/app/controllers/posts.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/padrino_test/app/controllers/users.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/padrino_test/app/helpers/posts_helper.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/padrino_test/app/helpers/users_helper.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/padrino_test/config.ru
%{gemdir}/gems/rabl-0.7.0/fixtures/padrino_test/config/apps.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/padrino_test/config/boot.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/padrino_test/config/database.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/padrino_test/db/schema.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/padrino_test/public/favicon.ico
%{gemdir}/gems/rabl-0.7.0/fixtures/padrino_test/test/app/controllers/posts_controller_test.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/padrino_test/test/app/controllers/users_controller_test.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/padrino_test/test/test.rake
%{gemdir}/gems/rabl-0.7.0/fixtures/padrino_test/test/test_config.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails2/.gitignore
%{gemdir}/gems/rabl-0.7.0/fixtures/rails2/Gemfile
%{gemdir}/gems/rabl-0.7.0/fixtures/rails2/Rakefile
%{gemdir}/gems/rabl-0.7.0/fixtures/rails2/app/controllers/application_controller.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails2/app/controllers/posts_controller.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails2/app/controllers/users_controller.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails2/app/helpers/application_helper.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails2/app/helpers/posts_helper.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails2/app/helpers/users_helper.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails2/config/boot.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails2/config/database.yml
%{gemdir}/gems/rabl-0.7.0/fixtures/rails2/config/environment.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails2/config/environments/development.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails2/config/environments/production.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails2/config/environments/test.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails2/config/initializers/backtrace_silencers.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails2/config/initializers/cookie_verification_secret.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails2/config/initializers/inflections.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails2/config/initializers/mime_types.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails2/config/initializers/new_rails_defaults.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails2/config/initializers/session_store.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails2/config/locales/en.yml
%{gemdir}/gems/rabl-0.7.0/fixtures/rails2/config/preinitializer.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails2/config/routes.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails2/db/schema.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails2/db/seeds.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails2/public/404.html
%{gemdir}/gems/rabl-0.7.0/fixtures/rails2/public/422.html
%{gemdir}/gems/rabl-0.7.0/fixtures/rails2/public/500.html
%{gemdir}/gems/rabl-0.7.0/fixtures/rails2/public/favicon.ico
%{gemdir}/gems/rabl-0.7.0/fixtures/rails2/public/images/rails.png
%{gemdir}/gems/rabl-0.7.0/fixtures/rails2/public/index.html
%{gemdir}/gems/rabl-0.7.0/fixtures/rails2/public/robots.txt
%{gemdir}/gems/rabl-0.7.0/fixtures/rails2/script/about
%{gemdir}/gems/rabl-0.7.0/fixtures/rails2/script/console
%{gemdir}/gems/rabl-0.7.0/fixtures/rails2/script/dbconsole
%{gemdir}/gems/rabl-0.7.0/fixtures/rails2/script/destroy
%{gemdir}/gems/rabl-0.7.0/fixtures/rails2/script/generate
%{gemdir}/gems/rabl-0.7.0/fixtures/rails2/script/performance/benchmarker
%{gemdir}/gems/rabl-0.7.0/fixtures/rails2/script/performance/profiler
%{gemdir}/gems/rabl-0.7.0/fixtures/rails2/script/plugin
%{gemdir}/gems/rabl-0.7.0/fixtures/rails2/script/runner
%{gemdir}/gems/rabl-0.7.0/fixtures/rails2/script/server
%{gemdir}/gems/rabl-0.7.0/fixtures/rails2/test/functionals/posts_controller_test.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails2/test/functionals/users_controller_test.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails2/test/test_helper.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3/.gitignore
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3/Gemfile
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3/Rakefile
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3/app/controllers/application_controller.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3/app/controllers/posts_controller.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3/app/controllers/users_controller.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3/config.ru
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3/config/application.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3/config/boot.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3/config/database.yml
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3/config/environment.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3/config/environments/development.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3/config/environments/production.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3/config/environments/test.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3/config/initializers/backtrace_silencers.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3/config/initializers/inflections.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3/config/initializers/mime_types.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3/config/initializers/secret_token.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3/config/initializers/session_store.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3/config/locales/en.yml
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3/config/routes.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3/db/seeds.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3/lib/tasks/.gitkeep
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3/public/404.html
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3/public/422.html
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3/public/500.html
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3/public/favicon.ico
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3/public/images/rails.png
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3/public/index.html
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3/public/robots.txt
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3/public/stylesheets/.gitkeep
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3/script/rails
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3/test/functional/posts_controller_test.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3/test/functional/users_controller_test.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3/test/test_helper.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/.gitignore
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/Gemfile
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/README.rdoc
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/Rakefile
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/app/assets/images/rails.png
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/app/assets/javascripts/application.js
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/app/assets/javascripts/posts.js.coffee
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/app/assets/javascripts/users.js.coffee
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/app/assets/stylesheets/application.css
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/app/assets/stylesheets/posts.css.scss
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/app/assets/stylesheets/users.css.scss
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/app/controllers/application_controller.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/app/controllers/posts_controller.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/app/controllers/users_controller.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/app/helpers/application_helper.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/app/helpers/posts_helper.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/app/helpers/users_helper.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/app/mailers/.gitkeep
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/config.ru
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/config/application.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/config/boot.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/config/database.yml
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/config/environment.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/config/environments/development.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/config/environments/production.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/config/environments/test.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/config/initializers/backtrace_silencers.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/config/initializers/inflections.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/config/initializers/mime_types.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/config/initializers/secret_token.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/config/initializers/session_store.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/config/initializers/wrap_parameters.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/config/locales/en.yml
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/config/routes.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/db/schema.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/db/seeds.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/doc/README_FOR_APP
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/lib/assets/.gitkeep
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/lib/tasks/.gitkeep
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/log/.gitkeep
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/public/404.html
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/public/422.html
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/public/500.html
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/public/favicon.ico
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/public/index.html
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/public/robots.txt
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/script/rails
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/test/fixtures/.gitkeep
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/test/fixtures/phone_numbers.yml
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/test/fixtures/posts.yml
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/test/fixtures/users.yml
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/test/functional/.gitkeep
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/test/functional/posts_controller_test.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/test/functional/users_controller_test.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/test/integration/.gitkeep
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/test/performance/browsing_test.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/test/test_helper.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/test/unit/.gitkeep
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/test/unit/helpers/posts_helper_test.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/test/unit/helpers/users_helper_test.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/test/unit/phone_number_test.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/test/unit/post_test.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/test/unit/user_test.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/vendor/assets/javascripts/.gitkeep
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/vendor/assets/stylesheets/.gitkeep
%{gemdir}/gems/rabl-0.7.0/fixtures/rails3_2/vendor/plugins/.gitkeep
%{gemdir}/gems/rabl-0.7.0/fixtures/sinatra_test/Gemfile
%{gemdir}/gems/rabl-0.7.0/fixtures/sinatra_test/Rakefile
%{gemdir}/gems/rabl-0.7.0/fixtures/sinatra_test/app.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/sinatra_test/config.ru
%{gemdir}/gems/rabl-0.7.0/fixtures/sinatra_test/test/functional/posts_controller_test.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/sinatra_test/test/functional/users_controller_test.rb
%{gemdir}/gems/rabl-0.7.0/fixtures/sinatra_test/test/test_helper.rb
%{gemdir}/gems/rabl-0.7.0/lib/rabl.rb
%{gemdir}/gems/rabl-0.7.0/lib/rabl/builder.rb
%{gemdir}/gems/rabl-0.7.0/lib/rabl/cache_engine.rb
%{gemdir}/gems/rabl-0.7.0/lib/rabl/configuration.rb
%{gemdir}/gems/rabl-0.7.0/lib/rabl/engine.rb
%{gemdir}/gems/rabl-0.7.0/lib/rabl/helpers.rb
%{gemdir}/gems/rabl-0.7.0/lib/rabl/partials.rb
%{gemdir}/gems/rabl-0.7.0/lib/rabl/railtie.rb
%{gemdir}/gems/rabl-0.7.0/lib/rabl/renderer.rb
%{gemdir}/gems/rabl-0.7.0/lib/rabl/template.rb
%{gemdir}/gems/rabl-0.7.0/lib/rabl/version.rb
%{gemdir}/gems/rabl-0.7.0/rabl.gemspec
%{gemdir}/gems/rabl-0.7.0/test.watchr
%{gemdir}/gems/rabl-0.7.0/test/bson_engine_test.rb
%{gemdir}/gems/rabl-0.7.0/test/builder_test.rb
%{gemdir}/gems/rabl-0.7.0/test/configuration_test.rb
%{gemdir}/gems/rabl-0.7.0/test/engine_test.rb
%{gemdir}/gems/rabl-0.7.0/test/helpers_test.rb
%{gemdir}/gems/rabl-0.7.0/test/integration/posts_controller_test.rb
%{gemdir}/gems/rabl-0.7.0/test/integration/rails3_2/posts_controller_test.rb
%{gemdir}/gems/rabl-0.7.0/test/integration/rails3_2/users_controller_test.rb
%{gemdir}/gems/rabl-0.7.0/test/integration/test_init.rb
%{gemdir}/gems/rabl-0.7.0/test/integration/users_controller_test.rb
%{gemdir}/gems/rabl-0.7.0/test/models/ormless.rb
%{gemdir}/gems/rabl-0.7.0/test/models/user.rb
%{gemdir}/gems/rabl-0.7.0/test/msgpack_engine_test.rb
%{gemdir}/gems/rabl-0.7.0/test/partials_test.rb
%{gemdir}/gems/rabl-0.7.0/test/plist_engine_test.rb
%{gemdir}/gems/rabl-0.7.0/test/renderer_test.rb
%{gemdir}/gems/rabl-0.7.0/test/silence.rb
%{gemdir}/gems/rabl-0.7.0/test/template_test.rb
%{gemdir}/gems/rabl-0.7.0/test/teststrap.rb


%doc %{gemdir}/doc/rabl-0.7.0
%{gemdir}/cache/rabl-0.7.0.gem
%{gemdir}/specifications/rabl-0.7.0.gemspec

%changelog
