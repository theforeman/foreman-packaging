%global npm_name dotenv
%global enable_tests 1

Name: nodejs-%{npm_name}
Version: 5.0.1
Release: 1%{?dist}
Summary: Loads environment variables from .env for nodejs projects
License: BSD-2-Clause
Group: Development/Libraries
URL: https://github.com/motdotla/dotenv#readme
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
cp -pfr config.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
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

%changelog
* Wed Apr 25 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 5.0.1-1
- Update to 5.0.1

* Tue Nov 07 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 2.0.0-1
- new package built with tito

