%global npm_name d3
%global enable_tests 1

Name: nodejs-%{npm_name}
Version: 3.5.17
Release: 1%{?dist}
Summary: A JavaScript visualization library for HTML and SVG
License: BSD-3-Clause
Group: Development/Libraries
URL: http://d3js.org
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
cp -pfr bin %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr d3.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr d3.min.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
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
%doc CONTRIBUTING.md
%doc README.md

%changelog
* Thu Feb 22 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 3.5.17-1
- new package built with tito

