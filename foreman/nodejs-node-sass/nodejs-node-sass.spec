%global npm_name node-sass

%{?nodejs_find_provides_and_requires}

# Disable debuginfo as symbols aren't extracted from the binary in vendor/
%global debug_package %{nil}

Name: nodejs-%{npm_name}
Version: 4.5.0
Release: 2%{?dist}
Summary: Wrapper around libsass
License: MIT
URL: https://github.com/sass/node-sass
Source0: http://registry.npmjs.org/node-sass/-/node-sass-4.5.0.tgz
Source1: http://registry.npmjs.org/in-publish/-/in-publish-2.0.0.tgz
Source2: http://registry.npmjs.org/chalk/-/chalk-1.1.3.tgz
Source3: http://registry.npmjs.org/lodash.assign/-/lodash.assign-4.2.0.tgz
Source4: http://registry.npmjs.org/get-stdin/-/get-stdin-4.0.1.tgz
Source5: http://registry.npmjs.org/cross-spawn/-/cross-spawn-3.0.1.tgz
Source6: http://registry.npmjs.org/async-foreach/-/async-foreach-0.1.3.tgz
Source7: http://registry.npmjs.org/gaze/-/gaze-1.1.2.tgz
Source8: http://registry.npmjs.org/glob/-/glob-7.1.1.tgz
Source9: http://registry.npmjs.org/mkdirp/-/mkdirp-0.5.1.tgz
Source10: http://registry.npmjs.org/lodash.clonedeep/-/lodash.clonedeep-4.5.0.tgz
Source11: http://registry.npmjs.org/meow/-/meow-3.7.0.tgz
Source12: http://registry.npmjs.org/npmlog/-/npmlog-4.0.2.tgz
Source13: http://registry.npmjs.org/lodash.mergewith/-/lodash.mergewith-4.6.0.tgz
Source14: http://registry.npmjs.org/nan/-/nan-2.5.1.tgz
Source15: http://registry.npmjs.org/node-gyp/-/node-gyp-3.5.0.tgz
Source16: http://registry.npmjs.org/request/-/request-2.79.0.tgz
Source17: http://registry.npmjs.org/stdout-stream/-/stdout-stream-1.4.0.tgz
Source18: http://registry.npmjs.org/has-ansi/-/has-ansi-2.0.0.tgz
Source19: http://registry.npmjs.org/sass-graph/-/sass-graph-2.1.2.tgz
Source20: http://registry.npmjs.org/ansi-styles/-/ansi-styles-2.2.1.tgz
Source21: http://registry.npmjs.org/escape-string-regexp/-/escape-string-regexp-1.0.5.tgz
Source22: http://registry.npmjs.org/strip-ansi/-/strip-ansi-3.0.1.tgz
Source23: http://registry.npmjs.org/lru-cache/-/lru-cache-4.0.2.tgz
Source24: http://registry.npmjs.org/supports-color/-/supports-color-2.0.0.tgz
Source25: http://registry.npmjs.org/globule/-/globule-1.1.0.tgz
Source26: http://registry.npmjs.org/inflight/-/inflight-1.0.6.tgz
Source27: http://registry.npmjs.org/inherits/-/inherits-2.0.3.tgz
Source28: http://registry.npmjs.org/once/-/once-1.4.0.tgz
Source29: http://registry.npmjs.org/fs.realpath/-/fs.realpath-1.0.0.tgz
Source30: http://registry.npmjs.org/which/-/which-1.2.12.tgz
Source31: http://registry.npmjs.org/path-is-absolute/-/path-is-absolute-1.0.1.tgz
Source32: http://registry.npmjs.org/minimatch/-/minimatch-3.0.3.tgz
Source33: http://registry.npmjs.org/decamelize/-/decamelize-1.2.0.tgz
Source34: http://registry.npmjs.org/camelcase-keys/-/camelcase-keys-2.1.0.tgz
Source35: http://registry.npmjs.org/minimist/-/minimist-0.0.8.tgz
Source36: http://registry.npmjs.org/map-obj/-/map-obj-1.0.1.tgz
Source37: http://registry.npmjs.org/minimist/-/minimist-1.2.0.tgz
Source38: http://registry.npmjs.org/normalize-package-data/-/normalize-package-data-2.3.5.tgz
Source39: http://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz
Source40: http://registry.npmjs.org/read-pkg-up/-/read-pkg-up-1.0.1.tgz
Source41: http://registry.npmjs.org/trim-newlines/-/trim-newlines-1.0.0.tgz
Source42: http://registry.npmjs.org/redent/-/redent-1.0.0.tgz
Source43: http://registry.npmjs.org/console-control-strings/-/console-control-strings-1.1.0.tgz
Source44: http://registry.npmjs.org/are-we-there-yet/-/are-we-there-yet-1.1.2.tgz
Source45: http://registry.npmjs.org/loud-rejection/-/loud-rejection-1.6.0.tgz
Source46: http://registry.npmjs.org/set-blocking/-/set-blocking-2.0.0.tgz
Source47: http://registry.npmjs.org/gauge/-/gauge-2.7.3.tgz
Source48: http://registry.npmjs.org/fstream/-/fstream-1.0.10.tgz
Source49: http://registry.npmjs.org/graceful-fs/-/graceful-fs-4.1.11.tgz
Source50: http://registry.npmjs.org/nopt/-/nopt-3.0.6.tgz
Source51: http://registry.npmjs.org/osenv/-/osenv-0.1.4.tgz
Source52: http://registry.npmjs.org/caseless/-/caseless-0.11.0.tgz
Source53: http://registry.npmjs.org/aws-sign2/-/aws-sign2-0.6.0.tgz
Source54: http://registry.npmjs.org/semver/-/semver-5.3.0.tgz
Source55: http://registry.npmjs.org/rimraf/-/rimraf-2.6.1.tgz
Source56: http://registry.npmjs.org/tar/-/tar-2.2.1.tgz
Source57: http://registry.npmjs.org/aws4/-/aws4-1.6.0.tgz
Source58: http://registry.npmjs.org/extend/-/extend-3.0.0.tgz
Source59: http://registry.npmjs.org/combined-stream/-/combined-stream-1.0.5.tgz
Source60: http://registry.npmjs.org/har-validator/-/har-validator-2.0.6.tgz
Source61: http://registry.npmjs.org/forever-agent/-/forever-agent-0.6.1.tgz
Source62: http://registry.npmjs.org/is-typedarray/-/is-typedarray-1.0.0.tgz
Source63: http://registry.npmjs.org/isstream/-/isstream-0.1.2.tgz
Source64: http://registry.npmjs.org/http-signature/-/http-signature-1.1.1.tgz
Source65: http://registry.npmjs.org/mime-types/-/mime-types-2.1.14.tgz
Source66: http://registry.npmjs.org/form-data/-/form-data-2.1.2.tgz
Source67: http://registry.npmjs.org/hawk/-/hawk-3.1.3.tgz
Source68: http://registry.npmjs.org/json-stringify-safe/-/json-stringify-safe-5.0.1.tgz
Source69: http://registry.npmjs.org/tunnel-agent/-/tunnel-agent-0.4.3.tgz
Source70: http://registry.npmjs.org/oauth-sign/-/oauth-sign-0.8.2.tgz
Source71: http://registry.npmjs.org/stringstream/-/stringstream-0.0.5.tgz
Source72: http://registry.npmjs.org/qs/-/qs-6.3.1.tgz
Source73: http://registry.npmjs.org/ansi-regex/-/ansi-regex-2.1.1.tgz
Source74: http://registry.npmjs.org/tough-cookie/-/tough-cookie-2.3.2.tgz
Source75: http://registry.npmjs.org/uuid/-/uuid-3.0.1.tgz
Source76: http://registry.npmjs.org/readable-stream/-/readable-stream-2.2.3.tgz
Source77: http://registry.npmjs.org/pseudomap/-/pseudomap-1.0.2.tgz
Source78: http://registry.npmjs.org/yallist/-/yallist-2.0.0.tgz
Source79: http://registry.npmjs.org/lodash/-/lodash-4.17.4.tgz
Source80: http://registry.npmjs.org/yargs/-/yargs-4.8.1.tgz
Source81: http://registry.npmjs.org/lodash/-/lodash-4.16.6.tgz
Source82: http://registry.npmjs.org/wrappy/-/wrappy-1.0.2.tgz
Source83: http://registry.npmjs.org/isexe/-/isexe-1.1.2.tgz
Source84: http://registry.npmjs.org/validate-npm-package-license/-/validate-npm-package-license-3.0.1.tgz
Source85: http://registry.npmjs.org/brace-expansion/-/brace-expansion-1.1.6.tgz
Source86: http://registry.npmjs.org/is-builtin-module/-/is-builtin-module-1.0.0.tgz
Source87: http://registry.npmjs.org/hosted-git-info/-/hosted-git-info-2.2.0.tgz
Source88: http://registry.npmjs.org/find-up/-/find-up-1.1.2.tgz
Source89: http://registry.npmjs.org/delegates/-/delegates-1.0.0.tgz
Source90: http://registry.npmjs.org/aproba/-/aproba-1.1.1.tgz
Source91: http://registry.npmjs.org/read-pkg/-/read-pkg-1.1.0.tgz
Source92: http://registry.npmjs.org/strip-indent/-/strip-indent-1.0.1.tgz
Source93: http://registry.npmjs.org/currently-unhandled/-/currently-unhandled-0.4.1.tgz
Source94: http://registry.npmjs.org/signal-exit/-/signal-exit-3.0.2.tgz
Source95: http://registry.npmjs.org/indent-string/-/indent-string-2.1.0.tgz
Source96: http://registry.npmjs.org/wide-align/-/wide-align-1.1.0.tgz
Source97: http://registry.npmjs.org/has-unicode/-/has-unicode-2.0.1.tgz
Source98: http://registry.npmjs.org/camelcase/-/camelcase-2.1.1.tgz
Source99: http://registry.npmjs.org/abbrev/-/abbrev-1.1.0.tgz
Source100: http://registry.npmjs.org/os-homedir/-/os-homedir-1.0.2.tgz
Source101: http://registry.npmjs.org/os-tmpdir/-/os-tmpdir-1.0.2.tgz
Source102: http://registry.npmjs.org/block-stream/-/block-stream-0.0.9.tgz
Source103: http://registry.npmjs.org/delayed-stream/-/delayed-stream-1.0.0.tgz
Source104: http://registry.npmjs.org/string-width/-/string-width-1.0.2.tgz
Source105: http://registry.npmjs.org/pinkie-promise/-/pinkie-promise-2.0.1.tgz
Source106: http://registry.npmjs.org/commander/-/commander-2.9.0.tgz
Source107: http://registry.npmjs.org/asynckit/-/asynckit-0.4.0.tgz
Source108: http://registry.npmjs.org/mime-db/-/mime-db-1.26.0.tgz
Source109: http://registry.npmjs.org/sshpk/-/sshpk-1.10.2.tgz
Source110: http://registry.npmjs.org/assert-plus/-/assert-plus-0.2.0.tgz
Source111: http://registry.npmjs.org/jsprim/-/jsprim-1.3.1.tgz
Source112: http://registry.npmjs.org/buffer-shims/-/buffer-shims-1.0.0.tgz
Source113: http://registry.npmjs.org/sntp/-/sntp-1.0.9.tgz
Source114: http://registry.npmjs.org/punycode/-/punycode-1.4.1.tgz
Source115: http://registry.npmjs.org/boom/-/boom-2.10.1.tgz
Source116: http://registry.npmjs.org/cryptiles/-/cryptiles-2.0.5.tgz
Source117: http://registry.npmjs.org/core-util-is/-/core-util-is-1.0.2.tgz
Source118: http://registry.npmjs.org/hoek/-/hoek-2.16.3.tgz
Source119: http://registry.npmjs.org/isarray/-/isarray-1.0.0.tgz
Source120: http://registry.npmjs.org/is-my-json-valid/-/is-my-json-valid-2.16.0.tgz
Source121: http://registry.npmjs.org/process-nextick-args/-/process-nextick-args-1.0.7.tgz
Source122: http://registry.npmjs.org/string_decoder/-/string_decoder-0.10.31.tgz
Source123: http://registry.npmjs.org/util-deprecate/-/util-deprecate-1.0.2.tgz
Source124: http://registry.npmjs.org/cliui/-/cliui-3.2.0.tgz
Source125: http://registry.npmjs.org/get-caller-file/-/get-caller-file-1.0.2.tgz
Source126: http://registry.npmjs.org/os-locale/-/os-locale-1.4.0.tgz
Source127: http://registry.npmjs.org/require-main-filename/-/require-main-filename-1.0.1.tgz
Source128: http://registry.npmjs.org/require-directory/-/require-directory-2.1.1.tgz
Source129: http://registry.npmjs.org/which-module/-/which-module-1.0.0.tgz
Source130: http://registry.npmjs.org/window-size/-/window-size-0.2.0.tgz
Source131: http://registry.npmjs.org/y18n/-/y18n-3.2.1.tgz
Source132: http://registry.npmjs.org/spdx-correct/-/spdx-correct-1.0.2.tgz
Source133: http://registry.npmjs.org/spdx-expression-parse/-/spdx-expression-parse-1.0.4.tgz
Source134: http://registry.npmjs.org/yargs-parser/-/yargs-parser-2.4.1.tgz
Source135: http://registry.npmjs.org/builtin-modules/-/builtin-modules-1.1.1.tgz
Source136: http://registry.npmjs.org/balanced-match/-/balanced-match-0.4.2.tgz
Source137: http://registry.npmjs.org/concat-map/-/concat-map-0.0.1.tgz
Source138: http://registry.npmjs.org/load-json-file/-/load-json-file-1.1.0.tgz
Source139: http://registry.npmjs.org/path-exists/-/path-exists-2.1.0.tgz
Source140: http://registry.npmjs.org/path-type/-/path-type-1.1.0.tgz
Source141: http://registry.npmjs.org/repeating/-/repeating-2.0.1.tgz
Source142: http://registry.npmjs.org/code-point-at/-/code-point-at-1.1.0.tgz
Source143: http://registry.npmjs.org/array-find-index/-/array-find-index-1.0.2.tgz
Source144: http://registry.npmjs.org/is-fullwidth-code-point/-/is-fullwidth-code-point-1.0.0.tgz
Source145: http://registry.npmjs.org/graceful-readlink/-/graceful-readlink-1.0.1.tgz
Source146: http://registry.npmjs.org/assert-plus/-/assert-plus-1.0.0.tgz
Source147: http://registry.npmjs.org/pinkie/-/pinkie-2.0.4.tgz
Source148: http://registry.npmjs.org/getpass/-/getpass-0.1.6.tgz
Source149: http://registry.npmjs.org/asn1/-/asn1-0.2.3.tgz
Source150: http://registry.npmjs.org/dashdash/-/dashdash-1.14.1.tgz
Source151: http://registry.npmjs.org/jsbn/-/jsbn-0.1.1.tgz
Source152: http://registry.npmjs.org/jodid25519/-/jodid25519-1.0.2.tgz
Source153: http://registry.npmjs.org/json-schema/-/json-schema-0.2.3.tgz
Source154: http://registry.npmjs.org/bcrypt-pbkdf/-/bcrypt-pbkdf-1.0.1.tgz
Source155: http://registry.npmjs.org/verror/-/verror-1.3.6.tgz
Source156: http://registry.npmjs.org/generate-function/-/generate-function-2.0.0.tgz
Source157: http://registry.npmjs.org/generate-object-property/-/generate-object-property-1.2.0.tgz
Source158: http://registry.npmjs.org/jsonpointer/-/jsonpointer-4.0.1.tgz
Source159: http://registry.npmjs.org/xtend/-/xtend-4.0.1.tgz
Source160: http://registry.npmjs.org/wrap-ansi/-/wrap-ansi-2.1.0.tgz
Source161: http://registry.npmjs.org/ecc-jsbn/-/ecc-jsbn-0.1.1.tgz
Source162: http://registry.npmjs.org/extsprintf/-/extsprintf-1.0.2.tgz
Source163: http://registry.npmjs.org/lcid/-/lcid-1.0.0.tgz
Source164: http://registry.npmjs.org/camelcase/-/camelcase-3.0.0.tgz
Source165: http://registry.npmjs.org/spdx-license-ids/-/spdx-license-ids-1.2.2.tgz
Source166: http://registry.npmjs.org/pify/-/pify-2.3.0.tgz
Source167: http://registry.npmjs.org/parse-json/-/parse-json-2.2.0.tgz
Source168: http://registry.npmjs.org/tweetnacl/-/tweetnacl-0.14.5.tgz
Source169: http://registry.npmjs.org/strip-bom/-/strip-bom-2.0.0.tgz
Source170: http://registry.npmjs.org/number-is-nan/-/number-is-nan-1.0.1.tgz
Source171: http://registry.npmjs.org/is-finite/-/is-finite-1.0.2.tgz
Source172: http://registry.npmjs.org/is-property/-/is-property-1.0.2.tgz
Source173: http://registry.npmjs.org/invert-kv/-/invert-kv-1.0.0.tgz
Source174: http://registry.npmjs.org/is-utf8/-/is-utf8-0.2.1.tgz
Source175: http://registry.npmjs.org/error-ex/-/error-ex-1.3.0.tgz
Source176: http://registry.npmjs.org/is-arrayish/-/is-arrayish-0.2.1.tgz
Source177: node-sass-4.5.0-registry.npmjs.org.tgz
Requires: nodejs(engine)
Requires: npm(node-gyp)
BuildRequires: nodejs-devel
BuildRequires: nodejs-packaging
BuildRequires: npm
BuildRequires: npm(node-gyp)
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches}
%else
ExclusiveArch: %{ix86} x86_64 %{arm}
%endif
Provides: npm(%{npm_name}) = %{version}
Provides: bundled(libsass) = 3.5.0.beta.2
Provides: bundled-npm(node-sass) = 4.5.0
Provides: bundled-npm(in-publish) = 2.0.0
Provides: bundled-npm(chalk) = 1.1.3
Provides: bundled-npm(lodash.assign) = 4.2.0
Provides: bundled-npm(get-stdin) = 4.0.1
Provides: bundled-npm(cross-spawn) = 3.0.1
Provides: bundled-npm(async-foreach) = 0.1.3
Provides: bundled-npm(gaze) = 1.1.2
Provides: bundled-npm(glob) = 7.1.1
Provides: bundled-npm(mkdirp) = 0.5.1
Provides: bundled-npm(lodash.clonedeep) = 4.5.0
Provides: bundled-npm(meow) = 3.7.0
Provides: bundled-npm(npmlog) = 4.0.2
Provides: bundled-npm(lodash.mergewith) = 4.6.0
Provides: bundled-npm(nan) = 2.5.1
Provides: bundled-npm(node-gyp) = 3.5.0
Provides: bundled-npm(request) = 2.79.0
Provides: bundled-npm(stdout-stream) = 1.4.0
Provides: bundled-npm(has-ansi) = 2.0.0
Provides: bundled-npm(sass-graph) = 2.1.2
Provides: bundled-npm(ansi-styles) = 2.2.1
Provides: bundled-npm(escape-string-regexp) = 1.0.5
Provides: bundled-npm(strip-ansi) = 3.0.1
Provides: bundled-npm(lru-cache) = 4.0.2
Provides: bundled-npm(supports-color) = 2.0.0
Provides: bundled-npm(globule) = 1.1.0
Provides: bundled-npm(inflight) = 1.0.6
Provides: bundled-npm(inherits) = 2.0.3
Provides: bundled-npm(once) = 1.4.0
Provides: bundled-npm(fs.realpath) = 1.0.0
Provides: bundled-npm(which) = 1.2.12
Provides: bundled-npm(path-is-absolute) = 1.0.1
Provides: bundled-npm(minimatch) = 3.0.3
Provides: bundled-npm(decamelize) = 1.2.0
Provides: bundled-npm(camelcase-keys) = 2.1.0
Provides: bundled-npm(minimist) = 0.0.8
Provides: bundled-npm(map-obj) = 1.0.1
Provides: bundled-npm(minimist) = 1.2.0
Provides: bundled-npm(normalize-package-data) = 2.3.5
Provides: bundled-npm(object-assign) = 4.1.1
Provides: bundled-npm(read-pkg-up) = 1.0.1
Provides: bundled-npm(trim-newlines) = 1.0.0
Provides: bundled-npm(redent) = 1.0.0
Provides: bundled-npm(console-control-strings) = 1.1.0
Provides: bundled-npm(are-we-there-yet) = 1.1.2
Provides: bundled-npm(loud-rejection) = 1.6.0
Provides: bundled-npm(set-blocking) = 2.0.0
Provides: bundled-npm(gauge) = 2.7.3
Provides: bundled-npm(fstream) = 1.0.10
Provides: bundled-npm(graceful-fs) = 4.1.11
Provides: bundled-npm(nopt) = 3.0.6
Provides: bundled-npm(osenv) = 0.1.4
Provides: bundled-npm(caseless) = 0.11.0
Provides: bundled-npm(aws-sign2) = 0.6.0
Provides: bundled-npm(semver) = 5.3.0
Provides: bundled-npm(rimraf) = 2.6.1
Provides: bundled-npm(tar) = 2.2.1
Provides: bundled-npm(aws4) = 1.6.0
Provides: bundled-npm(extend) = 3.0.0
Provides: bundled-npm(combined-stream) = 1.0.5
Provides: bundled-npm(har-validator) = 2.0.6
Provides: bundled-npm(forever-agent) = 0.6.1
Provides: bundled-npm(is-typedarray) = 1.0.0
Provides: bundled-npm(isstream) = 0.1.2
Provides: bundled-npm(http-signature) = 1.1.1
Provides: bundled-npm(mime-types) = 2.1.14
Provides: bundled-npm(form-data) = 2.1.2
Provides: bundled-npm(hawk) = 3.1.3
Provides: bundled-npm(json-stringify-safe) = 5.0.1
Provides: bundled-npm(tunnel-agent) = 0.4.3
Provides: bundled-npm(oauth-sign) = 0.8.2
Provides: bundled-npm(stringstream) = 0.0.5
Provides: bundled-npm(qs) = 6.3.1
Provides: bundled-npm(ansi-regex) = 2.1.1
Provides: bundled-npm(tough-cookie) = 2.3.2
Provides: bundled-npm(uuid) = 3.0.1
Provides: bundled-npm(readable-stream) = 2.2.3
Provides: bundled-npm(pseudomap) = 1.0.2
Provides: bundled-npm(yallist) = 2.0.0
Provides: bundled-npm(lodash) = 4.17.4
Provides: bundled-npm(yargs) = 4.8.1
Provides: bundled-npm(lodash) = 4.16.6
Provides: bundled-npm(wrappy) = 1.0.2
Provides: bundled-npm(isexe) = 1.1.2
Provides: bundled-npm(validate-npm-package-license) = 3.0.1
Provides: bundled-npm(brace-expansion) = 1.1.6
Provides: bundled-npm(is-builtin-module) = 1.0.0
Provides: bundled-npm(hosted-git-info) = 2.2.0
Provides: bundled-npm(find-up) = 1.1.2
Provides: bundled-npm(delegates) = 1.0.0
Provides: bundled-npm(aproba) = 1.1.1
Provides: bundled-npm(read-pkg) = 1.1.0
Provides: bundled-npm(strip-indent) = 1.0.1
Provides: bundled-npm(currently-unhandled) = 0.4.1
Provides: bundled-npm(signal-exit) = 3.0.2
Provides: bundled-npm(indent-string) = 2.1.0
Provides: bundled-npm(wide-align) = 1.1.0
Provides: bundled-npm(has-unicode) = 2.0.1
Provides: bundled-npm(camelcase) = 2.1.1
Provides: bundled-npm(abbrev) = 1.1.0
Provides: bundled-npm(os-homedir) = 1.0.2
Provides: bundled-npm(os-tmpdir) = 1.0.2
Provides: bundled-npm(block-stream) = 0.0.9
Provides: bundled-npm(delayed-stream) = 1.0.0
Provides: bundled-npm(string-width) = 1.0.2
Provides: bundled-npm(pinkie-promise) = 2.0.1
Provides: bundled-npm(commander) = 2.9.0
Provides: bundled-npm(asynckit) = 0.4.0
Provides: bundled-npm(mime-db) = 1.26.0
Provides: bundled-npm(sshpk) = 1.10.2
Provides: bundled-npm(assert-plus) = 0.2.0
Provides: bundled-npm(jsprim) = 1.3.1
Provides: bundled-npm(buffer-shims) = 1.0.0
Provides: bundled-npm(sntp) = 1.0.9
Provides: bundled-npm(punycode) = 1.4.1
Provides: bundled-npm(boom) = 2.10.1
Provides: bundled-npm(cryptiles) = 2.0.5
Provides: bundled-npm(core-util-is) = 1.0.2
Provides: bundled-npm(hoek) = 2.16.3
Provides: bundled-npm(isarray) = 1.0.0
Provides: bundled-npm(is-my-json-valid) = 2.16.0
Provides: bundled-npm(process-nextick-args) = 1.0.7
Provides: bundled-npm(string_decoder) = 0.10.31
Provides: bundled-npm(util-deprecate) = 1.0.2
Provides: bundled-npm(cliui) = 3.2.0
Provides: bundled-npm(get-caller-file) = 1.0.2
Provides: bundled-npm(os-locale) = 1.4.0
Provides: bundled-npm(require-main-filename) = 1.0.1
Provides: bundled-npm(require-directory) = 2.1.1
Provides: bundled-npm(which-module) = 1.0.0
Provides: bundled-npm(window-size) = 0.2.0
Provides: bundled-npm(y18n) = 3.2.1
Provides: bundled-npm(spdx-correct) = 1.0.2
Provides: bundled-npm(spdx-expression-parse) = 1.0.4
Provides: bundled-npm(yargs-parser) = 2.4.1
Provides: bundled-npm(builtin-modules) = 1.1.1
Provides: bundled-npm(balanced-match) = 0.4.2
Provides: bundled-npm(concat-map) = 0.0.1
Provides: bundled-npm(load-json-file) = 1.1.0
Provides: bundled-npm(path-exists) = 2.1.0
Provides: bundled-npm(path-type) = 1.1.0
Provides: bundled-npm(repeating) = 2.0.1
Provides: bundled-npm(code-point-at) = 1.1.0
Provides: bundled-npm(array-find-index) = 1.0.2
Provides: bundled-npm(is-fullwidth-code-point) = 1.0.0
Provides: bundled-npm(graceful-readlink) = 1.0.1
Provides: bundled-npm(assert-plus) = 1.0.0
Provides: bundled-npm(pinkie) = 2.0.4
Provides: bundled-npm(getpass) = 0.1.6
Provides: bundled-npm(asn1) = 0.2.3
Provides: bundled-npm(dashdash) = 1.14.1
Provides: bundled-npm(jsbn) = 0.1.1
Provides: bundled-npm(jodid25519) = 1.0.2
Provides: bundled-npm(json-schema) = 0.2.3
Provides: bundled-npm(bcrypt-pbkdf) = 1.0.1
Provides: bundled-npm(verror) = 1.3.6
Provides: bundled-npm(generate-function) = 2.0.0
Provides: bundled-npm(generate-object-property) = 1.2.0
Provides: bundled-npm(jsonpointer) = 4.0.1
Provides: bundled-npm(xtend) = 4.0.1
Provides: bundled-npm(wrap-ansi) = 2.1.0
Provides: bundled-npm(ecc-jsbn) = 0.1.1
Provides: bundled-npm(extsprintf) = 1.0.2
Provides: bundled-npm(lcid) = 1.0.0
Provides: bundled-npm(camelcase) = 3.0.0
Provides: bundled-npm(spdx-license-ids) = 1.2.2
Provides: bundled-npm(pify) = 2.3.0
Provides: bundled-npm(parse-json) = 2.2.0
Provides: bundled-npm(tweetnacl) = 0.14.5
Provides: bundled-npm(strip-bom) = 2.0.0
Provides: bundled-npm(number-is-nan) = 1.0.1
Provides: bundled-npm(is-finite) = 1.0.2
Provides: bundled-npm(is-property) = 1.0.2
Provides: bundled-npm(invert-kv) = 1.0.0
Provides: bundled-npm(is-utf8) = 0.2.1
Provides: bundled-npm(error-ex) = 1.3.0
Provides: bundled-npm(is-arrayish) = 0.2.1
AutoReq: no
AutoProv: no

%description
%{summary}

%prep
mkdir npm_cache
for tgz in %{sources}; do
  echo $tgz | grep -q "registry.npmjs.org" || npm cache add --cache ./npm_cache $tgz
done

%setup -T -q -a 177 -D -n npm_cache

%build
# Disable download of pre-existing library binaries during installation
export SKIP_SASS_BINARY_DOWNLOAD_FOR_CI=true
npm install --cache-min Infinity --cache . --no-optional --global-style true --ignore-scripts %{npm_name}@%{version} || true

# Replace node-gyp with packaged version that uses nodejs-devel headers
rm -rf node_modules/%{npm_name}/node_modules/node-gyp
ln -s %{nodejs_sitelib}/node-gyp node_modules/%{npm_name}/node_modules/

pushd node_modules/%{npm_name}
node scripts/build -f
popd

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cd node_modules/node-sass
cp -pfr CHANGELOG.md LICENSE README.md bin binding.gyp lib package.json scripts src test node_modules vendor %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pf CHANGELOG.md LICENSE README.md ../../

mkdir -p %{buildroot}%{nodejs_sitelib}/${npm_name}/bin
mkdir -p %{buildroot}%{_bindir}/
install -p -D -m0755 bin/node-sass %{buildroot}%{nodejs_sitelib}/%{npm_name}/bin/node-sass
ln -sf %{nodejs_sitelib}/%{npm_name}/bin/node-sass %{buildroot}%{_bindir}/node-sass


%files
%{_bindir}/node-sass
%{nodejs_sitelib}/%{npm_name}
%license LICENSE
%doc CHANGELOG.md
%doc README.md

%changelog
* Fri Mar 03 2017 Dominic Cleal <dominic@cleal.org> 4.5.0-2
- Add runtime dep on gyp, to satisfy symlink (dominic@cleal.org)

* Thu Mar 02 2017 Dominic Cleal <dominic@cleal.org> 4.5.0-1
- new package built with tito

