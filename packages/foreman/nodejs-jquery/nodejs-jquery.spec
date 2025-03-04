%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name jquery

Name: %{?scl_prefix}nodejs-jquery
Version: 3.7.1
Release: 1%{?dist}
Summary: JavaScript library for DOM operations
License: MIT
Group: Development/Libraries
URL: https://jquery.com
Source0: https://registry.npmjs.org/jquery/-/jquery-%{version}.tgz
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
cp -pfr dist %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr src %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%check
%{nodejs_symlink_deps} --check

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE.txt
%doc AUTHORS.txt
%doc README.md

%changelog
* Tue Mar 04 2025 Foreman Packaging Automation <packaging@theforeman.org> 3.7.1-1
- Update to 3.7.1

* Tue Mar 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.2.4-4
- Bump packages to build for el8

* Tue Oct 22 2019 Eric D. Helms <ericdhelms@gmail.com> - 2.2.4-3
- Build for SCL

* Fri Oct 04 2019 Eric D. Helms <ericdhelms@gmail.com> - 2.2.4-2
- Update specs to handle SCL

* Thu Jan 26 2017 Dominic Cleal <dominic@cleal.org> 2.2.4-1
- Update nodejs-jquery to 2.2.4 (dominic@cleal.org)

* Sat Sep 24 2016 Eric D Helms <ericdhelms@gmail.com> 1.11.3-3
- Fix ExclusiveArch for nodejs packages on EL6 (ericdhelms@gmail.com)

* Fri Aug 12 2016 Dominic Cleal <dominic@cleal.org> 1.11.3-2
- Fix pkg/npm_name macro reference (dominic@cleal.org)

* Thu Aug 11 2016 Dominic Cleal <dominic@cleal.org> 1.11.3-1
- new package built with tito
