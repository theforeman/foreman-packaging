%global npm_name es6-promise

Name: nodejs-%{npm_name}
Version: 3.2.1
Release: 1%{?dist}
Summary: A lightweight library that provides tools for organizing asynchronous code
License: MIT
Group: Development/Libraries
URL: https://github.com/jakearchibald/ES6-Promises
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
A lightweight library that provides tools for organizing asynchronous code

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
cp -pfr CHANGELOG.md LICENSE README.md dist lib package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%check

%files
%{nodejs_sitelib}/%{npm_name}
%doc LICENSE

%files doc
%doc CHANGELOG.md
%doc README.md

%changelog
* Wed Aug 31 2016 Dominic Cleal <dominic@cleal.org> 3.2.1-1
- new package built with tito

