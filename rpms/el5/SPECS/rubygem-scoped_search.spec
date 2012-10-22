%define rbname scoped_search
%define version 2.4.0
%define release 1

Summary: Easily search you ActiveRecord models with a simple query language using a named scope.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://github.com/wvanbergen/scoped_search/wiki
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.8.10

Requires: rubygem-activerecord >= 2.1.0
BuildRequires: ruby 
BuildRequires: rubygems >= 1.8.10
BuildArch: noarch
Provides: rubygem(scoped_search) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
Scoped search makes it easy to search your ActiveRecord-based models.
It will create a named scope :search_for that can be called with a query
string. It will build an SQL query using
the provided query string and a definition that specifies on what fields to
search. Because the functionality is
built on named_scope, the result of the search_for call can be used like any
other named_scope, so it can be
chained with another scope or combined with will_paginate.
Because it uses standard SQL, it does not require any setup, indexers or
daemons. This makes scoped_search
suitable to quickly add basic search functionality to your application with
little hassle. On the other hand,
it may not be the best choice if it is going to be used on very large datasets
or by a large user base.


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
%{gemdir}/gems/scoped_search-%{version}/.gitignore
%{gemdir}/gems/scoped_search-%{version}/.infinity_test
%{gemdir}/gems/scoped_search-%{version}/Gemfile
%{gemdir}/gems/scoped_search-%{version}/LICENSE
%doc %{gemdir}/gems/scoped_search-%{version}/README.rdoc
%{gemdir}/gems/scoped_search-%{version}/Rakefile
%{gemdir}/gems/scoped_search-%{version}/init.rb
%{gemdir}/gems/scoped_search-%{version}/lib/scoped_search.rb
%{gemdir}/gems/scoped_search-%{version}/lib/scoped_search/auto_complete_builder.rb
%{gemdir}/gems/scoped_search-%{version}/lib/scoped_search/definition.rb
%{gemdir}/gems/scoped_search-%{version}/lib/scoped_search/query_builder.rb
%{gemdir}/gems/scoped_search-%{version}/lib/scoped_search/query_language.rb
%{gemdir}/gems/scoped_search-%{version}/lib/scoped_search/query_language/ast.rb
%{gemdir}/gems/scoped_search-%{version}/lib/scoped_search/query_language/parser.rb
%{gemdir}/gems/scoped_search-%{version}/lib/scoped_search/query_language/tokenizer.rb
%{gemdir}/gems/scoped_search-%{version}/lib/scoped_search/rails_helper.rb
%{gemdir}/gems/scoped_search-%{version}/scoped_search.gemspec
%{gemdir}/gems/scoped_search-%{version}/spec/database.yml
%{gemdir}/gems/scoped_search-%{version}/spec/integration/api_spec.rb
%{gemdir}/gems/scoped_search-%{version}/spec/integration/auto_complete_spec.rb
%{gemdir}/gems/scoped_search-%{version}/spec/integration/key_value_querying_spec.rb
%{gemdir}/gems/scoped_search-%{version}/spec/integration/ordinal_querying_spec.rb
%{gemdir}/gems/scoped_search-%{version}/spec/integration/profile_querying_spec.rb
%{gemdir}/gems/scoped_search-%{version}/spec/integration/relation_querying_spec.rb
%{gemdir}/gems/scoped_search-%{version}/spec/integration/set_query_spec.rb
%{gemdir}/gems/scoped_search-%{version}/spec/integration/string_querying_spec.rb
%{gemdir}/gems/scoped_search-%{version}/spec/lib/database.rb
%{gemdir}/gems/scoped_search-%{version}/spec/lib/matchers.rb
%{gemdir}/gems/scoped_search-%{version}/spec/lib/mocks.rb
%{gemdir}/gems/scoped_search-%{version}/spec/spec_helper.rb
%{gemdir}/gems/scoped_search-%{version}/spec/unit/ast_spec.rb
%{gemdir}/gems/scoped_search-%{version}/spec/unit/auto_complete_builder_spec.rb
%{gemdir}/gems/scoped_search-%{version}/spec/unit/definition_spec.rb
%{gemdir}/gems/scoped_search-%{version}/spec/unit/parser_spec.rb
%{gemdir}/gems/scoped_search-%{version}/spec/unit/query_builder_spec.rb
%{gemdir}/gems/scoped_search-%{version}/spec/unit/tokenizer_spec.rb
%{gemdir}/gems/scoped_search-%{version}/tasks/github-gem.rake


%doc %{gemdir}/doc/scoped_search-%{version}
%{gemdir}/cache/scoped_search-%{version}.gem
%{gemdir}/specifications/scoped_search-%{version}.gemspec

%changelog
