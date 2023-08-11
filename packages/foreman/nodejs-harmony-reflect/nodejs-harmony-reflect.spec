%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name harmony-reflect

Name: %{?scl_prefix}nodejs-harmony-reflect
Version: 1.6.2
Release: 1%{?dist}
Summary: ES5 shim for ES6 (ECMAScript 6) Reflect and Proxy objects
License: (Apache-2.0 OR MPL-1.1)
Group: Development/Libraries
URL: https://github.com/tvcutsem/harmony-reflect
Source0: https://registry.npmjs.org/harmony-reflect/-/harmony-reflect-%{version}.tgz
%if 0%{?!scl:1}
BuildRequires: nodejs-packaging
%endif
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch
Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}

%description
%{summary}

%prep
%setup -q -n package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr index.d.ts %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr reflect.js %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%check
%{nodejs_symlink_deps} --check

%files
%{nodejs_sitelib}/%{npm_name}
%doc README.md

%changelog
* Fri Aug 11 2023 Foreman Packaging Automation <packaging@theforeman.org> 1.6.2-1
- Update to 1.6.2

* Tue Mar 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.5.1-5
- Bump packages to build for el8

* Tue Oct 22 2019 Eric D. Helms <ericdhelms@gmail.com> - 1.5.1-4
- Build for SCL

* Fri Oct 04 2019 Eric D. Helms <ericdhelms@gmail.com> - 1.5.1-3
- Update specs to handle SCL

* Wed Sep 12 2018 Bryan Kearney <bryan.kearney@gmail.com> - 1.5.1-2
- Use ASL 2.0 instead of Apache 2.0 or Apache-2.0

* Tue Nov 07 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.5.1-1
- new package built with tito
