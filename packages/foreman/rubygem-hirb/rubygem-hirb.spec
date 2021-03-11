%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name hirb

Summary: A mini view framework for console/irb that's easy to use, even while under its influence.
Name: %{?scl_prefix}rubygem-%{gem_name}

Version: 0.7.0
Release: 13%{?dist}
Group: Development/Ruby
License: MIT
URL: http://tagaholic.me/hirb/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems
Requires: %{?scl_prefix_ruby}rubygems
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(hirb) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%global gembuilddir %{buildroot}%{gem_dir}

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
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/LICENSE.txt
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/lib
%exclude %{gem_cache}
%{gem_spec}

%files doc
%{gem_instdir}/test
%{gem_instdir}/Rakefile
%{gem_instdir}/.gemspec
%doc %{gem_instdir}/CHANGELOG.rdoc
%{gem_instdir}/.travis.yml
%{gem_docdir}

%changelog
* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.7.0-13
- Rebuild against rh-ruby27

* Wed Apr 08 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.7.0-12
- Bump to release for EL8

* Wed Sep 05 2018 Eric D. Helms <ericdhelms@gmail.com> - 0.7.0-11
- Rebuild for Rails 5.2 and Ruby 2.5

* Fri Jan 05 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.7.0-10
- More rebuilds for Rails 5.1 (ericdhelms@gmail.com)
- Use HTTPS URLs for github and rubygems (ewoud@kohlvanwijngaarden.nl)
- Set proper download URLs for rubygems (komidore64@gmail.com)

* Wed May 04 2016 Dominic Cleal <dominic@cleal.org> 0.7.0-9
- Use gem_install macro (dominic@cleal.org)

* Tue Dec 22 2015 Dominic Cleal <dcleal@redhat.com> 0.7.0-8
- Replace ruby(abi) for ruby22 rebuild (dcleal@redhat.com)

* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 0.7.0-7
- Converted to tfm SCL (dcleal@redhat.com)
- Fixes #9703 - change %%{dist} to %%{?dist} (jmontleo@redhat.com)
- Add full rubygems.org source URL (dcleal@redhat.com)

* Thu Jul 04 2013 Dominic Cleal <dcleal@redhat.com> 0.7.0-6
- change ruby(abi) to ruby(release) for F19+ (dcleal@redhat.com)
- delete all zero sized tito.props (msuchy@redhat.com)
- with recent tito you do not need SCL meta package (msuchy@redhat.com)

* Wed Mar 13 2013 Miroslav Suchý <msuchy@redhat.com> 0.7.0-4
- new package built with tito

* Tue Sep 11 2012 Miroslav Suchý <msuchy@redhat.com> 0.7.0-3
- add gem file to src.rpm (msuchy@redhat.com)

* Tue Sep 11 2012 Miroslav Suchý <msuchy@redhat.com> 0.7.0-2
- new package built with tito
