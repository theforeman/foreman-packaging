# Generated from arel-2.0.10.gem by gem2rpm -*- rpm-spec -*-
%global gem_name arel
%global rubyabi 1.9.1

Summary: Arel is a Relational Algebra for Ruby
Name: rubygem-%{gem_name}
Version: 2.0.10
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://github.com/rails/arel
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems)
Requires: ruby
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Arel is a Relational Algebra for Ruby. It 1) simplifies the generation complex
of SQL queries and it 2) adapts to various RDBMS systems. It is intended to be
a framework framework; that is, you can build your own ORM with it, focusing
on innovative object and collection modeling as opposed to database
compatibility and query generation.


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
/usr/share/gems/gems/arel-2.0.10/.autotest
/usr/share/gems/gems/arel-2.0.10/.gemtest
/usr/share/gems/gems/arel-2.0.10/Rakefile
/usr/share/gems/gems/arel-2.0.10/arel.gemspec
/usr/share/gems/gems/arel-2.0.10/test/attributes/test_attribute.rb
/usr/share/gems/gems/arel-2.0.10/test/helper.rb
/usr/share/gems/gems/arel-2.0.10/test/nodes/test_as.rb
/usr/share/gems/gems/arel-2.0.10/test/nodes/test_count.rb
/usr/share/gems/gems/arel-2.0.10/test/nodes/test_delete_statement.rb
/usr/share/gems/gems/arel-2.0.10/test/nodes/test_equality.rb
/usr/share/gems/gems/arel-2.0.10/test/nodes/test_insert_statement.rb
/usr/share/gems/gems/arel-2.0.10/test/nodes/test_node.rb
/usr/share/gems/gems/arel-2.0.10/test/nodes/test_not.rb
/usr/share/gems/gems/arel-2.0.10/test/nodes/test_or.rb
/usr/share/gems/gems/arel-2.0.10/test/nodes/test_select_core.rb
/usr/share/gems/gems/arel-2.0.10/test/nodes/test_select_statement.rb
/usr/share/gems/gems/arel-2.0.10/test/nodes/test_sql_literal.rb
/usr/share/gems/gems/arel-2.0.10/test/nodes/test_sum.rb
/usr/share/gems/gems/arel-2.0.10/test/nodes/test_update_statement.rb
/usr/share/gems/gems/arel-2.0.10/test/support/fake_record.rb
/usr/share/gems/gems/arel-2.0.10/test/test_activerecord_compat.rb
/usr/share/gems/gems/arel-2.0.10/test/test_attributes.rb
/usr/share/gems/gems/arel-2.0.10/test/test_crud.rb
/usr/share/gems/gems/arel-2.0.10/test/test_delete_manager.rb
/usr/share/gems/gems/arel-2.0.10/test/test_insert_manager.rb
/usr/share/gems/gems/arel-2.0.10/test/test_select_manager.rb
/usr/share/gems/gems/arel-2.0.10/test/test_table.rb
/usr/share/gems/gems/arel-2.0.10/test/test_update_manager.rb
/usr/share/gems/gems/arel-2.0.10/test/visitors/test_depth_first.rb
/usr/share/gems/gems/arel-2.0.10/test/visitors/test_dot.rb
/usr/share/gems/gems/arel-2.0.10/test/visitors/test_join_sql.rb
/usr/share/gems/gems/arel-2.0.10/test/visitors/test_mssql.rb
/usr/share/gems/gems/arel-2.0.10/test/visitors/test_mysql.rb
/usr/share/gems/gems/arel-2.0.10/test/visitors/test_oracle.rb
/usr/share/gems/gems/arel-2.0.10/test/visitors/test_postgres.rb
/usr/share/gems/gems/arel-2.0.10/test/visitors/test_sqlite.rb
/usr/share/gems/gems/arel-2.0.10/test/visitors/test_to_sql.rb

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/History.txt
%doc %{gem_instdir}/MIT-LICENSE.txt
%doc %{gem_instdir}/Manifest.txt
%doc %{gem_instdir}/README.markdown

%changelog
* Thu Jun 14 2012 jason - 2.0.10-1
- Initial package
