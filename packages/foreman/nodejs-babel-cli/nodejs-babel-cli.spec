%global npm_name babel-cli
%global enable_tests 0

Name: nodejs-%{npm_name}
Version: 6.26.0
Release: 1%{?dist}
Summary: Babel command line
License: MIT
URL: https://babeljs.io/
Source0: http://registry.npmjs.org/babel-cli/-/babel-cli-6.26.0.tgz
Source1: http://registry.npmjs.org/fs-readdir-recursive/-/fs-readdir-recursive-1.0.0.tgz
Source2: http://registry.npmjs.org/babel-polyfill/-/babel-polyfill-6.26.0.tgz
Source3: http://registry.npmjs.org/convert-source-map/-/convert-source-map-1.5.0.tgz
Source4: http://registry.npmjs.org/commander/-/commander-2.11.0.tgz
Source5: http://registry.npmjs.org/babel-register/-/babel-register-6.26.0.tgz
Source6: http://registry.npmjs.org/glob/-/glob-7.1.2.tgz
Source7: http://registry.npmjs.org/output-file-sync/-/output-file-sync-1.1.2.tgz
Source8: http://registry.npmjs.org/babel-runtime/-/babel-runtime-6.26.0.tgz
Source9: http://registry.npmjs.org/slash/-/slash-1.0.0.tgz
Source10: http://registry.npmjs.org/path-is-absolute/-/path-is-absolute-1.0.1.tgz
Source11: http://registry.npmjs.org/v8flags/-/v8flags-2.1.1.tgz
Source12: http://registry.npmjs.org/babel-core/-/babel-core-6.26.0.tgz
Source13: http://registry.npmjs.org/lodash/-/lodash-4.17.4.tgz
Source14: http://registry.npmjs.org/source-map/-/source-map-0.5.7.tgz
Source15: http://registry.npmjs.org/chokidar/-/chokidar-1.7.0.tgz
Source16: http://registry.npmjs.org/regenerator-runtime/-/regenerator-runtime-0.10.5.tgz
Source17: http://registry.npmjs.org/home-or-tmp/-/home-or-tmp-2.0.0.tgz
Source18: http://registry.npmjs.org/core-js/-/core-js-2.5.1.tgz
Source19: http://registry.npmjs.org/mkdirp/-/mkdirp-0.5.1.tgz
Source20: http://registry.npmjs.org/source-map-support/-/source-map-support-0.4.18.tgz
Source21: http://registry.npmjs.org/inherits/-/inherits-2.0.3.tgz
Source22: http://registry.npmjs.org/inflight/-/inflight-1.0.6.tgz
Source23: http://registry.npmjs.org/fs.realpath/-/fs.realpath-1.0.0.tgz
Source24: http://registry.npmjs.org/once/-/once-1.4.0.tgz
Source25: http://registry.npmjs.org/minimatch/-/minimatch-3.0.4.tgz
Source26: http://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz
Source27: http://registry.npmjs.org/regenerator-runtime/-/regenerator-runtime-0.11.0.tgz
Source28: http://registry.npmjs.org/user-home/-/user-home-1.1.1.tgz
Source29: http://registry.npmjs.org/babel-code-frame/-/babel-code-frame-6.26.0.tgz
Source30: http://registry.npmjs.org/babel-messages/-/babel-messages-6.23.0.tgz
Source31: http://registry.npmjs.org/babel-helpers/-/babel-helpers-6.24.1.tgz
Source32: http://registry.npmjs.org/babel-generator/-/babel-generator-6.26.0.tgz
Source33: http://registry.npmjs.org/babel-template/-/babel-template-6.26.0.tgz
Source34: http://registry.npmjs.org/json5/-/json5-0.5.1.tgz
Source35: http://registry.npmjs.org/babel-traverse/-/babel-traverse-6.26.0.tgz
Source36: http://registry.npmjs.org/babel-types/-/babel-types-6.26.0.tgz
Source37: http://registry.npmjs.org/private/-/private-0.1.8.tgz
Source38: http://registry.npmjs.org/graceful-fs/-/graceful-fs-4.1.11.tgz
Source39: http://registry.npmjs.org/babylon/-/babylon-6.18.0.tgz
Source40: http://registry.npmjs.org/async-each/-/async-each-1.0.1.tgz
Source41: http://registry.npmjs.org/glob-parent/-/glob-parent-2.0.0.tgz
Source42: http://registry.npmjs.org/anymatch/-/anymatch-1.3.2.tgz
Source43: http://registry.npmjs.org/is-binary-path/-/is-binary-path-1.0.1.tgz
Source44: http://registry.npmjs.org/readdirp/-/readdirp-2.1.0.tgz
Source45: http://registry.npmjs.org/os-homedir/-/os-homedir-1.0.2.tgz
Source46: http://registry.npmjs.org/os-tmpdir/-/os-tmpdir-1.0.2.tgz
Source47: http://registry.npmjs.org/fsevents/-/fsevents-1.1.2.tgz
Source48: http://registry.npmjs.org/is-glob/-/is-glob-2.0.1.tgz
Source49: http://registry.npmjs.org/wrappy/-/wrappy-1.0.2.tgz
Source50: http://registry.npmjs.org/brace-expansion/-/brace-expansion-1.1.8.tgz
Source51: http://registry.npmjs.org/esutils/-/esutils-2.0.2.tgz
Source52: http://registry.npmjs.org/js-tokens/-/js-tokens-3.0.2.tgz
Source53: http://registry.npmjs.org/chalk/-/chalk-1.1.3.tgz
Source54: http://registry.npmjs.org/detect-indent/-/detect-indent-4.0.0.tgz
Source55: http://registry.npmjs.org/jsesc/-/jsesc-1.3.0.tgz
Source56: http://registry.npmjs.org/minimist/-/minimist-0.0.8.tgz
Source57: http://registry.npmjs.org/trim-right/-/trim-right-1.0.1.tgz
Source58: http://registry.npmjs.org/globals/-/globals-9.18.0.tgz
Source59: http://registry.npmjs.org/invariant/-/invariant-2.2.2.tgz
Source60: http://registry.npmjs.org/to-fast-properties/-/to-fast-properties-1.0.3.tgz
Source61: http://registry.npmjs.org/normalize-path/-/normalize-path-2.1.1.tgz
Source62: http://registry.npmjs.org/binary-extensions/-/binary-extensions-1.10.0.tgz
Source63: http://registry.npmjs.org/micromatch/-/micromatch-2.3.11.tgz
Source64: http://registry.npmjs.org/set-immediate-shim/-/set-immediate-shim-1.0.1.tgz
Source65: http://registry.npmjs.org/is-extglob/-/is-extglob-1.0.0.tgz
Source66: http://registry.npmjs.org/concat-map/-/concat-map-0.0.1.tgz
Source67: http://registry.npmjs.org/balanced-match/-/balanced-match-1.0.0.tgz
Source68: http://registry.npmjs.org/node-pre-gyp/-/node-pre-gyp-0.6.39.tgz
Source69: http://registry.npmjs.org/readable-stream/-/readable-stream-2.3.3.tgz
Source70: http://registry.npmjs.org/ansi-styles/-/ansi-styles-2.2.1.tgz
Source71: http://registry.npmjs.org/has-ansi/-/has-ansi-2.0.0.tgz
Source72: http://registry.npmjs.org/escape-string-regexp/-/escape-string-regexp-1.0.5.tgz
Source73: http://registry.npmjs.org/strip-ansi/-/strip-ansi-3.0.1.tgz
Source74: http://registry.npmjs.org/supports-color/-/supports-color-2.0.0.tgz
Source75: http://registry.npmjs.org/repeating/-/repeating-2.0.1.tgz
Source76: http://registry.npmjs.org/loose-envify/-/loose-envify-1.3.1.tgz
Source77: http://registry.npmjs.org/remove-trailing-separator/-/remove-trailing-separator-1.1.0.tgz
Source78: http://registry.npmjs.org/arr-diff/-/arr-diff-2.0.0.tgz
Source79: http://registry.npmjs.org/array-unique/-/array-unique-0.2.1.tgz
Source80: http://registry.npmjs.org/debug/-/debug-2.6.9.tgz
Source81: http://registry.npmjs.org/expand-brackets/-/expand-brackets-0.1.5.tgz
Source82: http://registry.npmjs.org/braces/-/braces-1.8.5.tgz
Source83: http://registry.npmjs.org/extglob/-/extglob-0.3.2.tgz
Source84: http://registry.npmjs.org/filename-regex/-/filename-regex-2.0.1.tgz
Source85: http://registry.npmjs.org/object.omit/-/object.omit-2.0.1.tgz
Source86: http://registry.npmjs.org/nan/-/nan-2.7.0.tgz
Source87: http://registry.npmjs.org/parse-glob/-/parse-glob-3.0.4.tgz
Source88: http://registry.npmjs.org/kind-of/-/kind-of-3.2.2.tgz
Source89: http://registry.npmjs.org/regex-cache/-/regex-cache-0.4.4.tgz
Source90: http://registry.npmjs.org/npmlog/-/npmlog-4.1.2.tgz
Source91: http://registry.npmjs.org/rc/-/rc-1.2.2.tgz
Source92: http://registry.npmjs.org/hawk/-/hawk-3.1.3.tgz
Source93: http://registry.npmjs.org/rimraf/-/rimraf-2.6.2.tgz
Source94: http://registry.npmjs.org/detect-libc/-/detect-libc-1.0.2.tgz
Source95: http://registry.npmjs.org/semver/-/semver-5.4.1.tgz
Source96: http://registry.npmjs.org/request/-/request-2.81.0.tgz
Source97: http://registry.npmjs.org/tar-pack/-/tar-pack-3.4.1.tgz
Source98: http://registry.npmjs.org/tar/-/tar-2.2.1.tgz
Source99: http://registry.npmjs.org/core-util-is/-/core-util-is-1.0.2.tgz
Source100: http://registry.npmjs.org/process-nextick-args/-/process-nextick-args-1.0.7.tgz
Source101: http://registry.npmjs.org/ansi-regex/-/ansi-regex-2.1.1.tgz
Source102: http://registry.npmjs.org/safe-buffer/-/safe-buffer-5.1.1.tgz
Source103: http://registry.npmjs.org/util-deprecate/-/util-deprecate-1.0.2.tgz
Source104: http://registry.npmjs.org/string_decoder/-/string_decoder-1.0.3.tgz
Source105: http://registry.npmjs.org/is-finite/-/is-finite-1.0.2.tgz
Source106: http://registry.npmjs.org/nopt/-/nopt-4.0.1.tgz
Source107: http://registry.npmjs.org/arr-flatten/-/arr-flatten-1.1.0.tgz
Source108: http://registry.npmjs.org/ms/-/ms-2.0.0.tgz
Source109: http://registry.npmjs.org/is-posix-bracket/-/is-posix-bracket-0.1.1.tgz
Source110: http://registry.npmjs.org/preserve/-/preserve-0.2.0.tgz
Source111: http://registry.npmjs.org/expand-range/-/expand-range-1.8.2.tgz
Source112: http://registry.npmjs.org/repeat-element/-/repeat-element-1.1.2.tgz
Source113: http://registry.npmjs.org/is-extendable/-/is-extendable-0.1.1.tgz
Source114: http://registry.npmjs.org/for-own/-/for-own-0.1.5.tgz
Source115: http://registry.npmjs.org/glob-base/-/glob-base-0.3.0.tgz
Source116: http://registry.npmjs.org/is-dotfile/-/is-dotfile-1.0.3.tgz
Source117: http://registry.npmjs.org/is-equal-shallow/-/is-equal-shallow-0.1.3.tgz
Source118: http://registry.npmjs.org/isarray/-/isarray-1.0.0.tgz
Source119: http://registry.npmjs.org/are-we-there-yet/-/are-we-there-yet-1.1.4.tgz
Source120: http://registry.npmjs.org/console-control-strings/-/console-control-strings-1.1.0.tgz
Source121: http://registry.npmjs.org/set-blocking/-/set-blocking-2.0.0.tgz
Source122: http://registry.npmjs.org/minimist/-/minimist-1.2.0.tgz
Source123: http://registry.npmjs.org/gauge/-/gauge-2.7.4.tgz
Source124: http://registry.npmjs.org/is-buffer/-/is-buffer-1.1.6.tgz
Source125: http://registry.npmjs.org/strip-json-comments/-/strip-json-comments-2.0.1.tgz
Source126: http://registry.npmjs.org/deep-extend/-/deep-extend-0.4.2.tgz
Source127: http://registry.npmjs.org/cryptiles/-/cryptiles-2.0.5.tgz
Source128: http://registry.npmjs.org/ini/-/ini-1.3.4.tgz
Source129: http://registry.npmjs.org/sntp/-/sntp-1.0.9.tgz
Source130: http://registry.npmjs.org/hoek/-/hoek-2.16.3.tgz
Source131: http://registry.npmjs.org/boom/-/boom-2.10.1.tgz
Source132: http://registry.npmjs.org/combined-stream/-/combined-stream-1.0.5.tgz
Source133: http://registry.npmjs.org/aws-sign2/-/aws-sign2-0.6.0.tgz
Source134: http://registry.npmjs.org/aws4/-/aws4-1.6.0.tgz
Source135: http://registry.npmjs.org/forever-agent/-/forever-agent-0.6.1.tgz
Source136: http://registry.npmjs.org/extend/-/extend-3.0.1.tgz
Source137: http://registry.npmjs.org/form-data/-/form-data-2.1.4.tgz
Source138: http://registry.npmjs.org/har-validator/-/har-validator-4.2.1.tgz
Source139: http://registry.npmjs.org/caseless/-/caseless-0.12.0.tgz
Source140: http://registry.npmjs.org/is-typedarray/-/is-typedarray-1.0.0.tgz
Source141: http://registry.npmjs.org/isstream/-/isstream-0.1.2.tgz
Source142: http://registry.npmjs.org/json-stringify-safe/-/json-stringify-safe-5.0.1.tgz
Source143: http://registry.npmjs.org/mime-types/-/mime-types-2.1.17.tgz
Source144: http://registry.npmjs.org/performance-now/-/performance-now-0.2.0.tgz
Source145: http://registry.npmjs.org/oauth-sign/-/oauth-sign-0.8.2.tgz
Source146: http://registry.npmjs.org/tough-cookie/-/tough-cookie-2.3.3.tgz
Source147: http://registry.npmjs.org/stringstream/-/stringstream-0.0.5.tgz
Source148: http://registry.npmjs.org/tunnel-agent/-/tunnel-agent-0.6.0.tgz
Source149: http://registry.npmjs.org/fstream/-/fstream-1.0.11.tgz
Source150: http://registry.npmjs.org/fstream-ignore/-/fstream-ignore-1.0.5.tgz
Source151: http://registry.npmjs.org/qs/-/qs-6.4.0.tgz
Source152: http://registry.npmjs.org/uuid/-/uuid-3.1.0.tgz
Source153: http://registry.npmjs.org/block-stream/-/block-stream-0.0.9.tgz
Source154: http://registry.npmjs.org/uid-number/-/uid-number-0.0.6.tgz
Source155: http://registry.npmjs.org/number-is-nan/-/number-is-nan-1.0.1.tgz
Source156: http://registry.npmjs.org/abbrev/-/abbrev-1.1.1.tgz
Source157: http://registry.npmjs.org/osenv/-/osenv-0.1.4.tgz
Source158: http://registry.npmjs.org/fill-range/-/fill-range-2.2.3.tgz
Source159: http://registry.npmjs.org/for-in/-/for-in-1.0.2.tgz
Source160: http://registry.npmjs.org/is-primitive/-/is-primitive-2.0.0.tgz
Source161: http://registry.npmjs.org/delegates/-/delegates-1.0.0.tgz
Source162: http://registry.npmjs.org/has-unicode/-/has-unicode-2.0.1.tgz
Source163: http://registry.npmjs.org/aproba/-/aproba-1.2.0.tgz
Source164: http://registry.npmjs.org/string-width/-/string-width-1.0.2.tgz
Source165: http://registry.npmjs.org/signal-exit/-/signal-exit-3.0.2.tgz
Source166: http://registry.npmjs.org/wide-align/-/wide-align-1.1.2.tgz
Source167: http://registry.npmjs.org/asynckit/-/asynckit-0.4.0.tgz
Source168: http://registry.npmjs.org/har-schema/-/har-schema-1.0.5.tgz
Source169: http://registry.npmjs.org/punycode/-/punycode-1.4.1.tgz
Source170: http://registry.npmjs.org/mime-db/-/mime-db-1.30.0.tgz
Source171: http://registry.npmjs.org/delayed-stream/-/delayed-stream-1.0.0.tgz
Source172: http://registry.npmjs.org/ajv/-/ajv-4.11.8.tgz
Source173: http://registry.npmjs.org/is-number/-/is-number-2.1.0.tgz
Source174: http://registry.npmjs.org/isobject/-/isobject-2.1.0.tgz
Source175: http://registry.npmjs.org/randomatic/-/randomatic-1.1.7.tgz
Source176: http://registry.npmjs.org/code-point-at/-/code-point-at-1.1.0.tgz
Source177: http://registry.npmjs.org/repeat-string/-/repeat-string-1.6.1.tgz
Source178: http://registry.npmjs.org/json-stable-stringify/-/json-stable-stringify-1.0.1.tgz
Source179: http://registry.npmjs.org/is-fullwidth-code-point/-/is-fullwidth-code-point-1.0.0.tgz
Source180: http://registry.npmjs.org/co/-/co-4.6.0.tgz
Source181: http://registry.npmjs.org/jsonify/-/jsonify-0.0.0.tgz
Source182: http://registry.npmjs.org/is-number/-/is-number-3.0.0.tgz
Source183: http://registry.npmjs.org/kind-of/-/kind-of-4.0.0.tgz
Source184: http://registry.npmjs.org/http-signature/-/http-signature-1.1.1.tgz
Source185: http://registry.npmjs.org/assert-plus/-/assert-plus-0.2.0.tgz
Source186: http://registry.npmjs.org/jsprim/-/jsprim-1.4.1.tgz
Source187: http://registry.npmjs.org/sshpk/-/sshpk-1.13.1.tgz
Source188: http://registry.npmjs.org/assert-plus/-/assert-plus-1.0.0.tgz
Source189: http://registry.npmjs.org/json-schema/-/json-schema-0.2.3.tgz
Source190: http://registry.npmjs.org/extsprintf/-/extsprintf-1.3.0.tgz
Source191: http://registry.npmjs.org/verror/-/verror-1.10.0.tgz
Source192: http://registry.npmjs.org/dashdash/-/dashdash-1.14.1.tgz
Source193: http://registry.npmjs.org/ecc-jsbn/-/ecc-jsbn-0.1.1.tgz
Source194: http://registry.npmjs.org/asn1/-/asn1-0.2.3.tgz
Source195: http://registry.npmjs.org/jsbn/-/jsbn-0.1.1.tgz
Source196: http://registry.npmjs.org/tweetnacl/-/tweetnacl-0.14.5.tgz
Source197: http://registry.npmjs.org/bcrypt-pbkdf/-/bcrypt-pbkdf-1.0.1.tgz
Source198: http://registry.npmjs.org/getpass/-/getpass-0.1.7.tgz
Source199: babel-cli-6.26.0-registry.npmjs.org.tgz
BuildRequires: nodejs-packaging
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: npm(%{npm_name}) = %{version}
Provides: bundled(npm(babel-cli)) = 6.26.0
Provides: bundled(npm(fs-readdir-recursive)) = 1.0.0
Provides: bundled(npm(babel-polyfill)) = 6.26.0
Provides: bundled(npm(convert-source-map)) = 1.5.0
Provides: bundled(npm(commander)) = 2.11.0
Provides: bundled(npm(babel-register)) = 6.26.0
Provides: bundled(npm(glob)) = 7.1.2
Provides: bundled(npm(output-file-sync)) = 1.1.2
Provides: bundled(npm(babel-runtime)) = 6.26.0
Provides: bundled(npm(slash)) = 1.0.0
Provides: bundled(npm(path-is-absolute)) = 1.0.1
Provides: bundled(npm(v8flags)) = 2.1.1
Provides: bundled(npm(babel-core)) = 6.26.0
Provides: bundled(npm(lodash)) = 4.17.4
Provides: bundled(npm(source-map)) = 0.5.7
Provides: bundled(npm(chokidar)) = 1.7.0
Provides: bundled(npm(regenerator-runtime)) = 0.10.5
Provides: bundled(npm(home-or-tmp)) = 2.0.0
Provides: bundled(npm(core-js)) = 2.5.1
Provides: bundled(npm(mkdirp)) = 0.5.1
Provides: bundled(npm(source-map-support)) = 0.4.18
Provides: bundled(npm(inherits)) = 2.0.3
Provides: bundled(npm(inflight)) = 1.0.6
Provides: bundled(npm(fs.realpath)) = 1.0.0
Provides: bundled(npm(once)) = 1.4.0
Provides: bundled(npm(minimatch)) = 3.0.4
Provides: bundled(npm(object-assign)) = 4.1.1
Provides: bundled(npm(regenerator-runtime)) = 0.11.0
Provides: bundled(npm(user-home)) = 1.1.1
Provides: bundled(npm(babel-code-frame)) = 6.26.0
Provides: bundled(npm(babel-messages)) = 6.23.0
Provides: bundled(npm(babel-helpers)) = 6.24.1
Provides: bundled(npm(babel-generator)) = 6.26.0
Provides: bundled(npm(babel-template)) = 6.26.0
Provides: bundled(npm(json5)) = 0.5.1
Provides: bundled(npm(babel-traverse)) = 6.26.0
Provides: bundled(npm(babel-types)) = 6.26.0
Provides: bundled(npm(private)) = 0.1.8
Provides: bundled(npm(graceful-fs)) = 4.1.11
Provides: bundled(npm(babylon)) = 6.18.0
Provides: bundled(npm(async-each)) = 1.0.1
Provides: bundled(npm(glob-parent)) = 2.0.0
Provides: bundled(npm(anymatch)) = 1.3.2
Provides: bundled(npm(is-binary-path)) = 1.0.1
Provides: bundled(npm(readdirp)) = 2.1.0
Provides: bundled(npm(os-homedir)) = 1.0.2
Provides: bundled(npm(os-tmpdir)) = 1.0.2
Provides: bundled(npm(fsevents)) = 1.1.2
Provides: bundled(npm(is-glob)) = 2.0.1
Provides: bundled(npm(wrappy)) = 1.0.2
Provides: bundled(npm(brace-expansion)) = 1.1.8
Provides: bundled(npm(esutils)) = 2.0.2
Provides: bundled(npm(js-tokens)) = 3.0.2
Provides: bundled(npm(chalk)) = 1.1.3
Provides: bundled(npm(detect-indent)) = 4.0.0
Provides: bundled(npm(jsesc)) = 1.3.0
Provides: bundled(npm(minimist)) = 0.0.8
Provides: bundled(npm(trim-right)) = 1.0.1
Provides: bundled(npm(globals)) = 9.18.0
Provides: bundled(npm(invariant)) = 2.2.2
Provides: bundled(npm(to-fast-properties)) = 1.0.3
Provides: bundled(npm(normalize-path)) = 2.1.1
Provides: bundled(npm(binary-extensions)) = 1.10.0
Provides: bundled(npm(micromatch)) = 2.3.11
Provides: bundled(npm(set-immediate-shim)) = 1.0.1
Provides: bundled(npm(is-extglob)) = 1.0.0
Provides: bundled(npm(concat-map)) = 0.0.1
Provides: bundled(npm(balanced-match)) = 1.0.0
Provides: bundled(npm(node-pre-gyp)) = 0.6.39
Provides: bundled(npm(readable-stream)) = 2.3.3
Provides: bundled(npm(ansi-styles)) = 2.2.1
Provides: bundled(npm(has-ansi)) = 2.0.0
Provides: bundled(npm(escape-string-regexp)) = 1.0.5
Provides: bundled(npm(strip-ansi)) = 3.0.1
Provides: bundled(npm(supports-color)) = 2.0.0
Provides: bundled(npm(repeating)) = 2.0.1
Provides: bundled(npm(loose-envify)) = 1.3.1
Provides: bundled(npm(remove-trailing-separator)) = 1.1.0
Provides: bundled(npm(arr-diff)) = 2.0.0
Provides: bundled(npm(array-unique)) = 0.2.1
Provides: bundled(npm(debug)) = 2.6.9
Provides: bundled(npm(expand-brackets)) = 0.1.5
Provides: bundled(npm(braces)) = 1.8.5
Provides: bundled(npm(extglob)) = 0.3.2
Provides: bundled(npm(filename-regex)) = 2.0.1
Provides: bundled(npm(object.omit)) = 2.0.1
Provides: bundled(npm(nan)) = 2.7.0
Provides: bundled(npm(parse-glob)) = 3.0.4
Provides: bundled(npm(kind-of)) = 3.2.2
Provides: bundled(npm(regex-cache)) = 0.4.4
Provides: bundled(npm(npmlog)) = 4.1.2
Provides: bundled(npm(rc)) = 1.2.2
Provides: bundled(npm(hawk)) = 3.1.3
Provides: bundled(npm(rimraf)) = 2.6.2
Provides: bundled(npm(detect-libc)) = 1.0.2
Provides: bundled(npm(semver)) = 5.4.1
Provides: bundled(npm(request)) = 2.81.0
Provides: bundled(npm(tar-pack)) = 3.4.1
Provides: bundled(npm(tar)) = 2.2.1
Provides: bundled(npm(core-util-is)) = 1.0.2
Provides: bundled(npm(process-nextick-args)) = 1.0.7
Provides: bundled(npm(ansi-regex)) = 2.1.1
Provides: bundled(npm(safe-buffer)) = 5.1.1
Provides: bundled(npm(util-deprecate)) = 1.0.2
Provides: bundled(npm(string_decoder)) = 1.0.3
Provides: bundled(npm(is-finite)) = 1.0.2
Provides: bundled(npm(nopt)) = 4.0.1
Provides: bundled(npm(arr-flatten)) = 1.1.0
Provides: bundled(npm(ms)) = 2.0.0
Provides: bundled(npm(is-posix-bracket)) = 0.1.1
Provides: bundled(npm(preserve)) = 0.2.0
Provides: bundled(npm(expand-range)) = 1.8.2
Provides: bundled(npm(repeat-element)) = 1.1.2
Provides: bundled(npm(is-extendable)) = 0.1.1
Provides: bundled(npm(for-own)) = 0.1.5
Provides: bundled(npm(glob-base)) = 0.3.0
Provides: bundled(npm(is-dotfile)) = 1.0.3
Provides: bundled(npm(is-equal-shallow)) = 0.1.3
Provides: bundled(npm(isarray)) = 1.0.0
Provides: bundled(npm(are-we-there-yet)) = 1.1.4
Provides: bundled(npm(console-control-strings)) = 1.1.0
Provides: bundled(npm(set-blocking)) = 2.0.0
Provides: bundled(npm(minimist)) = 1.2.0
Provides: bundled(npm(gauge)) = 2.7.4
Provides: bundled(npm(is-buffer)) = 1.1.6
Provides: bundled(npm(strip-json-comments)) = 2.0.1
Provides: bundled(npm(deep-extend)) = 0.4.2
Provides: bundled(npm(cryptiles)) = 2.0.5
Provides: bundled(npm(ini)) = 1.3.4
Provides: bundled(npm(sntp)) = 1.0.9
Provides: bundled(npm(hoek)) = 2.16.3
Provides: bundled(npm(boom)) = 2.10.1
Provides: bundled(npm(combined-stream)) = 1.0.5
Provides: bundled(npm(aws-sign2)) = 0.6.0
Provides: bundled(npm(aws4)) = 1.6.0
Provides: bundled(npm(forever-agent)) = 0.6.1
Provides: bundled(npm(extend)) = 3.0.1
Provides: bundled(npm(form-data)) = 2.1.4
Provides: bundled(npm(har-validator)) = 4.2.1
Provides: bundled(npm(caseless)) = 0.12.0
Provides: bundled(npm(is-typedarray)) = 1.0.0
Provides: bundled(npm(isstream)) = 0.1.2
Provides: bundled(npm(json-stringify-safe)) = 5.0.1
Provides: bundled(npm(mime-types)) = 2.1.17
Provides: bundled(npm(performance-now)) = 0.2.0
Provides: bundled(npm(oauth-sign)) = 0.8.2
Provides: bundled(npm(tough-cookie)) = 2.3.3
Provides: bundled(npm(stringstream)) = 0.0.5
Provides: bundled(npm(tunnel-agent)) = 0.6.0
Provides: bundled(npm(fstream)) = 1.0.11
Provides: bundled(npm(fstream-ignore)) = 1.0.5
Provides: bundled(npm(qs)) = 6.4.0
Provides: bundled(npm(uuid)) = 3.1.0
Provides: bundled(npm(block-stream)) = 0.0.9
Provides: bundled(npm(uid-number)) = 0.0.6
Provides: bundled(npm(number-is-nan)) = 1.0.1
Provides: bundled(npm(abbrev)) = 1.1.1
Provides: bundled(npm(osenv)) = 0.1.4
Provides: bundled(npm(fill-range)) = 2.2.3
Provides: bundled(npm(for-in)) = 1.0.2
Provides: bundled(npm(is-primitive)) = 2.0.0
Provides: bundled(npm(delegates)) = 1.0.0
Provides: bundled(npm(has-unicode)) = 2.0.1
Provides: bundled(npm(aproba)) = 1.2.0
Provides: bundled(npm(string-width)) = 1.0.2
Provides: bundled(npm(signal-exit)) = 3.0.2
Provides: bundled(npm(wide-align)) = 1.1.2
Provides: bundled(npm(asynckit)) = 0.4.0
Provides: bundled(npm(har-schema)) = 1.0.5
Provides: bundled(npm(punycode)) = 1.4.1
Provides: bundled(npm(mime-db)) = 1.30.0
Provides: bundled(npm(delayed-stream)) = 1.0.0
Provides: bundled(npm(ajv)) = 4.11.8
Provides: bundled(npm(is-number)) = 2.1.0
Provides: bundled(npm(isobject)) = 2.1.0
Provides: bundled(npm(randomatic)) = 1.1.7
Provides: bundled(npm(code-point-at)) = 1.1.0
Provides: bundled(npm(repeat-string)) = 1.6.1
Provides: bundled(npm(json-stable-stringify)) = 1.0.1
Provides: bundled(npm(is-fullwidth-code-point)) = 1.0.0
Provides: bundled(npm(co)) = 4.6.0
Provides: bundled(npm(jsonify)) = 0.0.0
Provides: bundled(npm(is-number)) = 3.0.0
Provides: bundled(npm(kind-of)) = 4.0.0
Provides: bundled(npm(http-signature)) = 1.1.1
Provides: bundled(npm(assert-plus)) = 0.2.0
Provides: bundled(npm(jsprim)) = 1.4.1
Provides: bundled(npm(sshpk)) = 1.13.1
Provides: bundled(npm(assert-plus)) = 1.0.0
Provides: bundled(npm(json-schema)) = 0.2.3
Provides: bundled(npm(extsprintf)) = 1.3.0
Provides: bundled(npm(verror)) = 1.10.0
Provides: bundled(npm(dashdash)) = 1.14.1
Provides: bundled(npm(ecc-jsbn)) = 0.1.1
Provides: bundled(npm(asn1)) = 0.2.3
Provides: bundled(npm(jsbn)) = 0.1.1
Provides: bundled(npm(tweetnacl)) = 0.14.5
Provides: bundled(npm(bcrypt-pbkdf)) = 1.0.1
Provides: bundled(npm(getpass)) = 0.1.7
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

%setup -T -q -a 199 -D -n %{npm_cache_dir}

%build
npm install --cache-min Infinity --cache %{npm_cache_dir} --no-optional --global-style true %{npm_name}@%{version}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cd node_modules/babel-cli
cp -pfr .npmignore README.md bin index.js lib package-lock.json package.json scripts node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pf README.md  ../../
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}/bin
mkdir -p %{buildroot}%{_bindir}/
install -p -D -m0755 bin/babel-doctor.js %{buildroot}%{nodejs_sitelib}/%{npm_name}/bin/babel-doctor.js
ln -sf %{nodejs_sitelib}/%{npm_name}/bin/babel-doctor.js %{buildroot}%{_bindir}/babel-doctor.js
install -p -D -m0755 bin/babel.js %{buildroot}%{nodejs_sitelib}/%{npm_name}/bin/babel.js
ln -sf %{nodejs_sitelib}/%{npm_name}/bin/babel.js %{buildroot}%{_bindir}/babel.js
install -p -D -m0755 bin/babel-node.js %{buildroot}%{nodejs_sitelib}/%{npm_name}/bin/babel-node.js
ln -sf %{nodejs_sitelib}/%{npm_name}/bin/babel-node.js %{buildroot}%{_bindir}/babel-node.js
install -p -D -m0755 bin/babel-external-helpers.js %{buildroot}%{nodejs_sitelib}/%{npm_name}/bin/babel-external-helpers.js
ln -sf %{nodejs_sitelib}/%{npm_name}/bin/babel-external-helpers.js %{buildroot}%{_bindir}/babel-external-helpers.js

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%endif

%files
%{nodejs_sitelib}/%{npm_name}
%{_bindir}/babel-doctor.js
%{_bindir}/babel.js
%{_bindir}/babel-node.js
%{_bindir}/babel-external-helpers.js

%doc README.md

%changelog
* Tue Nov 07 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 6.26.0-1
- new package built with tito

