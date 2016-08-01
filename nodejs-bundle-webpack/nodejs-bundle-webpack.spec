# TODO
#
# Remove nodejs_symlink_deps if installing bundled module with NPM

%global npm_name bundle-webpack

Name: nodejs-%{npm_name}
Version: 1.13.1
Release: 1%{?dist}
Summary: Packs CommonJs/AMD modules for the browser
License: MIT
Group: Development/Libraries
URL: https://github.com/webpack/webpack
Source0: http://registry.npmjs.org/webpack/-/webpack-1.13.1.tgz
Source1: http://registry.npmjs.org/mkdirp/-/mkdirp-0.5.1.tgz
Source2: http://registry.npmjs.org/interpret/-/interpret-0.6.6.tgz
Source3: http://registry.npmjs.org/memory-fs/-/memory-fs-0.3.0.tgz
Source4: http://registry.npmjs.org/loader-utils/-/loader-utils-0.2.15.tgz
Source5: http://registry.npmjs.org/clone/-/clone-1.0.2.tgz
Source6: http://registry.npmjs.org/acorn/-/acorn-3.3.0.tgz
Source7: http://registry.npmjs.org/node-libs-browser/-/node-libs-browser-0.5.3.tgz
Source8: http://registry.npmjs.org/supports-color/-/supports-color-3.1.2.tgz
Source9: http://registry.npmjs.org/enhanced-resolve/-/enhanced-resolve-0.9.1.tgz
Source10: http://registry.npmjs.org/optimist/-/optimist-0.6.1.tgz
Source11: http://registry.npmjs.org/async/-/async-1.5.2.tgz
Source12: http://registry.npmjs.org/minimist/-/minimist-0.0.8.tgz
Source13: http://registry.npmjs.org/uglify-js/-/uglify-js-2.6.4.tgz
Source14: http://registry.npmjs.org/tapable/-/tapable-0.1.10.tgz
Source15: http://registry.npmjs.org/webpack-core/-/webpack-core-0.6.8.tgz
Source16: http://registry.npmjs.org/errno/-/errno-0.1.4.tgz
Source17: http://registry.npmjs.org/watchpack/-/watchpack-0.2.9.tgz
Source18: http://registry.npmjs.org/json5/-/json5-0.5.0.tgz
Source19: http://registry.npmjs.org/object-assign/-/object-assign-4.1.0.tgz
Source20: http://registry.npmjs.org/browserify-zlib/-/browserify-zlib-0.1.4.tgz
Source21: http://registry.npmjs.org/emojis-list/-/emojis-list-2.0.1.tgz
Source22: http://registry.npmjs.org/big.js/-/big.js-3.1.3.tgz
Source23: http://registry.npmjs.org/readable-stream/-/readable-stream-2.1.4.tgz
Source24: http://registry.npmjs.org/assert/-/assert-1.4.1.tgz
Source25: http://registry.npmjs.org/constants-browserify/-/constants-browserify-0.0.1.tgz
Source26: http://registry.npmjs.org/events/-/events-1.1.1.tgz
Source27: http://registry.npmjs.org/domain-browser/-/domain-browser-1.1.7.tgz
Source28: http://registry.npmjs.org/crypto-browserify/-/crypto-browserify-3.2.8.tgz
Source29: http://registry.npmjs.org/os-browserify/-/os-browserify-0.1.2.tgz
Source30: http://registry.npmjs.org/console-browserify/-/console-browserify-1.1.0.tgz
Source31: http://registry.npmjs.org/path-browserify/-/path-browserify-0.0.0.tgz
Source32: http://registry.npmjs.org/buffer/-/buffer-3.6.0.tgz
Source33: http://registry.npmjs.org/process/-/process-0.11.6.tgz
Source34: http://registry.npmjs.org/punycode/-/punycode-1.4.1.tgz
Source35: http://registry.npmjs.org/querystring-es3/-/querystring-es3-0.2.1.tgz
Source36: http://registry.npmjs.org/https-browserify/-/https-browserify-0.0.0.tgz
Source37: http://registry.npmjs.org/string_decoder/-/string_decoder-0.10.31.tgz
Source38: http://registry.npmjs.org/timers-browserify/-/timers-browserify-1.4.2.tgz
Source39: http://registry.npmjs.org/vm-browserify/-/vm-browserify-0.0.4.tgz
Source40: http://registry.npmjs.org/url/-/url-0.10.3.tgz
Source41: http://registry.npmjs.org/has-flag/-/has-flag-1.0.0.tgz
Source42: http://registry.npmjs.org/stream-browserify/-/stream-browserify-1.0.0.tgz
Source43: http://registry.npmjs.org/http-browserify/-/http-browserify-1.7.0.tgz
Source44: http://registry.npmjs.org/util/-/util-0.10.3.tgz
Source45: http://registry.npmjs.org/readable-stream/-/readable-stream-1.1.14.tgz
Source46: http://registry.npmjs.org/memory-fs/-/memory-fs-0.2.0.tgz
Source47: http://registry.npmjs.org/wordwrap/-/wordwrap-0.0.3.tgz
Source48: http://registry.npmjs.org/graceful-fs/-/graceful-fs-4.1.5.tgz
Source49: http://registry.npmjs.org/minimist/-/minimist-0.0.10.tgz
Source50: http://registry.npmjs.org/tty-browserify/-/tty-browserify-0.0.0.tgz
Source51: http://registry.npmjs.org/source-map/-/source-map-0.5.6.tgz
Source52: http://registry.npmjs.org/uglify-to-browserify/-/uglify-to-browserify-1.0.2.tgz
Source53: http://registry.npmjs.org/prr/-/prr-0.0.0.tgz
Source54: http://registry.npmjs.org/yargs/-/yargs-3.10.0.tgz
Source55: http://registry.npmjs.org/buffer-shims/-/buffer-shims-1.0.0.tgz
Source56: http://registry.npmjs.org/async/-/async-0.2.10.tgz
Source57: http://registry.npmjs.org/source-map/-/source-map-0.4.4.tgz
Source58: http://registry.npmjs.org/pako/-/pako-0.2.9.tgz
Source59: http://registry.npmjs.org/source-list-map/-/source-list-map-0.1.6.tgz
Source60: http://registry.npmjs.org/core-util-is/-/core-util-is-1.0.2.tgz
Source61: http://registry.npmjs.org/async/-/async-0.9.2.tgz
Source62: http://registry.npmjs.org/isarray/-/isarray-1.0.0.tgz
Source63: http://registry.npmjs.org/inherits/-/inherits-2.0.1.tgz
Source64: http://registry.npmjs.org/util-deprecate/-/util-deprecate-1.0.2.tgz
Source65: http://registry.npmjs.org/chokidar/-/chokidar-1.6.0.tgz
Source66: http://registry.npmjs.org/process-nextick-args/-/process-nextick-args-1.0.7.tgz
Source67: http://registry.npmjs.org/ripemd160/-/ripemd160-0.2.0.tgz
Source68: http://registry.npmjs.org/pbkdf2-compat/-/pbkdf2-compat-2.0.1.tgz
Source69: http://registry.npmjs.org/ieee754/-/ieee754-1.1.6.tgz
Source70: http://registry.npmjs.org/base64-js/-/base64-js-0.0.8.tgz
Source71: http://registry.npmjs.org/date-now/-/date-now-0.1.4.tgz
Source72: http://registry.npmjs.org/sha.js/-/sha.js-2.2.6.tgz
Source73: http://registry.npmjs.org/punycode/-/punycode-1.3.2.tgz
Source74: http://registry.npmjs.org/indexof/-/indexof-0.0.1.tgz
Source75: http://registry.npmjs.org/querystring/-/querystring-0.2.0.tgz
Source76: http://registry.npmjs.org/isarray/-/isarray-0.0.1.tgz
Source77: http://registry.npmjs.org/Base64/-/Base64-0.2.1.tgz
Source78: http://registry.npmjs.org/decamelize/-/decamelize-1.2.0.tgz
Source79: http://registry.npmjs.org/anymatch/-/anymatch-1.3.0.tgz
Source80: http://registry.npmjs.org/camelcase/-/camelcase-1.2.1.tgz
Source81: http://registry.npmjs.org/window-size/-/window-size-0.1.0.tgz
Source82: http://registry.npmjs.org/amdefine/-/amdefine-1.0.0.tgz
Source83: http://registry.npmjs.org/async-each/-/async-each-1.0.0.tgz
Source84: http://registry.npmjs.org/glob-parent/-/glob-parent-2.0.0.tgz
Source85: http://registry.npmjs.org/cliui/-/cliui-2.1.0.tgz
Source86: http://registry.npmjs.org/is-binary-path/-/is-binary-path-1.0.1.tgz
Source87: http://registry.npmjs.org/path-is-absolute/-/path-is-absolute-1.0.0.tgz
Source88: http://registry.npmjs.org/readdirp/-/readdirp-2.1.0.tgz
Source89: http://registry.npmjs.org/arrify/-/arrify-1.0.1.tgz
Source90: http://registry.npmjs.org/is-glob/-/is-glob-2.0.1.tgz
Source91: http://registry.npmjs.org/center-align/-/center-align-0.1.3.tgz
Source92: http://registry.npmjs.org/right-align/-/right-align-0.1.3.tgz
Source93: http://registry.npmjs.org/fsevents/-/fsevents-1.0.14.tgz
Source94: http://registry.npmjs.org/wordwrap/-/wordwrap-0.0.2.tgz
Source95: http://registry.npmjs.org/micromatch/-/micromatch-2.3.11.tgz
Source96: http://registry.npmjs.org/binary-extensions/-/binary-extensions-1.5.0.tgz
Source97: http://registry.npmjs.org/align-text/-/align-text-0.1.4.tgz
Source98: http://registry.npmjs.org/is-extglob/-/is-extglob-1.0.0.tgz
Source99: http://registry.npmjs.org/set-immediate-shim/-/set-immediate-shim-1.0.1.tgz
Source100: http://registry.npmjs.org/lazy-cache/-/lazy-cache-1.0.4.tgz
Source101: http://registry.npmjs.org/array-unique/-/array-unique-0.2.1.tgz
Source102: http://registry.npmjs.org/nan/-/nan-2.4.0.tgz
Source103: http://registry.npmjs.org/minimatch/-/minimatch-3.0.2.tgz
Source104: http://registry.npmjs.org/expand-brackets/-/expand-brackets-0.1.5.tgz
Source105: http://registry.npmjs.org/arr-diff/-/arr-diff-2.0.0.tgz
Source106: http://registry.npmjs.org/braces/-/braces-1.8.5.tgz
Source107: http://registry.npmjs.org/extglob/-/extglob-0.3.2.tgz
Source108: http://registry.npmjs.org/kind-of/-/kind-of-3.0.4.tgz
Source109: http://registry.npmjs.org/normalize-path/-/normalize-path-2.0.1.tgz
Source110: http://registry.npmjs.org/filename-regex/-/filename-regex-2.0.0.tgz
Source111: http://registry.npmjs.org/node-pre-gyp/-/node-pre-gyp-0.6.29.tgz
Source112: http://registry.npmjs.org/longest/-/longest-1.0.1.tgz
Source113: http://registry.npmjs.org/object.omit/-/object.omit-2.0.0.tgz
Source114: http://registry.npmjs.org/brace-expansion/-/brace-expansion-1.1.6.tgz
Source115: http://registry.npmjs.org/parse-glob/-/parse-glob-3.0.4.tgz
Source116: http://registry.npmjs.org/regex-cache/-/regex-cache-0.4.3.tgz
Source117: http://registry.npmjs.org/repeat-string/-/repeat-string-1.5.4.tgz
Source118: http://registry.npmjs.org/is-posix-bracket/-/is-posix-bracket-0.1.1.tgz
Source119: http://registry.npmjs.org/is-buffer/-/is-buffer-1.1.3.tgz
Source120: http://registry.npmjs.org/expand-range/-/expand-range-1.8.2.tgz
Source121: http://registry.npmjs.org/repeat-element/-/repeat-element-1.1.2.tgz
Source122: http://registry.npmjs.org/arr-flatten/-/arr-flatten-1.0.1.tgz
Source123: http://registry.npmjs.org/nopt/-/nopt-3.0.6.tgz
Source124: http://registry.npmjs.org/npmlog/-/npmlog-3.1.2.tgz
Source125: http://registry.npmjs.org/semver/-/semver-5.2.0.tgz
Source126: http://registry.npmjs.org/tar/-/tar-2.2.1.tgz
Source127: http://registry.npmjs.org/rc/-/rc-1.1.6.tgz
Source128: http://registry.npmjs.org/preserve/-/preserve-0.2.0.tgz
Source129: http://registry.npmjs.org/request/-/request-2.74.0.tgz
Source130: http://registry.npmjs.org/rimraf/-/rimraf-2.5.4.tgz
Source131: http://registry.npmjs.org/for-own/-/for-own-0.1.4.tgz
Source132: http://registry.npmjs.org/tar-pack/-/tar-pack-3.1.4.tgz
Source133: http://registry.npmjs.org/is-extendable/-/is-extendable-0.1.1.tgz
Source134: http://registry.npmjs.org/balanced-match/-/balanced-match-0.4.2.tgz
Source135: http://registry.npmjs.org/is-equal-shallow/-/is-equal-shallow-0.1.3.tgz
Source136: http://registry.npmjs.org/is-primitive/-/is-primitive-2.0.0.tgz
Source137: http://registry.npmjs.org/is-dotfile/-/is-dotfile-1.0.2.tgz
Source138: http://registry.npmjs.org/glob-base/-/glob-base-0.3.0.tgz
Source139: http://registry.npmjs.org/concat-map/-/concat-map-0.0.1.tgz
Source140: http://registry.npmjs.org/abbrev/-/abbrev-1.0.9.tgz
Source141: http://registry.npmjs.org/are-we-there-yet/-/are-we-there-yet-1.1.2.tgz
Source142: http://registry.npmjs.org/console-control-strings/-/console-control-strings-1.1.0.tgz
Source143: http://registry.npmjs.org/set-blocking/-/set-blocking-2.0.0.tgz
Source144: http://registry.npmjs.org/gauge/-/gauge-2.6.0.tgz
Source145: http://registry.npmjs.org/block-stream/-/block-stream-0.0.9.tgz
Source146: http://registry.npmjs.org/fill-range/-/fill-range-2.2.3.tgz
Source147: http://registry.npmjs.org/minimist/-/minimist-1.2.0.tgz
Source148: http://registry.npmjs.org/ini/-/ini-1.3.4.tgz
Source149: http://registry.npmjs.org/strip-json-comments/-/strip-json-comments-1.0.4.tgz
Source150: http://registry.npmjs.org/deep-extend/-/deep-extend-0.4.1.tgz
Source151: http://registry.npmjs.org/fstream/-/fstream-1.0.10.tgz
Source152: http://registry.npmjs.org/aws-sign2/-/aws-sign2-0.6.0.tgz
Source153: http://registry.npmjs.org/extend/-/extend-3.0.0.tgz
Source154: http://registry.npmjs.org/combined-stream/-/combined-stream-1.0.5.tgz
Source155: http://registry.npmjs.org/bl/-/bl-1.1.2.tgz
Source156: http://registry.npmjs.org/forever-agent/-/forever-agent-0.6.1.tgz
Source157: http://registry.npmjs.org/caseless/-/caseless-0.11.0.tgz
Source158: http://registry.npmjs.org/form-data/-/form-data-1.0.0-rc4.tgz
Source159: http://registry.npmjs.org/is-typedarray/-/is-typedarray-1.0.0.tgz
Source160: http://registry.npmjs.org/isstream/-/isstream-0.1.2.tgz
Source161: http://registry.npmjs.org/http-signature/-/http-signature-1.1.1.tgz
Source162: http://registry.npmjs.org/json-stringify-safe/-/json-stringify-safe-5.0.1.tgz
Source163: http://registry.npmjs.org/aws4/-/aws4-1.4.1.tgz
Source164: http://registry.npmjs.org/oauth-sign/-/oauth-sign-0.8.2.tgz
Source165: http://registry.npmjs.org/hawk/-/hawk-3.1.3.tgz
Source166: http://registry.npmjs.org/node-uuid/-/node-uuid-1.4.7.tgz
Source167: http://registry.npmjs.org/mime-types/-/mime-types-2.1.11.tgz
Source168: http://registry.npmjs.org/har-validator/-/har-validator-2.0.6.tgz
Source169: http://registry.npmjs.org/tough-cookie/-/tough-cookie-2.3.1.tgz
Source170: http://registry.npmjs.org/stringstream/-/stringstream-0.0.5.tgz
Source171: http://registry.npmjs.org/debug/-/debug-2.2.0.tgz
Source172: http://registry.npmjs.org/fstream-ignore/-/fstream-ignore-1.0.5.tgz
Source173: http://registry.npmjs.org/once/-/once-1.3.3.tgz
Source174: http://registry.npmjs.org/for-in/-/for-in-0.1.5.tgz
Source175: http://registry.npmjs.org/tunnel-agent/-/tunnel-agent-0.4.3.tgz
Source176: http://registry.npmjs.org/glob/-/glob-7.0.5.tgz
Source177: http://registry.npmjs.org/uid-number/-/uid-number-0.0.6.tgz
Source178: http://registry.npmjs.org/delegates/-/delegates-1.0.0.tgz
Source179: http://registry.npmjs.org/aproba/-/aproba-1.0.4.tgz
Source180: http://registry.npmjs.org/has-color/-/has-color-0.1.7.tgz
Source181: http://registry.npmjs.org/has-unicode/-/has-unicode-2.0.1.tgz
Source182: http://registry.npmjs.org/signal-exit/-/signal-exit-3.0.0.tgz
Source183: http://registry.npmjs.org/string-width/-/string-width-1.0.1.tgz
Source184: http://registry.npmjs.org/wide-align/-/wide-align-1.1.0.tgz
Source185: http://registry.npmjs.org/isobject/-/isobject-2.1.0.tgz
Source186: http://registry.npmjs.org/randomatic/-/randomatic-1.1.5.tgz
Source187: http://registry.npmjs.org/is-number/-/is-number-2.1.0.tgz
Source188: http://registry.npmjs.org/strip-ansi/-/strip-ansi-3.0.1.tgz
Source189: http://registry.npmjs.org/delayed-stream/-/delayed-stream-1.0.0.tgz
Source190: http://registry.npmjs.org/readable-stream/-/readable-stream-2.0.6.tgz
Source191: http://registry.npmjs.org/assert-plus/-/assert-plus-0.2.0.tgz
Source192: http://registry.npmjs.org/hoek/-/hoek-2.16.3.tgz
Source193: http://registry.npmjs.org/boom/-/boom-2.10.1.tgz
Source194: http://registry.npmjs.org/jsprim/-/jsprim-1.3.0.tgz
Source195: http://registry.npmjs.org/sntp/-/sntp-1.0.9.tgz
Source196: http://registry.npmjs.org/sshpk/-/sshpk-1.9.2.tgz
Source197: http://registry.npmjs.org/mime-db/-/mime-db-1.23.0.tgz
Source198: http://registry.npmjs.org/commander/-/commander-2.9.0.tgz
Source199: http://registry.npmjs.org/pinkie-promise/-/pinkie-promise-2.0.1.tgz
Source200: http://registry.npmjs.org/ms/-/ms-0.7.1.tgz
Source201: http://registry.npmjs.org/is-my-json-valid/-/is-my-json-valid-2.13.1.tgz
Source202: http://registry.npmjs.org/cryptiles/-/cryptiles-2.0.5.tgz
Source203: http://registry.npmjs.org/wrappy/-/wrappy-1.0.2.tgz
Source204: http://registry.npmjs.org/fs.realpath/-/fs.realpath-1.0.0.tgz
Source205: http://registry.npmjs.org/chalk/-/chalk-1.1.3.tgz
Source206: http://registry.npmjs.org/code-point-at/-/code-point-at-1.0.0.tgz
Source207: http://registry.npmjs.org/is-fullwidth-code-point/-/is-fullwidth-code-point-1.0.0.tgz
Source208: http://registry.npmjs.org/inflight/-/inflight-1.0.5.tgz
Source209: http://registry.npmjs.org/ansi-regex/-/ansi-regex-2.0.0.tgz
Source210: http://registry.npmjs.org/json-schema/-/json-schema-0.2.2.tgz
Source211: http://registry.npmjs.org/asn1/-/asn1-0.2.3.tgz
Source212: http://registry.npmjs.org/extsprintf/-/extsprintf-1.0.2.tgz
Source213: http://registry.npmjs.org/assert-plus/-/assert-plus-1.0.0.tgz
Source214: http://registry.npmjs.org/getpass/-/getpass-0.1.6.tgz
Source215: http://registry.npmjs.org/dashdash/-/dashdash-1.14.0.tgz
Source216: http://registry.npmjs.org/jsbn/-/jsbn-0.1.0.tgz
Source217: http://registry.npmjs.org/jodid25519/-/jodid25519-1.0.2.tgz
Source218: http://registry.npmjs.org/verror/-/verror-1.3.6.tgz
Source219: http://registry.npmjs.org/ecc-jsbn/-/ecc-jsbn-0.1.1.tgz
Source220: http://registry.npmjs.org/pinkie/-/pinkie-2.0.4.tgz
Source221: http://registry.npmjs.org/tweetnacl/-/tweetnacl-0.13.3.tgz
Source222: http://registry.npmjs.org/graceful-readlink/-/graceful-readlink-1.0.1.tgz
Source223: http://registry.npmjs.org/generate-function/-/generate-function-2.0.0.tgz
Source224: http://registry.npmjs.org/generate-object-property/-/generate-object-property-1.2.0.tgz
Source225: http://registry.npmjs.org/jsonpointer/-/jsonpointer-2.0.0.tgz
Source226: http://registry.npmjs.org/escape-string-regexp/-/escape-string-regexp-1.0.5.tgz
Source227: http://registry.npmjs.org/ansi-styles/-/ansi-styles-2.2.1.tgz
Source228: http://registry.npmjs.org/xtend/-/xtend-4.0.1.tgz
Source229: http://registry.npmjs.org/has-ansi/-/has-ansi-2.0.0.tgz
Source230: http://registry.npmjs.org/number-is-nan/-/number-is-nan-1.0.0.tgz
Source231: http://registry.npmjs.org/supports-color/-/supports-color-2.0.0.tgz
Source232: http://registry.npmjs.org/is-property/-/is-property-1.0.2.tgz
Source233: http://registry.npmjs.org/qs/-/qs-6.2.1.tgz
Source234: webpack-1.13.1-registry.npmjs.org.tgz
Requires: nodejs(engine)
BuildRequires: nodejs-devel
BuildRequires: nodejs-packaging
BuildRequires: npm
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch
Provides: npm(%{npm_name}) = %{version}
Provides: bundled-npm(webpack) = 1.13.1
Provides: bundled-npm(mkdirp) = 0.5.1
Provides: bundled-npm(interpret) = 0.6.6
Provides: bundled-npm(memory-fs) = 0.3.0
Provides: bundled-npm(loader-utils) = 0.2.15
Provides: bundled-npm(clone) = 1.0.2
Provides: bundled-npm(acorn) = 3.3.0
Provides: bundled-npm(node-libs-browser) = 0.5.3
Provides: bundled-npm(supports-color) = 3.1.2
Provides: bundled-npm(enhanced-resolve) = 0.9.1
Provides: bundled-npm(optimist) = 0.6.1
Provides: bundled-npm(async) = 1.5.2
Provides: bundled-npm(minimist) = 0.0.8
Provides: bundled-npm(uglify-js) = 2.6.4
Provides: bundled-npm(tapable) = 0.1.10
Provides: bundled-npm(webpack-core) = 0.6.8
Provides: bundled-npm(errno) = 0.1.4
Provides: bundled-npm(watchpack) = 0.2.9
Provides: bundled-npm(json5) = 0.5.0
Provides: bundled-npm(object-assign) = 4.1.0
Provides: bundled-npm(browserify-zlib) = 0.1.4
Provides: bundled-npm(emojis-list) = 2.0.1
Provides: bundled-npm(big.js) = 3.1.3
Provides: bundled-npm(readable-stream) = 2.1.4
Provides: bundled-npm(assert) = 1.4.1
Provides: bundled-npm(constants-browserify) = 0.0.1
Provides: bundled-npm(events) = 1.1.1
Provides: bundled-npm(domain-browser) = 1.1.7
Provides: bundled-npm(crypto-browserify) = 3.2.8
Provides: bundled-npm(os-browserify) = 0.1.2
Provides: bundled-npm(console-browserify) = 1.1.0
Provides: bundled-npm(path-browserify) = 0.0.0
Provides: bundled-npm(buffer) = 3.6.0
Provides: bundled-npm(process) = 0.11.6
Provides: bundled-npm(punycode) = 1.4.1
Provides: bundled-npm(querystring-es3) = 0.2.1
Provides: bundled-npm(https-browserify) = 0.0.0
Provides: bundled-npm(string_decoder) = 0.10.31
Provides: bundled-npm(timers-browserify) = 1.4.2
Provides: bundled-npm(vm-browserify) = 0.0.4
Provides: bundled-npm(url) = 0.10.3
Provides: bundled-npm(has-flag) = 1.0.0
Provides: bundled-npm(stream-browserify) = 1.0.0
Provides: bundled-npm(http-browserify) = 1.7.0
Provides: bundled-npm(util) = 0.10.3
Provides: bundled-npm(readable-stream) = 1.1.14
Provides: bundled-npm(memory-fs) = 0.2.0
Provides: bundled-npm(wordwrap) = 0.0.3
Provides: bundled-npm(graceful-fs) = 4.1.5
Provides: bundled-npm(minimist) = 0.0.10
Provides: bundled-npm(tty-browserify) = 0.0.0
Provides: bundled-npm(source-map) = 0.5.6
Provides: bundled-npm(uglify-to-browserify) = 1.0.2
Provides: bundled-npm(prr) = 0.0.0
Provides: bundled-npm(yargs) = 3.10.0
Provides: bundled-npm(buffer-shims) = 1.0.0
Provides: bundled-npm(async) = 0.2.10
Provides: bundled-npm(source-map) = 0.4.4
Provides: bundled-npm(pako) = 0.2.9
Provides: bundled-npm(source-list-map) = 0.1.6
Provides: bundled-npm(core-util-is) = 1.0.2
Provides: bundled-npm(async) = 0.9.2
Provides: bundled-npm(isarray) = 1.0.0
Provides: bundled-npm(inherits) = 2.0.1
Provides: bundled-npm(util-deprecate) = 1.0.2
Provides: bundled-npm(chokidar) = 1.6.0
Provides: bundled-npm(process-nextick-args) = 1.0.7
Provides: bundled-npm(ripemd160) = 0.2.0
Provides: bundled-npm(pbkdf2-compat) = 2.0.1
Provides: bundled-npm(ieee754) = 1.1.6
Provides: bundled-npm(base64-js) = 0.0.8
Provides: bundled-npm(date-now) = 0.1.4
Provides: bundled-npm(sha.js) = 2.2.6
Provides: bundled-npm(punycode) = 1.3.2
Provides: bundled-npm(indexof) = 0.0.1
Provides: bundled-npm(querystring) = 0.2.0
Provides: bundled-npm(isarray) = 0.0.1
Provides: bundled-npm(Base64) = 0.2.1
Provides: bundled-npm(decamelize) = 1.2.0
Provides: bundled-npm(anymatch) = 1.3.0
Provides: bundled-npm(camelcase) = 1.2.1
Provides: bundled-npm(window-size) = 0.1.0
Provides: bundled-npm(amdefine) = 1.0.0
Provides: bundled-npm(async-each) = 1.0.0
Provides: bundled-npm(glob-parent) = 2.0.0
Provides: bundled-npm(cliui) = 2.1.0
Provides: bundled-npm(is-binary-path) = 1.0.1
Provides: bundled-npm(path-is-absolute) = 1.0.0
Provides: bundled-npm(readdirp) = 2.1.0
Provides: bundled-npm(arrify) = 1.0.1
Provides: bundled-npm(is-glob) = 2.0.1
Provides: bundled-npm(center-align) = 0.1.3
Provides: bundled-npm(right-align) = 0.1.3
Provides: bundled-npm(fsevents) = 1.0.14
Provides: bundled-npm(wordwrap) = 0.0.2
Provides: bundled-npm(micromatch) = 2.3.11
Provides: bundled-npm(binary-extensions) = 1.5.0
Provides: bundled-npm(align-text) = 0.1.4
Provides: bundled-npm(is-extglob) = 1.0.0
Provides: bundled-npm(set-immediate-shim) = 1.0.1
Provides: bundled-npm(lazy-cache) = 1.0.4
Provides: bundled-npm(array-unique) = 0.2.1
Provides: bundled-npm(nan) = 2.4.0
Provides: bundled-npm(minimatch) = 3.0.2
Provides: bundled-npm(expand-brackets) = 0.1.5
Provides: bundled-npm(arr-diff) = 2.0.0
Provides: bundled-npm(braces) = 1.8.5
Provides: bundled-npm(extglob) = 0.3.2
Provides: bundled-npm(kind-of) = 3.0.4
Provides: bundled-npm(normalize-path) = 2.0.1
Provides: bundled-npm(filename-regex) = 2.0.0
Provides: bundled-npm(node-pre-gyp) = 0.6.29
Provides: bundled-npm(longest) = 1.0.1
Provides: bundled-npm(object.omit) = 2.0.0
Provides: bundled-npm(brace-expansion) = 1.1.6
Provides: bundled-npm(parse-glob) = 3.0.4
Provides: bundled-npm(regex-cache) = 0.4.3
Provides: bundled-npm(repeat-string) = 1.5.4
Provides: bundled-npm(is-posix-bracket) = 0.1.1
Provides: bundled-npm(is-buffer) = 1.1.3
Provides: bundled-npm(expand-range) = 1.8.2
Provides: bundled-npm(repeat-element) = 1.1.2
Provides: bundled-npm(arr-flatten) = 1.0.1
Provides: bundled-npm(nopt) = 3.0.6
Provides: bundled-npm(npmlog) = 3.1.2
Provides: bundled-npm(semver) = 5.2.0
Provides: bundled-npm(tar) = 2.2.1
Provides: bundled-npm(rc) = 1.1.6
Provides: bundled-npm(preserve) = 0.2.0
Provides: bundled-npm(request) = 2.74.0
Provides: bundled-npm(rimraf) = 2.5.4
Provides: bundled-npm(for-own) = 0.1.4
Provides: bundled-npm(tar-pack) = 3.1.4
Provides: bundled-npm(is-extendable) = 0.1.1
Provides: bundled-npm(balanced-match) = 0.4.2
Provides: bundled-npm(is-equal-shallow) = 0.1.3
Provides: bundled-npm(is-primitive) = 2.0.0
Provides: bundled-npm(is-dotfile) = 1.0.2
Provides: bundled-npm(glob-base) = 0.3.0
Provides: bundled-npm(concat-map) = 0.0.1
Provides: bundled-npm(abbrev) = 1.0.9
Provides: bundled-npm(are-we-there-yet) = 1.1.2
Provides: bundled-npm(console-control-strings) = 1.1.0
Provides: bundled-npm(set-blocking) = 2.0.0
Provides: bundled-npm(gauge) = 2.6.0
Provides: bundled-npm(block-stream) = 0.0.9
Provides: bundled-npm(fill-range) = 2.2.3
Provides: bundled-npm(minimist) = 1.2.0
Provides: bundled-npm(ini) = 1.3.4
Provides: bundled-npm(strip-json-comments) = 1.0.4
Provides: bundled-npm(deep-extend) = 0.4.1
Provides: bundled-npm(fstream) = 1.0.10
Provides: bundled-npm(aws-sign2) = 0.6.0
Provides: bundled-npm(extend) = 3.0.0
Provides: bundled-npm(combined-stream) = 1.0.5
Provides: bundled-npm(bl) = 1.1.2
Provides: bundled-npm(forever-agent) = 0.6.1
Provides: bundled-npm(caseless) = 0.11.0
Provides: bundled-npm(form-data) = 1.0.0-rc4
Provides: bundled-npm(is-typedarray) = 1.0.0
Provides: bundled-npm(isstream) = 0.1.2
Provides: bundled-npm(http-signature) = 1.1.1
Provides: bundled-npm(json-stringify-safe) = 5.0.1
Provides: bundled-npm(aws4) = 1.4.1
Provides: bundled-npm(oauth-sign) = 0.8.2
Provides: bundled-npm(hawk) = 3.1.3
Provides: bundled-npm(node-uuid) = 1.4.7
Provides: bundled-npm(mime-types) = 2.1.11
Provides: bundled-npm(har-validator) = 2.0.6
Provides: bundled-npm(tough-cookie) = 2.3.1
Provides: bundled-npm(stringstream) = 0.0.5
Provides: bundled-npm(debug) = 2.2.0
Provides: bundled-npm(fstream-ignore) = 1.0.5
Provides: bundled-npm(once) = 1.3.3
Provides: bundled-npm(for-in) = 0.1.5
Provides: bundled-npm(tunnel-agent) = 0.4.3
Provides: bundled-npm(glob) = 7.0.5
Provides: bundled-npm(uid-number) = 0.0.6
Provides: bundled-npm(delegates) = 1.0.0
Provides: bundled-npm(aproba) = 1.0.4
Provides: bundled-npm(has-color) = 0.1.7
Provides: bundled-npm(has-unicode) = 2.0.1
Provides: bundled-npm(signal-exit) = 3.0.0
Provides: bundled-npm(string-width) = 1.0.1
Provides: bundled-npm(wide-align) = 1.1.0
Provides: bundled-npm(isobject) = 2.1.0
Provides: bundled-npm(randomatic) = 1.1.5
Provides: bundled-npm(is-number) = 2.1.0
Provides: bundled-npm(strip-ansi) = 3.0.1
Provides: bundled-npm(delayed-stream) = 1.0.0
Provides: bundled-npm(readable-stream) = 2.0.6
Provides: bundled-npm(assert-plus) = 0.2.0
Provides: bundled-npm(hoek) = 2.16.3
Provides: bundled-npm(boom) = 2.10.1
Provides: bundled-npm(jsprim) = 1.3.0
Provides: bundled-npm(sntp) = 1.0.9
Provides: bundled-npm(sshpk) = 1.9.2
Provides: bundled-npm(mime-db) = 1.23.0
Provides: bundled-npm(commander) = 2.9.0
Provides: bundled-npm(pinkie-promise) = 2.0.1
Provides: bundled-npm(ms) = 0.7.1
Provides: bundled-npm(is-my-json-valid) = 2.13.1
Provides: bundled-npm(cryptiles) = 2.0.5
Provides: bundled-npm(wrappy) = 1.0.2
Provides: bundled-npm(fs.realpath) = 1.0.0
Provides: bundled-npm(chalk) = 1.1.3
Provides: bundled-npm(code-point-at) = 1.0.0
Provides: bundled-npm(is-fullwidth-code-point) = 1.0.0
Provides: bundled-npm(inflight) = 1.0.5
Provides: bundled-npm(ansi-regex) = 2.0.0
Provides: bundled-npm(json-schema) = 0.2.2
Provides: bundled-npm(asn1) = 0.2.3
Provides: bundled-npm(extsprintf) = 1.0.2
Provides: bundled-npm(assert-plus) = 1.0.0
Provides: bundled-npm(getpass) = 0.1.6
Provides: bundled-npm(dashdash) = 1.14.0
Provides: bundled-npm(jsbn) = 0.1.0
Provides: bundled-npm(jodid25519) = 1.0.2
Provides: bundled-npm(verror) = 1.3.6
Provides: bundled-npm(ecc-jsbn) = 0.1.1
Provides: bundled-npm(pinkie) = 2.0.4
Provides: bundled-npm(tweetnacl) = 0.13.3
Provides: bundled-npm(graceful-readlink) = 1.0.1
Provides: bundled-npm(generate-function) = 2.0.0
Provides: bundled-npm(generate-object-property) = 1.2.0
Provides: bundled-npm(jsonpointer) = 2.0.0
Provides: bundled-npm(escape-string-regexp) = 1.0.5
Provides: bundled-npm(ansi-styles) = 2.2.1
Provides: bundled-npm(xtend) = 4.0.1
Provides: bundled-npm(has-ansi) = 2.0.0
Provides: bundled-npm(number-is-nan) = 1.0.0
Provides: bundled-npm(supports-color) = 2.0.0
Provides: bundled-npm(is-property) = 1.0.2
Provides: bundled-npm(qs) = 6.2.1
AutoReq: no
AutoProv: no


%description
Packs CommonJs/AMD modules for the browser. Allows to split your codebase into multiple bundles, which can be loaded on demand. Support loaders to preprocess files, i.e. json, jade, coffee, css, less, ... and your custom stuff.

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

%setup -T -q -a 234 -D -n npm_cache

%build
npm install webpack@1.13.1 --cache-min Infinity --cache .  --verbose

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cd node_modules/webpack
cp -pfr README.md ../../
cp -pfr bin buildin hot lib package.json web_modules node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
# If any binaries are included, symlink them to bindir here
mkdir -p %{buildroot}%{nodejs_sitelib}/${npm_name}/bin
mkdir -p %{buildroot}%{_bindir}/
install -p -D -m0755 bin/webpack.js %{buildroot}%{nodejs_sitelib}/%{npm_name}/bin/webpack.js
ln -sf %{nodejs_sitelib}/%{npm_name}/bin/webpack.js %{buildroot}%{_bindir}/webpack.js

%check

%files
%{nodejs_sitelib}/%{npm_name}
%exclude %{nodejs_sitelib}/%{npm_name}/package.json
%{_bindir}/webpack.js

%files doc
%doc README.md

%changelog
