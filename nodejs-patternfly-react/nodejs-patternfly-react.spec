%global npm_name patternfly-react
%global enable_tests 1

Name: nodejs-%{npm_name}
Version: 0.19.2
Release: 1%{?dist}
Summary: This library provides a set of common React components for use with the PatternFly reference implementation
License: Apache-2.0
Group: Development/Libraries
URL: https://github.com/patternfly/patternfly-react#readme
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
Requires: npm(classnames) >= 2.2.5
Requires: npm(classnames) < 3.0.0
Requires: npm(react-bootstrap) >= 0.31.5
Requires: npm(react-bootstrap) < 1.0.0
Requires: npm(react-c3js) >= 0.1.20
Requires: npm(react-c3js) < 1.0.0
Requires: npm(react-fontawesome) >= 1.6.1
Requires: npm(react-fontawesome) < 2.0.0
Requires: npm(recompose) >= 0.26.0
Requires: npm(recompose) < 1.0.0
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
%{summary}

%prep
%setup -q -n package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr lib %{buildroot}%{nodejs_sitelib}/%{npm_name}
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
* Tue Dec 19 2017 Daniel Lobato Garcia <me@daniellobato.me> 0.19.2-1
- Update nodejs-patternfly-react to 0.19.2 (github@kohlvanwijngaarden.nl)

* Thu Dec 14 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.13.0-1
- Update patternfly-react to 0.13.0 (oprazak@redhat.com)

* Sun Nov 19 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.10.0-1
- Update nodejs-patternfly-react to 0.10.0 (ewoud@kohlvanwijngaarden.nl)

* Wed Nov 08 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.9.0-1
- new package built with tito
