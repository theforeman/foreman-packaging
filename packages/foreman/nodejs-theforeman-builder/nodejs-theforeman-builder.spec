%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name @theforeman/builder

Name: %{?scl_prefix}nodejs-theforeman-builder
Version: 4.14.0
Release: 1%{?dist}
Summary: Build production and development bundle files for foreman core and plugins
License: MIT
Group: Development/Libraries
URL: https://github.com/theforeman/foreman-js#readme
Source0: https://registry.npmjs.org/@babel/code-frame/-/code-frame-7.10.4.tgz
Source1: https://registry.npmjs.org/@babel/compat-data/-/compat-data-7.11.0.tgz
Source2: https://registry.npmjs.org/@babel/core/-/core-7.11.1.tgz
Source3: https://registry.npmjs.org/@babel/generator/-/generator-7.11.0.tgz
Source4: https://registry.npmjs.org/@babel/helper-annotate-as-pure/-/helper-annotate-as-pure-7.10.4.tgz
Source5: https://registry.npmjs.org/@babel/helper-builder-binary-assignment-operator-visitor/-/helper-builder-binary-assignment-operator-visitor-7.10.4.tgz
Source6: https://registry.npmjs.org/@babel/helper-builder-react-jsx/-/helper-builder-react-jsx-7.10.4.tgz
Source7: https://registry.npmjs.org/@babel/helper-builder-react-jsx-experimental/-/helper-builder-react-jsx-experimental-7.10.5.tgz
Source8: https://registry.npmjs.org/@babel/helper-compilation-targets/-/helper-compilation-targets-7.10.4.tgz
Source9: https://registry.npmjs.org/@babel/helper-create-class-features-plugin/-/helper-create-class-features-plugin-7.10.5.tgz
Source10: https://registry.npmjs.org/@babel/helper-create-regexp-features-plugin/-/helper-create-regexp-features-plugin-7.10.4.tgz
Source11: https://registry.npmjs.org/@babel/helper-define-map/-/helper-define-map-7.10.5.tgz
Source12: https://registry.npmjs.org/@babel/helper-explode-assignable-expression/-/helper-explode-assignable-expression-7.10.4.tgz
Source13: https://registry.npmjs.org/@babel/helper-function-name/-/helper-function-name-7.10.4.tgz
Source14: https://registry.npmjs.org/@babel/helper-get-function-arity/-/helper-get-function-arity-7.10.4.tgz
Source15: https://registry.npmjs.org/@babel/helper-hoist-variables/-/helper-hoist-variables-7.10.4.tgz
Source16: https://registry.npmjs.org/@babel/helper-member-expression-to-functions/-/helper-member-expression-to-functions-7.11.0.tgz
Source17: https://registry.npmjs.org/@babel/helper-module-imports/-/helper-module-imports-7.10.4.tgz
Source18: https://registry.npmjs.org/@babel/helper-module-transforms/-/helper-module-transforms-7.11.0.tgz
Source19: https://registry.npmjs.org/@babel/helper-optimise-call-expression/-/helper-optimise-call-expression-7.10.4.tgz
Source20: https://registry.npmjs.org/@babel/helper-plugin-utils/-/helper-plugin-utils-7.10.4.tgz
Source21: https://registry.npmjs.org/@babel/helper-regex/-/helper-regex-7.10.5.tgz
Source22: https://registry.npmjs.org/@babel/helper-remap-async-to-generator/-/helper-remap-async-to-generator-7.10.4.tgz
Source23: https://registry.npmjs.org/@babel/helper-replace-supers/-/helper-replace-supers-7.10.4.tgz
Source24: https://registry.npmjs.org/@babel/helper-simple-access/-/helper-simple-access-7.10.4.tgz
Source25: https://registry.npmjs.org/@babel/helper-skip-transparent-expression-wrappers/-/helper-skip-transparent-expression-wrappers-7.11.0.tgz
Source26: https://registry.npmjs.org/@babel/helper-split-export-declaration/-/helper-split-export-declaration-7.11.0.tgz
Source27: https://registry.npmjs.org/@babel/helper-validator-identifier/-/helper-validator-identifier-7.10.4.tgz
Source28: https://registry.npmjs.org/@babel/helper-wrap-function/-/helper-wrap-function-7.10.4.tgz
Source29: https://registry.npmjs.org/@babel/helpers/-/helpers-7.10.4.tgz
Source30: https://registry.npmjs.org/@babel/highlight/-/highlight-7.10.4.tgz
Source31: https://registry.npmjs.org/@babel/parser/-/parser-7.11.3.tgz
Source32: https://registry.npmjs.org/@babel/plugin-proposal-async-generator-functions/-/plugin-proposal-async-generator-functions-7.10.5.tgz
Source33: https://registry.npmjs.org/@babel/plugin-proposal-class-properties/-/plugin-proposal-class-properties-7.10.4.tgz
Source34: https://registry.npmjs.org/@babel/plugin-proposal-dynamic-import/-/plugin-proposal-dynamic-import-7.10.4.tgz
Source35: https://registry.npmjs.org/@babel/plugin-proposal-json-strings/-/plugin-proposal-json-strings-7.10.4.tgz
Source36: https://registry.npmjs.org/@babel/plugin-proposal-nullish-coalescing-operator/-/plugin-proposal-nullish-coalescing-operator-7.10.4.tgz
Source37: https://registry.npmjs.org/@babel/plugin-proposal-numeric-separator/-/plugin-proposal-numeric-separator-7.10.4.tgz
Source38: https://registry.npmjs.org/@babel/plugin-proposal-object-rest-spread/-/plugin-proposal-object-rest-spread-7.11.0.tgz
Source39: https://registry.npmjs.org/@babel/plugin-proposal-optional-catch-binding/-/plugin-proposal-optional-catch-binding-7.10.4.tgz
Source40: https://registry.npmjs.org/@babel/plugin-proposal-optional-chaining/-/plugin-proposal-optional-chaining-7.11.0.tgz
Source41: https://registry.npmjs.org/@babel/plugin-proposal-unicode-property-regex/-/plugin-proposal-unicode-property-regex-7.10.4.tgz
Source42: https://registry.npmjs.org/@babel/plugin-syntax-async-generators/-/plugin-syntax-async-generators-7.8.4.tgz
Source43: https://registry.npmjs.org/@babel/plugin-syntax-dynamic-import/-/plugin-syntax-dynamic-import-7.8.3.tgz
Source44: https://registry.npmjs.org/@babel/plugin-syntax-json-strings/-/plugin-syntax-json-strings-7.8.3.tgz
Source45: https://registry.npmjs.org/@babel/plugin-syntax-jsx/-/plugin-syntax-jsx-7.10.4.tgz
Source46: https://registry.npmjs.org/@babel/plugin-syntax-nullish-coalescing-operator/-/plugin-syntax-nullish-coalescing-operator-7.8.3.tgz
Source47: https://registry.npmjs.org/@babel/plugin-syntax-numeric-separator/-/plugin-syntax-numeric-separator-7.10.4.tgz
Source48: https://registry.npmjs.org/@babel/plugin-syntax-object-rest-spread/-/plugin-syntax-object-rest-spread-7.8.3.tgz
Source49: https://registry.npmjs.org/@babel/plugin-syntax-optional-catch-binding/-/plugin-syntax-optional-catch-binding-7.8.3.tgz
Source50: https://registry.npmjs.org/@babel/plugin-syntax-optional-chaining/-/plugin-syntax-optional-chaining-7.8.3.tgz
Source51: https://registry.npmjs.org/@babel/plugin-syntax-top-level-await/-/plugin-syntax-top-level-await-7.10.4.tgz
Source52: https://registry.npmjs.org/@babel/plugin-transform-arrow-functions/-/plugin-transform-arrow-functions-7.10.4.tgz
Source53: https://registry.npmjs.org/@babel/plugin-transform-async-to-generator/-/plugin-transform-async-to-generator-7.10.4.tgz
Source54: https://registry.npmjs.org/@babel/plugin-transform-block-scoped-functions/-/plugin-transform-block-scoped-functions-7.10.4.tgz
Source55: https://registry.npmjs.org/@babel/plugin-transform-block-scoping/-/plugin-transform-block-scoping-7.11.1.tgz
Source56: https://registry.npmjs.org/@babel/plugin-transform-classes/-/plugin-transform-classes-7.10.4.tgz
Source57: https://registry.npmjs.org/@babel/plugin-transform-computed-properties/-/plugin-transform-computed-properties-7.10.4.tgz
Source58: https://registry.npmjs.org/@babel/plugin-transform-destructuring/-/plugin-transform-destructuring-7.10.4.tgz
Source59: https://registry.npmjs.org/@babel/plugin-transform-dotall-regex/-/plugin-transform-dotall-regex-7.10.4.tgz
Source60: https://registry.npmjs.org/@babel/plugin-transform-duplicate-keys/-/plugin-transform-duplicate-keys-7.10.4.tgz
Source61: https://registry.npmjs.org/@babel/plugin-transform-exponentiation-operator/-/plugin-transform-exponentiation-operator-7.10.4.tgz
Source62: https://registry.npmjs.org/@babel/plugin-transform-for-of/-/plugin-transform-for-of-7.10.4.tgz
Source63: https://registry.npmjs.org/@babel/plugin-transform-function-name/-/plugin-transform-function-name-7.10.4.tgz
Source64: https://registry.npmjs.org/@babel/plugin-transform-literals/-/plugin-transform-literals-7.10.4.tgz
Source65: https://registry.npmjs.org/@babel/plugin-transform-member-expression-literals/-/plugin-transform-member-expression-literals-7.10.4.tgz
Source66: https://registry.npmjs.org/@babel/plugin-transform-modules-amd/-/plugin-transform-modules-amd-7.10.5.tgz
Source67: https://registry.npmjs.org/@babel/plugin-transform-modules-amd/-/plugin-transform-modules-amd-7.9.0.tgz
Source68: https://registry.npmjs.org/@babel/plugin-transform-modules-commonjs/-/plugin-transform-modules-commonjs-7.10.4.tgz
Source69: https://registry.npmjs.org/@babel/plugin-transform-modules-commonjs/-/plugin-transform-modules-commonjs-7.9.0.tgz
Source70: https://registry.npmjs.org/@babel/plugin-transform-modules-systemjs/-/plugin-transform-modules-systemjs-7.10.5.tgz
Source71: https://registry.npmjs.org/@babel/plugin-transform-modules-systemjs/-/plugin-transform-modules-systemjs-7.9.0.tgz
Source72: https://registry.npmjs.org/@babel/plugin-transform-modules-umd/-/plugin-transform-modules-umd-7.10.4.tgz
Source73: https://registry.npmjs.org/@babel/plugin-transform-named-capturing-groups-regex/-/plugin-transform-named-capturing-groups-regex-7.10.4.tgz
Source74: https://registry.npmjs.org/@babel/plugin-transform-new-target/-/plugin-transform-new-target-7.10.4.tgz
Source75: https://registry.npmjs.org/@babel/plugin-transform-object-assign/-/plugin-transform-object-assign-7.10.4.tgz
Source76: https://registry.npmjs.org/@babel/plugin-transform-object-super/-/plugin-transform-object-super-7.10.4.tgz
Source77: https://registry.npmjs.org/@babel/plugin-transform-parameters/-/plugin-transform-parameters-7.10.5.tgz
Source78: https://registry.npmjs.org/@babel/plugin-transform-property-literals/-/plugin-transform-property-literals-7.10.4.tgz
Source79: https://registry.npmjs.org/@babel/plugin-transform-react-display-name/-/plugin-transform-react-display-name-7.10.4.tgz
Source80: https://registry.npmjs.org/@babel/plugin-transform-react-jsx/-/plugin-transform-react-jsx-7.10.4.tgz
Source81: https://registry.npmjs.org/@babel/plugin-transform-react-jsx-development/-/plugin-transform-react-jsx-development-7.10.4.tgz
Source82: https://registry.npmjs.org/@babel/plugin-transform-react-jsx-self/-/plugin-transform-react-jsx-self-7.10.4.tgz
Source83: https://registry.npmjs.org/@babel/plugin-transform-react-jsx-source/-/plugin-transform-react-jsx-source-7.10.5.tgz
Source84: https://registry.npmjs.org/@babel/plugin-transform-react-pure-annotations/-/plugin-transform-react-pure-annotations-7.10.4.tgz
Source85: https://registry.npmjs.org/@babel/plugin-transform-regenerator/-/plugin-transform-regenerator-7.10.4.tgz
Source86: https://registry.npmjs.org/@babel/plugin-transform-reserved-words/-/plugin-transform-reserved-words-7.10.4.tgz
Source87: https://registry.npmjs.org/@babel/plugin-transform-shorthand-properties/-/plugin-transform-shorthand-properties-7.10.4.tgz
Source88: https://registry.npmjs.org/@babel/plugin-transform-spread/-/plugin-transform-spread-7.11.0.tgz
Source89: https://registry.npmjs.org/@babel/plugin-transform-sticky-regex/-/plugin-transform-sticky-regex-7.10.4.tgz
Source90: https://registry.npmjs.org/@babel/plugin-transform-template-literals/-/plugin-transform-template-literals-7.10.5.tgz
Source91: https://registry.npmjs.org/@babel/plugin-transform-typeof-symbol/-/plugin-transform-typeof-symbol-7.10.4.tgz
Source92: https://registry.npmjs.org/@babel/plugin-transform-unicode-regex/-/plugin-transform-unicode-regex-7.10.4.tgz
Source93: https://registry.npmjs.org/@babel/preset-env/-/preset-env-7.9.5.tgz
Source94: https://registry.npmjs.org/@babel/preset-modules/-/preset-modules-0.1.3.tgz
Source95: https://registry.npmjs.org/@babel/preset-react/-/preset-react-7.10.4.tgz
Source96: https://registry.npmjs.org/@babel/runtime/-/runtime-7.11.2.tgz
Source97: https://registry.npmjs.org/@babel/template/-/template-7.10.4.tgz
Source98: https://registry.npmjs.org/@babel/traverse/-/traverse-7.11.0.tgz
Source99: https://registry.npmjs.org/@babel/types/-/types-7.11.0.tgz
Source100: https://registry.npmjs.org/@theforeman/builder/-/builder-4.14.0.tgz
Source101: https://registry.npmjs.org/ansi-styles/-/ansi-styles-3.2.1.tgz
Source102: https://registry.npmjs.org/babel-plugin-dynamic-import-node/-/babel-plugin-dynamic-import-node-2.3.0.tgz
Source103: https://registry.npmjs.org/babel-plugin-dynamic-import-node/-/babel-plugin-dynamic-import-node-2.3.3.tgz
Source104: https://registry.npmjs.org/browserslist/-/browserslist-4.14.0.tgz
Source105: https://registry.npmjs.org/caniuse-lite/-/caniuse-lite-1.0.30001115.tgz
Source106: https://registry.npmjs.org/chalk/-/chalk-2.4.2.tgz
Source107: https://registry.npmjs.org/color-convert/-/color-convert-1.9.3.tgz
Source108: https://registry.npmjs.org/color-name/-/color-name-1.1.3.tgz
Source109: https://registry.npmjs.org/convert-source-map/-/convert-source-map-1.7.0.tgz
Source110: https://registry.npmjs.org/core-js-compat/-/core-js-compat-3.6.5.tgz
Source111: https://registry.npmjs.org/debug/-/debug-4.2.0.tgz
Source112: https://registry.npmjs.org/define-properties/-/define-properties-1.1.3.tgz
Source113: https://registry.npmjs.org/electron-to-chromium/-/electron-to-chromium-1.3.534.tgz
Source114: https://registry.npmjs.org/escalade/-/escalade-3.0.2.tgz
Source115: https://registry.npmjs.org/escape-string-regexp/-/escape-string-regexp-1.0.5.tgz
Source116: https://registry.npmjs.org/esutils/-/esutils-2.0.3.tgz
Source117: https://registry.npmjs.org/function-bind/-/function-bind-1.1.1.tgz
Source118: https://registry.npmjs.org/gensync/-/gensync-1.0.0-beta.1.tgz
Source119: https://registry.npmjs.org/globals/-/globals-11.12.0.tgz
Source120: https://registry.npmjs.org/has-flag/-/has-flag-3.0.0.tgz
Source121: https://registry.npmjs.org/has-symbols/-/has-symbols-1.0.1.tgz
Source122: https://registry.npmjs.org/invariant/-/invariant-2.2.4.tgz
Source123: https://registry.npmjs.org/js-tokens/-/js-tokens-4.0.0.tgz
Source124: https://registry.npmjs.org/jsesc/-/jsesc-0.5.0.tgz
Source125: https://registry.npmjs.org/jsesc/-/jsesc-2.5.2.tgz
Source126: https://registry.npmjs.org/json5/-/json5-2.1.3.tgz
Source127: https://registry.npmjs.org/leven/-/leven-3.1.0.tgz
Source128: https://registry.npmjs.org/levenary/-/levenary-1.1.1.tgz
Source129: https://registry.npmjs.org/lodash/-/lodash-4.17.20.tgz
Source130: https://registry.npmjs.org/loose-envify/-/loose-envify-1.4.0.tgz
Source131: https://registry.npmjs.org/minimist/-/minimist-1.2.5.tgz
Source132: https://registry.npmjs.org/ms/-/ms-2.1.2.tgz
Source133: https://registry.npmjs.org/node-releases/-/node-releases-1.1.60.tgz
Source134: https://registry.npmjs.org/object-keys/-/object-keys-1.1.1.tgz
Source135: https://registry.npmjs.org/object.assign/-/object.assign-4.1.0.tgz
Source136: https://registry.npmjs.org/path-parse/-/path-parse-1.0.6.tgz
Source137: https://registry.npmjs.org/regenerate/-/regenerate-1.4.1.tgz
Source138: https://registry.npmjs.org/regenerate-unicode-properties/-/regenerate-unicode-properties-8.2.0.tgz
Source139: https://registry.npmjs.org/regenerator-runtime/-/regenerator-runtime-0.13.7.tgz
Source140: https://registry.npmjs.org/regenerator-transform/-/regenerator-transform-0.14.5.tgz
Source141: https://registry.npmjs.org/regexpu-core/-/regexpu-core-4.7.0.tgz
Source142: https://registry.npmjs.org/regjsgen/-/regjsgen-0.5.2.tgz
Source143: https://registry.npmjs.org/regjsparser/-/regjsparser-0.6.4.tgz
Source144: https://registry.npmjs.org/resolve/-/resolve-1.17.0.tgz
Source145: https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.1.2.tgz
Source146: https://registry.npmjs.org/semver/-/semver-5.7.1.tgz
Source147: https://registry.npmjs.org/semver/-/semver-7.0.0.tgz
Source148: https://registry.npmjs.org/source-map/-/source-map-0.5.7.tgz
Source149: https://registry.npmjs.org/supports-color/-/supports-color-5.5.0.tgz
Source150: https://registry.npmjs.org/to-fast-properties/-/to-fast-properties-2.0.0.tgz
Source151: https://registry.npmjs.org/unicode-canonical-property-names-ecmascript/-/unicode-canonical-property-names-ecmascript-1.0.4.tgz
Source152: https://registry.npmjs.org/unicode-match-property-ecmascript/-/unicode-match-property-ecmascript-1.0.4.tgz
Source153: https://registry.npmjs.org/unicode-match-property-value-ecmascript/-/unicode-match-property-value-ecmascript-1.2.0.tgz
Source154: https://registry.npmjs.org/unicode-property-aliases-ecmascript/-/unicode-property-aliases-ecmascript-1.1.0.tgz
Source155: nodejs-theforeman-builder-%{version}-registry.npmjs.org.tgz
BuildRequires: %{?scl_prefix_nodejs}npm
%if 0%{!?scl:1}
BuildRequires: nodejs-packaging
%endif
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}
Provides: bundled(npm(@babel/code-frame)) = 7.10.4
Provides: bundled(npm(@babel/compat-data)) = 7.11.0
Provides: bundled(npm(@babel/core)) = 7.11.1
Provides: bundled(npm(@babel/generator)) = 7.11.0
Provides: bundled(npm(@babel/helper-annotate-as-pure)) = 7.10.4
Provides: bundled(npm(@babel/helper-builder-binary-assignment-operator-visitor)) = 7.10.4
Provides: bundled(npm(@babel/helper-builder-react-jsx)) = 7.10.4
Provides: bundled(npm(@babel/helper-builder-react-jsx-experimental)) = 7.10.5
Provides: bundled(npm(@babel/helper-compilation-targets)) = 7.10.4
Provides: bundled(npm(@babel/helper-create-class-features-plugin)) = 7.10.5
Provides: bundled(npm(@babel/helper-create-regexp-features-plugin)) = 7.10.4
Provides: bundled(npm(@babel/helper-define-map)) = 7.10.5
Provides: bundled(npm(@babel/helper-explode-assignable-expression)) = 7.10.4
Provides: bundled(npm(@babel/helper-function-name)) = 7.10.4
Provides: bundled(npm(@babel/helper-get-function-arity)) = 7.10.4
Provides: bundled(npm(@babel/helper-hoist-variables)) = 7.10.4
Provides: bundled(npm(@babel/helper-member-expression-to-functions)) = 7.11.0
Provides: bundled(npm(@babel/helper-module-imports)) = 7.10.4
Provides: bundled(npm(@babel/helper-module-transforms)) = 7.11.0
Provides: bundled(npm(@babel/helper-optimise-call-expression)) = 7.10.4
Provides: bundled(npm(@babel/helper-plugin-utils)) = 7.10.4
Provides: bundled(npm(@babel/helper-regex)) = 7.10.5
Provides: bundled(npm(@babel/helper-remap-async-to-generator)) = 7.10.4
Provides: bundled(npm(@babel/helper-replace-supers)) = 7.10.4
Provides: bundled(npm(@babel/helper-simple-access)) = 7.10.4
Provides: bundled(npm(@babel/helper-skip-transparent-expression-wrappers)) = 7.11.0
Provides: bundled(npm(@babel/helper-split-export-declaration)) = 7.11.0
Provides: bundled(npm(@babel/helper-validator-identifier)) = 7.10.4
Provides: bundled(npm(@babel/helper-wrap-function)) = 7.10.4
Provides: bundled(npm(@babel/helpers)) = 7.10.4
Provides: bundled(npm(@babel/highlight)) = 7.10.4
Provides: bundled(npm(@babel/parser)) = 7.11.3
Provides: bundled(npm(@babel/plugin-proposal-async-generator-functions)) = 7.10.5
Provides: bundled(npm(@babel/plugin-proposal-class-properties)) = 7.10.4
Provides: bundled(npm(@babel/plugin-proposal-dynamic-import)) = 7.10.4
Provides: bundled(npm(@babel/plugin-proposal-json-strings)) = 7.10.4
Provides: bundled(npm(@babel/plugin-proposal-nullish-coalescing-operator)) = 7.10.4
Provides: bundled(npm(@babel/plugin-proposal-numeric-separator)) = 7.10.4
Provides: bundled(npm(@babel/plugin-proposal-object-rest-spread)) = 7.11.0
Provides: bundled(npm(@babel/plugin-proposal-optional-catch-binding)) = 7.10.4
Provides: bundled(npm(@babel/plugin-proposal-optional-chaining)) = 7.11.0
Provides: bundled(npm(@babel/plugin-proposal-unicode-property-regex)) = 7.10.4
Provides: bundled(npm(@babel/plugin-syntax-async-generators)) = 7.8.4
Provides: bundled(npm(@babel/plugin-syntax-dynamic-import)) = 7.8.3
Provides: bundled(npm(@babel/plugin-syntax-json-strings)) = 7.8.3
Provides: bundled(npm(@babel/plugin-syntax-jsx)) = 7.10.4
Provides: bundled(npm(@babel/plugin-syntax-nullish-coalescing-operator)) = 7.8.3
Provides: bundled(npm(@babel/plugin-syntax-numeric-separator)) = 7.10.4
Provides: bundled(npm(@babel/plugin-syntax-object-rest-spread)) = 7.8.3
Provides: bundled(npm(@babel/plugin-syntax-optional-catch-binding)) = 7.8.3
Provides: bundled(npm(@babel/plugin-syntax-optional-chaining)) = 7.8.3
Provides: bundled(npm(@babel/plugin-syntax-top-level-await)) = 7.10.4
Provides: bundled(npm(@babel/plugin-transform-arrow-functions)) = 7.10.4
Provides: bundled(npm(@babel/plugin-transform-async-to-generator)) = 7.10.4
Provides: bundled(npm(@babel/plugin-transform-block-scoped-functions)) = 7.10.4
Provides: bundled(npm(@babel/plugin-transform-block-scoping)) = 7.11.1
Provides: bundled(npm(@babel/plugin-transform-classes)) = 7.10.4
Provides: bundled(npm(@babel/plugin-transform-computed-properties)) = 7.10.4
Provides: bundled(npm(@babel/plugin-transform-destructuring)) = 7.10.4
Provides: bundled(npm(@babel/plugin-transform-dotall-regex)) = 7.10.4
Provides: bundled(npm(@babel/plugin-transform-duplicate-keys)) = 7.10.4
Provides: bundled(npm(@babel/plugin-transform-exponentiation-operator)) = 7.10.4
Provides: bundled(npm(@babel/plugin-transform-for-of)) = 7.10.4
Provides: bundled(npm(@babel/plugin-transform-function-name)) = 7.10.4
Provides: bundled(npm(@babel/plugin-transform-literals)) = 7.10.4
Provides: bundled(npm(@babel/plugin-transform-member-expression-literals)) = 7.10.4
Provides: bundled(npm(@babel/plugin-transform-modules-amd)) = 7.10.5
Provides: bundled(npm(@babel/plugin-transform-modules-amd)) = 7.9.0
Provides: bundled(npm(@babel/plugin-transform-modules-commonjs)) = 7.10.4
Provides: bundled(npm(@babel/plugin-transform-modules-commonjs)) = 7.9.0
Provides: bundled(npm(@babel/plugin-transform-modules-systemjs)) = 7.10.5
Provides: bundled(npm(@babel/plugin-transform-modules-systemjs)) = 7.9.0
Provides: bundled(npm(@babel/plugin-transform-modules-umd)) = 7.10.4
Provides: bundled(npm(@babel/plugin-transform-named-capturing-groups-regex)) = 7.10.4
Provides: bundled(npm(@babel/plugin-transform-new-target)) = 7.10.4
Provides: bundled(npm(@babel/plugin-transform-object-assign)) = 7.10.4
Provides: bundled(npm(@babel/plugin-transform-object-super)) = 7.10.4
Provides: bundled(npm(@babel/plugin-transform-parameters)) = 7.10.5
Provides: bundled(npm(@babel/plugin-transform-property-literals)) = 7.10.4
Provides: bundled(npm(@babel/plugin-transform-react-display-name)) = 7.10.4
Provides: bundled(npm(@babel/plugin-transform-react-jsx)) = 7.10.4
Provides: bundled(npm(@babel/plugin-transform-react-jsx-development)) = 7.10.4
Provides: bundled(npm(@babel/plugin-transform-react-jsx-self)) = 7.10.4
Provides: bundled(npm(@babel/plugin-transform-react-jsx-source)) = 7.10.5
Provides: bundled(npm(@babel/plugin-transform-react-pure-annotations)) = 7.10.4
Provides: bundled(npm(@babel/plugin-transform-regenerator)) = 7.10.4
Provides: bundled(npm(@babel/plugin-transform-reserved-words)) = 7.10.4
Provides: bundled(npm(@babel/plugin-transform-shorthand-properties)) = 7.10.4
Provides: bundled(npm(@babel/plugin-transform-spread)) = 7.11.0
Provides: bundled(npm(@babel/plugin-transform-sticky-regex)) = 7.10.4
Provides: bundled(npm(@babel/plugin-transform-template-literals)) = 7.10.5
Provides: bundled(npm(@babel/plugin-transform-typeof-symbol)) = 7.10.4
Provides: bundled(npm(@babel/plugin-transform-unicode-regex)) = 7.10.4
Provides: bundled(npm(@babel/preset-env)) = 7.9.5
Provides: bundled(npm(@babel/preset-modules)) = 0.1.3
Provides: bundled(npm(@babel/preset-react)) = 7.10.4
Provides: bundled(npm(@babel/runtime)) = 7.11.2
Provides: bundled(npm(@babel/template)) = 7.10.4
Provides: bundled(npm(@babel/traverse)) = 7.11.0
Provides: bundled(npm(@babel/types)) = 7.11.0
Provides: bundled(npm(@theforeman/builder)) = 4.14.0
Provides: bundled(npm(ansi-styles)) = 3.2.1
Provides: bundled(npm(babel-plugin-dynamic-import-node)) = 2.3.0
Provides: bundled(npm(babel-plugin-dynamic-import-node)) = 2.3.3
Provides: bundled(npm(browserslist)) = 4.14.0
Provides: bundled(npm(caniuse-lite)) = 1.0.30001115
Provides: bundled(npm(chalk)) = 2.4.2
Provides: bundled(npm(color-convert)) = 1.9.3
Provides: bundled(npm(color-name)) = 1.1.3
Provides: bundled(npm(convert-source-map)) = 1.7.0
Provides: bundled(npm(core-js-compat)) = 3.6.5
Provides: bundled(npm(debug)) = 4.2.0
Provides: bundled(npm(define-properties)) = 1.1.3
Provides: bundled(npm(electron-to-chromium)) = 1.3.534
Provides: bundled(npm(escalade)) = 3.0.2
Provides: bundled(npm(escape-string-regexp)) = 1.0.5
Provides: bundled(npm(esutils)) = 2.0.3
Provides: bundled(npm(function-bind)) = 1.1.1
Provides: bundled(npm(gensync)) = 1.0.0-beta.1
Provides: bundled(npm(globals)) = 11.12.0
Provides: bundled(npm(has-flag)) = 3.0.0
Provides: bundled(npm(has-symbols)) = 1.0.1
Provides: bundled(npm(invariant)) = 2.2.4
Provides: bundled(npm(js-tokens)) = 4.0.0
Provides: bundled(npm(jsesc)) = 0.5.0
Provides: bundled(npm(jsesc)) = 2.5.2
Provides: bundled(npm(json5)) = 2.1.3
Provides: bundled(npm(leven)) = 3.1.0
Provides: bundled(npm(levenary)) = 1.1.1
Provides: bundled(npm(lodash)) = 4.17.20
Provides: bundled(npm(loose-envify)) = 1.4.0
Provides: bundled(npm(minimist)) = 1.2.5
Provides: bundled(npm(ms)) = 2.1.2
Provides: bundled(npm(node-releases)) = 1.1.60
Provides: bundled(npm(object-keys)) = 1.1.1
Provides: bundled(npm(object.assign)) = 4.1.0
Provides: bundled(npm(path-parse)) = 1.0.6
Provides: bundled(npm(regenerate)) = 1.4.1
Provides: bundled(npm(regenerate-unicode-properties)) = 8.2.0
Provides: bundled(npm(regenerator-runtime)) = 0.13.7
Provides: bundled(npm(regenerator-transform)) = 0.14.5
Provides: bundled(npm(regexpu-core)) = 4.7.0
Provides: bundled(npm(regjsgen)) = 0.5.2
Provides: bundled(npm(regjsparser)) = 0.6.4
Provides: bundled(npm(resolve)) = 1.17.0
Provides: bundled(npm(safe-buffer)) = 5.1.2
Provides: bundled(npm(semver)) = 5.7.1
Provides: bundled(npm(semver)) = 7.0.0
Provides: bundled(npm(source-map)) = 0.5.7
Provides: bundled(npm(supports-color)) = 5.5.0
Provides: bundled(npm(to-fast-properties)) = 2.0.0
Provides: bundled(npm(unicode-canonical-property-names-ecmascript)) = 1.0.4
Provides: bundled(npm(unicode-match-property-ecmascript)) = 1.0.4
Provides: bundled(npm(unicode-match-property-value-ecmascript)) = 1.2.0
Provides: bundled(npm(unicode-property-aliases-ecmascript)) = 1.1.0
AutoReq: no
AutoProv: no

%if 0%{?scl:1}
%define npm_cache_dir npm_cache
%else
%define npm_cache_dir /tmp/npm_cache_%{name}-%{version}-%{release}
%endif

%description
%{summary}

%prep
mkdir -p %{npm_cache_dir}
%{?scl:scl enable %{?scl_nodejs} - << \end_of_scl}
for tgz in %{sources}; do
  echo $tgz | grep -q registry.npmjs.org || npm cache add --cache %{npm_cache_dir} $tgz
done
%{?scl:end_of_scl}

%setup -T -q -a 155 -D -n %{npm_cache_dir}

%build
%{?scl:scl enable %{?scl_nodejs} - << \end_of_scl}
npm install --cache-min Infinity --cache %{?scl:../}%{npm_cache_dir} --no-shrinkwrap --no-optional --global-style true %{npm_name}@%{version}
%{?scl:end_of_scl}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/babel %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/bin %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

mkdir -p %{buildroot}%{_bindir}/
chmod 0755 %{buildroot}%{nodejs_sitelib}/%{npm_name}/bin/tfm-builder-install.js
ln -sf %{nodejs_sitelib}/%{npm_name}/bin/tfm-builder-install.js %{buildroot}%{_bindir}/tfm-builder-install
chmod 0755 %{buildroot}%{nodejs_sitelib}/%{npm_name}/bin/tfm-build.js
ln -sf %{nodejs_sitelib}/%{npm_name}/bin/tfm-build.js %{buildroot}%{_bindir}/tfm-build
chmod 0755 %{buildroot}%{nodejs_sitelib}/%{npm_name}/bin/tfm-dev-server.js
ln -sf %{nodejs_sitelib}/%{npm_name}/bin/tfm-dev-server.js %{buildroot}%{_bindir}/tfm-dev-server
chmod 0755 %{buildroot}%{nodejs_sitelib}/%{npm_name}/bin/tfm-builder-analyze.js
ln -sf %{nodejs_sitelib}/%{npm_name}/bin/tfm-builder-analyze.js %{buildroot}%{_bindir}/tfm-builder-analyze

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%{_bindir}/tfm-builder-install
%{_bindir}/tfm-build
%{_bindir}/tfm-dev-server
%{_bindir}/tfm-builder-analyze
%license node_modules/%{npm_name}/license
%doc node_modules/%{npm_name}/CHANGELOG.md
%doc node_modules/%{npm_name}/README.md

%changelog
* Tue Aug 18 2020 Avi Sharvit <sharvita@gmail.com> 4.14.0-1
- Update to 4.14.0

* Tue Jul 28 2020 MariaAga <mariaagaphonchev@gmail.com> 4.12.0-1
- Update to 4.12.0

* Thu Jul 09 2020 Avi Sharvit <sharvita@gmail.com> 4.11.1-1
- Update to 4.11.1

* Sun Jun 21 2020 Avi Sharvit <sharvita@gmail.com> 4.8.0-1
- Update to 4.8.0

* Tue Apr 07 2020 Zach Huntington-Meath <zhunting@redhat.com> - 4.3.0-2
- Bump packages to build for el8

* Fri Apr 03 2020 Evgeni Golov 4.3.0-1
- Update to 4.3.0

* Mon Jan 27 2020 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 4.0.7-1
- Update to 4.0.7

* Tue Jan 07 2020 Avi Sharvit <sharvita@gmail.com> 4.0.2-1
- Update to 4.0.2

* Tue Dec 17 2019 Evgeni Golov 3.9.0-1
- Update to 3.9.0

* Tue Dec 17 2019 Evgeni Golov 3.8.1-1
- Update to 3.8.1

* Sat Dec 07 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 3.5.2-1
- Update to 3.5.2

* Mon Dec 02 2019 Evgeni Golov 3.3.2-1
- Update to 3.3.2

* Mon Dec 02 2019 Evgeni Golov 3.3.1-1
- Update to 3.3.1

* Wed Nov 27 2019 Evgeni Golov 3.3.0-1
- Add nodejs-theforeman-builder generated by npm2rpm using the bundle strategy

