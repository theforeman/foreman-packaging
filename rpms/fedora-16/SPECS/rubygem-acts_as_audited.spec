%define rbname acts_as_audited
%define version 2.0.0
%define release 1

Summary: ActiveRecord extension that logs all changes to your models in an audits table
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://github.com/collectiveidea/acts_as_audited
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.8.10

Requires: rubygem-rails >= 3.0.3
BuildRequires: ruby 
BuildRequires: rubygems >= 1.8.10
BuildArch: noarch
Provides: rubygem(acts_as_audited) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description



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
%{gemdir}/gems/acts_as_audited-2.0.0/.gitignore
%{gemdir}/gems/acts_as_audited-2.0.0/.yardopts
%{gemdir}/gems/acts_as_audited-2.0.0/CHANGELOG
%{gemdir}/gems/acts_as_audited-2.0.0/Gemfile
%{gemdir}/gems/acts_as_audited-2.0.0/Gemfile.lock
%{gemdir}/gems/acts_as_audited-2.0.0/LICENSE
%{gemdir}/gems/acts_as_audited-2.0.0/README.textile
%{gemdir}/gems/acts_as_audited-2.0.0/Rakefile
%{gemdir}/gems/acts_as_audited-2.0.0/acts_as_audited.gemspec
%{gemdir}/gems/acts_as_audited-2.0.0/autotest/discover.rb
%{gemdir}/gems/acts_as_audited-2.0.0/lib/acts_as_audited.rb
%{gemdir}/gems/acts_as_audited-2.0.0/lib/acts_as_audited/audit.rb
%{gemdir}/gems/acts_as_audited-2.0.0/lib/acts_as_audited/audit_sweeper.rb
%{gemdir}/gems/acts_as_audited-2.0.0/lib/acts_as_audited/auditor.rb
%{gemdir}/gems/acts_as_audited-2.0.0/lib/generators/acts_as_audited/install_generator.rb
%{gemdir}/gems/acts_as_audited-2.0.0/lib/generators/acts_as_audited/templates/add_association_to_audits.rb
%{gemdir}/gems/acts_as_audited-2.0.0/lib/generators/acts_as_audited/templates/add_comment_to_audits.rb
%{gemdir}/gems/acts_as_audited-2.0.0/lib/generators/acts_as_audited/templates/add_remote_address_to_audits.rb
%{gemdir}/gems/acts_as_audited-2.0.0/lib/generators/acts_as_audited/templates/install.rb
%{gemdir}/gems/acts_as_audited-2.0.0/lib/generators/acts_as_audited/templates/rename_association_to_associated.rb
%{gemdir}/gems/acts_as_audited-2.0.0/lib/generators/acts_as_audited/templates/rename_changes_to_audited_changes.rb
%{gemdir}/gems/acts_as_audited-2.0.0/lib/generators/acts_as_audited/templates/rename_parent_to_association.rb
%{gemdir}/gems/acts_as_audited-2.0.0/lib/generators/acts_as_audited/upgrade_generator.rb
%{gemdir}/gems/acts_as_audited-2.0.0/spec/acts_as_audited_spec.rb
%{gemdir}/gems/acts_as_audited-2.0.0/spec/audit_spec.rb
%{gemdir}/gems/acts_as_audited-2.0.0/spec/audit_sweeper_spec.rb
%{gemdir}/gems/acts_as_audited-2.0.0/spec/audited_spec_helpers.rb
%{gemdir}/gems/acts_as_audited-2.0.0/spec/db/schema.rb
%{gemdir}/gems/acts_as_audited-2.0.0/spec/rails_app/config/application.rb
%{gemdir}/gems/acts_as_audited-2.0.0/spec/rails_app/config/boot.rb
%{gemdir}/gems/acts_as_audited-2.0.0/spec/rails_app/config/database.yml
%{gemdir}/gems/acts_as_audited-2.0.0/spec/rails_app/config/environment.rb
%{gemdir}/gems/acts_as_audited-2.0.0/spec/rails_app/config/environments/development.rb
%{gemdir}/gems/acts_as_audited-2.0.0/spec/rails_app/config/environments/production.rb
%{gemdir}/gems/acts_as_audited-2.0.0/spec/rails_app/config/environments/test.rb
%{gemdir}/gems/acts_as_audited-2.0.0/spec/rails_app/config/initializers/backtrace_silencers.rb
%{gemdir}/gems/acts_as_audited-2.0.0/spec/rails_app/config/initializers/inflections.rb
%{gemdir}/gems/acts_as_audited-2.0.0/spec/rails_app/config/initializers/secret_token.rb
%{gemdir}/gems/acts_as_audited-2.0.0/spec/rails_app/config/routes.rb
%{gemdir}/gems/acts_as_audited-2.0.0/spec/spec_helper.rb
%{gemdir}/gems/acts_as_audited-2.0.0/spec/spec_models.rb
%{gemdir}/gems/acts_as_audited-2.0.0/test/db/version_1.rb
%{gemdir}/gems/acts_as_audited-2.0.0/test/db/version_2.rb
%{gemdir}/gems/acts_as_audited-2.0.0/test/db/version_3.rb
%{gemdir}/gems/acts_as_audited-2.0.0/test/db/version_4.rb
%{gemdir}/gems/acts_as_audited-2.0.0/test/db/version_5.rb
%{gemdir}/gems/acts_as_audited-2.0.0/test/install_generator_test.rb
%{gemdir}/gems/acts_as_audited-2.0.0/test/test_helper.rb
%{gemdir}/gems/acts_as_audited-2.0.0/test/upgrade_generator_test.rb


%doc %{gemdir}/doc/acts_as_audited-2.0.0
%{gemdir}/cache/acts_as_audited-2.0.0.gem
%{gemdir}/specifications/acts_as_audited-2.0.0.gemspec

%changelog
