%global npm_name raf
%global enable_tests 0

Name: nodejs-%{npm_name}
Version: 3.4.0
Release: 2%{?dist}
Summary: requestAnimationFrame polyfill for node and the browser
License: MIT
Group: Development/Libraries
URL: https://github.com/chrisdickinson/raf
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

Requires: npm(performance-now) >= 2.1.0
Requires: npm(performance-now) < 3.0.0

%description
%{summary}

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr README.md index.js package.json polyfill.js test.js window.js %{buildroot}%{nodejs_sitelib}/%{npm_name}


%nodejs_symlink_deps

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%endif

%files
%{nodejs_sitelib}/%{npm_name}
%doc README.md

%changelog
* Tue Nov 07 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 3.4.0-1
- new package built with tito

