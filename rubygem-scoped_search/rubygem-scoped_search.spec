%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name scoped_search

Summary: Easily search your ActiveRecord models
Name: %{?scl_prefix}rubygem-%{gem_name}

Version: 3.2.1
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/wvanbergen/scoped_search/wiki
Source0: https://rubygems.org/downloads/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}rubygems
Requires: %{?scl_prefix}rubygem-activerecord >= 3.2.0
BuildRequires: %{?scl_prefix}ruby
BuildRequires: %{?scl_prefix}rubygems
%if 0%{?fedora} > 18
Requires: %{?scl_prefix}ruby(release)
%else
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
%endif
BuildRequires: %{?scl_prefix}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(scoped_search) = %{version}

# for check section
%if 0%{?fedora} > 21
BuildRequires: %{?scl_prefix}rubygem(rspec) >= 3.0
BuildRequires: %{?scl_prefix}rubygem(rspec) < 4.0
BuildRequires: %{?scl_prefix}rubygem(activerecord)
BuildRequires: %{?scl_prefix}rubygem(sqlite3)
%endif

%description
Scoped search makes it easy to search your ActiveRecord-based models. It will
create a named scope :search_for that can be called with a query string. It
will build an SQL query using the provided query string and a definition that
specifies on what fields to search. Because the functionality is built on
named_scope, the result of the search_for call can be used like any other
named_scope, so it can be chained with another scope or combined with
will_paginate. Because it uses standard SQL, it does not require any setup,
indexers or daemons. This makes scoped_search suitable to quickly add basic
search functionality to your application with little hassle. On the other hand,
it may not be the best choice if it is going to be used on very large data sets
or by a large user base.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.


%prep
%{?scl:scl enable %{scl} "}
gem unpack %{SOURCE0}
%{?scl:"}
%setup -q -D -T -n  %{gem_name}-%{version}
%{?scl:scl enable %{scl} "}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:"}

%build
mkdir -p .%{gem_dir}

%{?scl:scl enable %{scl} "}
# Create the gem as gem install only works on a gem file
%{?scl:"}
%{?scl:scl enable %{scl} "}
gem build %{gem_name}.gemspec
%{?scl:"}

%{?scl:scl enable %{scl} "}
gem install -V \
        --local \
        --install-dir ./%{gem_dir} \
        --force \
        --rdoc \
        %{gem_name}-%{version}.gem
%{?scl:"}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/
rm -rf %{buildroot}%{gem_dir}/gems/%{gem_name}-%{version}/{.yardoc,.gitignore,.infinity_test,.travis.yml}
mv %{buildroot}%{gem_instdir}/{LICENSE,*.rdoc} ./
rm %{buildroot}%{gem_cache}

%check
pushd .%{gem_instdir}
# Get rid of Bundler, not needed on Fedora.
sed -i "/require 'bundler\/setup'/ d" spec/spec_helper.rb
# sqlite3-ruby and sqlite3 are identical rubygems, where the former is
# older name for the gem. Would be nice if upstream support both
# reincarnations.
# do not test on postgresql and ruby
sed '5,15d' -i spec/database.ruby.yml
# tests require rspec 3, only on F22+
%if 0%{?fedora} > 21
%{?scl:scl enable %{scl} "}
rspec spec
%{?scl:"}
%endif
popd

%files
%doc LICENSE
%dir %{gem_instdir}
%{gem_instdir}/lib
%{gem_instdir}/app
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc CHANGELOG.rdoc CONTRIBUTING.rdoc README.rdoc
%{gem_instdir}/Rakefile
%{gem_instdir}/Gemfile*
%{gem_instdir}/spec
%{gem_instdir}/%{gem_name}.gemspec

%changelog
* Wed Jun 24 2015 Dominic Cleal <dcleal@redhat.com> 3.2.1-1
- Update scoped_search to 3.2.1 (dcleal@redhat.com)

* Mon May 11 2015 Dominic Cleal <dcleal@redhat.com> 3.2.0-2
- Fix ruby(abi) requirement on F19 (dcleal@redhat.com)

* Mon May 11 2015 Dominic Cleal <dcleal@redhat.com> 3.2.0-1
- Update scoped_search to 3.2.0 (dcleal@redhat.com)

* Mon Mar 24 2014 Dominic Cleal <dcleal@redhat.com> 2.7.1-1
- rebase to 2.7.1 release (dcleal@redhat.com)

* Mon Mar 10 2014 Dominic Cleal <dcleal@redhat.com> 2.6.5-1
- rebase to 2.6.5 release (dcleal@redhat.com)

* Wed Feb 12 2014 Dominic Cleal <dcleal@redhat.com> 2.6.3-1
- rebase to 2.6.3 release (dcleal@redhat.com)

* Mon Feb 10 2014 Dominic Cleal <dcleal@redhat.com> 2.6.2-1
- rebase to 2.6.2 release (dcleal@redhat.com)

* Thu Jun 20 2013 Miroslav Suchý <msuchy@redhat.com> 2.6.0-1
- rebase to 2.6.0 release (msuchy@redhat.com)

* Wed Apr 03 2013 Miroslav Suchý <msuchy@redhat.com> 2.5.1-3
- fix files section (msuchy@redhat.com)

* Wed Apr 03 2013 Miroslav Suchý <msuchy@redhat.com> 2.5.1-2
- fix files section (msuchy@redhat.com)

* Wed Apr 03 2013 Miroslav Suchý <msuchy@redhat.com> 2.5.1-1
- rebase to scoped_search 2.5.1 (msuchy@redhat.com)

* Tue Apr 02 2013 Miroslav Suchý <msuchy@redhat.com> 2.5.0-1
- rebase to scoped_search-2.5.0 (msuchy@redhat.com)

* Thu Mar 28 2013 Miroslav Suchý <msuchy@redhat.com> 2.4.1-3
- include vendor in file list (msuchy@redhat.com)

* Thu Mar 28 2013 Miroslav Suchý <msuchy@redhat.com> 2.4.1-2
- include assets in file list (msuchy@redhat.com)

* Thu Mar 28 2013 Miroslav Suchý <msuchy@redhat.com> 2.4.1-1
- rebase to scoped_search-2.4.1 (msuchy@redhat.com)
- require ruby193-build for tagging (msuchy@redhat.com)

* Wed Feb 27 2013 Miroslav Suchý <msuchy@redhat.com> 2.4.0-6
- new package built with tito

* Mon Dec 03 2012 Miroslav Suchý <msuchy@redhat.com> 2.4.0-5
- run test only on F18+ (msuchy@redhat.com)
- enable tests (msuchy@redhat.com)

* Tue Oct 30 2012 Miroslav Suchý <msuchy@redhat.com> 2.4.0-4
- do not run test on rhel6 at all due missing rspec (msuchy@redhat.com)

* Tue Oct 30 2012 Miroslav Suchý <msuchy@redhat.com> 2.4.0-3
- remove .travis.yml, add Gemfile.activerecord* (msuchy@redhat.com)

* Mon Oct 29 2012 Miroslav Suchý <msuchy@redhat.com> 2.4.0-2
- do not run test, because it is not working (msuchy@redhat.com)
- disable testing on other backend but sqllite (msuchy@redhat.com)
- update to recent scoped_search-2.4.0.gem (msuchy@redhat.com)

* Tue Oct 16 2012 Miroslav Suchý <msuchy@redhat.com> 2.4.0-1
- update to recent scoped_search-2.4.0.gem (msuchy@redhat.com)

* Wed Aug 15 2012 Miroslav Suchý <msuchy@redhat.com> 2.3.7-10
- 847504 - move gemspec to -doc subpackage (msuchy@redhat.com)

* Wed Aug 15 2012 Miroslav Suchý <msuchy@redhat.com> 2.3.7-9
- test suite is failing on F17 a lot - disable for now (msuchy@redhat.com)
- 847504 - use test suite (msuchy@redhat.com)
- 847504 - remove dot files in %%install section (msuchy@redhat.com)
- 847504 - use macro in SOURCE0 (msuchy@redhat.com)

* Tue Aug 14 2012 Miroslav Suchý <msuchy@redhat.com> 2.3.7-8
- 847504 - put in front of chmod link to github issue (msuchy@redhat.com)
- 847504 - fix typo in summary (msuchy@redhat.com)

* Tue Aug 14 2012 Miroslav Suchý <msuchy@redhat.com> 2.3.7-7
- 847504 - remove cached gem (msuchy@redhat.com)
- 847504 - correctly use dist tag (msuchy@redhat.com)
- 847504 - rewrap description (msuchy@redhat.com)

* Sun Aug 12 2012 Miroslav Suchý <msuchy@redhat.com> 2.3.7-6
- fix spelling error (msuchy@redhat.com)
- module scoped_search.rb should not be executable (msuchy@redhat.com)

* Sun Aug 12 2012 Miroslav Suchý <msuchy@redhat.com> 2.3.7-5
- buildroot is not needed (msuchy@redhat.com)
- change Group to valid item (msuchy@redhat.com)

* Fri Aug 10 2012 Miroslav Suchý <msuchy@redhat.com> 2.3.7-4
- there is no need to require rubygems in some version (msuchy@redhat.com)

* Fri Aug 10 2012 Miroslav Suchý <msuchy@redhat.com> 2.3.7-3
- there is no need to require rubygems in some version (msuchy@redhat.com)

* Thu Aug 09 2012 Miroslav Suchý <msuchy@redhat.com> 2.3.7-2
- fix filelist (msuchy@redhat.com)
- create doc subpackage (msuchy@redhat.com)
- fix requirements (msuchy@redhat.com)

* Thu Aug 09 2012 Miroslav Suchý <msuchy@redhat.com> 2.3.7-1
- edit rubygem-scoped_search.spec according guidelines (msuchy@redhat.com)
- import rubygem-scoped_search.spec from foreman-rpms (msuchy@redhat.com)

