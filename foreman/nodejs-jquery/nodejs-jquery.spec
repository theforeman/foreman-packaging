%global npm_name jquery

Name: nodejs-%{npm_name}
Version: 2.2.4
Release: 1%{?dist}
Summary: JavaScript library for DOM operations
License: MIT
Group: Development/Libraries
URL: https://github.com/jquery/jquery.git
Source0: http://registry.npmjs.org/jquery/-/jquery-2.2.4.tgz
Requires: nodejs(engine)
BuildRequires: nodejs-devel
BuildRequires: nodejs-packaging
BuildArch: noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif
Provides: npm(%{npm_name}) = %{version}

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
cp -pfr dist external src *.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%build

%check
%nodejs_symlink_deps --check

%files
%{nodejs_sitelib}/%{npm_name}
%doc LICENSE.txt

%files doc
%doc *.md
%doc *.txt
%exclude %{nodejs_sitelib}/%{npm_name}/.*
%exclude %{nodejs_sitelib}/%{npm_name}/bower.json

%changelog
* Thu Jan 26 2017 Dominic Cleal <dominic@cleal.org> 2.2.4-1
- Update nodejs-jquery to 2.2.4 (dominic@cleal.org)

* Sat Sep 24 2016 Eric D Helms <ericdhelms@gmail.com> 1.11.3-3
- Fix ExclusiveArch for nodejs packages on EL6 (ericdhelms@gmail.com)

* Fri Aug 12 2016 Dominic Cleal <dominic@cleal.org> 1.11.3-2
- Fix pkg/npm_name macro reference (dominic@cleal.org)

* Thu Aug 11 2016 Dominic Cleal <dominic@cleal.org> 1.11.3-1
- new package built with tito

