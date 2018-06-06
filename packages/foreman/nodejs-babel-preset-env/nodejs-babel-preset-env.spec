%global npm_name babel-preset-env

Name: nodejs-%{npm_name}
Version: 1.7.0
Release: 1%{?dist}
Summary: A Babel preset for each environment
License: MIT
Group: Development/Libraries
URL: https://babeljs.io/
Source0: https://registry.npmjs.org/babel-preset-env/-/babel-preset-env-1.7.0.tgz
Source1: https://registry.npmjs.org/babel-plugin-syntax-trailing-function-commas/-/babel-plugin-syntax-trailing-function-commas-6.22.0.tgz
Source2: https://registry.npmjs.org/babel-plugin-transform-es2015-block-scoped-functions/-/babel-plugin-transform-es2015-block-scoped-functions-6.22.0.tgz
Source3: https://registry.npmjs.org/babel-plugin-transform-es2015-computed-properties/-/babel-plugin-transform-es2015-computed-properties-6.24.1.tgz
Source4: https://registry.npmjs.org/babel-plugin-transform-es2015-arrow-functions/-/babel-plugin-transform-es2015-arrow-functions-6.22.0.tgz
Source5: https://registry.npmjs.org/babel-plugin-transform-async-to-generator/-/babel-plugin-transform-async-to-generator-6.24.1.tgz
Source6: https://registry.npmjs.org/babel-plugin-transform-es2015-classes/-/babel-plugin-transform-es2015-classes-6.24.1.tgz
Source7: https://registry.npmjs.org/babel-plugin-transform-es2015-block-scoping/-/babel-plugin-transform-es2015-block-scoping-6.26.0.tgz
Source8: https://registry.npmjs.org/babel-plugin-transform-es2015-destructuring/-/babel-plugin-transform-es2015-destructuring-6.23.0.tgz
Source9: https://registry.npmjs.org/babel-plugin-transform-es2015-duplicate-keys/-/babel-plugin-transform-es2015-duplicate-keys-6.24.1.tgz
Source10: https://registry.npmjs.org/babel-plugin-check-es2015-constants/-/babel-plugin-check-es2015-constants-6.22.0.tgz
Source11: https://registry.npmjs.org/babel-plugin-transform-es2015-literals/-/babel-plugin-transform-es2015-literals-6.22.0.tgz
Source12: https://registry.npmjs.org/babel-plugin-transform-es2015-for-of/-/babel-plugin-transform-es2015-for-of-6.23.0.tgz
Source13: https://registry.npmjs.org/babel-plugin-transform-es2015-function-name/-/babel-plugin-transform-es2015-function-name-6.24.1.tgz
Source14: https://registry.npmjs.org/babel-plugin-transform-es2015-modules-amd/-/babel-plugin-transform-es2015-modules-amd-6.24.1.tgz
Source15: https://registry.npmjs.org/babel-plugin-transform-es2015-modules-commonjs/-/babel-plugin-transform-es2015-modules-commonjs-6.26.2.tgz
Source16: https://registry.npmjs.org/babel-plugin-transform-es2015-shorthand-properties/-/babel-plugin-transform-es2015-shorthand-properties-6.24.1.tgz
Source17: https://registry.npmjs.org/babel-plugin-transform-es2015-modules-umd/-/babel-plugin-transform-es2015-modules-umd-6.24.1.tgz
Source18: https://registry.npmjs.org/babel-plugin-transform-es2015-modules-systemjs/-/babel-plugin-transform-es2015-modules-systemjs-6.24.1.tgz
Source19: https://registry.npmjs.org/babel-plugin-transform-es2015-object-super/-/babel-plugin-transform-es2015-object-super-6.24.1.tgz
Source20: https://registry.npmjs.org/babel-plugin-transform-es2015-parameters/-/babel-plugin-transform-es2015-parameters-6.24.1.tgz
Source21: https://registry.npmjs.org/babel-plugin-transform-es2015-spread/-/babel-plugin-transform-es2015-spread-6.22.0.tgz
Source22: https://registry.npmjs.org/babel-plugin-transform-es2015-sticky-regex/-/babel-plugin-transform-es2015-sticky-regex-6.24.1.tgz
Source23: https://registry.npmjs.org/babel-plugin-transform-es2015-template-literals/-/babel-plugin-transform-es2015-template-literals-6.22.0.tgz
Source24: https://registry.npmjs.org/babel-plugin-transform-es2015-typeof-symbol/-/babel-plugin-transform-es2015-typeof-symbol-6.23.0.tgz
Source25: https://registry.npmjs.org/babel-plugin-transform-es2015-unicode-regex/-/babel-plugin-transform-es2015-unicode-regex-6.24.1.tgz
Source26: https://registry.npmjs.org/invariant/-/invariant-2.2.4.tgz
Source27: https://registry.npmjs.org/babel-plugin-transform-exponentiation-operator/-/babel-plugin-transform-exponentiation-operator-6.24.1.tgz
Source28: https://registry.npmjs.org/browserslist/-/browserslist-3.2.8.tgz
Source29: https://registry.npmjs.org/semver/-/semver-5.5.0.tgz
Source30: https://registry.npmjs.org/babel-template/-/babel-template-6.26.0.tgz
Source31: https://registry.npmjs.org/babel-runtime/-/babel-runtime-6.26.0.tgz
Source32: https://registry.npmjs.org/babel-plugin-syntax-async-functions/-/babel-plugin-syntax-async-functions-6.13.0.tgz
Source33: https://registry.npmjs.org/babel-helper-remap-async-to-generator/-/babel-helper-remap-async-to-generator-6.24.1.tgz
Source34: https://registry.npmjs.org/babel-plugin-transform-regenerator/-/babel-plugin-transform-regenerator-6.26.0.tgz
Source35: https://registry.npmjs.org/babel-helper-optimise-call-expression/-/babel-helper-optimise-call-expression-6.24.1.tgz
Source36: https://registry.npmjs.org/babel-helper-replace-supers/-/babel-helper-replace-supers-6.24.1.tgz
Source37: https://registry.npmjs.org/babel-helper-function-name/-/babel-helper-function-name-6.24.1.tgz
Source38: https://registry.npmjs.org/babel-traverse/-/babel-traverse-6.26.0.tgz
Source39: https://registry.npmjs.org/babel-helper-define-map/-/babel-helper-define-map-6.26.0.tgz
Source40: https://registry.npmjs.org/babel-messages/-/babel-messages-6.23.0.tgz
Source41: https://registry.npmjs.org/lodash/-/lodash-4.17.10.tgz
Source42: https://registry.npmjs.org/babel-types/-/babel-types-6.26.0.tgz
Source43: https://registry.npmjs.org/babel-plugin-transform-strict-mode/-/babel-plugin-transform-strict-mode-6.24.1.tgz
Source44: https://registry.npmjs.org/babel-helper-hoist-variables/-/babel-helper-hoist-variables-6.24.1.tgz
Source45: https://registry.npmjs.org/babel-helper-call-delegate/-/babel-helper-call-delegate-6.24.1.tgz
Source46: https://registry.npmjs.org/babel-helper-get-function-arity/-/babel-helper-get-function-arity-6.24.1.tgz
Source47: https://registry.npmjs.org/babel-helper-regex/-/babel-helper-regex-6.26.0.tgz
Source48: https://registry.npmjs.org/regexpu-core/-/regexpu-core-2.0.0.tgz
Source49: https://registry.npmjs.org/loose-envify/-/loose-envify-1.3.1.tgz
Source50: https://registry.npmjs.org/babel-helper-builder-binary-assignment-operator-visitor/-/babel-helper-builder-binary-assignment-operator-visitor-6.24.1.tgz
Source51: https://registry.npmjs.org/babel-plugin-syntax-exponentiation-operator/-/babel-plugin-syntax-exponentiation-operator-6.13.0.tgz
Source52: https://registry.npmjs.org/electron-to-chromium/-/electron-to-chromium-1.3.48.tgz
Source53: https://registry.npmjs.org/caniuse-lite/-/caniuse-lite-1.0.30000849.tgz
Source54: https://registry.npmjs.org/regenerator-runtime/-/regenerator-runtime-0.11.1.tgz
Source55: https://registry.npmjs.org/babylon/-/babylon-6.18.0.tgz
Source56: https://registry.npmjs.org/core-js/-/core-js-2.5.7.tgz
Source57: https://registry.npmjs.org/regenerator-transform/-/regenerator-transform-0.10.1.tgz
Source58: https://registry.npmjs.org/babel-code-frame/-/babel-code-frame-6.26.0.tgz
Source59: https://registry.npmjs.org/debug/-/debug-2.6.9.tgz
Source60: https://registry.npmjs.org/globals/-/globals-9.18.0.tgz
Source61: https://registry.npmjs.org/esutils/-/esutils-2.0.2.tgz
Source62: https://registry.npmjs.org/to-fast-properties/-/to-fast-properties-1.0.3.tgz
Source63: https://registry.npmjs.org/regjsgen/-/regjsgen-0.2.0.tgz
Source64: https://registry.npmjs.org/regenerate/-/regenerate-1.4.0.tgz
Source65: https://registry.npmjs.org/regjsparser/-/regjsparser-0.1.5.tgz
Source66: https://registry.npmjs.org/js-tokens/-/js-tokens-3.0.2.tgz
Source67: https://registry.npmjs.org/private/-/private-0.1.8.tgz
Source68: https://registry.npmjs.org/chalk/-/chalk-1.1.3.tgz
Source69: https://registry.npmjs.org/ms/-/ms-2.0.0.tgz
Source70: https://registry.npmjs.org/ansi-styles/-/ansi-styles-2.2.1.tgz
Source71: https://registry.npmjs.org/jsesc/-/jsesc-0.5.0.tgz
Source72: https://registry.npmjs.org/babel-helper-explode-assignable-expression/-/babel-helper-explode-assignable-expression-6.24.1.tgz
Source73: https://registry.npmjs.org/escape-string-regexp/-/escape-string-regexp-1.0.5.tgz
Source74: https://registry.npmjs.org/has-ansi/-/has-ansi-2.0.0.tgz
Source75: https://registry.npmjs.org/strip-ansi/-/strip-ansi-3.0.1.tgz
Source76: https://registry.npmjs.org/supports-color/-/supports-color-2.0.0.tgz
Source77: https://registry.npmjs.org/ansi-regex/-/ansi-regex-2.1.1.tgz
Source78: %{npm_name}-%{version}-registry.npmjs.org.tgz
BuildRequires: nodejs-packaging
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: npm(%{npm_name}) = %{version}
Provides: bundled(npm(ansi-regex)) = 2.1.1
Provides: bundled(npm(ansi-styles)) = 2.2.1
Provides: bundled(npm(babel-code-frame)) = 6.26.0
Provides: bundled(npm(babel-helper-builder-binary-assignment-operator-visitor)) = 6.24.1
Provides: bundled(npm(babel-helper-call-delegate)) = 6.24.1
Provides: bundled(npm(babel-helper-define-map)) = 6.26.0
Provides: bundled(npm(babel-helper-explode-assignable-expression)) = 6.24.1
Provides: bundled(npm(babel-helper-function-name)) = 6.24.1
Provides: bundled(npm(babel-helper-get-function-arity)) = 6.24.1
Provides: bundled(npm(babel-helper-hoist-variables)) = 6.24.1
Provides: bundled(npm(babel-helper-optimise-call-expression)) = 6.24.1
Provides: bundled(npm(babel-helper-regex)) = 6.26.0
Provides: bundled(npm(babel-helper-remap-async-to-generator)) = 6.24.1
Provides: bundled(npm(babel-helper-replace-supers)) = 6.24.1
Provides: bundled(npm(babel-messages)) = 6.23.0
Provides: bundled(npm(babel-plugin-check-es2015-constants)) = 6.22.0
Provides: bundled(npm(babel-plugin-syntax-async-functions)) = 6.13.0
Provides: bundled(npm(babel-plugin-syntax-exponentiation-operator)) = 6.13.0
Provides: bundled(npm(babel-plugin-syntax-trailing-function-commas)) = 6.22.0
Provides: bundled(npm(babel-plugin-transform-async-to-generator)) = 6.24.1
Provides: bundled(npm(babel-plugin-transform-es2015-arrow-functions)) = 6.22.0
Provides: bundled(npm(babel-plugin-transform-es2015-block-scoped-functions)) = 6.22.0
Provides: bundled(npm(babel-plugin-transform-es2015-block-scoping)) = 6.26.0
Provides: bundled(npm(babel-plugin-transform-es2015-classes)) = 6.24.1
Provides: bundled(npm(babel-plugin-transform-es2015-computed-properties)) = 6.24.1
Provides: bundled(npm(babel-plugin-transform-es2015-destructuring)) = 6.23.0
Provides: bundled(npm(babel-plugin-transform-es2015-duplicate-keys)) = 6.24.1
Provides: bundled(npm(babel-plugin-transform-es2015-for-of)) = 6.23.0
Provides: bundled(npm(babel-plugin-transform-es2015-function-name)) = 6.24.1
Provides: bundled(npm(babel-plugin-transform-es2015-literals)) = 6.22.0
Provides: bundled(npm(babel-plugin-transform-es2015-modules-amd)) = 6.24.1
Provides: bundled(npm(babel-plugin-transform-es2015-modules-commonjs)) = 6.26.2
Provides: bundled(npm(babel-plugin-transform-es2015-modules-systemjs)) = 6.24.1
Provides: bundled(npm(babel-plugin-transform-es2015-modules-umd)) = 6.24.1
Provides: bundled(npm(babel-plugin-transform-es2015-object-super)) = 6.24.1
Provides: bundled(npm(babel-plugin-transform-es2015-parameters)) = 6.24.1
Provides: bundled(npm(babel-plugin-transform-es2015-shorthand-properties)) = 6.24.1
Provides: bundled(npm(babel-plugin-transform-es2015-spread)) = 6.22.0
Provides: bundled(npm(babel-plugin-transform-es2015-sticky-regex)) = 6.24.1
Provides: bundled(npm(babel-plugin-transform-es2015-template-literals)) = 6.22.0
Provides: bundled(npm(babel-plugin-transform-es2015-typeof-symbol)) = 6.23.0
Provides: bundled(npm(babel-plugin-transform-es2015-unicode-regex)) = 6.24.1
Provides: bundled(npm(babel-plugin-transform-exponentiation-operator)) = 6.24.1
Provides: bundled(npm(babel-plugin-transform-regenerator)) = 6.26.0
Provides: bundled(npm(babel-plugin-transform-strict-mode)) = 6.24.1
Provides: bundled(npm(babel-preset-env)) = 1.7.0
Provides: bundled(npm(babel-runtime)) = 6.26.0
Provides: bundled(npm(babel-template)) = 6.26.0
Provides: bundled(npm(babel-traverse)) = 6.26.0
Provides: bundled(npm(babel-types)) = 6.26.0
Provides: bundled(npm(babylon)) = 6.18.0
Provides: bundled(npm(browserslist)) = 3.2.8
Provides: bundled(npm(caniuse-lite)) = 1.0.30000849
Provides: bundled(npm(chalk)) = 1.1.3
Provides: bundled(npm(core-js)) = 2.5.7
Provides: bundled(npm(debug)) = 2.6.9
Provides: bundled(npm(electron-to-chromium)) = 1.3.48
Provides: bundled(npm(escape-string-regexp)) = 1.0.5
Provides: bundled(npm(esutils)) = 2.0.2
Provides: bundled(npm(globals)) = 9.18.0
Provides: bundled(npm(has-ansi)) = 2.0.0
Provides: bundled(npm(invariant)) = 2.2.4
Provides: bundled(npm(js-tokens)) = 3.0.2
Provides: bundled(npm(jsesc)) = 0.5.0
Provides: bundled(npm(lodash)) = 4.17.10
Provides: bundled(npm(loose-envify)) = 1.3.1
Provides: bundled(npm(ms)) = 2.0.0
Provides: bundled(npm(private)) = 0.1.8
Provides: bundled(npm(regenerate)) = 1.4.0
Provides: bundled(npm(regenerator-runtime)) = 0.11.1
Provides: bundled(npm(regenerator-transform)) = 0.10.1
Provides: bundled(npm(regexpu-core)) = 2.0.0
Provides: bundled(npm(regjsgen)) = 0.2.0
Provides: bundled(npm(regjsparser)) = 0.1.5
Provides: bundled(npm(semver)) = 5.5.0
Provides: bundled(npm(strip-ansi)) = 3.0.1
Provides: bundled(npm(supports-color)) = 2.0.0
Provides: bundled(npm(to-fast-properties)) = 1.0.3
AutoReq: no
AutoProv: no

%define npm_cache_dir /tmp/npm_cache_%{name}-%{version}-%{release}

%description
%{summary}

%prep
mkdir -p %{npm_cache_dir}
for tgz in %{sources}; do
  echo $tgz | grep -q registry.npmjs.org || npm cache add --cache %{npm_cache_dir} $tgz
done
%setup -T -q -a 78 -D -n %{npm_cache_dir}

%build
npm install --cache-min Infinity --cache %{npm_cache_dir} --no-shrinkwrap --no-optional --global-style true %{npm_name}@%{version}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/data %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/lib %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%license node_modules/%{npm_name}/LICENSE
%doc node_modules/%{npm_name}/CHANGELOG.md
%doc node_modules/%{npm_name}/CONTRIBUTING.md
%doc node_modules/%{npm_name}/README.md

%changelog
* Wed Jun 06 2018 Eric D. Helms <ericdhelms@gmail.com> 1.7.0-1
- Update to 1.7.0

* Mon Oct 30 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.6.1-1
- new package built with tito

