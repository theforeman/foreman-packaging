%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name react-c3js

Name: %{?scl_prefix}nodejs-react-c3js
Version: 0.1.20
Release: 2%{?dist}
Summary: React component for C3
License: MIT
Group: Development/Libraries
URL: https://github.com/bcbcarl/react-c3js#readme
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
%if 0%{?scl:1}
BuildRequires: %{?scl_prefix_nodejs}npm
%else
BuildRequires: nodejs-packaging
%endif
Requires: %{?scl_prefix}npm(c3) >= 0.4.11
Requires: %{?scl_prefix}npm(c3) < 0.5.0
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
cp -pfr react-c3js.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr src %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%check
%{nodejs_symlink_deps} --check

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE
%doc README.md

%changelog
* Fri Oct 04 2019 Eric D. Helms <ericdhelms@gmail.com> - 0.1.20-2
- Update specs to handle SCL

* Tue Dec 19 2017 Daniel Lobato Garcia <me@daniellobato.me> 0.1.20-1
- new package built with tito
