%global npm_name urijs
%global enable_tests 1

Name: nodejs-%{npm_name}
Version: 1.19.1
Release: 1%{?dist}
Summary: URI
License: MIT
Group: Development/Libraries
URL: http://medialize.github.io/URI.js/
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
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr src %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%endif

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE.txt
%doc CHANGELOG.md
%doc README.md

%changelog
* Wed May 30 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.19.1-1
- Update to 1.19.1

* Fri Jun 23 2017 Eric D. Helms <ericdhelms@gmail.com> 1.18.10-1
- new package built with tito

