%global npm_name css-loader

%{?nodejs_find_provides_and_requires}

Name: nodejs-%{npm_name}
Version: 0.23.1
Release: 2%{?dist}
Summary: css loader module for webpack
License: MIT
URL: https://www.npmjs.com/package/css-loader
Source0: http://registry.npmjs.org/css-loader/-/css-loader-0.23.1.tgz
Source1: http://registry.npmjs.org/object-assign/-/object-assign-4.1.0.tgz
Source2: http://registry.npmjs.org/postcss-modules-extract-imports/-/postcss-modules-extract-imports-1.0.1.tgz
Source3: http://registry.npmjs.org/postcss-modules-local-by-default/-/postcss-modules-local-by-default-1.1.1.tgz
Source4: http://registry.npmjs.org/lodash.camelcase/-/lodash.camelcase-3.0.1.tgz
Source5: http://registry.npmjs.org/css-selector-tokenizer/-/css-selector-tokenizer-0.5.4.tgz
Source6: http://registry.npmjs.org/cssnano/-/cssnano-3.7.4.tgz
Source7: http://registry.npmjs.org/postcss/-/postcss-5.1.2.tgz
Source8: http://registry.npmjs.org/source-list-map/-/source-list-map-0.1.6.tgz
Source9: http://registry.npmjs.org/postcss-modules-scope/-/postcss-modules-scope-1.0.2.tgz
Source10: http://registry.npmjs.org/css-selector-tokenizer/-/css-selector-tokenizer-0.6.0.tgz
Source11: http://registry.npmjs.org/loader-utils/-/loader-utils-0.2.15.tgz
Source12: http://registry.npmjs.org/postcss-modules-values/-/postcss-modules-values-1.2.2.tgz
Source13: http://registry.npmjs.org/lodash._createcompounder/-/lodash._createcompounder-3.0.0.tgz
Source14: http://registry.npmjs.org/cssesc/-/cssesc-0.1.0.tgz
Source15: http://registry.npmjs.org/decamelize/-/decamelize-1.2.0.tgz
Source16: http://registry.npmjs.org/fastparse/-/fastparse-1.1.1.tgz
Source17: http://registry.npmjs.org/has/-/has-1.0.1.tgz
Source18: http://registry.npmjs.org/defined/-/defined-1.0.0.tgz
Source19: http://registry.npmjs.org/postcss-calc/-/postcss-calc-5.3.1.tgz
Source20: http://registry.npmjs.org/postcss-colormin/-/postcss-colormin-2.2.0.tgz
Source21: http://registry.npmjs.org/postcss-discard-duplicates/-/postcss-discard-duplicates-2.0.1.tgz
Source22: http://registry.npmjs.org/postcss-discard-comments/-/postcss-discard-comments-2.0.4.tgz
Source23: http://registry.npmjs.org/postcss-convert-values/-/postcss-convert-values-2.4.0.tgz
Source24: http://registry.npmjs.org/postcss-discard-empty/-/postcss-discard-empty-2.1.0.tgz
Source25: http://registry.npmjs.org/postcss-discard-overridden/-/postcss-discard-overridden-0.1.1.tgz
Source26: http://registry.npmjs.org/postcss-merge-longhand/-/postcss-merge-longhand-2.0.1.tgz
Source27: http://registry.npmjs.org/postcss-filter-plugins/-/postcss-filter-plugins-2.0.1.tgz
Source28: http://registry.npmjs.org/postcss-minify-font-values/-/postcss-minify-font-values-1.0.5.tgz
Source29: http://registry.npmjs.org/postcss-merge-idents/-/postcss-merge-idents-2.1.7.tgz
Source30: http://registry.npmjs.org/postcss-merge-rules/-/postcss-merge-rules-2.0.10.tgz
Source31: http://registry.npmjs.org/postcss-discard-unused/-/postcss-discard-unused-2.2.1.tgz
Source32: http://registry.npmjs.org/postcss-minify-gradients/-/postcss-minify-gradients-1.0.3.tgz
Source33: http://registry.npmjs.org/postcss-minify-params/-/postcss-minify-params-1.0.5.tgz
Source34: http://registry.npmjs.org/postcss-normalize-charset/-/postcss-normalize-charset-1.1.0.tgz
Source35: http://registry.npmjs.org/postcss-normalize-url/-/postcss-normalize-url-3.0.7.tgz
Source36: http://registry.npmjs.org/postcss-minify-selectors/-/postcss-minify-selectors-2.0.5.tgz
Source37: http://registry.npmjs.org/postcss-reduce-initial/-/postcss-reduce-initial-1.0.0.tgz
Source38: http://registry.npmjs.org/postcss-reduce-idents/-/postcss-reduce-idents-2.3.0.tgz
Source39: http://registry.npmjs.org/postcss-ordered-values/-/postcss-ordered-values-2.2.1.tgz
Source40: http://registry.npmjs.org/postcss-reduce-transforms/-/postcss-reduce-transforms-1.0.3.tgz
Source41: http://registry.npmjs.org/postcss-svgo/-/postcss-svgo-2.1.4.tgz
Source42: http://registry.npmjs.org/postcss-unique-selectors/-/postcss-unique-selectors-2.0.2.tgz
Source43: http://registry.npmjs.org/postcss-zindex/-/postcss-zindex-2.1.1.tgz
Source44: http://registry.npmjs.org/postcss-value-parser/-/postcss-value-parser-3.3.0.tgz
Source45: http://registry.npmjs.org/supports-color/-/supports-color-3.1.2.tgz
Source46: http://registry.npmjs.org/js-base64/-/js-base64-2.1.9.tgz
Source47: http://registry.npmjs.org/source-map/-/source-map-0.5.6.tgz
Source48: http://registry.npmjs.org/icss-replace-symbols/-/icss-replace-symbols-1.0.2.tgz
Source49: http://registry.npmjs.org/big.js/-/big.js-3.1.3.tgz
Source50: http://registry.npmjs.org/lodash.deburr/-/lodash.deburr-3.2.0.tgz
Source51: http://registry.npmjs.org/function-bind/-/function-bind-1.1.0.tgz
Source52: http://registry.npmjs.org/lodash.words/-/lodash.words-3.2.0.tgz
Source53: http://registry.npmjs.org/postcss-message-helpers/-/postcss-message-helpers-2.0.0.tgz
Source54: http://registry.npmjs.org/json5/-/json5-0.5.0.tgz
Source55: http://registry.npmjs.org/reduce-css-calc/-/reduce-css-calc-1.3.0.tgz
Source56: http://registry.npmjs.org/colormin/-/colormin-1.1.2.tgz
Source57: http://registry.npmjs.org/autoprefixer/-/autoprefixer-6.4.0.tgz
Source58: http://registry.npmjs.org/uniqid/-/uniqid-3.1.0.tgz
Source59: http://registry.npmjs.org/vendors/-/vendors-1.0.1.tgz
Source60: http://registry.npmjs.org/flatten/-/flatten-1.0.2.tgz
Source61: http://registry.npmjs.org/uniqs/-/uniqs-2.0.0.tgz
Source62: http://registry.npmjs.org/alphanum-sort/-/alphanum-sort-1.0.2.tgz
Source63: http://registry.npmjs.org/emojis-list/-/emojis-list-2.0.1.tgz
Source64: http://registry.npmjs.org/regexpu-core/-/regexpu-core-1.0.0.tgz
Source65: http://registry.npmjs.org/is-absolute-url/-/is-absolute-url-2.0.0.tgz
Source66: http://registry.npmjs.org/normalize-url/-/normalize-url-1.6.0.tgz
Source67: http://registry.npmjs.org/postcss-selector-parser/-/postcss-selector-parser-2.2.1.tgz
Source68: http://registry.npmjs.org/is-svg/-/is-svg-2.0.1.tgz
Source69: http://registry.npmjs.org/svgo/-/svgo-0.6.6.tgz
Source70: http://registry.npmjs.org/balanced-match/-/balanced-match-0.4.2.tgz
Source71: http://registry.npmjs.org/reduce-function-call/-/reduce-function-call-1.0.1.tgz
Source72: http://registry.npmjs.org/math-expression-evaluator/-/math-expression-evaluator-1.2.14.tgz
Source73: http://registry.npmjs.org/has-flag/-/has-flag-1.0.0.tgz
Source74: http://registry.npmjs.org/lodash._root/-/lodash._root-3.0.1.tgz
Source75: http://registry.npmjs.org/color/-/color-0.11.3.tgz
Source76: http://registry.npmjs.org/normalize-range/-/normalize-range-0.1.2.tgz
Source77: http://registry.npmjs.org/css-color-names/-/css-color-names-0.0.4.tgz
Source78: http://registry.npmjs.org/num2fraction/-/num2fraction-1.2.2.tgz
Source79: http://registry.npmjs.org/browserslist/-/browserslist-1.3.6.tgz
Source80: http://registry.npmjs.org/macaddress/-/macaddress-0.2.8.tgz
Source81: http://registry.npmjs.org/regenerate/-/regenerate-1.3.1.tgz
Source82: http://registry.npmjs.org/caniuse-db/-/caniuse-db-1.0.30000527.tgz
Source83: http://registry.npmjs.org/query-string/-/query-string-4.2.3.tgz
Source84: http://registry.npmjs.org/regjsgen/-/regjsgen-0.2.0.tgz
Source85: http://registry.npmjs.org/regjsparser/-/regjsparser-0.1.5.tgz
Source86: http://registry.npmjs.org/sort-keys/-/sort-keys-1.1.2.tgz
Source87: http://registry.npmjs.org/indexes-of/-/indexes-of-1.0.1.tgz
Source88: http://registry.npmjs.org/html-comment-regex/-/html-comment-regex-1.1.1.tgz
Source89: http://registry.npmjs.org/uniq/-/uniq-1.0.1.tgz
Source90: http://registry.npmjs.org/coa/-/coa-1.0.1.tgz
Source91: http://registry.npmjs.org/prepend-http/-/prepend-http-1.0.4.tgz
Source92: http://registry.npmjs.org/whet.extend/-/whet.extend-0.9.9.tgz
Source93: http://registry.npmjs.org/colors/-/colors-1.1.2.tgz
Source94: http://registry.npmjs.org/js-yaml/-/js-yaml-3.6.1.tgz
Source95: http://registry.npmjs.org/mkdirp/-/mkdirp-0.5.1.tgz
Source96: http://registry.npmjs.org/lodash.indexof/-/lodash.indexof-4.0.5.tgz
Source97: http://registry.npmjs.org/balanced-match/-/balanced-match-0.1.0.tgz
Source98: http://registry.npmjs.org/csso/-/csso-2.0.0.tgz
Source99: http://registry.npmjs.org/color-convert/-/color-convert-1.4.0.tgz
Source100: http://registry.npmjs.org/color-string/-/color-string-0.3.0.tgz
Source101: http://registry.npmjs.org/strict-uri-encode/-/strict-uri-encode-1.1.0.tgz
Source102: http://registry.npmjs.org/is-plain-obj/-/is-plain-obj-1.1.0.tgz
Source103: http://registry.npmjs.org/jsesc/-/jsesc-0.5.0.tgz
Source104: http://registry.npmjs.org/clone/-/clone-1.0.2.tgz
Source105: http://registry.npmjs.org/q/-/q-1.4.1.tgz
Source106: http://registry.npmjs.org/esprima/-/esprima-2.7.3.tgz
Source107: http://registry.npmjs.org/argparse/-/argparse-1.0.7.tgz
Source108: http://registry.npmjs.org/clap/-/clap-1.1.1.tgz
Source109: http://registry.npmjs.org/color-name/-/color-name-1.1.1.tgz
Source110: http://registry.npmjs.org/sprintf-js/-/sprintf-js-1.0.3.tgz
Source111: http://registry.npmjs.org/chalk/-/chalk-1.1.3.tgz
Source112: http://registry.npmjs.org/sax/-/sax-1.2.1.tgz
Source113: http://registry.npmjs.org/escape-string-regexp/-/escape-string-regexp-1.0.5.tgz
Source114: http://registry.npmjs.org/has-ansi/-/has-ansi-2.0.0.tgz
Source115: http://registry.npmjs.org/ansi-styles/-/ansi-styles-2.2.1.tgz
Source116: http://registry.npmjs.org/strip-ansi/-/strip-ansi-3.0.1.tgz
Source117: http://registry.npmjs.org/supports-color/-/supports-color-2.0.0.tgz
Source118: http://registry.npmjs.org/ansi-regex/-/ansi-regex-2.0.0.tgz
Source119: http://registry.npmjs.org/minimist/-/minimist-0.0.8.tgz
Source120: css-loader-0.23.1-registry.npmjs.org.tgz
Requires: nodejs(engine)
BuildRequires: nodejs-packaging
BuildRequires: npm
BuildArch:  noarch

%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

Provides: npm(%{npm_name}) = %{version}
Provides: bundled-npm(css-loader) = 0.23.1
Provides: bundled-npm(object-assign) = 4.1.0
Provides: bundled-npm(postcss-modules-extract-imports) = 1.0.1
Provides: bundled-npm(postcss-modules-local-by-default) = 1.1.1
Provides: bundled-npm(lodash.camelcase) = 3.0.1
Provides: bundled-npm(css-selector-tokenizer) = 0.5.4
Provides: bundled-npm(cssnano) = 3.7.4
Provides: bundled-npm(postcss) = 5.1.2
Provides: bundled-npm(source-list-map) = 0.1.6
Provides: bundled-npm(postcss-modules-scope) = 1.0.2
Provides: bundled-npm(css-selector-tokenizer) = 0.6.0
Provides: bundled-npm(loader-utils) = 0.2.15
Provides: bundled-npm(postcss-modules-values) = 1.2.2
Provides: bundled-npm(lodash._createcompounder) = 3.0.0
Provides: bundled-npm(cssesc) = 0.1.0
Provides: bundled-npm(decamelize) = 1.2.0
Provides: bundled-npm(fastparse) = 1.1.1
Provides: bundled-npm(has) = 1.0.1
Provides: bundled-npm(defined) = 1.0.0
Provides: bundled-npm(postcss-calc) = 5.3.1
Provides: bundled-npm(postcss-colormin) = 2.2.0
Provides: bundled-npm(postcss-discard-duplicates) = 2.0.1
Provides: bundled-npm(postcss-discard-comments) = 2.0.4
Provides: bundled-npm(postcss-convert-values) = 2.4.0
Provides: bundled-npm(postcss-discard-empty) = 2.1.0
Provides: bundled-npm(postcss-discard-overridden) = 0.1.1
Provides: bundled-npm(postcss-merge-longhand) = 2.0.1
Provides: bundled-npm(postcss-filter-plugins) = 2.0.1
Provides: bundled-npm(postcss-minify-font-values) = 1.0.5
Provides: bundled-npm(postcss-merge-idents) = 2.1.7
Provides: bundled-npm(postcss-merge-rules) = 2.0.10
Provides: bundled-npm(postcss-discard-unused) = 2.2.1
Provides: bundled-npm(postcss-minify-gradients) = 1.0.3
Provides: bundled-npm(postcss-minify-params) = 1.0.5
Provides: bundled-npm(postcss-normalize-charset) = 1.1.0
Provides: bundled-npm(postcss-normalize-url) = 3.0.7
Provides: bundled-npm(postcss-minify-selectors) = 2.0.5
Provides: bundled-npm(postcss-reduce-initial) = 1.0.0
Provides: bundled-npm(postcss-reduce-idents) = 2.3.0
Provides: bundled-npm(postcss-ordered-values) = 2.2.1
Provides: bundled-npm(postcss-reduce-transforms) = 1.0.3
Provides: bundled-npm(postcss-svgo) = 2.1.4
Provides: bundled-npm(postcss-unique-selectors) = 2.0.2
Provides: bundled-npm(postcss-zindex) = 2.1.1
Provides: bundled-npm(postcss-value-parser) = 3.3.0
Provides: bundled-npm(supports-color) = 3.1.2
Provides: bundled-npm(js-base64) = 2.1.9
Provides: bundled-npm(source-map) = 0.5.6
Provides: bundled-npm(icss-replace-symbols) = 1.0.2
Provides: bundled-npm(big.js) = 3.1.3
Provides: bundled-npm(lodash.deburr) = 3.2.0
Provides: bundled-npm(function-bind) = 1.1.0
Provides: bundled-npm(lodash.words) = 3.2.0
Provides: bundled-npm(postcss-message-helpers) = 2.0.0
Provides: bundled-npm(json5) = 0.5.0
Provides: bundled-npm(reduce-css-calc) = 1.3.0
Provides: bundled-npm(colormin) = 1.1.2
Provides: bundled-npm(autoprefixer) = 6.4.0
Provides: bundled-npm(uniqid) = 3.1.0
Provides: bundled-npm(vendors) = 1.0.1
Provides: bundled-npm(flatten) = 1.0.2
Provides: bundled-npm(uniqs) = 2.0.0
Provides: bundled-npm(alphanum-sort) = 1.0.2
Provides: bundled-npm(emojis-list) = 2.0.1
Provides: bundled-npm(regexpu-core) = 1.0.0
Provides: bundled-npm(is-absolute-url) = 2.0.0
Provides: bundled-npm(normalize-url) = 1.6.0
Provides: bundled-npm(postcss-selector-parser) = 2.2.1
Provides: bundled-npm(is-svg) = 2.0.1
Provides: bundled-npm(svgo) = 0.6.6
Provides: bundled-npm(balanced-match) = 0.4.2
Provides: bundled-npm(reduce-function-call) = 1.0.1
Provides: bundled-npm(math-expression-evaluator) = 1.2.14
Provides: bundled-npm(has-flag) = 1.0.0
Provides: bundled-npm(lodash._root) = 3.0.1
Provides: bundled-npm(color) = 0.11.3
Provides: bundled-npm(normalize-range) = 0.1.2
Provides: bundled-npm(css-color-names) = 0.0.4
Provides: bundled-npm(num2fraction) = 1.2.2
Provides: bundled-npm(browserslist) = 1.3.6
Provides: bundled-npm(macaddress) = 0.2.8
Provides: bundled-npm(regenerate) = 1.3.1
Provides: bundled-npm(caniuse-db) = 1.0.30000527
Provides: bundled-npm(query-string) = 4.2.3
Provides: bundled-npm(regjsgen) = 0.2.0
Provides: bundled-npm(regjsparser) = 0.1.5
Provides: bundled-npm(sort-keys) = 1.1.2
Provides: bundled-npm(indexes-of) = 1.0.1
Provides: bundled-npm(html-comment-regex) = 1.1.1
Provides: bundled-npm(uniq) = 1.0.1
Provides: bundled-npm(coa) = 1.0.1
Provides: bundled-npm(prepend-http) = 1.0.4
Provides: bundled-npm(whet.extend) = 0.9.9
Provides: bundled-npm(colors) = 1.1.2
Provides: bundled-npm(js-yaml) = 3.6.1
Provides: bundled-npm(mkdirp) = 0.5.1
Provides: bundled-npm(lodash.indexof) = 4.0.5
Provides: bundled-npm(balanced-match) = 0.1.0
Provides: bundled-npm(csso) = 2.0.0
Provides: bundled-npm(color-convert) = 1.4.0
Provides: bundled-npm(color-string) = 0.3.0
Provides: bundled-npm(strict-uri-encode) = 1.1.0
Provides: bundled-npm(is-plain-obj) = 1.1.0
Provides: bundled-npm(jsesc) = 0.5.0
Provides: bundled-npm(clone) = 1.0.2
Provides: bundled-npm(q) = 1.4.1
Provides: bundled-npm(esprima) = 2.7.3
Provides: bundled-npm(argparse) = 1.0.7
Provides: bundled-npm(clap) = 1.1.1
Provides: bundled-npm(color-name) = 1.1.1
Provides: bundled-npm(sprintf-js) = 1.0.3
Provides: bundled-npm(chalk) = 1.1.3
Provides: bundled-npm(sax) = 1.2.1
Provides: bundled-npm(escape-string-regexp) = 1.0.5
Provides: bundled-npm(has-ansi) = 2.0.0
Provides: bundled-npm(ansi-styles) = 2.2.1
Provides: bundled-npm(strip-ansi) = 3.0.1
Provides: bundled-npm(supports-color) = 2.0.0
Provides: bundled-npm(ansi-regex) = 2.0.0
Provides: bundled-npm(minimist) = 0.0.8
AutoReq: no
AutoProv: no

%description
%{summary}

%prep
mkdir npm_cache
for tgz in %{sources}; do
  echo $tgz | grep -q registry.npmjs.org || npm cache add --cache ./npm_cache $tgz
done

%setup -T -q -a 120 -D -n npm_cache

%build
npm install --cache-min Infinity --cache . --global-style true %{npm_name}@%{version}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cd node_modules/css-loader
cp -pfr .eslintrc .npmignore .travis.yml README.md index.js lib locals.js package.json node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr README.md ../../

%files
%{nodejs_sitelib}/%{npm_name}
%doc README.md

%changelog
* Thu Sep 01 2016 Dominic Cleal <dominic@cleal.org> 0.23.1-1
- new package built with tito

