%global npm_name moment
%global enable_tests 1

Name: nodejs-%{npm_name}
Version: 2.14.1
Release: 1%{?dist}
Summary: Parse, validate, manipulate, and display dates
License: MIT
Group: Development/Libraries
URL: http://momentjs.com
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
%{summary}

%prep
%setup -q -n package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr ender.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr locale %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr min %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr moment.d.ts %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr moment.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr src %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%endif

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE
%doc CHANGELOG.md
%doc README.md

%changelog
* Thu Jan 26 2017 Dominic Cleal <dominic@cleal.org> 2.17.1-1
- new package built with tito

