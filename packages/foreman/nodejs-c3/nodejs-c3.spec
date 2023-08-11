%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name c3

Name: %{?scl_prefix}nodejs-c3
Version: 0.4.24
Release: 1%{?dist}
Summary: D3-based reusable chart library
License: MIT
Group: Development/Libraries
URL: https://github.com/c3js/c3#readme
Source0: https://registry.npmjs.org/c3/-/c3-%{version}.tgz
%if 0%{?!scl:1}
BuildRequires: nodejs-packaging
%endif
Requires: npm(d3) >= 3.5.0
Requires: npm(d3) < 3.6.0
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch
Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}

%description
%{summary}

%prep
%setup -q -n package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr c3.css %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr c3.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr c3.min.css %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr c3.min.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr component.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr extensions %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr rollup.config.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr spec %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr src %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%check
%{nodejs_symlink_deps} --check

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE
%doc CONTRIBUTING.md
%doc MAINTAINANCE.md
%doc README.md
%doc htdocs

%changelog
* Fri Aug 11 2023 Foreman Packaging Automation <packaging@theforeman.org> 0.4.24-1
- Update to 0.4.24

* Tue Mar 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.4.11-6
- Bump packages to build for el8

* Mon Oct 21 2019 Eric D. Helms <ericdhelms@gmail.com> - 0.4.11-5
- Build for SCL

* Thu Oct 10 2019 Eric D. Helms <ericdhelms@gmail.com> - 0.4.11-4
- Update requires for SCL prefix

* Fri Oct 04 2019 Eric D. Helms <ericdhelms@gmail.com> - 0.4.11-3
- Update specs to handle SCL

* Thu Feb 22 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.4.11-2
- Unbundle nodejs-c3 (ewoud@kohlvanwijngaarden.nl)
- Restructure foreman packages to prepare for obal (pcreech@redhat.com)

* Fri Oct 14 2016 Dominic Cleal <dominic@cleal.org> 0.4.11-1
- new package built with tito
