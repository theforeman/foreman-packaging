%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name classnames

Name: %{?scl_prefix}nodejs-classnames
Version: 2.2.5
Release: 4%{?dist}
Summary: A simple utility for conditionally joining classNames together
License: MIT
Group: Development/Libraries
URL: https://github.com/JedWatson/classnames#readme
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
%if 0%{?scl:1}
BuildRequires: %{?scl_prefix_nodejs}npm
%else
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
cp -pfr bind.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr dedupe.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr index.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%check
%{nodejs_symlink_deps} --check

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE
%doc CONTRIBUTING.md
%doc HISTORY.md
%doc README.md

%changelog
* Wed Mar 18 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.2.5-4
- Bump releases to build for el8

* Mon Oct 21 2019 Eric D. Helms <ericdhelms@gmail.com> - 2.2.5-3
- Build for SCL

* Fri Oct 04 2019 Eric D. Helms <ericdhelms@gmail.com> - 2.2.5-2
- Update specs to handle SCL

* Wed Nov 08 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 2.2.5-1
- new package built with tito
