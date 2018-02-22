%global npm_name c3
%global enable_tests 1

Name: nodejs-%{npm_name}
Version: 0.4.11
Release: 2%{?dist}
Summary: D3-based reusable chart library
License: MIT
Group: Development/Libraries
URL: https://github.com/masayuki0812/c3#readme
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
Requires: npm(d3) >= 3.5.0
Requires: npm(d3) < 3.6.0
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
%{summary}

%prep
%setup -q -n package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr Gruntfile.coffee %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr c3.css %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr c3.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr c3.min.css %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr c3.min.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr component.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr extensions %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr spec %{buildroot}%{nodejs_sitelib}/%{npm_name}
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
%doc htdocs

%changelog
* Thu Feb 22 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.4.11-2
- Unbundle nodejs-c3 (ewoud@kohlvanwijngaarden.nl)
- Restructure foreman packages to prepare for obal (pcreech@redhat.com)

* Fri Oct 14 2016 Dominic Cleal <dominic@cleal.org> 0.4.11-1
- new package built with tito

