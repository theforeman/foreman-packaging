%global npm_name webpack

%{?nodejs_find_provides_and_requires}

Name: nodejs-%{npm_name}
Version: 3.4.1
Release: 3%{?dist}
Summary: Packs CommonJs/AMD modules for the browser
License: MIT
URL: https://github.com/webpack/webpack
Source0: http://registry.npmjs.org/webpack/-/webpack-3.4.1.tgz
Source1: http://registry.npmjs.org/acorn-dynamic-import/-/acorn-dynamic-import-2.0.2.tgz
Source2: http://registry.npmjs.org/interpret/-/interpret-1.0.3.tgz
Source3: http://registry.npmjs.org/async/-/async-2.5.0.tgz
Source4: http://registry.npmjs.org/ajv-keywords/-/ajv-keywords-2.1.0.tgz
Source5: http://registry.npmjs.org/enhanced-resolve/-/enhanced-resolve-3.4.1.tgz
Source6: http://registry.npmjs.org/escope/-/escope-3.6.0.tgz
Source7: http://registry.npmjs.org/acorn/-/acorn-5.1.1.tgz
Source8: http://registry.npmjs.org/loader-runner/-/loader-runner-2.3.0.tgz
Source9: http://registry.npmjs.org/memory-fs/-/memory-fs-0.4.1.tgz
Source10: http://registry.npmjs.org/mkdirp/-/mkdirp-0.5.1.tgz
Source11: http://registry.npmjs.org/json5/-/json5-0.5.1.tgz
Source12: http://registry.npmjs.org/json-loader/-/json-loader-0.5.7.tgz
Source13: http://registry.npmjs.org/loader-utils/-/loader-utils-1.1.0.tgz
Source14: http://registry.npmjs.org/node-libs-browser/-/node-libs-browser-2.0.0.tgz
Source15: http://registry.npmjs.org/tapable/-/tapable-0.2.8.tgz
Source16: http://registry.npmjs.org/supports-color/-/supports-color-4.2.1.tgz
Source17: http://registry.npmjs.org/uglifyjs-webpack-plugin/-/uglifyjs-webpack-plugin-0.4.6.tgz
Source18: http://registry.npmjs.org/watchpack/-/watchpack-1.4.0.tgz
Source19: http://registry.npmjs.org/webpack-sources/-/webpack-sources-1.0.1.tgz
Source20: http://registry.npmjs.org/source-map/-/source-map-0.5.6.tgz
Source21: http://registry.npmjs.org/ajv/-/ajv-5.2.2.tgz
Source22: http://registry.npmjs.org/yargs/-/yargs-8.0.2.tgz
Source23: http://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz
Source24: http://registry.npmjs.org/lodash/-/lodash-4.17.4.tgz
Source25: http://registry.npmjs.org/graceful-fs/-/graceful-fs-4.1.11.tgz
Source26: http://registry.npmjs.org/es6-weak-map/-/es6-weak-map-2.0.2.tgz
Source27: http://registry.npmjs.org/acorn/-/acorn-4.0.13.tgz
Source28: http://registry.npmjs.org/es6-map/-/es6-map-0.1.5.tgz
Source29: http://registry.npmjs.org/esrecurse/-/esrecurse-4.2.0.tgz
Source30: http://registry.npmjs.org/errno/-/errno-0.1.4.tgz
Source31: http://registry.npmjs.org/estraverse/-/estraverse-4.2.0.tgz
Source32: http://registry.npmjs.org/emojis-list/-/emojis-list-2.1.0.tgz
Source33: http://registry.npmjs.org/minimist/-/minimist-0.0.8.tgz
Source34: http://registry.npmjs.org/big.js/-/big.js-3.1.3.tgz
Source35: http://registry.npmjs.org/readable-stream/-/readable-stream-2.3.3.tgz
Source36: http://registry.npmjs.org/assert/-/assert-1.4.1.tgz
Source37: http://registry.npmjs.org/browserify-zlib/-/browserify-zlib-0.1.4.tgz
Source38: http://registry.npmjs.org/constants-browserify/-/constants-browserify-1.0.0.tgz
Source39: http://registry.npmjs.org/console-browserify/-/console-browserify-1.1.0.tgz
Source40: http://registry.npmjs.org/domain-browser/-/domain-browser-1.1.7.tgz
Source41: http://registry.npmjs.org/https-browserify/-/https-browserify-0.0.1.tgz
Source42: http://registry.npmjs.org/crypto-browserify/-/crypto-browserify-3.11.1.tgz
Source43: http://registry.npmjs.org/os-browserify/-/os-browserify-0.2.1.tgz
Source44: http://registry.npmjs.org/path-browserify/-/path-browserify-0.0.0.tgz
Source45: http://registry.npmjs.org/events/-/events-1.1.1.tgz
Source46: http://registry.npmjs.org/querystring-es3/-/querystring-es3-0.2.1.tgz
Source47: http://registry.npmjs.org/buffer/-/buffer-4.9.1.tgz
Source48: http://registry.npmjs.org/process/-/process-0.11.10.tgz
Source49: http://registry.npmjs.org/punycode/-/punycode-1.4.1.tgz
Source50: http://registry.npmjs.org/stream-browserify/-/stream-browserify-2.0.1.tgz
Source51: http://registry.npmjs.org/stream-http/-/stream-http-2.7.2.tgz
Source52: http://registry.npmjs.org/string_decoder/-/string_decoder-0.10.31.tgz
Source53: http://registry.npmjs.org/timers-browserify/-/timers-browserify-2.0.3.tgz
Source54: http://registry.npmjs.org/tty-browserify/-/tty-browserify-0.0.0.tgz
Source55: http://registry.npmjs.org/url/-/url-0.11.0.tgz
Source56: http://registry.npmjs.org/util/-/util-0.10.3.tgz
Source57: http://registry.npmjs.org/vm-browserify/-/vm-browserify-0.0.4.tgz
Source58: http://registry.npmjs.org/has-flag/-/has-flag-2.0.0.tgz
Source59: http://registry.npmjs.org/source-list-map/-/source-list-map-2.0.0.tgz
Source60: http://registry.npmjs.org/chokidar/-/chokidar-1.7.0.tgz
Source61: http://registry.npmjs.org/uglify-js/-/uglify-js-2.8.29.tgz
Source62: http://registry.npmjs.org/fast-deep-equal/-/fast-deep-equal-1.0.0.tgz
Source63: http://registry.npmjs.org/co/-/co-4.6.0.tgz
Source64: http://registry.npmjs.org/json-stable-stringify/-/json-stable-stringify-1.0.1.tgz
Source65: http://registry.npmjs.org/json-schema-traverse/-/json-schema-traverse-0.3.1.tgz
Source66: http://registry.npmjs.org/camelcase/-/camelcase-4.1.0.tgz
Source67: http://registry.npmjs.org/cliui/-/cliui-3.2.0.tgz
Source68: http://registry.npmjs.org/os-locale/-/os-locale-2.1.0.tgz
Source69: http://registry.npmjs.org/decamelize/-/decamelize-1.2.0.tgz
Source70: http://registry.npmjs.org/get-caller-file/-/get-caller-file-1.0.2.tgz
Source71: http://registry.npmjs.org/require-directory/-/require-directory-2.1.1.tgz
Source72: http://registry.npmjs.org/require-main-filename/-/require-main-filename-1.0.1.tgz
Source73: http://registry.npmjs.org/read-pkg-up/-/read-pkg-up-2.0.0.tgz
Source74: http://registry.npmjs.org/set-blocking/-/set-blocking-2.0.0.tgz
Source75: http://registry.npmjs.org/string-width/-/string-width-2.1.1.tgz
Source76: http://registry.npmjs.org/y18n/-/y18n-3.2.1.tgz
Source77: http://registry.npmjs.org/which-module/-/which-module-2.0.0.tgz
Source78: http://registry.npmjs.org/d/-/d-1.0.0.tgz
Source79: http://registry.npmjs.org/yargs-parser/-/yargs-parser-7.0.0.tgz
Source80: http://registry.npmjs.org/es6-iterator/-/es6-iterator-2.0.1.tgz
Source81: http://registry.npmjs.org/es6-symbol/-/es6-symbol-3.1.1.tgz
Source82: http://registry.npmjs.org/es5-ext/-/es5-ext-0.10.26.tgz
Source83: http://registry.npmjs.org/es6-set/-/es6-set-0.1.5.tgz
Source84: http://registry.npmjs.org/event-emitter/-/event-emitter-0.3.5.tgz
Source85: http://registry.npmjs.org/prr/-/prr-0.0.0.tgz
Source86: http://registry.npmjs.org/isarray/-/isarray-1.0.0.tgz
Source87: http://registry.npmjs.org/process-nextick-args/-/process-nextick-args-1.0.7.tgz
Source88: http://registry.npmjs.org/inherits/-/inherits-2.0.3.tgz
Source89: http://registry.npmjs.org/core-util-is/-/core-util-is-1.0.2.tgz
Source90: http://registry.npmjs.org/safe-buffer/-/safe-buffer-5.1.1.tgz
Source91: http://registry.npmjs.org/string_decoder/-/string_decoder-1.0.3.tgz
Source92: http://registry.npmjs.org/util-deprecate/-/util-deprecate-1.0.2.tgz
Source93: http://registry.npmjs.org/date-now/-/date-now-0.1.4.tgz
Source94: http://registry.npmjs.org/pako/-/pako-0.2.9.tgz
Source95: http://registry.npmjs.org/create-hash/-/create-hash-1.1.3.tgz
Source96: http://registry.npmjs.org/browserify-cipher/-/browserify-cipher-1.0.0.tgz
Source97: http://registry.npmjs.org/create-ecdh/-/create-ecdh-4.0.0.tgz
Source98: http://registry.npmjs.org/browserify-sign/-/browserify-sign-4.0.4.tgz
Source99: http://registry.npmjs.org/create-hmac/-/create-hmac-1.1.6.tgz
Source100: http://registry.npmjs.org/diffie-hellman/-/diffie-hellman-5.0.2.tgz
Source101: http://registry.npmjs.org/pbkdf2/-/pbkdf2-3.0.13.tgz
Source102: http://registry.npmjs.org/randombytes/-/randombytes-2.0.5.tgz
Source103: http://registry.npmjs.org/public-encrypt/-/public-encrypt-4.0.0.tgz
Source104: http://registry.npmjs.org/base64-js/-/base64-js-1.2.1.tgz
Source105: http://registry.npmjs.org/ieee754/-/ieee754-1.1.8.tgz
Source106: http://registry.npmjs.org/builtin-status-codes/-/builtin-status-codes-3.0.0.tgz
Source107: http://registry.npmjs.org/to-arraybuffer/-/to-arraybuffer-1.0.1.tgz
Source108: http://registry.npmjs.org/xtend/-/xtend-4.0.1.tgz
Source109: http://registry.npmjs.org/inherits/-/inherits-2.0.1.tgz
Source110: http://registry.npmjs.org/setimmediate/-/setimmediate-1.0.5.tgz
Source111: http://registry.npmjs.org/global/-/global-4.3.2.tgz
Source112: http://registry.npmjs.org/querystring/-/querystring-0.2.0.tgz
Source113: http://registry.npmjs.org/punycode/-/punycode-1.3.2.tgz
Source114: http://registry.npmjs.org/indexof/-/indexof-0.0.1.tgz
Source115: http://registry.npmjs.org/anymatch/-/anymatch-1.3.2.tgz
Source116: http://registry.npmjs.org/async-each/-/async-each-1.0.1.tgz
Source117: http://registry.npmjs.org/glob-parent/-/glob-parent-2.0.0.tgz
Source118: http://registry.npmjs.org/is-binary-path/-/is-binary-path-1.0.1.tgz
Source119: http://registry.npmjs.org/path-is-absolute/-/path-is-absolute-1.0.1.tgz
Source120: http://registry.npmjs.org/is-glob/-/is-glob-2.0.1.tgz
Source121: http://registry.npmjs.org/readdirp/-/readdirp-2.1.0.tgz
Source122: http://registry.npmjs.org/fsevents/-/fsevents-1.1.2.tgz
Source123: http://registry.npmjs.org/uglify-to-browserify/-/uglify-to-browserify-1.0.2.tgz
Source124: http://registry.npmjs.org/jsonify/-/jsonify-0.0.0.tgz
Source125: http://registry.npmjs.org/string-width/-/string-width-1.0.2.tgz
Source126: http://registry.npmjs.org/strip-ansi/-/strip-ansi-3.0.1.tgz
Source127: http://registry.npmjs.org/wrap-ansi/-/wrap-ansi-2.1.0.tgz
Source128: http://registry.npmjs.org/lcid/-/lcid-1.0.0.tgz
Source129: http://registry.npmjs.org/execa/-/execa-0.7.0.tgz
Source130: http://registry.npmjs.org/mem/-/mem-1.1.0.tgz
Source131: http://registry.npmjs.org/yargs/-/yargs-3.10.0.tgz
Source132: http://registry.npmjs.org/read-pkg/-/read-pkg-2.0.0.tgz
Source133: http://registry.npmjs.org/find-up/-/find-up-2.1.0.tgz
Source134: http://registry.npmjs.org/is-fullwidth-code-point/-/is-fullwidth-code-point-2.0.0.tgz
Source135: http://registry.npmjs.org/strip-ansi/-/strip-ansi-4.0.0.tgz
Source136: http://registry.npmjs.org/cipher-base/-/cipher-base-1.0.4.tgz
Source137: http://registry.npmjs.org/ripemd160/-/ripemd160-2.0.1.tgz
Source138: http://registry.npmjs.org/browserify-aes/-/browserify-aes-1.0.6.tgz
Source139: http://registry.npmjs.org/browserify-des/-/browserify-des-1.0.0.tgz
Source140: http://registry.npmjs.org/sha.js/-/sha.js-2.4.8.tgz
Source141: http://registry.npmjs.org/evp_bytestokey/-/evp_bytestokey-1.0.0.tgz
Source142: http://registry.npmjs.org/browserify-rsa/-/browserify-rsa-4.0.1.tgz
Source143: http://registry.npmjs.org/bn.js/-/bn.js-4.11.7.tgz
Source144: http://registry.npmjs.org/elliptic/-/elliptic-6.4.0.tgz
Source145: http://registry.npmjs.org/parse-asn1/-/parse-asn1-5.1.0.tgz
Source146: http://registry.npmjs.org/miller-rabin/-/miller-rabin-4.0.0.tgz
Source147: http://registry.npmjs.org/process/-/process-0.5.2.tgz
Source148: http://registry.npmjs.org/normalize-path/-/normalize-path-2.1.1.tgz
Source149: http://registry.npmjs.org/min-document/-/min-document-2.19.0.tgz
Source150: http://registry.npmjs.org/binary-extensions/-/binary-extensions-1.9.0.tgz
Source151: http://registry.npmjs.org/is-extglob/-/is-extglob-1.0.0.tgz
Source152: http://registry.npmjs.org/micromatch/-/micromatch-2.3.11.tgz
Source153: http://registry.npmjs.org/set-immediate-shim/-/set-immediate-shim-1.0.1.tgz
Source154: http://registry.npmjs.org/is-fullwidth-code-point/-/is-fullwidth-code-point-1.0.0.tgz
Source155: http://registry.npmjs.org/code-point-at/-/code-point-at-1.1.0.tgz
Source156: http://registry.npmjs.org/minimatch/-/minimatch-3.0.4.tgz
Source157: http://registry.npmjs.org/node-pre-gyp/-/node-pre-gyp-0.6.36.tgz
Source158: http://registry.npmjs.org/ansi-regex/-/ansi-regex-2.1.1.tgz
Source159: http://registry.npmjs.org/invert-kv/-/invert-kv-1.0.0.tgz
Source160: http://registry.npmjs.org/nan/-/nan-2.6.2.tgz
Source161: http://registry.npmjs.org/is-stream/-/is-stream-1.1.0.tgz
Source162: http://registry.npmjs.org/npm-run-path/-/npm-run-path-2.0.2.tgz
Source163: http://registry.npmjs.org/get-stream/-/get-stream-3.0.0.tgz
Source164: http://registry.npmjs.org/p-finally/-/p-finally-1.0.0.tgz
Source165: http://registry.npmjs.org/cross-spawn/-/cross-spawn-5.1.0.tgz
Source166: http://registry.npmjs.org/signal-exit/-/signal-exit-3.0.2.tgz
Source167: http://registry.npmjs.org/strip-eof/-/strip-eof-1.0.0.tgz
Source168: http://registry.npmjs.org/mimic-fn/-/mimic-fn-1.1.0.tgz
Source169: http://registry.npmjs.org/camelcase/-/camelcase-1.2.1.tgz
Source170: http://registry.npmjs.org/window-size/-/window-size-0.1.0.tgz
Source171: http://registry.npmjs.org/cliui/-/cliui-2.1.0.tgz
Source172: http://registry.npmjs.org/path-type/-/path-type-2.0.0.tgz
Source173: http://registry.npmjs.org/load-json-file/-/load-json-file-2.0.0.tgz
Source174: http://registry.npmjs.org/normalize-package-data/-/normalize-package-data-2.4.0.tgz
Source175: http://registry.npmjs.org/locate-path/-/locate-path-2.0.0.tgz
Source176: http://registry.npmjs.org/buffer-xor/-/buffer-xor-1.0.3.tgz
Source177: http://registry.npmjs.org/ansi-regex/-/ansi-regex-3.0.0.tgz
Source178: http://registry.npmjs.org/hash-base/-/hash-base-2.0.2.tgz
Source179: http://registry.npmjs.org/des.js/-/des.js-1.0.0.tgz
Source180: http://registry.npmjs.org/minimalistic-assert/-/minimalistic-assert-1.0.0.tgz
Source181: http://registry.npmjs.org/brorand/-/brorand-1.1.0.tgz
Source182: http://registry.npmjs.org/hmac-drbg/-/hmac-drbg-1.0.1.tgz
Source183: http://registry.npmjs.org/minimalistic-crypto-utils/-/minimalistic-crypto-utils-1.0.1.tgz
Source184: http://registry.npmjs.org/hash.js/-/hash.js-1.1.3.tgz
Source185: http://registry.npmjs.org/asn1.js/-/asn1.js-4.9.1.tgz
Source186: http://registry.npmjs.org/remove-trailing-separator/-/remove-trailing-separator-1.0.2.tgz
Source187: http://registry.npmjs.org/dom-walk/-/dom-walk-0.1.1.tgz
Source188: http://registry.npmjs.org/arr-diff/-/arr-diff-2.0.0.tgz
Source189: http://registry.npmjs.org/array-unique/-/array-unique-0.2.1.tgz
Source190: http://registry.npmjs.org/braces/-/braces-1.8.5.tgz
Source191: http://registry.npmjs.org/expand-brackets/-/expand-brackets-0.1.5.tgz
Source192: http://registry.npmjs.org/filename-regex/-/filename-regex-2.0.1.tgz
Source193: http://registry.npmjs.org/extglob/-/extglob-0.3.2.tgz
Source194: http://registry.npmjs.org/object.omit/-/object.omit-2.0.1.tgz
Source195: http://registry.npmjs.org/parse-glob/-/parse-glob-3.0.4.tgz
Source196: http://registry.npmjs.org/kind-of/-/kind-of-3.2.2.tgz
Source197: http://registry.npmjs.org/number-is-nan/-/number-is-nan-1.0.1.tgz
Source198: http://registry.npmjs.org/regex-cache/-/regex-cache-0.4.3.tgz
Source199: http://registry.npmjs.org/brace-expansion/-/brace-expansion-1.1.8.tgz
Source200: http://registry.npmjs.org/nopt/-/nopt-4.0.1.tgz
Source201: http://registry.npmjs.org/npmlog/-/npmlog-4.1.2.tgz
Source202: http://registry.npmjs.org/rc/-/rc-1.2.1.tgz
Source203: http://registry.npmjs.org/request/-/request-2.81.0.tgz
Source204: http://registry.npmjs.org/path-key/-/path-key-2.0.1.tgz
Source205: http://registry.npmjs.org/tar/-/tar-2.2.1.tgz
Source206: http://registry.npmjs.org/semver/-/semver-5.4.1.tgz
Source207: http://registry.npmjs.org/rimraf/-/rimraf-2.6.1.tgz
Source208: http://registry.npmjs.org/lru-cache/-/lru-cache-4.1.1.tgz
Source209: http://registry.npmjs.org/tar-pack/-/tar-pack-3.4.0.tgz
Source210: http://registry.npmjs.org/shebang-command/-/shebang-command-1.2.0.tgz
Source211: http://registry.npmjs.org/right-align/-/right-align-0.1.3.tgz
Source212: http://registry.npmjs.org/center-align/-/center-align-0.1.3.tgz
Source213: http://registry.npmjs.org/wordwrap/-/wordwrap-0.0.2.tgz
Source214: http://registry.npmjs.org/parse-json/-/parse-json-2.2.0.tgz
Source215: http://registry.npmjs.org/pify/-/pify-2.3.0.tgz
Source216: http://registry.npmjs.org/which/-/which-1.3.0.tgz
Source217: http://registry.npmjs.org/strip-bom/-/strip-bom-3.0.0.tgz
Source218: http://registry.npmjs.org/is-builtin-module/-/is-builtin-module-1.0.0.tgz
Source219: http://registry.npmjs.org/p-locate/-/p-locate-2.0.0.tgz
Source220: http://registry.npmjs.org/validate-npm-package-license/-/validate-npm-package-license-3.0.1.tgz
Source221: http://registry.npmjs.org/path-exists/-/path-exists-3.0.0.tgz
Source222: http://registry.npmjs.org/hosted-git-info/-/hosted-git-info-2.5.0.tgz
Source223: http://registry.npmjs.org/preserve/-/preserve-0.2.0.tgz
Source224: http://registry.npmjs.org/expand-range/-/expand-range-1.8.2.tgz
Source225: http://registry.npmjs.org/arr-flatten/-/arr-flatten-1.1.0.tgz
Source226: http://registry.npmjs.org/repeat-element/-/repeat-element-1.1.2.tgz
Source227: http://registry.npmjs.org/is-posix-bracket/-/is-posix-bracket-0.1.1.tgz
Source228: http://registry.npmjs.org/is-extendable/-/is-extendable-0.1.1.tgz
Source229: http://registry.npmjs.org/glob-base/-/glob-base-0.3.0.tgz
Source230: http://registry.npmjs.org/for-own/-/for-own-0.1.5.tgz
Source231: http://registry.npmjs.org/is-dotfile/-/is-dotfile-1.0.3.tgz
Source232: http://registry.npmjs.org/is-buffer/-/is-buffer-1.1.5.tgz
Source233: http://registry.npmjs.org/is-equal-shallow/-/is-equal-shallow-0.1.3.tgz
Source234: http://registry.npmjs.org/concat-map/-/concat-map-0.0.1.tgz
Source235: http://registry.npmjs.org/is-primitive/-/is-primitive-2.0.0.tgz
Source236: http://registry.npmjs.org/osenv/-/osenv-0.1.4.tgz
Source237: http://registry.npmjs.org/balanced-match/-/balanced-match-1.0.0.tgz
Source238: http://registry.npmjs.org/console-control-strings/-/console-control-strings-1.1.0.tgz
Source239: http://registry.npmjs.org/abbrev/-/abbrev-1.1.0.tgz
Source240: http://registry.npmjs.org/are-we-there-yet/-/are-we-there-yet-1.1.4.tgz
Source241: http://registry.npmjs.org/aws-sign2/-/aws-sign2-0.6.0.tgz
Source242: http://registry.npmjs.org/deep-extend/-/deep-extend-0.4.2.tgz
Source243: http://registry.npmjs.org/strip-json-comments/-/strip-json-comments-2.0.1.tgz
Source244: http://registry.npmjs.org/ini/-/ini-1.3.4.tgz
Source245: http://registry.npmjs.org/minimist/-/minimist-1.2.0.tgz
Source246: http://registry.npmjs.org/aws4/-/aws4-1.6.0.tgz
Source247: http://registry.npmjs.org/gauge/-/gauge-2.7.4.tgz
Source248: http://registry.npmjs.org/caseless/-/caseless-0.12.0.tgz
Source249: http://registry.npmjs.org/combined-stream/-/combined-stream-1.0.5.tgz
Source250: http://registry.npmjs.org/extend/-/extend-3.0.1.tgz
Source251: http://registry.npmjs.org/forever-agent/-/forever-agent-0.6.1.tgz
Source252: http://registry.npmjs.org/http-signature/-/http-signature-1.1.1.tgz
Source253: http://registry.npmjs.org/form-data/-/form-data-2.1.4.tgz
Source254: http://registry.npmjs.org/har-validator/-/har-validator-4.2.1.tgz
Source255: http://registry.npmjs.org/hawk/-/hawk-3.1.3.tgz
Source256: http://registry.npmjs.org/is-typedarray/-/is-typedarray-1.0.0.tgz
Source257: http://registry.npmjs.org/json-stringify-safe/-/json-stringify-safe-5.0.1.tgz
Source258: http://registry.npmjs.org/isstream/-/isstream-0.1.2.tgz
Source259: http://registry.npmjs.org/oauth-sign/-/oauth-sign-0.8.2.tgz
Source260: http://registry.npmjs.org/performance-now/-/performance-now-0.2.0.tgz
Source261: http://registry.npmjs.org/qs/-/qs-6.4.0.tgz
Source262: http://registry.npmjs.org/mime-types/-/mime-types-2.1.16.tgz
Source263: http://registry.npmjs.org/stringstream/-/stringstream-0.0.5.tgz
Source264: http://registry.npmjs.org/tunnel-agent/-/tunnel-agent-0.6.0.tgz
Source265: http://registry.npmjs.org/block-stream/-/block-stream-0.0.9.tgz
Source266: http://registry.npmjs.org/tough-cookie/-/tough-cookie-2.3.2.tgz
Source267: http://registry.npmjs.org/uuid/-/uuid-3.1.0.tgz
Source268: http://registry.npmjs.org/fstream/-/fstream-1.0.11.tgz
Source269: http://registry.npmjs.org/pseudomap/-/pseudomap-1.0.2.tgz
Source270: http://registry.npmjs.org/yallist/-/yallist-2.1.2.tgz
Source271: http://registry.npmjs.org/fstream-ignore/-/fstream-ignore-1.0.5.tgz
Source272: http://registry.npmjs.org/debug/-/debug-2.6.8.tgz
Source273: http://registry.npmjs.org/glob/-/glob-7.1.2.tgz
Source274: http://registry.npmjs.org/once/-/once-1.4.0.tgz
Source275: http://registry.npmjs.org/shebang-regex/-/shebang-regex-1.0.0.tgz
Source276: http://registry.npmjs.org/uid-number/-/uid-number-0.0.6.tgz
Source277: http://registry.npmjs.org/align-text/-/align-text-0.1.4.tgz
Source278: http://registry.npmjs.org/lazy-cache/-/lazy-cache-1.0.4.tgz
Source279: http://registry.npmjs.org/isexe/-/isexe-2.0.0.tgz
Source280: http://registry.npmjs.org/error-ex/-/error-ex-1.3.1.tgz
Source281: http://registry.npmjs.org/p-limit/-/p-limit-1.1.0.tgz
Source282: http://registry.npmjs.org/spdx-expression-parse/-/spdx-expression-parse-1.0.4.tgz
Source283: http://registry.npmjs.org/builtin-modules/-/builtin-modules-1.1.1.tgz
Source284: http://registry.npmjs.org/spdx-correct/-/spdx-correct-1.0.2.tgz
Source285: http://registry.npmjs.org/fill-range/-/fill-range-2.2.3.tgz
Source286: http://registry.npmjs.org/os-tmpdir/-/os-tmpdir-1.0.2.tgz
Source287: http://registry.npmjs.org/os-homedir/-/os-homedir-1.0.2.tgz
Source288: http://registry.npmjs.org/for-in/-/for-in-1.0.2.tgz
Source289: http://registry.npmjs.org/delegates/-/delegates-1.0.0.tgz
Source290: http://registry.npmjs.org/aproba/-/aproba-1.1.2.tgz
Source291: http://registry.npmjs.org/has-unicode/-/has-unicode-2.0.1.tgz
Source292: http://registry.npmjs.org/wide-align/-/wide-align-1.1.2.tgz
Source293: http://registry.npmjs.org/delayed-stream/-/delayed-stream-1.0.0.tgz
Source294: http://registry.npmjs.org/assert-plus/-/assert-plus-0.2.0.tgz
Source295: http://registry.npmjs.org/jsprim/-/jsprim-1.4.1.tgz
Source296: http://registry.npmjs.org/asynckit/-/asynckit-0.4.0.tgz
Source297: http://registry.npmjs.org/har-schema/-/har-schema-1.0.5.tgz
Source298: http://registry.npmjs.org/sshpk/-/sshpk-1.13.1.tgz
Source299: http://registry.npmjs.org/hoek/-/hoek-2.16.3.tgz
Source300: http://registry.npmjs.org/sntp/-/sntp-1.0.9.tgz
Source301: http://registry.npmjs.org/cryptiles/-/cryptiles-2.0.5.tgz
Source302: http://registry.npmjs.org/mime-db/-/mime-db-1.29.0.tgz
Source303: http://registry.npmjs.org/boom/-/boom-2.10.1.tgz
Source304: http://registry.npmjs.org/ajv/-/ajv-4.11.8.tgz
Source305: http://registry.npmjs.org/fs.realpath/-/fs.realpath-1.0.0.tgz
Source306: http://registry.npmjs.org/inflight/-/inflight-1.0.6.tgz
Source307: http://registry.npmjs.org/ms/-/ms-2.0.0.tgz
Source308: http://registry.npmjs.org/wrappy/-/wrappy-1.0.2.tgz
Source309: http://registry.npmjs.org/is-arrayish/-/is-arrayish-0.2.1.tgz
Source310: http://registry.npmjs.org/longest/-/longest-1.0.1.tgz
Source311: http://registry.npmjs.org/spdx-license-ids/-/spdx-license-ids-1.2.2.tgz
Source312: http://registry.npmjs.org/is-number/-/is-number-2.1.0.tgz
Source313: http://registry.npmjs.org/repeat-string/-/repeat-string-1.6.1.tgz
Source314: http://registry.npmjs.org/isobject/-/isobject-2.1.0.tgz
Source315: http://registry.npmjs.org/assert-plus/-/assert-plus-1.0.0.tgz
Source316: http://registry.npmjs.org/randomatic/-/randomatic-1.1.7.tgz
Source317: http://registry.npmjs.org/extsprintf/-/extsprintf-1.3.0.tgz
Source318: http://registry.npmjs.org/json-schema/-/json-schema-0.2.3.tgz
Source319: http://registry.npmjs.org/verror/-/verror-1.10.0.tgz
Source320: http://registry.npmjs.org/jsbn/-/jsbn-0.1.1.tgz
Source321: http://registry.npmjs.org/getpass/-/getpass-0.1.7.tgz
Source322: http://registry.npmjs.org/ecc-jsbn/-/ecc-jsbn-0.1.1.tgz
Source323: http://registry.npmjs.org/dashdash/-/dashdash-1.14.1.tgz
Source324: http://registry.npmjs.org/asn1/-/asn1-0.2.3.tgz
Source325: http://registry.npmjs.org/bcrypt-pbkdf/-/bcrypt-pbkdf-1.0.1.tgz
Source326: http://registry.npmjs.org/tweetnacl/-/tweetnacl-0.14.5.tgz
Source327: http://registry.npmjs.org/is-number/-/is-number-3.0.0.tgz
Source328: http://registry.npmjs.org/kind-of/-/kind-of-4.0.0.tgz
Source329: webpack-3.4.1-registry.npmjs.org.tgz
BuildRequires: nodejs-packaging
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: npm(%{npm_name}) = %{version}
AutoReq: no
AutoProv: no

%description
%{summary}

%prep
mkdir -p npm_cache
for tgz in %{sources}; do
  echo $tgz | grep -q registry.npmjs.org || npm cache add --cache ./npm_cache $tgz
done

%setup -T -q -a 329 -D -n npm_cache

%build
npm install --cache-min Infinity --cache . --no-optional --global-style true %{npm_name}@%{version}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cd node_modules/webpack
cp -pfr LICENSE README.md bin buildin hot lib package.json schemas web_modules node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pf README.md LICENSE ../../
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}/bin
mkdir -p %{buildroot}%{_bindir}/
install -p -D -m0755 bin/webpack.js %{buildroot}%{nodejs_sitelib}/%{npm_name}/bin/webpack
ln -sf %{nodejs_sitelib}/%{npm_name}/bin/webpack %{buildroot}%{_bindir}/webpack

%files
%{nodejs_sitelib}/%{npm_name}
%{_bindir}/webpack
%license LICENSE
%doc README.md

%changelog
* Sat Oct 14 2017 Eric D. Helms <ericdhelms@gmail.com> 3.4.1-2
- Bump release to rebuild

* Mon Aug 07 2017 Eric D. Helms <ericdhelms@gmail.com> 3.4.1-1
- Update nodejs-weebpack to 3.4.1 (me@daniellobato.me)

* Sat Jul 15 2017 Eric D. Helms <ericdhelms@gmail.com> 3.0.0-2
- Add back missing Provides: npm (ericdhelms@gmail.com)

* Wed Jul 12 2017 Eric D. Helms <ericdhelms@gmail.com> 3.0.0-1
- update webpack to v3.0 (ohadlevy@gmail.com)
