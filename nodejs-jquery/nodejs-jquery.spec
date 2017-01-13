%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name jquery

Name: %{?scl_prefix}nodejs-%{npm_name}
Version: 1.11.3
Release: 3%{?dist}
Summary: JavaScript library for DOM operations
License: MIT
Group: Development/Libraries
URL: https://github.com/jquery/jquery.git
Source0: http://registry.npmjs.org/jquery/-/jquery-1.11.3.tgz
Requires: %{?scl_prefix_nodejs}nodejs(engine)
BuildRequires: %{?scl_prefix_nodejs}nodejs-devel
BuildArch: noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif
Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}

%description
JavaScript library for DOM operations

%package doc
Summary: Documentation for nodejs-%{npm_name}
Group: Documentation
Requires: nodejs-%{npm_name} = %{version}-%{release}
BuildArch: noarch

%description doc
This package contains documentation for nodejs-%{npm_name}.

%prep
%setup -q -n package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr dist src *.json *.md *.txt %{buildroot}%{nodejs_sitelib}/%{npm_name}

%build

%check
%nodejs_symlink_deps --check

%files
%{nodejs_sitelib}/%{npm_name}

%files doc
%doc %{nodejs_sitelib}/%{npm_name}/*.md
%doc %{nodejs_sitelib}/%{npm_name}/*.txt
%exclude %{nodejs_sitelib}/%{npm_name}/.*
%exclude %{nodejs_sitelib}/%{npm_name}/bower.json

%changelog
* Sat Sep 24 2016 Eric D Helms <ericdhelms@gmail.com> 1.11.3-3
- Fix ExclusiveArch for nodejs packages on EL6 (ericdhelms@gmail.com)

* Fri Aug 12 2016 Dominic Cleal <dominic@cleal.org> 1.11.3-2
- Fix pkg/npm_name macro reference (dominic@cleal.org)

* Thu Aug 11 2016 Dominic Cleal <dominic@cleal.org> 1.11.3-1
- new package built with tito

