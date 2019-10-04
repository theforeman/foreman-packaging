%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name webpack-stats-plugin

Name: %{?scl_prefix}nodejs-webpack-stats-plugin
Version: 0.1.5
Release: 2%{?dist}
Summary: Webpack stats plugin
License: MIT
Group: Development/Libraries
URL: https://github.com/FormidableLabs/webpack-stats-plugin#readme
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
cp -pfr index.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr lib %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%check
%{nodejs_symlink_deps} --check

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE.txt
%doc HISTORY.md
%doc README.md

%changelog
* Fri Oct 04 2019 Eric D. Helms <ericdhelms@gmail.com> - 0.1.5-2
- Update specs to handle SCL

* Tue Jul 18 2017 Michael Moll <kvedulv@kvedulv.de> 0.1.5-1
- Replace nodejs-stats-webpack-plugin with nodejs-webpack-stats-plugin
