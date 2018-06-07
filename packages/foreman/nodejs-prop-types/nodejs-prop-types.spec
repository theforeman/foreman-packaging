%global npm_name prop-types
%global enable_tests 1

Name: nodejs-%{npm_name}
Version: 15.6.1
Release: 1%{?dist}
Summary: Runtime type checking for React props and similar objects
License: MIT
Group: Development/Libraries
URL: https://facebook.github.io/react/
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
Requires: npm(fbjs) >= 0.8.16
Requires: npm(fbjs) < 1.0.0
Requires: npm(loose-envify) >= 1.3.1
Requires: npm(loose-envify) < 2.0.0
Requires: npm(object-assign) >= 4.1.1
Requires: npm(object-assign) < 5.0.0
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
%{summary}

%prep
%setup -q -n package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr checkPropTypes.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr factory.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr factoryWithThrowingShims.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr factoryWithTypeCheckers.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr index.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr lib %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr prop-types.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr prop-types.min.js %{buildroot}%{nodejs_sitelib}/%{npm_name}

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
* Thu Jun 07 2018 Tomas Strachota <tstrachota@redhat.com> 15.6.1-1
- Update to 15.6.1

* Thu Nov 23 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 15.6.0-2
- Unbundle nodejs-prop-types (github@kohlvanwijngaarden.nl)

* Thu Oct 05 2017 Eric D. Helms <ericdhelms@gmail.com> 15.6.0-1
- Update prop-types to 15.5.9 (me@daniellobato.me)

* Thu May 11 2017 Dominic Cleal <dominic@cleal.org> 15.5.9-1
- new package built with tito
