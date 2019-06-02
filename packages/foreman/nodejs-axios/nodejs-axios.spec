%global npm_name axios

Name: nodejs-axios
Version: 0.19.0
Release: 1%{?dist}
Summary: Promise based HTTP client for the browser and node
License: MIT
Group: Development/Libraries
URL: https://github.com/axios/axios
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
Requires: npm(follow-redirects) = 1.5.10
Requires: npm(is-buffer) >= 2.0.2
Requires: npm(is-buffer) < 3.0.0
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

%check
%{nodejs_symlink_deps} --check

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE
%doc CHANGELOG.md
%doc README.md
%doc UPGRADE_GUIDE.md

%changelog
* Sun Jun 02 2019 Ohad Levy <ohadlevy@gmail.com> 0.19.0-1
- Update to 0.19.0

* Tue Jan 30 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.17.1-1
- new package built with tito

