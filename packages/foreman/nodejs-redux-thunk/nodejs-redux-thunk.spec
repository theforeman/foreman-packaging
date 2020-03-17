%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name redux-thunk

Name: %{?scl_prefix}nodejs-redux-thunk
Version: 2.3.0
Release: 4%{?dist}
Summary: Thunk middleware for Redux
License: MIT
Group: Development/Libraries
URL: https://github.com/reduxjs/redux-thunk
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
%if 0%{?scl:1}
BuildRequires: %{?scl_prefix_nodejs}npm
%else
BuildRequires: nodejs-packaging
BuildRequires: npm
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
%doc README.md

%changelog
* Tue Mar 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.3.0-4
- Bump packages to build for el8

* Tue Oct 22 2019 Eric D. Helms <ericdhelms@gmail.com> - 2.3.0-3
- Build for SCL

* Fri Oct 04 2019 Eric D. Helms <ericdhelms@gmail.com> - 2.3.0-2
- Update specs to handle SCL

* Wed Jun 06 2018 Eric D. Helms <ericdhelms@gmail.com> 2.3.0-1
- Update to 2.3.0

* Thu Feb 16 2017 Dominic Cleal <dominic@cleal.org> 2.2.0-1
- new package built with tito
