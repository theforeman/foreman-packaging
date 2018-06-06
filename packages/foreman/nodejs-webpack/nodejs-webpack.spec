%global npm_name webpack

Name: nodejs-%{npm_name}
Version: 3.12.0
Release: 1%{?dist}
Summary: Packs CommonJs/AMD modules for the browser
License: MIT
Group: Development/Libraries
URL: https://github.com/webpack/webpack
Source0: https://registry.npmjs.org/webpack/-/webpack-3.12.0.tgz
Source1: https://registry.npmjs.org/ajv-keywords/-/ajv-keywords-3.2.0.tgz
Source2: https://registry.npmjs.org/acorn-dynamic-import/-/acorn-dynamic-import-2.0.2.tgz
Source3: https://registry.npmjs.org/interpret/-/interpret-1.1.0.tgz
Source4: https://registry.npmjs.org/escope/-/escope-3.6.0.tgz
Source5: https://registry.npmjs.org/acorn/-/acorn-5.6.2.tgz
Source6: https://registry.npmjs.org/async/-/async-2.6.1.tgz
Source7: https://registry.npmjs.org/enhanced-resolve/-/enhanced-resolve-3.4.1.tgz
Source8: https://registry.npmjs.org/json5/-/json5-0.5.1.tgz
Source9: https://registry.npmjs.org/json-loader/-/json-loader-0.5.7.tgz
Source10: https://registry.npmjs.org/loader-runner/-/loader-runner-2.3.0.tgz
Source11: https://registry.npmjs.org/loader-utils/-/loader-utils-1.1.0.tgz
Source12: https://registry.npmjs.org/memory-fs/-/memory-fs-0.4.1.tgz
Source13: https://registry.npmjs.org/mkdirp/-/mkdirp-0.5.1.tgz
Source14: https://registry.npmjs.org/ajv/-/ajv-6.5.0.tgz
Source15: https://registry.npmjs.org/node-libs-browser/-/node-libs-browser-2.1.0.tgz
Source16: https://registry.npmjs.org/tapable/-/tapable-0.2.8.tgz
Source17: https://registry.npmjs.org/supports-color/-/supports-color-4.5.0.tgz
Source18: https://registry.npmjs.org/source-map/-/source-map-0.5.7.tgz
Source19: https://registry.npmjs.org/watchpack/-/watchpack-1.6.0.tgz
Source20: https://registry.npmjs.org/webpack-sources/-/webpack-sources-1.1.0.tgz
Source21: https://registry.npmjs.org/es6-map/-/es6-map-0.1.5.tgz
Source22: https://registry.npmjs.org/uglifyjs-webpack-plugin/-/uglifyjs-webpack-plugin-0.4.6.tgz
Source23: https://registry.npmjs.org/es6-weak-map/-/es6-weak-map-2.0.2.tgz
Source24: https://registry.npmjs.org/esrecurse/-/esrecurse-4.2.1.tgz
Source25: https://registry.npmjs.org/acorn/-/acorn-4.0.13.tgz
Source26: https://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz
Source27: https://registry.npmjs.org/graceful-fs/-/graceful-fs-4.1.11.tgz
Source28: https://registry.npmjs.org/yargs/-/yargs-8.0.2.tgz
Source29: https://registry.npmjs.org/big.js/-/big.js-3.2.0.tgz
Source30: https://registry.npmjs.org/lodash/-/lodash-4.17.10.tgz
Source31: https://registry.npmjs.org/estraverse/-/estraverse-4.2.0.tgz
Source32: https://registry.npmjs.org/emojis-list/-/emojis-list-2.1.0.tgz
Source33: https://registry.npmjs.org/fast-deep-equal/-/fast-deep-equal-2.0.1.tgz
Source34: https://registry.npmjs.org/fast-json-stable-stringify/-/fast-json-stable-stringify-2.0.0.tgz
Source35: https://registry.npmjs.org/json-schema-traverse/-/json-schema-traverse-0.3.1.tgz
Source36: https://registry.npmjs.org/minimist/-/minimist-0.0.8.tgz
Source37: https://registry.npmjs.org/errno/-/errno-0.1.7.tgz
Source38: https://registry.npmjs.org/readable-stream/-/readable-stream-2.3.6.tgz
Source39: https://registry.npmjs.org/browserify-zlib/-/browserify-zlib-0.2.0.tgz
Source40: https://registry.npmjs.org/constants-browserify/-/constants-browserify-1.0.0.tgz
Source41: https://registry.npmjs.org/console-browserify/-/console-browserify-1.1.0.tgz
Source42: https://registry.npmjs.org/uri-js/-/uri-js-4.2.2.tgz
Source43: https://registry.npmjs.org/assert/-/assert-1.4.1.tgz
Source44: https://registry.npmjs.org/buffer/-/buffer-4.9.1.tgz
Source45: https://registry.npmjs.org/domain-browser/-/domain-browser-1.2.0.tgz
Source46: https://registry.npmjs.org/path-browserify/-/path-browserify-0.0.0.tgz
Source47: https://registry.npmjs.org/os-browserify/-/os-browserify-0.3.0.tgz
Source48: https://registry.npmjs.org/https-browserify/-/https-browserify-1.0.0.tgz
Source49: https://registry.npmjs.org/events/-/events-1.1.1.tgz
Source50: https://registry.npmjs.org/process/-/process-0.11.10.tgz
Source51: https://registry.npmjs.org/crypto-browserify/-/crypto-browserify-3.12.0.tgz
Source52: https://registry.npmjs.org/querystring-es3/-/querystring-es3-0.2.1.tgz
Source53: https://registry.npmjs.org/punycode/-/punycode-1.4.1.tgz
Source54: https://registry.npmjs.org/stream-browserify/-/stream-browserify-2.0.1.tgz
Source55: https://registry.npmjs.org/stream-http/-/stream-http-2.8.3.tgz
Source56: https://registry.npmjs.org/string_decoder/-/string_decoder-1.1.1.tgz
Source57: https://registry.npmjs.org/url/-/url-0.11.0.tgz
Source58: https://registry.npmjs.org/util/-/util-0.10.4.tgz
Source59: https://registry.npmjs.org/vm-browserify/-/vm-browserify-0.0.4.tgz
Source60: https://registry.npmjs.org/timers-browserify/-/timers-browserify-2.0.10.tgz
Source61: https://registry.npmjs.org/has-flag/-/has-flag-2.0.0.tgz
Source62: https://registry.npmjs.org/tty-browserify/-/tty-browserify-0.0.0.tgz
Source63: https://registry.npmjs.org/source-list-map/-/source-list-map-2.0.0.tgz
Source64: https://registry.npmjs.org/neo-async/-/neo-async-2.5.1.tgz
Source65: https://registry.npmjs.org/chokidar/-/chokidar-2.0.3.tgz
Source66: https://registry.npmjs.org/es6-set/-/es6-set-0.1.5.tgz
Source67: https://registry.npmjs.org/es5-ext/-/es5-ext-0.10.45.tgz
Source68: https://registry.npmjs.org/source-map/-/source-map-0.6.1.tgz
Source69: https://registry.npmjs.org/es6-iterator/-/es6-iterator-2.0.3.tgz
Source70: https://registry.npmjs.org/event-emitter/-/event-emitter-0.3.5.tgz
Source71: https://registry.npmjs.org/es6-symbol/-/es6-symbol-3.1.1.tgz
Source72: https://registry.npmjs.org/d/-/d-1.0.0.tgz
Source73: https://registry.npmjs.org/uglify-js/-/uglify-js-2.8.29.tgz
Source74: https://registry.npmjs.org/decamelize/-/decamelize-1.2.0.tgz
Source75: https://registry.npmjs.org/read-pkg-up/-/read-pkg-up-2.0.0.tgz
Source76: https://registry.npmjs.org/camelcase/-/camelcase-4.1.0.tgz
Source77: https://registry.npmjs.org/get-caller-file/-/get-caller-file-1.0.2.tgz
Source78: https://registry.npmjs.org/os-locale/-/os-locale-2.1.0.tgz
Source79: https://registry.npmjs.org/cliui/-/cliui-3.2.0.tgz
Source80: https://registry.npmjs.org/require-main-filename/-/require-main-filename-1.0.1.tgz
Source81: https://registry.npmjs.org/require-directory/-/require-directory-2.1.1.tgz
Source82: https://registry.npmjs.org/set-blocking/-/set-blocking-2.0.0.tgz
Source83: https://registry.npmjs.org/which-module/-/which-module-2.0.0.tgz
Source84: https://registry.npmjs.org/string-width/-/string-width-2.1.1.tgz
Source85: https://registry.npmjs.org/y18n/-/y18n-3.2.1.tgz
Source86: https://registry.npmjs.org/core-util-is/-/core-util-is-1.0.2.tgz
Source87: https://registry.npmjs.org/yargs-parser/-/yargs-parser-7.0.0.tgz
Source88: https://registry.npmjs.org/isarray/-/isarray-1.0.0.tgz
Source89: https://registry.npmjs.org/prr/-/prr-1.0.1.tgz
Source90: https://registry.npmjs.org/inherits/-/inherits-2.0.3.tgz
Source91: https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.1.2.tgz
Source92: https://registry.npmjs.org/process-nextick-args/-/process-nextick-args-2.0.0.tgz
Source93: https://registry.npmjs.org/util-deprecate/-/util-deprecate-1.0.2.tgz
Source94: https://registry.npmjs.org/date-now/-/date-now-0.1.4.tgz
Source95: https://registry.npmjs.org/util/-/util-0.10.3.tgz
Source96: https://registry.npmjs.org/punycode/-/punycode-2.1.1.tgz
Source97: https://registry.npmjs.org/base64-js/-/base64-js-1.3.0.tgz
Source98: https://registry.npmjs.org/ieee754/-/ieee754-1.1.11.tgz
Source99: https://registry.npmjs.org/browserify-cipher/-/browserify-cipher-1.0.1.tgz
Source100: https://registry.npmjs.org/create-ecdh/-/create-ecdh-4.0.3.tgz
Source101: https://registry.npmjs.org/create-hash/-/create-hash-1.2.0.tgz
Source102: https://registry.npmjs.org/browserify-sign/-/browserify-sign-4.0.4.tgz
Source103: https://registry.npmjs.org/create-hmac/-/create-hmac-1.1.7.tgz
Source104: https://registry.npmjs.org/diffie-hellman/-/diffie-hellman-5.0.3.tgz
Source105: https://registry.npmjs.org/public-encrypt/-/public-encrypt-4.0.2.tgz
Source106: https://registry.npmjs.org/randomfill/-/randomfill-1.0.4.tgz
Source107: https://registry.npmjs.org/randombytes/-/randombytes-2.0.6.tgz
Source108: https://registry.npmjs.org/pbkdf2/-/pbkdf2-3.0.16.tgz
Source109: https://registry.npmjs.org/to-arraybuffer/-/to-arraybuffer-1.0.1.tgz
Source110: https://registry.npmjs.org/xtend/-/xtend-4.0.1.tgz
Source111: https://registry.npmjs.org/punycode/-/punycode-1.3.2.tgz
Source112: https://registry.npmjs.org/querystring/-/querystring-0.2.0.tgz
Source113: https://registry.npmjs.org/indexof/-/indexof-0.0.1.tgz
Source114: https://registry.npmjs.org/async-each/-/async-each-1.0.1.tgz
Source115: https://registry.npmjs.org/setimmediate/-/setimmediate-1.0.5.tgz
Source116: https://registry.npmjs.org/anymatch/-/anymatch-2.0.0.tgz
Source117: https://registry.npmjs.org/glob-parent/-/glob-parent-3.1.0.tgz
Source118: https://registry.npmjs.org/normalize-path/-/normalize-path-2.1.1.tgz
Source119: https://registry.npmjs.org/is-glob/-/is-glob-4.0.0.tgz
Source120: https://registry.npmjs.org/is-binary-path/-/is-binary-path-1.0.1.tgz
Source121: https://registry.npmjs.org/path-is-absolute/-/path-is-absolute-1.0.1.tgz
Source122: https://registry.npmjs.org/readdirp/-/readdirp-2.1.0.tgz
Source123: https://registry.npmjs.org/fsevents/-/fsevents-1.2.4.tgz
Source124: https://registry.npmjs.org/upath/-/upath-1.1.0.tgz
Source125: https://registry.npmjs.org/braces/-/braces-2.3.2.tgz
Source126: https://registry.npmjs.org/next-tick/-/next-tick-1.0.0.tgz
Source127: https://registry.npmjs.org/find-up/-/find-up-2.1.0.tgz
Source128: https://registry.npmjs.org/read-pkg/-/read-pkg-2.0.0.tgz
Source129: https://registry.npmjs.org/execa/-/execa-0.7.0.tgz
Source130: https://registry.npmjs.org/uglify-to-browserify/-/uglify-to-browserify-1.0.2.tgz
Source131: https://registry.npmjs.org/mem/-/mem-1.1.0.tgz
Source132: https://registry.npmjs.org/lcid/-/lcid-1.0.0.tgz
Source133: https://registry.npmjs.org/string-width/-/string-width-1.0.2.tgz
Source134: https://registry.npmjs.org/yargs/-/yargs-3.10.0.tgz
Source135: https://registry.npmjs.org/is-fullwidth-code-point/-/is-fullwidth-code-point-2.0.0.tgz
Source136: https://registry.npmjs.org/strip-ansi/-/strip-ansi-3.0.1.tgz
Source137: https://registry.npmjs.org/wrap-ansi/-/wrap-ansi-2.1.0.tgz
Source138: https://registry.npmjs.org/strip-ansi/-/strip-ansi-4.0.0.tgz
Source139: https://registry.npmjs.org/browserify-des/-/browserify-des-1.0.1.tgz
Source140: https://registry.npmjs.org/browserify-aes/-/browserify-aes-1.2.0.tgz
Source141: https://registry.npmjs.org/inherits/-/inherits-2.0.1.tgz
Source142: https://registry.npmjs.org/evp_bytestokey/-/evp_bytestokey-1.0.3.tgz
Source143: https://registry.npmjs.org/elliptic/-/elliptic-6.4.0.tgz
Source144: https://registry.npmjs.org/bn.js/-/bn.js-4.11.8.tgz
Source145: https://registry.npmjs.org/cipher-base/-/cipher-base-1.0.4.tgz
Source146: https://registry.npmjs.org/ripemd160/-/ripemd160-2.0.2.tgz
Source147: https://registry.npmjs.org/browserify-rsa/-/browserify-rsa-4.0.1.tgz
Source148: https://registry.npmjs.org/md5.js/-/md5.js-1.3.4.tgz
Source149: https://registry.npmjs.org/sha.js/-/sha.js-2.4.11.tgz
Source150: https://registry.npmjs.org/parse-asn1/-/parse-asn1-5.1.1.tgz
Source151: https://registry.npmjs.org/miller-rabin/-/miller-rabin-4.0.1.tgz
Source152: https://registry.npmjs.org/micromatch/-/micromatch-3.1.10.tgz
Source153: https://registry.npmjs.org/remove-trailing-separator/-/remove-trailing-separator-1.1.0.tgz
Source154: https://registry.npmjs.org/path-dirname/-/path-dirname-1.0.2.tgz
Source155: https://registry.npmjs.org/is-extglob/-/is-extglob-2.1.1.tgz
Source156: https://registry.npmjs.org/binary-extensions/-/binary-extensions-1.11.0.tgz
Source157: https://registry.npmjs.org/set-immediate-shim/-/set-immediate-shim-1.0.1.tgz
Source158: https://registry.npmjs.org/minimatch/-/minimatch-3.0.4.tgz
Source159: https://registry.npmjs.org/nan/-/nan-2.10.0.tgz
Source160: https://registry.npmjs.org/arr-flatten/-/arr-flatten-1.1.0.tgz
Source161: https://registry.npmjs.org/extend-shallow/-/extend-shallow-2.0.1.tgz
Source162: https://registry.npmjs.org/fill-range/-/fill-range-4.0.0.tgz
Source163: https://registry.npmjs.org/node-pre-gyp/-/node-pre-gyp-0.10.0.tgz
Source164: https://registry.npmjs.org/repeat-element/-/repeat-element-1.1.2.tgz
Source165: https://registry.npmjs.org/isobject/-/isobject-3.0.1.tgz
Source166: https://registry.npmjs.org/array-unique/-/array-unique-0.3.2.tgz
Source167: https://registry.npmjs.org/snapdragon-node/-/snapdragon-node-2.1.1.tgz
Source168: https://registry.npmjs.org/snapdragon/-/snapdragon-0.8.2.tgz
Source169: https://registry.npmjs.org/split-string/-/split-string-3.1.0.tgz
Source170: https://registry.npmjs.org/to-regex/-/to-regex-3.0.2.tgz
Source171: https://registry.npmjs.org/load-json-file/-/load-json-file-2.0.0.tgz
Source172: https://registry.npmjs.org/locate-path/-/locate-path-2.0.0.tgz
Source173: https://registry.npmjs.org/path-type/-/path-type-2.0.0.tgz
Source174: https://registry.npmjs.org/is-stream/-/is-stream-1.1.0.tgz
Source175: https://registry.npmjs.org/cross-spawn/-/cross-spawn-5.1.0.tgz
Source176: https://registry.npmjs.org/get-stream/-/get-stream-3.0.0.tgz
Source177: https://registry.npmjs.org/pako/-/pako-1.0.6.tgz
Source178: https://registry.npmjs.org/npm-run-path/-/npm-run-path-2.0.2.tgz
Source179: https://registry.npmjs.org/p-finally/-/p-finally-1.0.0.tgz
Source180: https://registry.npmjs.org/mimic-fn/-/mimic-fn-1.2.0.tgz
Source181: https://registry.npmjs.org/strip-eof/-/strip-eof-1.0.0.tgz
Source182: https://registry.npmjs.org/signal-exit/-/signal-exit-3.0.2.tgz
Source183: https://registry.npmjs.org/normalize-package-data/-/normalize-package-data-2.4.0.tgz
Source184: https://registry.npmjs.org/invert-kv/-/invert-kv-1.0.0.tgz
Source185: https://registry.npmjs.org/code-point-at/-/code-point-at-1.1.0.tgz
Source186: https://registry.npmjs.org/is-fullwidth-code-point/-/is-fullwidth-code-point-1.0.0.tgz
Source187: https://registry.npmjs.org/camelcase/-/camelcase-1.2.1.tgz
Source188: https://registry.npmjs.org/cliui/-/cliui-2.1.0.tgz
Source189: https://registry.npmjs.org/builtin-status-codes/-/builtin-status-codes-3.0.0.tgz
Source190: https://registry.npmjs.org/window-size/-/window-size-0.1.0.tgz
Source191: https://registry.npmjs.org/ansi-regex/-/ansi-regex-2.1.1.tgz
Source192: https://registry.npmjs.org/ansi-regex/-/ansi-regex-3.0.0.tgz
Source193: https://registry.npmjs.org/des.js/-/des.js-1.0.0.tgz
Source194: https://registry.npmjs.org/buffer-xor/-/buffer-xor-1.0.3.tgz
Source195: https://registry.npmjs.org/hmac-drbg/-/hmac-drbg-1.0.1.tgz
Source196: https://registry.npmjs.org/brorand/-/brorand-1.1.0.tgz
Source197: https://registry.npmjs.org/minimalistic-assert/-/minimalistic-assert-1.0.1.tgz
Source198: https://registry.npmjs.org/minimalistic-crypto-utils/-/minimalistic-crypto-utils-1.0.1.tgz
Source199: https://registry.npmjs.org/hash-base/-/hash-base-3.0.4.tgz
Source200: https://registry.npmjs.org/hash.js/-/hash.js-1.1.3.tgz
Source201: https://registry.npmjs.org/asn1.js/-/asn1.js-4.10.1.tgz
Source202: https://registry.npmjs.org/arr-diff/-/arr-diff-4.0.0.tgz
Source203: https://registry.npmjs.org/fragment-cache/-/fragment-cache-0.2.1.tgz
Source204: https://registry.npmjs.org/extglob/-/extglob-2.0.4.tgz
Source205: https://registry.npmjs.org/kind-of/-/kind-of-6.0.2.tgz
Source206: https://registry.npmjs.org/nanomatch/-/nanomatch-1.2.9.tgz
Source207: https://registry.npmjs.org/object.pick/-/object.pick-1.3.0.tgz
Source208: https://registry.npmjs.org/regex-not/-/regex-not-1.0.2.tgz
Source209: https://registry.npmjs.org/brace-expansion/-/brace-expansion-1.1.11.tgz
Source210: https://registry.npmjs.org/is-glob/-/is-glob-3.1.0.tgz
Source211: https://registry.npmjs.org/is-number/-/is-number-3.0.0.tgz
Source212: https://registry.npmjs.org/repeat-string/-/repeat-string-1.6.1.tgz
Source213: https://registry.npmjs.org/to-regex-range/-/to-regex-range-2.1.1.tgz
Source214: https://registry.npmjs.org/detect-libc/-/detect-libc-1.0.3.tgz
Source215: https://registry.npmjs.org/nopt/-/nopt-4.0.1.tgz
Source216: https://registry.npmjs.org/npm-packlist/-/npm-packlist-1.1.10.tgz
Source217: https://registry.npmjs.org/npmlog/-/npmlog-4.1.2.tgz
Source218: https://registry.npmjs.org/needle/-/needle-2.2.1.tgz
Source219: https://registry.npmjs.org/rc/-/rc-1.2.8.tgz
Source220: https://registry.npmjs.org/rimraf/-/rimraf-2.6.2.tgz
Source221: https://registry.npmjs.org/semver/-/semver-5.5.0.tgz
Source222: https://registry.npmjs.org/tar/-/tar-4.4.4.tgz
Source223: https://registry.npmjs.org/define-property/-/define-property-1.0.0.tgz
Source224: https://registry.npmjs.org/snapdragon-util/-/snapdragon-util-3.0.1.tgz
Source225: https://registry.npmjs.org/define-property/-/define-property-0.2.5.tgz
Source226: https://registry.npmjs.org/debug/-/debug-2.6.9.tgz
Source227: https://registry.npmjs.org/base/-/base-0.11.2.tgz
Source228: https://registry.npmjs.org/map-cache/-/map-cache-0.2.2.tgz
Source229: https://registry.npmjs.org/source-map-resolve/-/source-map-resolve-0.5.2.tgz
Source230: https://registry.npmjs.org/use/-/use-3.1.0.tgz
Source231: https://registry.npmjs.org/define-property/-/define-property-2.0.2.tgz
Source232: https://registry.npmjs.org/extend-shallow/-/extend-shallow-3.0.2.tgz
Source233: https://registry.npmjs.org/safe-regex/-/safe-regex-1.1.0.tgz
Source234: https://registry.npmjs.org/strip-bom/-/strip-bom-3.0.0.tgz
Source235: https://registry.npmjs.org/parse-json/-/parse-json-2.2.0.tgz
Source236: https://registry.npmjs.org/pify/-/pify-2.3.0.tgz
Source237: https://registry.npmjs.org/path-exists/-/path-exists-3.0.0.tgz
Source238: https://registry.npmjs.org/p-locate/-/p-locate-2.0.0.tgz
Source239: https://registry.npmjs.org/shebang-command/-/shebang-command-1.2.0.tgz
Source240: https://registry.npmjs.org/path-key/-/path-key-2.0.1.tgz
Source241: https://registry.npmjs.org/which/-/which-1.3.1.tgz
Source242: https://registry.npmjs.org/lru-cache/-/lru-cache-4.1.3.tgz
Source243: https://registry.npmjs.org/hosted-git-info/-/hosted-git-info-2.6.0.tgz
Source244: https://registry.npmjs.org/is-builtin-module/-/is-builtin-module-1.0.0.tgz
Source245: https://registry.npmjs.org/validate-npm-package-license/-/validate-npm-package-license-3.0.3.tgz
Source246: https://registry.npmjs.org/center-align/-/center-align-0.1.3.tgz
Source247: https://registry.npmjs.org/number-is-nan/-/number-is-nan-1.0.1.tgz
Source248: https://registry.npmjs.org/right-align/-/right-align-0.1.3.tgz
Source249: https://registry.npmjs.org/wordwrap/-/wordwrap-0.0.2.tgz
Source250: https://registry.npmjs.org/expand-brackets/-/expand-brackets-2.1.4.tgz
Source251: https://registry.npmjs.org/is-extendable/-/is-extendable-0.1.1.tgz
Source252: https://registry.npmjs.org/is-windows/-/is-windows-1.0.2.tgz
Source253: https://registry.npmjs.org/is-odd/-/is-odd-2.0.0.tgz
Source254: https://registry.npmjs.org/concat-map/-/concat-map-0.0.1.tgz
Source255: https://registry.npmjs.org/balanced-match/-/balanced-match-1.0.0.tgz
Source256: https://registry.npmjs.org/abbrev/-/abbrev-1.1.1.tgz
Source257: https://registry.npmjs.org/osenv/-/osenv-0.1.5.tgz
Source258: https://registry.npmjs.org/ignore-walk/-/ignore-walk-3.0.1.tgz
Source259: https://registry.npmjs.org/npm-bundled/-/npm-bundled-1.0.3.tgz
Source260: https://registry.npmjs.org/console-control-strings/-/console-control-strings-1.1.0.tgz
Source261: https://registry.npmjs.org/are-we-there-yet/-/are-we-there-yet-1.1.5.tgz
Source262: https://registry.npmjs.org/gauge/-/gauge-2.7.4.tgz
Source263: https://registry.npmjs.org/iconv-lite/-/iconv-lite-0.4.23.tgz
Source264: https://registry.npmjs.org/ini/-/ini-1.3.5.tgz
Source265: https://registry.npmjs.org/deep-extend/-/deep-extend-0.6.0.tgz
Source266: https://registry.npmjs.org/sax/-/sax-1.2.4.tgz
Source267: https://registry.npmjs.org/minimist/-/minimist-1.2.0.tgz
Source268: https://registry.npmjs.org/chownr/-/chownr-1.0.1.tgz
Source269: https://registry.npmjs.org/glob/-/glob-7.1.2.tgz
Source270: https://registry.npmjs.org/fs-minipass/-/fs-minipass-1.2.5.tgz
Source271: https://registry.npmjs.org/minizlib/-/minizlib-1.1.0.tgz
Source272: https://registry.npmjs.org/strip-json-comments/-/strip-json-comments-2.0.1.tgz
Source273: https://registry.npmjs.org/minipass/-/minipass-2.3.3.tgz
Source274: https://registry.npmjs.org/yallist/-/yallist-3.0.2.tgz
Source275: https://registry.npmjs.org/is-descriptor/-/is-descriptor-1.0.2.tgz
Source276: https://registry.npmjs.org/kind-of/-/kind-of-3.2.2.tgz
Source277: https://registry.npmjs.org/is-descriptor/-/is-descriptor-0.1.6.tgz
Source278: https://registry.npmjs.org/ms/-/ms-2.0.0.tgz
Source279: https://registry.npmjs.org/component-emitter/-/component-emitter-1.2.1.tgz
Source280: https://registry.npmjs.org/class-utils/-/class-utils-0.3.6.tgz
Source281: https://registry.npmjs.org/cache-base/-/cache-base-1.0.1.tgz
Source282: https://registry.npmjs.org/pascalcase/-/pascalcase-0.1.1.tgz
Source283: https://registry.npmjs.org/atob/-/atob-2.1.1.tgz
Source284: https://registry.npmjs.org/mixin-deep/-/mixin-deep-1.3.1.tgz
Source285: https://registry.npmjs.org/decode-uri-component/-/decode-uri-component-0.2.0.tgz
Source286: https://registry.npmjs.org/resolve-url/-/resolve-url-0.2.1.tgz
Source287: https://registry.npmjs.org/source-map-url/-/source-map-url-0.4.0.tgz
Source288: https://registry.npmjs.org/urix/-/urix-0.1.0.tgz
Source289: https://registry.npmjs.org/assign-symbols/-/assign-symbols-1.0.0.tgz
Source290: https://registry.npmjs.org/is-extendable/-/is-extendable-1.0.1.tgz
Source291: https://registry.npmjs.org/ret/-/ret-0.1.15.tgz
Source292: https://registry.npmjs.org/p-limit/-/p-limit-1.2.0.tgz
Source293: https://registry.npmjs.org/shebang-regex/-/shebang-regex-1.0.0.tgz
Source294: https://registry.npmjs.org/error-ex/-/error-ex-1.3.1.tgz
Source295: https://registry.npmjs.org/isexe/-/isexe-2.0.0.tgz
Source296: https://registry.npmjs.org/pseudomap/-/pseudomap-1.0.2.tgz
Source297: https://registry.npmjs.org/builtin-modules/-/builtin-modules-1.1.1.tgz
Source298: https://registry.npmjs.org/yallist/-/yallist-2.1.2.tgz
Source299: https://registry.npmjs.org/spdx-correct/-/spdx-correct-3.0.0.tgz
Source300: https://registry.npmjs.org/spdx-expression-parse/-/spdx-expression-parse-3.0.0.tgz
Source301: https://registry.npmjs.org/align-text/-/align-text-0.1.4.tgz
Source302: https://registry.npmjs.org/lazy-cache/-/lazy-cache-1.0.4.tgz
Source303: https://registry.npmjs.org/posix-character-classes/-/posix-character-classes-0.1.1.tgz
Source304: https://registry.npmjs.org/is-number/-/is-number-4.0.0.tgz
Source305: https://registry.npmjs.org/os-tmpdir/-/os-tmpdir-1.0.2.tgz
Source306: https://registry.npmjs.org/os-homedir/-/os-homedir-1.0.2.tgz
Source307: https://registry.npmjs.org/delegates/-/delegates-1.0.0.tgz
Source308: https://registry.npmjs.org/aproba/-/aproba-1.2.0.tgz
Source309: https://registry.npmjs.org/has-unicode/-/has-unicode-2.0.1.tgz
Source310: https://registry.npmjs.org/safer-buffer/-/safer-buffer-2.1.2.tgz
Source311: https://registry.npmjs.org/wide-align/-/wide-align-1.1.3.tgz
Source312: https://registry.npmjs.org/fs.realpath/-/fs.realpath-1.0.0.tgz
Source313: https://registry.npmjs.org/inflight/-/inflight-1.0.6.tgz
Source314: https://registry.npmjs.org/once/-/once-1.4.0.tgz
Source315: https://registry.npmjs.org/is-accessor-descriptor/-/is-accessor-descriptor-1.0.0.tgz
Source316: https://registry.npmjs.org/is-accessor-descriptor/-/is-accessor-descriptor-0.1.6.tgz
Source317: https://registry.npmjs.org/is-buffer/-/is-buffer-1.1.6.tgz
Source318: https://registry.npmjs.org/is-data-descriptor/-/is-data-descriptor-1.0.0.tgz
Source319: https://registry.npmjs.org/kind-of/-/kind-of-5.1.0.tgz
Source320: https://registry.npmjs.org/is-data-descriptor/-/is-data-descriptor-0.1.4.tgz
Source321: https://registry.npmjs.org/arr-union/-/arr-union-3.1.0.tgz
Source322: https://registry.npmjs.org/static-extend/-/static-extend-0.1.2.tgz
Source323: https://registry.npmjs.org/collection-visit/-/collection-visit-1.0.0.tgz
Source324: https://registry.npmjs.org/has-value/-/has-value-1.0.0.tgz
Source325: https://registry.npmjs.org/to-object-path/-/to-object-path-0.3.0.tgz
Source326: https://registry.npmjs.org/union-value/-/union-value-1.0.0.tgz
Source327: https://registry.npmjs.org/unset-value/-/unset-value-1.0.0.tgz
Source328: https://registry.npmjs.org/set-value/-/set-value-2.0.0.tgz
Source329: https://registry.npmjs.org/for-in/-/for-in-1.0.2.tgz
Source330: https://registry.npmjs.org/is-plain-object/-/is-plain-object-2.0.4.tgz
Source331: https://registry.npmjs.org/p-try/-/p-try-1.0.0.tgz
Source332: https://registry.npmjs.org/is-arrayish/-/is-arrayish-0.2.1.tgz
Source333: https://registry.npmjs.org/spdx-license-ids/-/spdx-license-ids-3.0.0.tgz
Source334: https://registry.npmjs.org/spdx-exceptions/-/spdx-exceptions-2.1.0.tgz
Source335: https://registry.npmjs.org/longest/-/longest-1.0.1.tgz
Source336: https://registry.npmjs.org/wrappy/-/wrappy-1.0.2.tgz
Source337: https://registry.npmjs.org/object-copy/-/object-copy-0.1.0.tgz
Source338: https://registry.npmjs.org/map-visit/-/map-visit-1.0.0.tgz
Source339: https://registry.npmjs.org/object-visit/-/object-visit-1.0.1.tgz
Source340: https://registry.npmjs.org/get-value/-/get-value-2.0.6.tgz
Source341: https://registry.npmjs.org/has-values/-/has-values-1.0.0.tgz
Source342: https://registry.npmjs.org/set-value/-/set-value-0.4.3.tgz
Source343: https://registry.npmjs.org/has-value/-/has-value-0.3.1.tgz
Source344: https://registry.npmjs.org/copy-descriptor/-/copy-descriptor-0.1.1.tgz
Source345: https://registry.npmjs.org/kind-of/-/kind-of-4.0.0.tgz
Source346: https://registry.npmjs.org/has-values/-/has-values-0.1.4.tgz
Source347: https://registry.npmjs.org/isobject/-/isobject-2.1.0.tgz
Source348: %{npm_name}-%{version}-registry.npmjs.org.tgz
BuildRequires: nodejs-packaging
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: npm(%{npm_name}) = %{version}
Provides: bundled(npm(abbrev)) = 1.1.1
Provides: bundled(npm(acorn)) = 4.0.13
Provides: bundled(npm(acorn)) = 5.6.2
Provides: bundled(npm(acorn-dynamic-import)) = 2.0.2
Provides: bundled(npm(ajv)) = 6.5.0
Provides: bundled(npm(ajv-keywords)) = 3.2.0
Provides: bundled(npm(align-text)) = 0.1.4
Provides: bundled(npm(ansi-regex)) = 3.0.0
Provides: bundled(npm(ansi-regex)) = 2.1.1
Provides: bundled(npm(anymatch)) = 2.0.0
Provides: bundled(npm(aproba)) = 1.2.0
Provides: bundled(npm(are-we-there-yet)) = 1.1.5
Provides: bundled(npm(arr-diff)) = 4.0.0
Provides: bundled(npm(arr-flatten)) = 1.1.0
Provides: bundled(npm(arr-union)) = 3.1.0
Provides: bundled(npm(array-unique)) = 0.3.2
Provides: bundled(npm(asn1.js)) = 4.10.1
Provides: bundled(npm(assert)) = 1.4.1
Provides: bundled(npm(assign-symbols)) = 1.0.0
Provides: bundled(npm(async)) = 2.6.1
Provides: bundled(npm(async-each)) = 1.0.1
Provides: bundled(npm(atob)) = 2.1.1
Provides: bundled(npm(balanced-match)) = 1.0.0
Provides: bundled(npm(base)) = 0.11.2
Provides: bundled(npm(base64-js)) = 1.3.0
Provides: bundled(npm(big.js)) = 3.2.0
Provides: bundled(npm(binary-extensions)) = 1.11.0
Provides: bundled(npm(bn.js)) = 4.11.8
Provides: bundled(npm(brace-expansion)) = 1.1.11
Provides: bundled(npm(braces)) = 2.3.2
Provides: bundled(npm(brorand)) = 1.1.0
Provides: bundled(npm(browserify-aes)) = 1.2.0
Provides: bundled(npm(browserify-cipher)) = 1.0.1
Provides: bundled(npm(browserify-des)) = 1.0.1
Provides: bundled(npm(browserify-rsa)) = 4.0.1
Provides: bundled(npm(browserify-sign)) = 4.0.4
Provides: bundled(npm(browserify-zlib)) = 0.2.0
Provides: bundled(npm(buffer)) = 4.9.1
Provides: bundled(npm(buffer-xor)) = 1.0.3
Provides: bundled(npm(builtin-modules)) = 1.1.1
Provides: bundled(npm(builtin-status-codes)) = 3.0.0
Provides: bundled(npm(cache-base)) = 1.0.1
Provides: bundled(npm(camelcase)) = 1.2.1
Provides: bundled(npm(camelcase)) = 4.1.0
Provides: bundled(npm(center-align)) = 0.1.3
Provides: bundled(npm(chokidar)) = 2.0.3
Provides: bundled(npm(chownr)) = 1.0.1
Provides: bundled(npm(cipher-base)) = 1.0.4
Provides: bundled(npm(class-utils)) = 0.3.6
Provides: bundled(npm(cliui)) = 2.1.0
Provides: bundled(npm(cliui)) = 3.2.0
Provides: bundled(npm(code-point-at)) = 1.1.0
Provides: bundled(npm(collection-visit)) = 1.0.0
Provides: bundled(npm(component-emitter)) = 1.2.1
Provides: bundled(npm(concat-map)) = 0.0.1
Provides: bundled(npm(console-browserify)) = 1.1.0
Provides: bundled(npm(console-control-strings)) = 1.1.0
Provides: bundled(npm(constants-browserify)) = 1.0.0
Provides: bundled(npm(copy-descriptor)) = 0.1.1
Provides: bundled(npm(core-util-is)) = 1.0.2
Provides: bundled(npm(create-ecdh)) = 4.0.3
Provides: bundled(npm(create-hash)) = 1.2.0
Provides: bundled(npm(create-hmac)) = 1.1.7
Provides: bundled(npm(cross-spawn)) = 5.1.0
Provides: bundled(npm(crypto-browserify)) = 3.12.0
Provides: bundled(npm(d)) = 1.0.0
Provides: bundled(npm(date-now)) = 0.1.4
Provides: bundled(npm(debug)) = 2.6.9
Provides: bundled(npm(decamelize)) = 1.2.0
Provides: bundled(npm(decode-uri-component)) = 0.2.0
Provides: bundled(npm(deep-extend)) = 0.6.0
Provides: bundled(npm(define-property)) = 2.0.2
Provides: bundled(npm(define-property)) = 1.0.0
Provides: bundled(npm(define-property)) = 0.2.5
Provides: bundled(npm(delegates)) = 1.0.0
Provides: bundled(npm(des.js)) = 1.0.0
Provides: bundled(npm(detect-libc)) = 1.0.3
Provides: bundled(npm(diffie-hellman)) = 5.0.3
Provides: bundled(npm(domain-browser)) = 1.2.0
Provides: bundled(npm(elliptic)) = 6.4.0
Provides: bundled(npm(emojis-list)) = 2.1.0
Provides: bundled(npm(enhanced-resolve)) = 3.4.1
Provides: bundled(npm(errno)) = 0.1.7
Provides: bundled(npm(error-ex)) = 1.3.1
Provides: bundled(npm(es5-ext)) = 0.10.45
Provides: bundled(npm(es6-iterator)) = 2.0.3
Provides: bundled(npm(es6-map)) = 0.1.5
Provides: bundled(npm(es6-set)) = 0.1.5
Provides: bundled(npm(es6-symbol)) = 3.1.1
Provides: bundled(npm(es6-weak-map)) = 2.0.2
Provides: bundled(npm(escope)) = 3.6.0
Provides: bundled(npm(esrecurse)) = 4.2.1
Provides: bundled(npm(estraverse)) = 4.2.0
Provides: bundled(npm(event-emitter)) = 0.3.5
Provides: bundled(npm(events)) = 1.1.1
Provides: bundled(npm(evp_bytestokey)) = 1.0.3
Provides: bundled(npm(execa)) = 0.7.0
Provides: bundled(npm(expand-brackets)) = 2.1.4
Provides: bundled(npm(extend-shallow)) = 3.0.2
Provides: bundled(npm(extend-shallow)) = 2.0.1
Provides: bundled(npm(extglob)) = 2.0.4
Provides: bundled(npm(fast-deep-equal)) = 2.0.1
Provides: bundled(npm(fast-json-stable-stringify)) = 2.0.0
Provides: bundled(npm(fill-range)) = 4.0.0
Provides: bundled(npm(find-up)) = 2.1.0
Provides: bundled(npm(for-in)) = 1.0.2
Provides: bundled(npm(fragment-cache)) = 0.2.1
Provides: bundled(npm(fs-minipass)) = 1.2.5
Provides: bundled(npm(fs.realpath)) = 1.0.0
Provides: bundled(npm(fsevents)) = 1.2.4
Provides: bundled(npm(gauge)) = 2.7.4
Provides: bundled(npm(get-caller-file)) = 1.0.2
Provides: bundled(npm(get-stream)) = 3.0.0
Provides: bundled(npm(get-value)) = 2.0.6
Provides: bundled(npm(glob)) = 7.1.2
Provides: bundled(npm(glob-parent)) = 3.1.0
Provides: bundled(npm(graceful-fs)) = 4.1.11
Provides: bundled(npm(has-flag)) = 2.0.0
Provides: bundled(npm(has-unicode)) = 2.0.1
Provides: bundled(npm(has-value)) = 1.0.0
Provides: bundled(npm(has-value)) = 0.3.1
Provides: bundled(npm(has-values)) = 0.1.4
Provides: bundled(npm(has-values)) = 1.0.0
Provides: bundled(npm(hash-base)) = 3.0.4
Provides: bundled(npm(hash.js)) = 1.1.3
Provides: bundled(npm(hmac-drbg)) = 1.0.1
Provides: bundled(npm(hosted-git-info)) = 2.6.0
Provides: bundled(npm(https-browserify)) = 1.0.0
Provides: bundled(npm(iconv-lite)) = 0.4.23
Provides: bundled(npm(ieee754)) = 1.1.11
Provides: bundled(npm(ignore-walk)) = 3.0.1
Provides: bundled(npm(indexof)) = 0.0.1
Provides: bundled(npm(inflight)) = 1.0.6
Provides: bundled(npm(inherits)) = 2.0.1
Provides: bundled(npm(inherits)) = 2.0.3
Provides: bundled(npm(ini)) = 1.3.5
Provides: bundled(npm(interpret)) = 1.1.0
Provides: bundled(npm(invert-kv)) = 1.0.0
Provides: bundled(npm(is-accessor-descriptor)) = 0.1.6
Provides: bundled(npm(is-accessor-descriptor)) = 1.0.0
Provides: bundled(npm(is-arrayish)) = 0.2.1
Provides: bundled(npm(is-binary-path)) = 1.0.1
Provides: bundled(npm(is-buffer)) = 1.1.6
Provides: bundled(npm(is-builtin-module)) = 1.0.0
Provides: bundled(npm(is-data-descriptor)) = 1.0.0
Provides: bundled(npm(is-data-descriptor)) = 0.1.4
Provides: bundled(npm(is-descriptor)) = 0.1.6
Provides: bundled(npm(is-descriptor)) = 1.0.2
Provides: bundled(npm(is-extendable)) = 1.0.1
Provides: bundled(npm(is-extendable)) = 0.1.1
Provides: bundled(npm(is-extglob)) = 2.1.1
Provides: bundled(npm(is-fullwidth-code-point)) = 2.0.0
Provides: bundled(npm(is-fullwidth-code-point)) = 1.0.0
Provides: bundled(npm(is-glob)) = 4.0.0
Provides: bundled(npm(is-glob)) = 3.1.0
Provides: bundled(npm(is-number)) = 4.0.0
Provides: bundled(npm(is-number)) = 3.0.0
Provides: bundled(npm(is-odd)) = 2.0.0
Provides: bundled(npm(is-plain-object)) = 2.0.4
Provides: bundled(npm(is-stream)) = 1.1.0
Provides: bundled(npm(is-windows)) = 1.0.2
Provides: bundled(npm(isarray)) = 1.0.0
Provides: bundled(npm(isexe)) = 2.0.0
Provides: bundled(npm(isobject)) = 2.1.0
Provides: bundled(npm(isobject)) = 3.0.1
Provides: bundled(npm(json-loader)) = 0.5.7
Provides: bundled(npm(json-schema-traverse)) = 0.3.1
Provides: bundled(npm(json5)) = 0.5.1
Provides: bundled(npm(kind-of)) = 5.1.0
Provides: bundled(npm(kind-of)) = 3.2.2
Provides: bundled(npm(kind-of)) = 6.0.2
Provides: bundled(npm(kind-of)) = 4.0.0
Provides: bundled(npm(lazy-cache)) = 1.0.4
Provides: bundled(npm(lcid)) = 1.0.0
Provides: bundled(npm(load-json-file)) = 2.0.0
Provides: bundled(npm(loader-runner)) = 2.3.0
Provides: bundled(npm(loader-utils)) = 1.1.0
Provides: bundled(npm(locate-path)) = 2.0.0
Provides: bundled(npm(lodash)) = 4.17.10
Provides: bundled(npm(longest)) = 1.0.1
Provides: bundled(npm(lru-cache)) = 4.1.3
Provides: bundled(npm(map-cache)) = 0.2.2
Provides: bundled(npm(map-visit)) = 1.0.0
Provides: bundled(npm(md5.js)) = 1.3.4
Provides: bundled(npm(mem)) = 1.1.0
Provides: bundled(npm(memory-fs)) = 0.4.1
Provides: bundled(npm(micromatch)) = 3.1.10
Provides: bundled(npm(miller-rabin)) = 4.0.1
Provides: bundled(npm(mimic-fn)) = 1.2.0
Provides: bundled(npm(minimalistic-assert)) = 1.0.1
Provides: bundled(npm(minimalistic-crypto-utils)) = 1.0.1
Provides: bundled(npm(minimatch)) = 3.0.4
Provides: bundled(npm(minimist)) = 0.0.8
Provides: bundled(npm(minimist)) = 1.2.0
Provides: bundled(npm(minipass)) = 2.3.3
Provides: bundled(npm(minizlib)) = 1.1.0
Provides: bundled(npm(mixin-deep)) = 1.3.1
Provides: bundled(npm(mkdirp)) = 0.5.1
Provides: bundled(npm(ms)) = 2.0.0
Provides: bundled(npm(nan)) = 2.10.0
Provides: bundled(npm(nanomatch)) = 1.2.9
Provides: bundled(npm(needle)) = 2.2.1
Provides: bundled(npm(neo-async)) = 2.5.1
Provides: bundled(npm(next-tick)) = 1.0.0
Provides: bundled(npm(node-libs-browser)) = 2.1.0
Provides: bundled(npm(node-pre-gyp)) = 0.10.0
Provides: bundled(npm(nopt)) = 4.0.1
Provides: bundled(npm(normalize-package-data)) = 2.4.0
Provides: bundled(npm(normalize-path)) = 2.1.1
Provides: bundled(npm(npm-bundled)) = 1.0.3
Provides: bundled(npm(npm-packlist)) = 1.1.10
Provides: bundled(npm(npm-run-path)) = 2.0.2
Provides: bundled(npm(npmlog)) = 4.1.2
Provides: bundled(npm(number-is-nan)) = 1.0.1
Provides: bundled(npm(object-assign)) = 4.1.1
Provides: bundled(npm(object-copy)) = 0.1.0
Provides: bundled(npm(object-visit)) = 1.0.1
Provides: bundled(npm(object.pick)) = 1.3.0
Provides: bundled(npm(once)) = 1.4.0
Provides: bundled(npm(os-browserify)) = 0.3.0
Provides: bundled(npm(os-homedir)) = 1.0.2
Provides: bundled(npm(os-locale)) = 2.1.0
Provides: bundled(npm(os-tmpdir)) = 1.0.2
Provides: bundled(npm(osenv)) = 0.1.5
Provides: bundled(npm(p-finally)) = 1.0.0
Provides: bundled(npm(p-limit)) = 1.2.0
Provides: bundled(npm(p-locate)) = 2.0.0
Provides: bundled(npm(p-try)) = 1.0.0
Provides: bundled(npm(pako)) = 1.0.6
Provides: bundled(npm(parse-asn1)) = 5.1.1
Provides: bundled(npm(parse-json)) = 2.2.0
Provides: bundled(npm(pascalcase)) = 0.1.1
Provides: bundled(npm(path-browserify)) = 0.0.0
Provides: bundled(npm(path-dirname)) = 1.0.2
Provides: bundled(npm(path-exists)) = 3.0.0
Provides: bundled(npm(path-is-absolute)) = 1.0.1
Provides: bundled(npm(path-key)) = 2.0.1
Provides: bundled(npm(path-type)) = 2.0.0
Provides: bundled(npm(pbkdf2)) = 3.0.16
Provides: bundled(npm(pify)) = 2.3.0
Provides: bundled(npm(posix-character-classes)) = 0.1.1
Provides: bundled(npm(process)) = 0.11.10
Provides: bundled(npm(process-nextick-args)) = 2.0.0
Provides: bundled(npm(prr)) = 1.0.1
Provides: bundled(npm(pseudomap)) = 1.0.2
Provides: bundled(npm(public-encrypt)) = 4.0.2
Provides: bundled(npm(punycode)) = 2.1.1
Provides: bundled(npm(punycode)) = 1.4.1
Provides: bundled(npm(punycode)) = 1.3.2
Provides: bundled(npm(querystring)) = 0.2.0
Provides: bundled(npm(querystring-es3)) = 0.2.1
Provides: bundled(npm(randombytes)) = 2.0.6
Provides: bundled(npm(randomfill)) = 1.0.4
Provides: bundled(npm(rc)) = 1.2.8
Provides: bundled(npm(read-pkg)) = 2.0.0
Provides: bundled(npm(read-pkg-up)) = 2.0.0
Provides: bundled(npm(readable-stream)) = 2.3.6
Provides: bundled(npm(readdirp)) = 2.1.0
Provides: bundled(npm(regex-not)) = 1.0.2
Provides: bundled(npm(remove-trailing-separator)) = 1.1.0
Provides: bundled(npm(repeat-element)) = 1.1.2
Provides: bundled(npm(repeat-string)) = 1.6.1
Provides: bundled(npm(require-directory)) = 2.1.1
Provides: bundled(npm(require-main-filename)) = 1.0.1
Provides: bundled(npm(resolve-url)) = 0.2.1
Provides: bundled(npm(ret)) = 0.1.15
Provides: bundled(npm(right-align)) = 0.1.3
Provides: bundled(npm(rimraf)) = 2.6.2
Provides: bundled(npm(ripemd160)) = 2.0.2
Provides: bundled(npm(safe-buffer)) = 5.1.2
Provides: bundled(npm(safe-regex)) = 1.1.0
Provides: bundled(npm(safer-buffer)) = 2.1.2
Provides: bundled(npm(sax)) = 1.2.4
Provides: bundled(npm(semver)) = 5.5.0
Provides: bundled(npm(set-blocking)) = 2.0.0
Provides: bundled(npm(set-immediate-shim)) = 1.0.1
Provides: bundled(npm(set-value)) = 2.0.0
Provides: bundled(npm(set-value)) = 0.4.3
Provides: bundled(npm(setimmediate)) = 1.0.5
Provides: bundled(npm(sha.js)) = 2.4.11
Provides: bundled(npm(shebang-command)) = 1.2.0
Provides: bundled(npm(shebang-regex)) = 1.0.0
Provides: bundled(npm(signal-exit)) = 3.0.2
Provides: bundled(npm(snapdragon)) = 0.8.2
Provides: bundled(npm(snapdragon-node)) = 2.1.1
Provides: bundled(npm(snapdragon-util)) = 3.0.1
Provides: bundled(npm(source-list-map)) = 2.0.0
Provides: bundled(npm(source-map)) = 0.6.1
Provides: bundled(npm(source-map)) = 0.5.7
Provides: bundled(npm(source-map-resolve)) = 0.5.2
Provides: bundled(npm(source-map-url)) = 0.4.0
Provides: bundled(npm(spdx-correct)) = 3.0.0
Provides: bundled(npm(spdx-exceptions)) = 2.1.0
Provides: bundled(npm(spdx-expression-parse)) = 3.0.0
Provides: bundled(npm(spdx-license-ids)) = 3.0.0
Provides: bundled(npm(split-string)) = 3.1.0
Provides: bundled(npm(static-extend)) = 0.1.2
Provides: bundled(npm(stream-browserify)) = 2.0.1
Provides: bundled(npm(stream-http)) = 2.8.3
Provides: bundled(npm(string_decoder)) = 1.1.1
Provides: bundled(npm(string-width)) = 2.1.1
Provides: bundled(npm(string-width)) = 1.0.2
Provides: bundled(npm(strip-ansi)) = 3.0.1
Provides: bundled(npm(strip-ansi)) = 4.0.0
Provides: bundled(npm(strip-bom)) = 3.0.0
Provides: bundled(npm(strip-eof)) = 1.0.0
Provides: bundled(npm(strip-json-comments)) = 2.0.1
Provides: bundled(npm(supports-color)) = 4.5.0
Provides: bundled(npm(tapable)) = 0.2.8
Provides: bundled(npm(tar)) = 4.4.4
Provides: bundled(npm(timers-browserify)) = 2.0.10
Provides: bundled(npm(to-arraybuffer)) = 1.0.1
Provides: bundled(npm(to-object-path)) = 0.3.0
Provides: bundled(npm(to-regex)) = 3.0.2
Provides: bundled(npm(to-regex-range)) = 2.1.1
Provides: bundled(npm(tty-browserify)) = 0.0.0
Provides: bundled(npm(uglify-js)) = 2.8.29
Provides: bundled(npm(uglify-to-browserify)) = 1.0.2
Provides: bundled(npm(uglifyjs-webpack-plugin)) = 0.4.6
Provides: bundled(npm(union-value)) = 1.0.0
Provides: bundled(npm(unset-value)) = 1.0.0
Provides: bundled(npm(upath)) = 1.1.0
Provides: bundled(npm(uri-js)) = 4.2.2
Provides: bundled(npm(urix)) = 0.1.0
Provides: bundled(npm(url)) = 0.11.0
Provides: bundled(npm(use)) = 3.1.0
Provides: bundled(npm(util)) = 0.10.4
Provides: bundled(npm(util)) = 0.10.3
Provides: bundled(npm(util-deprecate)) = 1.0.2
Provides: bundled(npm(validate-npm-package-license)) = 3.0.3
Provides: bundled(npm(vm-browserify)) = 0.0.4
Provides: bundled(npm(watchpack)) = 1.6.0
Provides: bundled(npm(webpack)) = 3.12.0
Provides: bundled(npm(webpack-sources)) = 1.1.0
Provides: bundled(npm(which)) = 1.3.1
Provides: bundled(npm(which-module)) = 2.0.0
Provides: bundled(npm(wide-align)) = 1.1.3
Provides: bundled(npm(window-size)) = 0.1.0
Provides: bundled(npm(wordwrap)) = 0.0.2
Provides: bundled(npm(wrap-ansi)) = 2.1.0
Provides: bundled(npm(wrappy)) = 1.0.2
Provides: bundled(npm(xtend)) = 4.0.1
Provides: bundled(npm(y18n)) = 3.2.1
Provides: bundled(npm(yallist)) = 3.0.2
Provides: bundled(npm(yallist)) = 2.1.2
Provides: bundled(npm(yargs)) = 8.0.2
Provides: bundled(npm(yargs)) = 3.10.0
Provides: bundled(npm(yargs-parser)) = 7.0.0
AutoReq: no
AutoProv: no

%define npm_cache_dir /tmp/npm_cache_%{name}-%{version}-%{release}

%description
%{summary}

%prep
mkdir -p %{npm_cache_dir}
for tgz in %{sources}; do
  echo $tgz | grep -q registry.npmjs.org || npm cache add --cache %{npm_cache_dir} $tgz
done
%setup -T -q -a 348 -D -n %{npm_cache_dir}

%build
npm install --cache-min Infinity --cache %{npm_cache_dir} --no-shrinkwrap --no-optional --global-style true %{npm_name}@%{version}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/bin %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/buildin %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/hot %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/lib %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/schemas %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/web_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}

mkdir -p %{buildroot}%{_bindir}/
chmod 0755 %{buildroot}%{nodejs_sitelib}/%{npm_name}/bin/webpack.js
ln -sf %{nodejs_sitelib}/%{npm_name}/bin/webpack.js %{buildroot}%{_bindir}/webpack

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%{_bindir}/webpack
%license node_modules/%{npm_name}/LICENSE
%doc node_modules/%{npm_name}/README.md

%changelog
* Wed Jun 06 2018 Eric D. Helms <ericdhelms@gmail.com> 3.12.0-1
- Update to 3.12.0

* Wed Nov 22 2017 Daniel Lobato Garcia <me@daniellobato.me> 3.4.1-3
- Install webpack binary without the .js extension
  (github@kohlvanwijngaarden.nl)

* Sat Oct 14 2017 Eric D. Helms <ericdhelms@gmail.com> 3.4.1-2
- Bump release to rebuild

* Mon Aug 07 2017 Eric D. Helms <ericdhelms@gmail.com> 3.4.1-1
- Update nodejs-weebpack to 3.4.1 (me@daniellobato.me)

* Sat Jul 15 2017 Eric D. Helms <ericdhelms@gmail.com> 3.0.0-2
- Add back missing Provides: npm (ericdhelms@gmail.com)

* Wed Jul 12 2017 Eric D. Helms <ericdhelms@gmail.com> 3.0.0-1
- update webpack to v3.0 (ohadlevy@gmail.com)
