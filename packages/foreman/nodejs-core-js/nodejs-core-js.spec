%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name core-js

Name: %{?scl_prefix}nodejs-core-js
Version: 2.6.12
Release: 1%{?dist}
Summary: Standard library
License: MIT
Group: Development/Libraries
URL: https://github.com/zloirock/core-js#readme
Source0: https://registry.npmjs.org/core-js/-/core-js-%{version}.tgz
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
cp -pfr build %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr client %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr core %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr es5 %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr es6 %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr es7 %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr fn %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr index.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr library %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr postinstall.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr shim.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr stage %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr web %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%check
%{nodejs_symlink_deps} --check

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE
%doc CHANGELOG.md
%doc README.md

%changelog
* Fri Aug 11 2023 Foreman Packaging Automation <packaging@theforeman.org> 2.6.12-1
- Update to 2.6.12

* Tue Mar 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.5.5-4
- Bump packages to build for el8

* Mon Oct 21 2019 Eric D. Helms <ericdhelms@gmail.com> - 2.5.5-3
- Build for SCL

* Fri Oct 04 2019 Eric D. Helms <ericdhelms@gmail.com> - 2.5.5-2
- Update specs to handle SCL

* Thu Apr 26 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 2.5.5-1
- Add nodejs-core-js generated by npm2rpm using the single strategy
