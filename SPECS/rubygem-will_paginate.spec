%define rbname will_paginate
%define version 3.0.3
%define release 1

Summary: Pagination plugin for web frameworks and other apps
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: https://github.com/mislav/will_paginate/wiki
Source0: %{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.8.10
BuildRequires: ruby 
BuildRequires: rubygems >= 1.8.10
BuildArch: noarch
Provides: rubygem(will_paginate) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
will_paginate provides a simple API for performing paginated queries with
Active Record, DataMapper and Sequel, and includes helpers for rendering
pagination links in Rails, Sinatra and Merb web apps.


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
%{gemdir}/gems/will_paginate-3.0.3/Rakefile
%{gemdir}/gems/will_paginate-3.0.3/lib/will_paginate/active_record.rb
%{gemdir}/gems/will_paginate-3.0.3/lib/will_paginate/array.rb
%{gemdir}/gems/will_paginate-3.0.3/lib/will_paginate/collection.rb
%{gemdir}/gems/will_paginate-3.0.3/lib/will_paginate/core_ext.rb
%{gemdir}/gems/will_paginate-3.0.3/lib/will_paginate/data_mapper.rb
%{gemdir}/gems/will_paginate-3.0.3/lib/will_paginate/deprecation.rb
%{gemdir}/gems/will_paginate-3.0.3/lib/will_paginate/i18n.rb
%{gemdir}/gems/will_paginate-3.0.3/lib/will_paginate/locale/en.yml
%{gemdir}/gems/will_paginate-3.0.3/lib/will_paginate/page_number.rb
%{gemdir}/gems/will_paginate-3.0.3/lib/will_paginate/per_page.rb
%{gemdir}/gems/will_paginate-3.0.3/lib/will_paginate/railtie.rb
%{gemdir}/gems/will_paginate-3.0.3/lib/will_paginate/sequel.rb
%{gemdir}/gems/will_paginate-3.0.3/lib/will_paginate/version.rb
%{gemdir}/gems/will_paginate-3.0.3/lib/will_paginate/view_helpers/action_view.rb
%{gemdir}/gems/will_paginate-3.0.3/lib/will_paginate/view_helpers/link_renderer.rb
%{gemdir}/gems/will_paginate-3.0.3/lib/will_paginate/view_helpers/link_renderer_base.rb
%{gemdir}/gems/will_paginate-3.0.3/lib/will_paginate/view_helpers/merb.rb
%{gemdir}/gems/will_paginate-3.0.3/lib/will_paginate/view_helpers/sinatra.rb
%{gemdir}/gems/will_paginate-3.0.3/lib/will_paginate/view_helpers.rb
%{gemdir}/gems/will_paginate-3.0.3/lib/will_paginate.rb
%{gemdir}/gems/will_paginate-3.0.3/spec/ci.rb
%{gemdir}/gems/will_paginate-3.0.3/spec/collection_spec.rb
%{gemdir}/gems/will_paginate-3.0.3/spec/console
%{gemdir}/gems/will_paginate-3.0.3/spec/console_fixtures.rb
%{gemdir}/gems/will_paginate-3.0.3/spec/database.yml
%{gemdir}/gems/will_paginate-3.0.3/spec/finders/active_record_spec.rb
%{gemdir}/gems/will_paginate-3.0.3/spec/finders/activerecord_test_connector.rb
%{gemdir}/gems/will_paginate-3.0.3/spec/finders/data_mapper_spec.rb
%{gemdir}/gems/will_paginate-3.0.3/spec/finders/data_mapper_test_connector.rb
%{gemdir}/gems/will_paginate-3.0.3/spec/finders/sequel_spec.rb
%{gemdir}/gems/will_paginate-3.0.3/spec/finders/sequel_test_connector.rb
%{gemdir}/gems/will_paginate-3.0.3/spec/fixtures/admin.rb
%{gemdir}/gems/will_paginate-3.0.3/spec/fixtures/developer.rb
%{gemdir}/gems/will_paginate-3.0.3/spec/fixtures/developers_projects.yml
%{gemdir}/gems/will_paginate-3.0.3/spec/fixtures/project.rb
%{gemdir}/gems/will_paginate-3.0.3/spec/fixtures/projects.yml
%{gemdir}/gems/will_paginate-3.0.3/spec/fixtures/replies.yml
%{gemdir}/gems/will_paginate-3.0.3/spec/fixtures/reply.rb
%{gemdir}/gems/will_paginate-3.0.3/spec/fixtures/schema.rb
%{gemdir}/gems/will_paginate-3.0.3/spec/fixtures/topic.rb
%{gemdir}/gems/will_paginate-3.0.3/spec/fixtures/topics.yml
%{gemdir}/gems/will_paginate-3.0.3/spec/fixtures/user.rb
%{gemdir}/gems/will_paginate-3.0.3/spec/fixtures/users.yml
%{gemdir}/gems/will_paginate-3.0.3/spec/page_number_spec.rb
%{gemdir}/gems/will_paginate-3.0.3/spec/per_page_spec.rb
%{gemdir}/gems/will_paginate-3.0.3/spec/spec_helper.rb
%{gemdir}/gems/will_paginate-3.0.3/spec/view_helpers/action_view_spec.rb
%{gemdir}/gems/will_paginate-3.0.3/spec/view_helpers/base_spec.rb
%{gemdir}/gems/will_paginate-3.0.3/spec/view_helpers/link_renderer_base_spec.rb
%{gemdir}/gems/will_paginate-3.0.3/spec/view_helpers/view_example_group.rb
%doc %{gemdir}/gems/will_paginate-3.0.3/README.md
%doc %{gemdir}/gems/will_paginate-3.0.3/LICENSE


%doc %{gemdir}/doc/will_paginate-3.0.3
%{gemdir}/cache/will_paginate-3.0.3.gem
%{gemdir}/specifications/will_paginate-3.0.3.gemspec

%changelog
