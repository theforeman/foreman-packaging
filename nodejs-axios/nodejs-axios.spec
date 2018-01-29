%global npm_name axios
%global enable_tests 1

Name: nodejs-%{npm_name}
Version: 0.17.1
Release: 1%{?dist}
Summary: Promise based HTTP client for the browser and node
License: MIT
Group: Development/Libraries
URL: https://github.com/axios/axios
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
Requires: npm(follow-redirects) >= 1.2.5
Requires: npm(follow-redirects) < 2.0.0
Requires: npm(is-buffer) >= 1.1.5
Requires: npm(is-buffer) < 2.0.0
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
%{summary}

%prep
%setup -q -n package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr dist %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr index.d.ts %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr index.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr lib %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

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
%doc UPGRADE_GUIDE.md

%changelog
