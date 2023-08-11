%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name js-tokens

Name: %{?scl_prefix}nodejs-js-tokens
Version: 4.0.0
Release: 1%{?dist}
Summary: A regex that tokenizes JavaScript
License: MIT
Group: Development/Libraries
URL: https://github.com/lydell/js-tokens#readme
Source0: https://registry.npmjs.org/js-tokens/-/js-tokens-%{version}.tgz
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
cp -pfr index.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%check
%{nodejs_symlink_deps} --check

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE
%doc CHANGELOG.md
%doc README.md

%changelog
* Fri Aug 11 2023 Foreman Packaging Automation <packaging@theforeman.org> 4.0.0-1
- Update to 4.0.0

* Tue Mar 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.0.2-4
- Bump packages to build for el8

* Tue Oct 22 2019 Eric D. Helms <ericdhelms@gmail.com> - 3.0.2-3
- Build for SCL

* Fri Oct 04 2019 Eric D. Helms <ericdhelms@gmail.com> - 3.0.2-2
- Update specs to handle SCL

* Wed Oct 18 2017 Eric D. Helms <ericdhelms@gmail.com> 3.0.2-1
- new package built with tito
