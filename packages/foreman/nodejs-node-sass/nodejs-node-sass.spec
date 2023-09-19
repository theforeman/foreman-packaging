%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global debug_package %{nil}
%global __debug_install_post /bin/true
%global npm_name node-sass

Name: %{?scl_prefix}nodejs-node-sass
Version: 4.14.1
Release: 2%{?dist}
Summary: Wrapper around libsass
License: MIT
Group: Development/Libraries
URL: https://github.com/sass/node-sass
Source0: https://registry.npmjs.org/abbrev/-/abbrev-1.1.1.tgz
Source1: https://registry.npmjs.org/ajv/-/ajv-6.12.6.tgz
Source2: https://registry.npmjs.org/amdefine/-/amdefine-1.0.1.tgz
Source3: https://registry.npmjs.org/ansi-regex/-/ansi-regex-2.1.1.tgz
Source4: https://registry.npmjs.org/ansi-regex/-/ansi-regex-4.1.1.tgz
Source5: https://registry.npmjs.org/ansi-regex/-/ansi-regex-5.0.1.tgz
Source6: https://registry.npmjs.org/ansi-styles/-/ansi-styles-2.2.1.tgz
Source7: https://registry.npmjs.org/ansi-styles/-/ansi-styles-3.2.1.tgz
Source8: https://registry.npmjs.org/aproba/-/aproba-1.2.0.tgz
Source9: https://registry.npmjs.org/are-we-there-yet/-/are-we-there-yet-1.1.7.tgz
Source10: https://registry.npmjs.org/array-find-index/-/array-find-index-1.0.2.tgz
Source11: https://registry.npmjs.org/asn1/-/asn1-0.2.6.tgz
Source12: https://registry.npmjs.org/assert-plus/-/assert-plus-1.0.0.tgz
Source13: https://registry.npmjs.org/async-foreach/-/async-foreach-0.1.3.tgz
Source14: https://registry.npmjs.org/asynckit/-/asynckit-0.4.0.tgz
Source15: https://registry.npmjs.org/aws-sign2/-/aws-sign2-0.7.0.tgz
Source16: https://registry.npmjs.org/aws4/-/aws4-1.12.0.tgz
Source17: https://registry.npmjs.org/balanced-match/-/balanced-match-1.0.2.tgz
Source18: https://registry.npmjs.org/bcrypt-pbkdf/-/bcrypt-pbkdf-1.0.2.tgz
Source19: https://registry.npmjs.org/block-stream/-/block-stream-0.0.9.tgz
Source20: https://registry.npmjs.org/brace-expansion/-/brace-expansion-1.1.11.tgz
Source21: https://registry.npmjs.org/camelcase/-/camelcase-2.1.1.tgz
Source22: https://registry.npmjs.org/camelcase/-/camelcase-5.3.1.tgz
Source23: https://registry.npmjs.org/camelcase-keys/-/camelcase-keys-2.1.0.tgz
Source24: https://registry.npmjs.org/caseless/-/caseless-0.12.0.tgz
Source25: https://registry.npmjs.org/chalk/-/chalk-1.1.3.tgz
Source26: https://registry.npmjs.org/cliui/-/cliui-5.0.0.tgz
Source27: https://registry.npmjs.org/code-point-at/-/code-point-at-1.1.0.tgz
Source28: https://registry.npmjs.org/color-convert/-/color-convert-1.9.3.tgz
Source29: https://registry.npmjs.org/color-name/-/color-name-1.1.3.tgz
Source30: https://registry.npmjs.org/combined-stream/-/combined-stream-1.0.8.tgz
Source31: https://registry.npmjs.org/concat-map/-/concat-map-0.0.1.tgz
Source32: https://registry.npmjs.org/console-control-strings/-/console-control-strings-1.1.0.tgz
Source33: https://registry.npmjs.org/core-util-is/-/core-util-is-1.0.2.tgz
Source34: https://registry.npmjs.org/core-util-is/-/core-util-is-1.0.3.tgz
Source35: https://registry.npmjs.org/cross-spawn/-/cross-spawn-3.0.1.tgz
Source36: https://registry.npmjs.org/currently-unhandled/-/currently-unhandled-0.4.1.tgz
Source37: https://registry.npmjs.org/dashdash/-/dashdash-1.14.1.tgz
Source38: https://registry.npmjs.org/decamelize/-/decamelize-1.2.0.tgz
Source39: https://registry.npmjs.org/delayed-stream/-/delayed-stream-1.0.0.tgz
Source40: https://registry.npmjs.org/delegates/-/delegates-1.0.0.tgz
Source41: https://registry.npmjs.org/ecc-jsbn/-/ecc-jsbn-0.1.2.tgz
Source42: https://registry.npmjs.org/emoji-regex/-/emoji-regex-7.0.3.tgz
Source43: https://registry.npmjs.org/emoji-regex/-/emoji-regex-8.0.0.tgz
Source44: https://registry.npmjs.org/error-ex/-/error-ex-1.3.2.tgz
Source45: https://registry.npmjs.org/escape-string-regexp/-/escape-string-regexp-1.0.5.tgz
Source46: https://registry.npmjs.org/extend/-/extend-3.0.2.tgz
Source47: https://registry.npmjs.org/extsprintf/-/extsprintf-1.3.0.tgz
Source48: https://registry.npmjs.org/extsprintf/-/extsprintf-1.4.1.tgz
Source49: https://registry.npmjs.org/fast-deep-equal/-/fast-deep-equal-3.1.3.tgz
Source50: https://registry.npmjs.org/fast-json-stable-stringify/-/fast-json-stable-stringify-2.1.0.tgz
Source51: https://registry.npmjs.org/find-up/-/find-up-1.1.2.tgz
Source52: https://registry.npmjs.org/find-up/-/find-up-3.0.0.tgz
Source53: https://registry.npmjs.org/forever-agent/-/forever-agent-0.6.1.tgz
Source54: https://registry.npmjs.org/form-data/-/form-data-2.3.3.tgz
Source55: https://registry.npmjs.org/fs.realpath/-/fs.realpath-1.0.0.tgz
Source56: https://registry.npmjs.org/fstream/-/fstream-1.0.12.tgz
Source57: https://registry.npmjs.org/function-bind/-/function-bind-1.1.1.tgz
Source58: https://registry.npmjs.org/gauge/-/gauge-2.7.4.tgz
Source59: https://registry.npmjs.org/gaze/-/gaze-1.1.3.tgz
Source60: https://registry.npmjs.org/get-caller-file/-/get-caller-file-2.0.5.tgz
Source61: https://registry.npmjs.org/get-stdin/-/get-stdin-4.0.1.tgz
Source62: https://registry.npmjs.org/getpass/-/getpass-0.1.7.tgz
Source63: https://registry.npmjs.org/glob/-/glob-7.1.7.tgz
Source64: https://registry.npmjs.org/glob/-/glob-7.2.3.tgz
Source65: https://registry.npmjs.org/globule/-/globule-1.3.4.tgz
Source66: https://registry.npmjs.org/graceful-fs/-/graceful-fs-4.2.11.tgz
Source67: https://registry.npmjs.org/har-schema/-/har-schema-2.0.0.tgz
Source68: https://registry.npmjs.org/har-validator/-/har-validator-5.1.5.tgz
Source69: https://registry.npmjs.org/has/-/has-1.0.3.tgz
Source70: https://registry.npmjs.org/has-ansi/-/has-ansi-2.0.0.tgz
Source71: https://registry.npmjs.org/has-unicode/-/has-unicode-2.0.1.tgz
Source72: https://registry.npmjs.org/hosted-git-info/-/hosted-git-info-2.8.9.tgz
Source73: https://registry.npmjs.org/http-signature/-/http-signature-1.2.0.tgz
Source74: https://registry.npmjs.org/in-publish/-/in-publish-2.0.1.tgz
Source75: https://registry.npmjs.org/indent-string/-/indent-string-2.1.0.tgz
Source76: https://registry.npmjs.org/inflight/-/inflight-1.0.6.tgz
Source77: https://registry.npmjs.org/inherits/-/inherits-2.0.4.tgz
Source78: https://registry.npmjs.org/is-arrayish/-/is-arrayish-0.2.1.tgz
Source79: https://registry.npmjs.org/is-core-module/-/is-core-module-2.13.0.tgz
Source80: https://registry.npmjs.org/is-finite/-/is-finite-1.1.0.tgz
Source81: https://registry.npmjs.org/is-fullwidth-code-point/-/is-fullwidth-code-point-1.0.0.tgz
Source82: https://registry.npmjs.org/is-fullwidth-code-point/-/is-fullwidth-code-point-2.0.0.tgz
Source83: https://registry.npmjs.org/is-fullwidth-code-point/-/is-fullwidth-code-point-3.0.0.tgz
Source84: https://registry.npmjs.org/is-typedarray/-/is-typedarray-1.0.0.tgz
Source85: https://registry.npmjs.org/is-utf8/-/is-utf8-0.2.1.tgz
Source86: https://registry.npmjs.org/isarray/-/isarray-1.0.0.tgz
Source87: https://registry.npmjs.org/isexe/-/isexe-2.0.0.tgz
Source88: https://registry.npmjs.org/isstream/-/isstream-0.1.2.tgz
Source89: https://registry.npmjs.org/js-base64/-/js-base64-2.6.4.tgz
Source90: https://registry.npmjs.org/jsbn/-/jsbn-0.1.1.tgz
Source91: https://registry.npmjs.org/json-schema/-/json-schema-0.4.0.tgz
Source92: https://registry.npmjs.org/json-schema-traverse/-/json-schema-traverse-0.4.1.tgz
Source93: https://registry.npmjs.org/json-stringify-safe/-/json-stringify-safe-5.0.1.tgz
Source94: https://registry.npmjs.org/jsprim/-/jsprim-1.4.2.tgz
Source95: https://registry.npmjs.org/load-json-file/-/load-json-file-1.1.0.tgz
Source96: https://registry.npmjs.org/locate-path/-/locate-path-3.0.0.tgz
Source97: https://registry.npmjs.org/lodash/-/lodash-4.17.21.tgz
Source98: https://registry.npmjs.org/loud-rejection/-/loud-rejection-1.6.0.tgz
Source99: https://registry.npmjs.org/lru-cache/-/lru-cache-4.1.5.tgz
Source100: https://registry.npmjs.org/map-obj/-/map-obj-1.0.1.tgz
Source101: https://registry.npmjs.org/meow/-/meow-3.7.0.tgz
Source102: https://registry.npmjs.org/mime-db/-/mime-db-1.52.0.tgz
Source103: https://registry.npmjs.org/mime-types/-/mime-types-2.1.35.tgz
Source104: https://registry.npmjs.org/minimatch/-/minimatch-3.0.8.tgz
Source105: https://registry.npmjs.org/minimatch/-/minimatch-3.1.2.tgz
Source106: https://registry.npmjs.org/minimist/-/minimist-1.2.8.tgz
Source107: https://registry.npmjs.org/mkdirp/-/mkdirp-0.5.6.tgz
Source108: https://registry.npmjs.org/nan/-/nan-2.18.0.tgz
Source109: https://registry.npmjs.org/node-gyp/-/node-gyp-3.8.0.tgz
Source110: https://registry.npmjs.org/node-sass/-/node-sass-4.14.1.tgz
Source111: https://registry.npmjs.org/nopt/-/nopt-3.0.6.tgz
Source112: https://registry.npmjs.org/normalize-package-data/-/normalize-package-data-2.5.0.tgz
Source113: https://registry.npmjs.org/npmlog/-/npmlog-4.1.2.tgz
Source114: https://registry.npmjs.org/number-is-nan/-/number-is-nan-1.0.1.tgz
Source115: https://registry.npmjs.org/oauth-sign/-/oauth-sign-0.9.0.tgz
Source116: https://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz
Source117: https://registry.npmjs.org/once/-/once-1.4.0.tgz
Source118: https://registry.npmjs.org/os-homedir/-/os-homedir-1.0.2.tgz
Source119: https://registry.npmjs.org/os-tmpdir/-/os-tmpdir-1.0.2.tgz
Source120: https://registry.npmjs.org/osenv/-/osenv-0.1.5.tgz
Source121: https://registry.npmjs.org/p-limit/-/p-limit-2.3.0.tgz
Source122: https://registry.npmjs.org/p-locate/-/p-locate-3.0.0.tgz
Source123: https://registry.npmjs.org/p-try/-/p-try-2.2.0.tgz
Source124: https://registry.npmjs.org/parse-json/-/parse-json-2.2.0.tgz
Source125: https://registry.npmjs.org/path-exists/-/path-exists-2.1.0.tgz
Source126: https://registry.npmjs.org/path-exists/-/path-exists-3.0.0.tgz
Source127: https://registry.npmjs.org/path-is-absolute/-/path-is-absolute-1.0.1.tgz
Source128: https://registry.npmjs.org/path-parse/-/path-parse-1.0.7.tgz
Source129: https://registry.npmjs.org/path-type/-/path-type-1.1.0.tgz
Source130: https://registry.npmjs.org/performance-now/-/performance-now-2.1.0.tgz
Source131: https://registry.npmjs.org/pify/-/pify-2.3.0.tgz
Source132: https://registry.npmjs.org/pinkie/-/pinkie-2.0.4.tgz
Source133: https://registry.npmjs.org/pinkie-promise/-/pinkie-promise-2.0.1.tgz
Source134: https://registry.npmjs.org/process-nextick-args/-/process-nextick-args-2.0.1.tgz
Source135: https://registry.npmjs.org/pseudomap/-/pseudomap-1.0.2.tgz
Source136: https://registry.npmjs.org/psl/-/psl-1.9.0.tgz
Source137: https://registry.npmjs.org/punycode/-/punycode-2.3.0.tgz
Source138: https://registry.npmjs.org/qs/-/qs-6.5.3.tgz
Source139: https://registry.npmjs.org/read-pkg/-/read-pkg-1.1.0.tgz
Source140: https://registry.npmjs.org/read-pkg-up/-/read-pkg-up-1.0.1.tgz
Source141: https://registry.npmjs.org/readable-stream/-/readable-stream-2.3.8.tgz
Source142: https://registry.npmjs.org/redent/-/redent-1.0.0.tgz
Source143: https://registry.npmjs.org/repeating/-/repeating-2.0.1.tgz
Source144: https://registry.npmjs.org/request/-/request-2.88.2.tgz
Source145: https://registry.npmjs.org/require-directory/-/require-directory-2.1.1.tgz
Source146: https://registry.npmjs.org/require-main-filename/-/require-main-filename-2.0.0.tgz
Source147: https://registry.npmjs.org/resolve/-/resolve-1.22.4.tgz
Source148: https://registry.npmjs.org/rimraf/-/rimraf-2.7.1.tgz
Source149: https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.1.2.tgz
Source150: https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.2.1.tgz
Source151: https://registry.npmjs.org/safer-buffer/-/safer-buffer-2.1.2.tgz
Source152: https://registry.npmjs.org/sass-graph/-/sass-graph-2.2.5.tgz
Source153: https://registry.npmjs.org/scss-tokenizer/-/scss-tokenizer-0.2.3.tgz
Source154: https://registry.npmjs.org/semver/-/semver-5.3.0.tgz
Source155: https://registry.npmjs.org/semver/-/semver-5.7.2.tgz
Source156: https://registry.npmjs.org/set-blocking/-/set-blocking-2.0.0.tgz
Source157: https://registry.npmjs.org/signal-exit/-/signal-exit-3.0.7.tgz
Source158: https://registry.npmjs.org/source-map/-/source-map-0.4.4.tgz
Source159: https://registry.npmjs.org/spdx-correct/-/spdx-correct-3.2.0.tgz
Source160: https://registry.npmjs.org/spdx-exceptions/-/spdx-exceptions-2.3.0.tgz
Source161: https://registry.npmjs.org/spdx-expression-parse/-/spdx-expression-parse-3.0.1.tgz
Source162: https://registry.npmjs.org/spdx-license-ids/-/spdx-license-ids-3.0.13.tgz
Source163: https://registry.npmjs.org/sshpk/-/sshpk-1.17.0.tgz
Source164: https://registry.npmjs.org/stdout-stream/-/stdout-stream-1.4.1.tgz
Source165: https://registry.npmjs.org/string_decoder/-/string_decoder-1.1.1.tgz
Source166: https://registry.npmjs.org/string-width/-/string-width-1.0.2.tgz
Source167: https://registry.npmjs.org/string-width/-/string-width-3.1.0.tgz
Source168: https://registry.npmjs.org/string-width/-/string-width-4.2.3.tgz
Source169: https://registry.npmjs.org/strip-ansi/-/strip-ansi-3.0.1.tgz
Source170: https://registry.npmjs.org/strip-ansi/-/strip-ansi-5.2.0.tgz
Source171: https://registry.npmjs.org/strip-ansi/-/strip-ansi-6.0.1.tgz
Source172: https://registry.npmjs.org/strip-bom/-/strip-bom-2.0.0.tgz
Source173: https://registry.npmjs.org/strip-indent/-/strip-indent-1.0.1.tgz
Source174: https://registry.npmjs.org/supports-color/-/supports-color-2.0.0.tgz
Source175: https://registry.npmjs.org/supports-preserve-symlinks-flag/-/supports-preserve-symlinks-flag-1.0.0.tgz
Source176: https://registry.npmjs.org/tar/-/tar-2.2.2.tgz
Source177: https://registry.npmjs.org/tough-cookie/-/tough-cookie-2.5.0.tgz
Source178: https://registry.npmjs.org/trim-newlines/-/trim-newlines-1.0.0.tgz
Source179: https://registry.npmjs.org/true-case-path/-/true-case-path-1.0.3.tgz
Source180: https://registry.npmjs.org/tunnel-agent/-/tunnel-agent-0.6.0.tgz
Source181: https://registry.npmjs.org/tweetnacl/-/tweetnacl-0.14.5.tgz
Source182: https://registry.npmjs.org/uri-js/-/uri-js-4.4.1.tgz
Source183: https://registry.npmjs.org/util-deprecate/-/util-deprecate-1.0.2.tgz
Source184: https://registry.npmjs.org/uuid/-/uuid-3.4.0.tgz
Source185: https://registry.npmjs.org/validate-npm-package-license/-/validate-npm-package-license-3.0.4.tgz
Source186: https://registry.npmjs.org/verror/-/verror-1.10.0.tgz
Source187: https://registry.npmjs.org/which/-/which-1.3.1.tgz
Source188: https://registry.npmjs.org/which-module/-/which-module-2.0.1.tgz
Source189: https://registry.npmjs.org/wide-align/-/wide-align-1.1.5.tgz
Source190: https://registry.npmjs.org/wrap-ansi/-/wrap-ansi-5.1.0.tgz
Source191: https://registry.npmjs.org/wrappy/-/wrappy-1.0.2.tgz
Source192: https://registry.npmjs.org/y18n/-/y18n-4.0.3.tgz
Source193: https://registry.npmjs.org/yallist/-/yallist-2.1.2.tgz
Source194: https://registry.npmjs.org/yargs/-/yargs-13.3.2.tgz
Source195: https://registry.npmjs.org/yargs-parser/-/yargs-parser-13.1.2.tgz
Source196: nodejs-node-sass-%{version}-registry.npmjs.org.tgz

BuildRequires: npm
BuildRequires: nodejs-node-gyp
BuildRequires: nodejs-devel
BuildRequires: nodejs-packaging
BuildRequires: npm
BuildRequires: python3

ExclusiveArch: x86_64

Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}
Provides: bundled(npm(abbrev)) = 1.1.1
Provides: bundled(npm(ajv)) = 6.12.6
Provides: bundled(npm(amdefine)) = 1.0.1
Provides: bundled(npm(ansi-regex)) = 2.1.1
Provides: bundled(npm(ansi-regex)) = 4.1.1
Provides: bundled(npm(ansi-regex)) = 5.0.1
Provides: bundled(npm(ansi-styles)) = 2.2.1
Provides: bundled(npm(ansi-styles)) = 3.2.1
Provides: bundled(npm(aproba)) = 1.2.0
Provides: bundled(npm(are-we-there-yet)) = 1.1.7
Provides: bundled(npm(array-find-index)) = 1.0.2
Provides: bundled(npm(asn1)) = 0.2.6
Provides: bundled(npm(assert-plus)) = 1.0.0
Provides: bundled(npm(async-foreach)) = 0.1.3
Provides: bundled(npm(asynckit)) = 0.4.0
Provides: bundled(npm(aws-sign2)) = 0.7.0
Provides: bundled(npm(aws4)) = 1.12.0
Provides: bundled(npm(balanced-match)) = 1.0.2
Provides: bundled(npm(bcrypt-pbkdf)) = 1.0.2
Provides: bundled(npm(block-stream)) = 0.0.9
Provides: bundled(npm(brace-expansion)) = 1.1.11
Provides: bundled(npm(camelcase)) = 2.1.1
Provides: bundled(npm(camelcase)) = 5.3.1
Provides: bundled(npm(camelcase-keys)) = 2.1.0
Provides: bundled(npm(caseless)) = 0.12.0
Provides: bundled(npm(chalk)) = 1.1.3
Provides: bundled(npm(cliui)) = 5.0.0
Provides: bundled(npm(code-point-at)) = 1.1.0
Provides: bundled(npm(color-convert)) = 1.9.3
Provides: bundled(npm(color-name)) = 1.1.3
Provides: bundled(npm(combined-stream)) = 1.0.8
Provides: bundled(npm(concat-map)) = 0.0.1
Provides: bundled(npm(console-control-strings)) = 1.1.0
Provides: bundled(npm(core-util-is)) = 1.0.2
Provides: bundled(npm(core-util-is)) = 1.0.3
Provides: bundled(npm(cross-spawn)) = 3.0.1
Provides: bundled(npm(currently-unhandled)) = 0.4.1
Provides: bundled(npm(dashdash)) = 1.14.1
Provides: bundled(npm(decamelize)) = 1.2.0
Provides: bundled(npm(delayed-stream)) = 1.0.0
Provides: bundled(npm(delegates)) = 1.0.0
Provides: bundled(npm(ecc-jsbn)) = 0.1.2
Provides: bundled(npm(emoji-regex)) = 7.0.3
Provides: bundled(npm(emoji-regex)) = 8.0.0
Provides: bundled(npm(error-ex)) = 1.3.2
Provides: bundled(npm(escape-string-regexp)) = 1.0.5
Provides: bundled(npm(extend)) = 3.0.2
Provides: bundled(npm(extsprintf)) = 1.3.0
Provides: bundled(npm(extsprintf)) = 1.4.1
Provides: bundled(npm(fast-deep-equal)) = 3.1.3
Provides: bundled(npm(fast-json-stable-stringify)) = 2.1.0
Provides: bundled(npm(find-up)) = 1.1.2
Provides: bundled(npm(find-up)) = 3.0.0
Provides: bundled(npm(forever-agent)) = 0.6.1
Provides: bundled(npm(form-data)) = 2.3.3
Provides: bundled(npm(fs.realpath)) = 1.0.0
Provides: bundled(npm(fstream)) = 1.0.12
Provides: bundled(npm(function-bind)) = 1.1.1
Provides: bundled(npm(gauge)) = 2.7.4
Provides: bundled(npm(gaze)) = 1.1.3
Provides: bundled(npm(get-caller-file)) = 2.0.5
Provides: bundled(npm(get-stdin)) = 4.0.1
Provides: bundled(npm(getpass)) = 0.1.7
Provides: bundled(npm(glob)) = 7.1.7
Provides: bundled(npm(glob)) = 7.2.3
Provides: bundled(npm(globule)) = 1.3.4
Provides: bundled(npm(graceful-fs)) = 4.2.11
Provides: bundled(npm(har-schema)) = 2.0.0
Provides: bundled(npm(har-validator)) = 5.1.5
Provides: bundled(npm(has)) = 1.0.3
Provides: bundled(npm(has-ansi)) = 2.0.0
Provides: bundled(npm(has-unicode)) = 2.0.1
Provides: bundled(npm(hosted-git-info)) = 2.8.9
Provides: bundled(npm(http-signature)) = 1.2.0
Provides: bundled(npm(in-publish)) = 2.0.1
Provides: bundled(npm(indent-string)) = 2.1.0
Provides: bundled(npm(inflight)) = 1.0.6
Provides: bundled(npm(inherits)) = 2.0.4
Provides: bundled(npm(is-arrayish)) = 0.2.1
Provides: bundled(npm(is-core-module)) = 2.13.0
Provides: bundled(npm(is-finite)) = 1.1.0
Provides: bundled(npm(is-fullwidth-code-point)) = 1.0.0
Provides: bundled(npm(is-fullwidth-code-point)) = 2.0.0
Provides: bundled(npm(is-fullwidth-code-point)) = 3.0.0
Provides: bundled(npm(is-typedarray)) = 1.0.0
Provides: bundled(npm(is-utf8)) = 0.2.1
Provides: bundled(npm(isarray)) = 1.0.0
Provides: bundled(npm(isexe)) = 2.0.0
Provides: bundled(npm(isstream)) = 0.1.2
Provides: bundled(npm(js-base64)) = 2.6.4
Provides: bundled(npm(jsbn)) = 0.1.1
Provides: bundled(npm(json-schema)) = 0.4.0
Provides: bundled(npm(json-schema-traverse)) = 0.4.1
Provides: bundled(npm(json-stringify-safe)) = 5.0.1
Provides: bundled(npm(jsprim)) = 1.4.2
Provides: bundled(npm(load-json-file)) = 1.1.0
Provides: bundled(npm(locate-path)) = 3.0.0
Provides: bundled(npm(lodash)) = 4.17.21
Provides: bundled(npm(loud-rejection)) = 1.6.0
Provides: bundled(npm(lru-cache)) = 4.1.5
Provides: bundled(npm(map-obj)) = 1.0.1
Provides: bundled(npm(meow)) = 3.7.0
Provides: bundled(npm(mime-db)) = 1.52.0
Provides: bundled(npm(mime-types)) = 2.1.35
Provides: bundled(npm(minimatch)) = 3.0.8
Provides: bundled(npm(minimatch)) = 3.1.2
Provides: bundled(npm(minimist)) = 1.2.8
Provides: bundled(npm(mkdirp)) = 0.5.6
Provides: bundled(npm(nan)) = 2.18.0
Provides: bundled(npm(node-gyp)) = 3.8.0
Provides: bundled(npm(node-sass)) = 4.14.1
Provides: bundled(npm(nopt)) = 3.0.6
Provides: bundled(npm(normalize-package-data)) = 2.5.0
Provides: bundled(npm(npmlog)) = 4.1.2
Provides: bundled(npm(number-is-nan)) = 1.0.1
Provides: bundled(npm(oauth-sign)) = 0.9.0
Provides: bundled(npm(object-assign)) = 4.1.1
Provides: bundled(npm(once)) = 1.4.0
Provides: bundled(npm(os-homedir)) = 1.0.2
Provides: bundled(npm(os-tmpdir)) = 1.0.2
Provides: bundled(npm(osenv)) = 0.1.5
Provides: bundled(npm(p-limit)) = 2.3.0
Provides: bundled(npm(p-locate)) = 3.0.0
Provides: bundled(npm(p-try)) = 2.2.0
Provides: bundled(npm(parse-json)) = 2.2.0
Provides: bundled(npm(path-exists)) = 2.1.0
Provides: bundled(npm(path-exists)) = 3.0.0
Provides: bundled(npm(path-is-absolute)) = 1.0.1
Provides: bundled(npm(path-parse)) = 1.0.7
Provides: bundled(npm(path-type)) = 1.1.0
Provides: bundled(npm(performance-now)) = 2.1.0
Provides: bundled(npm(pify)) = 2.3.0
Provides: bundled(npm(pinkie)) = 2.0.4
Provides: bundled(npm(pinkie-promise)) = 2.0.1
Provides: bundled(npm(process-nextick-args)) = 2.0.1
Provides: bundled(npm(pseudomap)) = 1.0.2
Provides: bundled(npm(psl)) = 1.9.0
Provides: bundled(npm(punycode)) = 2.3.0
Provides: bundled(npm(qs)) = 6.5.3
Provides: bundled(npm(read-pkg)) = 1.1.0
Provides: bundled(npm(read-pkg-up)) = 1.0.1
Provides: bundled(npm(readable-stream)) = 2.3.8
Provides: bundled(npm(redent)) = 1.0.0
Provides: bundled(npm(repeating)) = 2.0.1
Provides: bundled(npm(request)) = 2.88.2
Provides: bundled(npm(require-directory)) = 2.1.1
Provides: bundled(npm(require-main-filename)) = 2.0.0
Provides: bundled(npm(resolve)) = 1.22.4
Provides: bundled(npm(rimraf)) = 2.7.1
Provides: bundled(npm(safe-buffer)) = 5.1.2
Provides: bundled(npm(safe-buffer)) = 5.2.1
Provides: bundled(npm(safer-buffer)) = 2.1.2
Provides: bundled(npm(sass-graph)) = 2.2.5
Provides: bundled(npm(scss-tokenizer)) = 0.2.3
Provides: bundled(npm(semver)) = 5.3.0
Provides: bundled(npm(semver)) = 5.7.2
Provides: bundled(npm(set-blocking)) = 2.0.0
Provides: bundled(npm(signal-exit)) = 3.0.7
Provides: bundled(npm(source-map)) = 0.4.4
Provides: bundled(npm(spdx-correct)) = 3.2.0
Provides: bundled(npm(spdx-exceptions)) = 2.3.0
Provides: bundled(npm(spdx-expression-parse)) = 3.0.1
Provides: bundled(npm(spdx-license-ids)) = 3.0.13
Provides: bundled(npm(sshpk)) = 1.17.0
Provides: bundled(npm(stdout-stream)) = 1.4.1
Provides: bundled(npm(string_decoder)) = 1.1.1
Provides: bundled(npm(string-width)) = 1.0.2
Provides: bundled(npm(string-width)) = 3.1.0
Provides: bundled(npm(string-width)) = 4.2.3
Provides: bundled(npm(strip-ansi)) = 3.0.1
Provides: bundled(npm(strip-ansi)) = 5.2.0
Provides: bundled(npm(strip-ansi)) = 6.0.1
Provides: bundled(npm(strip-bom)) = 2.0.0
Provides: bundled(npm(strip-indent)) = 1.0.1
Provides: bundled(npm(supports-color)) = 2.0.0
Provides: bundled(npm(supports-preserve-symlinks-flag)) = 1.0.0
Provides: bundled(npm(tar)) = 2.2.2
Provides: bundled(npm(tough-cookie)) = 2.5.0
Provides: bundled(npm(trim-newlines)) = 1.0.0
Provides: bundled(npm(true-case-path)) = 1.0.3
Provides: bundled(npm(tunnel-agent)) = 0.6.0
Provides: bundled(npm(tweetnacl)) = 0.14.5
Provides: bundled(npm(uri-js)) = 4.4.1
Provides: bundled(npm(util-deprecate)) = 1.0.2
Provides: bundled(npm(uuid)) = 3.4.0
Provides: bundled(npm(validate-npm-package-license)) = 3.0.4
Provides: bundled(npm(verror)) = 1.10.0
Provides: bundled(npm(which)) = 1.3.1
Provides: bundled(npm(which-module)) = 2.0.1
Provides: bundled(npm(wide-align)) = 1.1.5
Provides: bundled(npm(wrap-ansi)) = 5.1.0
Provides: bundled(npm(wrappy)) = 1.0.2
Provides: bundled(npm(y18n)) = 4.0.3
Provides: bundled(npm(yallist)) = 2.1.2
Provides: bundled(npm(yargs)) = 13.3.2
Provides: bundled(npm(yargs-parser)) = 13.1.2
AutoReq: no
AutoProv: no

%define npm_cache_dir npm_cache

%description
%{summary}

%prep
mkdir -p %{npm_cache_dir}
%{?scl:scl enable %{?scl_nodejs} - << \end_of_scl}
for tgz in %{sources}; do
  echo $tgz | grep -q registry.npmjs.org || npm cache add --cache %{npm_cache_dir} $tgz
done
%{?scl:end_of_scl}

%setup -T -q -a 196 -D -n %{npm_cache_dir}

%build
export SKIP_SASS_BINARY_DOWNLOAD_FOR_CI=true

%{?scl:scl enable %{?scl_nodejs} - << \end_of_scl}
npm install --ignore-scripts --cache-min Infinity --cache ../%{npm_cache_dir} --no-shrinkwrap --no-optional --global-style true %{npm_name}@%{version}
%{?scl:end_of_scl}

# Replace node-gyp with packaged version that uses nodejs-devel headers
rm -rf node_modules/%{npm_name}/node_modules/node-gyp
ln -s %{nodejs_sitelib}/node-gyp node_modules/%{npm_name}/node_modules/

pushd node_modules/%{npm_name}
npm_config_nodedir=/usr/include/node node scripts/build -f
popd

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/bin %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/binding.gyp %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/lib %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/scripts %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/src %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/test %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/vendor %{buildroot}%{nodejs_sitelib}/%{npm_name}

mkdir -p %{buildroot}%{_bindir}/
chmod 0755 %{buildroot}%{nodejs_sitelib}/%{npm_name}/bin/node-sass
ln -sf %{nodejs_sitelib}/%{npm_name}/bin/node-sass %{buildroot}%{_bindir}/node-sass

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%{_bindir}/node-sass
%license node_modules/%{npm_name}/LICENSE
%doc node_modules/%{npm_name}/CHANGELOG.md
%doc node_modules/%{npm_name}/README.md

%changelog
* Tue Sep 19 2023 Eric D. Helms <ericdhelms@gmail.com> - 4.14.1-2
- nInclude vendor directory

* Wed Sep 13 2023 Foreman Packaging Automation <packaging@theforeman.org> 4.14.1-1
- Update to 4.14.1

* Thu Mar 26 2020 Zach Huntington-Meath <zhunting@redhat.com> 4.13.1-1
- Update to 4.13.1

* Tue Mar 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 4.12.0-3
- Bump packages to build for el8

* Wed Oct 23 2019 Eric D. Helms <ericdhelms@gmail.com> - 4.12.0-2
- Fix missing vendor

* Mon Oct 21 2019 Eric D. Helms <ericdhelms@gmail.com> - 4.12.0-1
- Build for SCL

* Fri Mar 03 2017 Dominic Cleal <dominic@cleal.org> 4.5.0-2
- Add runtime dep on gyp, to satisfy symlink (dominic@cleal.org)

* Thu Mar 02 2017 Dominic Cleal <dominic@cleal.org> 4.5.0-1
- new package built with tito
