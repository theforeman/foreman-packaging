%global npm_name intl
%global enable_tests 1 

Name: nodejs-%{npm_name}
Version: 1.2.5
Release: 1%{?dist}
Summary: Polyfill the ECMA-402 Intl API (except collation)
License: MIT
URL: https://github.com/andyearnshaw/Intl.js/issues
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
%{summary}

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr CONTRIBUTING.md LICENSE.txt README.md bower.json dist index.js lib locale-data package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%endif

%files
%{nodejs_sitelib}/%{npm_name}

%license LICENSE.txt
%doc CONTRIBUTING.md
%doc LICENSE.txt
%doc README.md

%changelog
* Thu Dec 14 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.2.5-1
- new package built with tito

