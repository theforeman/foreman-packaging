%global npm_name follow-redirects
%global enable_tests 1

Name: nodejs-%{npm_name}
Version: 1.4.1
Release: 1%{?dist}
Summary: HTTP and HTTPS modules that follow redirects
License: MIT
Group: Development/Libraries
URL: https://github.com/olalonde/follow-redirects
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
Requires: npm(debug) >= 3.1.0
Requires: npm(debug) < 4.0.0
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
%{summary}

%prep
%setup -q -n package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr http.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr https.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr index.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

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
