%define rbname hirb
%define version 0.6.2
%define release 1

Summary: A mini view framework for console/irb that's easy to use, even while under its influence.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://tagaholic.me/hirb/
Source0: http://rubygems.org/downloads/%{rbname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems >= 1.8.10
BuildRequires: ruby 
BuildRequires: rubygems >= 1.8.10
BuildArch: noarch
Provides: rubygem(hirb) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
Hirb provides a mini view framework for console applications and uses it to
improve ripl(irb)'s default inspect output. Given an object or array of
objects, hirb renders a view based on the object's class and/or ancestry. Hirb
offers reusable views in the form of helper classes. The two main helpers,
Hirb::Helpers::Table and Hirb::Helpers::Tree, provide several options for
generating ascii tables and trees. Using Hirb::Helpers::AutoTable, hirb has
useful default views for at least ten popular database gems i.e. Rails'
ActiveRecord::Base. Other than views, hirb offers a smart pager and a console
menu. The smart pager only pages when the output exceeds the current screen
size. The menu is used in conjunction with tables to offer two dimensional
menus.


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
%{gemdir}/gems/hirb-0.6.2/lib/bond/completions/hirb.rb
%{gemdir}/gems/hirb-0.6.2/lib/hirb/console.rb
%{gemdir}/gems/hirb-0.6.2/lib/hirb/dynamic_view.rb
%{gemdir}/gems/hirb-0.6.2/lib/hirb/formatter.rb
%{gemdir}/gems/hirb-0.6.2/lib/hirb/helpers/auto_table.rb
%{gemdir}/gems/hirb-0.6.2/lib/hirb/helpers/object_table.rb
%{gemdir}/gems/hirb-0.6.2/lib/hirb/helpers/parent_child_tree.rb
%{gemdir}/gems/hirb-0.6.2/lib/hirb/helpers/tab_table.rb
%{gemdir}/gems/hirb-0.6.2/lib/hirb/helpers/table/filters.rb
%{gemdir}/gems/hirb-0.6.2/lib/hirb/helpers/table/resizer.rb
%{gemdir}/gems/hirb-0.6.2/lib/hirb/helpers/table.rb
%{gemdir}/gems/hirb-0.6.2/lib/hirb/helpers/tree.rb
%{gemdir}/gems/hirb-0.6.2/lib/hirb/helpers/unicode_table.rb
%{gemdir}/gems/hirb-0.6.2/lib/hirb/helpers/vertical_table.rb
%{gemdir}/gems/hirb-0.6.2/lib/hirb/helpers.rb
%{gemdir}/gems/hirb-0.6.2/lib/hirb/import_object.rb
%{gemdir}/gems/hirb-0.6.2/lib/hirb/menu.rb
%{gemdir}/gems/hirb-0.6.2/lib/hirb/pager.rb
%{gemdir}/gems/hirb-0.6.2/lib/hirb/string.rb
%{gemdir}/gems/hirb-0.6.2/lib/hirb/util.rb
%{gemdir}/gems/hirb-0.6.2/lib/hirb/version.rb
%{gemdir}/gems/hirb-0.6.2/lib/hirb/view.rb
%{gemdir}/gems/hirb-0.6.2/lib/hirb/views/couch_db.rb
%{gemdir}/gems/hirb-0.6.2/lib/hirb/views/misc_db.rb
%{gemdir}/gems/hirb-0.6.2/lib/hirb/views/mongo_db.rb
%{gemdir}/gems/hirb-0.6.2/lib/hirb/views/orm.rb
%{gemdir}/gems/hirb-0.6.2/lib/hirb/views/rails.rb
%{gemdir}/gems/hirb-0.6.2/lib/hirb/views.rb
%{gemdir}/gems/hirb-0.6.2/lib/hirb.rb
%{gemdir}/gems/hirb-0.6.2/lib/ripl/hirb.rb
%{gemdir}/gems/hirb-0.6.2/test/auto_table_test.rb
%{gemdir}/gems/hirb-0.6.2/test/console_test.rb
%{gemdir}/gems/hirb-0.6.2/test/dynamic_view_test.rb
%{gemdir}/gems/hirb-0.6.2/test/formatter_test.rb
%{gemdir}/gems/hirb-0.6.2/test/hirb_test.rb
%{gemdir}/gems/hirb-0.6.2/test/import_test.rb
%{gemdir}/gems/hirb-0.6.2/test/menu_test.rb
%{gemdir}/gems/hirb-0.6.2/test/object_table_test.rb
%{gemdir}/gems/hirb-0.6.2/test/pager_test.rb
%{gemdir}/gems/hirb-0.6.2/test/resizer_test.rb
%{gemdir}/gems/hirb-0.6.2/test/table_test.rb
%{gemdir}/gems/hirb-0.6.2/test/test_helper.rb
%{gemdir}/gems/hirb-0.6.2/test/tree_test.rb
%{gemdir}/gems/hirb-0.6.2/test/util_test.rb
%{gemdir}/gems/hirb-0.6.2/test/view_test.rb
%{gemdir}/gems/hirb-0.6.2/test/views_test.rb
%doc %{gemdir}/gems/hirb-0.6.2/LICENSE.txt
%{gemdir}/gems/hirb-0.6.2/CHANGELOG.rdoc
%doc %{gemdir}/gems/hirb-0.6.2/README.rdoc
%{gemdir}/gems/hirb-0.6.2/test/deps.rip
%{gemdir}/gems/hirb-0.6.2/Rakefile
%{gemdir}/gems/hirb-0.6.2/.gemspec
%{gemdir}/gems/hirb-0.6.2/.travis.yml


%doc %{gemdir}/doc/hirb-0.6.2
%{gemdir}/cache/hirb-0.6.2.gem
%{gemdir}/specifications/hirb-0.6.2.gemspec

%changelog
