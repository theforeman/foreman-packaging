%define rbname arel
%define version 2.0.10
%define release 1

Summary: Arel is a Relational Algebra for Ruby
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://github.com/rails/arel
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.8.10
BuildRequires: ruby 
BuildRequires: rubygems >= 1.8.10
BuildArch: noarch
Provides: rubygem(arel) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
Arel is a Relational Algebra for Ruby. It 1) simplifies the generation complex
of SQL queries and it 2) adapts to various RDBMS systems. It is intended to be
a framework framework; that is, you can build your own ORM with it, focusing
on innovative object and collection modeling as opposed to database
compatibility and query generation.


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
%{gemdir}/gems/arel-2.0.10/.autotest
%doc %{gemdir}/gems/arel-2.0.10/History.txt
%doc %{gemdir}/gems/arel-2.0.10/MIT-LICENSE.txt
%doc %{gemdir}/gems/arel-2.0.10/Manifest.txt
%doc %{gemdir}/gems/arel-2.0.10/README.markdown
%{gemdir}/gems/arel-2.0.10/Rakefile
%{gemdir}/gems/arel-2.0.10/arel.gemspec
%{gemdir}/gems/arel-2.0.10/lib/arel.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/attributes.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/attributes/attribute.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/compatibility/wheres.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/crud.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/delete_manager.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/deprecated.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/expression.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/expressions.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/insert_manager.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/nodes.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/nodes/and.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/nodes/as.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/nodes/assignment.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/nodes/avg.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/nodes/between.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/nodes/binary.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/nodes/count.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/nodes/delete_statement.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/nodes/does_not_match.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/nodes/equality.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/nodes/except.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/nodes/exists.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/nodes/function.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/nodes/greater_than.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/nodes/greater_than_or_equal.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/nodes/group.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/nodes/grouping.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/nodes/having.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/nodes/in.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/nodes/inner_join.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/nodes/insert_statement.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/nodes/intersect.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/nodes/join.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/nodes/less_than.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/nodes/less_than_or_equal.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/nodes/limit.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/nodes/lock.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/nodes/matches.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/nodes/max.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/nodes/min.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/nodes/node.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/nodes/not.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/nodes/not_equal.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/nodes/not_in.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/nodes/offset.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/nodes/on.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/nodes/or.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/nodes/ordering.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/nodes/outer_join.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/nodes/select_core.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/nodes/select_statement.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/nodes/sql_literal.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/nodes/string_join.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/nodes/sum.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/nodes/table_alias.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/nodes/top.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/nodes/unary.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/nodes/union.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/nodes/union_all.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/nodes/unqualified_column.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/nodes/update_statement.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/nodes/values.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/predications.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/relation.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/select_manager.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/sql/engine.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/sql_literal.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/table.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/tree_manager.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/update_manager.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/visitors.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/visitors/depth_first.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/visitors/dot.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/visitors/join_sql.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/visitors/mssql.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/visitors/mysql.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/visitors/oracle.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/visitors/order_clauses.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/visitors/postgresql.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/visitors/sqlite.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/visitors/to_sql.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/visitors/visitor.rb
%{gemdir}/gems/arel-2.0.10/lib/arel/visitors/where_sql.rb
%{gemdir}/gems/arel-2.0.10/test/attributes/test_attribute.rb
%{gemdir}/gems/arel-2.0.10/test/helper.rb
%{gemdir}/gems/arel-2.0.10/test/nodes/test_as.rb
%{gemdir}/gems/arel-2.0.10/test/nodes/test_count.rb
%{gemdir}/gems/arel-2.0.10/test/nodes/test_delete_statement.rb
%{gemdir}/gems/arel-2.0.10/test/nodes/test_equality.rb
%{gemdir}/gems/arel-2.0.10/test/nodes/test_insert_statement.rb
%{gemdir}/gems/arel-2.0.10/test/nodes/test_node.rb
%{gemdir}/gems/arel-2.0.10/test/nodes/test_not.rb
%{gemdir}/gems/arel-2.0.10/test/nodes/test_or.rb
%{gemdir}/gems/arel-2.0.10/test/nodes/test_select_core.rb
%{gemdir}/gems/arel-2.0.10/test/nodes/test_select_statement.rb
%{gemdir}/gems/arel-2.0.10/test/nodes/test_sql_literal.rb
%{gemdir}/gems/arel-2.0.10/test/nodes/test_sum.rb
%{gemdir}/gems/arel-2.0.10/test/nodes/test_update_statement.rb
%{gemdir}/gems/arel-2.0.10/test/support/fake_record.rb
%{gemdir}/gems/arel-2.0.10/test/test_activerecord_compat.rb
%{gemdir}/gems/arel-2.0.10/test/test_attributes.rb
%{gemdir}/gems/arel-2.0.10/test/test_crud.rb
%{gemdir}/gems/arel-2.0.10/test/test_delete_manager.rb
%{gemdir}/gems/arel-2.0.10/test/test_insert_manager.rb
%{gemdir}/gems/arel-2.0.10/test/test_select_manager.rb
%{gemdir}/gems/arel-2.0.10/test/test_table.rb
%{gemdir}/gems/arel-2.0.10/test/test_update_manager.rb
%{gemdir}/gems/arel-2.0.10/test/visitors/test_depth_first.rb
%{gemdir}/gems/arel-2.0.10/test/visitors/test_dot.rb
%{gemdir}/gems/arel-2.0.10/test/visitors/test_join_sql.rb
%{gemdir}/gems/arel-2.0.10/test/visitors/test_mssql.rb
%{gemdir}/gems/arel-2.0.10/test/visitors/test_mysql.rb
%{gemdir}/gems/arel-2.0.10/test/visitors/test_oracle.rb
%{gemdir}/gems/arel-2.0.10/test/visitors/test_postgres.rb
%{gemdir}/gems/arel-2.0.10/test/visitors/test_sqlite.rb
%{gemdir}/gems/arel-2.0.10/test/visitors/test_to_sql.rb
%{gemdir}/gems/arel-2.0.10/.gemtest


%doc %{gemdir}/doc/arel-2.0.10
%{gemdir}/cache/arel-2.0.10.gem
%{gemdir}/specifications/arel-2.0.10.gemspec

%changelog
