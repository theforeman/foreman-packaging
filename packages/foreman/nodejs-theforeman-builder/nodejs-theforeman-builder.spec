%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name @theforeman/builder

Name: %{?scl_prefix}nodejs-theforeman-builder
Version: 15.0.0
Release: 1%{?dist}
Summary: Build production and development bundle files for foreman core and plugins
License: MIT
Group: Development/Libraries
URL: https://github.com/theforeman/foreman-js#readme
Source0: https://registry.npmjs.org/@ampproject/remapping/-/remapping-2.3.0.tgz
Source1: https://registry.npmjs.org/@babel/code-frame/-/code-frame-7.26.2.tgz
Source2: https://registry.npmjs.org/@babel/compat-data/-/compat-data-7.26.8.tgz
Source3: https://registry.npmjs.org/@babel/core/-/core-7.17.10.tgz
Source4: https://registry.npmjs.org/@babel/generator/-/generator-7.26.9.tgz
Source5: https://registry.npmjs.org/@babel/helper-annotate-as-pure/-/helper-annotate-as-pure-7.25.9.tgz
Source6: https://registry.npmjs.org/@babel/helper-compilation-targets/-/helper-compilation-targets-7.26.5.tgz
Source7: https://registry.npmjs.org/@babel/helper-create-class-features-plugin/-/helper-create-class-features-plugin-7.26.9.tgz
Source8: https://registry.npmjs.org/@babel/helper-create-regexp-features-plugin/-/helper-create-regexp-features-plugin-7.26.3.tgz
Source9: https://registry.npmjs.org/@babel/helper-environment-visitor/-/helper-environment-visitor-7.24.7.tgz
Source10: https://registry.npmjs.org/@babel/helper-hoist-variables/-/helper-hoist-variables-7.24.7.tgz
Source11: https://registry.npmjs.org/@babel/helper-member-expression-to-functions/-/helper-member-expression-to-functions-7.25.9.tgz
Source12: https://registry.npmjs.org/@babel/helper-module-imports/-/helper-module-imports-7.25.9.tgz
Source13: https://registry.npmjs.org/@babel/helper-module-transforms/-/helper-module-transforms-7.26.0.tgz
Source14: https://registry.npmjs.org/@babel/helper-optimise-call-expression/-/helper-optimise-call-expression-7.25.9.tgz
Source15: https://registry.npmjs.org/@babel/helper-plugin-utils/-/helper-plugin-utils-7.26.5.tgz
Source16: https://registry.npmjs.org/@babel/helper-remap-async-to-generator/-/helper-remap-async-to-generator-7.25.9.tgz
Source17: https://registry.npmjs.org/@babel/helper-replace-supers/-/helper-replace-supers-7.26.5.tgz
Source18: https://registry.npmjs.org/@babel/helper-simple-access/-/helper-simple-access-7.25.9.tgz
Source19: https://registry.npmjs.org/@babel/helper-skip-transparent-expression-wrappers/-/helper-skip-transparent-expression-wrappers-7.25.9.tgz
Source20: https://registry.npmjs.org/@babel/helper-string-parser/-/helper-string-parser-7.25.9.tgz
Source21: https://registry.npmjs.org/@babel/helper-validator-identifier/-/helper-validator-identifier-7.25.9.tgz
Source22: https://registry.npmjs.org/@babel/helper-validator-option/-/helper-validator-option-7.25.9.tgz
Source23: https://registry.npmjs.org/@babel/helper-wrap-function/-/helper-wrap-function-7.25.9.tgz
Source24: https://registry.npmjs.org/@babel/helpers/-/helpers-7.26.9.tgz
Source25: https://registry.npmjs.org/@babel/parser/-/parser-7.26.9.tgz
Source26: https://registry.npmjs.org/@babel/plugin-proposal-async-generator-functions/-/plugin-proposal-async-generator-functions-7.20.7.tgz
Source27: https://registry.npmjs.org/@babel/plugin-proposal-class-properties/-/plugin-proposal-class-properties-7.16.7.tgz
Source28: https://registry.npmjs.org/@babel/plugin-proposal-dynamic-import/-/plugin-proposal-dynamic-import-7.18.6.tgz
Source29: https://registry.npmjs.org/@babel/plugin-proposal-json-strings/-/plugin-proposal-json-strings-7.18.6.tgz
Source30: https://registry.npmjs.org/@babel/plugin-proposal-nullish-coalescing-operator/-/plugin-proposal-nullish-coalescing-operator-7.18.6.tgz
Source31: https://registry.npmjs.org/@babel/plugin-proposal-numeric-separator/-/plugin-proposal-numeric-separator-7.18.6.tgz
Source32: https://registry.npmjs.org/@babel/plugin-proposal-object-rest-spread/-/plugin-proposal-object-rest-spread-7.16.7.tgz
Source33: https://registry.npmjs.org/@babel/plugin-proposal-object-rest-spread/-/plugin-proposal-object-rest-spread-7.20.7.tgz
Source34: https://registry.npmjs.org/@babel/plugin-proposal-optional-catch-binding/-/plugin-proposal-optional-catch-binding-7.18.6.tgz
Source35: https://registry.npmjs.org/@babel/plugin-proposal-optional-chaining/-/plugin-proposal-optional-chaining-7.21.0.tgz
Source36: https://registry.npmjs.org/@babel/plugin-proposal-unicode-property-regex/-/plugin-proposal-unicode-property-regex-7.18.6.tgz
Source37: https://registry.npmjs.org/@babel/plugin-syntax-async-generators/-/plugin-syntax-async-generators-7.8.4.tgz
Source38: https://registry.npmjs.org/@babel/plugin-syntax-dynamic-import/-/plugin-syntax-dynamic-import-7.8.3.tgz
Source39: https://registry.npmjs.org/@babel/plugin-syntax-json-strings/-/plugin-syntax-json-strings-7.8.3.tgz
Source40: https://registry.npmjs.org/@babel/plugin-syntax-jsx/-/plugin-syntax-jsx-7.25.9.tgz
Source41: https://registry.npmjs.org/@babel/plugin-syntax-nullish-coalescing-operator/-/plugin-syntax-nullish-coalescing-operator-7.8.3.tgz
Source42: https://registry.npmjs.org/@babel/plugin-syntax-numeric-separator/-/plugin-syntax-numeric-separator-7.10.4.tgz
Source43: https://registry.npmjs.org/@babel/plugin-syntax-object-rest-spread/-/plugin-syntax-object-rest-spread-7.8.3.tgz
Source44: https://registry.npmjs.org/@babel/plugin-syntax-optional-catch-binding/-/plugin-syntax-optional-catch-binding-7.8.3.tgz
Source45: https://registry.npmjs.org/@babel/plugin-syntax-optional-chaining/-/plugin-syntax-optional-chaining-7.8.3.tgz
Source46: https://registry.npmjs.org/@babel/plugin-syntax-top-level-await/-/plugin-syntax-top-level-await-7.14.5.tgz
Source47: https://registry.npmjs.org/@babel/plugin-transform-arrow-functions/-/plugin-transform-arrow-functions-7.25.9.tgz
Source48: https://registry.npmjs.org/@babel/plugin-transform-async-to-generator/-/plugin-transform-async-to-generator-7.25.9.tgz
Source49: https://registry.npmjs.org/@babel/plugin-transform-block-scoped-functions/-/plugin-transform-block-scoped-functions-7.26.5.tgz
Source50: https://registry.npmjs.org/@babel/plugin-transform-block-scoping/-/plugin-transform-block-scoping-7.25.9.tgz
Source51: https://registry.npmjs.org/@babel/plugin-transform-classes/-/plugin-transform-classes-7.25.9.tgz
Source52: https://registry.npmjs.org/@babel/plugin-transform-computed-properties/-/plugin-transform-computed-properties-7.25.9.tgz
Source53: https://registry.npmjs.org/@babel/plugin-transform-destructuring/-/plugin-transform-destructuring-7.25.9.tgz
Source54: https://registry.npmjs.org/@babel/plugin-transform-dotall-regex/-/plugin-transform-dotall-regex-7.25.9.tgz
Source55: https://registry.npmjs.org/@babel/plugin-transform-duplicate-keys/-/plugin-transform-duplicate-keys-7.25.9.tgz
Source56: https://registry.npmjs.org/@babel/plugin-transform-exponentiation-operator/-/plugin-transform-exponentiation-operator-7.26.3.tgz
Source57: https://registry.npmjs.org/@babel/plugin-transform-for-of/-/plugin-transform-for-of-7.26.9.tgz
Source58: https://registry.npmjs.org/@babel/plugin-transform-function-name/-/plugin-transform-function-name-7.25.9.tgz
Source59: https://registry.npmjs.org/@babel/plugin-transform-literals/-/plugin-transform-literals-7.25.9.tgz
Source60: https://registry.npmjs.org/@babel/plugin-transform-member-expression-literals/-/plugin-transform-member-expression-literals-7.25.9.tgz
Source61: https://registry.npmjs.org/@babel/plugin-transform-modules-amd/-/plugin-transform-modules-amd-7.25.9.tgz
Source62: https://registry.npmjs.org/@babel/plugin-transform-modules-amd/-/plugin-transform-modules-amd-7.9.0.tgz
Source63: https://registry.npmjs.org/@babel/plugin-transform-modules-commonjs/-/plugin-transform-modules-commonjs-7.26.3.tgz
Source64: https://registry.npmjs.org/@babel/plugin-transform-modules-commonjs/-/plugin-transform-modules-commonjs-7.9.0.tgz
Source65: https://registry.npmjs.org/@babel/plugin-transform-modules-systemjs/-/plugin-transform-modules-systemjs-7.25.9.tgz
Source66: https://registry.npmjs.org/@babel/plugin-transform-modules-systemjs/-/plugin-transform-modules-systemjs-7.9.0.tgz
Source67: https://registry.npmjs.org/@babel/plugin-transform-modules-umd/-/plugin-transform-modules-umd-7.25.9.tgz
Source68: https://registry.npmjs.org/@babel/plugin-transform-named-capturing-groups-regex/-/plugin-transform-named-capturing-groups-regex-7.25.9.tgz
Source69: https://registry.npmjs.org/@babel/plugin-transform-new-target/-/plugin-transform-new-target-7.25.9.tgz
Source70: https://registry.npmjs.org/@babel/plugin-transform-object-assign/-/plugin-transform-object-assign-7.25.9.tgz
Source71: https://registry.npmjs.org/@babel/plugin-transform-object-super/-/plugin-transform-object-super-7.25.9.tgz
Source72: https://registry.npmjs.org/@babel/plugin-transform-parameters/-/plugin-transform-parameters-7.25.9.tgz
Source73: https://registry.npmjs.org/@babel/plugin-transform-property-literals/-/plugin-transform-property-literals-7.25.9.tgz
Source74: https://registry.npmjs.org/@babel/plugin-transform-react-display-name/-/plugin-transform-react-display-name-7.25.9.tgz
Source75: https://registry.npmjs.org/@babel/plugin-transform-react-jsx/-/plugin-transform-react-jsx-7.25.9.tgz
Source76: https://registry.npmjs.org/@babel/plugin-transform-react-jsx-development/-/plugin-transform-react-jsx-development-7.25.9.tgz
Source77: https://registry.npmjs.org/@babel/plugin-transform-react-pure-annotations/-/plugin-transform-react-pure-annotations-7.25.9.tgz
Source78: https://registry.npmjs.org/@babel/plugin-transform-regenerator/-/plugin-transform-regenerator-7.25.9.tgz
Source79: https://registry.npmjs.org/@babel/plugin-transform-reserved-words/-/plugin-transform-reserved-words-7.25.9.tgz
Source80: https://registry.npmjs.org/@babel/plugin-transform-shorthand-properties/-/plugin-transform-shorthand-properties-7.25.9.tgz
Source81: https://registry.npmjs.org/@babel/plugin-transform-spread/-/plugin-transform-spread-7.25.9.tgz
Source82: https://registry.npmjs.org/@babel/plugin-transform-sticky-regex/-/plugin-transform-sticky-regex-7.25.9.tgz
Source83: https://registry.npmjs.org/@babel/plugin-transform-template-literals/-/plugin-transform-template-literals-7.26.8.tgz
Source84: https://registry.npmjs.org/@babel/plugin-transform-typeof-symbol/-/plugin-transform-typeof-symbol-7.26.7.tgz
Source85: https://registry.npmjs.org/@babel/plugin-transform-unicode-regex/-/plugin-transform-unicode-regex-7.25.9.tgz
Source86: https://registry.npmjs.org/@babel/preset-env/-/preset-env-7.9.5.tgz
Source87: https://registry.npmjs.org/@babel/preset-modules/-/preset-modules-0.1.6.tgz
Source88: https://registry.npmjs.org/@babel/preset-react/-/preset-react-7.16.7.tgz
Source89: https://registry.npmjs.org/@babel/runtime/-/runtime-7.26.9.tgz
Source90: https://registry.npmjs.org/@babel/template/-/template-7.26.9.tgz
Source91: https://registry.npmjs.org/@babel/traverse/-/traverse-7.26.9.tgz
Source92: https://registry.npmjs.org/@babel/types/-/types-7.26.9.tgz
Source93: https://registry.npmjs.org/@jridgewell/gen-mapping/-/gen-mapping-0.3.8.tgz
Source94: https://registry.npmjs.org/@jridgewell/resolve-uri/-/resolve-uri-3.1.2.tgz
Source95: https://registry.npmjs.org/@jridgewell/set-array/-/set-array-1.2.1.tgz
Source96: https://registry.npmjs.org/@jridgewell/sourcemap-codec/-/sourcemap-codec-1.5.0.tgz
Source97: https://registry.npmjs.org/@jridgewell/trace-mapping/-/trace-mapping-0.3.25.tgz
Source98: https://registry.npmjs.org/@theforeman/builder/-/builder-15.0.0.tgz
Source99: https://registry.npmjs.org/babel-plugin-dynamic-import-node/-/babel-plugin-dynamic-import-node-2.3.0.tgz
Source100: https://registry.npmjs.org/babel-plugin-dynamic-import-node/-/babel-plugin-dynamic-import-node-2.3.3.tgz
Source101: https://registry.npmjs.org/browserslist/-/browserslist-4.24.4.tgz
Source102: https://registry.npmjs.org/call-bind/-/call-bind-1.0.8.tgz
Source103: https://registry.npmjs.org/call-bind-apply-helpers/-/call-bind-apply-helpers-1.0.2.tgz
Source104: https://registry.npmjs.org/call-bound/-/call-bound-1.0.4.tgz
Source105: https://registry.npmjs.org/caniuse-lite/-/caniuse-lite-1.0.30001702.tgz
Source106: https://registry.npmjs.org/convert-source-map/-/convert-source-map-1.9.0.tgz
Source107: https://registry.npmjs.org/core-js-compat/-/core-js-compat-3.41.0.tgz
Source108: https://registry.npmjs.org/debug/-/debug-4.4.0.tgz
Source109: https://registry.npmjs.org/define-data-property/-/define-data-property-1.1.4.tgz
Source110: https://registry.npmjs.org/define-properties/-/define-properties-1.2.1.tgz
Source111: https://registry.npmjs.org/dunder-proto/-/dunder-proto-1.0.1.tgz
Source112: https://registry.npmjs.org/electron-to-chromium/-/electron-to-chromium-1.5.112.tgz
Source113: https://registry.npmjs.org/es-define-property/-/es-define-property-1.0.1.tgz
Source114: https://registry.npmjs.org/es-errors/-/es-errors-1.3.0.tgz
Source115: https://registry.npmjs.org/es-object-atoms/-/es-object-atoms-1.1.1.tgz
Source116: https://registry.npmjs.org/escalade/-/escalade-3.2.0.tgz
Source117: https://registry.npmjs.org/esutils/-/esutils-2.0.3.tgz
Source118: https://registry.npmjs.org/function-bind/-/function-bind-1.1.2.tgz
Source119: https://registry.npmjs.org/gensync/-/gensync-1.0.0-beta.2.tgz
Source120: https://registry.npmjs.org/get-intrinsic/-/get-intrinsic-1.3.0.tgz
Source121: https://registry.npmjs.org/get-proto/-/get-proto-1.0.1.tgz
Source122: https://registry.npmjs.org/globals/-/globals-11.12.0.tgz
Source123: https://registry.npmjs.org/gopd/-/gopd-1.2.0.tgz
Source124: https://registry.npmjs.org/has-property-descriptors/-/has-property-descriptors-1.0.2.tgz
Source125: https://registry.npmjs.org/has-symbols/-/has-symbols-1.1.0.tgz
Source126: https://registry.npmjs.org/hasown/-/hasown-2.0.2.tgz
Source127: https://registry.npmjs.org/invariant/-/invariant-2.2.4.tgz
Source128: https://registry.npmjs.org/js-tokens/-/js-tokens-4.0.0.tgz
Source129: https://registry.npmjs.org/jsesc/-/jsesc-3.0.2.tgz
Source130: https://registry.npmjs.org/jsesc/-/jsesc-3.1.0.tgz
Source131: https://registry.npmjs.org/json5/-/json5-2.2.3.tgz
Source132: https://registry.npmjs.org/leven/-/leven-3.1.0.tgz
Source133: https://registry.npmjs.org/levenary/-/levenary-1.1.1.tgz
Source134: https://registry.npmjs.org/loose-envify/-/loose-envify-1.4.0.tgz
Source135: https://registry.npmjs.org/lru-cache/-/lru-cache-5.1.1.tgz
Source136: https://registry.npmjs.org/math-intrinsics/-/math-intrinsics-1.1.0.tgz
Source137: https://registry.npmjs.org/ms/-/ms-2.1.3.tgz
Source138: https://registry.npmjs.org/node-releases/-/node-releases-2.0.19.tgz
Source139: https://registry.npmjs.org/object-keys/-/object-keys-1.1.1.tgz
Source140: https://registry.npmjs.org/object.assign/-/object.assign-4.1.7.tgz
Source141: https://registry.npmjs.org/picocolors/-/picocolors-1.1.1.tgz
Source142: https://registry.npmjs.org/regenerate/-/regenerate-1.4.2.tgz
Source143: https://registry.npmjs.org/regenerate-unicode-properties/-/regenerate-unicode-properties-10.2.0.tgz
Source144: https://registry.npmjs.org/regenerator-runtime/-/regenerator-runtime-0.14.1.tgz
Source145: https://registry.npmjs.org/regenerator-transform/-/regenerator-transform-0.15.2.tgz
Source146: https://registry.npmjs.org/regexpu-core/-/regexpu-core-6.2.0.tgz
Source147: https://registry.npmjs.org/regjsgen/-/regjsgen-0.8.0.tgz
Source148: https://registry.npmjs.org/regjsparser/-/regjsparser-0.12.0.tgz
Source149: https://registry.npmjs.org/semver/-/semver-5.7.2.tgz
Source150: https://registry.npmjs.org/semver/-/semver-6.3.1.tgz
Source151: https://registry.npmjs.org/set-function-length/-/set-function-length-1.2.2.tgz
Source152: https://registry.npmjs.org/unicode-canonical-property-names-ecmascript/-/unicode-canonical-property-names-ecmascript-2.0.1.tgz
Source153: https://registry.npmjs.org/unicode-match-property-ecmascript/-/unicode-match-property-ecmascript-2.0.0.tgz
Source154: https://registry.npmjs.org/unicode-match-property-value-ecmascript/-/unicode-match-property-value-ecmascript-2.2.0.tgz
Source155: https://registry.npmjs.org/unicode-property-aliases-ecmascript/-/unicode-property-aliases-ecmascript-2.1.0.tgz
Source156: https://registry.npmjs.org/update-browserslist-db/-/update-browserslist-db-1.1.3.tgz
Source157: https://registry.npmjs.org/yallist/-/yallist-3.1.1.tgz
Source158: nodejs-theforeman-builder-%{version}-registry.npmjs.org.tgz
BuildRequires: %{?scl_prefix_nodejs}npm
%if 0%{!?scl:1}
BuildRequires: nodejs-packaging
%endif
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}
Provides: bundled(npm(@ampproject/remapping)) = 2.3.0
Provides: bundled(npm(@babel/code-frame)) = 7.26.2
Provides: bundled(npm(@babel/compat-data)) = 7.26.8
Provides: bundled(npm(@babel/core)) = 7.17.10
Provides: bundled(npm(@babel/generator)) = 7.26.9
Provides: bundled(npm(@babel/helper-annotate-as-pure)) = 7.25.9
Provides: bundled(npm(@babel/helper-compilation-targets)) = 7.26.5
Provides: bundled(npm(@babel/helper-create-class-features-plugin)) = 7.26.9
Provides: bundled(npm(@babel/helper-create-regexp-features-plugin)) = 7.26.3
Provides: bundled(npm(@babel/helper-environment-visitor)) = 7.24.7
Provides: bundled(npm(@babel/helper-hoist-variables)) = 7.24.7
Provides: bundled(npm(@babel/helper-member-expression-to-functions)) = 7.25.9
Provides: bundled(npm(@babel/helper-module-imports)) = 7.25.9
Provides: bundled(npm(@babel/helper-module-transforms)) = 7.26.0
Provides: bundled(npm(@babel/helper-optimise-call-expression)) = 7.25.9
Provides: bundled(npm(@babel/helper-plugin-utils)) = 7.26.5
Provides: bundled(npm(@babel/helper-remap-async-to-generator)) = 7.25.9
Provides: bundled(npm(@babel/helper-replace-supers)) = 7.26.5
Provides: bundled(npm(@babel/helper-simple-access)) = 7.25.9
Provides: bundled(npm(@babel/helper-skip-transparent-expression-wrappers)) = 7.25.9
Provides: bundled(npm(@babel/helper-string-parser)) = 7.25.9
Provides: bundled(npm(@babel/helper-validator-identifier)) = 7.25.9
Provides: bundled(npm(@babel/helper-validator-option)) = 7.25.9
Provides: bundled(npm(@babel/helper-wrap-function)) = 7.25.9
Provides: bundled(npm(@babel/helpers)) = 7.26.9
Provides: bundled(npm(@babel/parser)) = 7.26.9
Provides: bundled(npm(@babel/plugin-proposal-async-generator-functions)) = 7.20.7
Provides: bundled(npm(@babel/plugin-proposal-class-properties)) = 7.16.7
Provides: bundled(npm(@babel/plugin-proposal-dynamic-import)) = 7.18.6
Provides: bundled(npm(@babel/plugin-proposal-json-strings)) = 7.18.6
Provides: bundled(npm(@babel/plugin-proposal-nullish-coalescing-operator)) = 7.18.6
Provides: bundled(npm(@babel/plugin-proposal-numeric-separator)) = 7.18.6
Provides: bundled(npm(@babel/plugin-proposal-object-rest-spread)) = 7.16.7
Provides: bundled(npm(@babel/plugin-proposal-object-rest-spread)) = 7.20.7
Provides: bundled(npm(@babel/plugin-proposal-optional-catch-binding)) = 7.18.6
Provides: bundled(npm(@babel/plugin-proposal-optional-chaining)) = 7.21.0
Provides: bundled(npm(@babel/plugin-proposal-unicode-property-regex)) = 7.18.6
Provides: bundled(npm(@babel/plugin-syntax-async-generators)) = 7.8.4
Provides: bundled(npm(@babel/plugin-syntax-dynamic-import)) = 7.8.3
Provides: bundled(npm(@babel/plugin-syntax-json-strings)) = 7.8.3
Provides: bundled(npm(@babel/plugin-syntax-jsx)) = 7.25.9
Provides: bundled(npm(@babel/plugin-syntax-nullish-coalescing-operator)) = 7.8.3
Provides: bundled(npm(@babel/plugin-syntax-numeric-separator)) = 7.10.4
Provides: bundled(npm(@babel/plugin-syntax-object-rest-spread)) = 7.8.3
Provides: bundled(npm(@babel/plugin-syntax-optional-catch-binding)) = 7.8.3
Provides: bundled(npm(@babel/plugin-syntax-optional-chaining)) = 7.8.3
Provides: bundled(npm(@babel/plugin-syntax-top-level-await)) = 7.14.5
Provides: bundled(npm(@babel/plugin-transform-arrow-functions)) = 7.25.9
Provides: bundled(npm(@babel/plugin-transform-async-to-generator)) = 7.25.9
Provides: bundled(npm(@babel/plugin-transform-block-scoped-functions)) = 7.26.5
Provides: bundled(npm(@babel/plugin-transform-block-scoping)) = 7.25.9
Provides: bundled(npm(@babel/plugin-transform-classes)) = 7.25.9
Provides: bundled(npm(@babel/plugin-transform-computed-properties)) = 7.25.9
Provides: bundled(npm(@babel/plugin-transform-destructuring)) = 7.25.9
Provides: bundled(npm(@babel/plugin-transform-dotall-regex)) = 7.25.9
Provides: bundled(npm(@babel/plugin-transform-duplicate-keys)) = 7.25.9
Provides: bundled(npm(@babel/plugin-transform-exponentiation-operator)) = 7.26.3
Provides: bundled(npm(@babel/plugin-transform-for-of)) = 7.26.9
Provides: bundled(npm(@babel/plugin-transform-function-name)) = 7.25.9
Provides: bundled(npm(@babel/plugin-transform-literals)) = 7.25.9
Provides: bundled(npm(@babel/plugin-transform-member-expression-literals)) = 7.25.9
Provides: bundled(npm(@babel/plugin-transform-modules-amd)) = 7.25.9
Provides: bundled(npm(@babel/plugin-transform-modules-amd)) = 7.9.0
Provides: bundled(npm(@babel/plugin-transform-modules-commonjs)) = 7.26.3
Provides: bundled(npm(@babel/plugin-transform-modules-commonjs)) = 7.9.0
Provides: bundled(npm(@babel/plugin-transform-modules-systemjs)) = 7.25.9
Provides: bundled(npm(@babel/plugin-transform-modules-systemjs)) = 7.9.0
Provides: bundled(npm(@babel/plugin-transform-modules-umd)) = 7.25.9
Provides: bundled(npm(@babel/plugin-transform-named-capturing-groups-regex)) = 7.25.9
Provides: bundled(npm(@babel/plugin-transform-new-target)) = 7.25.9
Provides: bundled(npm(@babel/plugin-transform-object-assign)) = 7.25.9
Provides: bundled(npm(@babel/plugin-transform-object-super)) = 7.25.9
Provides: bundled(npm(@babel/plugin-transform-parameters)) = 7.25.9
Provides: bundled(npm(@babel/plugin-transform-property-literals)) = 7.25.9
Provides: bundled(npm(@babel/plugin-transform-react-display-name)) = 7.25.9
Provides: bundled(npm(@babel/plugin-transform-react-jsx)) = 7.25.9
Provides: bundled(npm(@babel/plugin-transform-react-jsx-development)) = 7.25.9
Provides: bundled(npm(@babel/plugin-transform-react-pure-annotations)) = 7.25.9
Provides: bundled(npm(@babel/plugin-transform-regenerator)) = 7.25.9
Provides: bundled(npm(@babel/plugin-transform-reserved-words)) = 7.25.9
Provides: bundled(npm(@babel/plugin-transform-shorthand-properties)) = 7.25.9
Provides: bundled(npm(@babel/plugin-transform-spread)) = 7.25.9
Provides: bundled(npm(@babel/plugin-transform-sticky-regex)) = 7.25.9
Provides: bundled(npm(@babel/plugin-transform-template-literals)) = 7.26.8
Provides: bundled(npm(@babel/plugin-transform-typeof-symbol)) = 7.26.7
Provides: bundled(npm(@babel/plugin-transform-unicode-regex)) = 7.25.9
Provides: bundled(npm(@babel/preset-env)) = 7.9.5
Provides: bundled(npm(@babel/preset-modules)) = 0.1.6
Provides: bundled(npm(@babel/preset-react)) = 7.16.7
Provides: bundled(npm(@babel/runtime)) = 7.26.9
Provides: bundled(npm(@babel/template)) = 7.26.9
Provides: bundled(npm(@babel/traverse)) = 7.26.9
Provides: bundled(npm(@babel/types)) = 7.26.9
Provides: bundled(npm(@jridgewell/gen-mapping)) = 0.3.8
Provides: bundled(npm(@jridgewell/resolve-uri)) = 3.1.2
Provides: bundled(npm(@jridgewell/set-array)) = 1.2.1
Provides: bundled(npm(@jridgewell/sourcemap-codec)) = 1.5.0
Provides: bundled(npm(@jridgewell/trace-mapping)) = 0.3.25
Provides: bundled(npm(@theforeman/builder)) = 15.0.0
Provides: bundled(npm(babel-plugin-dynamic-import-node)) = 2.3.0
Provides: bundled(npm(babel-plugin-dynamic-import-node)) = 2.3.3
Provides: bundled(npm(browserslist)) = 4.24.4
Provides: bundled(npm(call-bind)) = 1.0.8
Provides: bundled(npm(call-bind-apply-helpers)) = 1.0.2
Provides: bundled(npm(call-bound)) = 1.0.4
Provides: bundled(npm(caniuse-lite)) = 1.0.30001702
Provides: bundled(npm(convert-source-map)) = 1.9.0
Provides: bundled(npm(core-js-compat)) = 3.41.0
Provides: bundled(npm(debug)) = 4.4.0
Provides: bundled(npm(define-data-property)) = 1.1.4
Provides: bundled(npm(define-properties)) = 1.2.1
Provides: bundled(npm(dunder-proto)) = 1.0.1
Provides: bundled(npm(electron-to-chromium)) = 1.5.112
Provides: bundled(npm(es-define-property)) = 1.0.1
Provides: bundled(npm(es-errors)) = 1.3.0
Provides: bundled(npm(es-object-atoms)) = 1.1.1
Provides: bundled(npm(escalade)) = 3.2.0
Provides: bundled(npm(esutils)) = 2.0.3
Provides: bundled(npm(function-bind)) = 1.1.2
Provides: bundled(npm(gensync)) = 1.0.0-beta.2
Provides: bundled(npm(get-intrinsic)) = 1.3.0
Provides: bundled(npm(get-proto)) = 1.0.1
Provides: bundled(npm(globals)) = 11.12.0
Provides: bundled(npm(gopd)) = 1.2.0
Provides: bundled(npm(has-property-descriptors)) = 1.0.2
Provides: bundled(npm(has-symbols)) = 1.1.0
Provides: bundled(npm(hasown)) = 2.0.2
Provides: bundled(npm(invariant)) = 2.2.4
Provides: bundled(npm(js-tokens)) = 4.0.0
Provides: bundled(npm(jsesc)) = 3.0.2
Provides: bundled(npm(jsesc)) = 3.1.0
Provides: bundled(npm(json5)) = 2.2.3
Provides: bundled(npm(leven)) = 3.1.0
Provides: bundled(npm(levenary)) = 1.1.1
Provides: bundled(npm(loose-envify)) = 1.4.0
Provides: bundled(npm(lru-cache)) = 5.1.1
Provides: bundled(npm(math-intrinsics)) = 1.1.0
Provides: bundled(npm(ms)) = 2.1.3
Provides: bundled(npm(node-releases)) = 2.0.19
Provides: bundled(npm(object-keys)) = 1.1.1
Provides: bundled(npm(object.assign)) = 4.1.7
Provides: bundled(npm(picocolors)) = 1.1.1
Provides: bundled(npm(regenerate)) = 1.4.2
Provides: bundled(npm(regenerate-unicode-properties)) = 10.2.0
Provides: bundled(npm(regenerator-runtime)) = 0.14.1
Provides: bundled(npm(regenerator-transform)) = 0.15.2
Provides: bundled(npm(regexpu-core)) = 6.2.0
Provides: bundled(npm(regjsgen)) = 0.8.0
Provides: bundled(npm(regjsparser)) = 0.12.0
Provides: bundled(npm(semver)) = 5.7.2
Provides: bundled(npm(semver)) = 6.3.1
Provides: bundled(npm(set-function-length)) = 1.2.2
Provides: bundled(npm(unicode-canonical-property-names-ecmascript)) = 2.0.1
Provides: bundled(npm(unicode-match-property-ecmascript)) = 2.0.0
Provides: bundled(npm(unicode-match-property-value-ecmascript)) = 2.2.0
Provides: bundled(npm(unicode-property-aliases-ecmascript)) = 2.1.0
Provides: bundled(npm(update-browserslist-db)) = 1.1.3
Provides: bundled(npm(yallist)) = 3.1.1
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

%setup -T -q -a 158 -D -n %{npm_cache_dir}

%build
%{?scl:scl enable %{?scl_nodejs} - << \end_of_scl}
npm install --legacy-peer-deps --cache-min Infinity --cache %{?scl:../}%{npm_cache_dir} --no-shrinkwrap --no-optional --global-style true %{npm_name}@%{version}
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
* Thu Mar 06 2025 Evgeni Golov 15.0.0-1
- Update to 15.0.0

* Wed Jan 22 2025 Evgeni Golov 14.0.0-1
- Update to 14.0.0

* Mon May 06 2024 Foreman Packaging Automation <packaging@theforeman.org> 13.1.0-1
- Update to 13.1.0

* Tue Apr 09 2024 Evgeni Golov 13.0.1-1
- Update to 13.0.1

* Thu Feb 01 2024 Eric D. Helms <ericdhelms@gmail.com> - 12.2.3-2
- Use --legacy-peer-deps during npm install

* Tue Jan 02 2024 Foreman Packaging Automation <packaging@theforeman.org> 12.2.3-1
- Update to 12.2.3

* Fri Aug 11 2023 Foreman Packaging Automation <packaging@theforeman.org> 12.2.0-1
- Update to 12.2.0

* Thu Feb 09 2023 MariaAga <mariaaga@redhat.com> 12.0.1-1
- Update to 12.0.1

* Tue Sep 06 2022 Ron Lavi <1ronlavi@gmail.com> 10.1.7-1
- Update to 10.1.7

* Mon Feb 21 2022 Oleh Fedorenko <ofedoren@redhat.com> 10.1.0-1
- Update to 10.1.0

* Tue Jan 18 2022 MariaAga <mariaaga@redhat.com> 10.0.0-1
- Update to 10.0.0

* Thu Oct 21 2021 Ron Lavi <1ronlavi@gmail.com> 8.16.0-1
- Update to 8.16.0

* Wed Oct 06 2021 Ron Lavi <1ronlavi@gmail.com> 8.15.0-1
- Update to 8.15.0

* Sat Jul 03 2021 Eric D. Helms <ericdhelms@gmail.com> 8.7.2-1
- Update to 8.7.2

* Wed Jun 30 2021 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 8.7.0-1
- Update to 8.7.0

* Fri Apr 30 2021 Evgeni Golov 8.4.5-1
- Update to 8.4.5

* Tue Feb 16 2021 Ondrej Prazak <oprazak@redhat.com> 8.3.3-1
- Update to 8.3.3

* Tue Feb 09 2021 Ondrej Prazak <oprazak@redhat.com> 8.3.0-1
- Update to 8.3.0

* Wed Nov 18 2020 Evgeni Golov 6.0.0-1
- Update to 6.0.0

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

