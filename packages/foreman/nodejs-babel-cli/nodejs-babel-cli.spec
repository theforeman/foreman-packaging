%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name babel-cli

Name: %{?scl_prefix}nodejs-babel-cli
Version: 6.26.0
Release: 4%{?dist}
Summary: Babel command line
License: MIT
Group: Development/Libraries
URL: https://babeljs.io/
Source0: https://registry.npmjs.org/abbrev/-/abbrev-1.1.1.tgz
Source1: https://registry.npmjs.org/ansi-regex/-/ansi-regex-2.1.1.tgz
Source2: https://registry.npmjs.org/ansi-regex/-/ansi-regex-3.0.0.tgz
Source3: https://registry.npmjs.org/ansi-styles/-/ansi-styles-2.2.1.tgz
Source4: https://registry.npmjs.org/anymatch/-/anymatch-1.3.2.tgz
Source5: https://registry.npmjs.org/aproba/-/aproba-1.2.0.tgz
Source6: https://registry.npmjs.org/are-we-there-yet/-/are-we-there-yet-1.1.5.tgz
Source7: https://registry.npmjs.org/arr-diff/-/arr-diff-2.0.0.tgz
Source8: https://registry.npmjs.org/arr-diff/-/arr-diff-4.0.0.tgz
Source9: https://registry.npmjs.org/arr-flatten/-/arr-flatten-1.1.0.tgz
Source10: https://registry.npmjs.org/arr-union/-/arr-union-3.1.0.tgz
Source11: https://registry.npmjs.org/array-unique/-/array-unique-0.2.1.tgz
Source12: https://registry.npmjs.org/array-unique/-/array-unique-0.3.2.tgz
Source13: https://registry.npmjs.org/assign-symbols/-/assign-symbols-1.0.0.tgz
Source14: https://registry.npmjs.org/async-each/-/async-each-1.0.3.tgz
Source15: https://registry.npmjs.org/atob/-/atob-2.1.2.tgz
Source16: https://registry.npmjs.org/babel-cli/-/babel-cli-6.26.0.tgz
Source17: https://registry.npmjs.org/babel-code-frame/-/babel-code-frame-6.26.0.tgz
Source18: https://registry.npmjs.org/babel-core/-/babel-core-6.26.3.tgz
Source19: https://registry.npmjs.org/babel-generator/-/babel-generator-6.26.1.tgz
Source20: https://registry.npmjs.org/babel-helpers/-/babel-helpers-6.24.1.tgz
Source21: https://registry.npmjs.org/babel-messages/-/babel-messages-6.23.0.tgz
Source22: https://registry.npmjs.org/babel-polyfill/-/babel-polyfill-6.26.0.tgz
Source23: https://registry.npmjs.org/babel-register/-/babel-register-6.26.0.tgz
Source24: https://registry.npmjs.org/babel-runtime/-/babel-runtime-6.26.0.tgz
Source25: https://registry.npmjs.org/babel-template/-/babel-template-6.26.0.tgz
Source26: https://registry.npmjs.org/babel-traverse/-/babel-traverse-6.26.0.tgz
Source27: https://registry.npmjs.org/babel-types/-/babel-types-6.26.0.tgz
Source28: https://registry.npmjs.org/babylon/-/babylon-6.18.0.tgz
Source29: https://registry.npmjs.org/balanced-match/-/balanced-match-1.0.0.tgz
Source30: https://registry.npmjs.org/base/-/base-0.11.2.tgz
Source31: https://registry.npmjs.org/binary-extensions/-/binary-extensions-1.13.1.tgz
Source32: https://registry.npmjs.org/brace-expansion/-/brace-expansion-1.1.11.tgz
Source33: https://registry.npmjs.org/braces/-/braces-1.8.5.tgz
Source34: https://registry.npmjs.org/braces/-/braces-2.3.2.tgz
Source35: https://registry.npmjs.org/cache-base/-/cache-base-1.0.1.tgz
Source36: https://registry.npmjs.org/chalk/-/chalk-1.1.3.tgz
Source37: https://registry.npmjs.org/chokidar/-/chokidar-1.7.0.tgz
Source38: https://registry.npmjs.org/chownr/-/chownr-1.1.3.tgz
Source39: https://registry.npmjs.org/class-utils/-/class-utils-0.3.6.tgz
Source40: https://registry.npmjs.org/code-point-at/-/code-point-at-1.1.0.tgz
Source41: https://registry.npmjs.org/collection-visit/-/collection-visit-1.0.0.tgz
Source42: https://registry.npmjs.org/commander/-/commander-2.20.1.tgz
Source43: https://registry.npmjs.org/component-emitter/-/component-emitter-1.3.0.tgz
Source44: https://registry.npmjs.org/concat-map/-/concat-map-0.0.1.tgz
Source45: https://registry.npmjs.org/console-control-strings/-/console-control-strings-1.1.0.tgz
Source46: https://registry.npmjs.org/convert-source-map/-/convert-source-map-1.6.0.tgz
Source47: https://registry.npmjs.org/copy-descriptor/-/copy-descriptor-0.1.1.tgz
Source48: https://registry.npmjs.org/core-js/-/core-js-2.6.9.tgz
Source49: https://registry.npmjs.org/core-util-is/-/core-util-is-1.0.2.tgz
Source50: https://registry.npmjs.org/debug/-/debug-2.6.9.tgz
Source51: https://registry.npmjs.org/debug/-/debug-3.2.6.tgz
Source52: https://registry.npmjs.org/decode-uri-component/-/decode-uri-component-0.2.0.tgz
Source53: https://registry.npmjs.org/deep-extend/-/deep-extend-0.6.0.tgz
Source54: https://registry.npmjs.org/define-property/-/define-property-0.2.5.tgz
Source55: https://registry.npmjs.org/define-property/-/define-property-1.0.0.tgz
Source56: https://registry.npmjs.org/define-property/-/define-property-2.0.2.tgz
Source57: https://registry.npmjs.org/delegates/-/delegates-1.0.0.tgz
Source58: https://registry.npmjs.org/detect-indent/-/detect-indent-4.0.0.tgz
Source59: https://registry.npmjs.org/detect-libc/-/detect-libc-1.0.3.tgz
Source60: https://registry.npmjs.org/escape-string-regexp/-/escape-string-regexp-1.0.5.tgz
Source61: https://registry.npmjs.org/esutils/-/esutils-2.0.3.tgz
Source62: https://registry.npmjs.org/expand-brackets/-/expand-brackets-0.1.5.tgz
Source63: https://registry.npmjs.org/expand-brackets/-/expand-brackets-2.1.4.tgz
Source64: https://registry.npmjs.org/expand-range/-/expand-range-1.8.2.tgz
Source65: https://registry.npmjs.org/extend-shallow/-/extend-shallow-2.0.1.tgz
Source66: https://registry.npmjs.org/extend-shallow/-/extend-shallow-3.0.2.tgz
Source67: https://registry.npmjs.org/extglob/-/extglob-0.3.2.tgz
Source68: https://registry.npmjs.org/extglob/-/extglob-2.0.4.tgz
Source69: https://registry.npmjs.org/filename-regex/-/filename-regex-2.0.1.tgz
Source70: https://registry.npmjs.org/fill-range/-/fill-range-2.2.4.tgz
Source71: https://registry.npmjs.org/fill-range/-/fill-range-4.0.0.tgz
Source72: https://registry.npmjs.org/for-in/-/for-in-1.0.2.tgz
Source73: https://registry.npmjs.org/for-own/-/for-own-0.1.5.tgz
Source74: https://registry.npmjs.org/fragment-cache/-/fragment-cache-0.2.1.tgz
Source75: https://registry.npmjs.org/fs-minipass/-/fs-minipass-1.2.7.tgz
Source76: https://registry.npmjs.org/fs-readdir-recursive/-/fs-readdir-recursive-1.1.0.tgz
Source77: https://registry.npmjs.org/fs.realpath/-/fs.realpath-1.0.0.tgz
Source78: https://registry.npmjs.org/fsevents/-/fsevents-1.2.9.tgz
Source79: https://registry.npmjs.org/gauge/-/gauge-2.7.4.tgz
Source80: https://registry.npmjs.org/get-value/-/get-value-2.0.6.tgz
Source81: https://registry.npmjs.org/glob/-/glob-7.1.4.tgz
Source82: https://registry.npmjs.org/glob-base/-/glob-base-0.3.0.tgz
Source83: https://registry.npmjs.org/glob-parent/-/glob-parent-2.0.0.tgz
Source84: https://registry.npmjs.org/globals/-/globals-9.18.0.tgz
Source85: https://registry.npmjs.org/graceful-fs/-/graceful-fs-4.2.2.tgz
Source86: https://registry.npmjs.org/has-ansi/-/has-ansi-2.0.0.tgz
Source87: https://registry.npmjs.org/has-unicode/-/has-unicode-2.0.1.tgz
Source88: https://registry.npmjs.org/has-value/-/has-value-0.3.1.tgz
Source89: https://registry.npmjs.org/has-value/-/has-value-1.0.0.tgz
Source90: https://registry.npmjs.org/has-values/-/has-values-0.1.4.tgz
Source91: https://registry.npmjs.org/has-values/-/has-values-1.0.0.tgz
Source92: https://registry.npmjs.org/home-or-tmp/-/home-or-tmp-2.0.0.tgz
Source93: https://registry.npmjs.org/iconv-lite/-/iconv-lite-0.4.24.tgz
Source94: https://registry.npmjs.org/ignore-walk/-/ignore-walk-3.0.2.tgz
Source95: https://registry.npmjs.org/inflight/-/inflight-1.0.6.tgz
Source96: https://registry.npmjs.org/inherits/-/inherits-2.0.4.tgz
Source97: https://registry.npmjs.org/ini/-/ini-1.3.5.tgz
Source98: https://registry.npmjs.org/invariant/-/invariant-2.2.4.tgz
Source99: https://registry.npmjs.org/is-accessor-descriptor/-/is-accessor-descriptor-0.1.6.tgz
Source100: https://registry.npmjs.org/is-accessor-descriptor/-/is-accessor-descriptor-1.0.0.tgz
Source101: https://registry.npmjs.org/is-binary-path/-/is-binary-path-1.0.1.tgz
Source102: https://registry.npmjs.org/is-buffer/-/is-buffer-1.1.6.tgz
Source103: https://registry.npmjs.org/is-data-descriptor/-/is-data-descriptor-0.1.4.tgz
Source104: https://registry.npmjs.org/is-data-descriptor/-/is-data-descriptor-1.0.0.tgz
Source105: https://registry.npmjs.org/is-descriptor/-/is-descriptor-0.1.6.tgz
Source106: https://registry.npmjs.org/is-descriptor/-/is-descriptor-1.0.2.tgz
Source107: https://registry.npmjs.org/is-dotfile/-/is-dotfile-1.0.3.tgz
Source108: https://registry.npmjs.org/is-equal-shallow/-/is-equal-shallow-0.1.3.tgz
Source109: https://registry.npmjs.org/is-extendable/-/is-extendable-0.1.1.tgz
Source110: https://registry.npmjs.org/is-extendable/-/is-extendable-1.0.1.tgz
Source111: https://registry.npmjs.org/is-extglob/-/is-extglob-1.0.0.tgz
Source112: https://registry.npmjs.org/is-finite/-/is-finite-1.0.2.tgz
Source113: https://registry.npmjs.org/is-fullwidth-code-point/-/is-fullwidth-code-point-1.0.0.tgz
Source114: https://registry.npmjs.org/is-fullwidth-code-point/-/is-fullwidth-code-point-2.0.0.tgz
Source115: https://registry.npmjs.org/is-glob/-/is-glob-2.0.1.tgz
Source116: https://registry.npmjs.org/is-number/-/is-number-2.1.0.tgz
Source117: https://registry.npmjs.org/is-number/-/is-number-3.0.0.tgz
Source118: https://registry.npmjs.org/is-number/-/is-number-4.0.0.tgz
Source119: https://registry.npmjs.org/is-plain-object/-/is-plain-object-2.0.4.tgz
Source120: https://registry.npmjs.org/is-posix-bracket/-/is-posix-bracket-0.1.1.tgz
Source121: https://registry.npmjs.org/is-primitive/-/is-primitive-2.0.0.tgz
Source122: https://registry.npmjs.org/is-windows/-/is-windows-1.0.2.tgz
Source123: https://registry.npmjs.org/isarray/-/isarray-1.0.0.tgz
Source124: https://registry.npmjs.org/isobject/-/isobject-2.1.0.tgz
Source125: https://registry.npmjs.org/isobject/-/isobject-3.0.1.tgz
Source126: https://registry.npmjs.org/js-tokens/-/js-tokens-3.0.2.tgz
Source127: https://registry.npmjs.org/js-tokens/-/js-tokens-4.0.0.tgz
Source128: https://registry.npmjs.org/jsesc/-/jsesc-1.3.0.tgz
Source129: https://registry.npmjs.org/json5/-/json5-0.5.1.tgz
Source130: https://registry.npmjs.org/kind-of/-/kind-of-3.2.2.tgz
Source131: https://registry.npmjs.org/kind-of/-/kind-of-4.0.0.tgz
Source132: https://registry.npmjs.org/kind-of/-/kind-of-5.1.0.tgz
Source133: https://registry.npmjs.org/kind-of/-/kind-of-6.0.2.tgz
Source134: https://registry.npmjs.org/lodash/-/lodash-4.17.15.tgz
Source135: https://registry.npmjs.org/loose-envify/-/loose-envify-1.4.0.tgz
Source136: https://registry.npmjs.org/map-cache/-/map-cache-0.2.2.tgz
Source137: https://registry.npmjs.org/map-visit/-/map-visit-1.0.0.tgz
Source138: https://registry.npmjs.org/math-random/-/math-random-1.0.4.tgz
Source139: https://registry.npmjs.org/micromatch/-/micromatch-2.3.11.tgz
Source140: https://registry.npmjs.org/micromatch/-/micromatch-3.1.10.tgz
Source141: https://registry.npmjs.org/minimatch/-/minimatch-3.0.4.tgz
Source142: https://registry.npmjs.org/minimist/-/minimist-0.0.8.tgz
Source143: https://registry.npmjs.org/minimist/-/minimist-1.2.0.tgz
Source144: https://registry.npmjs.org/minipass/-/minipass-2.9.0.tgz
Source145: https://registry.npmjs.org/minizlib/-/minizlib-1.3.3.tgz
Source146: https://registry.npmjs.org/mixin-deep/-/mixin-deep-1.3.2.tgz
Source147: https://registry.npmjs.org/mkdirp/-/mkdirp-0.5.1.tgz
Source148: https://registry.npmjs.org/ms/-/ms-2.0.0.tgz
Source149: https://registry.npmjs.org/ms/-/ms-2.1.2.tgz
Source150: https://registry.npmjs.org/nan/-/nan-2.14.0.tgz
Source151: https://registry.npmjs.org/nanomatch/-/nanomatch-1.2.13.tgz
Source152: https://registry.npmjs.org/needle/-/needle-2.4.0.tgz
Source153: https://registry.npmjs.org/node-pre-gyp/-/node-pre-gyp-0.12.0.tgz
Source154: https://registry.npmjs.org/nopt/-/nopt-4.0.1.tgz
Source155: https://registry.npmjs.org/normalize-path/-/normalize-path-2.1.1.tgz
Source156: https://registry.npmjs.org/npm-bundled/-/npm-bundled-1.0.6.tgz
Source157: https://registry.npmjs.org/npm-packlist/-/npm-packlist-1.4.4.tgz
Source158: https://registry.npmjs.org/npmlog/-/npmlog-4.1.2.tgz
Source159: https://registry.npmjs.org/number-is-nan/-/number-is-nan-1.0.1.tgz
Source160: https://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz
Source161: https://registry.npmjs.org/object-copy/-/object-copy-0.1.0.tgz
Source162: https://registry.npmjs.org/object-visit/-/object-visit-1.0.1.tgz
Source163: https://registry.npmjs.org/object.omit/-/object.omit-2.0.1.tgz
Source164: https://registry.npmjs.org/object.pick/-/object.pick-1.3.0.tgz
Source165: https://registry.npmjs.org/once/-/once-1.4.0.tgz
Source166: https://registry.npmjs.org/os-homedir/-/os-homedir-1.0.2.tgz
Source167: https://registry.npmjs.org/os-tmpdir/-/os-tmpdir-1.0.2.tgz
Source168: https://registry.npmjs.org/osenv/-/osenv-0.1.5.tgz
Source169: https://registry.npmjs.org/output-file-sync/-/output-file-sync-1.1.2.tgz
Source170: https://registry.npmjs.org/parse-glob/-/parse-glob-3.0.4.tgz
Source171: https://registry.npmjs.org/pascalcase/-/pascalcase-0.1.1.tgz
Source172: https://registry.npmjs.org/path-is-absolute/-/path-is-absolute-1.0.1.tgz
Source173: https://registry.npmjs.org/posix-character-classes/-/posix-character-classes-0.1.1.tgz
Source174: https://registry.npmjs.org/preserve/-/preserve-0.2.0.tgz
Source175: https://registry.npmjs.org/private/-/private-0.1.8.tgz
Source176: https://registry.npmjs.org/process-nextick-args/-/process-nextick-args-2.0.1.tgz
Source177: https://registry.npmjs.org/randomatic/-/randomatic-3.1.1.tgz
Source178: https://registry.npmjs.org/rc/-/rc-1.2.8.tgz
Source179: https://registry.npmjs.org/readable-stream/-/readable-stream-2.3.6.tgz
Source180: https://registry.npmjs.org/readdirp/-/readdirp-2.2.1.tgz
Source181: https://registry.npmjs.org/regenerator-runtime/-/regenerator-runtime-0.10.5.tgz
Source182: https://registry.npmjs.org/regenerator-runtime/-/regenerator-runtime-0.11.1.tgz
Source183: https://registry.npmjs.org/regex-cache/-/regex-cache-0.4.4.tgz
Source184: https://registry.npmjs.org/regex-not/-/regex-not-1.0.2.tgz
Source185: https://registry.npmjs.org/remove-trailing-separator/-/remove-trailing-separator-1.1.0.tgz
Source186: https://registry.npmjs.org/repeat-element/-/repeat-element-1.1.3.tgz
Source187: https://registry.npmjs.org/repeat-string/-/repeat-string-1.6.1.tgz
Source188: https://registry.npmjs.org/repeating/-/repeating-2.0.1.tgz
Source189: https://registry.npmjs.org/resolve-url/-/resolve-url-0.2.1.tgz
Source190: https://registry.npmjs.org/ret/-/ret-0.1.15.tgz
Source191: https://registry.npmjs.org/rimraf/-/rimraf-2.7.1.tgz
Source192: https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.1.2.tgz
Source193: https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.2.0.tgz
Source194: https://registry.npmjs.org/safe-regex/-/safe-regex-1.1.0.tgz
Source195: https://registry.npmjs.org/safer-buffer/-/safer-buffer-2.1.2.tgz
Source196: https://registry.npmjs.org/sax/-/sax-1.2.4.tgz
Source197: https://registry.npmjs.org/semver/-/semver-5.7.1.tgz
Source198: https://registry.npmjs.org/set-blocking/-/set-blocking-2.0.0.tgz
Source199: https://registry.npmjs.org/set-value/-/set-value-2.0.1.tgz
Source200: https://registry.npmjs.org/signal-exit/-/signal-exit-3.0.2.tgz
Source201: https://registry.npmjs.org/slash/-/slash-1.0.0.tgz
Source202: https://registry.npmjs.org/snapdragon/-/snapdragon-0.8.2.tgz
Source203: https://registry.npmjs.org/snapdragon-node/-/snapdragon-node-2.1.1.tgz
Source204: https://registry.npmjs.org/snapdragon-util/-/snapdragon-util-3.0.1.tgz
Source205: https://registry.npmjs.org/source-map/-/source-map-0.5.7.tgz
Source206: https://registry.npmjs.org/source-map-resolve/-/source-map-resolve-0.5.2.tgz
Source207: https://registry.npmjs.org/source-map-support/-/source-map-support-0.4.18.tgz
Source208: https://registry.npmjs.org/source-map-url/-/source-map-url-0.4.0.tgz
Source209: https://registry.npmjs.org/split-string/-/split-string-3.1.0.tgz
Source210: https://registry.npmjs.org/static-extend/-/static-extend-0.1.2.tgz
Source211: https://registry.npmjs.org/string_decoder/-/string_decoder-1.1.1.tgz
Source212: https://registry.npmjs.org/string-width/-/string-width-1.0.2.tgz
Source213: https://registry.npmjs.org/string-width/-/string-width-2.1.1.tgz
Source214: https://registry.npmjs.org/strip-ansi/-/strip-ansi-3.0.1.tgz
Source215: https://registry.npmjs.org/strip-ansi/-/strip-ansi-4.0.0.tgz
Source216: https://registry.npmjs.org/strip-json-comments/-/strip-json-comments-2.0.1.tgz
Source217: https://registry.npmjs.org/supports-color/-/supports-color-2.0.0.tgz
Source218: https://registry.npmjs.org/tar/-/tar-4.4.13.tgz
Source219: https://registry.npmjs.org/to-fast-properties/-/to-fast-properties-1.0.3.tgz
Source220: https://registry.npmjs.org/to-object-path/-/to-object-path-0.3.0.tgz
Source221: https://registry.npmjs.org/to-regex/-/to-regex-3.0.2.tgz
Source222: https://registry.npmjs.org/to-regex-range/-/to-regex-range-2.1.1.tgz
Source223: https://registry.npmjs.org/trim-right/-/trim-right-1.0.1.tgz
Source224: https://registry.npmjs.org/union-value/-/union-value-1.0.1.tgz
Source225: https://registry.npmjs.org/unset-value/-/unset-value-1.0.0.tgz
Source226: https://registry.npmjs.org/urix/-/urix-0.1.0.tgz
Source227: https://registry.npmjs.org/use/-/use-3.1.1.tgz
Source228: https://registry.npmjs.org/user-home/-/user-home-1.1.1.tgz
Source229: https://registry.npmjs.org/util-deprecate/-/util-deprecate-1.0.2.tgz
Source230: https://registry.npmjs.org/v8flags/-/v8flags-2.1.1.tgz
Source231: https://registry.npmjs.org/wide-align/-/wide-align-1.1.3.tgz
Source232: https://registry.npmjs.org/wrappy/-/wrappy-1.0.2.tgz
Source233: https://registry.npmjs.org/yallist/-/yallist-3.1.1.tgz
Source234: nodejs-babel-cli-%{version}-registry.npmjs.org.tgz
%if 0%{?scl:1}
BuildRequires: %{?scl_prefix_nodejs}npm
%else
BuildRequires: nodejs-packaging
BuildRequires: npm
%endif
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}
Provides: bundled(npm(abbrev)) = 1.1.1
Provides: bundled(npm(ansi-regex)) = 2.1.1
Provides: bundled(npm(ansi-regex)) = 3.0.0
Provides: bundled(npm(ansi-styles)) = 2.2.1
Provides: bundled(npm(anymatch)) = 1.3.2
Provides: bundled(npm(aproba)) = 1.2.0
Provides: bundled(npm(are-we-there-yet)) = 1.1.5
Provides: bundled(npm(arr-diff)) = 2.0.0
Provides: bundled(npm(arr-diff)) = 4.0.0
Provides: bundled(npm(arr-flatten)) = 1.1.0
Provides: bundled(npm(arr-union)) = 3.1.0
Provides: bundled(npm(array-unique)) = 0.2.1
Provides: bundled(npm(array-unique)) = 0.3.2
Provides: bundled(npm(assign-symbols)) = 1.0.0
Provides: bundled(npm(async-each)) = 1.0.3
Provides: bundled(npm(atob)) = 2.1.2
Provides: bundled(npm(babel-cli)) = 6.26.0
Provides: bundled(npm(babel-code-frame)) = 6.26.0
Provides: bundled(npm(babel-core)) = 6.26.3
Provides: bundled(npm(babel-generator)) = 6.26.1
Provides: bundled(npm(babel-helpers)) = 6.24.1
Provides: bundled(npm(babel-messages)) = 6.23.0
Provides: bundled(npm(babel-polyfill)) = 6.26.0
Provides: bundled(npm(babel-register)) = 6.26.0
Provides: bundled(npm(babel-runtime)) = 6.26.0
Provides: bundled(npm(babel-template)) = 6.26.0
Provides: bundled(npm(babel-traverse)) = 6.26.0
Provides: bundled(npm(babel-types)) = 6.26.0
Provides: bundled(npm(babylon)) = 6.18.0
Provides: bundled(npm(balanced-match)) = 1.0.0
Provides: bundled(npm(base)) = 0.11.2
Provides: bundled(npm(binary-extensions)) = 1.13.1
Provides: bundled(npm(brace-expansion)) = 1.1.11
Provides: bundled(npm(braces)) = 1.8.5
Provides: bundled(npm(braces)) = 2.3.2
Provides: bundled(npm(cache-base)) = 1.0.1
Provides: bundled(npm(chalk)) = 1.1.3
Provides: bundled(npm(chokidar)) = 1.7.0
Provides: bundled(npm(chownr)) = 1.1.3
Provides: bundled(npm(class-utils)) = 0.3.6
Provides: bundled(npm(code-point-at)) = 1.1.0
Provides: bundled(npm(collection-visit)) = 1.0.0
Provides: bundled(npm(commander)) = 2.20.1
Provides: bundled(npm(component-emitter)) = 1.3.0
Provides: bundled(npm(concat-map)) = 0.0.1
Provides: bundled(npm(console-control-strings)) = 1.1.0
Provides: bundled(npm(convert-source-map)) = 1.6.0
Provides: bundled(npm(copy-descriptor)) = 0.1.1
Provides: bundled(npm(core-js)) = 2.6.9
Provides: bundled(npm(core-util-is)) = 1.0.2
Provides: bundled(npm(debug)) = 2.6.9
Provides: bundled(npm(debug)) = 3.2.6
Provides: bundled(npm(decode-uri-component)) = 0.2.0
Provides: bundled(npm(deep-extend)) = 0.6.0
Provides: bundled(npm(define-property)) = 0.2.5
Provides: bundled(npm(define-property)) = 1.0.0
Provides: bundled(npm(define-property)) = 2.0.2
Provides: bundled(npm(delegates)) = 1.0.0
Provides: bundled(npm(detect-indent)) = 4.0.0
Provides: bundled(npm(detect-libc)) = 1.0.3
Provides: bundled(npm(escape-string-regexp)) = 1.0.5
Provides: bundled(npm(esutils)) = 2.0.3
Provides: bundled(npm(expand-brackets)) = 0.1.5
Provides: bundled(npm(expand-brackets)) = 2.1.4
Provides: bundled(npm(expand-range)) = 1.8.2
Provides: bundled(npm(extend-shallow)) = 2.0.1
Provides: bundled(npm(extend-shallow)) = 3.0.2
Provides: bundled(npm(extglob)) = 0.3.2
Provides: bundled(npm(extglob)) = 2.0.4
Provides: bundled(npm(filename-regex)) = 2.0.1
Provides: bundled(npm(fill-range)) = 2.2.4
Provides: bundled(npm(fill-range)) = 4.0.0
Provides: bundled(npm(for-in)) = 1.0.2
Provides: bundled(npm(for-own)) = 0.1.5
Provides: bundled(npm(fragment-cache)) = 0.2.1
Provides: bundled(npm(fs-minipass)) = 1.2.7
Provides: bundled(npm(fs-readdir-recursive)) = 1.1.0
Provides: bundled(npm(fs.realpath)) = 1.0.0
Provides: bundled(npm(fsevents)) = 1.2.9
Provides: bundled(npm(gauge)) = 2.7.4
Provides: bundled(npm(get-value)) = 2.0.6
Provides: bundled(npm(glob)) = 7.1.4
Provides: bundled(npm(glob-base)) = 0.3.0
Provides: bundled(npm(glob-parent)) = 2.0.0
Provides: bundled(npm(globals)) = 9.18.0
Provides: bundled(npm(graceful-fs)) = 4.2.2
Provides: bundled(npm(has-ansi)) = 2.0.0
Provides: bundled(npm(has-unicode)) = 2.0.1
Provides: bundled(npm(has-value)) = 0.3.1
Provides: bundled(npm(has-value)) = 1.0.0
Provides: bundled(npm(has-values)) = 0.1.4
Provides: bundled(npm(has-values)) = 1.0.0
Provides: bundled(npm(home-or-tmp)) = 2.0.0
Provides: bundled(npm(iconv-lite)) = 0.4.24
Provides: bundled(npm(ignore-walk)) = 3.0.2
Provides: bundled(npm(inflight)) = 1.0.6
Provides: bundled(npm(inherits)) = 2.0.4
Provides: bundled(npm(ini)) = 1.3.5
Provides: bundled(npm(invariant)) = 2.2.4
Provides: bundled(npm(is-accessor-descriptor)) = 0.1.6
Provides: bundled(npm(is-accessor-descriptor)) = 1.0.0
Provides: bundled(npm(is-binary-path)) = 1.0.1
Provides: bundled(npm(is-buffer)) = 1.1.6
Provides: bundled(npm(is-data-descriptor)) = 0.1.4
Provides: bundled(npm(is-data-descriptor)) = 1.0.0
Provides: bundled(npm(is-descriptor)) = 0.1.6
Provides: bundled(npm(is-descriptor)) = 1.0.2
Provides: bundled(npm(is-dotfile)) = 1.0.3
Provides: bundled(npm(is-equal-shallow)) = 0.1.3
Provides: bundled(npm(is-extendable)) = 0.1.1
Provides: bundled(npm(is-extendable)) = 1.0.1
Provides: bundled(npm(is-extglob)) = 1.0.0
Provides: bundled(npm(is-finite)) = 1.0.2
Provides: bundled(npm(is-fullwidth-code-point)) = 1.0.0
Provides: bundled(npm(is-fullwidth-code-point)) = 2.0.0
Provides: bundled(npm(is-glob)) = 2.0.1
Provides: bundled(npm(is-number)) = 2.1.0
Provides: bundled(npm(is-number)) = 3.0.0
Provides: bundled(npm(is-number)) = 4.0.0
Provides: bundled(npm(is-plain-object)) = 2.0.4
Provides: bundled(npm(is-posix-bracket)) = 0.1.1
Provides: bundled(npm(is-primitive)) = 2.0.0
Provides: bundled(npm(is-windows)) = 1.0.2
Provides: bundled(npm(isarray)) = 1.0.0
Provides: bundled(npm(isobject)) = 2.1.0
Provides: bundled(npm(isobject)) = 3.0.1
Provides: bundled(npm(js-tokens)) = 3.0.2
Provides: bundled(npm(js-tokens)) = 4.0.0
Provides: bundled(npm(jsesc)) = 1.3.0
Provides: bundled(npm(json5)) = 0.5.1
Provides: bundled(npm(kind-of)) = 3.2.2
Provides: bundled(npm(kind-of)) = 4.0.0
Provides: bundled(npm(kind-of)) = 5.1.0
Provides: bundled(npm(kind-of)) = 6.0.2
Provides: bundled(npm(lodash)) = 4.17.15
Provides: bundled(npm(loose-envify)) = 1.4.0
Provides: bundled(npm(map-cache)) = 0.2.2
Provides: bundled(npm(map-visit)) = 1.0.0
Provides: bundled(npm(math-random)) = 1.0.4
Provides: bundled(npm(micromatch)) = 2.3.11
Provides: bundled(npm(micromatch)) = 3.1.10
Provides: bundled(npm(minimatch)) = 3.0.4
Provides: bundled(npm(minimist)) = 0.0.8
Provides: bundled(npm(minimist)) = 1.2.0
Provides: bundled(npm(minipass)) = 2.9.0
Provides: bundled(npm(minizlib)) = 1.3.3
Provides: bundled(npm(mixin-deep)) = 1.3.2
Provides: bundled(npm(mkdirp)) = 0.5.1
Provides: bundled(npm(ms)) = 2.0.0
Provides: bundled(npm(ms)) = 2.1.2
Provides: bundled(npm(nan)) = 2.14.0
Provides: bundled(npm(nanomatch)) = 1.2.13
Provides: bundled(npm(needle)) = 2.4.0
Provides: bundled(npm(node-pre-gyp)) = 0.12.0
Provides: bundled(npm(nopt)) = 4.0.1
Provides: bundled(npm(normalize-path)) = 2.1.1
Provides: bundled(npm(npm-bundled)) = 1.0.6
Provides: bundled(npm(npm-packlist)) = 1.4.4
Provides: bundled(npm(npmlog)) = 4.1.2
Provides: bundled(npm(number-is-nan)) = 1.0.1
Provides: bundled(npm(object-assign)) = 4.1.1
Provides: bundled(npm(object-copy)) = 0.1.0
Provides: bundled(npm(object-visit)) = 1.0.1
Provides: bundled(npm(object.omit)) = 2.0.1
Provides: bundled(npm(object.pick)) = 1.3.0
Provides: bundled(npm(once)) = 1.4.0
Provides: bundled(npm(os-homedir)) = 1.0.2
Provides: bundled(npm(os-tmpdir)) = 1.0.2
Provides: bundled(npm(osenv)) = 0.1.5
Provides: bundled(npm(output-file-sync)) = 1.1.2
Provides: bundled(npm(parse-glob)) = 3.0.4
Provides: bundled(npm(pascalcase)) = 0.1.1
Provides: bundled(npm(path-is-absolute)) = 1.0.1
Provides: bundled(npm(posix-character-classes)) = 0.1.1
Provides: bundled(npm(preserve)) = 0.2.0
Provides: bundled(npm(private)) = 0.1.8
Provides: bundled(npm(process-nextick-args)) = 2.0.1
Provides: bundled(npm(randomatic)) = 3.1.1
Provides: bundled(npm(rc)) = 1.2.8
Provides: bundled(npm(readable-stream)) = 2.3.6
Provides: bundled(npm(readdirp)) = 2.2.1
Provides: bundled(npm(regenerator-runtime)) = 0.10.5
Provides: bundled(npm(regenerator-runtime)) = 0.11.1
Provides: bundled(npm(regex-cache)) = 0.4.4
Provides: bundled(npm(regex-not)) = 1.0.2
Provides: bundled(npm(remove-trailing-separator)) = 1.1.0
Provides: bundled(npm(repeat-element)) = 1.1.3
Provides: bundled(npm(repeat-string)) = 1.6.1
Provides: bundled(npm(repeating)) = 2.0.1
Provides: bundled(npm(resolve-url)) = 0.2.1
Provides: bundled(npm(ret)) = 0.1.15
Provides: bundled(npm(rimraf)) = 2.7.1
Provides: bundled(npm(safe-buffer)) = 5.1.2
Provides: bundled(npm(safe-buffer)) = 5.2.0
Provides: bundled(npm(safe-regex)) = 1.1.0
Provides: bundled(npm(safer-buffer)) = 2.1.2
Provides: bundled(npm(sax)) = 1.2.4
Provides: bundled(npm(semver)) = 5.7.1
Provides: bundled(npm(set-blocking)) = 2.0.0
Provides: bundled(npm(set-value)) = 2.0.1
Provides: bundled(npm(signal-exit)) = 3.0.2
Provides: bundled(npm(slash)) = 1.0.0
Provides: bundled(npm(snapdragon)) = 0.8.2
Provides: bundled(npm(snapdragon-node)) = 2.1.1
Provides: bundled(npm(snapdragon-util)) = 3.0.1
Provides: bundled(npm(source-map)) = 0.5.7
Provides: bundled(npm(source-map-resolve)) = 0.5.2
Provides: bundled(npm(source-map-support)) = 0.4.18
Provides: bundled(npm(source-map-url)) = 0.4.0
Provides: bundled(npm(split-string)) = 3.1.0
Provides: bundled(npm(static-extend)) = 0.1.2
Provides: bundled(npm(string_decoder)) = 1.1.1
Provides: bundled(npm(string-width)) = 1.0.2
Provides: bundled(npm(string-width)) = 2.1.1
Provides: bundled(npm(strip-ansi)) = 3.0.1
Provides: bundled(npm(strip-ansi)) = 4.0.0
Provides: bundled(npm(strip-json-comments)) = 2.0.1
Provides: bundled(npm(supports-color)) = 2.0.0
Provides: bundled(npm(tar)) = 4.4.13
Provides: bundled(npm(to-fast-properties)) = 1.0.3
Provides: bundled(npm(to-object-path)) = 0.3.0
Provides: bundled(npm(to-regex)) = 3.0.2
Provides: bundled(npm(to-regex-range)) = 2.1.1
Provides: bundled(npm(trim-right)) = 1.0.1
Provides: bundled(npm(union-value)) = 1.0.1
Provides: bundled(npm(unset-value)) = 1.0.0
Provides: bundled(npm(urix)) = 0.1.0
Provides: bundled(npm(use)) = 3.1.1
Provides: bundled(npm(user-home)) = 1.1.1
Provides: bundled(npm(util-deprecate)) = 1.0.2
Provides: bundled(npm(v8flags)) = 2.1.1
Provides: bundled(npm(wide-align)) = 1.1.3
Provides: bundled(npm(wrappy)) = 1.0.2
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

%setup -T -q -a 234 -D -n %{npm_cache_dir}

%build
%{?scl:scl enable %{?scl_nodejs} - << \end_of_scl}
npm install --cache-min Infinity --cache %{?scl:../}%{npm_cache_dir} --no-shrinkwrap --no-optional --global-style true %{npm_name}@%{version}
%{?scl:end_of_scl}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/bin %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/index.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/lib %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/scripts %{buildroot}%{nodejs_sitelib}/%{npm_name}

mkdir -p %{buildroot}%{_bindir}/
chmod 0755 %{buildroot}%{nodejs_sitelib}/%{npm_name}/bin/babel-doctor.js
ln -sf %{nodejs_sitelib}/%{npm_name}/bin/babel-doctor.js %{buildroot}%{_bindir}/babel-doctor
chmod 0755 %{buildroot}%{nodejs_sitelib}/%{npm_name}/bin/babel.js
ln -sf %{nodejs_sitelib}/%{npm_name}/bin/babel.js %{buildroot}%{_bindir}/babel
chmod 0755 %{buildroot}%{nodejs_sitelib}/%{npm_name}/bin/babel-node.js
ln -sf %{nodejs_sitelib}/%{npm_name}/bin/babel-node.js %{buildroot}%{_bindir}/babel-node
chmod 0755 %{buildroot}%{nodejs_sitelib}/%{npm_name}/bin/babel-external-helpers.js
ln -sf %{nodejs_sitelib}/%{npm_name}/bin/babel-external-helpers.js %{buildroot}%{_bindir}/babel-external-helpers

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%{_bindir}/babel-doctor
%{_bindir}/babel
%{_bindir}/babel-node
%{_bindir}/babel-external-helpers
%doc node_modules/%{npm_name}/README.md

%changelog
* Tue Mar 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 6.26.0-4
- Bump packages to build for el8

* Mon Oct 21 2019 Eric D. Helms <ericdhelms@gmail.com> - 6.26.0-3
- Build for SCL

* Fri Oct 04 2019 Eric D. Helms <ericdhelms@gmail.com> - 6.26.0-2
- Update specs to handle SCL

* Tue Nov 07 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 6.26.0-1
- new package built with tito
