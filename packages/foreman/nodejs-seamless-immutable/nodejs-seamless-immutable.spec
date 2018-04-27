%global npm_name seamless-immutable
%global enable_tests 1

Name: nodejs-%{npm_name}
Version: 7.1.3
Release: 1%{?dist}
Summary: Immutable backwards-compatible data structures for JavaScript
License: BSD
Group: Development/Libraries
URL: https://github.com/rtfeldman/seamless-immutable
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
Immutable data structures for JavaScript which are backwards-compatible with
normal JS Arrays and Objects.

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

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%endif

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE
%doc README.md

%changelog
* Fri Apr 27 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 7.1.3-1
- Update to 7.1.3

* Thu Feb 16 2017 Dominic Cleal <dominic@cleal.org> 7.0.1-1
- new package built with tito

