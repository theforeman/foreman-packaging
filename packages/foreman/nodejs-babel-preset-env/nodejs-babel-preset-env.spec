%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name @babel/preset-env

Name: %{?scl_prefix}nodejs-babel-preset-env
Version: 7.9.5
Release: 1%{?dist}
Summary: A Babel preset for each environment
License: MIT
Group: Development/Libraries
URL: https://babeljs.io/
Source0: https://registry.npmjs.org/@babel/preset-env/-/preset-env-%{version}.tgz
%if 0%{?!scl:1}
BuildRequires: nodejs-packaging
%endif
Requires: npm(@babel/compat-data) >= 7.9.0
Requires: npm(@babel/compat-data) < 8.0.0
Requires: npm(@babel/helper-compilation-targets) >= 7.8.7
Requires: npm(@babel/helper-compilation-targets) < 8.0.0
Requires: npm(@babel/helper-module-imports) >= 7.8.3
Requires: npm(@babel/helper-module-imports) < 8.0.0
Requires: npm(@babel/helper-plugin-utils) >= 7.8.3
Requires: npm(@babel/helper-plugin-utils) < 8.0.0
Requires: npm(@babel/plugin-proposal-async-generator-functions) >= 7.8.3
Requires: npm(@babel/plugin-proposal-async-generator-functions) < 8.0.0
Requires: npm(@babel/plugin-proposal-dynamic-import) >= 7.8.3
Requires: npm(@babel/plugin-proposal-dynamic-import) < 8.0.0
Requires: npm(@babel/plugin-proposal-json-strings) >= 7.8.3
Requires: npm(@babel/plugin-proposal-json-strings) < 8.0.0
Requires: npm(@babel/plugin-proposal-nullish-coalescing-operator) >= 7.8.3
Requires: npm(@babel/plugin-proposal-nullish-coalescing-operator) < 8.0.0
Requires: npm(@babel/plugin-proposal-numeric-separator) >= 7.8.3
Requires: npm(@babel/plugin-proposal-numeric-separator) < 8.0.0
Requires: npm(@babel/plugin-proposal-object-rest-spread) >= 7.9.5
Requires: npm(@babel/plugin-proposal-object-rest-spread) < 8.0.0
Requires: npm(@babel/plugin-proposal-optional-catch-binding) >= 7.8.3
Requires: npm(@babel/plugin-proposal-optional-catch-binding) < 8.0.0
Requires: npm(@babel/plugin-proposal-optional-chaining) >= 7.9.0
Requires: npm(@babel/plugin-proposal-optional-chaining) < 8.0.0
Requires: npm(@babel/plugin-proposal-unicode-property-regex) >= 7.8.3
Requires: npm(@babel/plugin-proposal-unicode-property-regex) < 8.0.0
Requires: npm(@babel/plugin-syntax-async-generators) >= 7.8.0
Requires: npm(@babel/plugin-syntax-async-generators) < 8.0.0
Requires: npm(@babel/plugin-syntax-dynamic-import) >= 7.8.0
Requires: npm(@babel/plugin-syntax-dynamic-import) < 8.0.0
Requires: npm(@babel/plugin-syntax-json-strings) >= 7.8.0
Requires: npm(@babel/plugin-syntax-json-strings) < 8.0.0
Requires: npm(@babel/plugin-syntax-nullish-coalescing-operator) >= 7.8.0
Requires: npm(@babel/plugin-syntax-nullish-coalescing-operator) < 8.0.0
Requires: npm(@babel/plugin-syntax-numeric-separator) >= 7.8.0
Requires: npm(@babel/plugin-syntax-numeric-separator) < 8.0.0
Requires: npm(@babel/plugin-syntax-object-rest-spread) >= 7.8.0
Requires: npm(@babel/plugin-syntax-object-rest-spread) < 8.0.0
Requires: npm(@babel/plugin-syntax-optional-catch-binding) >= 7.8.0
Requires: npm(@babel/plugin-syntax-optional-catch-binding) < 8.0.0
Requires: npm(@babel/plugin-syntax-optional-chaining) >= 7.8.0
Requires: npm(@babel/plugin-syntax-optional-chaining) < 8.0.0
Requires: npm(@babel/plugin-syntax-top-level-await) >= 7.8.3
Requires: npm(@babel/plugin-syntax-top-level-await) < 8.0.0
Requires: npm(@babel/plugin-transform-arrow-functions) >= 7.8.3
Requires: npm(@babel/plugin-transform-arrow-functions) < 8.0.0
Requires: npm(@babel/plugin-transform-async-to-generator) >= 7.8.3
Requires: npm(@babel/plugin-transform-async-to-generator) < 8.0.0
Requires: npm(@babel/plugin-transform-block-scoped-functions) >= 7.8.3
Requires: npm(@babel/plugin-transform-block-scoped-functions) < 8.0.0
Requires: npm(@babel/plugin-transform-block-scoping) >= 7.8.3
Requires: npm(@babel/plugin-transform-block-scoping) < 8.0.0
Requires: npm(@babel/plugin-transform-classes) >= 7.9.5
Requires: npm(@babel/plugin-transform-classes) < 8.0.0
Requires: npm(@babel/plugin-transform-computed-properties) >= 7.8.3
Requires: npm(@babel/plugin-transform-computed-properties) < 8.0.0
Requires: npm(@babel/plugin-transform-destructuring) >= 7.9.5
Requires: npm(@babel/plugin-transform-destructuring) < 8.0.0
Requires: npm(@babel/plugin-transform-dotall-regex) >= 7.8.3
Requires: npm(@babel/plugin-transform-dotall-regex) < 8.0.0
Requires: npm(@babel/plugin-transform-duplicate-keys) >= 7.8.3
Requires: npm(@babel/plugin-transform-duplicate-keys) < 8.0.0
Requires: npm(@babel/plugin-transform-exponentiation-operator) >= 7.8.3
Requires: npm(@babel/plugin-transform-exponentiation-operator) < 8.0.0
Requires: npm(@babel/plugin-transform-for-of) >= 7.9.0
Requires: npm(@babel/plugin-transform-for-of) < 8.0.0
Requires: npm(@babel/plugin-transform-function-name) >= 7.8.3
Requires: npm(@babel/plugin-transform-function-name) < 8.0.0
Requires: npm(@babel/plugin-transform-literals) >= 7.8.3
Requires: npm(@babel/plugin-transform-literals) < 8.0.0
Requires: npm(@babel/plugin-transform-member-expression-literals) >= 7.8.3
Requires: npm(@babel/plugin-transform-member-expression-literals) < 8.0.0
Requires: npm(@babel/plugin-transform-modules-amd) >= 7.9.0
Requires: npm(@babel/plugin-transform-modules-amd) < 8.0.0
Requires: npm(@babel/plugin-transform-modules-commonjs) >= 7.9.0
Requires: npm(@babel/plugin-transform-modules-commonjs) < 8.0.0
Requires: npm(@babel/plugin-transform-modules-systemjs) >= 7.9.0
Requires: npm(@babel/plugin-transform-modules-systemjs) < 8.0.0
Requires: npm(@babel/plugin-transform-modules-umd) >= 7.9.0
Requires: npm(@babel/plugin-transform-modules-umd) < 8.0.0
Requires: npm(@babel/plugin-transform-named-capturing-groups-regex) >= 7.8.3
Requires: npm(@babel/plugin-transform-named-capturing-groups-regex) < 8.0.0
Requires: npm(@babel/plugin-transform-new-target) >= 7.8.3
Requires: npm(@babel/plugin-transform-new-target) < 8.0.0
Requires: npm(@babel/plugin-transform-object-super) >= 7.8.3
Requires: npm(@babel/plugin-transform-object-super) < 8.0.0
Requires: npm(@babel/plugin-transform-parameters) >= 7.9.5
Requires: npm(@babel/plugin-transform-parameters) < 8.0.0
Requires: npm(@babel/plugin-transform-property-literals) >= 7.8.3
Requires: npm(@babel/plugin-transform-property-literals) < 8.0.0
Requires: npm(@babel/plugin-transform-regenerator) >= 7.8.7
Requires: npm(@babel/plugin-transform-regenerator) < 8.0.0
Requires: npm(@babel/plugin-transform-reserved-words) >= 7.8.3
Requires: npm(@babel/plugin-transform-reserved-words) < 8.0.0
Requires: npm(@babel/plugin-transform-shorthand-properties) >= 7.8.3
Requires: npm(@babel/plugin-transform-shorthand-properties) < 8.0.0
Requires: npm(@babel/plugin-transform-spread) >= 7.8.3
Requires: npm(@babel/plugin-transform-spread) < 8.0.0
Requires: npm(@babel/plugin-transform-sticky-regex) >= 7.8.3
Requires: npm(@babel/plugin-transform-sticky-regex) < 8.0.0
Requires: npm(@babel/plugin-transform-template-literals) >= 7.8.3
Requires: npm(@babel/plugin-transform-template-literals) < 8.0.0
Requires: npm(@babel/plugin-transform-typeof-symbol) >= 7.8.4
Requires: npm(@babel/plugin-transform-typeof-symbol) < 8.0.0
Requires: npm(@babel/plugin-transform-unicode-regex) >= 7.8.3
Requires: npm(@babel/plugin-transform-unicode-regex) < 8.0.0
Requires: npm(@babel/preset-modules) >= 0.1.3
Requires: npm(@babel/preset-modules) < 0.2.0
Requires: npm(@babel/types) >= 7.9.5
Requires: npm(@babel/types) < 8.0.0
Requires: npm(browserslist) >= 4.9.1
Requires: npm(browserslist) < 5.0.0
Requires: npm(core-js-compat) >= 3.6.2
Requires: npm(core-js-compat) < 4.0.0
Requires: npm(invariant) >= 2.2.2
Requires: npm(invariant) < 3.0.0
Requires: npm(levenary) >= 1.1.1
Requires: npm(levenary) < 2.0.0
Requires: npm(semver) >= 5.5.0
Requires: npm(semver) < 6.0.0
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch
Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}

%description
%{summary}

%prep
%setup -q -n package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr data %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr lib %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}


%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE
%doc README.md

%changelog
* Tue Sep 17 2024 MariaAga <mariaaga@redhat.com> 7.9.5-1
- Update to 7.9.5

* Thu Feb 01 2024 Eric D. Helms <ericdhelms@gmail.com> - 1.7.0-5
- Use --legacy-peer-deps during npm install

* Tue Mar 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.7.0-4
- Bump packages to build for el8

* Mon Oct 21 2019 Eric D. Helms <ericdhelms@gmail.com> - 1.7.0-3
- Build for SCL

* Fri Oct 04 2019 Eric D. Helms <ericdhelms@gmail.com> - 1.7.0-2
- Update specs to handle SCL

* Wed Jun 06 2018 Eric D. Helms <ericdhelms@gmail.com> 1.7.0-1
- Update to 1.7.0

* Mon Oct 30 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.6.1-1
- new package built with tito
