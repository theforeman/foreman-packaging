# Generated from hirb-0.6.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name hirb
%global rubyabi 1.9.1

Summary: A mini view framework for console/irb that's easy to use, even while under its influence
Name: rubygem-%{gem_name}
Version: 0.6.2
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://tagaholic.me/hirb/
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) >= 1.3.5
Requires: ruby
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: rubygems-devel >= 1.3.5
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

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
/usr/share/gems/gems/hirb-0.6.2/.gemspec
/usr/share/gems/gems/hirb-0.6.2/.travis.yml
/usr/share/gems/gems/hirb-0.6.2/CHANGELOG.rdoc
/usr/share/gems/gems/hirb-0.6.2/Rakefile
/usr/share/gems/gems/hirb-0.6.2/test/
%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/LICENSE.txt

%changelog
* Thu Jun 14 2012 jason - 0.6.2-1
- Initial package
