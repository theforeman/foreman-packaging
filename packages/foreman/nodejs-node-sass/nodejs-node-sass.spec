%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global debug_package %{nil}
%global __debug_install_post /bin/true
%global npm_name node-sass

Name: %{?scl_prefix}nodejs-node-sass
Version: 8.0.0
Release: 1%{?dist}
Summary: Wrapper around libsass
License: MIT
Group: Development/Libraries
URL: https://github.com/sass/node-sass
Source0: https://registry.npmjs.org/@babel/code-frame/-/code-frame-7.23.5.tgz
Source1: https://registry.npmjs.org/@babel/helper-validator-identifier/-/helper-validator-identifier-7.22.20.tgz
Source2: https://registry.npmjs.org/@babel/highlight/-/highlight-7.23.4.tgz
Source3: https://registry.npmjs.org/@gar/promisify/-/promisify-1.1.3.tgz
Source4: https://registry.npmjs.org/@npmcli/fs/-/fs-1.1.1.tgz
Source5: https://registry.npmjs.org/@npmcli/fs/-/fs-2.1.2.tgz
Source6: https://registry.npmjs.org/@npmcli/move-file/-/move-file-1.1.2.tgz
Source7: https://registry.npmjs.org/@npmcli/move-file/-/move-file-2.0.1.tgz
Source8: https://registry.npmjs.org/@tootallnate/once/-/once-1.1.2.tgz
Source9: https://registry.npmjs.org/@tootallnate/once/-/once-2.0.0.tgz
Source10: https://registry.npmjs.org/@types/minimist/-/minimist-1.2.5.tgz
Source11: https://registry.npmjs.org/@types/normalize-package-data/-/normalize-package-data-2.4.4.tgz
Source12: https://registry.npmjs.org/abbrev/-/abbrev-1.1.1.tgz
Source13: https://registry.npmjs.org/agent-base/-/agent-base-6.0.2.tgz
Source14: https://registry.npmjs.org/agentkeepalive/-/agentkeepalive-4.5.0.tgz
Source15: https://registry.npmjs.org/aggregate-error/-/aggregate-error-3.1.0.tgz
Source16: https://registry.npmjs.org/ansi-regex/-/ansi-regex-5.0.1.tgz
Source17: https://registry.npmjs.org/ansi-styles/-/ansi-styles-3.2.1.tgz
Source18: https://registry.npmjs.org/ansi-styles/-/ansi-styles-4.3.0.tgz
Source19: https://registry.npmjs.org/aproba/-/aproba-2.0.0.tgz
Source20: https://registry.npmjs.org/are-we-there-yet/-/are-we-there-yet-3.0.1.tgz
Source21: https://registry.npmjs.org/arrify/-/arrify-1.0.1.tgz
Source22: https://registry.npmjs.org/async-foreach/-/async-foreach-0.1.3.tgz
Source23: https://registry.npmjs.org/balanced-match/-/balanced-match-1.0.2.tgz
Source24: https://registry.npmjs.org/brace-expansion/-/brace-expansion-1.1.11.tgz
Source25: https://registry.npmjs.org/brace-expansion/-/brace-expansion-2.0.1.tgz
Source26: https://registry.npmjs.org/cacache/-/cacache-15.3.0.tgz
Source27: https://registry.npmjs.org/cacache/-/cacache-16.1.3.tgz
Source28: https://registry.npmjs.org/camelcase/-/camelcase-5.3.1.tgz
Source29: https://registry.npmjs.org/camelcase-keys/-/camelcase-keys-6.2.2.tgz
Source30: https://registry.npmjs.org/chalk/-/chalk-2.4.2.tgz
Source31: https://registry.npmjs.org/chalk/-/chalk-4.1.2.tgz
Source32: https://registry.npmjs.org/chownr/-/chownr-2.0.0.tgz
Source33: https://registry.npmjs.org/clean-stack/-/clean-stack-2.2.0.tgz
Source34: https://registry.npmjs.org/cliui/-/cliui-8.0.1.tgz
Source35: https://registry.npmjs.org/color-convert/-/color-convert-1.9.3.tgz
Source36: https://registry.npmjs.org/color-convert/-/color-convert-2.0.1.tgz
Source37: https://registry.npmjs.org/color-name/-/color-name-1.1.3.tgz
Source38: https://registry.npmjs.org/color-name/-/color-name-1.1.4.tgz
Source39: https://registry.npmjs.org/color-support/-/color-support-1.1.3.tgz
Source40: https://registry.npmjs.org/concat-map/-/concat-map-0.0.1.tgz
Source41: https://registry.npmjs.org/console-control-strings/-/console-control-strings-1.1.0.tgz
Source42: https://registry.npmjs.org/core-util-is/-/core-util-is-1.0.3.tgz
Source43: https://registry.npmjs.org/cross-spawn/-/cross-spawn-7.0.3.tgz
Source44: https://registry.npmjs.org/debug/-/debug-4.3.4.tgz
Source45: https://registry.npmjs.org/decamelize/-/decamelize-1.2.0.tgz
Source46: https://registry.npmjs.org/decamelize-keys/-/decamelize-keys-1.1.1.tgz
Source47: https://registry.npmjs.org/delegates/-/delegates-1.0.0.tgz
Source48: https://registry.npmjs.org/emoji-regex/-/emoji-regex-8.0.0.tgz
Source49: https://registry.npmjs.org/encoding/-/encoding-0.1.13.tgz
Source50: https://registry.npmjs.org/env-paths/-/env-paths-2.2.1.tgz
Source51: https://registry.npmjs.org/err-code/-/err-code-2.0.3.tgz
Source52: https://registry.npmjs.org/error-ex/-/error-ex-1.3.2.tgz
Source53: https://registry.npmjs.org/escalade/-/escalade-3.1.1.tgz
Source54: https://registry.npmjs.org/escape-string-regexp/-/escape-string-regexp-1.0.5.tgz
Source55: https://registry.npmjs.org/find-up/-/find-up-4.1.0.tgz
Source56: https://registry.npmjs.org/fs-minipass/-/fs-minipass-2.1.0.tgz
Source57: https://registry.npmjs.org/fs.realpath/-/fs.realpath-1.0.0.tgz
Source58: https://registry.npmjs.org/function-bind/-/function-bind-1.1.2.tgz
Source59: https://registry.npmjs.org/gauge/-/gauge-4.0.4.tgz
Source60: https://registry.npmjs.org/gaze/-/gaze-1.1.3.tgz
Source61: https://registry.npmjs.org/get-caller-file/-/get-caller-file-2.0.5.tgz
Source62: https://registry.npmjs.org/get-stdin/-/get-stdin-4.0.1.tgz
Source63: https://registry.npmjs.org/glob/-/glob-7.1.7.tgz
Source64: https://registry.npmjs.org/glob/-/glob-7.2.3.tgz
Source65: https://registry.npmjs.org/glob/-/glob-8.1.0.tgz
Source66: https://registry.npmjs.org/globule/-/globule-1.3.4.tgz
Source67: https://registry.npmjs.org/graceful-fs/-/graceful-fs-4.2.11.tgz
Source68: https://registry.npmjs.org/hard-rejection/-/hard-rejection-2.1.0.tgz
Source69: https://registry.npmjs.org/has-flag/-/has-flag-3.0.0.tgz
Source70: https://registry.npmjs.org/has-flag/-/has-flag-4.0.0.tgz
Source71: https://registry.npmjs.org/has-unicode/-/has-unicode-2.0.1.tgz
Source72: https://registry.npmjs.org/hasown/-/hasown-2.0.0.tgz
Source73: https://registry.npmjs.org/hosted-git-info/-/hosted-git-info-2.8.9.tgz
Source74: https://registry.npmjs.org/hosted-git-info/-/hosted-git-info-4.1.0.tgz
Source75: https://registry.npmjs.org/http-cache-semantics/-/http-cache-semantics-4.1.1.tgz
Source76: https://registry.npmjs.org/http-proxy-agent/-/http-proxy-agent-4.0.1.tgz
Source77: https://registry.npmjs.org/http-proxy-agent/-/http-proxy-agent-5.0.0.tgz
Source78: https://registry.npmjs.org/https-proxy-agent/-/https-proxy-agent-5.0.1.tgz
Source79: https://registry.npmjs.org/humanize-ms/-/humanize-ms-1.2.1.tgz
Source80: https://registry.npmjs.org/iconv-lite/-/iconv-lite-0.6.3.tgz
Source81: https://registry.npmjs.org/imurmurhash/-/imurmurhash-0.1.4.tgz
Source82: https://registry.npmjs.org/indent-string/-/indent-string-4.0.0.tgz
Source83: https://registry.npmjs.org/infer-owner/-/infer-owner-1.0.4.tgz
Source84: https://registry.npmjs.org/inflight/-/inflight-1.0.6.tgz
Source85: https://registry.npmjs.org/inherits/-/inherits-2.0.4.tgz
Source86: https://registry.npmjs.org/ip/-/ip-2.0.0.tgz
Source87: https://registry.npmjs.org/is-arrayish/-/is-arrayish-0.2.1.tgz
Source88: https://registry.npmjs.org/is-core-module/-/is-core-module-2.13.1.tgz
Source89: https://registry.npmjs.org/is-fullwidth-code-point/-/is-fullwidth-code-point-3.0.0.tgz
Source90: https://registry.npmjs.org/is-lambda/-/is-lambda-1.0.1.tgz
Source91: https://registry.npmjs.org/is-plain-obj/-/is-plain-obj-1.1.0.tgz
Source92: https://registry.npmjs.org/isarray/-/isarray-1.0.0.tgz
Source93: https://registry.npmjs.org/isexe/-/isexe-2.0.0.tgz
Source94: https://registry.npmjs.org/js-base64/-/js-base64-2.6.4.tgz
Source95: https://registry.npmjs.org/js-tokens/-/js-tokens-4.0.0.tgz
Source96: https://registry.npmjs.org/json-parse-even-better-errors/-/json-parse-even-better-errors-2.3.1.tgz
Source97: https://registry.npmjs.org/kind-of/-/kind-of-6.0.3.tgz
Source98: https://registry.npmjs.org/lines-and-columns/-/lines-and-columns-1.2.4.tgz
Source99: https://registry.npmjs.org/locate-path/-/locate-path-5.0.0.tgz
Source100: https://registry.npmjs.org/lodash/-/lodash-4.17.21.tgz
Source101: https://registry.npmjs.org/lru-cache/-/lru-cache-6.0.0.tgz
Source102: https://registry.npmjs.org/lru-cache/-/lru-cache-7.18.3.tgz
Source103: https://registry.npmjs.org/make-fetch-happen/-/make-fetch-happen-10.2.1.tgz
Source104: https://registry.npmjs.org/make-fetch-happen/-/make-fetch-happen-9.1.0.tgz
Source105: https://registry.npmjs.org/map-obj/-/map-obj-1.0.1.tgz
Source106: https://registry.npmjs.org/map-obj/-/map-obj-4.3.0.tgz
Source107: https://registry.npmjs.org/meow/-/meow-9.0.0.tgz
Source108: https://registry.npmjs.org/min-indent/-/min-indent-1.0.1.tgz
Source109: https://registry.npmjs.org/minimatch/-/minimatch-3.0.8.tgz
Source110: https://registry.npmjs.org/minimatch/-/minimatch-3.1.2.tgz
Source111: https://registry.npmjs.org/minimatch/-/minimatch-5.1.6.tgz
Source112: https://registry.npmjs.org/minimist-options/-/minimist-options-4.1.0.tgz
Source113: https://registry.npmjs.org/minipass/-/minipass-3.3.6.tgz
Source114: https://registry.npmjs.org/minipass/-/minipass-5.0.0.tgz
Source115: https://registry.npmjs.org/minipass-collect/-/minipass-collect-1.0.2.tgz
Source116: https://registry.npmjs.org/minipass-fetch/-/minipass-fetch-1.4.1.tgz
Source117: https://registry.npmjs.org/minipass-fetch/-/minipass-fetch-2.1.2.tgz
Source118: https://registry.npmjs.org/minipass-flush/-/minipass-flush-1.0.5.tgz
Source119: https://registry.npmjs.org/minipass-pipeline/-/minipass-pipeline-1.2.4.tgz
Source120: https://registry.npmjs.org/minipass-sized/-/minipass-sized-1.0.3.tgz
Source121: https://registry.npmjs.org/minizlib/-/minizlib-2.1.2.tgz
Source122: https://registry.npmjs.org/mkdirp/-/mkdirp-1.0.4.tgz
Source123: https://registry.npmjs.org/ms/-/ms-2.1.2.tgz
Source124: https://registry.npmjs.org/ms/-/ms-2.1.3.tgz
Source125: https://registry.npmjs.org/nan/-/nan-2.18.0.tgz
Source126: https://registry.npmjs.org/negotiator/-/negotiator-0.6.3.tgz
Source127: https://registry.npmjs.org/node-gyp/-/node-gyp-8.4.1.tgz
Source128: https://registry.npmjs.org/node-sass/-/node-sass-8.0.0.tgz
Source129: https://registry.npmjs.org/nopt/-/nopt-5.0.0.tgz
Source130: https://registry.npmjs.org/normalize-package-data/-/normalize-package-data-2.5.0.tgz
Source131: https://registry.npmjs.org/normalize-package-data/-/normalize-package-data-3.0.3.tgz
Source132: https://registry.npmjs.org/npmlog/-/npmlog-6.0.2.tgz
Source133: https://registry.npmjs.org/once/-/once-1.4.0.tgz
Source134: https://registry.npmjs.org/p-limit/-/p-limit-2.3.0.tgz
Source135: https://registry.npmjs.org/p-locate/-/p-locate-4.1.0.tgz
Source136: https://registry.npmjs.org/p-map/-/p-map-4.0.0.tgz
Source137: https://registry.npmjs.org/p-try/-/p-try-2.2.0.tgz
Source138: https://registry.npmjs.org/parse-json/-/parse-json-5.2.0.tgz
Source139: https://registry.npmjs.org/path-exists/-/path-exists-4.0.0.tgz
Source140: https://registry.npmjs.org/path-is-absolute/-/path-is-absolute-1.0.1.tgz
Source141: https://registry.npmjs.org/path-key/-/path-key-3.1.1.tgz
Source142: https://registry.npmjs.org/path-parse/-/path-parse-1.0.7.tgz
Source143: https://registry.npmjs.org/process-nextick-args/-/process-nextick-args-2.0.1.tgz
Source144: https://registry.npmjs.org/promise-inflight/-/promise-inflight-1.0.1.tgz
Source145: https://registry.npmjs.org/promise-retry/-/promise-retry-2.0.1.tgz
Source146: https://registry.npmjs.org/quick-lru/-/quick-lru-4.0.1.tgz
Source147: https://registry.npmjs.org/read-pkg/-/read-pkg-5.2.0.tgz
Source148: https://registry.npmjs.org/read-pkg-up/-/read-pkg-up-7.0.1.tgz
Source149: https://registry.npmjs.org/readable-stream/-/readable-stream-2.3.8.tgz
Source150: https://registry.npmjs.org/readable-stream/-/readable-stream-3.6.2.tgz
Source151: https://registry.npmjs.org/redent/-/redent-3.0.0.tgz
Source152: https://registry.npmjs.org/require-directory/-/require-directory-2.1.1.tgz
Source153: https://registry.npmjs.org/resolve/-/resolve-1.22.8.tgz
Source154: https://registry.npmjs.org/retry/-/retry-0.12.0.tgz
Source155: https://registry.npmjs.org/rimraf/-/rimraf-3.0.2.tgz
Source156: https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.1.2.tgz
Source157: https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.2.1.tgz
Source158: https://registry.npmjs.org/safer-buffer/-/safer-buffer-2.1.2.tgz
Source159: https://registry.npmjs.org/sass-graph/-/sass-graph-4.0.1.tgz
Source160: https://registry.npmjs.org/scss-tokenizer/-/scss-tokenizer-0.4.3.tgz
Source161: https://registry.npmjs.org/semver/-/semver-5.7.2.tgz
Source162: https://registry.npmjs.org/semver/-/semver-7.5.4.tgz
Source163: https://registry.npmjs.org/set-blocking/-/set-blocking-2.0.0.tgz
Source164: https://registry.npmjs.org/shebang-command/-/shebang-command-2.0.0.tgz
Source165: https://registry.npmjs.org/shebang-regex/-/shebang-regex-3.0.0.tgz
Source166: https://registry.npmjs.org/signal-exit/-/signal-exit-3.0.7.tgz
Source167: https://registry.npmjs.org/smart-buffer/-/smart-buffer-4.2.0.tgz
Source168: https://registry.npmjs.org/socks/-/socks-2.7.1.tgz
Source169: https://registry.npmjs.org/socks-proxy-agent/-/socks-proxy-agent-6.2.1.tgz
Source170: https://registry.npmjs.org/socks-proxy-agent/-/socks-proxy-agent-7.0.0.tgz
Source171: https://registry.npmjs.org/source-map/-/source-map-0.7.4.tgz
Source172: https://registry.npmjs.org/spdx-correct/-/spdx-correct-3.2.0.tgz
Source173: https://registry.npmjs.org/spdx-exceptions/-/spdx-exceptions-2.3.0.tgz
Source174: https://registry.npmjs.org/spdx-expression-parse/-/spdx-expression-parse-3.0.1.tgz
Source175: https://registry.npmjs.org/spdx-license-ids/-/spdx-license-ids-3.0.16.tgz
Source176: https://registry.npmjs.org/ssri/-/ssri-8.0.1.tgz
Source177: https://registry.npmjs.org/ssri/-/ssri-9.0.1.tgz
Source178: https://registry.npmjs.org/stdout-stream/-/stdout-stream-1.4.1.tgz
Source179: https://registry.npmjs.org/string_decoder/-/string_decoder-1.1.1.tgz
Source180: https://registry.npmjs.org/string_decoder/-/string_decoder-1.3.0.tgz
Source181: https://registry.npmjs.org/string-width/-/string-width-4.2.3.tgz
Source182: https://registry.npmjs.org/strip-ansi/-/strip-ansi-6.0.1.tgz
Source183: https://registry.npmjs.org/strip-indent/-/strip-indent-3.0.0.tgz
Source184: https://registry.npmjs.org/supports-color/-/supports-color-5.5.0.tgz
Source185: https://registry.npmjs.org/supports-color/-/supports-color-7.2.0.tgz
Source186: https://registry.npmjs.org/supports-preserve-symlinks-flag/-/supports-preserve-symlinks-flag-1.0.0.tgz
Source187: https://registry.npmjs.org/tar/-/tar-6.2.0.tgz
Source188: https://registry.npmjs.org/trim-newlines/-/trim-newlines-3.0.1.tgz
Source189: https://registry.npmjs.org/true-case-path/-/true-case-path-2.2.1.tgz
Source190: https://registry.npmjs.org/type-fest/-/type-fest-0.18.1.tgz
Source191: https://registry.npmjs.org/type-fest/-/type-fest-0.6.0.tgz
Source192: https://registry.npmjs.org/type-fest/-/type-fest-0.8.1.tgz
Source193: https://registry.npmjs.org/unique-filename/-/unique-filename-1.1.1.tgz
Source194: https://registry.npmjs.org/unique-filename/-/unique-filename-2.0.1.tgz
Source195: https://registry.npmjs.org/unique-slug/-/unique-slug-2.0.2.tgz
Source196: https://registry.npmjs.org/unique-slug/-/unique-slug-3.0.0.tgz
Source197: https://registry.npmjs.org/util-deprecate/-/util-deprecate-1.0.2.tgz
Source198: https://registry.npmjs.org/validate-npm-package-license/-/validate-npm-package-license-3.0.4.tgz
Source199: https://registry.npmjs.org/which/-/which-2.0.2.tgz
Source200: https://registry.npmjs.org/wide-align/-/wide-align-1.1.5.tgz
Source201: https://registry.npmjs.org/wrap-ansi/-/wrap-ansi-7.0.0.tgz
Source202: https://registry.npmjs.org/wrappy/-/wrappy-1.0.2.tgz
Source203: https://registry.npmjs.org/y18n/-/y18n-5.0.8.tgz
Source204: https://registry.npmjs.org/yallist/-/yallist-4.0.0.tgz
Source205: https://registry.npmjs.org/yargs/-/yargs-17.7.2.tgz
Source206: https://registry.npmjs.org/yargs-parser/-/yargs-parser-20.2.9.tgz
Source207: https://registry.npmjs.org/yargs-parser/-/yargs-parser-21.1.1.tgz
Source208: nodejs-node-sass-%{version}-registry.npmjs.org.tgz
BuildRequires: %{?scl_prefix_nodejs}npm
BuildRequires: nodejs-node-gyp
BuildRequires: nodejs-devel
%if 0%{!?scl:1}
BuildRequires: nodejs-packaging
%endif
ExclusiveArch: x86_64

Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}
Provides: bundled(npm(@babel/code-frame)) = 7.23.5
Provides: bundled(npm(@babel/helper-validator-identifier)) = 7.22.20
Provides: bundled(npm(@babel/highlight)) = 7.23.4
Provides: bundled(npm(@gar/promisify)) = 1.1.3
Provides: bundled(npm(@npmcli/fs)) = 1.1.1
Provides: bundled(npm(@npmcli/fs)) = 2.1.2
Provides: bundled(npm(@npmcli/move-file)) = 1.1.2
Provides: bundled(npm(@npmcli/move-file)) = 2.0.1
Provides: bundled(npm(@tootallnate/once)) = 1.1.2
Provides: bundled(npm(@tootallnate/once)) = 2.0.0
Provides: bundled(npm(@types/minimist)) = 1.2.5
Provides: bundled(npm(@types/normalize-package-data)) = 2.4.4
Provides: bundled(npm(abbrev)) = 1.1.1
Provides: bundled(npm(agent-base)) = 6.0.2
Provides: bundled(npm(agentkeepalive)) = 4.5.0
Provides: bundled(npm(aggregate-error)) = 3.1.0
Provides: bundled(npm(ansi-regex)) = 5.0.1
Provides: bundled(npm(ansi-styles)) = 3.2.1
Provides: bundled(npm(ansi-styles)) = 4.3.0
Provides: bundled(npm(aproba)) = 2.0.0
Provides: bundled(npm(are-we-there-yet)) = 3.0.1
Provides: bundled(npm(arrify)) = 1.0.1
Provides: bundled(npm(async-foreach)) = 0.1.3
Provides: bundled(npm(balanced-match)) = 1.0.2
Provides: bundled(npm(brace-expansion)) = 1.1.11
Provides: bundled(npm(brace-expansion)) = 2.0.1
Provides: bundled(npm(cacache)) = 15.3.0
Provides: bundled(npm(cacache)) = 16.1.3
Provides: bundled(npm(camelcase)) = 5.3.1
Provides: bundled(npm(camelcase-keys)) = 6.2.2
Provides: bundled(npm(chalk)) = 2.4.2
Provides: bundled(npm(chalk)) = 4.1.2
Provides: bundled(npm(chownr)) = 2.0.0
Provides: bundled(npm(clean-stack)) = 2.2.0
Provides: bundled(npm(cliui)) = 8.0.1
Provides: bundled(npm(color-convert)) = 1.9.3
Provides: bundled(npm(color-convert)) = 2.0.1
Provides: bundled(npm(color-name)) = 1.1.3
Provides: bundled(npm(color-name)) = 1.1.4
Provides: bundled(npm(color-support)) = 1.1.3
Provides: bundled(npm(concat-map)) = 0.0.1
Provides: bundled(npm(console-control-strings)) = 1.1.0
Provides: bundled(npm(core-util-is)) = 1.0.3
Provides: bundled(npm(cross-spawn)) = 7.0.3
Provides: bundled(npm(debug)) = 4.3.4
Provides: bundled(npm(decamelize)) = 1.2.0
Provides: bundled(npm(decamelize-keys)) = 1.1.1
Provides: bundled(npm(delegates)) = 1.0.0
Provides: bundled(npm(emoji-regex)) = 8.0.0
Provides: bundled(npm(encoding)) = 0.1.13
Provides: bundled(npm(env-paths)) = 2.2.1
Provides: bundled(npm(err-code)) = 2.0.3
Provides: bundled(npm(error-ex)) = 1.3.2
Provides: bundled(npm(escalade)) = 3.1.1
Provides: bundled(npm(escape-string-regexp)) = 1.0.5
Provides: bundled(npm(find-up)) = 4.1.0
Provides: bundled(npm(fs-minipass)) = 2.1.0
Provides: bundled(npm(fs.realpath)) = 1.0.0
Provides: bundled(npm(function-bind)) = 1.1.2
Provides: bundled(npm(gauge)) = 4.0.4
Provides: bundled(npm(gaze)) = 1.1.3
Provides: bundled(npm(get-caller-file)) = 2.0.5
Provides: bundled(npm(get-stdin)) = 4.0.1
Provides: bundled(npm(glob)) = 7.1.7
Provides: bundled(npm(glob)) = 7.2.3
Provides: bundled(npm(glob)) = 8.1.0
Provides: bundled(npm(globule)) = 1.3.4
Provides: bundled(npm(graceful-fs)) = 4.2.11
Provides: bundled(npm(hard-rejection)) = 2.1.0
Provides: bundled(npm(has-flag)) = 3.0.0
Provides: bundled(npm(has-flag)) = 4.0.0
Provides: bundled(npm(has-unicode)) = 2.0.1
Provides: bundled(npm(hasown)) = 2.0.0
Provides: bundled(npm(hosted-git-info)) = 2.8.9
Provides: bundled(npm(hosted-git-info)) = 4.1.0
Provides: bundled(npm(http-cache-semantics)) = 4.1.1
Provides: bundled(npm(http-proxy-agent)) = 4.0.1
Provides: bundled(npm(http-proxy-agent)) = 5.0.0
Provides: bundled(npm(https-proxy-agent)) = 5.0.1
Provides: bundled(npm(humanize-ms)) = 1.2.1
Provides: bundled(npm(iconv-lite)) = 0.6.3
Provides: bundled(npm(imurmurhash)) = 0.1.4
Provides: bundled(npm(indent-string)) = 4.0.0
Provides: bundled(npm(infer-owner)) = 1.0.4
Provides: bundled(npm(inflight)) = 1.0.6
Provides: bundled(npm(inherits)) = 2.0.4
Provides: bundled(npm(ip)) = 2.0.0
Provides: bundled(npm(is-arrayish)) = 0.2.1
Provides: bundled(npm(is-core-module)) = 2.13.1
Provides: bundled(npm(is-fullwidth-code-point)) = 3.0.0
Provides: bundled(npm(is-lambda)) = 1.0.1
Provides: bundled(npm(is-plain-obj)) = 1.1.0
Provides: bundled(npm(isarray)) = 1.0.0
Provides: bundled(npm(isexe)) = 2.0.0
Provides: bundled(npm(js-base64)) = 2.6.4
Provides: bundled(npm(js-tokens)) = 4.0.0
Provides: bundled(npm(json-parse-even-better-errors)) = 2.3.1
Provides: bundled(npm(kind-of)) = 6.0.3
Provides: bundled(npm(lines-and-columns)) = 1.2.4
Provides: bundled(npm(locate-path)) = 5.0.0
Provides: bundled(npm(lodash)) = 4.17.21
Provides: bundled(npm(lru-cache)) = 6.0.0
Provides: bundled(npm(lru-cache)) = 7.18.3
Provides: bundled(npm(make-fetch-happen)) = 10.2.1
Provides: bundled(npm(make-fetch-happen)) = 9.1.0
Provides: bundled(npm(map-obj)) = 1.0.1
Provides: bundled(npm(map-obj)) = 4.3.0
Provides: bundled(npm(meow)) = 9.0.0
Provides: bundled(npm(min-indent)) = 1.0.1
Provides: bundled(npm(minimatch)) = 3.0.8
Provides: bundled(npm(minimatch)) = 3.1.2
Provides: bundled(npm(minimatch)) = 5.1.6
Provides: bundled(npm(minimist-options)) = 4.1.0
Provides: bundled(npm(minipass)) = 3.3.6
Provides: bundled(npm(minipass)) = 5.0.0
Provides: bundled(npm(minipass-collect)) = 1.0.2
Provides: bundled(npm(minipass-fetch)) = 1.4.1
Provides: bundled(npm(minipass-fetch)) = 2.1.2
Provides: bundled(npm(minipass-flush)) = 1.0.5
Provides: bundled(npm(minipass-pipeline)) = 1.2.4
Provides: bundled(npm(minipass-sized)) = 1.0.3
Provides: bundled(npm(minizlib)) = 2.1.2
Provides: bundled(npm(mkdirp)) = 1.0.4
Provides: bundled(npm(ms)) = 2.1.2
Provides: bundled(npm(ms)) = 2.1.3
Provides: bundled(npm(nan)) = 2.18.0
Provides: bundled(npm(negotiator)) = 0.6.3
Provides: bundled(npm(node-gyp)) = 8.4.1
Provides: bundled(npm(node-sass)) = 8.0.0
Provides: bundled(npm(nopt)) = 5.0.0
Provides: bundled(npm(normalize-package-data)) = 2.5.0
Provides: bundled(npm(normalize-package-data)) = 3.0.3
Provides: bundled(npm(npmlog)) = 6.0.2
Provides: bundled(npm(once)) = 1.4.0
Provides: bundled(npm(p-limit)) = 2.3.0
Provides: bundled(npm(p-locate)) = 4.1.0
Provides: bundled(npm(p-map)) = 4.0.0
Provides: bundled(npm(p-try)) = 2.2.0
Provides: bundled(npm(parse-json)) = 5.2.0
Provides: bundled(npm(path-exists)) = 4.0.0
Provides: bundled(npm(path-is-absolute)) = 1.0.1
Provides: bundled(npm(path-key)) = 3.1.1
Provides: bundled(npm(path-parse)) = 1.0.7
Provides: bundled(npm(process-nextick-args)) = 2.0.1
Provides: bundled(npm(promise-inflight)) = 1.0.1
Provides: bundled(npm(promise-retry)) = 2.0.1
Provides: bundled(npm(quick-lru)) = 4.0.1
Provides: bundled(npm(read-pkg)) = 5.2.0
Provides: bundled(npm(read-pkg-up)) = 7.0.1
Provides: bundled(npm(readable-stream)) = 2.3.8
Provides: bundled(npm(readable-stream)) = 3.6.2
Provides: bundled(npm(redent)) = 3.0.0
Provides: bundled(npm(require-directory)) = 2.1.1
Provides: bundled(npm(resolve)) = 1.22.8
Provides: bundled(npm(retry)) = 0.12.0
Provides: bundled(npm(rimraf)) = 3.0.2
Provides: bundled(npm(safe-buffer)) = 5.1.2
Provides: bundled(npm(safe-buffer)) = 5.2.1
Provides: bundled(npm(safer-buffer)) = 2.1.2
Provides: bundled(npm(sass-graph)) = 4.0.1
Provides: bundled(npm(scss-tokenizer)) = 0.4.3
Provides: bundled(npm(semver)) = 5.7.2
Provides: bundled(npm(semver)) = 7.5.4
Provides: bundled(npm(set-blocking)) = 2.0.0
Provides: bundled(npm(shebang-command)) = 2.0.0
Provides: bundled(npm(shebang-regex)) = 3.0.0
Provides: bundled(npm(signal-exit)) = 3.0.7
Provides: bundled(npm(smart-buffer)) = 4.2.0
Provides: bundled(npm(socks)) = 2.7.1
Provides: bundled(npm(socks-proxy-agent)) = 6.2.1
Provides: bundled(npm(socks-proxy-agent)) = 7.0.0
Provides: bundled(npm(source-map)) = 0.7.4
Provides: bundled(npm(spdx-correct)) = 3.2.0
Provides: bundled(npm(spdx-exceptions)) = 2.3.0
Provides: bundled(npm(spdx-expression-parse)) = 3.0.1
Provides: bundled(npm(spdx-license-ids)) = 3.0.16
Provides: bundled(npm(ssri)) = 8.0.1
Provides: bundled(npm(ssri)) = 9.0.1
Provides: bundled(npm(stdout-stream)) = 1.4.1
Provides: bundled(npm(string_decoder)) = 1.1.1
Provides: bundled(npm(string_decoder)) = 1.3.0
Provides: bundled(npm(string-width)) = 4.2.3
Provides: bundled(npm(strip-ansi)) = 6.0.1
Provides: bundled(npm(strip-indent)) = 3.0.0
Provides: bundled(npm(supports-color)) = 5.5.0
Provides: bundled(npm(supports-color)) = 7.2.0
Provides: bundled(npm(supports-preserve-symlinks-flag)) = 1.0.0
Provides: bundled(npm(tar)) = 6.2.0
Provides: bundled(npm(trim-newlines)) = 3.0.1
Provides: bundled(npm(true-case-path)) = 2.2.1
Provides: bundled(npm(type-fest)) = 0.18.1
Provides: bundled(npm(type-fest)) = 0.6.0
Provides: bundled(npm(type-fest)) = 0.8.1
Provides: bundled(npm(unique-filename)) = 1.1.1
Provides: bundled(npm(unique-filename)) = 2.0.1
Provides: bundled(npm(unique-slug)) = 2.0.2
Provides: bundled(npm(unique-slug)) = 3.0.0
Provides: bundled(npm(util-deprecate)) = 1.0.2
Provides: bundled(npm(validate-npm-package-license)) = 3.0.4
Provides: bundled(npm(which)) = 2.0.2
Provides: bundled(npm(wide-align)) = 1.1.5
Provides: bundled(npm(wrap-ansi)) = 7.0.0
Provides: bundled(npm(wrappy)) = 1.0.2
Provides: bundled(npm(y18n)) = 5.0.8
Provides: bundled(npm(yallist)) = 4.0.0
Provides: bundled(npm(yargs)) = 17.7.2
Provides: bundled(npm(yargs-parser)) = 20.2.9
Provides: bundled(npm(yargs-parser)) = 21.1.1
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

%setup -T -q -a 208 -D -n %{npm_cache_dir}

%build
export SKIP_SASS_BINARY_DOWNLOAD_FOR_CI=true

%{?scl:scl enable %{?scl_nodejs} - << \end_of_scl}
npm install --ignore-scripts --cache-min Infinity --cache %{?scl:../}%{npm_cache_dir} --no-shrinkwrap --no-optional --global-style true %{npm_name}@%{version}
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
%doc node_modules/%{npm_name}/README.md

%changelog
* Wed Dec 13 2023 Evgeni Golov 8.0.0-1
- Update to 8.0.0

* Wed Oct 25 2023 Eric D. Helms <ericdhelms@gmail.com> - 4.14.1-3
- Rebuild against NodeJS 14

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
