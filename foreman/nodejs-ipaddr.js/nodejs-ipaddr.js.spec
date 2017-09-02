%global npm_name ipaddr.js
%global enable_tests 1

%{?nodejs_find_provides_and_requires}

Name: nodejs-%{npm_name}
Version: 1.2.0
Release: 1%{?dist}
Summary: A library for manipulating IPv4 and IPv6 addresses in JavaScript
License: MIT
URL: https://github.com/whitequark/ipaddr.js 
Source0: http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
BuildArch:  noarch

%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

%{?nodejs_find_provides_and_requires}

%description
%{summary}

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
cp -pfr .npmignore .travis.yml Cakefile LICENSE README.md bower.json ipaddr.min.js lib package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%endif

%files
%{nodejs_sitelib}/%{npm_name}
%doc LICENSE

%files doc
%doc README.md

%changelog
* Wed Sep 07 2016 Dominic Cleal <dominic@cleal.org> 1.2.0-1
- new package built with tito

