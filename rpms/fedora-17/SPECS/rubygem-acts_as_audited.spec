# Generated from acts_as_audited-2.0.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name acts_as_audited
%global rubyabi 1.9.1

Summary: ActiveRecord extension that logs all changes to your models in an audits table
Name: rubygem-%{gem_name}
Version: 2.0.0
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://github.com/collectiveidea/acts_as_audited
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) >= 1.3.6
Requires: ruby 
Requires: rubygem(rails) >= 3.0.3
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: rubygems-devel >= 1.3.6
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description



%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
%setup -q -c -T
mkdir -p .%{gem_dir}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/





%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
/usr/share/gems/gems/acts_as_audited-2.0.0/.gitignore
/usr/share/gems/gems/acts_as_audited-2.0.0/.yardopts
/usr/share/gems/gems/acts_as_audited-2.0.0/CHANGELOG
/usr/share/gems/gems/acts_as_audited-2.0.0/Gemfile
/usr/share/gems/gems/acts_as_audited-2.0.0/Gemfile.lock
/usr/share/gems/gems/acts_as_audited-2.0.0/LICENSE
/usr/share/gems/gems/acts_as_audited-2.0.0/README.textile
/usr/share/gems/gems/acts_as_audited-2.0.0/Rakefile
/usr/share/gems/gems/acts_as_audited-2.0.0/acts_as_audited.gemspec
/usr/share/gems/gems/acts_as_audited-2.0.0/autotest/discover.rb
/usr/share/gems/gems/acts_as_audited-2.0.0/spec/acts_as_audited_spec.rb
/usr/share/gems/gems/acts_as_audited-2.0.0/spec/audit_spec.rb
/usr/share/gems/gems/acts_as_audited-2.0.0/spec/audit_sweeper_spec.rb
/usr/share/gems/gems/acts_as_audited-2.0.0/spec/audited_spec_helpers.rb
/usr/share/gems/gems/acts_as_audited-2.0.0/spec/db/schema.rb
/usr/share/gems/gems/acts_as_audited-2.0.0/spec/rails_app/config/application.rb
/usr/share/gems/gems/acts_as_audited-2.0.0/spec/rails_app/config/boot.rb
/usr/share/gems/gems/acts_as_audited-2.0.0/spec/rails_app/config/database.yml
/usr/share/gems/gems/acts_as_audited-2.0.0/spec/rails_app/config/environment.rb
/usr/share/gems/gems/acts_as_audited-2.0.0/spec/rails_app/config/environments/development.rb
/usr/share/gems/gems/acts_as_audited-2.0.0/spec/rails_app/config/environments/production.rb
/usr/share/gems/gems/acts_as_audited-2.0.0/spec/rails_app/config/environments/test.rb
/usr/share/gems/gems/acts_as_audited-2.0.0/spec/rails_app/config/initializers/backtrace_silencers.rb
/usr/share/gems/gems/acts_as_audited-2.0.0/spec/rails_app/config/initializers/inflections.rb
/usr/share/gems/gems/acts_as_audited-2.0.0/spec/rails_app/config/initializers/secret_token.rb
/usr/share/gems/gems/acts_as_audited-2.0.0/spec/rails_app/config/routes.rb
/usr/share/gems/gems/acts_as_audited-2.0.0/spec/spec_helper.rb
/usr/share/gems/gems/acts_as_audited-2.0.0/spec/spec_models.rb
/usr/share/gems/gems/acts_as_audited-2.0.0/test/db/version_1.rb
/usr/share/gems/gems/acts_as_audited-2.0.0/test/db/version_2.rb
/usr/share/gems/gems/acts_as_audited-2.0.0/test/db/version_3.rb
/usr/share/gems/gems/acts_as_audited-2.0.0/test/db/version_4.rb
/usr/share/gems/gems/acts_as_audited-2.0.0/test/db/version_5.rb
/usr/share/gems/gems/acts_as_audited-2.0.0/test/install_generator_test.rb
/usr/share/gems/gems/acts_as_audited-2.0.0/test/test_helper.rb
/usr/share/gems/gems/acts_as_audited-2.0.0/test/upgrade_generator_test.rb

%files doc
%doc %{gem_docdir}

%changelog
* Thu Jun 14 2012 jason - 2.0.0-1
- Initial package
