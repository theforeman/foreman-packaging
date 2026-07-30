%global npm_name style-loader

Name: nodejs-style-loader
Version: 1.3.0
Release: 4%{?dist}
Summary: style loader module for webpack
License: MIT
URL: https://github.com/webpack-contrib/style-loader
Source0: https://registry.npmjs.org/style-loader/-/style-loader-%{version}.tgz
BuildRequires: nodejs-packaging
%if 0%{?rhel} == 10
# https://issues.redhat.com/browse/RHEL-137712 is fixed in RHEL 10.3
BuildRequires: /usr/bin/node
%endif
Requires: npm(loader-utils) >= 2.0.0
Requires: npm(loader-utils) < 3.0.0
Requires: npm(schema-utils) >= 2.7.0
Requires: npm(schema-utils) < 3.0.0
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch
Provides: npm(%{npm_name}) = %{version}

%description
%{summary}

%prep
%setup -q -n package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr dist %{buildroot}%{nodejs_sitelib}/%{npm_name}
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
* Thu Jul 30 2026 Zach Huntington-Meath <zhunting@redhat.com> 1.3.0-4
- Update to 1.3.0

* Wed Dec 24 2025 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.3.0-3
- Rebuild vendor cache for NodeJS 22

* Thu Feb 01 2024 Eric D. Helms <ericdhelms@gmail.com> - 1.3.0-2
- Use --legacy-peer-deps during npm install

* Wed Dec 13 2023 Evgeni Golov 1.3.0-1
- Update to 1.3.0

* Tue Mar 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.13.2-4
- Bump packages to build for el8

* Tue Oct 22 2019 Eric D. Helms <ericdhelms@gmail.com> - 0.13.2-3
- Build for SCL

* Fri Oct 04 2019 Eric D. Helms <ericdhelms@gmail.com> - 0.13.2-2
- Update specs to handle SCL

* Wed Jun 06 2018 Eric D. Helms <ericdhelms@gmail.com> 0.13.2-1
- Update to 0.13.2

* Thu Sep 01 2016 Dominic Cleal <dominic@cleal.org> 0.13.1-1
- new package built with tito
