%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name optimize-css-assets-webpack-plugin

Name: %{?scl_prefix}nodejs-optimize-css-assets-webpack-plugin
Version: 3.2.1
Release: 1%{?dist}
Summary: A Webpack plugin to optimize \ minimize CSS assets
License: MIT
Group: Development/Libraries
URL: http://github.com/NMFR/optimize-css-assets-webpack-plugin
Source0: https://registry.npmjs.org/@types/q/-/q-1.5.5.tgz
Source1: https://registry.npmjs.org/alphanum-sort/-/alphanum-sort-1.0.2.tgz
Source2: https://registry.npmjs.org/ansi-styles/-/ansi-styles-3.2.1.tgz
Source3: https://registry.npmjs.org/argparse/-/argparse-1.0.10.tgz
Source4: https://registry.npmjs.org/array-buffer-byte-length/-/array-buffer-byte-length-1.0.0.tgz
Source5: https://registry.npmjs.org/array.prototype.reduce/-/array.prototype.reduce-1.0.5.tgz
Source6: https://registry.npmjs.org/arraybuffer.prototype.slice/-/arraybuffer.prototype.slice-1.0.1.tgz
Source7: https://registry.npmjs.org/available-typed-arrays/-/available-typed-arrays-1.0.5.tgz
Source8: https://registry.npmjs.org/boolbase/-/boolbase-1.0.0.tgz
Source9: https://registry.npmjs.org/browserslist/-/browserslist-4.21.10.tgz
Source10: https://registry.npmjs.org/call-bind/-/call-bind-1.0.2.tgz
Source11: https://registry.npmjs.org/caller-callsite/-/caller-callsite-2.0.0.tgz
Source12: https://registry.npmjs.org/caller-path/-/caller-path-2.0.0.tgz
Source13: https://registry.npmjs.org/callsites/-/callsites-2.0.0.tgz
Source14: https://registry.npmjs.org/caniuse-api/-/caniuse-api-3.0.0.tgz
Source15: https://registry.npmjs.org/caniuse-lite/-/caniuse-lite-1.0.30001519.tgz
Source16: https://registry.npmjs.org/chalk/-/chalk-2.4.2.tgz
Source17: https://registry.npmjs.org/coa/-/coa-2.0.2.tgz
Source18: https://registry.npmjs.org/color/-/color-3.2.1.tgz
Source19: https://registry.npmjs.org/color-convert/-/color-convert-1.9.3.tgz
Source20: https://registry.npmjs.org/color-name/-/color-name-1.1.3.tgz
Source21: https://registry.npmjs.org/color-name/-/color-name-1.1.4.tgz
Source22: https://registry.npmjs.org/color-string/-/color-string-1.9.1.tgz
Source23: https://registry.npmjs.org/cosmiconfig/-/cosmiconfig-5.2.1.tgz
Source24: https://registry.npmjs.org/css-color-names/-/css-color-names-0.0.4.tgz
Source25: https://registry.npmjs.org/css-declaration-sorter/-/css-declaration-sorter-4.0.1.tgz
Source26: https://registry.npmjs.org/css-select/-/css-select-2.1.0.tgz
Source27: https://registry.npmjs.org/css-select-base-adapter/-/css-select-base-adapter-0.1.1.tgz
Source28: https://registry.npmjs.org/css-tree/-/css-tree-1.0.0-alpha.37.tgz
Source29: https://registry.npmjs.org/css-tree/-/css-tree-1.1.3.tgz
Source30: https://registry.npmjs.org/css-what/-/css-what-3.4.2.tgz
Source31: https://registry.npmjs.org/cssesc/-/cssesc-3.0.0.tgz
Source32: https://registry.npmjs.org/cssnano/-/cssnano-4.1.11.tgz
Source33: https://registry.npmjs.org/cssnano-preset-default/-/cssnano-preset-default-4.0.8.tgz
Source34: https://registry.npmjs.org/cssnano-util-get-arguments/-/cssnano-util-get-arguments-4.0.0.tgz
Source35: https://registry.npmjs.org/cssnano-util-get-match/-/cssnano-util-get-match-4.0.0.tgz
Source36: https://registry.npmjs.org/cssnano-util-raw-cache/-/cssnano-util-raw-cache-4.0.1.tgz
Source37: https://registry.npmjs.org/cssnano-util-same-parent/-/cssnano-util-same-parent-4.0.1.tgz
Source38: https://registry.npmjs.org/csso/-/csso-4.2.0.tgz
Source39: https://registry.npmjs.org/define-properties/-/define-properties-1.2.0.tgz
Source40: https://registry.npmjs.org/dom-serializer/-/dom-serializer-0.2.2.tgz
Source41: https://registry.npmjs.org/domelementtype/-/domelementtype-1.3.1.tgz
Source42: https://registry.npmjs.org/domelementtype/-/domelementtype-2.3.0.tgz
Source43: https://registry.npmjs.org/domutils/-/domutils-1.7.0.tgz
Source44: https://registry.npmjs.org/dot-prop/-/dot-prop-5.3.0.tgz
Source45: https://registry.npmjs.org/electron-to-chromium/-/electron-to-chromium-1.4.490.tgz
Source46: https://registry.npmjs.org/entities/-/entities-2.2.0.tgz
Source47: https://registry.npmjs.org/error-ex/-/error-ex-1.3.2.tgz
Source48: https://registry.npmjs.org/es-abstract/-/es-abstract-1.22.1.tgz
Source49: https://registry.npmjs.org/es-array-method-boxes-properly/-/es-array-method-boxes-properly-1.0.0.tgz
Source50: https://registry.npmjs.org/es-set-tostringtag/-/es-set-tostringtag-2.0.1.tgz
Source51: https://registry.npmjs.org/es-to-primitive/-/es-to-primitive-1.2.1.tgz
Source52: https://registry.npmjs.org/escalade/-/escalade-3.1.1.tgz
Source53: https://registry.npmjs.org/escape-string-regexp/-/escape-string-regexp-1.0.5.tgz
Source54: https://registry.npmjs.org/esprima/-/esprima-4.0.1.tgz
Source55: https://registry.npmjs.org/for-each/-/for-each-0.3.3.tgz
Source56: https://registry.npmjs.org/function-bind/-/function-bind-1.1.1.tgz
Source57: https://registry.npmjs.org/function.prototype.name/-/function.prototype.name-1.1.5.tgz
Source58: https://registry.npmjs.org/functions-have-names/-/functions-have-names-1.2.3.tgz
Source59: https://registry.npmjs.org/get-intrinsic/-/get-intrinsic-1.2.1.tgz
Source60: https://registry.npmjs.org/get-symbol-description/-/get-symbol-description-1.0.0.tgz
Source61: https://registry.npmjs.org/globalthis/-/globalthis-1.0.3.tgz
Source62: https://registry.npmjs.org/gopd/-/gopd-1.0.1.tgz
Source63: https://registry.npmjs.org/has/-/has-1.0.3.tgz
Source64: https://registry.npmjs.org/has-bigints/-/has-bigints-1.0.2.tgz
Source65: https://registry.npmjs.org/has-flag/-/has-flag-3.0.0.tgz
Source66: https://registry.npmjs.org/has-property-descriptors/-/has-property-descriptors-1.0.0.tgz
Source67: https://registry.npmjs.org/has-proto/-/has-proto-1.0.1.tgz
Source68: https://registry.npmjs.org/has-symbols/-/has-symbols-1.0.3.tgz
Source69: https://registry.npmjs.org/has-tostringtag/-/has-tostringtag-1.0.0.tgz
Source70: https://registry.npmjs.org/hex-color-regex/-/hex-color-regex-1.1.0.tgz
Source71: https://registry.npmjs.org/hsl-regex/-/hsl-regex-1.0.0.tgz
Source72: https://registry.npmjs.org/hsla-regex/-/hsla-regex-1.0.0.tgz
Source73: https://registry.npmjs.org/import-fresh/-/import-fresh-2.0.0.tgz
Source74: https://registry.npmjs.org/indexes-of/-/indexes-of-1.0.1.tgz
Source75: https://registry.npmjs.org/internal-slot/-/internal-slot-1.0.5.tgz
Source76: https://registry.npmjs.org/is-absolute-url/-/is-absolute-url-2.1.0.tgz
Source77: https://registry.npmjs.org/is-array-buffer/-/is-array-buffer-3.0.2.tgz
Source78: https://registry.npmjs.org/is-arrayish/-/is-arrayish-0.2.1.tgz
Source79: https://registry.npmjs.org/is-arrayish/-/is-arrayish-0.3.2.tgz
Source80: https://registry.npmjs.org/is-bigint/-/is-bigint-1.0.4.tgz
Source81: https://registry.npmjs.org/is-boolean-object/-/is-boolean-object-1.1.2.tgz
Source82: https://registry.npmjs.org/is-callable/-/is-callable-1.2.7.tgz
Source83: https://registry.npmjs.org/is-color-stop/-/is-color-stop-1.1.0.tgz
Source84: https://registry.npmjs.org/is-date-object/-/is-date-object-1.0.5.tgz
Source85: https://registry.npmjs.org/is-directory/-/is-directory-0.3.1.tgz
Source86: https://registry.npmjs.org/is-negative-zero/-/is-negative-zero-2.0.2.tgz
Source87: https://registry.npmjs.org/is-number-object/-/is-number-object-1.0.7.tgz
Source88: https://registry.npmjs.org/is-obj/-/is-obj-2.0.0.tgz
Source89: https://registry.npmjs.org/is-regex/-/is-regex-1.1.4.tgz
Source90: https://registry.npmjs.org/is-resolvable/-/is-resolvable-1.1.0.tgz
Source91: https://registry.npmjs.org/is-shared-array-buffer/-/is-shared-array-buffer-1.0.2.tgz
Source92: https://registry.npmjs.org/is-string/-/is-string-1.0.7.tgz
Source93: https://registry.npmjs.org/is-symbol/-/is-symbol-1.0.4.tgz
Source94: https://registry.npmjs.org/is-typed-array/-/is-typed-array-1.1.12.tgz
Source95: https://registry.npmjs.org/is-weakref/-/is-weakref-1.0.2.tgz
Source96: https://registry.npmjs.org/isarray/-/isarray-2.0.5.tgz
Source97: https://registry.npmjs.org/js-yaml/-/js-yaml-3.14.1.tgz
Source98: https://registry.npmjs.org/json-parse-better-errors/-/json-parse-better-errors-1.0.2.tgz
Source99: https://registry.npmjs.org/last-call-webpack-plugin/-/last-call-webpack-plugin-2.1.2.tgz
Source100: https://registry.npmjs.org/lodash/-/lodash-4.17.21.tgz
Source101: https://registry.npmjs.org/lodash.memoize/-/lodash.memoize-4.1.2.tgz
Source102: https://registry.npmjs.org/lodash.uniq/-/lodash.uniq-4.5.0.tgz
Source103: https://registry.npmjs.org/mdn-data/-/mdn-data-2.0.14.tgz
Source104: https://registry.npmjs.org/mdn-data/-/mdn-data-2.0.4.tgz
Source105: https://registry.npmjs.org/minimist/-/minimist-1.2.8.tgz
Source106: https://registry.npmjs.org/mkdirp/-/mkdirp-0.5.6.tgz
Source107: https://registry.npmjs.org/node-releases/-/node-releases-2.0.13.tgz
Source108: https://registry.npmjs.org/normalize-url/-/normalize-url-3.3.0.tgz
Source109: https://registry.npmjs.org/nth-check/-/nth-check-1.0.2.tgz
Source110: https://registry.npmjs.org/object-inspect/-/object-inspect-1.12.3.tgz
Source111: https://registry.npmjs.org/object-keys/-/object-keys-1.1.1.tgz
Source112: https://registry.npmjs.org/object.assign/-/object.assign-4.1.4.tgz
Source113: https://registry.npmjs.org/object.getownpropertydescriptors/-/object.getownpropertydescriptors-2.1.6.tgz
Source114: https://registry.npmjs.org/object.values/-/object.values-1.1.6.tgz
Source115: https://registry.npmjs.org/optimize-css-assets-webpack-plugin/-/optimize-css-assets-webpack-plugin-3.2.1.tgz
Source116: https://registry.npmjs.org/parse-json/-/parse-json-4.0.0.tgz
Source117: https://registry.npmjs.org/picocolors/-/picocolors-0.2.1.tgz
Source118: https://registry.npmjs.org/picocolors/-/picocolors-1.0.0.tgz
Source119: https://registry.npmjs.org/postcss/-/postcss-7.0.39.tgz
Source120: https://registry.npmjs.org/postcss-calc/-/postcss-calc-7.0.5.tgz
Source121: https://registry.npmjs.org/postcss-colormin/-/postcss-colormin-4.0.3.tgz
Source122: https://registry.npmjs.org/postcss-convert-values/-/postcss-convert-values-4.0.1.tgz
Source123: https://registry.npmjs.org/postcss-discard-comments/-/postcss-discard-comments-4.0.2.tgz
Source124: https://registry.npmjs.org/postcss-discard-duplicates/-/postcss-discard-duplicates-4.0.2.tgz
Source125: https://registry.npmjs.org/postcss-discard-empty/-/postcss-discard-empty-4.0.1.tgz
Source126: https://registry.npmjs.org/postcss-discard-overridden/-/postcss-discard-overridden-4.0.1.tgz
Source127: https://registry.npmjs.org/postcss-merge-longhand/-/postcss-merge-longhand-4.0.11.tgz
Source128: https://registry.npmjs.org/postcss-merge-rules/-/postcss-merge-rules-4.0.3.tgz
Source129: https://registry.npmjs.org/postcss-minify-font-values/-/postcss-minify-font-values-4.0.2.tgz
Source130: https://registry.npmjs.org/postcss-minify-gradients/-/postcss-minify-gradients-4.0.2.tgz
Source131: https://registry.npmjs.org/postcss-minify-params/-/postcss-minify-params-4.0.2.tgz
Source132: https://registry.npmjs.org/postcss-minify-selectors/-/postcss-minify-selectors-4.0.2.tgz
Source133: https://registry.npmjs.org/postcss-normalize-charset/-/postcss-normalize-charset-4.0.1.tgz
Source134: https://registry.npmjs.org/postcss-normalize-display-values/-/postcss-normalize-display-values-4.0.2.tgz
Source135: https://registry.npmjs.org/postcss-normalize-positions/-/postcss-normalize-positions-4.0.2.tgz
Source136: https://registry.npmjs.org/postcss-normalize-repeat-style/-/postcss-normalize-repeat-style-4.0.2.tgz
Source137: https://registry.npmjs.org/postcss-normalize-string/-/postcss-normalize-string-4.0.2.tgz
Source138: https://registry.npmjs.org/postcss-normalize-timing-functions/-/postcss-normalize-timing-functions-4.0.2.tgz
Source139: https://registry.npmjs.org/postcss-normalize-unicode/-/postcss-normalize-unicode-4.0.1.tgz
Source140: https://registry.npmjs.org/postcss-normalize-url/-/postcss-normalize-url-4.0.1.tgz
Source141: https://registry.npmjs.org/postcss-normalize-whitespace/-/postcss-normalize-whitespace-4.0.2.tgz
Source142: https://registry.npmjs.org/postcss-ordered-values/-/postcss-ordered-values-4.1.2.tgz
Source143: https://registry.npmjs.org/postcss-reduce-initial/-/postcss-reduce-initial-4.0.3.tgz
Source144: https://registry.npmjs.org/postcss-reduce-transforms/-/postcss-reduce-transforms-4.0.2.tgz
Source145: https://registry.npmjs.org/postcss-selector-parser/-/postcss-selector-parser-3.1.2.tgz
Source146: https://registry.npmjs.org/postcss-selector-parser/-/postcss-selector-parser-6.0.13.tgz
Source147: https://registry.npmjs.org/postcss-svgo/-/postcss-svgo-4.0.3.tgz
Source148: https://registry.npmjs.org/postcss-unique-selectors/-/postcss-unique-selectors-4.0.1.tgz
Source149: https://registry.npmjs.org/postcss-value-parser/-/postcss-value-parser-3.3.1.tgz
Source150: https://registry.npmjs.org/postcss-value-parser/-/postcss-value-parser-4.2.0.tgz
Source151: https://registry.npmjs.org/q/-/q-1.5.1.tgz
Source152: https://registry.npmjs.org/regexp.prototype.flags/-/regexp.prototype.flags-1.5.0.tgz
Source153: https://registry.npmjs.org/resolve-from/-/resolve-from-3.0.0.tgz
Source154: https://registry.npmjs.org/rgb-regex/-/rgb-regex-1.0.1.tgz
Source155: https://registry.npmjs.org/rgba-regex/-/rgba-regex-1.0.0.tgz
Source156: https://registry.npmjs.org/safe-array-concat/-/safe-array-concat-1.0.0.tgz
Source157: https://registry.npmjs.org/safe-regex-test/-/safe-regex-test-1.0.0.tgz
Source158: https://registry.npmjs.org/sax/-/sax-1.2.4.tgz
Source159: https://registry.npmjs.org/side-channel/-/side-channel-1.0.4.tgz
Source160: https://registry.npmjs.org/simple-swizzle/-/simple-swizzle-0.2.2.tgz
Source161: https://registry.npmjs.org/source-list-map/-/source-list-map-2.0.1.tgz
Source162: https://registry.npmjs.org/source-map/-/source-map-0.6.1.tgz
Source163: https://registry.npmjs.org/sprintf-js/-/sprintf-js-1.0.3.tgz
Source164: https://registry.npmjs.org/stable/-/stable-0.1.8.tgz
Source165: https://registry.npmjs.org/string.prototype.trim/-/string.prototype.trim-1.2.7.tgz
Source166: https://registry.npmjs.org/string.prototype.trimend/-/string.prototype.trimend-1.0.6.tgz
Source167: https://registry.npmjs.org/string.prototype.trimstart/-/string.prototype.trimstart-1.0.6.tgz
Source168: https://registry.npmjs.org/stylehacks/-/stylehacks-4.0.3.tgz
Source169: https://registry.npmjs.org/supports-color/-/supports-color-5.5.0.tgz
Source170: https://registry.npmjs.org/svgo/-/svgo-1.3.2.tgz
Source171: https://registry.npmjs.org/timsort/-/timsort-0.3.0.tgz
Source172: https://registry.npmjs.org/typed-array-buffer/-/typed-array-buffer-1.0.0.tgz
Source173: https://registry.npmjs.org/typed-array-byte-length/-/typed-array-byte-length-1.0.0.tgz
Source174: https://registry.npmjs.org/typed-array-byte-offset/-/typed-array-byte-offset-1.0.0.tgz
Source175: https://registry.npmjs.org/typed-array-length/-/typed-array-length-1.0.4.tgz
Source176: https://registry.npmjs.org/unbox-primitive/-/unbox-primitive-1.0.2.tgz
Source177: https://registry.npmjs.org/uniq/-/uniq-1.0.1.tgz
Source178: https://registry.npmjs.org/uniqs/-/uniqs-2.0.0.tgz
Source179: https://registry.npmjs.org/unquote/-/unquote-1.1.1.tgz
Source180: https://registry.npmjs.org/update-browserslist-db/-/update-browserslist-db-1.0.11.tgz
Source181: https://registry.npmjs.org/util-deprecate/-/util-deprecate-1.0.2.tgz
Source182: https://registry.npmjs.org/util.promisify/-/util.promisify-1.0.1.tgz
Source183: https://registry.npmjs.org/vendors/-/vendors-1.0.4.tgz
Source184: https://registry.npmjs.org/webpack-sources/-/webpack-sources-1.4.3.tgz
Source185: https://registry.npmjs.org/which-boxed-primitive/-/which-boxed-primitive-1.0.2.tgz
Source186: https://registry.npmjs.org/which-typed-array/-/which-typed-array-1.1.11.tgz
Source187: nodejs-optimize-css-assets-webpack-plugin-%{version}-registry.npmjs.org.tgz
BuildRequires: %{?scl_prefix_nodejs}npm
%if 0%{!?scl:1}
BuildRequires: nodejs-packaging
%endif
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}
Provides: bundled(npm(@types/q)) = 1.5.5
Provides: bundled(npm(alphanum-sort)) = 1.0.2
Provides: bundled(npm(ansi-styles)) = 3.2.1
Provides: bundled(npm(argparse)) = 1.0.10
Provides: bundled(npm(array-buffer-byte-length)) = 1.0.0
Provides: bundled(npm(array.prototype.reduce)) = 1.0.5
Provides: bundled(npm(arraybuffer.prototype.slice)) = 1.0.1
Provides: bundled(npm(available-typed-arrays)) = 1.0.5
Provides: bundled(npm(boolbase)) = 1.0.0
Provides: bundled(npm(browserslist)) = 4.21.10
Provides: bundled(npm(call-bind)) = 1.0.2
Provides: bundled(npm(caller-callsite)) = 2.0.0
Provides: bundled(npm(caller-path)) = 2.0.0
Provides: bundled(npm(callsites)) = 2.0.0
Provides: bundled(npm(caniuse-api)) = 3.0.0
Provides: bundled(npm(caniuse-lite)) = 1.0.30001519
Provides: bundled(npm(chalk)) = 2.4.2
Provides: bundled(npm(coa)) = 2.0.2
Provides: bundled(npm(color)) = 3.2.1
Provides: bundled(npm(color-convert)) = 1.9.3
Provides: bundled(npm(color-name)) = 1.1.3
Provides: bundled(npm(color-name)) = 1.1.4
Provides: bundled(npm(color-string)) = 1.9.1
Provides: bundled(npm(cosmiconfig)) = 5.2.1
Provides: bundled(npm(css-color-names)) = 0.0.4
Provides: bundled(npm(css-declaration-sorter)) = 4.0.1
Provides: bundled(npm(css-select)) = 2.1.0
Provides: bundled(npm(css-select-base-adapter)) = 0.1.1
Provides: bundled(npm(css-tree)) = 1.0.0-alpha.37
Provides: bundled(npm(css-tree)) = 1.1.3
Provides: bundled(npm(css-what)) = 3.4.2
Provides: bundled(npm(cssesc)) = 3.0.0
Provides: bundled(npm(cssnano)) = 4.1.11
Provides: bundled(npm(cssnano-preset-default)) = 4.0.8
Provides: bundled(npm(cssnano-util-get-arguments)) = 4.0.0
Provides: bundled(npm(cssnano-util-get-match)) = 4.0.0
Provides: bundled(npm(cssnano-util-raw-cache)) = 4.0.1
Provides: bundled(npm(cssnano-util-same-parent)) = 4.0.1
Provides: bundled(npm(csso)) = 4.2.0
Provides: bundled(npm(define-properties)) = 1.2.0
Provides: bundled(npm(dom-serializer)) = 0.2.2
Provides: bundled(npm(domelementtype)) = 1.3.1
Provides: bundled(npm(domelementtype)) = 2.3.0
Provides: bundled(npm(domutils)) = 1.7.0
Provides: bundled(npm(dot-prop)) = 5.3.0
Provides: bundled(npm(electron-to-chromium)) = 1.4.490
Provides: bundled(npm(entities)) = 2.2.0
Provides: bundled(npm(error-ex)) = 1.3.2
Provides: bundled(npm(es-abstract)) = 1.22.1
Provides: bundled(npm(es-array-method-boxes-properly)) = 1.0.0
Provides: bundled(npm(es-set-tostringtag)) = 2.0.1
Provides: bundled(npm(es-to-primitive)) = 1.2.1
Provides: bundled(npm(escalade)) = 3.1.1
Provides: bundled(npm(escape-string-regexp)) = 1.0.5
Provides: bundled(npm(esprima)) = 4.0.1
Provides: bundled(npm(for-each)) = 0.3.3
Provides: bundled(npm(function-bind)) = 1.1.1
Provides: bundled(npm(function.prototype.name)) = 1.1.5
Provides: bundled(npm(functions-have-names)) = 1.2.3
Provides: bundled(npm(get-intrinsic)) = 1.2.1
Provides: bundled(npm(get-symbol-description)) = 1.0.0
Provides: bundled(npm(globalthis)) = 1.0.3
Provides: bundled(npm(gopd)) = 1.0.1
Provides: bundled(npm(has)) = 1.0.3
Provides: bundled(npm(has-bigints)) = 1.0.2
Provides: bundled(npm(has-flag)) = 3.0.0
Provides: bundled(npm(has-property-descriptors)) = 1.0.0
Provides: bundled(npm(has-proto)) = 1.0.1
Provides: bundled(npm(has-symbols)) = 1.0.3
Provides: bundled(npm(has-tostringtag)) = 1.0.0
Provides: bundled(npm(hex-color-regex)) = 1.1.0
Provides: bundled(npm(hsl-regex)) = 1.0.0
Provides: bundled(npm(hsla-regex)) = 1.0.0
Provides: bundled(npm(import-fresh)) = 2.0.0
Provides: bundled(npm(indexes-of)) = 1.0.1
Provides: bundled(npm(internal-slot)) = 1.0.5
Provides: bundled(npm(is-absolute-url)) = 2.1.0
Provides: bundled(npm(is-array-buffer)) = 3.0.2
Provides: bundled(npm(is-arrayish)) = 0.2.1
Provides: bundled(npm(is-arrayish)) = 0.3.2
Provides: bundled(npm(is-bigint)) = 1.0.4
Provides: bundled(npm(is-boolean-object)) = 1.1.2
Provides: bundled(npm(is-callable)) = 1.2.7
Provides: bundled(npm(is-color-stop)) = 1.1.0
Provides: bundled(npm(is-date-object)) = 1.0.5
Provides: bundled(npm(is-directory)) = 0.3.1
Provides: bundled(npm(is-negative-zero)) = 2.0.2
Provides: bundled(npm(is-number-object)) = 1.0.7
Provides: bundled(npm(is-obj)) = 2.0.0
Provides: bundled(npm(is-regex)) = 1.1.4
Provides: bundled(npm(is-resolvable)) = 1.1.0
Provides: bundled(npm(is-shared-array-buffer)) = 1.0.2
Provides: bundled(npm(is-string)) = 1.0.7
Provides: bundled(npm(is-symbol)) = 1.0.4
Provides: bundled(npm(is-typed-array)) = 1.1.12
Provides: bundled(npm(is-weakref)) = 1.0.2
Provides: bundled(npm(isarray)) = 2.0.5
Provides: bundled(npm(js-yaml)) = 3.14.1
Provides: bundled(npm(json-parse-better-errors)) = 1.0.2
Provides: bundled(npm(last-call-webpack-plugin)) = 2.1.2
Provides: bundled(npm(lodash)) = 4.17.21
Provides: bundled(npm(lodash.memoize)) = 4.1.2
Provides: bundled(npm(lodash.uniq)) = 4.5.0
Provides: bundled(npm(mdn-data)) = 2.0.14
Provides: bundled(npm(mdn-data)) = 2.0.4
Provides: bundled(npm(minimist)) = 1.2.8
Provides: bundled(npm(mkdirp)) = 0.5.6
Provides: bundled(npm(node-releases)) = 2.0.13
Provides: bundled(npm(normalize-url)) = 3.3.0
Provides: bundled(npm(nth-check)) = 1.0.2
Provides: bundled(npm(object-inspect)) = 1.12.3
Provides: bundled(npm(object-keys)) = 1.1.1
Provides: bundled(npm(object.assign)) = 4.1.4
Provides: bundled(npm(object.getownpropertydescriptors)) = 2.1.6
Provides: bundled(npm(object.values)) = 1.1.6
Provides: bundled(npm(optimize-css-assets-webpack-plugin)) = 3.2.1
Provides: bundled(npm(parse-json)) = 4.0.0
Provides: bundled(npm(picocolors)) = 0.2.1
Provides: bundled(npm(picocolors)) = 1.0.0
Provides: bundled(npm(postcss)) = 7.0.39
Provides: bundled(npm(postcss-calc)) = 7.0.5
Provides: bundled(npm(postcss-colormin)) = 4.0.3
Provides: bundled(npm(postcss-convert-values)) = 4.0.1
Provides: bundled(npm(postcss-discard-comments)) = 4.0.2
Provides: bundled(npm(postcss-discard-duplicates)) = 4.0.2
Provides: bundled(npm(postcss-discard-empty)) = 4.0.1
Provides: bundled(npm(postcss-discard-overridden)) = 4.0.1
Provides: bundled(npm(postcss-merge-longhand)) = 4.0.11
Provides: bundled(npm(postcss-merge-rules)) = 4.0.3
Provides: bundled(npm(postcss-minify-font-values)) = 4.0.2
Provides: bundled(npm(postcss-minify-gradients)) = 4.0.2
Provides: bundled(npm(postcss-minify-params)) = 4.0.2
Provides: bundled(npm(postcss-minify-selectors)) = 4.0.2
Provides: bundled(npm(postcss-normalize-charset)) = 4.0.1
Provides: bundled(npm(postcss-normalize-display-values)) = 4.0.2
Provides: bundled(npm(postcss-normalize-positions)) = 4.0.2
Provides: bundled(npm(postcss-normalize-repeat-style)) = 4.0.2
Provides: bundled(npm(postcss-normalize-string)) = 4.0.2
Provides: bundled(npm(postcss-normalize-timing-functions)) = 4.0.2
Provides: bundled(npm(postcss-normalize-unicode)) = 4.0.1
Provides: bundled(npm(postcss-normalize-url)) = 4.0.1
Provides: bundled(npm(postcss-normalize-whitespace)) = 4.0.2
Provides: bundled(npm(postcss-ordered-values)) = 4.1.2
Provides: bundled(npm(postcss-reduce-initial)) = 4.0.3
Provides: bundled(npm(postcss-reduce-transforms)) = 4.0.2
Provides: bundled(npm(postcss-selector-parser)) = 3.1.2
Provides: bundled(npm(postcss-selector-parser)) = 6.0.13
Provides: bundled(npm(postcss-svgo)) = 4.0.3
Provides: bundled(npm(postcss-unique-selectors)) = 4.0.1
Provides: bundled(npm(postcss-value-parser)) = 3.3.1
Provides: bundled(npm(postcss-value-parser)) = 4.2.0
Provides: bundled(npm(q)) = 1.5.1
Provides: bundled(npm(regexp.prototype.flags)) = 1.5.0
Provides: bundled(npm(resolve-from)) = 3.0.0
Provides: bundled(npm(rgb-regex)) = 1.0.1
Provides: bundled(npm(rgba-regex)) = 1.0.0
Provides: bundled(npm(safe-array-concat)) = 1.0.0
Provides: bundled(npm(safe-regex-test)) = 1.0.0
Provides: bundled(npm(sax)) = 1.2.4
Provides: bundled(npm(side-channel)) = 1.0.4
Provides: bundled(npm(simple-swizzle)) = 0.2.2
Provides: bundled(npm(source-list-map)) = 2.0.1
Provides: bundled(npm(source-map)) = 0.6.1
Provides: bundled(npm(sprintf-js)) = 1.0.3
Provides: bundled(npm(stable)) = 0.1.8
Provides: bundled(npm(string.prototype.trim)) = 1.2.7
Provides: bundled(npm(string.prototype.trimend)) = 1.0.6
Provides: bundled(npm(string.prototype.trimstart)) = 1.0.6
Provides: bundled(npm(stylehacks)) = 4.0.3
Provides: bundled(npm(supports-color)) = 5.5.0
Provides: bundled(npm(svgo)) = 1.3.2
Provides: bundled(npm(timsort)) = 0.3.0
Provides: bundled(npm(typed-array-buffer)) = 1.0.0
Provides: bundled(npm(typed-array-byte-length)) = 1.0.0
Provides: bundled(npm(typed-array-byte-offset)) = 1.0.0
Provides: bundled(npm(typed-array-length)) = 1.0.4
Provides: bundled(npm(unbox-primitive)) = 1.0.2
Provides: bundled(npm(uniq)) = 1.0.1
Provides: bundled(npm(uniqs)) = 2.0.0
Provides: bundled(npm(unquote)) = 1.1.1
Provides: bundled(npm(update-browserslist-db)) = 1.0.11
Provides: bundled(npm(util-deprecate)) = 1.0.2
Provides: bundled(npm(util.promisify)) = 1.0.1
Provides: bundled(npm(vendors)) = 1.0.4
Provides: bundled(npm(webpack-sources)) = 1.4.3
Provides: bundled(npm(which-boxed-primitive)) = 1.0.2
Provides: bundled(npm(which-typed-array)) = 1.1.11
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

%setup -T -q -a 187 -D -n %{npm_cache_dir}

%build
%{?scl:scl enable %{?scl_nodejs} - << \end_of_scl}
npm install --cache-min Infinity --cache %{?scl:../}%{npm_cache_dir} --no-shrinkwrap --no-optional --global-style true %{npm_name}@%{version}
%{?scl:end_of_scl}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/index.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%license node_modules/%{npm_name}/LICENSE
%doc node_modules/%{npm_name}/README.md

%changelog
* Fri Aug 11 2023 Foreman Packaging Automation <packaging@theforeman.org> 3.2.1-1
- Update to 3.2.1

* Wed Nov 11 2020 vagrant 3.2.0-1
- Add nodejs-optimize-css-assets-webpack-plugin generated by npm2rpm using the bundle strategy

