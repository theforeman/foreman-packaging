%global npm_name @babel/preset-env

Name: nodejs-babel-preset-env
Version: 7.29.7
Release: 1%{?dist}
Summary: A Babel preset for each environment
License: MIT
Group: Development/Libraries
URL: https://babel.dev/docs/en/next/babel-preset-env
Source0: https://registry.npmjs.org/@babel/code-frame/-/code-frame-7.29.7.tgz
Source1: https://registry.npmjs.org/@babel/compat-data/-/compat-data-7.29.7.tgz
Source2: https://registry.npmjs.org/@babel/generator/-/generator-7.29.8.tgz
Source3: https://registry.npmjs.org/@babel/helper-annotate-as-pure/-/helper-annotate-as-pure-7.29.7.tgz
Source4: https://registry.npmjs.org/@babel/helper-compilation-targets/-/helper-compilation-targets-7.29.7.tgz
Source5: https://registry.npmjs.org/@babel/helper-create-class-features-plugin/-/helper-create-class-features-plugin-7.29.7.tgz
Source6: https://registry.npmjs.org/@babel/helper-create-regexp-features-plugin/-/helper-create-regexp-features-plugin-7.29.7.tgz
Source7: https://registry.npmjs.org/@babel/helper-define-polyfill-provider/-/helper-define-polyfill-provider-0.6.8.tgz
Source8: https://registry.npmjs.org/@babel/helper-globals/-/helper-globals-7.29.7.tgz
Source9: https://registry.npmjs.org/@babel/helper-member-expression-to-functions/-/helper-member-expression-to-functions-7.29.7.tgz
Source10: https://registry.npmjs.org/@babel/helper-module-imports/-/helper-module-imports-7.29.7.tgz
Source11: https://registry.npmjs.org/@babel/helper-module-transforms/-/helper-module-transforms-7.29.7.tgz
Source12: https://registry.npmjs.org/@babel/helper-optimise-call-expression/-/helper-optimise-call-expression-7.29.7.tgz
Source13: https://registry.npmjs.org/@babel/helper-plugin-utils/-/helper-plugin-utils-7.29.7.tgz
Source14: https://registry.npmjs.org/@babel/helper-remap-async-to-generator/-/helper-remap-async-to-generator-7.29.7.tgz
Source15: https://registry.npmjs.org/@babel/helper-replace-supers/-/helper-replace-supers-7.29.7.tgz
Source16: https://registry.npmjs.org/@babel/helper-skip-transparent-expression-wrappers/-/helper-skip-transparent-expression-wrappers-7.29.7.tgz
Source17: https://registry.npmjs.org/@babel/helper-string-parser/-/helper-string-parser-7.29.7.tgz
Source18: https://registry.npmjs.org/@babel/helper-validator-identifier/-/helper-validator-identifier-7.29.7.tgz
Source19: https://registry.npmjs.org/@babel/helper-validator-option/-/helper-validator-option-7.29.7.tgz
Source20: https://registry.npmjs.org/@babel/helper-wrap-function/-/helper-wrap-function-7.29.7.tgz
Source21: https://registry.npmjs.org/@babel/parser/-/parser-7.29.8.tgz
Source22: https://registry.npmjs.org/@babel/plugin-bugfix-firefox-class-in-computed-class-key/-/plugin-bugfix-firefox-class-in-computed-class-key-7.29.7.tgz
Source23: https://registry.npmjs.org/@babel/plugin-bugfix-safari-class-field-initializer-scope/-/plugin-bugfix-safari-class-field-initializer-scope-7.29.7.tgz
Source24: https://registry.npmjs.org/@babel/plugin-bugfix-safari-id-destructuring-collision-in-function-expression/-/plugin-bugfix-safari-id-destructuring-collision-in-function-expression-7.29.7.tgz
Source25: https://registry.npmjs.org/@babel/plugin-bugfix-safari-rest-destructuring-rhs-array/-/plugin-bugfix-safari-rest-destructuring-rhs-array-7.29.7.tgz
Source26: https://registry.npmjs.org/@babel/plugin-bugfix-v8-spread-parameters-in-optional-chaining/-/plugin-bugfix-v8-spread-parameters-in-optional-chaining-7.29.7.tgz
Source27: https://registry.npmjs.org/@babel/plugin-bugfix-v8-static-class-fields-redefine-readonly/-/plugin-bugfix-v8-static-class-fields-redefine-readonly-7.29.7.tgz
Source28: https://registry.npmjs.org/@babel/plugin-proposal-private-property-in-object/-/plugin-proposal-private-property-in-object-7.21.0-placeholder-for-preset-env.2.tgz
Source29: https://registry.npmjs.org/@babel/plugin-syntax-import-assertions/-/plugin-syntax-import-assertions-7.29.7.tgz
Source30: https://registry.npmjs.org/@babel/plugin-syntax-import-attributes/-/plugin-syntax-import-attributes-7.29.7.tgz
Source31: https://registry.npmjs.org/@babel/plugin-syntax-unicode-sets-regex/-/plugin-syntax-unicode-sets-regex-7.18.6.tgz
Source32: https://registry.npmjs.org/@babel/plugin-transform-arrow-functions/-/plugin-transform-arrow-functions-7.29.7.tgz
Source33: https://registry.npmjs.org/@babel/plugin-transform-async-generator-functions/-/plugin-transform-async-generator-functions-7.29.7.tgz
Source34: https://registry.npmjs.org/@babel/plugin-transform-async-to-generator/-/plugin-transform-async-to-generator-7.29.7.tgz
Source35: https://registry.npmjs.org/@babel/plugin-transform-block-scoped-functions/-/plugin-transform-block-scoped-functions-7.29.7.tgz
Source36: https://registry.npmjs.org/@babel/plugin-transform-block-scoping/-/plugin-transform-block-scoping-7.29.7.tgz
Source37: https://registry.npmjs.org/@babel/plugin-transform-class-properties/-/plugin-transform-class-properties-7.29.7.tgz
Source38: https://registry.npmjs.org/@babel/plugin-transform-class-static-block/-/plugin-transform-class-static-block-7.29.7.tgz
Source39: https://registry.npmjs.org/@babel/plugin-transform-classes/-/plugin-transform-classes-7.29.7.tgz
Source40: https://registry.npmjs.org/@babel/plugin-transform-computed-properties/-/plugin-transform-computed-properties-7.29.7.tgz
Source41: https://registry.npmjs.org/@babel/plugin-transform-destructuring/-/plugin-transform-destructuring-7.29.7.tgz
Source42: https://registry.npmjs.org/@babel/plugin-transform-dotall-regex/-/plugin-transform-dotall-regex-7.29.7.tgz
Source43: https://registry.npmjs.org/@babel/plugin-transform-duplicate-keys/-/plugin-transform-duplicate-keys-7.29.7.tgz
Source44: https://registry.npmjs.org/@babel/plugin-transform-duplicate-named-capturing-groups-regex/-/plugin-transform-duplicate-named-capturing-groups-regex-7.29.7.tgz
Source45: https://registry.npmjs.org/@babel/plugin-transform-dynamic-import/-/plugin-transform-dynamic-import-7.29.7.tgz
Source46: https://registry.npmjs.org/@babel/plugin-transform-explicit-resource-management/-/plugin-transform-explicit-resource-management-7.29.7.tgz
Source47: https://registry.npmjs.org/@babel/plugin-transform-exponentiation-operator/-/plugin-transform-exponentiation-operator-7.29.7.tgz
Source48: https://registry.npmjs.org/@babel/plugin-transform-export-namespace-from/-/plugin-transform-export-namespace-from-7.29.7.tgz
Source49: https://registry.npmjs.org/@babel/plugin-transform-for-of/-/plugin-transform-for-of-7.29.7.tgz
Source50: https://registry.npmjs.org/@babel/plugin-transform-function-name/-/plugin-transform-function-name-7.29.7.tgz
Source51: https://registry.npmjs.org/@babel/plugin-transform-json-strings/-/plugin-transform-json-strings-7.29.7.tgz
Source52: https://registry.npmjs.org/@babel/plugin-transform-literals/-/plugin-transform-literals-7.29.7.tgz
Source53: https://registry.npmjs.org/@babel/plugin-transform-logical-assignment-operators/-/plugin-transform-logical-assignment-operators-7.29.7.tgz
Source54: https://registry.npmjs.org/@babel/plugin-transform-member-expression-literals/-/plugin-transform-member-expression-literals-7.29.7.tgz
Source55: https://registry.npmjs.org/@babel/plugin-transform-modules-amd/-/plugin-transform-modules-amd-7.29.7.tgz
Source56: https://registry.npmjs.org/@babel/plugin-transform-modules-commonjs/-/plugin-transform-modules-commonjs-7.29.7.tgz
Source57: https://registry.npmjs.org/@babel/plugin-transform-modules-systemjs/-/plugin-transform-modules-systemjs-7.29.8.tgz
Source58: https://registry.npmjs.org/@babel/plugin-transform-modules-umd/-/plugin-transform-modules-umd-7.29.7.tgz
Source59: https://registry.npmjs.org/@babel/plugin-transform-named-capturing-groups-regex/-/plugin-transform-named-capturing-groups-regex-7.29.7.tgz
Source60: https://registry.npmjs.org/@babel/plugin-transform-new-target/-/plugin-transform-new-target-7.29.7.tgz
Source61: https://registry.npmjs.org/@babel/plugin-transform-nullish-coalescing-operator/-/plugin-transform-nullish-coalescing-operator-7.29.7.tgz
Source62: https://registry.npmjs.org/@babel/plugin-transform-numeric-separator/-/plugin-transform-numeric-separator-7.29.7.tgz
Source63: https://registry.npmjs.org/@babel/plugin-transform-object-rest-spread/-/plugin-transform-object-rest-spread-7.29.7.tgz
Source64: https://registry.npmjs.org/@babel/plugin-transform-object-super/-/plugin-transform-object-super-7.29.7.tgz
Source65: https://registry.npmjs.org/@babel/plugin-transform-optional-catch-binding/-/plugin-transform-optional-catch-binding-7.29.7.tgz
Source66: https://registry.npmjs.org/@babel/plugin-transform-optional-chaining/-/plugin-transform-optional-chaining-7.29.7.tgz
Source67: https://registry.npmjs.org/@babel/plugin-transform-parameters/-/plugin-transform-parameters-7.29.7.tgz
Source68: https://registry.npmjs.org/@babel/plugin-transform-private-methods/-/plugin-transform-private-methods-7.29.7.tgz
Source69: https://registry.npmjs.org/@babel/plugin-transform-private-property-in-object/-/plugin-transform-private-property-in-object-7.29.7.tgz
Source70: https://registry.npmjs.org/@babel/plugin-transform-property-literals/-/plugin-transform-property-literals-7.29.7.tgz
Source71: https://registry.npmjs.org/@babel/plugin-transform-regenerator/-/plugin-transform-regenerator-7.29.8.tgz
Source72: https://registry.npmjs.org/@babel/plugin-transform-regexp-modifiers/-/plugin-transform-regexp-modifiers-7.29.7.tgz
Source73: https://registry.npmjs.org/@babel/plugin-transform-reserved-words/-/plugin-transform-reserved-words-7.29.7.tgz
Source74: https://registry.npmjs.org/@babel/plugin-transform-shorthand-properties/-/plugin-transform-shorthand-properties-7.29.7.tgz
Source75: https://registry.npmjs.org/@babel/plugin-transform-spread/-/plugin-transform-spread-7.29.8.tgz
Source76: https://registry.npmjs.org/@babel/plugin-transform-sticky-regex/-/plugin-transform-sticky-regex-7.29.7.tgz
Source77: https://registry.npmjs.org/@babel/plugin-transform-template-literals/-/plugin-transform-template-literals-7.29.7.tgz
Source78: https://registry.npmjs.org/@babel/plugin-transform-typeof-symbol/-/plugin-transform-typeof-symbol-7.29.7.tgz
Source79: https://registry.npmjs.org/@babel/plugin-transform-unicode-escapes/-/plugin-transform-unicode-escapes-7.29.7.tgz
Source80: https://registry.npmjs.org/@babel/plugin-transform-unicode-property-regex/-/plugin-transform-unicode-property-regex-7.29.7.tgz
Source81: https://registry.npmjs.org/@babel/plugin-transform-unicode-regex/-/plugin-transform-unicode-regex-7.29.7.tgz
Source82: https://registry.npmjs.org/@babel/plugin-transform-unicode-sets-regex/-/plugin-transform-unicode-sets-regex-7.29.7.tgz
Source83: https://registry.npmjs.org/@babel/preset-env/-/preset-env-7.29.7.tgz
Source84: https://registry.npmjs.org/@babel/preset-modules/-/preset-modules-0.1.6-no-external-plugins.tgz
Source85: https://registry.npmjs.org/@babel/template/-/template-7.29.7.tgz
Source86: https://registry.npmjs.org/@babel/traverse/-/traverse-7.29.8.tgz
Source87: https://registry.npmjs.org/@babel/types/-/types-7.29.8.tgz
Source88: https://registry.npmjs.org/@jridgewell/gen-mapping/-/gen-mapping-0.3.13.tgz
Source89: https://registry.npmjs.org/@jridgewell/resolve-uri/-/resolve-uri-3.1.2.tgz
Source90: https://registry.npmjs.org/@jridgewell/sourcemap-codec/-/sourcemap-codec-1.5.5.tgz
Source91: https://registry.npmjs.org/@jridgewell/trace-mapping/-/trace-mapping-0.3.31.tgz
Source92: https://registry.npmjs.org/babel-plugin-polyfill-corejs2/-/babel-plugin-polyfill-corejs2-0.4.17.tgz
Source93: https://registry.npmjs.org/babel-plugin-polyfill-corejs3/-/babel-plugin-polyfill-corejs3-0.14.2.tgz
Source94: https://registry.npmjs.org/babel-plugin-polyfill-regenerator/-/babel-plugin-polyfill-regenerator-0.6.8.tgz
Source95: https://registry.npmjs.org/baseline-browser-mapping/-/baseline-browser-mapping-2.11.12.tgz
Source96: https://registry.npmjs.org/browserslist/-/browserslist-4.28.7.tgz
Source97: https://registry.npmjs.org/caniuse-lite/-/caniuse-lite-1.0.30001807.tgz
Source98: https://registry.npmjs.org/core-js-compat/-/core-js-compat-3.50.0.tgz
Source99: https://registry.npmjs.org/debug/-/debug-4.4.3.tgz
Source100: https://registry.npmjs.org/electron-to-chromium/-/electron-to-chromium-1.5.402.tgz
Source101: https://registry.npmjs.org/es-errors/-/es-errors-1.3.0.tgz
Source102: https://registry.npmjs.org/escalade/-/escalade-3.2.0.tgz
Source103: https://registry.npmjs.org/esutils/-/esutils-2.0.3.tgz
Source104: https://registry.npmjs.org/function-bind/-/function-bind-1.1.2.tgz
Source105: https://registry.npmjs.org/hasown/-/hasown-2.0.4.tgz
Source106: https://registry.npmjs.org/is-core-module/-/is-core-module-2.16.2.tgz
Source107: https://registry.npmjs.org/js-tokens/-/js-tokens-4.0.0.tgz
Source108: https://registry.npmjs.org/jsesc/-/jsesc-3.1.0.tgz
Source109: https://registry.npmjs.org/lodash.debounce/-/lodash.debounce-4.0.8.tgz
Source110: https://registry.npmjs.org/lru-cache/-/lru-cache-5.1.1.tgz
Source111: https://registry.npmjs.org/ms/-/ms-2.1.3.tgz
Source112: https://registry.npmjs.org/node-releases/-/node-releases-2.0.53.tgz
Source113: https://registry.npmjs.org/path-parse/-/path-parse-1.0.7.tgz
Source114: https://registry.npmjs.org/picocolors/-/picocolors-1.1.1.tgz
Source115: https://registry.npmjs.org/regenerate/-/regenerate-1.4.2.tgz
Source116: https://registry.npmjs.org/regenerate-unicode-properties/-/regenerate-unicode-properties-10.2.2.tgz
Source117: https://registry.npmjs.org/regexpu-core/-/regexpu-core-6.4.0.tgz
Source118: https://registry.npmjs.org/regjsgen/-/regjsgen-0.8.0.tgz
Source119: https://registry.npmjs.org/regjsparser/-/regjsparser-0.13.2.tgz
Source120: https://registry.npmjs.org/resolve/-/resolve-1.22.12.tgz
Source121: https://registry.npmjs.org/semver/-/semver-6.3.1.tgz
Source122: https://registry.npmjs.org/supports-preserve-symlinks-flag/-/supports-preserve-symlinks-flag-1.0.0.tgz
Source123: https://registry.npmjs.org/unicode-canonical-property-names-ecmascript/-/unicode-canonical-property-names-ecmascript-2.0.1.tgz
Source124: https://registry.npmjs.org/unicode-match-property-ecmascript/-/unicode-match-property-ecmascript-2.0.0.tgz
Source125: https://registry.npmjs.org/unicode-match-property-value-ecmascript/-/unicode-match-property-value-ecmascript-2.2.1.tgz
Source126: https://registry.npmjs.org/unicode-property-aliases-ecmascript/-/unicode-property-aliases-ecmascript-2.2.0.tgz
Source127: https://registry.npmjs.org/update-browserslist-db/-/update-browserslist-db-1.2.3.tgz
Source128: https://registry.npmjs.org/yallist/-/yallist-3.1.1.tgz
Source129: nodejs-babel-preset-env-%{version}-package-lock.json
BuildRequires: npm >= 7
BuildRequires: nodejs-packaging
# The prep section runs node directly, so this is needed unconditionally. It
# also works around https://issues.redhat.com/browse/RHEL-137712 on RHEL 10
# before 10.3, where the nodejs major version macro does not resolve without
# node in the buildroot.
BuildRequires: /usr/bin/node
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: npm(%{npm_name}) = %{version}
Provides: bundled(npm(@babel/code-frame)) = 7.29.7
Provides: bundled(npm(@babel/compat-data)) = 7.29.7
Provides: bundled(npm(@babel/generator)) = 7.29.8
Provides: bundled(npm(@babel/helper-annotate-as-pure)) = 7.29.7
Provides: bundled(npm(@babel/helper-compilation-targets)) = 7.29.7
Provides: bundled(npm(@babel/helper-create-class-features-plugin)) = 7.29.7
Provides: bundled(npm(@babel/helper-create-regexp-features-plugin)) = 7.29.7
Provides: bundled(npm(@babel/helper-define-polyfill-provider)) = 0.6.8
Provides: bundled(npm(@babel/helper-globals)) = 7.29.7
Provides: bundled(npm(@babel/helper-member-expression-to-functions)) = 7.29.7
Provides: bundled(npm(@babel/helper-module-imports)) = 7.29.7
Provides: bundled(npm(@babel/helper-module-transforms)) = 7.29.7
Provides: bundled(npm(@babel/helper-optimise-call-expression)) = 7.29.7
Provides: bundled(npm(@babel/helper-plugin-utils)) = 7.29.7
Provides: bundled(npm(@babel/helper-remap-async-to-generator)) = 7.29.7
Provides: bundled(npm(@babel/helper-replace-supers)) = 7.29.7
Provides: bundled(npm(@babel/helper-skip-transparent-expression-wrappers)) = 7.29.7
Provides: bundled(npm(@babel/helper-string-parser)) = 7.29.7
Provides: bundled(npm(@babel/helper-validator-identifier)) = 7.29.7
Provides: bundled(npm(@babel/helper-validator-option)) = 7.29.7
Provides: bundled(npm(@babel/helper-wrap-function)) = 7.29.7
Provides: bundled(npm(@babel/parser)) = 7.29.8
Provides: bundled(npm(@babel/plugin-bugfix-firefox-class-in-computed-class-key)) = 7.29.7
Provides: bundled(npm(@babel/plugin-bugfix-safari-class-field-initializer-scope)) = 7.29.7
Provides: bundled(npm(@babel/plugin-bugfix-safari-id-destructuring-collision-in-function-expression)) = 7.29.7
Provides: bundled(npm(@babel/plugin-bugfix-safari-rest-destructuring-rhs-array)) = 7.29.7
Provides: bundled(npm(@babel/plugin-bugfix-v8-spread-parameters-in-optional-chaining)) = 7.29.7
Provides: bundled(npm(@babel/plugin-bugfix-v8-static-class-fields-redefine-readonly)) = 7.29.7
Provides: bundled(npm(@babel/plugin-proposal-private-property-in-object)) = 7.21.0^placeholder.for.preset.env.2
Provides: bundled(npm(@babel/plugin-syntax-import-assertions)) = 7.29.7
Provides: bundled(npm(@babel/plugin-syntax-import-attributes)) = 7.29.7
Provides: bundled(npm(@babel/plugin-syntax-unicode-sets-regex)) = 7.18.6
Provides: bundled(npm(@babel/plugin-transform-arrow-functions)) = 7.29.7
Provides: bundled(npm(@babel/plugin-transform-async-generator-functions)) = 7.29.7
Provides: bundled(npm(@babel/plugin-transform-async-to-generator)) = 7.29.7
Provides: bundled(npm(@babel/plugin-transform-block-scoped-functions)) = 7.29.7
Provides: bundled(npm(@babel/plugin-transform-block-scoping)) = 7.29.7
Provides: bundled(npm(@babel/plugin-transform-class-properties)) = 7.29.7
Provides: bundled(npm(@babel/plugin-transform-class-static-block)) = 7.29.7
Provides: bundled(npm(@babel/plugin-transform-classes)) = 7.29.7
Provides: bundled(npm(@babel/plugin-transform-computed-properties)) = 7.29.7
Provides: bundled(npm(@babel/plugin-transform-destructuring)) = 7.29.7
Provides: bundled(npm(@babel/plugin-transform-dotall-regex)) = 7.29.7
Provides: bundled(npm(@babel/plugin-transform-duplicate-keys)) = 7.29.7
Provides: bundled(npm(@babel/plugin-transform-duplicate-named-capturing-groups-regex)) = 7.29.7
Provides: bundled(npm(@babel/plugin-transform-dynamic-import)) = 7.29.7
Provides: bundled(npm(@babel/plugin-transform-explicit-resource-management)) = 7.29.7
Provides: bundled(npm(@babel/plugin-transform-exponentiation-operator)) = 7.29.7
Provides: bundled(npm(@babel/plugin-transform-export-namespace-from)) = 7.29.7
Provides: bundled(npm(@babel/plugin-transform-for-of)) = 7.29.7
Provides: bundled(npm(@babel/plugin-transform-function-name)) = 7.29.7
Provides: bundled(npm(@babel/plugin-transform-json-strings)) = 7.29.7
Provides: bundled(npm(@babel/plugin-transform-literals)) = 7.29.7
Provides: bundled(npm(@babel/plugin-transform-logical-assignment-operators)) = 7.29.7
Provides: bundled(npm(@babel/plugin-transform-member-expression-literals)) = 7.29.7
Provides: bundled(npm(@babel/plugin-transform-modules-amd)) = 7.29.7
Provides: bundled(npm(@babel/plugin-transform-modules-commonjs)) = 7.29.7
Provides: bundled(npm(@babel/plugin-transform-modules-systemjs)) = 7.29.8
Provides: bundled(npm(@babel/plugin-transform-modules-umd)) = 7.29.7
Provides: bundled(npm(@babel/plugin-transform-named-capturing-groups-regex)) = 7.29.7
Provides: bundled(npm(@babel/plugin-transform-new-target)) = 7.29.7
Provides: bundled(npm(@babel/plugin-transform-nullish-coalescing-operator)) = 7.29.7
Provides: bundled(npm(@babel/plugin-transform-numeric-separator)) = 7.29.7
Provides: bundled(npm(@babel/plugin-transform-object-rest-spread)) = 7.29.7
Provides: bundled(npm(@babel/plugin-transform-object-super)) = 7.29.7
Provides: bundled(npm(@babel/plugin-transform-optional-catch-binding)) = 7.29.7
Provides: bundled(npm(@babel/plugin-transform-optional-chaining)) = 7.29.7
Provides: bundled(npm(@babel/plugin-transform-parameters)) = 7.29.7
Provides: bundled(npm(@babel/plugin-transform-private-methods)) = 7.29.7
Provides: bundled(npm(@babel/plugin-transform-private-property-in-object)) = 7.29.7
Provides: bundled(npm(@babel/plugin-transform-property-literals)) = 7.29.7
Provides: bundled(npm(@babel/plugin-transform-regenerator)) = 7.29.8
Provides: bundled(npm(@babel/plugin-transform-regexp-modifiers)) = 7.29.7
Provides: bundled(npm(@babel/plugin-transform-reserved-words)) = 7.29.7
Provides: bundled(npm(@babel/plugin-transform-shorthand-properties)) = 7.29.7
Provides: bundled(npm(@babel/plugin-transform-spread)) = 7.29.8
Provides: bundled(npm(@babel/plugin-transform-sticky-regex)) = 7.29.7
Provides: bundled(npm(@babel/plugin-transform-template-literals)) = 7.29.7
Provides: bundled(npm(@babel/plugin-transform-typeof-symbol)) = 7.29.7
Provides: bundled(npm(@babel/plugin-transform-unicode-escapes)) = 7.29.7
Provides: bundled(npm(@babel/plugin-transform-unicode-property-regex)) = 7.29.7
Provides: bundled(npm(@babel/plugin-transform-unicode-regex)) = 7.29.7
Provides: bundled(npm(@babel/plugin-transform-unicode-sets-regex)) = 7.29.7
Provides: bundled(npm(@babel/preset-env)) = 7.29.7
Provides: bundled(npm(@babel/preset-modules)) = 0.1.6^no.external.plugins
Provides: bundled(npm(@babel/template)) = 7.29.7
Provides: bundled(npm(@babel/traverse)) = 7.29.8
Provides: bundled(npm(@babel/types)) = 7.29.8
Provides: bundled(npm(@jridgewell/gen-mapping)) = 0.3.13
Provides: bundled(npm(@jridgewell/resolve-uri)) = 3.1.2
Provides: bundled(npm(@jridgewell/sourcemap-codec)) = 1.5.5
Provides: bundled(npm(@jridgewell/trace-mapping)) = 0.3.31
Provides: bundled(npm(babel-plugin-polyfill-corejs2)) = 0.4.17
Provides: bundled(npm(babel-plugin-polyfill-corejs3)) = 0.14.2
Provides: bundled(npm(babel-plugin-polyfill-regenerator)) = 0.6.8
Provides: bundled(npm(baseline-browser-mapping)) = 2.11.12
Provides: bundled(npm(browserslist)) = 4.28.7
Provides: bundled(npm(caniuse-lite)) = 1.0.30001807
Provides: bundled(npm(core-js-compat)) = 3.50.0
Provides: bundled(npm(debug)) = 4.4.3
Provides: bundled(npm(electron-to-chromium)) = 1.5.402
Provides: bundled(npm(es-errors)) = 1.3.0
Provides: bundled(npm(escalade)) = 3.2.0
Provides: bundled(npm(esutils)) = 2.0.3
Provides: bundled(npm(function-bind)) = 1.1.2
Provides: bundled(npm(hasown)) = 2.0.4
Provides: bundled(npm(is-core-module)) = 2.16.2
Provides: bundled(npm(js-tokens)) = 4.0.0
Provides: bundled(npm(jsesc)) = 3.1.0
Provides: bundled(npm(lodash.debounce)) = 4.0.8
Provides: bundled(npm(lru-cache)) = 5.1.1
Provides: bundled(npm(ms)) = 2.1.3
Provides: bundled(npm(node-releases)) = 2.0.53
Provides: bundled(npm(path-parse)) = 1.0.7
Provides: bundled(npm(picocolors)) = 1.1.1
Provides: bundled(npm(regenerate)) = 1.4.2
Provides: bundled(npm(regenerate-unicode-properties)) = 10.2.2
Provides: bundled(npm(regexpu-core)) = 6.4.0
Provides: bundled(npm(regjsgen)) = 0.8.0
Provides: bundled(npm(regjsparser)) = 0.13.2
Provides: bundled(npm(resolve)) = 1.22.12
Provides: bundled(npm(semver)) = 6.3.1
Provides: bundled(npm(supports-preserve-symlinks-flag)) = 1.0.0
Provides: bundled(npm(unicode-canonical-property-names-ecmascript)) = 2.0.1
Provides: bundled(npm(unicode-match-property-ecmascript)) = 2.0.0
Provides: bundled(npm(unicode-match-property-value-ecmascript)) = 2.2.1
Provides: bundled(npm(unicode-property-aliases-ecmascript)) = 2.2.0
Provides: bundled(npm(update-browserslist-db)) = 1.2.3
Provides: bundled(npm(yallist)) = 3.1.1
AutoReq: no
AutoProv: no

%define npm_cache_dir npm_cache_%{name}-%{version}-%{release}

%description
%{summary}

%prep
# There is deliberately no setup section: every Source is consumed explicitly
# below, so the build runs in the top-level build directory. Do not name the
# setup macro here even in a comment - rpm expands macros inside comments, and
# on rpm 6 that runs it, unpacking Source0 and cd-ing into a directory that
# does not exist.
mkdir -p %{npm_cache_dir}
# npm ci installs the tree recorded in the lockfile: every entry carries a
# resolved URL and an integrity hash, and npm serves the tarballs from the
# cache primed here by content hash. No registry access is needed.
for src in %{sources}; do
  case "$src" in
    *.tgz) npm cache add --cache %{npm_cache_dir} "$src" ;;
    *-package-lock.json) cp "$src" package-lock.json ;;
    *) echo "unexpected Source, do not know how to handle it: $src" >&2; exit 1 ;;
  esac
done

# Derive package.json from the lockfile so the two cannot disagree.
node -e '
const fs = require("fs");
const lock = JSON.parse(fs.readFileSync("package-lock.json"));
fs.writeFileSync("package.json", JSON.stringify({
  name: lock.name,
  version: lock.version,
  dependencies: lock.packages[""].dependencies
}, null, 2) + "\n");
'

%build
npm ci --legacy-peer-deps --offline --cache %{_builddir}/%{npm_cache_dir} --omit optional

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
# npm creates a scope directory for every scope named in the lockfile, including
# scopes whose packages were all omitted, which leaves empty dirs behind.
# -delete implies -depth, so nested empties go bottom-up in a single pass.
find %{buildroot}%{nodejs_sitelib}/%{npm_name} -type d -empty -delete
cp -pfr node_modules/%{npm_name}/data %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/lib %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%license node_modules/%{npm_name}/LICENSE
%doc node_modules/%{npm_name}/CONTRIBUTING.md
%doc node_modules/%{npm_name}/README.md

%changelog
* Thu Aug 06 2026 MariaAga <mariaaga@redhat.com> 7.29.7-1
- Update to 7.29.7

* Thu Jul 30 2026 Zach Huntington-Meath <zhunting@redhat.com> - 7.9.5-2
- Regenerate with correct npm2rpm strategy

* Thu Jul 30 2026 Zach Huntington-Meath <zhunting@redhat.com> 7.9.5-1
- Update to 7.9.5

* Thu Jul 30 2026 Zach Huntington-Meath <zhunting@redhat.com> 7.9.5-2
- Update to 7.9.5

* Tue Sep 02 2025 Evgeni Golov 7.9.5-1
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
