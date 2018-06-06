%global npm_name reactabular-table
%global enable_tests 1

Name: nodejs-%{npm_name}
Version: 8.14.0
Release: 1%{?dist}
Summary: Table components for Reactabular
License: MIT
Group: Development/Libraries
URL: http://reactabular.js.org/
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
Requires: npm(classnames) >= 2.2.5
Requires: npm(classnames) < 3.0.0
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
%{summary}

%prep
%setup -q -n package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr dist %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%endif

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE
%doc CHANGELOG.md
%doc README.md

%changelog
* Wed Jun 06 2018 Eric D. Helms <ericdhelms@gmail.com> 8.14.0-1
- Update to 8.14.0

* Tue May 01 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 8.13.0-1
- Update to 8.13.0

* Wed Feb 21 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 8.12.0-1
- new package built with tito

