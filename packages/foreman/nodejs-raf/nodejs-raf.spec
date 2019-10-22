%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name raf

Name: %{?scl_prefix}nodejs-raf
Version: 3.4.0
Release: 4%{?dist}
Summary: requestAnimationFrame polyfill for node and the browser
License: MIT
Group: Development/Libraries
URL: https://github.com/chrisdickinson/raf#readme
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
%if 0%{?scl:1}
BuildRequires: %{?scl_prefix_nodejs}npm
%else
BuildRequires: nodejs-packaging
%endif
Requires: %{?scl_prefix}npm(performance-now) >= 2.1.0
Requires: %{?scl_prefix}npm(performance-now) < 3.0.0
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
cp -pfr polyfill.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr test.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr window.js %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%check
%{nodejs_symlink_deps} --check

%files
%{nodejs_sitelib}/%{npm_name}
%doc README.md

%changelog
* Tue Oct 22 2019 Eric D. Helms <ericdhelms@gmail.com> - 3.4.0-4
- Build for SCL

* Fri Oct 04 2019 Eric D. Helms <ericdhelms@gmail.com> - 3.4.0-3
- Update specs to handle SCL

* Sun Nov 19 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 3.4.0-2
- Set explicit dependencies for nodejs-raf (ewoud@kohlvanwijngaarden.nl)

* Tue Nov 07 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 3.4.0-1
- new package built with tito
