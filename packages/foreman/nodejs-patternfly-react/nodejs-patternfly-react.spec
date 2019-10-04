%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name patternfly-react

Name: %{?scl_prefix}nodejs-patternfly-react
Version: 2.34.1
Release: 2%{?dist}
Summary: This library provides a set of common React components for use with the PatternFly reference implementation
License: MIT
Group: Development/Libraries
URL: https://github.com/patternfly/patternfly-react#readme
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
%if 0%{?scl:1}
BuildRequires: %{?scl_prefix_nodejs}npm
%else
BuildRequires: nodejs-packaging
%endif
Requires: %{?scl_prefix}npm(bootstrap-slider-without-jquery) >= 10.0.0
Requires: %{?scl_prefix}npm(bootstrap-slider-without-jquery) < 11.0.0
Requires: %{?scl_prefix}npm(breakjs) >= 1.0.0
Requires: %{?scl_prefix}npm(breakjs) < 2.0.0
Requires: %{?scl_prefix}npm(classnames) >= 2.2.5
Requires: %{?scl_prefix}npm(classnames) < 3.0.0
Requires: %{?scl_prefix}npm(css-element-queries) >= 1.0.1
Requires: %{?scl_prefix}npm(css-element-queries) < 2.0.0
Requires: %{?scl_prefix}npm(lodash) >= 4.17.11
Requires: %{?scl_prefix}npm(lodash) < 5.0.0
Requires: %{?scl_prefix}npm(patternfly) >= 3.58.0
Requires: %{?scl_prefix}npm(patternfly) < 4.0.0
Requires: %{?scl_prefix}npm(react-bootstrap) >= 0.32.1
Requires: %{?scl_prefix}npm(react-bootstrap) < 0.33.0
Requires: %{?scl_prefix}npm(react-bootstrap-switch) >= 15.5.3
Requires: %{?scl_prefix}npm(react-bootstrap-switch) < 16.0.0
Requires: %{?scl_prefix}npm(react-bootstrap-typeahead) >= 3.4.1
Requires: %{?scl_prefix}npm(react-bootstrap-typeahead) < 4.0.0
Requires: %{?scl_prefix}npm(react-c3js) >= 0.1.20
Requires: %{?scl_prefix}npm(react-c3js) < 0.2.0
Requires: %{?scl_prefix}npm(react-click-outside) >= 3.0.1
Requires: %{?scl_prefix}npm(react-click-outside) < 4.0.0
Requires: %{?scl_prefix}npm(react-collapse) >= 4.0.3
Requires: %{?scl_prefix}npm(react-collapse) < 5.0.0
Requires: %{?scl_prefix}npm(react-debounce-input) >= 3.2.0
Requires: %{?scl_prefix}npm(react-debounce-input) < 4.0.0
Requires: %{?scl_prefix}npm(react-ellipsis-with-tooltip) >= 1.0.8
Requires: %{?scl_prefix}npm(react-ellipsis-with-tooltip) < 2.0.0
Requires: %{?scl_prefix}npm(react-fontawesome) >= 1.6.1
Requires: %{?scl_prefix}npm(react-fontawesome) < 2.0.0
Requires: %{?scl_prefix}npm(react-motion) >= 0.5.2
Requires: %{?scl_prefix}npm(react-motion) < 0.6.0
Requires: %{?scl_prefix}npm(reactabular-table) >= 8.14.0
Requires: %{?scl_prefix}npm(reactabular-table) < 9.0.0
Requires: %{?scl_prefix}npm(recompose) >= 0.26.0
Requires: %{?scl_prefix}npm(recompose) < 0.27.0
Requires: %{?scl_prefix}npm(sortabular) >= 1.5.1
Requires: %{?scl_prefix}npm(sortabular) < 2.0.0
Requires: %{?scl_prefix}npm(table-resolver) >= 3.2.0
Requires: %{?scl_prefix}npm(table-resolver) < 4.0.0
Requires: %{?scl_prefix}npm(uuid) >= 3.3.2
Requires: %{?scl_prefix}npm(uuid) < 4.0.0
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch
Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}

%description
%{summary}

%prep
%setup -q -n package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr __mocks__ %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr build %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr dist %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%check
%{nodejs_symlink_deps} --check

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE
%doc CHANGELOG.md
%doc CONTRIBUTING.md
%doc README.md

%changelog
* Fri Oct 04 2019 Eric D. Helms <ericdhelms@gmail.com> - 2.34.1-2
- Update specs to handle SCL

* Thu May 16 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 2.34.1-1
- Update to 2.34.1

* Tue Mar 19 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 2.31.0-1
- Update to 2.31.0

* Thu Jan 17 2019 Avi Sharvit <asharvit@redhat.com> 2.29.0-1
- Update to 2.29.0

* Tue Dec 11 2018 Ondrej Prazak <oprazak@redhat.com> 2.25.5-1
- Update to 2.25.5

* Wed Oct 10 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 2.19.1-2
- Unbundle dependencies

* Thu Oct 04 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 2.19.1-1
- Update to 2.19.1

* Wed Sep 12 2018 Bryan Kearney <bryan.kearney@gmail.com> - 2.5.1-2
- Use ASL 2.0 instead of Apache 2.0 or Apache-2.0

* Wed Jun 06 2018 Eric D. Helms <ericdhelms@gmail.com> 2.5.1-1
- Update to 2.5.1

* Tue May 22 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 2.3.4-1
- Update to 2.3.4

* Tue May 01 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 2.2.1-1
- Update to 2.2.1

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
