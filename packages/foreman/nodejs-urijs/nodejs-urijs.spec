%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name urijs

Name: %{?scl_prefix}nodejs-urijs
Version: 1.19.1
Release: 2%{?dist}
Summary: URI
License: MIT
Group: Development/Libraries
URL: http://medialize.github.io/URI.js/
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
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr src %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%check
%{nodejs_symlink_deps} --check

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE.txt
%doc CHANGELOG.md
%doc README.md

%changelog
* Fri Oct 04 2019 Eric D. Helms <ericdhelms@gmail.com> - 1.19.1-2
- Update specs to handle SCL

* Wed May 30 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.19.1-1
- Update to 1.19.1

* Fri Jun 23 2017 Eric D. Helms <ericdhelms@gmail.com> 1.18.10-1
- new package built with tito
