%global npm_name sass-loader

Name: nodejs-sass-loader
Version: 13.3.3
Release: 4%{?dist}
Summary: Sass loader for webpack
License: MIT
URL: https://github.com/webpack-contrib/sass-loader
Source0: https://registry.npmjs.org/sass-loader/-/sass-loader-%{version}.tgz
BuildRequires: nodejs-packaging
%if 0%{?rhel} == 10
# https://issues.redhat.com/browse/RHEL-137712
BuildRequires: /usr/bin/node
%endif
Requires: npm(neo-async) >= 2.6.2
Requires: npm(neo-async) < 3.0.0
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
%doc README.md

%changelog
* Sat Jun 06 2026 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 13.3.3-4
- Regenerate spec file

* Tue Dec 23 2025 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 13.3.3-3
- Unbundle dependencies

* Thu Feb 01 2024 Eric D. Helms <ericdhelms@gmail.com> - 13.3.3-2
- Use --legacy-peer-deps during npm install

* Fri Jan 26 2024 Foreman Packaging Automation <packaging@theforeman.org> 13.3.3-1
- Update to 13.3.3

* Wed Dec 13 2023 Evgeni Golov 13.3.2-1
- Update to 13.3.2

* Tue Mar 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 6.0.7-4
- Bump packages to build for el8

* Tue Oct 22 2019 Eric D. Helms <ericdhelms@gmail.com> - 6.0.7-3
- Build for SCL

* Fri Oct 04 2019 Eric D. Helms <ericdhelms@gmail.com> - 6.0.7-2
- Update specs to handle SCL

* Wed Jun 06 2018 Eric D. Helms <ericdhelms@gmail.com> 6.0.7-1
- Update to 6.0.7

* Tue Nov 07 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 6.0.6-1
- Update nodejs-sass-loader to 6.0.6 (ewoud@kohlvanwijngaarden.nl)

* Tue Feb 28 2017 Dominic Cleal <dominic@cleal.org> 4.1.1-1
- new package built with tito
