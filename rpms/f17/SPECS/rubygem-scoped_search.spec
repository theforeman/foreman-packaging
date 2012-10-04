# Generated from scoped_search-2.3.6.gem by gem2rpm -*- rpm-spec -*-
%global gem_name scoped_search
%global rubyabi 1.9.1

Summary: Easily search you ActiveRecord models with a simple query language using a named scope
Name: rubygem-%{gem_name}
Version: 2.3.7
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://github.com/wvanbergen/scoped_search/wiki
Source0: %{gem_name}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
Requires: ruby 
Requires: rubygem(activerecord) >= 2.1.0
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

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
/usr/share/gems/gems/scoped_search-2.3.7/
%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.rdoc

%changelog
* Thu Jun 14 2012 jason - 2.3.6-1
- Initial package
