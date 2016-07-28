%global npm_name babel-preset-es2015

Name: nodejs-%{npm_name}
Version: 6.6.0
Release: 1%{?dist}
Summary: Babel preset for all es2015 plugins
License: MIT
Group: Development/Libraries
URL: https://babeljs.io/
Source0: http://registry.npmjs.org/babel-preset-es2015/-/babel-preset-es2015-6.6.0.tgz
Source1: http://registry.npmjs.org/babel-plugin-transform-es2015-object-super/-/babel-plugin-transform-es2015-object-super-6.8.0.tgz
Source2: http://registry.npmjs.org/babel-plugin-transform-es2015-block-scoped-functions/-/babel-plugin-transform-es2015-block-scoped-functions-6.8.0.tgz
Source3: http://registry.npmjs.org/babel-plugin-transform-es2015-shorthand-properties/-/babel-plugin-transform-es2015-shorthand-properties-6.8.0.tgz
Source4: http://registry.npmjs.org/babel-plugin-transform-es2015-function-name/-/babel-plugin-transform-es2015-function-name-6.9.0.tgz
Source5: http://registry.npmjs.org/babel-plugin-transform-es2015-template-literals/-/babel-plugin-transform-es2015-template-literals-6.8.0.tgz
Source6: http://registry.npmjs.org/babel-plugin-transform-es2015-classes/-/babel-plugin-transform-es2015-classes-6.9.0.tgz
Source7: http://registry.npmjs.org/babel-plugin-transform-es2015-literals/-/babel-plugin-transform-es2015-literals-6.8.0.tgz
Source8: http://registry.npmjs.org/babel-plugin-transform-es2015-arrow-functions/-/babel-plugin-transform-es2015-arrow-functions-6.8.0.tgz
Source9: http://registry.npmjs.org/babel-plugin-transform-es2015-duplicate-keys/-/babel-plugin-transform-es2015-duplicate-keys-6.8.0.tgz
Source10: http://registry.npmjs.org/babel-plugin-transform-es2015-computed-properties/-/babel-plugin-transform-es2015-computed-properties-6.8.0.tgz
Source11: http://registry.npmjs.org/babel-plugin-transform-es2015-sticky-regex/-/babel-plugin-transform-es2015-sticky-regex-6.8.0.tgz
Source12: http://registry.npmjs.org/babel-plugin-transform-es2015-for-of/-/babel-plugin-transform-es2015-for-of-6.8.0.tgz
Source13: http://registry.npmjs.org/babel-plugin-check-es2015-constants/-/babel-plugin-check-es2015-constants-6.8.0.tgz
Source14: http://registry.npmjs.org/babel-plugin-transform-es2015-parameters/-/babel-plugin-transform-es2015-parameters-6.11.4.tgz
Source15: http://registry.npmjs.org/babel-plugin-transform-es2015-block-scoping/-/babel-plugin-transform-es2015-block-scoping-6.10.1.tgz
Source16: http://registry.npmjs.org/babel-plugin-transform-es2015-unicode-regex/-/babel-plugin-transform-es2015-unicode-regex-6.11.0.tgz
Source17: http://registry.npmjs.org/babel-plugin-transform-es2015-spread/-/babel-plugin-transform-es2015-spread-6.8.0.tgz
Source18: http://registry.npmjs.org/babel-plugin-transform-es2015-typeof-symbol/-/babel-plugin-transform-es2015-typeof-symbol-6.8.0.tgz
Source19: http://registry.npmjs.org/babel-runtime/-/babel-runtime-6.11.6.tgz
Source20: http://registry.npmjs.org/babel-plugin-transform-es2015-modules-commonjs/-/babel-plugin-transform-es2015-modules-commonjs-6.11.5.tgz
Source21: http://registry.npmjs.org/babel-plugin-transform-es2015-destructuring/-/babel-plugin-transform-es2015-destructuring-6.9.0.tgz
Source22: http://registry.npmjs.org/babel-helper-function-name/-/babel-helper-function-name-6.8.0.tgz
Source23: http://registry.npmjs.org/babel-helper-replace-supers/-/babel-helper-replace-supers-6.8.0.tgz
Source24: http://registry.npmjs.org/babel-types/-/babel-types-6.11.1.tgz
Source25: http://registry.npmjs.org/babel-plugin-transform-regenerator/-/babel-plugin-transform-regenerator-6.11.4.tgz
Source26: http://registry.npmjs.org/babel-helper-optimise-call-expression/-/babel-helper-optimise-call-expression-6.8.0.tgz
Source27: http://registry.npmjs.org/babel-traverse/-/babel-traverse-6.12.0.tgz
Source28: http://registry.npmjs.org/babel-template/-/babel-template-6.9.0.tgz
Source29: http://registry.npmjs.org/babel-messages/-/babel-messages-6.8.0.tgz
Source30: http://registry.npmjs.org/babel-helper-define-map/-/babel-helper-define-map-6.9.0.tgz
Source31: http://registry.npmjs.org/babel-helper-regex/-/babel-helper-regex-6.9.0.tgz
Source32: http://registry.npmjs.org/babel-helper-get-function-arity/-/babel-helper-get-function-arity-6.8.0.tgz
Source33: http://registry.npmjs.org/babel-helper-call-delegate/-/babel-helper-call-delegate-6.8.0.tgz
Source34: http://registry.npmjs.org/regexpu-core/-/regexpu-core-2.0.0.tgz
Source35: http://registry.npmjs.org/lodash/-/lodash-4.14.0.tgz
Source36: http://registry.npmjs.org/core-js/-/core-js-2.4.1.tgz
Source37: http://registry.npmjs.org/regenerator-runtime/-/regenerator-runtime-0.9.5.tgz
Source38: http://registry.npmjs.org/babel-plugin-transform-strict-mode/-/babel-plugin-transform-strict-mode-6.11.3.tgz
Source39: http://registry.npmjs.org/esutils/-/esutils-2.0.2.tgz
Source40: http://registry.npmjs.org/to-fast-properties/-/to-fast-properties-1.0.2.tgz
Source41: http://registry.npmjs.org/babel-core/-/babel-core-6.11.4.tgz
Source42: http://registry.npmjs.org/babel-plugin-syntax-async-functions/-/babel-plugin-syntax-async-functions-6.8.0.tgz
Source43: http://registry.npmjs.org/babel-code-frame/-/babel-code-frame-6.11.0.tgz
Source44: http://registry.npmjs.org/babylon/-/babylon-6.8.4.tgz
Source45: http://registry.npmjs.org/invariant/-/invariant-2.2.1.tgz
Source46: http://registry.npmjs.org/private/-/private-0.1.6.tgz
Source47: http://registry.npmjs.org/globals/-/globals-8.18.0.tgz
Source48: http://registry.npmjs.org/debug/-/debug-2.2.0.tgz
Source49: http://registry.npmjs.org/regenerate/-/regenerate-1.3.1.tgz
Source50: http://registry.npmjs.org/regjsgen/-/regjsgen-0.2.0.tgz
Source51: http://registry.npmjs.org/babel-helper-hoist-variables/-/babel-helper-hoist-variables-6.8.0.tgz
Source52: http://registry.npmjs.org/regjsparser/-/regjsparser-0.1.5.tgz
Source53: http://registry.npmjs.org/babel-generator/-/babel-generator-6.11.4.tgz
Source54: http://registry.npmjs.org/babel-helpers/-/babel-helpers-6.8.0.tgz
Source55: http://registry.npmjs.org/babel-register/-/babel-register-6.11.6.tgz
Source56: http://registry.npmjs.org/convert-source-map/-/convert-source-map-1.3.0.tgz
Source57: http://registry.npmjs.org/path-exists/-/path-exists-1.0.0.tgz
Source58: http://registry.npmjs.org/json5/-/json5-0.4.0.tgz
Source59: http://registry.npmjs.org/slash/-/slash-1.0.0.tgz
Source60: http://registry.npmjs.org/shebang-regex/-/shebang-regex-1.0.0.tgz
Source61: http://registry.npmjs.org/source-map/-/source-map-0.5.6.tgz
Source62: http://registry.npmjs.org/path-is-absolute/-/path-is-absolute-1.0.0.tgz
Source63: http://registry.npmjs.org/minimatch/-/minimatch-3.0.2.tgz
Source64: http://registry.npmjs.org/js-tokens/-/js-tokens-2.0.0.tgz
Source65: http://registry.npmjs.org/chalk/-/chalk-1.1.3.tgz
Source66: http://registry.npmjs.org/ms/-/ms-0.7.1.tgz
Source67: http://registry.npmjs.org/loose-envify/-/loose-envify-1.2.0.tgz
Source68: http://registry.npmjs.org/detect-indent/-/detect-indent-3.0.1.tgz
Source69: http://registry.npmjs.org/jsesc/-/jsesc-0.5.0.tgz
Source70: http://registry.npmjs.org/home-or-tmp/-/home-or-tmp-1.0.0.tgz
Source71: http://registry.npmjs.org/source-map-support/-/source-map-support-0.2.10.tgz
Source72: http://registry.npmjs.org/mkdirp/-/mkdirp-0.5.1.tgz
Source73: http://registry.npmjs.org/has-ansi/-/has-ansi-2.0.0.tgz
Source74: http://registry.npmjs.org/escape-string-regexp/-/escape-string-regexp-1.0.5.tgz
Source75: http://registry.npmjs.org/ansi-styles/-/ansi-styles-2.2.1.tgz
Source76: http://registry.npmjs.org/strip-ansi/-/strip-ansi-3.0.1.tgz
Source77: http://registry.npmjs.org/supports-color/-/supports-color-2.0.0.tgz
Source78: http://registry.npmjs.org/js-tokens/-/js-tokens-1.0.3.tgz
Source79: http://registry.npmjs.org/minimist/-/minimist-1.2.0.tgz
Source80: http://registry.npmjs.org/os-tmpdir/-/os-tmpdir-1.0.1.tgz
Source81: http://registry.npmjs.org/get-stdin/-/get-stdin-4.0.1.tgz
Source82: http://registry.npmjs.org/repeating/-/repeating-1.1.3.tgz
Source83: http://registry.npmjs.org/user-home/-/user-home-1.1.1.tgz
Source84: http://registry.npmjs.org/source-map/-/source-map-0.1.32.tgz
Source85: http://registry.npmjs.org/ansi-regex/-/ansi-regex-2.0.0.tgz
Source86: http://registry.npmjs.org/minimist/-/minimist-0.0.8.tgz
Source87: http://registry.npmjs.org/is-finite/-/is-finite-1.0.1.tgz
Source88: http://registry.npmjs.org/amdefine/-/amdefine-1.0.0.tgz
Source89: http://registry.npmjs.org/brace-expansion/-/brace-expansion-1.1.6.tgz
Source90: http://registry.npmjs.org/number-is-nan/-/number-is-nan-1.0.0.tgz
Source91: http://registry.npmjs.org/concat-map/-/concat-map-0.0.1.tgz
Source92: http://registry.npmjs.org/balanced-match/-/balanced-match-0.4.2.tgz
Source93: babel-preset-es2015-6.6.0-registry.npmjs.org.tgz
Requires: nodejs(engine)
BuildRequires: nodejs-devel
BuildRequires: nodejs-packaging
BuildRequires: npm
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch
Provides: npm(%{npm_name}) = %{version}
Provides: bundled-npm(babel-preset-es2015) = 6.6.0
Provides: bundled-npm(babel-plugin-transform-es2015-object-super) = 6.8.0
Provides: bundled-npm(babel-plugin-transform-es2015-block-scoped-functions) = 6.8.0
Provides: bundled-npm(babel-plugin-transform-es2015-shorthand-properties) = 6.8.0
Provides: bundled-npm(babel-plugin-transform-es2015-function-name) = 6.9.0
Provides: bundled-npm(babel-plugin-transform-es2015-template-literals) = 6.8.0
Provides: bundled-npm(babel-plugin-transform-es2015-classes) = 6.9.0
Provides: bundled-npm(babel-plugin-transform-es2015-literals) = 6.8.0
Provides: bundled-npm(babel-plugin-transform-es2015-arrow-functions) = 6.8.0
Provides: bundled-npm(babel-plugin-transform-es2015-duplicate-keys) = 6.8.0
Provides: bundled-npm(babel-plugin-transform-es2015-computed-properties) = 6.8.0
Provides: bundled-npm(babel-plugin-transform-es2015-sticky-regex) = 6.8.0
Provides: bundled-npm(babel-plugin-transform-es2015-for-of) = 6.8.0
Provides: bundled-npm(babel-plugin-check-es2015-constants) = 6.8.0
Provides: bundled-npm(babel-plugin-transform-es2015-parameters) = 6.11.4
Provides: bundled-npm(babel-plugin-transform-es2015-block-scoping) = 6.10.1
Provides: bundled-npm(babel-plugin-transform-es2015-unicode-regex) = 6.11.0
Provides: bundled-npm(babel-plugin-transform-es2015-spread) = 6.8.0
Provides: bundled-npm(babel-plugin-transform-es2015-typeof-symbol) = 6.8.0
Provides: bundled-npm(babel-runtime) = 6.11.6
Provides: bundled-npm(babel-plugin-transform-es2015-modules-commonjs) = 6.11.5
Provides: bundled-npm(babel-plugin-transform-es2015-destructuring) = 6.9.0
Provides: bundled-npm(babel-helper-function-name) = 6.8.0
Provides: bundled-npm(babel-helper-replace-supers) = 6.8.0
Provides: bundled-npm(babel-types) = 6.11.1
Provides: bundled-npm(babel-plugin-transform-regenerator) = 6.11.4
Provides: bundled-npm(babel-helper-optimise-call-expression) = 6.8.0
Provides: bundled-npm(babel-traverse) = 6.12.0
Provides: bundled-npm(babel-template) = 6.9.0
Provides: bundled-npm(babel-messages) = 6.8.0
Provides: bundled-npm(babel-helper-define-map) = 6.9.0
Provides: bundled-npm(babel-helper-regex) = 6.9.0
Provides: bundled-npm(babel-helper-get-function-arity) = 6.8.0
Provides: bundled-npm(babel-helper-call-delegate) = 6.8.0
Provides: bundled-npm(regexpu-core) = 2.0.0
Provides: bundled-npm(lodash) = 4.14.0
Provides: bundled-npm(core-js) = 2.4.1
Provides: bundled-npm(regenerator-runtime) = 0.9.5
Provides: bundled-npm(babel-plugin-transform-strict-mode) = 6.11.3
Provides: bundled-npm(esutils) = 2.0.2
Provides: bundled-npm(to-fast-properties) = 1.0.2
Provides: bundled-npm(babel-core) = 6.11.4
Provides: bundled-npm(babel-plugin-syntax-async-functions) = 6.8.0
Provides: bundled-npm(babel-code-frame) = 6.11.0
Provides: bundled-npm(babylon) = 6.8.4
Provides: bundled-npm(invariant) = 2.2.1
Provides: bundled-npm(private) = 0.1.6
Provides: bundled-npm(globals) = 8.18.0
Provides: bundled-npm(debug) = 2.2.0
Provides: bundled-npm(regenerate) = 1.3.1
Provides: bundled-npm(regjsgen) = 0.2.0
Provides: bundled-npm(babel-helper-hoist-variables) = 6.8.0
Provides: bundled-npm(regjsparser) = 0.1.5
Provides: bundled-npm(babel-generator) = 6.11.4
Provides: bundled-npm(babel-helpers) = 6.8.0
Provides: bundled-npm(babel-register) = 6.11.6
Provides: bundled-npm(convert-source-map) = 1.3.0
Provides: bundled-npm(path-exists) = 1.0.0
Provides: bundled-npm(json5) = 0.4.0
Provides: bundled-npm(slash) = 1.0.0
Provides: bundled-npm(shebang-regex) = 1.0.0
Provides: bundled-npm(source-map) = 0.5.6
Provides: bundled-npm(path-is-absolute) = 1.0.0
Provides: bundled-npm(minimatch) = 3.0.2
Provides: bundled-npm(js-tokens) = 2.0.0
Provides: bundled-npm(chalk) = 1.1.3
Provides: bundled-npm(ms) = 0.7.1
Provides: bundled-npm(loose-envify) = 1.2.0
Provides: bundled-npm(detect-indent) = 3.0.1
Provides: bundled-npm(jsesc) = 0.5.0
Provides: bundled-npm(home-or-tmp) = 1.0.0
Provides: bundled-npm(source-map-support) = 0.2.10
Provides: bundled-npm(mkdirp) = 0.5.1
Provides: bundled-npm(has-ansi) = 2.0.0
Provides: bundled-npm(escape-string-regexp) = 1.0.5
Provides: bundled-npm(ansi-styles) = 2.2.1
Provides: bundled-npm(strip-ansi) = 3.0.1
Provides: bundled-npm(supports-color) = 2.0.0
Provides: bundled-npm(js-tokens) = 1.0.3
Provides: bundled-npm(minimist) = 1.2.0
Provides: bundled-npm(os-tmpdir) = 1.0.1
Provides: bundled-npm(get-stdin) = 4.0.1
Provides: bundled-npm(repeating) = 1.1.3
Provides: bundled-npm(user-home) = 1.1.1
Provides: bundled-npm(source-map) = 0.1.32
Provides: bundled-npm(ansi-regex) = 2.0.0
Provides: bundled-npm(minimist) = 0.0.8
Provides: bundled-npm(is-finite) = 1.0.1
Provides: bundled-npm(amdefine) = 1.0.0
Provides: bundled-npm(brace-expansion) = 1.1.6
Provides: bundled-npm(number-is-nan) = 1.0.0
Provides: bundled-npm(concat-map) = 0.0.1
Provides: bundled-npm(balanced-match) = 0.4.2
AutoReq: no
AutoProv: no


%description
Babel preset for all es2015 plugins.

%package doc
Summary: Documentation for nodejs-%{npm_name}
Group: Documentation
Requires: nodejs-%{npm_name} = %{version}-%{release}
BuildArch: noarch

%description doc
This package contains documentation for nodejs-%{npm_name}

%prep
mkdir npm_cache
for tgz in %{sources}; do
  echo $tgz | grep -q registry.npmjs.org || npm cache add --cache ./npm_cache $tgz
done

%setup -T -q -a 93 -D -n npm_cache

%build
npm install %{npm_name}@%{version} --cache-min Infinity --cache . --verbose

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cd node_modules/babel-preset-es2015
cp -pfr README.md ../../
cp -pfr index.js package.json node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
# If any binaries are included, symlink them to bindir here
mkdir -p %{buildroot}%{nodejs_sitelib}/${npm_name}/bin
mkdir -p %{buildroot}%{_bindir}/

%check

%files
%{nodejs_sitelib}/%{npm_name}

%doc

%files doc
%doc README.md

%changelog
