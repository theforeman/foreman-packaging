%define rbname activerecord
%define version 3.2.13
%define release 1

Summary: Object-relational mapper framework (part of Rails).
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
Requires: rubygem-activesupport = 3.2.13
Requires: rubygem-activemodel = 3.2.13
Requires: rubygem-arel => 3.0.2
Requires: rubygem-arel < 3.1
Requires: rubygem-tzinfo => 0.3.29
Requires: rubygem-tzinfo < 0.4

BuildRequires: ruby >= 1.8.7
BuildRequires: rubygems >= 1.8.10
BuildArch: noarch

Provides: rubygem(activerecord) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
Databases on Rails. Build a persistent domain model by mapping database tables
to Ruby classes. Strong conventions for associations, validations,
aggregations, migrations, and testing come baked-in.


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
%{gemdir}/gems/activerecord-%{version}/CHANGELOG.md
%{gemdir}/gems/activerecord-%{version}/MIT-LICENSE
%doc %{gemdir}/gems/activerecord-%{version}/README.rdoc
%{gemdir}/gems/activerecord-%{version}/examples/associations.png
%{gemdir}/gems/activerecord-%{version}/examples/performance.rb
%{gemdir}/gems/activerecord-%{version}/examples/simple.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/aggregations.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/associations/alias_tracker.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/associations/association.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/associations/association_scope.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/associations/belongs_to_association.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/associations/belongs_to_polymorphic_association.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/associations/builder/association.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/associations/builder/belongs_to.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/associations/builder/collection_association.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/associations/builder/has_and_belongs_to_many.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/associations/builder/has_many.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/associations/builder/has_one.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/associations/builder/singular_association.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/associations/collection_association.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/associations/collection_proxy.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/associations/has_and_belongs_to_many_association.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/associations/has_many_association.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/associations/has_many_through_association.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/associations/has_one_association.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/associations/has_one_through_association.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/associations/join_dependency/join_association.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/associations/join_dependency/join_base.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/associations/join_dependency/join_part.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/associations/join_dependency.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/associations/join_helper.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/associations/preloader/association.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/associations/preloader/belongs_to.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/associations/preloader/collection_association.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/associations/preloader/has_and_belongs_to_many.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/associations/preloader/has_many.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/associations/preloader/has_many_through.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/associations/preloader/has_one.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/associations/preloader/has_one_through.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/associations/preloader/singular_association.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/associations/preloader/through_association.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/associations/preloader.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/associations/singular_association.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/associations/through_association.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/associations.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/attribute_assignment.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/attribute_methods/before_type_cast.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/attribute_methods/deprecated_underscore_read.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/attribute_methods/dirty.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/attribute_methods/primary_key.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/attribute_methods/query.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/attribute_methods/read.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/attribute_methods/serialization.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/attribute_methods/time_zone_conversion.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/attribute_methods/write.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/attribute_methods.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/autosave_association.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/base.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/callbacks.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/coders/yaml_column.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/connection_adapters/abstract/connection_pool.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/connection_adapters/abstract/connection_specification.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/connection_adapters/abstract/database_limits.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/connection_adapters/abstract/database_statements.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/connection_adapters/abstract/query_cache.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/connection_adapters/abstract/quoting.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/connection_adapters/abstract/schema_definitions.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/connection_adapters/abstract/schema_statements.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/connection_adapters/abstract_adapter.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/connection_adapters/abstract_mysql_adapter.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/connection_adapters/column.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/connection_adapters/mysql2_adapter.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/connection_adapters/mysql_adapter.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/connection_adapters/postgresql_adapter.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/connection_adapters/schema_cache.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/connection_adapters/sqlite3_adapter.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/connection_adapters/sqlite_adapter.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/connection_adapters/statement_pool.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/counter_cache.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/dynamic_finder_match.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/dynamic_matchers.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/dynamic_scope_match.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/errors.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/explain.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/explain_subscriber.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/fixtures/file.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/fixtures.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/identity_map.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/inheritance.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/integration.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/locale/en.yml
%{gemdir}/gems/activerecord-%{version}/lib/active_record/locking/optimistic.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/locking/pessimistic.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/log_subscriber.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/migration/command_recorder.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/migration.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/model_schema.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/nested_attributes.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/observer.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/persistence.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/query_cache.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/querying.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/railtie.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/railties/console_sandbox.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/railties/controller_runtime.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/railties/databases.rake
%{gemdir}/gems/activerecord-%{version}/lib/active_record/railties/jdbcmysql_error.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/readonly_attributes.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/reflection.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/relation/batches.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/relation/calculations.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/relation/delegation.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/relation/finder_methods.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/relation/predicate_builder.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/relation/query_methods.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/relation/spawn_methods.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/relation.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/result.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/sanitization.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/schema.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/schema_dumper.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/scoping/default.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/scoping/named.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/scoping.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/serialization.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/serializers/xml_serializer.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/session_store.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/store.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/test_case.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/timestamp.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/transactions.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/translation.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/validations/associated.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/validations/uniqueness.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/validations.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record/version.rb
%{gemdir}/gems/activerecord-%{version}/lib/active_record.rb
%{gemdir}/gems/activerecord-%{version}/lib/rails/generators/active_record/migration/migration_generator.rb
%{gemdir}/gems/activerecord-%{version}/lib/rails/generators/active_record/migration/templates/migration.rb
%{gemdir}/gems/activerecord-%{version}/lib/rails/generators/active_record/migration.rb
%{gemdir}/gems/activerecord-%{version}/lib/rails/generators/active_record/model/model_generator.rb
%{gemdir}/gems/activerecord-%{version}/lib/rails/generators/active_record/model/templates/migration.rb
%{gemdir}/gems/activerecord-%{version}/lib/rails/generators/active_record/model/templates/model.rb
%{gemdir}/gems/activerecord-%{version}/lib/rails/generators/active_record/model/templates/module.rb
%{gemdir}/gems/activerecord-%{version}/lib/rails/generators/active_record/observer/observer_generator.rb
%{gemdir}/gems/activerecord-%{version}/lib/rails/generators/active_record/observer/templates/observer.rb
%{gemdir}/gems/activerecord-%{version}/lib/rails/generators/active_record/session_migration/session_migration_generator.rb
%{gemdir}/gems/activerecord-%{version}/lib/rails/generators/active_record/session_migration/templates/migration.rb
%{gemdir}/gems/activerecord-%{version}/lib/rails/generators/active_record.rb


%doc %{gemdir}/doc/activerecord-%{version}
%{gemdir}/cache/activerecord-%{version}.gem
%{gemdir}/specifications/activerecord-%{version}.gemspec

%changelog
* Fri Apr 12 2013 shk@redhat.com 3.2.13-1
- Updated to 3.2.13
* Mon Feb 4 2013 shk@redhat.com 3.0.20-1
- Updated to 3.0.20
* Fri Jan 25 2013 shk@redhat.com 3.0.19-1
- Updated to 3.0.19
