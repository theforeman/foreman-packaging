%global npm_name jquery.cookie

Name: nodejs-%{npm_name}
Version: 1.4.1
Release: 2%{?dist}
Summary: A simple, lightweight jQuery plugin for reading, writing and deleting cookies.
License: MIT
Group: Development/Libraries
URL: https://github.com/carhartl/jquery-cookie
Source0: http://registry.npmjs.org/jquery.cookie/-/jquery.cookie-1.4.1.tgz

BuildRequires: nodejs-devel
BuildRequires: nodejs-packaging
Requires: npm(jquery) >= 1.2.0
BuildArch: noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif
Provides: npm(%{npm_name}) = %{version}

%description
A simple, lightweight jQuery plugin for reading, writing and deleting cookies.

%package doc
Summary: Documentation for nodejs-%{npm_name}
Group: Documentation
Requires: nodejs-%{npm_name} = %{version}-%{release}
BuildArch: noarch

%description doc
This package contains documentation for nodejs-%{npm_name}

%prep
%setup -q -n package

rm -rf node_modules

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr test  *.json *.md *.js *.txt %{buildroot}%{nodejs_sitelib}/%{npm_name}
%nodejs_symlink_deps

%check

%files
%{nodejs_sitelib}/%{npm_name}
%doc %{nodejs_sitelib}/%{npm_name}/MIT-LICENSE.txt


%files doc
%doc %{nodejs_sitelib}/%{npm_name}/README.md
%doc %{nodejs_sitelib}/%{npm_name}/CONTRIBUTING.md
%doc %{nodejs_sitelib}/%{npm_name}/CHANGELOG.md

%changelog
* Sat Sep 24 2016 Eric D Helms <ericdhelms@gmail.com> 1.4.1-2
- Fix ExclusiveArch for nodejs packages on EL6 (ericdhelms@gmail.com)

* Thu Aug 11 2016 Dominic Cleal <dominic@cleal.org> 1.4.1-1
- new package built with tito

