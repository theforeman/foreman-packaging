%define rbname audited
%define version 3.0.0.rc1
%define release 1

Summary: Log all changes to your models
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: https://github.com/collectiveidea/audited
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.8.10
BuildRequires: ruby 
BuildRequires: rubygems >= 1.8.10
BuildArch: noarch
Provides: rubygem(audited) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
Log all changes to your models


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
%{gemdir}/gems/audited-3.0.0.rc1/.gitignore
%{gemdir}/gems/audited-3.0.0.rc1/.travis.yml
%{gemdir}/gems/audited-3.0.0.rc1/.yardopts
%{gemdir}/gems/audited-3.0.0.rc1/Appraisals
%{gemdir}/gems/audited-3.0.0.rc1/CHANGELOG
%{gemdir}/gems/audited-3.0.0.rc1/Gemfile
%{gemdir}/gems/audited-3.0.0.rc1/LICENSE
%{gemdir}/gems/audited-3.0.0.rc1/README.md
%{gemdir}/gems/audited-3.0.0.rc1/Rakefile
%{gemdir}/gems/audited-3.0.0.rc1/audited-activerecord.gemspec
%{gemdir}/gems/audited-3.0.0.rc1/audited-mongo_mapper.gemspec
%{gemdir}/gems/audited-3.0.0.rc1/audited.gemspec
%{gemdir}/gems/audited-3.0.0.rc1/gemfiles/rails30.gemfile
%{gemdir}/gems/audited-3.0.0.rc1/gemfiles/rails31.gemfile
%{gemdir}/gems/audited-3.0.0.rc1/gemfiles/rails32.gemfile
%{gemdir}/gems/audited-3.0.0.rc1/lib/audited.rb
%{gemdir}/gems/audited-3.0.0.rc1/lib/audited/audit.rb
%{gemdir}/gems/audited-3.0.0.rc1/lib/audited/auditor.rb
%{gemdir}/gems/audited-3.0.0.rc1/lib/audited/sweeper.rb
%{gemdir}/gems/audited-3.0.0.rc1/spec/audited_spec_helpers.rb
%{gemdir}/gems/audited-3.0.0.rc1/spec/rails_app/config/application.rb
%{gemdir}/gems/audited-3.0.0.rc1/spec/rails_app/config/database.yml
%{gemdir}/gems/audited-3.0.0.rc1/spec/rails_app/config/environment.rb
%{gemdir}/gems/audited-3.0.0.rc1/spec/rails_app/config/environments/development.rb
%{gemdir}/gems/audited-3.0.0.rc1/spec/rails_app/config/environments/production.rb
%{gemdir}/gems/audited-3.0.0.rc1/spec/rails_app/config/environments/test.rb
%{gemdir}/gems/audited-3.0.0.rc1/spec/rails_app/config/initializers/backtrace_silencers.rb
%{gemdir}/gems/audited-3.0.0.rc1/spec/rails_app/config/initializers/inflections.rb
%{gemdir}/gems/audited-3.0.0.rc1/spec/rails_app/config/initializers/secret_token.rb
%{gemdir}/gems/audited-3.0.0.rc1/spec/rails_app/config/routes.rb
%{gemdir}/gems/audited-3.0.0.rc1/spec/spec_helper.rb
%{gemdir}/gems/audited-3.0.0.rc1/spec/support/active_record/models.rb
%{gemdir}/gems/audited-3.0.0.rc1/spec/support/active_record/schema.rb
%{gemdir}/gems/audited-3.0.0.rc1/spec/support/mongo_mapper/connection.rb
%{gemdir}/gems/audited-3.0.0.rc1/spec/support/mongo_mapper/models.rb
%{gemdir}/gems/audited-3.0.0.rc1/test/db/version_1.rb
%{gemdir}/gems/audited-3.0.0.rc1/test/db/version_2.rb
%{gemdir}/gems/audited-3.0.0.rc1/test/db/version_3.rb
%{gemdir}/gems/audited-3.0.0.rc1/test/db/version_4.rb
%{gemdir}/gems/audited-3.0.0.rc1/test/db/version_5.rb
%{gemdir}/gems/audited-3.0.0.rc1/test/install_generator_test.rb
%{gemdir}/gems/audited-3.0.0.rc1/test/test_helper.rb
%{gemdir}/gems/audited-3.0.0.rc1/test/upgrade_generator_test.rb


%doc %{gemdir}/doc/audited-3.0.0.rc1
%{gemdir}/cache/audited-3.0.0.rc1.gem
%{gemdir}/specifications/audited-3.0.0.rc1.gemspec

%changelog
