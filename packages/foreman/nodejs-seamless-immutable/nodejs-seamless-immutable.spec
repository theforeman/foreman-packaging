%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name seamless-immutable

Name: %{?scl_prefix}nodejs-seamless-immutable
Version: 7.1.3
Release: 2%{?dist}
Summary: Immutable data structures for JavaScript which are backwards-compatible with normal JS Arrays and Objects
License: BSD-3-Clause
Group: Development/Libraries
URL: https://github.com/rtfeldman/seamless-immutable
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
%if 0%{?scl:1}
BuildRequires: %{?scl_prefix_nodejs}npm
%else
BuildRequires: nodejs-packaging
%endif
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch
Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}

%description
%{summary}

%prep
%setup -q -n package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr seamless-immutable.development.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr seamless-immutable.development.min.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr seamless-immutable.production.min.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr src %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%check
%{nodejs_symlink_deps} --check

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE
%doc README.md

%changelog
* Fri Oct 04 2019 Eric D. Helms <ericdhelms@gmail.com> - 7.1.3-2
- Update specs to handle SCL

* Fri Apr 27 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 7.1.3-1
- Update to 7.1.3

* Thu Feb 16 2017 Dominic Cleal <dominic@cleal.org> 7.0.1-1
- new package built with tito
