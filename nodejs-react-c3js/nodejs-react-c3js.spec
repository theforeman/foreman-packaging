%global npm_name react-c3js
%global enable_tests 1

Name: nodejs-%{npm_name}
Version: 0.1.20
Release: 1%{?dist}
Summary: React component for C3
License: MIT
Group: Development/Libraries
URL: https://github.com/bcbcarl/react-c3js#readme
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
Requires: npm(c3) >= 0.4.11
Requires: npm(c3) < 1.0.0
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

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

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%endif

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE
%doc README.md

%changelog
* Tue Dec 19 2017 Daniel Lobato Garcia <me@daniellobato.me> 0.1.20-1
- new package built with tito

