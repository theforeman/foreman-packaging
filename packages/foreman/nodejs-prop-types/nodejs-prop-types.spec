%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name prop-types

Name: %{?scl_prefix}nodejs-prop-types
Version: 15.6.2
Release: 4%{?dist}
Summary: Runtime type checking for React props and similar objects
License: MIT
Group: Development/Libraries
URL: https://facebook.github.io/react/
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
%if 0%{?scl:1}
BuildRequires: %{?scl_prefix_nodejs}npm
%else
BuildRequires: nodejs-packaging
BuildRequires: npm
%endif
Requires: %{?scl_prefix}npm(loose-envify) >= 1.3.1
Requires: %{?scl_prefix}npm(loose-envify) < 2.0.0
Requires: %{?scl_prefix}npm(object-assign) >= 4.1.1
Requires: %{?scl_prefix}npm(object-assign) < 5.0.0
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch
Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}

%description
%{summary}

%prep
%setup -q -n package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr checkPropTypes.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr factory.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr factoryWithThrowingShims.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr factoryWithTypeCheckers.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr index.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr lib %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr prop-types.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr prop-types.min.js %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%check
%{nodejs_symlink_deps} --check

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE
%doc CHANGELOG.md
%doc README.md

%changelog
* Tue Mar 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 15.6.2-4
- Bump packages to build for el8

* Tue Oct 22 2019 Eric D. Helms <ericdhelms@gmail.com> - 15.6.2-3
- Build for SCL

* Fri Oct 04 2019 Eric D. Helms <ericdhelms@gmail.com> - 15.6.2-2
- Update specs to handle SCL

* Wed Oct 10 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 15.6.2-1
- Update to 15.6.2

* Wed Jun 06 2018 Eric D. Helms <ericdhelms@gmail.com> 15.6.1-1
- Update to 15.6.1

* Thu Nov 23 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 15.6.0-2
- Unbundle nodejs-prop-types (github@kohlvanwijngaarden.nl)

* Thu Oct 05 2017 Eric D. Helms <ericdhelms@gmail.com> 15.6.0-1
- Update prop-types to 15.5.9 (me@daniellobato.me)

* Thu May 11 2017 Dominic Cleal <dominic@cleal.org> 15.5.9-1
- new package built with tito
