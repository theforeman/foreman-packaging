%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name webpack-stats-plugin

Name: %{?scl_prefix}nodejs-webpack-stats-plugin
Version: 1.1.3
Release: 1%{?dist}
Summary: Webpack stats plugin
License: MIT
Group: Development/Libraries
URL: https://github.com/FormidableLabs/webpack-stats-plugin#readme
Source0: https://registry.npmjs.org/webpack-stats-plugin/-/webpack-stats-plugin-%{version}.tgz
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
cp -pfr lib %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%check
%{nodejs_symlink_deps} --check

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE.txt
%doc README.md

%changelog
* Wed Dec 13 2023 Evgeni Golov 1.1.3-1
- Update to 1.1.3

* Tue Mar 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.1.5-4
- Bump packages to build for el8

* Tue Oct 22 2019 Eric D. Helms <ericdhelms@gmail.com> - 0.1.5-3
- Build for SCL

* Fri Oct 04 2019 Eric D. Helms <ericdhelms@gmail.com> - 0.1.5-2
- Update specs to handle SCL

* Tue Jul 18 2017 Michael Moll <kvedulv@kvedulv.de> 0.1.5-1
- Replace nodejs-stats-webpack-plugin with nodejs-webpack-stats-plugin
