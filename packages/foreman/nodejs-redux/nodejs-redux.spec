%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name redux

Name: %{?scl_prefix}nodejs-redux
Version: 3.7.2
Release: 2%{?dist}
Summary: Predictable state container for JavaScript apps
License: MIT
Group: Development/Libraries
URL: http://redux.js.org
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
%if 0%{?scl:1}
BuildRequires: %{?scl_prefix_nodejs}npm
%else
BuildRequires: nodejs-packaging
%endif
Requires: %{?scl_prefix}npm(lodash) >= 4.2.1
Requires: %{?scl_prefix}npm(lodash) < 5.0.0
Requires: %{?scl_prefix}npm(lodash-es) >= 4.2.1
Requires: %{?scl_prefix}npm(lodash-es) < 5.0.0
Requires: %{?scl_prefix}npm(loose-envify) >= 1.1.0
Requires: %{?scl_prefix}npm(loose-envify) < 2.0.0
Requires: %{?scl_prefix}npm(symbol-observable) >= 1.0.3
Requires: %{?scl_prefix}npm(symbol-observable) < 2.0.0
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch
Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}

%description
%{summary}

%prep
%setup -q -n package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr dist %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr es %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr index.d.ts %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr lib %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr src %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%check
%{nodejs_symlink_deps} --check

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE.md
%doc CHANGELOG.md
%doc README.md

%changelog
* Fri Oct 04 2019 Eric D. Helms <ericdhelms@gmail.com> - 3.7.2-2
- Update specs to handle SCL

* Thu Apr 26 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 3.7.2-1
- Update to 3.7.2

* Thu Feb 16 2017 Dominic Cleal <dominic@cleal.org> 3.6.0-1
- new package built with tito
