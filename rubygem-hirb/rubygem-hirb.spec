%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name hirb

Summary: A mini view framework for console/irb that's easy to use, even while under its influence.
Name: %{?scl_prefix}rubygem-%{gem_name}

Version: 0.7.0
Release: 6%{?dist}
Group: Development/Ruby
License: MIT
URL: http://tagaholic.me/hirb/
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem
%if 0%{?fedora} > 18
Requires: %{?scl_prefix}ruby(release)
%else
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
%endif
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygems
Requires: %{?scl_prefix}rubygems
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(hirb) = %{version}

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
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%setup -n %{pkg_name}-%{version} -T -c

%build

%install
mkdir -p %{gembuilddir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir %{gembuilddir} --force %{SOURCE0}
%{?scl:"}

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

