%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name @theforeman/env

Name: %{?scl_prefix}nodejs-theforeman-env
Version: 3.8.0
Release: 1%{?dist}
Summary: Development environment for foreman core and plugins
License: MIT
Group: Development/Libraries
URL: https://github.com/theforeman/foreman-js#readme
Source0: https://registry.npmjs.org/@babel/code-frame/-/@babel/code-frame-7.5.5.tgz
Source1: https://registry.npmjs.org/@babel/core/-/@babel/core-7.7.5.tgz
Source2: https://registry.npmjs.org/@babel/generator/-/@babel/generator-7.7.4.tgz
Source3: https://registry.npmjs.org/@babel/helper-function-name/-/@babel/helper-function-name-7.7.4.tgz
Source4: https://registry.npmjs.org/@babel/helper-get-function-arity/-/@babel/helper-get-function-arity-7.7.4.tgz
Source5: https://registry.npmjs.org/@babel/helper-plugin-utils/-/@babel/helper-plugin-utils-7.0.0.tgz
Source6: https://registry.npmjs.org/@babel/helper-split-export-declaration/-/@babel/helper-split-export-declaration-7.7.4.tgz
Source7: https://registry.npmjs.org/@babel/helpers/-/@babel/helpers-7.7.4.tgz
Source8: https://registry.npmjs.org/@babel/highlight/-/@babel/highlight-7.5.0.tgz
Source9: https://registry.npmjs.org/@babel/parser/-/@babel/parser-7.7.5.tgz
Source10: https://registry.npmjs.org/@babel/plugin-syntax-object-rest-spread/-/@babel/plugin-syntax-object-rest-spread-7.7.4.tgz
Source11: https://registry.npmjs.org/@babel/template/-/@babel/template-7.7.4.tgz
Source12: https://registry.npmjs.org/@babel/traverse/-/@babel/traverse-7.7.4.tgz
Source13: https://registry.npmjs.org/@babel/types/-/@babel/types-7.7.4.tgz
Source14: https://registry.npmjs.org/@cnakazawa/watch/-/@cnakazawa/watch-1.0.3.tgz
Source15: https://registry.npmjs.org/@jest/console/-/@jest/console-24.9.0.tgz
Source16: https://registry.npmjs.org/@jest/core/-/@jest/core-24.9.0.tgz
Source17: https://registry.npmjs.org/@jest/environment/-/@jest/environment-24.9.0.tgz
Source18: https://registry.npmjs.org/@jest/fake-timers/-/@jest/fake-timers-24.9.0.tgz
Source19: https://registry.npmjs.org/@jest/reporters/-/@jest/reporters-24.9.0.tgz
Source20: https://registry.npmjs.org/@jest/source-map/-/@jest/source-map-24.9.0.tgz
Source21: https://registry.npmjs.org/@jest/test-result/-/@jest/test-result-24.9.0.tgz
Source22: https://registry.npmjs.org/@jest/test-sequencer/-/@jest/test-sequencer-24.9.0.tgz
Source23: https://registry.npmjs.org/@jest/transform/-/@jest/transform-24.9.0.tgz
Source24: https://registry.npmjs.org/@jest/types/-/@jest/types-24.9.0.tgz
Source25: https://registry.npmjs.org/@theforeman/env/-/@theforeman/env-3.8.0.tgz
Source26: https://registry.npmjs.org/@types/babel__core/-/@types/babel__core-7.1.3.tgz
Source27: https://registry.npmjs.org/@types/babel__generator/-/@types/babel__generator-7.6.1.tgz
Source28: https://registry.npmjs.org/@types/babel__template/-/@types/babel__template-7.0.2.tgz
Source29: https://registry.npmjs.org/@types/babel__traverse/-/@types/babel__traverse-7.0.8.tgz
Source30: https://registry.npmjs.org/@types/istanbul-lib-coverage/-/@types/istanbul-lib-coverage-2.0.1.tgz
Source31: https://registry.npmjs.org/@types/istanbul-lib-report/-/@types/istanbul-lib-report-1.1.1.tgz
Source32: https://registry.npmjs.org/@types/istanbul-reports/-/@types/istanbul-reports-1.1.1.tgz
Source33: https://registry.npmjs.org/@types/node/-/@types/node-12.12.18.tgz
Source34: https://registry.npmjs.org/@types/stack-utils/-/@types/stack-utils-1.0.1.tgz
Source35: https://registry.npmjs.org/@types/yargs/-/@types/yargs-13.0.3.tgz
Source36: https://registry.npmjs.org/@types/yargs-parser/-/@types/yargs-parser-13.1.0.tgz
Source37: https://registry.npmjs.org/abab/-/abab-2.0.3.tgz
Source38: https://registry.npmjs.org/abbrev/-/abbrev-1.1.1.tgz
Source39: https://registry.npmjs.org/acorn/-/acorn-5.7.3.tgz
Source40: https://registry.npmjs.org/acorn/-/acorn-6.4.0.tgz
Source41: https://registry.npmjs.org/acorn-globals/-/acorn-globals-4.3.4.tgz
Source42: https://registry.npmjs.org/acorn-walk/-/acorn-walk-6.2.0.tgz
Source43: https://registry.npmjs.org/airbnb-prop-types/-/airbnb-prop-types-2.15.0.tgz
Source44: https://registry.npmjs.org/ajv/-/ajv-6.10.2.tgz
Source45: https://registry.npmjs.org/ansi-escapes/-/ansi-escapes-3.2.0.tgz
Source46: https://registry.npmjs.org/ansi-regex/-/ansi-regex-2.1.1.tgz
Source47: https://registry.npmjs.org/ansi-regex/-/ansi-regex-3.0.0.tgz
Source48: https://registry.npmjs.org/ansi-regex/-/ansi-regex-4.1.0.tgz
Source49: https://registry.npmjs.org/ansi-styles/-/ansi-styles-3.2.1.tgz
Source50: https://registry.npmjs.org/anymatch/-/anymatch-2.0.0.tgz
Source51: https://registry.npmjs.org/aproba/-/aproba-1.2.0.tgz
Source52: https://registry.npmjs.org/are-we-there-yet/-/are-we-there-yet-1.1.5.tgz
Source53: https://registry.npmjs.org/arr-diff/-/arr-diff-4.0.0.tgz
Source54: https://registry.npmjs.org/arr-flatten/-/arr-flatten-1.1.0.tgz
Source55: https://registry.npmjs.org/arr-union/-/arr-union-3.1.0.tgz
Source56: https://registry.npmjs.org/array-equal/-/array-equal-1.0.0.tgz
Source57: https://registry.npmjs.org/array-filter/-/array-filter-1.0.0.tgz
Source58: https://registry.npmjs.org/array-unique/-/array-unique-0.3.2.tgz
Source59: https://registry.npmjs.org/array.prototype.find/-/array.prototype.find-2.1.0.tgz
Source60: https://registry.npmjs.org/array.prototype.flat/-/array.prototype.flat-1.2.3.tgz
Source61: https://registry.npmjs.org/asn1/-/asn1-0.2.4.tgz
Source62: https://registry.npmjs.org/assert-plus/-/assert-plus-1.0.0.tgz
Source63: https://registry.npmjs.org/assign-symbols/-/assign-symbols-1.0.0.tgz
Source64: https://registry.npmjs.org/astral-regex/-/astral-regex-1.0.0.tgz
Source65: https://registry.npmjs.org/async-limiter/-/async-limiter-1.0.1.tgz
Source66: https://registry.npmjs.org/asynckit/-/asynckit-0.4.0.tgz
Source67: https://registry.npmjs.org/atob/-/atob-2.1.2.tgz
Source68: https://registry.npmjs.org/aws-sign2/-/aws-sign2-0.7.0.tgz
Source69: https://registry.npmjs.org/aws4/-/aws4-1.9.0.tgz
Source70: https://registry.npmjs.org/babel-jest/-/babel-jest-24.9.0.tgz
Source71: https://registry.npmjs.org/babel-plugin-dynamic-import-node/-/babel-plugin-dynamic-import-node-2.3.0.tgz
Source72: https://registry.npmjs.org/babel-plugin-istanbul/-/babel-plugin-istanbul-5.2.0.tgz
Source73: https://registry.npmjs.org/babel-plugin-jest-hoist/-/babel-plugin-jest-hoist-24.9.0.tgz
Source74: https://registry.npmjs.org/babel-preset-jest/-/babel-preset-jest-24.9.0.tgz
Source75: https://registry.npmjs.org/balanced-match/-/balanced-match-1.0.0.tgz
Source76: https://registry.npmjs.org/base/-/base-0.11.2.tgz
Source77: https://registry.npmjs.org/bcrypt-pbkdf/-/bcrypt-pbkdf-1.0.2.tgz
Source78: https://registry.npmjs.org/bindings/-/bindings-1.5.0.tgz
Source79: https://registry.npmjs.org/boolbase/-/boolbase-1.0.0.tgz
Source80: https://registry.npmjs.org/brace-expansion/-/brace-expansion-1.1.11.tgz
Source81: https://registry.npmjs.org/braces/-/braces-2.3.2.tgz
Source82: https://registry.npmjs.org/browser-process-hrtime/-/browser-process-hrtime-0.1.3.tgz
Source83: https://registry.npmjs.org/browser-resolve/-/browser-resolve-1.11.3.tgz
Source84: https://registry.npmjs.org/bser/-/bser-2.1.1.tgz
Source85: https://registry.npmjs.org/buffer-from/-/buffer-from-1.1.1.tgz
Source86: https://registry.npmjs.org/cache-base/-/cache-base-1.0.1.tgz
Source87: https://registry.npmjs.org/callsites/-/callsites-3.1.0.tgz
Source88: https://registry.npmjs.org/camelcase/-/camelcase-5.3.1.tgz
Source89: https://registry.npmjs.org/capture-exit/-/capture-exit-2.0.0.tgz
Source90: https://registry.npmjs.org/caseless/-/caseless-0.12.0.tgz
Source91: https://registry.npmjs.org/chalk/-/chalk-2.4.2.tgz
Source92: https://registry.npmjs.org/cheerio/-/cheerio-1.0.0-rc.3.tgz
Source93: https://registry.npmjs.org/chownr/-/chownr-1.1.3.tgz
Source94: https://registry.npmjs.org/ci-info/-/ci-info-2.0.0.tgz
Source95: https://registry.npmjs.org/class-utils/-/class-utils-0.3.6.tgz
Source96: https://registry.npmjs.org/cliui/-/cliui-5.0.0.tgz
Source97: https://registry.npmjs.org/co/-/co-4.6.0.tgz
Source98: https://registry.npmjs.org/code-point-at/-/code-point-at-1.1.0.tgz
Source99: https://registry.npmjs.org/collection-visit/-/collection-visit-1.0.0.tgz
Source100: https://registry.npmjs.org/color-convert/-/color-convert-1.9.3.tgz
Source101: https://registry.npmjs.org/color-name/-/color-name-1.1.3.tgz
Source102: https://registry.npmjs.org/combined-stream/-/combined-stream-1.0.8.tgz
Source103: https://registry.npmjs.org/commander/-/commander-2.20.3.tgz
Source104: https://registry.npmjs.org/component-emitter/-/component-emitter-1.3.0.tgz
Source105: https://registry.npmjs.org/concat-map/-/concat-map-0.0.1.tgz
Source106: https://registry.npmjs.org/console-control-strings/-/console-control-strings-1.1.0.tgz
Source107: https://registry.npmjs.org/convert-source-map/-/convert-source-map-1.7.0.tgz
Source108: https://registry.npmjs.org/copy-descriptor/-/copy-descriptor-0.1.1.tgz
Source109: https://registry.npmjs.org/core-js/-/core-js-3.5.0.tgz
Source110: https://registry.npmjs.org/core-util-is/-/core-util-is-1.0.2.tgz
Source111: https://registry.npmjs.org/cross-spawn/-/cross-spawn-6.0.5.tgz
Source112: https://registry.npmjs.org/css-select/-/css-select-1.2.0.tgz
Source113: https://registry.npmjs.org/css-what/-/css-what-2.1.3.tgz
Source114: https://registry.npmjs.org/cssom/-/cssom-0.3.8.tgz
Source115: https://registry.npmjs.org/cssstyle/-/cssstyle-1.4.0.tgz
Source116: https://registry.npmjs.org/dashdash/-/dashdash-1.14.1.tgz
Source117: https://registry.npmjs.org/data-urls/-/data-urls-1.1.0.tgz
Source118: https://registry.npmjs.org/debug/-/debug-2.6.9.tgz
Source119: https://registry.npmjs.org/debug/-/debug-3.2.6.tgz
Source120: https://registry.npmjs.org/debug/-/debug-4.1.1.tgz
Source121: https://registry.npmjs.org/decamelize/-/decamelize-1.2.0.tgz
Source122: https://registry.npmjs.org/decode-uri-component/-/decode-uri-component-0.2.0.tgz
Source123: https://registry.npmjs.org/deep-extend/-/deep-extend-0.6.0.tgz
Source124: https://registry.npmjs.org/deep-is/-/deep-is-0.1.3.tgz
Source125: https://registry.npmjs.org/define-properties/-/define-properties-1.1.3.tgz
Source126: https://registry.npmjs.org/define-property/-/define-property-0.2.5.tgz
Source127: https://registry.npmjs.org/define-property/-/define-property-1.0.0.tgz
Source128: https://registry.npmjs.org/define-property/-/define-property-2.0.2.tgz
Source129: https://registry.npmjs.org/delayed-stream/-/delayed-stream-1.0.0.tgz
Source130: https://registry.npmjs.org/delegates/-/delegates-1.0.0.tgz
Source131: https://registry.npmjs.org/detect-libc/-/detect-libc-1.0.3.tgz
Source132: https://registry.npmjs.org/detect-newline/-/detect-newline-2.1.0.tgz
Source133: https://registry.npmjs.org/diff-sequences/-/diff-sequences-24.9.0.tgz
Source134: https://registry.npmjs.org/discontinuous-range/-/discontinuous-range-1.0.0.tgz
Source135: https://registry.npmjs.org/dom-serializer/-/dom-serializer-0.1.1.tgz
Source136: https://registry.npmjs.org/dom-serializer/-/dom-serializer-0.2.2.tgz
Source137: https://registry.npmjs.org/domelementtype/-/domelementtype-1.3.1.tgz
Source138: https://registry.npmjs.org/domelementtype/-/domelementtype-2.0.1.tgz
Source139: https://registry.npmjs.org/domexception/-/domexception-1.0.1.tgz
Source140: https://registry.npmjs.org/domhandler/-/domhandler-2.4.2.tgz
Source141: https://registry.npmjs.org/domutils/-/domutils-1.5.1.tgz
Source142: https://registry.npmjs.org/domutils/-/domutils-1.7.0.tgz
Source143: https://registry.npmjs.org/ecc-jsbn/-/ecc-jsbn-0.1.2.tgz
Source144: https://registry.npmjs.org/emoji-regex/-/emoji-regex-7.0.3.tgz
Source145: https://registry.npmjs.org/end-of-stream/-/end-of-stream-1.4.4.tgz
Source146: https://registry.npmjs.org/entities/-/entities-1.1.2.tgz
Source147: https://registry.npmjs.org/entities/-/entities-2.0.0.tgz
Source148: https://registry.npmjs.org/enzyme/-/enzyme-3.10.0.tgz
Source149: https://registry.npmjs.org/enzyme-adapter-react-16/-/enzyme-adapter-react-16-1.15.1.tgz
Source150: https://registry.npmjs.org/enzyme-adapter-utils/-/enzyme-adapter-utils-1.12.1.tgz
Source151: https://registry.npmjs.org/enzyme-shallow-equal/-/enzyme-shallow-equal-1.0.0.tgz
Source152: https://registry.npmjs.org/enzyme-to-json/-/enzyme-to-json-3.4.3.tgz
Source153: https://registry.npmjs.org/error-ex/-/error-ex-1.3.2.tgz
Source154: https://registry.npmjs.org/es-abstract/-/es-abstract-1.16.3.tgz
Source155: https://registry.npmjs.org/es-abstract/-/es-abstract-1.17.0-next.1.tgz
Source156: https://registry.npmjs.org/es-to-primitive/-/es-to-primitive-1.2.1.tgz
Source157: https://registry.npmjs.org/escape-string-regexp/-/escape-string-regexp-1.0.5.tgz
Source158: https://registry.npmjs.org/escodegen/-/escodegen-1.12.0.tgz
Source159: https://registry.npmjs.org/esprima/-/esprima-3.1.3.tgz
Source160: https://registry.npmjs.org/estraverse/-/estraverse-4.3.0.tgz
Source161: https://registry.npmjs.org/esutils/-/esutils-2.0.3.tgz
Source162: https://registry.npmjs.org/exec-sh/-/exec-sh-0.3.4.tgz
Source163: https://registry.npmjs.org/execa/-/execa-1.0.0.tgz
Source164: https://registry.npmjs.org/exit/-/exit-0.1.2.tgz
Source165: https://registry.npmjs.org/expand-brackets/-/expand-brackets-2.1.4.tgz
Source166: https://registry.npmjs.org/expect/-/expect-24.9.0.tgz
Source167: https://registry.npmjs.org/extend/-/extend-3.0.2.tgz
Source168: https://registry.npmjs.org/extend-shallow/-/extend-shallow-2.0.1.tgz
Source169: https://registry.npmjs.org/extend-shallow/-/extend-shallow-3.0.2.tgz
Source170: https://registry.npmjs.org/extglob/-/extglob-2.0.4.tgz
Source171: https://registry.npmjs.org/extsprintf/-/extsprintf-1.3.0.tgz
Source172: https://registry.npmjs.org/extsprintf/-/extsprintf-1.4.0.tgz
Source173: https://registry.npmjs.org/fast-deep-equal/-/fast-deep-equal-2.0.1.tgz
Source174: https://registry.npmjs.org/fast-json-stable-stringify/-/fast-json-stable-stringify-2.1.0.tgz
Source175: https://registry.npmjs.org/fast-levenshtein/-/fast-levenshtein-2.0.6.tgz
Source176: https://registry.npmjs.org/fb-watchman/-/fb-watchman-2.0.1.tgz
Source177: https://registry.npmjs.org/file-uri-to-path/-/file-uri-to-path-1.0.0.tgz
Source178: https://registry.npmjs.org/fill-range/-/fill-range-4.0.0.tgz
Source179: https://registry.npmjs.org/find-up/-/find-up-3.0.0.tgz
Source180: https://registry.npmjs.org/for-in/-/for-in-1.0.2.tgz
Source181: https://registry.npmjs.org/forever-agent/-/forever-agent-0.6.1.tgz
Source182: https://registry.npmjs.org/form-data/-/form-data-2.3.3.tgz
Source183: https://registry.npmjs.org/fragment-cache/-/fragment-cache-0.2.1.tgz
Source184: https://registry.npmjs.org/fs-minipass/-/fs-minipass-1.2.7.tgz
Source185: https://registry.npmjs.org/fs.realpath/-/fs.realpath-1.0.0.tgz
Source186: https://registry.npmjs.org/fsevents/-/fsevents-1.2.11.tgz
Source187: https://registry.npmjs.org/function-bind/-/function-bind-1.1.1.tgz
Source188: https://registry.npmjs.org/function.prototype.name/-/function.prototype.name-1.1.2.tgz
Source189: https://registry.npmjs.org/functions-have-names/-/functions-have-names-1.2.0.tgz
Source190: https://registry.npmjs.org/gauge/-/gauge-2.7.4.tgz
Source191: https://registry.npmjs.org/get-caller-file/-/get-caller-file-2.0.5.tgz
Source192: https://registry.npmjs.org/get-stream/-/get-stream-4.1.0.tgz
Source193: https://registry.npmjs.org/get-value/-/get-value-2.0.6.tgz
Source194: https://registry.npmjs.org/getpass/-/getpass-0.1.7.tgz
Source195: https://registry.npmjs.org/glob/-/glob-7.1.6.tgz
Source196: https://registry.npmjs.org/globals/-/globals-11.12.0.tgz
Source197: https://registry.npmjs.org/graceful-fs/-/graceful-fs-4.2.3.tgz
Source198: https://registry.npmjs.org/growly/-/growly-1.3.0.tgz
Source199: https://registry.npmjs.org/handlebars/-/handlebars-4.5.3.tgz
Source200: https://registry.npmjs.org/har-schema/-/har-schema-2.0.0.tgz
Source201: https://registry.npmjs.org/har-validator/-/har-validator-5.1.3.tgz
Source202: https://registry.npmjs.org/has/-/has-1.0.3.tgz
Source203: https://registry.npmjs.org/has-flag/-/has-flag-3.0.0.tgz
Source204: https://registry.npmjs.org/has-symbols/-/has-symbols-1.0.1.tgz
Source205: https://registry.npmjs.org/has-unicode/-/has-unicode-2.0.1.tgz
Source206: https://registry.npmjs.org/has-value/-/has-value-0.3.1.tgz
Source207: https://registry.npmjs.org/has-value/-/has-value-1.0.0.tgz
Source208: https://registry.npmjs.org/has-values/-/has-values-0.1.4.tgz
Source209: https://registry.npmjs.org/has-values/-/has-values-1.0.0.tgz
Source210: https://registry.npmjs.org/hosted-git-info/-/hosted-git-info-2.8.5.tgz
Source211: https://registry.npmjs.org/html-element-map/-/html-element-map-1.2.0.tgz
Source212: https://registry.npmjs.org/html-encoding-sniffer/-/html-encoding-sniffer-1.0.2.tgz
Source213: https://registry.npmjs.org/htmlparser2/-/htmlparser2-3.10.1.tgz
Source214: https://registry.npmjs.org/http-signature/-/http-signature-1.2.0.tgz
Source215: https://registry.npmjs.org/iconv-lite/-/iconv-lite-0.4.24.tgz
Source216: https://registry.npmjs.org/ignore-walk/-/ignore-walk-3.0.3.tgz
Source217: https://registry.npmjs.org/import-local/-/import-local-2.0.0.tgz
Source218: https://registry.npmjs.org/imurmurhash/-/imurmurhash-0.1.4.tgz
Source219: https://registry.npmjs.org/inflight/-/inflight-1.0.6.tgz
Source220: https://registry.npmjs.org/inherits/-/inherits-2.0.4.tgz
Source221: https://registry.npmjs.org/ini/-/ini-1.3.5.tgz
Source222: https://registry.npmjs.org/invariant/-/invariant-2.2.4.tgz
Source223: https://registry.npmjs.org/is-accessor-descriptor/-/is-accessor-descriptor-0.1.6.tgz
Source224: https://registry.npmjs.org/is-accessor-descriptor/-/is-accessor-descriptor-1.0.0.tgz
Source225: https://registry.npmjs.org/is-arrayish/-/is-arrayish-0.2.1.tgz
Source226: https://registry.npmjs.org/is-boolean-object/-/is-boolean-object-1.0.0.tgz
Source227: https://registry.npmjs.org/is-buffer/-/is-buffer-1.1.6.tgz
Source228: https://registry.npmjs.org/is-callable/-/is-callable-1.1.4.tgz
Source229: https://registry.npmjs.org/is-ci/-/is-ci-2.0.0.tgz
Source230: https://registry.npmjs.org/is-data-descriptor/-/is-data-descriptor-0.1.4.tgz
Source231: https://registry.npmjs.org/is-data-descriptor/-/is-data-descriptor-1.0.0.tgz
Source232: https://registry.npmjs.org/is-date-object/-/is-date-object-1.0.1.tgz
Source233: https://registry.npmjs.org/is-descriptor/-/is-descriptor-0.1.6.tgz
Source234: https://registry.npmjs.org/is-descriptor/-/is-descriptor-1.0.2.tgz
Source235: https://registry.npmjs.org/is-extendable/-/is-extendable-0.1.1.tgz
Source236: https://registry.npmjs.org/is-extendable/-/is-extendable-1.0.1.tgz
Source237: https://registry.npmjs.org/is-fullwidth-code-point/-/is-fullwidth-code-point-1.0.0.tgz
Source238: https://registry.npmjs.org/is-fullwidth-code-point/-/is-fullwidth-code-point-2.0.0.tgz
Source239: https://registry.npmjs.org/is-generator-fn/-/is-generator-fn-2.1.0.tgz
Source240: https://registry.npmjs.org/is-number/-/is-number-3.0.0.tgz
Source241: https://registry.npmjs.org/is-number-object/-/is-number-object-1.0.3.tgz
Source242: https://registry.npmjs.org/is-plain-object/-/is-plain-object-2.0.4.tgz
Source243: https://registry.npmjs.org/is-regex/-/is-regex-1.0.5.tgz
Source244: https://registry.npmjs.org/is-stream/-/is-stream-1.1.0.tgz
Source245: https://registry.npmjs.org/is-string/-/is-string-1.0.4.tgz
Source246: https://registry.npmjs.org/is-subset/-/is-subset-0.1.1.tgz
Source247: https://registry.npmjs.org/is-symbol/-/is-symbol-1.0.3.tgz
Source248: https://registry.npmjs.org/is-typedarray/-/is-typedarray-1.0.0.tgz
Source249: https://registry.npmjs.org/is-windows/-/is-windows-1.0.2.tgz
Source250: https://registry.npmjs.org/is-wsl/-/is-wsl-1.1.0.tgz
Source251: https://registry.npmjs.org/isarray/-/isarray-1.0.0.tgz
Source252: https://registry.npmjs.org/isexe/-/isexe-2.0.0.tgz
Source253: https://registry.npmjs.org/isobject/-/isobject-2.1.0.tgz
Source254: https://registry.npmjs.org/isobject/-/isobject-3.0.1.tgz
Source255: https://registry.npmjs.org/isstream/-/isstream-0.1.2.tgz
Source256: https://registry.npmjs.org/istanbul-lib-coverage/-/istanbul-lib-coverage-2.0.5.tgz
Source257: https://registry.npmjs.org/istanbul-lib-instrument/-/istanbul-lib-instrument-3.3.0.tgz
Source258: https://registry.npmjs.org/istanbul-lib-report/-/istanbul-lib-report-2.0.8.tgz
Source259: https://registry.npmjs.org/istanbul-lib-source-maps/-/istanbul-lib-source-maps-3.0.6.tgz
Source260: https://registry.npmjs.org/istanbul-reports/-/istanbul-reports-2.2.6.tgz
Source261: https://registry.npmjs.org/jest/-/jest-24.9.0.tgz
Source262: https://registry.npmjs.org/jest-changed-files/-/jest-changed-files-24.9.0.tgz
Source263: https://registry.npmjs.org/jest-cli/-/jest-cli-24.9.0.tgz
Source264: https://registry.npmjs.org/jest-config/-/jest-config-24.9.0.tgz
Source265: https://registry.npmjs.org/jest-diff/-/jest-diff-24.9.0.tgz
Source266: https://registry.npmjs.org/jest-docblock/-/jest-docblock-24.9.0.tgz
Source267: https://registry.npmjs.org/jest-each/-/jest-each-24.9.0.tgz
Source268: https://registry.npmjs.org/jest-environment-jsdom/-/jest-environment-jsdom-24.9.0.tgz
Source269: https://registry.npmjs.org/jest-environment-node/-/jest-environment-node-24.9.0.tgz
Source270: https://registry.npmjs.org/jest-get-type/-/jest-get-type-24.9.0.tgz
Source271: https://registry.npmjs.org/jest-haste-map/-/jest-haste-map-24.9.0.tgz
Source272: https://registry.npmjs.org/jest-jasmine2/-/jest-jasmine2-24.9.0.tgz
Source273: https://registry.npmjs.org/jest-leak-detector/-/jest-leak-detector-24.9.0.tgz
Source274: https://registry.npmjs.org/jest-matcher-utils/-/jest-matcher-utils-24.9.0.tgz
Source275: https://registry.npmjs.org/jest-message-util/-/jest-message-util-24.9.0.tgz
Source276: https://registry.npmjs.org/jest-mock/-/jest-mock-24.9.0.tgz
Source277: https://registry.npmjs.org/jest-pnp-resolver/-/jest-pnp-resolver-1.2.1.tgz
Source278: https://registry.npmjs.org/jest-prop-type-error/-/jest-prop-type-error-1.1.0.tgz
Source279: https://registry.npmjs.org/jest-regex-util/-/jest-regex-util-24.9.0.tgz
Source280: https://registry.npmjs.org/jest-resolve/-/jest-resolve-24.9.0.tgz
Source281: https://registry.npmjs.org/jest-resolve-dependencies/-/jest-resolve-dependencies-24.9.0.tgz
Source282: https://registry.npmjs.org/jest-runner/-/jest-runner-24.9.0.tgz
Source283: https://registry.npmjs.org/jest-runtime/-/jest-runtime-24.9.0.tgz
Source284: https://registry.npmjs.org/jest-serializer/-/jest-serializer-24.9.0.tgz
Source285: https://registry.npmjs.org/jest-snapshot/-/jest-snapshot-24.9.0.tgz
Source286: https://registry.npmjs.org/jest-util/-/jest-util-24.9.0.tgz
Source287: https://registry.npmjs.org/jest-validate/-/jest-validate-24.9.0.tgz
Source288: https://registry.npmjs.org/jest-watcher/-/jest-watcher-24.9.0.tgz
Source289: https://registry.npmjs.org/jest-worker/-/jest-worker-24.9.0.tgz
Source290: https://registry.npmjs.org/js-tokens/-/js-tokens-4.0.0.tgz
Source291: https://registry.npmjs.org/jsbn/-/jsbn-0.1.1.tgz
Source292: https://registry.npmjs.org/jsdom/-/jsdom-11.12.0.tgz
Source293: https://registry.npmjs.org/jsesc/-/jsesc-2.5.2.tgz
Source294: https://registry.npmjs.org/json-parse-better-errors/-/json-parse-better-errors-1.0.2.tgz
Source295: https://registry.npmjs.org/json-schema/-/json-schema-0.2.3.tgz
Source296: https://registry.npmjs.org/json-schema-traverse/-/json-schema-traverse-0.4.1.tgz
Source297: https://registry.npmjs.org/json-stringify-safe/-/json-stringify-safe-5.0.1.tgz
Source298: https://registry.npmjs.org/json5/-/json5-2.1.1.tgz
Source299: https://registry.npmjs.org/jsprim/-/jsprim-1.4.1.tgz
Source300: https://registry.npmjs.org/kind-of/-/kind-of-3.2.2.tgz
Source301: https://registry.npmjs.org/kind-of/-/kind-of-4.0.0.tgz
Source302: https://registry.npmjs.org/kind-of/-/kind-of-5.1.0.tgz
Source303: https://registry.npmjs.org/kind-of/-/kind-of-6.0.2.tgz
Source304: https://registry.npmjs.org/kleur/-/kleur-3.0.3.tgz
Source305: https://registry.npmjs.org/left-pad/-/left-pad-1.3.0.tgz
Source306: https://registry.npmjs.org/leven/-/leven-3.1.0.tgz
Source307: https://registry.npmjs.org/levn/-/levn-0.3.0.tgz
Source308: https://registry.npmjs.org/load-json-file/-/load-json-file-4.0.0.tgz
Source309: https://registry.npmjs.org/locate-path/-/locate-path-3.0.0.tgz
Source310: https://registry.npmjs.org/lodash/-/lodash-4.17.15.tgz
Source311: https://registry.npmjs.org/lodash.escape/-/lodash.escape-4.0.1.tgz
Source312: https://registry.npmjs.org/lodash.flattendeep/-/lodash.flattendeep-4.4.0.tgz
Source313: https://registry.npmjs.org/lodash.isequal/-/lodash.isequal-4.5.0.tgz
Source314: https://registry.npmjs.org/lodash.sortby/-/lodash.sortby-4.7.0.tgz
Source315: https://registry.npmjs.org/loose-envify/-/loose-envify-1.4.0.tgz
Source316: https://registry.npmjs.org/make-dir/-/make-dir-2.1.0.tgz
Source317: https://registry.npmjs.org/makeerror/-/makeerror-1.0.11.tgz
Source318: https://registry.npmjs.org/map-cache/-/map-cache-0.2.2.tgz
Source319: https://registry.npmjs.org/map-visit/-/map-visit-1.0.0.tgz
Source320: https://registry.npmjs.org/merge-stream/-/merge-stream-2.0.0.tgz
Source321: https://registry.npmjs.org/micromatch/-/micromatch-3.1.10.tgz
Source322: https://registry.npmjs.org/mime-db/-/mime-db-1.42.0.tgz
Source323: https://registry.npmjs.org/mime-types/-/mime-types-2.1.25.tgz
Source324: https://registry.npmjs.org/minimatch/-/minimatch-3.0.4.tgz
Source325: https://registry.npmjs.org/minimist/-/minimist-0.0.10.tgz
Source326: https://registry.npmjs.org/minimist/-/minimist-0.0.8.tgz
Source327: https://registry.npmjs.org/minimist/-/minimist-1.2.0.tgz
Source328: https://registry.npmjs.org/minipass/-/minipass-2.9.0.tgz
Source329: https://registry.npmjs.org/minizlib/-/minizlib-1.3.3.tgz
Source330: https://registry.npmjs.org/mixin-deep/-/mixin-deep-1.3.2.tgz
Source331: https://registry.npmjs.org/mkdirp/-/mkdirp-0.5.1.tgz
Source332: https://registry.npmjs.org/moo/-/moo-0.4.3.tgz
Source333: https://registry.npmjs.org/ms/-/ms-2.0.0.tgz
Source334: https://registry.npmjs.org/ms/-/ms-2.1.2.tgz
Source335: https://registry.npmjs.org/nan/-/nan-2.14.0.tgz
Source336: https://registry.npmjs.org/nanomatch/-/nanomatch-1.2.13.tgz
Source337: https://registry.npmjs.org/natural-compare/-/natural-compare-1.4.0.tgz
Source338: https://registry.npmjs.org/nearley/-/nearley-2.19.0.tgz
Source339: https://registry.npmjs.org/needle/-/needle-2.4.0.tgz
Source340: https://registry.npmjs.org/neo-async/-/neo-async-2.6.1.tgz
Source341: https://registry.npmjs.org/nice-try/-/nice-try-1.0.5.tgz
Source342: https://registry.npmjs.org/node-int64/-/node-int64-0.4.0.tgz
Source343: https://registry.npmjs.org/node-modules-regexp/-/node-modules-regexp-1.0.0.tgz
Source344: https://registry.npmjs.org/node-notifier/-/node-notifier-5.4.3.tgz
Source345: https://registry.npmjs.org/node-pre-gyp/-/node-pre-gyp-0.14.0.tgz
Source346: https://registry.npmjs.org/nopt/-/nopt-4.0.1.tgz
Source347: https://registry.npmjs.org/normalize-package-data/-/normalize-package-data-2.5.0.tgz
Source348: https://registry.npmjs.org/normalize-path/-/normalize-path-2.1.1.tgz
Source349: https://registry.npmjs.org/npm-bundled/-/npm-bundled-1.1.1.tgz
Source350: https://registry.npmjs.org/npm-normalize-package-bin/-/npm-normalize-package-bin-1.0.1.tgz
Source351: https://registry.npmjs.org/npm-packlist/-/npm-packlist-1.4.7.tgz
Source352: https://registry.npmjs.org/npm-run-path/-/npm-run-path-2.0.2.tgz
Source353: https://registry.npmjs.org/npmlog/-/npmlog-4.1.2.tgz
Source354: https://registry.npmjs.org/nth-check/-/nth-check-1.0.2.tgz
Source355: https://registry.npmjs.org/number-is-nan/-/number-is-nan-1.0.1.tgz
Source356: https://registry.npmjs.org/nwsapi/-/nwsapi-2.2.0.tgz
Source357: https://registry.npmjs.org/oauth-sign/-/oauth-sign-0.9.0.tgz
Source358: https://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz
Source359: https://registry.npmjs.org/object-copy/-/object-copy-0.1.0.tgz
Source360: https://registry.npmjs.org/object-inspect/-/object-inspect-1.7.0.tgz
Source361: https://registry.npmjs.org/object-is/-/object-is-1.0.2.tgz
Source362: https://registry.npmjs.org/object-keys/-/object-keys-1.1.1.tgz
Source363: https://registry.npmjs.org/object-visit/-/object-visit-1.0.1.tgz
Source364: https://registry.npmjs.org/object.assign/-/object.assign-4.1.0.tgz
Source365: https://registry.npmjs.org/object.entries/-/object.entries-1.1.1.tgz
Source366: https://registry.npmjs.org/object.fromentries/-/object.fromentries-2.0.2.tgz
Source367: https://registry.npmjs.org/object.getownpropertydescriptors/-/object.getownpropertydescriptors-2.1.0.tgz
Source368: https://registry.npmjs.org/object.pick/-/object.pick-1.3.0.tgz
Source369: https://registry.npmjs.org/object.values/-/object.values-1.1.1.tgz
Source370: https://registry.npmjs.org/once/-/once-1.4.0.tgz
Source371: https://registry.npmjs.org/optimist/-/optimist-0.6.1.tgz
Source372: https://registry.npmjs.org/optionator/-/optionator-0.8.3.tgz
Source373: https://registry.npmjs.org/os-homedir/-/os-homedir-1.0.2.tgz
Source374: https://registry.npmjs.org/os-tmpdir/-/os-tmpdir-1.0.2.tgz
Source375: https://registry.npmjs.org/osenv/-/osenv-0.1.5.tgz
Source376: https://registry.npmjs.org/p-each-series/-/p-each-series-1.0.0.tgz
Source377: https://registry.npmjs.org/p-finally/-/p-finally-1.0.0.tgz
Source378: https://registry.npmjs.org/p-limit/-/p-limit-2.2.1.tgz
Source379: https://registry.npmjs.org/p-locate/-/p-locate-3.0.0.tgz
Source380: https://registry.npmjs.org/p-reduce/-/p-reduce-1.0.0.tgz
Source381: https://registry.npmjs.org/p-try/-/p-try-2.2.0.tgz
Source382: https://registry.npmjs.org/parse-json/-/parse-json-4.0.0.tgz
Source383: https://registry.npmjs.org/parse5/-/parse5-3.0.3.tgz
Source384: https://registry.npmjs.org/parse5/-/parse5-4.0.0.tgz
Source385: https://registry.npmjs.org/pascalcase/-/pascalcase-0.1.1.tgz
Source386: https://registry.npmjs.org/path-exists/-/path-exists-3.0.0.tgz
Source387: https://registry.npmjs.org/path-is-absolute/-/path-is-absolute-1.0.1.tgz
Source388: https://registry.npmjs.org/path-key/-/path-key-2.0.1.tgz
Source389: https://registry.npmjs.org/path-parse/-/path-parse-1.0.6.tgz
Source390: https://registry.npmjs.org/path-type/-/path-type-3.0.0.tgz
Source391: https://registry.npmjs.org/performance-now/-/performance-now-2.1.0.tgz
Source392: https://registry.npmjs.org/pify/-/pify-3.0.0.tgz
Source393: https://registry.npmjs.org/pify/-/pify-4.0.1.tgz
Source394: https://registry.npmjs.org/pirates/-/pirates-4.0.1.tgz
Source395: https://registry.npmjs.org/pkg-dir/-/pkg-dir-3.0.0.tgz
Source396: https://registry.npmjs.org/pn/-/pn-1.1.0.tgz
Source397: https://registry.npmjs.org/posix-character-classes/-/posix-character-classes-0.1.1.tgz
Source398: https://registry.npmjs.org/prelude-ls/-/prelude-ls-1.1.2.tgz
Source399: https://registry.npmjs.org/pretty-format/-/pretty-format-24.9.0.tgz
Source400: https://registry.npmjs.org/process-nextick-args/-/process-nextick-args-2.0.1.tgz
Source401: https://registry.npmjs.org/prompts/-/prompts-2.3.0.tgz
Source402: https://registry.npmjs.org/prop-types/-/prop-types-15.7.2.tgz
Source403: https://registry.npmjs.org/prop-types-exact/-/prop-types-exact-1.2.0.tgz
Source404: https://registry.npmjs.org/psl/-/psl-1.6.0.tgz
Source405: https://registry.npmjs.org/pump/-/pump-3.0.0.tgz
Source406: https://registry.npmjs.org/punycode/-/punycode-1.4.1.tgz
Source407: https://registry.npmjs.org/punycode/-/punycode-2.1.1.tgz
Source408: https://registry.npmjs.org/qs/-/qs-6.5.2.tgz
Source409: https://registry.npmjs.org/raf/-/raf-3.4.1.tgz
Source410: https://registry.npmjs.org/railroad-diagrams/-/railroad-diagrams-1.0.0.tgz
Source411: https://registry.npmjs.org/randexp/-/randexp-0.4.6.tgz
Source412: https://registry.npmjs.org/rc/-/rc-1.2.8.tgz
Source413: https://registry.npmjs.org/react-is/-/react-is-16.12.0.tgz
Source414: https://registry.npmjs.org/react-test-renderer/-/react-test-renderer-16.12.0.tgz
Source415: https://registry.npmjs.org/read-pkg/-/read-pkg-3.0.0.tgz
Source416: https://registry.npmjs.org/read-pkg-up/-/read-pkg-up-4.0.0.tgz
Source417: https://registry.npmjs.org/readable-stream/-/readable-stream-2.3.6.tgz
Source418: https://registry.npmjs.org/readable-stream/-/readable-stream-3.4.0.tgz
Source419: https://registry.npmjs.org/realpath-native/-/realpath-native-1.1.0.tgz
Source420: https://registry.npmjs.org/reflect.ownkeys/-/reflect.ownkeys-0.2.0.tgz
Source421: https://registry.npmjs.org/regenerator-runtime/-/regenerator-runtime-0.13.3.tgz
Source422: https://registry.npmjs.org/regex-not/-/regex-not-1.0.2.tgz
Source423: https://registry.npmjs.org/remove-trailing-separator/-/remove-trailing-separator-1.1.0.tgz
Source424: https://registry.npmjs.org/repeat-element/-/repeat-element-1.1.3.tgz
Source425: https://registry.npmjs.org/repeat-string/-/repeat-string-1.6.1.tgz
Source426: https://registry.npmjs.org/request/-/request-2.88.0.tgz
Source427: https://registry.npmjs.org/request-promise-core/-/request-promise-core-1.1.3.tgz
Source428: https://registry.npmjs.org/request-promise-native/-/request-promise-native-1.0.8.tgz
Source429: https://registry.npmjs.org/require-directory/-/require-directory-2.1.1.tgz
Source430: https://registry.npmjs.org/require-main-filename/-/require-main-filename-2.0.0.tgz
Source431: https://registry.npmjs.org/resolve/-/resolve-1.1.7.tgz
Source432: https://registry.npmjs.org/resolve/-/resolve-1.13.1.tgz
Source433: https://registry.npmjs.org/resolve-cwd/-/resolve-cwd-2.0.0.tgz
Source434: https://registry.npmjs.org/resolve-from/-/resolve-from-3.0.0.tgz
Source435: https://registry.npmjs.org/resolve-url/-/resolve-url-0.2.1.tgz
Source436: https://registry.npmjs.org/ret/-/ret-0.1.15.tgz
Source437: https://registry.npmjs.org/rimraf/-/rimraf-2.7.1.tgz
Source438: https://registry.npmjs.org/rst-selector-parser/-/rst-selector-parser-2.2.3.tgz
Source439: https://registry.npmjs.org/rsvp/-/rsvp-4.8.5.tgz
Source440: https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.1.2.tgz
Source441: https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.2.0.tgz
Source442: https://registry.npmjs.org/safe-regex/-/safe-regex-1.1.0.tgz
Source443: https://registry.npmjs.org/safer-buffer/-/safer-buffer-2.1.2.tgz
Source444: https://registry.npmjs.org/sane/-/sane-4.1.0.tgz
Source445: https://registry.npmjs.org/sax/-/sax-1.2.4.tgz
Source446: https://registry.npmjs.org/scheduler/-/scheduler-0.18.0.tgz
Source447: https://registry.npmjs.org/semver/-/semver-5.7.1.tgz
Source448: https://registry.npmjs.org/semver/-/semver-6.3.0.tgz
Source449: https://registry.npmjs.org/set-blocking/-/set-blocking-2.0.0.tgz
Source450: https://registry.npmjs.org/set-value/-/set-value-2.0.1.tgz
Source451: https://registry.npmjs.org/shebang-command/-/shebang-command-1.2.0.tgz
Source452: https://registry.npmjs.org/shebang-regex/-/shebang-regex-1.0.0.tgz
Source453: https://registry.npmjs.org/shellwords/-/shellwords-0.1.1.tgz
Source454: https://registry.npmjs.org/signal-exit/-/signal-exit-3.0.2.tgz
Source455: https://registry.npmjs.org/sisteransi/-/sisteransi-1.0.4.tgz
Source456: https://registry.npmjs.org/slash/-/slash-2.0.0.tgz
Source457: https://registry.npmjs.org/snapdragon/-/snapdragon-0.8.2.tgz
Source458: https://registry.npmjs.org/snapdragon-node/-/snapdragon-node-2.1.1.tgz
Source459: https://registry.npmjs.org/snapdragon-util/-/snapdragon-util-3.0.1.tgz
Source460: https://registry.npmjs.org/source-map/-/source-map-0.5.7.tgz
Source461: https://registry.npmjs.org/source-map/-/source-map-0.6.1.tgz
Source462: https://registry.npmjs.org/source-map-resolve/-/source-map-resolve-0.5.2.tgz
Source463: https://registry.npmjs.org/source-map-support/-/source-map-support-0.5.16.tgz
Source464: https://registry.npmjs.org/source-map-url/-/source-map-url-0.4.0.tgz
Source465: https://registry.npmjs.org/spdx-correct/-/spdx-correct-3.1.0.tgz
Source466: https://registry.npmjs.org/spdx-exceptions/-/spdx-exceptions-2.2.0.tgz
Source467: https://registry.npmjs.org/spdx-expression-parse/-/spdx-expression-parse-3.0.0.tgz
Source468: https://registry.npmjs.org/spdx-license-ids/-/spdx-license-ids-3.0.5.tgz
Source469: https://registry.npmjs.org/split-string/-/split-string-3.1.0.tgz
Source470: https://registry.npmjs.org/sshpk/-/sshpk-1.16.1.tgz
Source471: https://registry.npmjs.org/stack-utils/-/stack-utils-1.0.2.tgz
Source472: https://registry.npmjs.org/static-extend/-/static-extend-0.1.2.tgz
Source473: https://registry.npmjs.org/stealthy-require/-/stealthy-require-1.1.1.tgz
Source474: https://registry.npmjs.org/string_decoder/-/string_decoder-1.1.1.tgz
Source475: https://registry.npmjs.org/string_decoder/-/string_decoder-1.3.0.tgz
Source476: https://registry.npmjs.org/string-length/-/string-length-2.0.0.tgz
Source477: https://registry.npmjs.org/string-width/-/string-width-1.0.2.tgz
Source478: https://registry.npmjs.org/string-width/-/string-width-2.1.1.tgz
Source479: https://registry.npmjs.org/string-width/-/string-width-3.1.0.tgz
Source480: https://registry.npmjs.org/string.prototype.trim/-/string.prototype.trim-1.2.1.tgz
Source481: https://registry.npmjs.org/string.prototype.trimleft/-/string.prototype.trimleft-2.1.0.tgz
Source482: https://registry.npmjs.org/string.prototype.trimright/-/string.prototype.trimright-2.1.0.tgz
Source483: https://registry.npmjs.org/strip-ansi/-/strip-ansi-3.0.1.tgz
Source484: https://registry.npmjs.org/strip-ansi/-/strip-ansi-4.0.0.tgz
Source485: https://registry.npmjs.org/strip-ansi/-/strip-ansi-5.2.0.tgz
Source486: https://registry.npmjs.org/strip-bom/-/strip-bom-3.0.0.tgz
Source487: https://registry.npmjs.org/strip-eof/-/strip-eof-1.0.0.tgz
Source488: https://registry.npmjs.org/strip-json-comments/-/strip-json-comments-2.0.1.tgz
Source489: https://registry.npmjs.org/supports-color/-/supports-color-5.5.0.tgz
Source490: https://registry.npmjs.org/supports-color/-/supports-color-6.1.0.tgz
Source491: https://registry.npmjs.org/symbol-tree/-/symbol-tree-3.2.4.tgz
Source492: https://registry.npmjs.org/tar/-/tar-4.4.13.tgz
Source493: https://registry.npmjs.org/test-exclude/-/test-exclude-5.2.3.tgz
Source494: https://registry.npmjs.org/throat/-/throat-4.1.0.tgz
Source495: https://registry.npmjs.org/tmpl/-/tmpl-1.0.4.tgz
Source496: https://registry.npmjs.org/to-fast-properties/-/to-fast-properties-2.0.0.tgz
Source497: https://registry.npmjs.org/to-object-path/-/to-object-path-0.3.0.tgz
Source498: https://registry.npmjs.org/to-regex/-/to-regex-3.0.2.tgz
Source499: https://registry.npmjs.org/to-regex-range/-/to-regex-range-2.1.1.tgz
Source500: https://registry.npmjs.org/tough-cookie/-/tough-cookie-2.4.3.tgz
Source501: https://registry.npmjs.org/tough-cookie/-/tough-cookie-2.5.0.tgz
Source502: https://registry.npmjs.org/tr46/-/tr46-1.0.1.tgz
Source503: https://registry.npmjs.org/tunnel-agent/-/tunnel-agent-0.6.0.tgz
Source504: https://registry.npmjs.org/tweetnacl/-/tweetnacl-0.14.5.tgz
Source505: https://registry.npmjs.org/type-check/-/type-check-0.3.2.tgz
Source506: https://registry.npmjs.org/uglify-js/-/uglify-js-3.7.2.tgz
Source507: https://registry.npmjs.org/union-value/-/union-value-1.0.1.tgz
Source508: https://registry.npmjs.org/unset-value/-/unset-value-1.0.0.tgz
Source509: https://registry.npmjs.org/uri-js/-/uri-js-4.2.2.tgz
Source510: https://registry.npmjs.org/urix/-/urix-0.1.0.tgz
Source511: https://registry.npmjs.org/use/-/use-3.1.1.tgz
Source512: https://registry.npmjs.org/util-deprecate/-/util-deprecate-1.0.2.tgz
Source513: https://registry.npmjs.org/util.promisify/-/util.promisify-1.0.0.tgz
Source514: https://registry.npmjs.org/uuid/-/uuid-3.3.3.tgz
Source515: https://registry.npmjs.org/validate-npm-package-license/-/validate-npm-package-license-3.0.4.tgz
Source516: https://registry.npmjs.org/verror/-/verror-1.10.0.tgz
Source517: https://registry.npmjs.org/w3c-hr-time/-/w3c-hr-time-1.0.1.tgz
Source518: https://registry.npmjs.org/walker/-/walker-1.0.7.tgz
Source519: https://registry.npmjs.org/webidl-conversions/-/webidl-conversions-4.0.2.tgz
Source520: https://registry.npmjs.org/whatwg-encoding/-/whatwg-encoding-1.0.5.tgz
Source521: https://registry.npmjs.org/whatwg-mimetype/-/whatwg-mimetype-2.3.0.tgz
Source522: https://registry.npmjs.org/whatwg-url/-/whatwg-url-6.5.0.tgz
Source523: https://registry.npmjs.org/whatwg-url/-/whatwg-url-7.1.0.tgz
Source524: https://registry.npmjs.org/which/-/which-1.3.1.tgz
Source525: https://registry.npmjs.org/which-module/-/which-module-2.0.0.tgz
Source526: https://registry.npmjs.org/wide-align/-/wide-align-1.1.3.tgz
Source527: https://registry.npmjs.org/word-wrap/-/word-wrap-1.2.3.tgz
Source528: https://registry.npmjs.org/wordwrap/-/wordwrap-0.0.3.tgz
Source529: https://registry.npmjs.org/wrap-ansi/-/wrap-ansi-5.1.0.tgz
Source530: https://registry.npmjs.org/wrappy/-/wrappy-1.0.2.tgz
Source531: https://registry.npmjs.org/write-file-atomic/-/write-file-atomic-2.4.1.tgz
Source532: https://registry.npmjs.org/ws/-/ws-5.2.2.tgz
Source533: https://registry.npmjs.org/xml-name-validator/-/xml-name-validator-3.0.0.tgz
Source534: https://registry.npmjs.org/y18n/-/y18n-4.0.0.tgz
Source535: https://registry.npmjs.org/yallist/-/yallist-3.1.1.tgz
Source536: https://registry.npmjs.org/yargs/-/yargs-13.3.0.tgz
Source537: https://registry.npmjs.org/yargs-parser/-/yargs-parser-13.1.1.tgz
Source538: nodejs-theforeman-env-%{version}-registry.npmjs.org.tgz
%if 0%{?scl:1}
BuildRequires: %{?scl_prefix_nodejs}npm
%else
BuildRequires: nodejs-packaging
%endif
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}
Provides: bundled(npm(@babel/code-frame)) = 7.5.5
Provides: bundled(npm(@babel/core)) = 7.7.5
Provides: bundled(npm(@babel/generator)) = 7.7.4
Provides: bundled(npm(@babel/helper-function-name)) = 7.7.4
Provides: bundled(npm(@babel/helper-get-function-arity)) = 7.7.4
Provides: bundled(npm(@babel/helper-plugin-utils)) = 7.0.0
Provides: bundled(npm(@babel/helper-split-export-declaration)) = 7.7.4
Provides: bundled(npm(@babel/helpers)) = 7.7.4
Provides: bundled(npm(@babel/highlight)) = 7.5.0
Provides: bundled(npm(@babel/parser)) = 7.7.5
Provides: bundled(npm(@babel/plugin-syntax-object-rest-spread)) = 7.7.4
Provides: bundled(npm(@babel/template)) = 7.7.4
Provides: bundled(npm(@babel/traverse)) = 7.7.4
Provides: bundled(npm(@babel/types)) = 7.7.4
Provides: bundled(npm(@cnakazawa/watch)) = 1.0.3
Provides: bundled(npm(@jest/console)) = 24.9.0
Provides: bundled(npm(@jest/core)) = 24.9.0
Provides: bundled(npm(@jest/environment)) = 24.9.0
Provides: bundled(npm(@jest/fake-timers)) = 24.9.0
Provides: bundled(npm(@jest/reporters)) = 24.9.0
Provides: bundled(npm(@jest/source-map)) = 24.9.0
Provides: bundled(npm(@jest/test-result)) = 24.9.0
Provides: bundled(npm(@jest/test-sequencer)) = 24.9.0
Provides: bundled(npm(@jest/transform)) = 24.9.0
Provides: bundled(npm(@jest/types)) = 24.9.0
Provides: bundled(npm(@theforeman/env)) = 3.8.0
Provides: bundled(npm(@types/babel__core)) = 7.1.3
Provides: bundled(npm(@types/babel__generator)) = 7.6.1
Provides: bundled(npm(@types/babel__template)) = 7.0.2
Provides: bundled(npm(@types/babel__traverse)) = 7.0.8
Provides: bundled(npm(@types/istanbul-lib-coverage)) = 2.0.1
Provides: bundled(npm(@types/istanbul-lib-report)) = 1.1.1
Provides: bundled(npm(@types/istanbul-reports)) = 1.1.1
Provides: bundled(npm(@types/node)) = 12.12.18
Provides: bundled(npm(@types/stack-utils)) = 1.0.1
Provides: bundled(npm(@types/yargs)) = 13.0.3
Provides: bundled(npm(@types/yargs-parser)) = 13.1.0
Provides: bundled(npm(abab)) = 2.0.3
Provides: bundled(npm(abbrev)) = 1.1.1
Provides: bundled(npm(acorn)) = 5.7.3
Provides: bundled(npm(acorn)) = 6.4.0
Provides: bundled(npm(acorn-globals)) = 4.3.4
Provides: bundled(npm(acorn-walk)) = 6.2.0
Provides: bundled(npm(airbnb-prop-types)) = 2.15.0
Provides: bundled(npm(ajv)) = 6.10.2
Provides: bundled(npm(ansi-escapes)) = 3.2.0
Provides: bundled(npm(ansi-regex)) = 2.1.1
Provides: bundled(npm(ansi-regex)) = 3.0.0
Provides: bundled(npm(ansi-regex)) = 4.1.0
Provides: bundled(npm(ansi-styles)) = 3.2.1
Provides: bundled(npm(anymatch)) = 2.0.0
Provides: bundled(npm(aproba)) = 1.2.0
Provides: bundled(npm(are-we-there-yet)) = 1.1.5
Provides: bundled(npm(arr-diff)) = 4.0.0
Provides: bundled(npm(arr-flatten)) = 1.1.0
Provides: bundled(npm(arr-union)) = 3.1.0
Provides: bundled(npm(array-equal)) = 1.0.0
Provides: bundled(npm(array-filter)) = 1.0.0
Provides: bundled(npm(array-unique)) = 0.3.2
Provides: bundled(npm(array.prototype.find)) = 2.1.0
Provides: bundled(npm(array.prototype.flat)) = 1.2.3
Provides: bundled(npm(asn1)) = 0.2.4
Provides: bundled(npm(assert-plus)) = 1.0.0
Provides: bundled(npm(assign-symbols)) = 1.0.0
Provides: bundled(npm(astral-regex)) = 1.0.0
Provides: bundled(npm(async-limiter)) = 1.0.1
Provides: bundled(npm(asynckit)) = 0.4.0
Provides: bundled(npm(atob)) = 2.1.2
Provides: bundled(npm(aws-sign2)) = 0.7.0
Provides: bundled(npm(aws4)) = 1.9.0
Provides: bundled(npm(babel-jest)) = 24.9.0
Provides: bundled(npm(babel-plugin-dynamic-import-node)) = 2.3.0
Provides: bundled(npm(babel-plugin-istanbul)) = 5.2.0
Provides: bundled(npm(babel-plugin-jest-hoist)) = 24.9.0
Provides: bundled(npm(babel-preset-jest)) = 24.9.0
Provides: bundled(npm(balanced-match)) = 1.0.0
Provides: bundled(npm(base)) = 0.11.2
Provides: bundled(npm(bcrypt-pbkdf)) = 1.0.2
Provides: bundled(npm(bindings)) = 1.5.0
Provides: bundled(npm(boolbase)) = 1.0.0
Provides: bundled(npm(brace-expansion)) = 1.1.11
Provides: bundled(npm(braces)) = 2.3.2
Provides: bundled(npm(browser-process-hrtime)) = 0.1.3
Provides: bundled(npm(browser-resolve)) = 1.11.3
Provides: bundled(npm(bser)) = 2.1.1
Provides: bundled(npm(buffer-from)) = 1.1.1
Provides: bundled(npm(cache-base)) = 1.0.1
Provides: bundled(npm(callsites)) = 3.1.0
Provides: bundled(npm(camelcase)) = 5.3.1
Provides: bundled(npm(capture-exit)) = 2.0.0
Provides: bundled(npm(caseless)) = 0.12.0
Provides: bundled(npm(chalk)) = 2.4.2
Provides: bundled(npm(cheerio)) = 1.0.0-rc.3
Provides: bundled(npm(chownr)) = 1.1.3
Provides: bundled(npm(ci-info)) = 2.0.0
Provides: bundled(npm(class-utils)) = 0.3.6
Provides: bundled(npm(cliui)) = 5.0.0
Provides: bundled(npm(co)) = 4.6.0
Provides: bundled(npm(code-point-at)) = 1.1.0
Provides: bundled(npm(collection-visit)) = 1.0.0
Provides: bundled(npm(color-convert)) = 1.9.3
Provides: bundled(npm(color-name)) = 1.1.3
Provides: bundled(npm(combined-stream)) = 1.0.8
Provides: bundled(npm(commander)) = 2.20.3
Provides: bundled(npm(component-emitter)) = 1.3.0
Provides: bundled(npm(concat-map)) = 0.0.1
Provides: bundled(npm(console-control-strings)) = 1.1.0
Provides: bundled(npm(convert-source-map)) = 1.7.0
Provides: bundled(npm(copy-descriptor)) = 0.1.1
Provides: bundled(npm(core-js)) = 3.5.0
Provides: bundled(npm(core-util-is)) = 1.0.2
Provides: bundled(npm(cross-spawn)) = 6.0.5
Provides: bundled(npm(css-select)) = 1.2.0
Provides: bundled(npm(css-what)) = 2.1.3
Provides: bundled(npm(cssom)) = 0.3.8
Provides: bundled(npm(cssstyle)) = 1.4.0
Provides: bundled(npm(dashdash)) = 1.14.1
Provides: bundled(npm(data-urls)) = 1.1.0
Provides: bundled(npm(debug)) = 2.6.9
Provides: bundled(npm(debug)) = 3.2.6
Provides: bundled(npm(debug)) = 4.1.1
Provides: bundled(npm(decamelize)) = 1.2.0
Provides: bundled(npm(decode-uri-component)) = 0.2.0
Provides: bundled(npm(deep-extend)) = 0.6.0
Provides: bundled(npm(deep-is)) = 0.1.3
Provides: bundled(npm(define-properties)) = 1.1.3
Provides: bundled(npm(define-property)) = 0.2.5
Provides: bundled(npm(define-property)) = 1.0.0
Provides: bundled(npm(define-property)) = 2.0.2
Provides: bundled(npm(delayed-stream)) = 1.0.0
Provides: bundled(npm(delegates)) = 1.0.0
Provides: bundled(npm(detect-libc)) = 1.0.3
Provides: bundled(npm(detect-newline)) = 2.1.0
Provides: bundled(npm(diff-sequences)) = 24.9.0
Provides: bundled(npm(discontinuous-range)) = 1.0.0
Provides: bundled(npm(dom-serializer)) = 0.1.1
Provides: bundled(npm(dom-serializer)) = 0.2.2
Provides: bundled(npm(domelementtype)) = 1.3.1
Provides: bundled(npm(domelementtype)) = 2.0.1
Provides: bundled(npm(domexception)) = 1.0.1
Provides: bundled(npm(domhandler)) = 2.4.2
Provides: bundled(npm(domutils)) = 1.5.1
Provides: bundled(npm(domutils)) = 1.7.0
Provides: bundled(npm(ecc-jsbn)) = 0.1.2
Provides: bundled(npm(emoji-regex)) = 7.0.3
Provides: bundled(npm(end-of-stream)) = 1.4.4
Provides: bundled(npm(entities)) = 1.1.2
Provides: bundled(npm(entities)) = 2.0.0
Provides: bundled(npm(enzyme)) = 3.10.0
Provides: bundled(npm(enzyme-adapter-react-16)) = 1.15.1
Provides: bundled(npm(enzyme-adapter-utils)) = 1.12.1
Provides: bundled(npm(enzyme-shallow-equal)) = 1.0.0
Provides: bundled(npm(enzyme-to-json)) = 3.4.3
Provides: bundled(npm(error-ex)) = 1.3.2
Provides: bundled(npm(es-abstract)) = 1.16.3
Provides: bundled(npm(es-abstract)) = 1.17.0-next.1
Provides: bundled(npm(es-to-primitive)) = 1.2.1
Provides: bundled(npm(escape-string-regexp)) = 1.0.5
Provides: bundled(npm(escodegen)) = 1.12.0
Provides: bundled(npm(esprima)) = 3.1.3
Provides: bundled(npm(estraverse)) = 4.3.0
Provides: bundled(npm(esutils)) = 2.0.3
Provides: bundled(npm(exec-sh)) = 0.3.4
Provides: bundled(npm(execa)) = 1.0.0
Provides: bundled(npm(exit)) = 0.1.2
Provides: bundled(npm(expand-brackets)) = 2.1.4
Provides: bundled(npm(expect)) = 24.9.0
Provides: bundled(npm(extend)) = 3.0.2
Provides: bundled(npm(extend-shallow)) = 2.0.1
Provides: bundled(npm(extend-shallow)) = 3.0.2
Provides: bundled(npm(extglob)) = 2.0.4
Provides: bundled(npm(extsprintf)) = 1.3.0
Provides: bundled(npm(extsprintf)) = 1.4.0
Provides: bundled(npm(fast-deep-equal)) = 2.0.1
Provides: bundled(npm(fast-json-stable-stringify)) = 2.1.0
Provides: bundled(npm(fast-levenshtein)) = 2.0.6
Provides: bundled(npm(fb-watchman)) = 2.0.1
Provides: bundled(npm(file-uri-to-path)) = 1.0.0
Provides: bundled(npm(fill-range)) = 4.0.0
Provides: bundled(npm(find-up)) = 3.0.0
Provides: bundled(npm(for-in)) = 1.0.2
Provides: bundled(npm(forever-agent)) = 0.6.1
Provides: bundled(npm(form-data)) = 2.3.3
Provides: bundled(npm(fragment-cache)) = 0.2.1
Provides: bundled(npm(fs-minipass)) = 1.2.7
Provides: bundled(npm(fs.realpath)) = 1.0.0
Provides: bundled(npm(fsevents)) = 1.2.11
Provides: bundled(npm(function-bind)) = 1.1.1
Provides: bundled(npm(function.prototype.name)) = 1.1.2
Provides: bundled(npm(functions-have-names)) = 1.2.0
Provides: bundled(npm(gauge)) = 2.7.4
Provides: bundled(npm(get-caller-file)) = 2.0.5
Provides: bundled(npm(get-stream)) = 4.1.0
Provides: bundled(npm(get-value)) = 2.0.6
Provides: bundled(npm(getpass)) = 0.1.7
Provides: bundled(npm(glob)) = 7.1.6
Provides: bundled(npm(globals)) = 11.12.0
Provides: bundled(npm(graceful-fs)) = 4.2.3
Provides: bundled(npm(growly)) = 1.3.0
Provides: bundled(npm(handlebars)) = 4.5.3
Provides: bundled(npm(har-schema)) = 2.0.0
Provides: bundled(npm(har-validator)) = 5.1.3
Provides: bundled(npm(has)) = 1.0.3
Provides: bundled(npm(has-flag)) = 3.0.0
Provides: bundled(npm(has-symbols)) = 1.0.1
Provides: bundled(npm(has-unicode)) = 2.0.1
Provides: bundled(npm(has-value)) = 0.3.1
Provides: bundled(npm(has-value)) = 1.0.0
Provides: bundled(npm(has-values)) = 0.1.4
Provides: bundled(npm(has-values)) = 1.0.0
Provides: bundled(npm(hosted-git-info)) = 2.8.5
Provides: bundled(npm(html-element-map)) = 1.2.0
Provides: bundled(npm(html-encoding-sniffer)) = 1.0.2
Provides: bundled(npm(htmlparser2)) = 3.10.1
Provides: bundled(npm(http-signature)) = 1.2.0
Provides: bundled(npm(iconv-lite)) = 0.4.24
Provides: bundled(npm(ignore-walk)) = 3.0.3
Provides: bundled(npm(import-local)) = 2.0.0
Provides: bundled(npm(imurmurhash)) = 0.1.4
Provides: bundled(npm(inflight)) = 1.0.6
Provides: bundled(npm(inherits)) = 2.0.4
Provides: bundled(npm(ini)) = 1.3.5
Provides: bundled(npm(invariant)) = 2.2.4
Provides: bundled(npm(is-accessor-descriptor)) = 0.1.6
Provides: bundled(npm(is-accessor-descriptor)) = 1.0.0
Provides: bundled(npm(is-arrayish)) = 0.2.1
Provides: bundled(npm(is-boolean-object)) = 1.0.0
Provides: bundled(npm(is-buffer)) = 1.1.6
Provides: bundled(npm(is-callable)) = 1.1.4
Provides: bundled(npm(is-ci)) = 2.0.0
Provides: bundled(npm(is-data-descriptor)) = 0.1.4
Provides: bundled(npm(is-data-descriptor)) = 1.0.0
Provides: bundled(npm(is-date-object)) = 1.0.1
Provides: bundled(npm(is-descriptor)) = 0.1.6
Provides: bundled(npm(is-descriptor)) = 1.0.2
Provides: bundled(npm(is-extendable)) = 0.1.1
Provides: bundled(npm(is-extendable)) = 1.0.1
Provides: bundled(npm(is-fullwidth-code-point)) = 1.0.0
Provides: bundled(npm(is-fullwidth-code-point)) = 2.0.0
Provides: bundled(npm(is-generator-fn)) = 2.1.0
Provides: bundled(npm(is-number)) = 3.0.0
Provides: bundled(npm(is-number-object)) = 1.0.3
Provides: bundled(npm(is-plain-object)) = 2.0.4
Provides: bundled(npm(is-regex)) = 1.0.5
Provides: bundled(npm(is-stream)) = 1.1.0
Provides: bundled(npm(is-string)) = 1.0.4
Provides: bundled(npm(is-subset)) = 0.1.1
Provides: bundled(npm(is-symbol)) = 1.0.3
Provides: bundled(npm(is-typedarray)) = 1.0.0
Provides: bundled(npm(is-windows)) = 1.0.2
Provides: bundled(npm(is-wsl)) = 1.1.0
Provides: bundled(npm(isarray)) = 1.0.0
Provides: bundled(npm(isexe)) = 2.0.0
Provides: bundled(npm(isobject)) = 2.1.0
Provides: bundled(npm(isobject)) = 3.0.1
Provides: bundled(npm(isstream)) = 0.1.2
Provides: bundled(npm(istanbul-lib-coverage)) = 2.0.5
Provides: bundled(npm(istanbul-lib-instrument)) = 3.3.0
Provides: bundled(npm(istanbul-lib-report)) = 2.0.8
Provides: bundled(npm(istanbul-lib-source-maps)) = 3.0.6
Provides: bundled(npm(istanbul-reports)) = 2.2.6
Provides: bundled(npm(jest)) = 24.9.0
Provides: bundled(npm(jest-changed-files)) = 24.9.0
Provides: bundled(npm(jest-cli)) = 24.9.0
Provides: bundled(npm(jest-config)) = 24.9.0
Provides: bundled(npm(jest-diff)) = 24.9.0
Provides: bundled(npm(jest-docblock)) = 24.9.0
Provides: bundled(npm(jest-each)) = 24.9.0
Provides: bundled(npm(jest-environment-jsdom)) = 24.9.0
Provides: bundled(npm(jest-environment-node)) = 24.9.0
Provides: bundled(npm(jest-get-type)) = 24.9.0
Provides: bundled(npm(jest-haste-map)) = 24.9.0
Provides: bundled(npm(jest-jasmine2)) = 24.9.0
Provides: bundled(npm(jest-leak-detector)) = 24.9.0
Provides: bundled(npm(jest-matcher-utils)) = 24.9.0
Provides: bundled(npm(jest-message-util)) = 24.9.0
Provides: bundled(npm(jest-mock)) = 24.9.0
Provides: bundled(npm(jest-pnp-resolver)) = 1.2.1
Provides: bundled(npm(jest-prop-type-error)) = 1.1.0
Provides: bundled(npm(jest-regex-util)) = 24.9.0
Provides: bundled(npm(jest-resolve)) = 24.9.0
Provides: bundled(npm(jest-resolve-dependencies)) = 24.9.0
Provides: bundled(npm(jest-runner)) = 24.9.0
Provides: bundled(npm(jest-runtime)) = 24.9.0
Provides: bundled(npm(jest-serializer)) = 24.9.0
Provides: bundled(npm(jest-snapshot)) = 24.9.0
Provides: bundled(npm(jest-util)) = 24.9.0
Provides: bundled(npm(jest-validate)) = 24.9.0
Provides: bundled(npm(jest-watcher)) = 24.9.0
Provides: bundled(npm(jest-worker)) = 24.9.0
Provides: bundled(npm(js-tokens)) = 4.0.0
Provides: bundled(npm(jsbn)) = 0.1.1
Provides: bundled(npm(jsdom)) = 11.12.0
Provides: bundled(npm(jsesc)) = 2.5.2
Provides: bundled(npm(json-parse-better-errors)) = 1.0.2
Provides: bundled(npm(json-schema)) = 0.2.3
Provides: bundled(npm(json-schema-traverse)) = 0.4.1
Provides: bundled(npm(json-stringify-safe)) = 5.0.1
Provides: bundled(npm(json5)) = 2.1.1
Provides: bundled(npm(jsprim)) = 1.4.1
Provides: bundled(npm(kind-of)) = 3.2.2
Provides: bundled(npm(kind-of)) = 4.0.0
Provides: bundled(npm(kind-of)) = 5.1.0
Provides: bundled(npm(kind-of)) = 6.0.2
Provides: bundled(npm(kleur)) = 3.0.3
Provides: bundled(npm(left-pad)) = 1.3.0
Provides: bundled(npm(leven)) = 3.1.0
Provides: bundled(npm(levn)) = 0.3.0
Provides: bundled(npm(load-json-file)) = 4.0.0
Provides: bundled(npm(locate-path)) = 3.0.0
Provides: bundled(npm(lodash)) = 4.17.15
Provides: bundled(npm(lodash.escape)) = 4.0.1
Provides: bundled(npm(lodash.flattendeep)) = 4.4.0
Provides: bundled(npm(lodash.isequal)) = 4.5.0
Provides: bundled(npm(lodash.sortby)) = 4.7.0
Provides: bundled(npm(loose-envify)) = 1.4.0
Provides: bundled(npm(make-dir)) = 2.1.0
Provides: bundled(npm(makeerror)) = 1.0.11
Provides: bundled(npm(map-cache)) = 0.2.2
Provides: bundled(npm(map-visit)) = 1.0.0
Provides: bundled(npm(merge-stream)) = 2.0.0
Provides: bundled(npm(micromatch)) = 3.1.10
Provides: bundled(npm(mime-db)) = 1.42.0
Provides: bundled(npm(mime-types)) = 2.1.25
Provides: bundled(npm(minimatch)) = 3.0.4
Provides: bundled(npm(minimist)) = 0.0.10
Provides: bundled(npm(minimist)) = 0.0.8
Provides: bundled(npm(minimist)) = 1.2.0
Provides: bundled(npm(minipass)) = 2.9.0
Provides: bundled(npm(minizlib)) = 1.3.3
Provides: bundled(npm(mixin-deep)) = 1.3.2
Provides: bundled(npm(mkdirp)) = 0.5.1
Provides: bundled(npm(moo)) = 0.4.3
Provides: bundled(npm(ms)) = 2.0.0
Provides: bundled(npm(ms)) = 2.1.2
Provides: bundled(npm(nan)) = 2.14.0
Provides: bundled(npm(nanomatch)) = 1.2.13
Provides: bundled(npm(natural-compare)) = 1.4.0
Provides: bundled(npm(nearley)) = 2.19.0
Provides: bundled(npm(needle)) = 2.4.0
Provides: bundled(npm(neo-async)) = 2.6.1
Provides: bundled(npm(nice-try)) = 1.0.5
Provides: bundled(npm(node-int64)) = 0.4.0
Provides: bundled(npm(node-modules-regexp)) = 1.0.0
Provides: bundled(npm(node-notifier)) = 5.4.3
Provides: bundled(npm(node-pre-gyp)) = 0.14.0
Provides: bundled(npm(nopt)) = 4.0.1
Provides: bundled(npm(normalize-package-data)) = 2.5.0
Provides: bundled(npm(normalize-path)) = 2.1.1
Provides: bundled(npm(npm-bundled)) = 1.1.1
Provides: bundled(npm(npm-normalize-package-bin)) = 1.0.1
Provides: bundled(npm(npm-packlist)) = 1.4.7
Provides: bundled(npm(npm-run-path)) = 2.0.2
Provides: bundled(npm(npmlog)) = 4.1.2
Provides: bundled(npm(nth-check)) = 1.0.2
Provides: bundled(npm(number-is-nan)) = 1.0.1
Provides: bundled(npm(nwsapi)) = 2.2.0
Provides: bundled(npm(oauth-sign)) = 0.9.0
Provides: bundled(npm(object-assign)) = 4.1.1
Provides: bundled(npm(object-copy)) = 0.1.0
Provides: bundled(npm(object-inspect)) = 1.7.0
Provides: bundled(npm(object-is)) = 1.0.2
Provides: bundled(npm(object-keys)) = 1.1.1
Provides: bundled(npm(object-visit)) = 1.0.1
Provides: bundled(npm(object.assign)) = 4.1.0
Provides: bundled(npm(object.entries)) = 1.1.1
Provides: bundled(npm(object.fromentries)) = 2.0.2
Provides: bundled(npm(object.getownpropertydescriptors)) = 2.1.0
Provides: bundled(npm(object.pick)) = 1.3.0
Provides: bundled(npm(object.values)) = 1.1.1
Provides: bundled(npm(once)) = 1.4.0
Provides: bundled(npm(optimist)) = 0.6.1
Provides: bundled(npm(optionator)) = 0.8.3
Provides: bundled(npm(os-homedir)) = 1.0.2
Provides: bundled(npm(os-tmpdir)) = 1.0.2
Provides: bundled(npm(osenv)) = 0.1.5
Provides: bundled(npm(p-each-series)) = 1.0.0
Provides: bundled(npm(p-finally)) = 1.0.0
Provides: bundled(npm(p-limit)) = 2.2.1
Provides: bundled(npm(p-locate)) = 3.0.0
Provides: bundled(npm(p-reduce)) = 1.0.0
Provides: bundled(npm(p-try)) = 2.2.0
Provides: bundled(npm(parse-json)) = 4.0.0
Provides: bundled(npm(parse5)) = 3.0.3
Provides: bundled(npm(parse5)) = 4.0.0
Provides: bundled(npm(pascalcase)) = 0.1.1
Provides: bundled(npm(path-exists)) = 3.0.0
Provides: bundled(npm(path-is-absolute)) = 1.0.1
Provides: bundled(npm(path-key)) = 2.0.1
Provides: bundled(npm(path-parse)) = 1.0.6
Provides: bundled(npm(path-type)) = 3.0.0
Provides: bundled(npm(performance-now)) = 2.1.0
Provides: bundled(npm(pify)) = 3.0.0
Provides: bundled(npm(pify)) = 4.0.1
Provides: bundled(npm(pirates)) = 4.0.1
Provides: bundled(npm(pkg-dir)) = 3.0.0
Provides: bundled(npm(pn)) = 1.1.0
Provides: bundled(npm(posix-character-classes)) = 0.1.1
Provides: bundled(npm(prelude-ls)) = 1.1.2
Provides: bundled(npm(pretty-format)) = 24.9.0
Provides: bundled(npm(process-nextick-args)) = 2.0.1
Provides: bundled(npm(prompts)) = 2.3.0
Provides: bundled(npm(prop-types)) = 15.7.2
Provides: bundled(npm(prop-types-exact)) = 1.2.0
Provides: bundled(npm(psl)) = 1.6.0
Provides: bundled(npm(pump)) = 3.0.0
Provides: bundled(npm(punycode)) = 1.4.1
Provides: bundled(npm(punycode)) = 2.1.1
Provides: bundled(npm(qs)) = 6.5.2
Provides: bundled(npm(raf)) = 3.4.1
Provides: bundled(npm(railroad-diagrams)) = 1.0.0
Provides: bundled(npm(randexp)) = 0.4.6
Provides: bundled(npm(rc)) = 1.2.8
Provides: bundled(npm(react-is)) = 16.12.0
Provides: bundled(npm(react-test-renderer)) = 16.12.0
Provides: bundled(npm(read-pkg)) = 3.0.0
Provides: bundled(npm(read-pkg-up)) = 4.0.0
Provides: bundled(npm(readable-stream)) = 2.3.6
Provides: bundled(npm(readable-stream)) = 3.4.0
Provides: bundled(npm(realpath-native)) = 1.1.0
Provides: bundled(npm(reflect.ownkeys)) = 0.2.0
Provides: bundled(npm(regenerator-runtime)) = 0.13.3
Provides: bundled(npm(regex-not)) = 1.0.2
Provides: bundled(npm(remove-trailing-separator)) = 1.1.0
Provides: bundled(npm(repeat-element)) = 1.1.3
Provides: bundled(npm(repeat-string)) = 1.6.1
Provides: bundled(npm(request)) = 2.88.0
Provides: bundled(npm(request-promise-core)) = 1.1.3
Provides: bundled(npm(request-promise-native)) = 1.0.8
Provides: bundled(npm(require-directory)) = 2.1.1
Provides: bundled(npm(require-main-filename)) = 2.0.0
Provides: bundled(npm(resolve)) = 1.1.7
Provides: bundled(npm(resolve)) = 1.13.1
Provides: bundled(npm(resolve-cwd)) = 2.0.0
Provides: bundled(npm(resolve-from)) = 3.0.0
Provides: bundled(npm(resolve-url)) = 0.2.1
Provides: bundled(npm(ret)) = 0.1.15
Provides: bundled(npm(rimraf)) = 2.7.1
Provides: bundled(npm(rst-selector-parser)) = 2.2.3
Provides: bundled(npm(rsvp)) = 4.8.5
Provides: bundled(npm(safe-buffer)) = 5.1.2
Provides: bundled(npm(safe-buffer)) = 5.2.0
Provides: bundled(npm(safe-regex)) = 1.1.0
Provides: bundled(npm(safer-buffer)) = 2.1.2
Provides: bundled(npm(sane)) = 4.1.0
Provides: bundled(npm(sax)) = 1.2.4
Provides: bundled(npm(scheduler)) = 0.18.0
Provides: bundled(npm(semver)) = 5.7.1
Provides: bundled(npm(semver)) = 6.3.0
Provides: bundled(npm(set-blocking)) = 2.0.0
Provides: bundled(npm(set-value)) = 2.0.1
Provides: bundled(npm(shebang-command)) = 1.2.0
Provides: bundled(npm(shebang-regex)) = 1.0.0
Provides: bundled(npm(shellwords)) = 0.1.1
Provides: bundled(npm(signal-exit)) = 3.0.2
Provides: bundled(npm(sisteransi)) = 1.0.4
Provides: bundled(npm(slash)) = 2.0.0
Provides: bundled(npm(snapdragon)) = 0.8.2
Provides: bundled(npm(snapdragon-node)) = 2.1.1
Provides: bundled(npm(snapdragon-util)) = 3.0.1
Provides: bundled(npm(source-map)) = 0.5.7
Provides: bundled(npm(source-map)) = 0.6.1
Provides: bundled(npm(source-map-resolve)) = 0.5.2
Provides: bundled(npm(source-map-support)) = 0.5.16
Provides: bundled(npm(source-map-url)) = 0.4.0
Provides: bundled(npm(spdx-correct)) = 3.1.0
Provides: bundled(npm(spdx-exceptions)) = 2.2.0
Provides: bundled(npm(spdx-expression-parse)) = 3.0.0
Provides: bundled(npm(spdx-license-ids)) = 3.0.5
Provides: bundled(npm(split-string)) = 3.1.0
Provides: bundled(npm(sshpk)) = 1.16.1
Provides: bundled(npm(stack-utils)) = 1.0.2
Provides: bundled(npm(static-extend)) = 0.1.2
Provides: bundled(npm(stealthy-require)) = 1.1.1
Provides: bundled(npm(string_decoder)) = 1.1.1
Provides: bundled(npm(string_decoder)) = 1.3.0
Provides: bundled(npm(string-length)) = 2.0.0
Provides: bundled(npm(string-width)) = 1.0.2
Provides: bundled(npm(string-width)) = 2.1.1
Provides: bundled(npm(string-width)) = 3.1.0
Provides: bundled(npm(string.prototype.trim)) = 1.2.1
Provides: bundled(npm(string.prototype.trimleft)) = 2.1.0
Provides: bundled(npm(string.prototype.trimright)) = 2.1.0
Provides: bundled(npm(strip-ansi)) = 3.0.1
Provides: bundled(npm(strip-ansi)) = 4.0.0
Provides: bundled(npm(strip-ansi)) = 5.2.0
Provides: bundled(npm(strip-bom)) = 3.0.0
Provides: bundled(npm(strip-eof)) = 1.0.0
Provides: bundled(npm(strip-json-comments)) = 2.0.1
Provides: bundled(npm(supports-color)) = 5.5.0
Provides: bundled(npm(supports-color)) = 6.1.0
Provides: bundled(npm(symbol-tree)) = 3.2.4
Provides: bundled(npm(tar)) = 4.4.13
Provides: bundled(npm(test-exclude)) = 5.2.3
Provides: bundled(npm(throat)) = 4.1.0
Provides: bundled(npm(tmpl)) = 1.0.4
Provides: bundled(npm(to-fast-properties)) = 2.0.0
Provides: bundled(npm(to-object-path)) = 0.3.0
Provides: bundled(npm(to-regex)) = 3.0.2
Provides: bundled(npm(to-regex-range)) = 2.1.1
Provides: bundled(npm(tough-cookie)) = 2.4.3
Provides: bundled(npm(tough-cookie)) = 2.5.0
Provides: bundled(npm(tr46)) = 1.0.1
Provides: bundled(npm(tunnel-agent)) = 0.6.0
Provides: bundled(npm(tweetnacl)) = 0.14.5
Provides: bundled(npm(type-check)) = 0.3.2
Provides: bundled(npm(uglify-js)) = 3.7.2
Provides: bundled(npm(union-value)) = 1.0.1
Provides: bundled(npm(unset-value)) = 1.0.0
Provides: bundled(npm(uri-js)) = 4.2.2
Provides: bundled(npm(urix)) = 0.1.0
Provides: bundled(npm(use)) = 3.1.1
Provides: bundled(npm(util-deprecate)) = 1.0.2
Provides: bundled(npm(util.promisify)) = 1.0.0
Provides: bundled(npm(uuid)) = 3.3.3
Provides: bundled(npm(validate-npm-package-license)) = 3.0.4
Provides: bundled(npm(verror)) = 1.10.0
Provides: bundled(npm(w3c-hr-time)) = 1.0.1
Provides: bundled(npm(walker)) = 1.0.7
Provides: bundled(npm(webidl-conversions)) = 4.0.2
Provides: bundled(npm(whatwg-encoding)) = 1.0.5
Provides: bundled(npm(whatwg-mimetype)) = 2.3.0
Provides: bundled(npm(whatwg-url)) = 6.5.0
Provides: bundled(npm(whatwg-url)) = 7.1.0
Provides: bundled(npm(which)) = 1.3.1
Provides: bundled(npm(which-module)) = 2.0.0
Provides: bundled(npm(wide-align)) = 1.1.3
Provides: bundled(npm(word-wrap)) = 1.2.3
Provides: bundled(npm(wordwrap)) = 0.0.3
Provides: bundled(npm(wrap-ansi)) = 5.1.0
Provides: bundled(npm(wrappy)) = 1.0.2
Provides: bundled(npm(write-file-atomic)) = 2.4.1
Provides: bundled(npm(ws)) = 5.2.2
Provides: bundled(npm(xml-name-validator)) = 3.0.0
Provides: bundled(npm(y18n)) = 4.0.0
Provides: bundled(npm(yallist)) = 3.1.1
Provides: bundled(npm(yargs)) = 13.3.0
Provides: bundled(npm(yargs-parser)) = 13.1.1
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

%setup -T -q -a 538 -D -n %{npm_cache_dir}

%build
%{?scl:scl enable %{?scl_nodejs} - << \end_of_scl}
npm install --cache-min Infinity --cache %{?scl:../}%{npm_cache_dir} --no-shrinkwrap --no-optional --global-style true %{npm_name}@%{version}
%{?scl:end_of_scl}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/babel %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/test %{buildroot}%{nodejs_sitelib}/%{npm_name}

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%license node_modules/%{npm_name}/license
%doc node_modules/%{npm_name}/CHANGELOG.md
%doc node_modules/%{npm_name}/README.md

%changelog
* Mon Dec 16 2019 vagrant 3.8.0-1
- Add nodejs-theforeman-env generated by npm2rpm using the bundle strategy

