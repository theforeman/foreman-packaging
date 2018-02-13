%global npm_name jstz

Name: nodejs-%{npm_name}
Version: 1.0.7
Release: 2%{?dist}
Summary: Timezone detection for JavaScript
License: MIT
Group: Development/Libraries
URL: https://github.com/iansinnott/jstz
Source0: http://registry.npmjs.org/jstz/-/jstz-1.0.7.tgz

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
Timezone detection for JavaScript

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
cp -pfr dist utilities  *.json *.md *.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
#if any binaries are included, symlink them to bindir here
mkdir -p %{buildroot}%{_bindir}

%nodejs_symlink_deps

%check

%files
%{nodejs_sitelib}/%{npm_name}
%exclude %{nodejs_sitelib}/%{npm_name}/README.md
%doc LICENCE

%files doc
%doc README.md

%changelog
* Sat Sep 24 2016 Eric D Helms <ericdhelms@gmail.com> 1.0.7-2
- Fix ExclusiveArch for nodejs packages on EL6 (ericdhelms@gmail.com)

* Thu Aug 11 2016 Dominic Cleal <dominic@cleal.org> 1.0.7-1
- new package built with tito

