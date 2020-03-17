%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name css-loader

Name: %{?scl_prefix}nodejs-css-loader
Version: 0.23.1
Release: 5%{?dist}
Summary: css loader module for webpack
License: MIT
Group: Development/Libraries
URL: https://github.com/webpack/css-loader#readme
Source0: https://registry.npmjs.org/alphanum-sort/-/alphanum-sort-1.0.2.tgz
Source1: https://registry.npmjs.org/ansi-regex/-/ansi-regex-2.1.1.tgz
Source2: https://registry.npmjs.org/ansi-styles/-/ansi-styles-2.2.1.tgz
Source3: https://registry.npmjs.org/ansi-styles/-/ansi-styles-3.2.1.tgz
Source4: https://registry.npmjs.org/argparse/-/argparse-1.0.10.tgz
Source5: https://registry.npmjs.org/autoprefixer/-/autoprefixer-6.7.7.tgz
Source6: https://registry.npmjs.org/balanced-match/-/balanced-match-0.4.2.tgz
Source7: https://registry.npmjs.org/balanced-match/-/balanced-match-1.0.0.tgz
Source8: https://registry.npmjs.org/big.js/-/big.js-3.2.0.tgz
Source9: https://registry.npmjs.org/browserslist/-/browserslist-1.7.7.tgz
Source10: https://registry.npmjs.org/caniuse-api/-/caniuse-api-1.6.1.tgz
Source11: https://registry.npmjs.org/caniuse-db/-/caniuse-db-1.0.30000998.tgz
Source12: https://registry.npmjs.org/chalk/-/chalk-1.1.3.tgz
Source13: https://registry.npmjs.org/chalk/-/chalk-2.4.2.tgz
Source14: https://registry.npmjs.org/clap/-/clap-1.2.3.tgz
Source15: https://registry.npmjs.org/clone/-/clone-1.0.4.tgz
Source16: https://registry.npmjs.org/coa/-/coa-1.0.4.tgz
Source17: https://registry.npmjs.org/color/-/color-0.11.4.tgz
Source18: https://registry.npmjs.org/color-convert/-/color-convert-1.9.3.tgz
Source19: https://registry.npmjs.org/color-name/-/color-name-1.1.3.tgz
Source20: https://registry.npmjs.org/color-name/-/color-name-1.1.4.tgz
Source21: https://registry.npmjs.org/color-string/-/color-string-0.3.0.tgz
Source22: https://registry.npmjs.org/colormin/-/colormin-1.1.2.tgz
Source23: https://registry.npmjs.org/colors/-/colors-1.1.2.tgz
Source24: https://registry.npmjs.org/css-color-names/-/css-color-names-0.0.4.tgz
Source25: https://registry.npmjs.org/css-loader/-/css-loader-0.23.1.tgz
Source26: https://registry.npmjs.org/css-selector-tokenizer/-/css-selector-tokenizer-0.5.4.tgz
Source27: https://registry.npmjs.org/css-selector-tokenizer/-/css-selector-tokenizer-0.7.1.tgz
Source28: https://registry.npmjs.org/cssesc/-/cssesc-0.1.0.tgz
Source29: https://registry.npmjs.org/cssnano/-/cssnano-3.10.0.tgz
Source30: https://registry.npmjs.org/csso/-/csso-2.3.2.tgz
Source31: https://registry.npmjs.org/decamelize/-/decamelize-1.2.0.tgz
Source32: https://registry.npmjs.org/defined/-/defined-1.0.0.tgz
Source33: https://registry.npmjs.org/electron-to-chromium/-/electron-to-chromium-1.3.273.tgz
Source34: https://registry.npmjs.org/emojis-list/-/emojis-list-2.1.0.tgz
Source35: https://registry.npmjs.org/escape-string-regexp/-/escape-string-regexp-1.0.5.tgz
Source36: https://registry.npmjs.org/esprima/-/esprima-2.7.3.tgz
Source37: https://registry.npmjs.org/fastparse/-/fastparse-1.1.2.tgz
Source38: https://registry.npmjs.org/flatten/-/flatten-1.0.2.tgz
Source39: https://registry.npmjs.org/function-bind/-/function-bind-1.1.1.tgz
Source40: https://registry.npmjs.org/has/-/has-1.0.3.tgz
Source41: https://registry.npmjs.org/has-ansi/-/has-ansi-2.0.0.tgz
Source42: https://registry.npmjs.org/has-flag/-/has-flag-1.0.0.tgz
Source43: https://registry.npmjs.org/has-flag/-/has-flag-3.0.0.tgz
Source44: https://registry.npmjs.org/html-comment-regex/-/html-comment-regex-1.1.2.tgz
Source45: https://registry.npmjs.org/icss-replace-symbols/-/icss-replace-symbols-1.1.0.tgz
Source46: https://registry.npmjs.org/indexes-of/-/indexes-of-1.0.1.tgz
Source47: https://registry.npmjs.org/is-absolute-url/-/is-absolute-url-2.1.0.tgz
Source48: https://registry.npmjs.org/is-plain-obj/-/is-plain-obj-1.1.0.tgz
Source49: https://registry.npmjs.org/is-svg/-/is-svg-2.1.0.tgz
Source50: https://registry.npmjs.org/js-base64/-/js-base64-2.5.1.tgz
Source51: https://registry.npmjs.org/js-yaml/-/js-yaml-3.7.0.tgz
Source52: https://registry.npmjs.org/jsesc/-/jsesc-0.5.0.tgz
Source53: https://registry.npmjs.org/json5/-/json5-0.5.1.tgz
Source54: https://registry.npmjs.org/loader-utils/-/loader-utils-0.2.17.tgz
Source55: https://registry.npmjs.org/lodash._createcompounder/-/lodash._createcompounder-3.0.0.tgz
Source56: https://registry.npmjs.org/lodash._root/-/lodash._root-3.0.1.tgz
Source57: https://registry.npmjs.org/lodash.camelcase/-/lodash.camelcase-3.0.1.tgz
Source58: https://registry.npmjs.org/lodash.deburr/-/lodash.deburr-3.2.0.tgz
Source59: https://registry.npmjs.org/lodash.memoize/-/lodash.memoize-4.1.2.tgz
Source60: https://registry.npmjs.org/lodash.uniq/-/lodash.uniq-4.5.0.tgz
Source61: https://registry.npmjs.org/lodash.words/-/lodash.words-3.2.0.tgz
Source62: https://registry.npmjs.org/math-expression-evaluator/-/math-expression-evaluator-1.2.17.tgz
Source63: https://registry.npmjs.org/minimist/-/minimist-0.0.8.tgz
Source64: https://registry.npmjs.org/mkdirp/-/mkdirp-0.5.1.tgz
Source65: https://registry.npmjs.org/normalize-range/-/normalize-range-0.1.2.tgz
Source66: https://registry.npmjs.org/normalize-url/-/normalize-url-1.9.1.tgz
Source67: https://registry.npmjs.org/num2fraction/-/num2fraction-1.2.2.tgz
Source68: https://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz
Source69: https://registry.npmjs.org/postcss/-/postcss-5.2.18.tgz
Source70: https://registry.npmjs.org/postcss/-/postcss-6.0.23.tgz
Source71: https://registry.npmjs.org/postcss-calc/-/postcss-calc-5.3.1.tgz
Source72: https://registry.npmjs.org/postcss-colormin/-/postcss-colormin-2.2.2.tgz
Source73: https://registry.npmjs.org/postcss-convert-values/-/postcss-convert-values-2.6.1.tgz
Source74: https://registry.npmjs.org/postcss-discard-comments/-/postcss-discard-comments-2.0.4.tgz
Source75: https://registry.npmjs.org/postcss-discard-duplicates/-/postcss-discard-duplicates-2.1.0.tgz
Source76: https://registry.npmjs.org/postcss-discard-empty/-/postcss-discard-empty-2.1.0.tgz
Source77: https://registry.npmjs.org/postcss-discard-overridden/-/postcss-discard-overridden-0.1.1.tgz
Source78: https://registry.npmjs.org/postcss-discard-unused/-/postcss-discard-unused-2.2.3.tgz
Source79: https://registry.npmjs.org/postcss-filter-plugins/-/postcss-filter-plugins-2.0.3.tgz
Source80: https://registry.npmjs.org/postcss-merge-idents/-/postcss-merge-idents-2.1.7.tgz
Source81: https://registry.npmjs.org/postcss-merge-longhand/-/postcss-merge-longhand-2.0.2.tgz
Source82: https://registry.npmjs.org/postcss-merge-rules/-/postcss-merge-rules-2.1.2.tgz
Source83: https://registry.npmjs.org/postcss-message-helpers/-/postcss-message-helpers-2.0.0.tgz
Source84: https://registry.npmjs.org/postcss-minify-font-values/-/postcss-minify-font-values-1.0.5.tgz
Source85: https://registry.npmjs.org/postcss-minify-gradients/-/postcss-minify-gradients-1.0.5.tgz
Source86: https://registry.npmjs.org/postcss-minify-params/-/postcss-minify-params-1.2.2.tgz
Source87: https://registry.npmjs.org/postcss-minify-selectors/-/postcss-minify-selectors-2.1.1.tgz
Source88: https://registry.npmjs.org/postcss-modules-extract-imports/-/postcss-modules-extract-imports-1.2.1.tgz
Source89: https://registry.npmjs.org/postcss-modules-local-by-default/-/postcss-modules-local-by-default-1.2.0.tgz
Source90: https://registry.npmjs.org/postcss-modules-scope/-/postcss-modules-scope-1.1.0.tgz
Source91: https://registry.npmjs.org/postcss-modules-values/-/postcss-modules-values-1.3.0.tgz
Source92: https://registry.npmjs.org/postcss-normalize-charset/-/postcss-normalize-charset-1.1.1.tgz
Source93: https://registry.npmjs.org/postcss-normalize-url/-/postcss-normalize-url-3.0.8.tgz
Source94: https://registry.npmjs.org/postcss-ordered-values/-/postcss-ordered-values-2.2.3.tgz
Source95: https://registry.npmjs.org/postcss-reduce-idents/-/postcss-reduce-idents-2.4.0.tgz
Source96: https://registry.npmjs.org/postcss-reduce-initial/-/postcss-reduce-initial-1.0.1.tgz
Source97: https://registry.npmjs.org/postcss-reduce-transforms/-/postcss-reduce-transforms-1.0.4.tgz
Source98: https://registry.npmjs.org/postcss-selector-parser/-/postcss-selector-parser-2.2.3.tgz
Source99: https://registry.npmjs.org/postcss-svgo/-/postcss-svgo-2.1.6.tgz
Source100: https://registry.npmjs.org/postcss-unique-selectors/-/postcss-unique-selectors-2.0.2.tgz
Source101: https://registry.npmjs.org/postcss-value-parser/-/postcss-value-parser-3.3.1.tgz
Source102: https://registry.npmjs.org/postcss-zindex/-/postcss-zindex-2.2.0.tgz
Source103: https://registry.npmjs.org/prepend-http/-/prepend-http-1.0.4.tgz
Source104: https://registry.npmjs.org/q/-/q-1.5.1.tgz
Source105: https://registry.npmjs.org/query-string/-/query-string-4.3.4.tgz
Source106: https://registry.npmjs.org/reduce-css-calc/-/reduce-css-calc-1.3.0.tgz
Source107: https://registry.npmjs.org/reduce-function-call/-/reduce-function-call-1.0.3.tgz
Source108: https://registry.npmjs.org/regenerate/-/regenerate-1.4.0.tgz
Source109: https://registry.npmjs.org/regexpu-core/-/regexpu-core-1.0.0.tgz
Source110: https://registry.npmjs.org/regjsgen/-/regjsgen-0.2.0.tgz
Source111: https://registry.npmjs.org/regjsparser/-/regjsparser-0.1.5.tgz
Source112: https://registry.npmjs.org/sax/-/sax-1.2.4.tgz
Source113: https://registry.npmjs.org/sort-keys/-/sort-keys-1.1.2.tgz
Source114: https://registry.npmjs.org/source-list-map/-/source-list-map-0.1.8.tgz
Source115: https://registry.npmjs.org/source-map/-/source-map-0.5.7.tgz
Source116: https://registry.npmjs.org/source-map/-/source-map-0.6.1.tgz
Source117: https://registry.npmjs.org/sprintf-js/-/sprintf-js-1.0.3.tgz
Source118: https://registry.npmjs.org/strict-uri-encode/-/strict-uri-encode-1.1.0.tgz
Source119: https://registry.npmjs.org/strip-ansi/-/strip-ansi-3.0.1.tgz
Source120: https://registry.npmjs.org/supports-color/-/supports-color-2.0.0.tgz
Source121: https://registry.npmjs.org/supports-color/-/supports-color-3.2.3.tgz
Source122: https://registry.npmjs.org/supports-color/-/supports-color-5.5.0.tgz
Source123: https://registry.npmjs.org/svgo/-/svgo-0.7.2.tgz
Source124: https://registry.npmjs.org/uniq/-/uniq-1.0.1.tgz
Source125: https://registry.npmjs.org/uniqs/-/uniqs-2.0.0.tgz
Source126: https://registry.npmjs.org/vendors/-/vendors-1.0.3.tgz
Source127: https://registry.npmjs.org/whet.extend/-/whet.extend-0.9.9.tgz
Source128: nodejs-css-loader-%{version}-registry.npmjs.org.tgz
%if 0%{?scl:1}
BuildRequires: %{?scl_prefix_nodejs}npm
%else
BuildRequires: nodejs-packaging
BuildRequires: npm
%endif
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}
Provides: bundled(npm(alphanum-sort)) = 1.0.2
Provides: bundled(npm(ansi-regex)) = 2.1.1
Provides: bundled(npm(ansi-styles)) = 2.2.1
Provides: bundled(npm(ansi-styles)) = 3.2.1
Provides: bundled(npm(argparse)) = 1.0.10
Provides: bundled(npm(autoprefixer)) = 6.7.7
Provides: bundled(npm(balanced-match)) = 0.4.2
Provides: bundled(npm(balanced-match)) = 1.0.0
Provides: bundled(npm(big.js)) = 3.2.0
Provides: bundled(npm(browserslist)) = 1.7.7
Provides: bundled(npm(caniuse-api)) = 1.6.1
Provides: bundled(npm(caniuse-db)) = 1.0.30000998
Provides: bundled(npm(chalk)) = 1.1.3
Provides: bundled(npm(chalk)) = 2.4.2
Provides: bundled(npm(clap)) = 1.2.3
Provides: bundled(npm(clone)) = 1.0.4
Provides: bundled(npm(coa)) = 1.0.4
Provides: bundled(npm(color)) = 0.11.4
Provides: bundled(npm(color-convert)) = 1.9.3
Provides: bundled(npm(color-name)) = 1.1.3
Provides: bundled(npm(color-name)) = 1.1.4
Provides: bundled(npm(color-string)) = 0.3.0
Provides: bundled(npm(colormin)) = 1.1.2
Provides: bundled(npm(colors)) = 1.1.2
Provides: bundled(npm(css-color-names)) = 0.0.4
Provides: bundled(npm(css-loader)) = 0.23.1
Provides: bundled(npm(css-selector-tokenizer)) = 0.5.4
Provides: bundled(npm(css-selector-tokenizer)) = 0.7.1
Provides: bundled(npm(cssesc)) = 0.1.0
Provides: bundled(npm(cssnano)) = 3.10.0
Provides: bundled(npm(csso)) = 2.3.2
Provides: bundled(npm(decamelize)) = 1.2.0
Provides: bundled(npm(defined)) = 1.0.0
Provides: bundled(npm(electron-to-chromium)) = 1.3.273
Provides: bundled(npm(emojis-list)) = 2.1.0
Provides: bundled(npm(escape-string-regexp)) = 1.0.5
Provides: bundled(npm(esprima)) = 2.7.3
Provides: bundled(npm(fastparse)) = 1.1.2
Provides: bundled(npm(flatten)) = 1.0.2
Provides: bundled(npm(function-bind)) = 1.1.1
Provides: bundled(npm(has)) = 1.0.3
Provides: bundled(npm(has-ansi)) = 2.0.0
Provides: bundled(npm(has-flag)) = 1.0.0
Provides: bundled(npm(has-flag)) = 3.0.0
Provides: bundled(npm(html-comment-regex)) = 1.1.2
Provides: bundled(npm(icss-replace-symbols)) = 1.1.0
Provides: bundled(npm(indexes-of)) = 1.0.1
Provides: bundled(npm(is-absolute-url)) = 2.1.0
Provides: bundled(npm(is-plain-obj)) = 1.1.0
Provides: bundled(npm(is-svg)) = 2.1.0
Provides: bundled(npm(js-base64)) = 2.5.1
Provides: bundled(npm(js-yaml)) = 3.7.0
Provides: bundled(npm(jsesc)) = 0.5.0
Provides: bundled(npm(json5)) = 0.5.1
Provides: bundled(npm(loader-utils)) = 0.2.17
Provides: bundled(npm(lodash._createcompounder)) = 3.0.0
Provides: bundled(npm(lodash._root)) = 3.0.1
Provides: bundled(npm(lodash.camelcase)) = 3.0.1
Provides: bundled(npm(lodash.deburr)) = 3.2.0
Provides: bundled(npm(lodash.memoize)) = 4.1.2
Provides: bundled(npm(lodash.uniq)) = 4.5.0
Provides: bundled(npm(lodash.words)) = 3.2.0
Provides: bundled(npm(math-expression-evaluator)) = 1.2.17
Provides: bundled(npm(minimist)) = 0.0.8
Provides: bundled(npm(mkdirp)) = 0.5.1
Provides: bundled(npm(normalize-range)) = 0.1.2
Provides: bundled(npm(normalize-url)) = 1.9.1
Provides: bundled(npm(num2fraction)) = 1.2.2
Provides: bundled(npm(object-assign)) = 4.1.1
Provides: bundled(npm(postcss)) = 5.2.18
Provides: bundled(npm(postcss)) = 6.0.23
Provides: bundled(npm(postcss-calc)) = 5.3.1
Provides: bundled(npm(postcss-colormin)) = 2.2.2
Provides: bundled(npm(postcss-convert-values)) = 2.6.1
Provides: bundled(npm(postcss-discard-comments)) = 2.0.4
Provides: bundled(npm(postcss-discard-duplicates)) = 2.1.0
Provides: bundled(npm(postcss-discard-empty)) = 2.1.0
Provides: bundled(npm(postcss-discard-overridden)) = 0.1.1
Provides: bundled(npm(postcss-discard-unused)) = 2.2.3
Provides: bundled(npm(postcss-filter-plugins)) = 2.0.3
Provides: bundled(npm(postcss-merge-idents)) = 2.1.7
Provides: bundled(npm(postcss-merge-longhand)) = 2.0.2
Provides: bundled(npm(postcss-merge-rules)) = 2.1.2
Provides: bundled(npm(postcss-message-helpers)) = 2.0.0
Provides: bundled(npm(postcss-minify-font-values)) = 1.0.5
Provides: bundled(npm(postcss-minify-gradients)) = 1.0.5
Provides: bundled(npm(postcss-minify-params)) = 1.2.2
Provides: bundled(npm(postcss-minify-selectors)) = 2.1.1
Provides: bundled(npm(postcss-modules-extract-imports)) = 1.2.1
Provides: bundled(npm(postcss-modules-local-by-default)) = 1.2.0
Provides: bundled(npm(postcss-modules-scope)) = 1.1.0
Provides: bundled(npm(postcss-modules-values)) = 1.3.0
Provides: bundled(npm(postcss-normalize-charset)) = 1.1.1
Provides: bundled(npm(postcss-normalize-url)) = 3.0.8
Provides: bundled(npm(postcss-ordered-values)) = 2.2.3
Provides: bundled(npm(postcss-reduce-idents)) = 2.4.0
Provides: bundled(npm(postcss-reduce-initial)) = 1.0.1
Provides: bundled(npm(postcss-reduce-transforms)) = 1.0.4
Provides: bundled(npm(postcss-selector-parser)) = 2.2.3
Provides: bundled(npm(postcss-svgo)) = 2.1.6
Provides: bundled(npm(postcss-unique-selectors)) = 2.0.2
Provides: bundled(npm(postcss-value-parser)) = 3.3.1
Provides: bundled(npm(postcss-zindex)) = 2.2.0
Provides: bundled(npm(prepend-http)) = 1.0.4
Provides: bundled(npm(q)) = 1.5.1
Provides: bundled(npm(query-string)) = 4.3.4
Provides: bundled(npm(reduce-css-calc)) = 1.3.0
Provides: bundled(npm(reduce-function-call)) = 1.0.3
Provides: bundled(npm(regenerate)) = 1.4.0
Provides: bundled(npm(regexpu-core)) = 1.0.0
Provides: bundled(npm(regjsgen)) = 0.2.0
Provides: bundled(npm(regjsparser)) = 0.1.5
Provides: bundled(npm(sax)) = 1.2.4
Provides: bundled(npm(sort-keys)) = 1.1.2
Provides: bundled(npm(source-list-map)) = 0.1.8
Provides: bundled(npm(source-map)) = 0.5.7
Provides: bundled(npm(source-map)) = 0.6.1
Provides: bundled(npm(sprintf-js)) = 1.0.3
Provides: bundled(npm(strict-uri-encode)) = 1.1.0
Provides: bundled(npm(strip-ansi)) = 3.0.1
Provides: bundled(npm(supports-color)) = 2.0.0
Provides: bundled(npm(supports-color)) = 3.2.3
Provides: bundled(npm(supports-color)) = 5.5.0
Provides: bundled(npm(svgo)) = 0.7.2
Provides: bundled(npm(uniq)) = 1.0.1
Provides: bundled(npm(uniqs)) = 2.0.0
Provides: bundled(npm(vendors)) = 1.0.3
Provides: bundled(npm(whet.extend)) = 0.9.9
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

%setup -T -q -a 128 -D -n %{npm_cache_dir}

%build
%{?scl:scl enable %{?scl_nodejs} - << \end_of_scl}
npm install --cache-min Infinity --cache %{?scl:../}%{npm_cache_dir} --no-shrinkwrap --no-optional --global-style true %{npm_name}@%{version}
%{?scl:end_of_scl}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/index.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/lib %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/locals.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%doc node_modules/%{npm_name}/README.md

%changelog
* Tue Mar 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.23.1-5
- Bump packages to build for el8

* Mon Oct 21 2019 Eric D. Helms <ericdhelms@gmail.com> - 0.23.1-4
- Build for SCL

* Fri Oct 04 2019 Eric D. Helms <ericdhelms@gmail.com> - 0.23.1-3
- Update specs to handle SCL

* Thu Sep 01 2016 Dominic Cleal <dominic@cleal.org> 0.23.1-1
- new package built with tito
