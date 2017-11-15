%global npm_name identity-obj-proxy
%global enable_tests 1

Name: nodejs-%{npm_name}
Version: 3.0.0
Release: 2%{?dist}
Summary: an identity object using ES6 proxies
License: MIT
Group: Development/Libraries
URL: https://github.com/keyanzhang/identity-obj-proxy#readme
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

Requires: npm(harmony-reflect) >= 1.4.6
Requires: npm(harmony-reflect) < 2.0.0

%description
%{summary}

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr LICENSE README.md package.json src %{buildroot}%{nodejs_sitelib}/%{npm_name}

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
* Tue Nov 07 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 3.0.0-1
- new package built with tito

