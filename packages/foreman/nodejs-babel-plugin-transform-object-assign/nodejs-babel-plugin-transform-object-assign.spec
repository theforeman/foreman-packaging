%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name babel-plugin-transform-object-assign

Name: %{?scl_prefix}nodejs-babel-plugin-transform-object-assign
Version: 6.22.0
Release: 2%{?dist}
Summary: Replace Object
License: MIT
Group: Development/Libraries
URL: https://github.com/babel/babel/tree/master/packages/babel-plugin-transform-object-assign
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
%if 0%{?scl:1}
BuildRequires: %{?scl_prefix_nodejs}npm
%else
BuildRequires: nodejs-packaging
%endif
Requires: npm(babel-runtime) >= 6.22.0
Requires: npm(babel-runtime) < 7.0.0
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
%license LICENSE
%doc README.md

%changelog
* Fri Oct 04 2019 Eric D. Helms <ericdhelms@gmail.com> - 6.22.0-2
- Update specs to handle SCL

* Wed May 30 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 6.22.0-1
- Update to 6.22.0

* Fri Oct 14 2016 Dominic Cleal <dominic@cleal.org> 6.8.0-1
- new package built with tito
