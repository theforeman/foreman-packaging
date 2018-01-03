%global npm_name moment-timezone
%global enable_tests 1

Name: nodejs-%{npm_name}
Version: 0.5.14
Release: 1%{?dist}
Summary: Parse and display moments in any timezone
License: MIT
Group: Development/Libraries
URL: http://momentjs.com/timezone/
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
Requires: npm(moment) >= 2.9.0
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
%{summary}

%prep
%setup -q -n package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr builds %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr data %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr index.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr moment-timezone-utils.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr moment-timezone.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
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
%doc changelog.md

%changelog
