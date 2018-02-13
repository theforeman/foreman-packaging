%global npm_name expose-loader

Name: nodejs-%{npm_name}
Version: 0.6.0
Release: 2%{?dist}
Summary: expose loader module for webpack
License: MIT
Group: Development/Libraries
URL: https://github.com/webpack/expose-loader
Source0: http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
Requires: nodejs(engine)
BuildRequires: nodejs-devel
BuildRequires: nodejs-packaging
BuildRequires: npm
BuildArch: noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif
Provides: npm(%{npm_name}) = %{version}
%{?nodejs_find_provides_and_requires}

%description
expose loader module for webpack

%package doc
Summary: Documentation for nodejs-%{npm_name}
Group: Documentation
Requires: nodejs-%{npm_name} = %{version}-%{release}
BuildArch: noarch

%description doc
This package contains documentation for nodejs-%{npm_name}

%prep
%setup -q -n package

%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr README.md index.js package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
%nodejs_symlink_deps

%check

%files
%{nodejs_sitelib}/%{npm_name}

%files doc
%doc README.md

%changelog
* Sat Sep 24 2016 Eric D Helms <ericdhelms@gmail.com> 0.6.0-2
- Fix ExclusiveArch for nodejs packages on EL6 (ericdhelms@gmail.com)

* Thu Aug 11 2016 Dominic Cleal <dominic@cleal.org> 0.6.0-1
- new package built with tito

