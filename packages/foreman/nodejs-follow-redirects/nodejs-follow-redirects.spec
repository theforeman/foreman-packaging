%global npm_name follow-redirects

Name: nodejs-follow-redirects
Version: 1.5.10
Release: 1%{?dist}
Summary: HTTP and HTTPS modules that follow redirects
License: MIT
Group: Development/Libraries
URL: https://github.com/follow-redirects/follow-redirects
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
Requires: npm(debug) = 3.1.0
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

%check
%{nodejs_symlink_deps} --check

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE
%doc README.md

%changelog
* Mon Jun 03 2019 Ohad Levy <ohadlevy@gmail.com> 1.5.10-1
- Update to 1.5.10

* Tue Jan 30 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.4.1-1
- new package built with tito

