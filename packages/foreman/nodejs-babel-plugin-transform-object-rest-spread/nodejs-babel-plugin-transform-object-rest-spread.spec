%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name babel-plugin-transform-object-rest-spread

Name: %{?scl_prefix}nodejs-babel-plugin-transform-object-rest-spread
Version: 6.26.0
Release: 4%{?dist}
Summary: Compile object rest and spread to ES5
License: MIT
Group: Development/Libraries
URL: https://github.com/babel/babel/tree/master/packages/babel-plugin-transform-object-rest-spread
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
%if 0%{?scl:1}
BuildRequires: %{?scl_prefix_nodejs}npm
%else
BuildRequires: nodejs-packaging
%endif
Requires: %{?scl_prefix}npm(babel-plugin-syntax-object-rest-spread) >= 6.8.0
Requires: %{?scl_prefix}npm(babel-plugin-syntax-object-rest-spread) < 7.0.0
Requires: %{?scl_prefix}npm(babel-runtime) >= 6.26.0
Requires: %{?scl_prefix}npm(babel-runtime) < 7.0.0
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch
Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}

%description
%{summary}

%prep
%setup -q -n package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr lib %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%check
%{nodejs_symlink_deps} --check

%files
%{nodejs_sitelib}/%{npm_name}
%doc README.md

%changelog
* Mon Oct 21 2019 Eric D. Helms <ericdhelms@gmail.com> - 6.26.0-4
- Build for SCL

* Thu Oct 10 2019 Eric D. Helms <ericdhelms@gmail.com> - 6.26.0-3
- Update requires for SCL prefix

* Fri Oct 04 2019 Eric D. Helms <ericdhelms@gmail.com> - 6.26.0-2
- Update specs to handle SCL

* Mon May 28 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 6.26.0-1
- Update to 6.26.0

* Fri Oct 14 2016 Dominic Cleal <dominic@cleal.org> 6.16.0-1
- new package built with tito
