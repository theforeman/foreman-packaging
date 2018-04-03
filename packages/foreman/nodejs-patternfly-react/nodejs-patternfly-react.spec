%global npm_name patternfly-react
%global enable_tests 1

Name: nodejs-%{npm_name}
Version: 1.16.4
Release: 1%{?dist}
Summary: This library provides a set of common React components for use with the PatternFly reference implementation
License: Apache-2.0
Group: Development/Libraries
URL: https://github.com/patternfly/patternfly-react#readme
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
Requires: npm(breakjs) >= 1.0.0
Requires: npm(breakjs) < 2.0.0
Requires: npm(classnames) >= 2.2.5
Requires: npm(classnames) < 3.0.0
Requires: npm(css-element-queries) >= 1.0.1
Requires: npm(css-element-queries) < 2.0.0
Requires: npm(lodash.orderby) >= 4.6.0
Requires: npm(lodash.orderby) < 5.0.0
Requires: npm(patternfly) >= 3.38.0
Requires: npm(patternfly) < 4.0.0
Requires: npm(react-bootstrap) >= 0.31.5
Requires: npm(react-bootstrap) < 1.0.0
Requires: npm(react-bootstrap-switch) >= 15.5.3
Requires: npm(react-bootstrap-switch) < 16.0.0
Requires: npm(react-c3js) >= 0.1.20
Requires: npm(react-c3js) < 1.0.0
Requires: npm(react-fontawesome) >= 1.6.1
Requires: npm(react-fontawesome) < 2.0.0
Requires: npm(reactabular-table) >= 8.12.0
Requires: npm(reactabular-table) < 9.0.0
Requires: npm(recompose) >= 0.26.0
Requires: npm(recompose) < 1.0.0
Requires: npm(sortabular) >= 1.5.1
Requires: npm(sortabular) < 2.0.0
Requires: npm(table-resolver) >= 3.2.0
Requires: npm(table-resolver) < 4.0.0
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
%{summary}

%prep
%setup -q -n package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr coverage %{buildroot}%{nodejs_sitelib}/%{npm_name}
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
%doc CONTRIBUTING.md
%doc README.md

%changelog
* Tue Apr 03 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.16.4-1
- Update to 1.16.4

* Thu Mar 01 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.11.0-1
- Refs #22724 - Bump nodejs-patternfly-react to 1.11.0
  (ewoud@kohlvanwijngaarden.nl)

* Mon Feb 26 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.10.0-1
- Bump nodejs-patternfly-react to 1.10.0 (ewoud@kohlvanwijngaarden.nl)

* Wed Feb 21 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.6.0-1
- Bump nodejs-patternfly-react to 1.6.0 (ewoud@kohlvanwijngaarden.nl)
- Restructure foreman packages to prepare for obal (pcreech@redhat.com)

* Tue Jan 16 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.26.0-1
- Bump nodejs-patternfly-react to 0.26.0 (ewoud@kohlvanwijngaarden.nl)

* Tue Dec 19 2017 Daniel Lobato Garcia <me@daniellobato.me> 0.19.2-1
- Update nodejs-patternfly-react to 0.19.2 (github@kohlvanwijngaarden.nl)

* Thu Dec 14 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.13.0-1
- Update patternfly-react to 0.13.0 (oprazak@redhat.com)

* Sun Nov 19 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.10.0-1
- Update nodejs-patternfly-react to 0.10.0 (ewoud@kohlvanwijngaarden.nl)

* Wed Nov 08 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.9.0-1
- new package built with tito
