%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name patternfly-react-extensions

Name: %{?scl_prefix}nodejs-patternfly-react-extensions
Version: 3.0.15
Release: 1%{?dist}
Summary: This library provides an extended set of React components for use with the PatternFly reference implementation
License: MIT
Group: Development/Libraries
URL: https://github.com/patternfly/patternfly-react/blob/master/packages/patternfly-react-extensions/README.md
Source0: https://registry.npmjs.org/@babel/code-frame/-/code-frame-7.27.1.tgz
Source1: https://registry.npmjs.org/@babel/helper-validator-identifier/-/helper-validator-identifier-7.27.1.tgz
Source2: https://registry.npmjs.org/@babel/runtime/-/runtime-7.27.6.tgz
Source3: https://registry.npmjs.org/@babel/runtime-corejs2/-/runtime-corejs2-7.27.6.tgz
Source4: https://registry.npmjs.org/@commitlint/config-validator/-/config-validator-19.8.1.tgz
Source5: https://registry.npmjs.org/@commitlint/execute-rule/-/execute-rule-19.8.1.tgz
Source6: https://registry.npmjs.org/@commitlint/load/-/load-19.8.1.tgz
Source7: https://registry.npmjs.org/@commitlint/resolve-extends/-/resolve-extends-19.8.1.tgz
Source8: https://registry.npmjs.org/@commitlint/types/-/types-19.8.1.tgz
Source9: https://registry.npmjs.org/@hypnosphi/create-react-context/-/create-react-context-0.3.1.tgz
Source10: https://registry.npmjs.org/@iarna/cli/-/cli-2.2.0.tgz
Source11: https://registry.npmjs.org/@nodelib/fs.scandir/-/fs.scandir-2.1.5.tgz
Source12: https://registry.npmjs.org/@nodelib/fs.stat/-/fs.stat-2.0.5.tgz
Source13: https://registry.npmjs.org/@nodelib/fs.walk/-/fs.walk-1.2.8.tgz
Source14: https://registry.npmjs.org/@octokit/auth-token/-/auth-token-2.5.0.tgz
Source15: https://registry.npmjs.org/@octokit/endpoint/-/endpoint-6.0.12.tgz
Source16: https://registry.npmjs.org/@octokit/openapi-types/-/openapi-types-12.11.0.tgz
Source17: https://registry.npmjs.org/@octokit/plugin-paginate-rest/-/plugin-paginate-rest-1.1.2.tgz
Source18: https://registry.npmjs.org/@octokit/plugin-request-log/-/plugin-request-log-1.0.4.tgz
Source19: https://registry.npmjs.org/@octokit/plugin-rest-endpoint-methods/-/plugin-rest-endpoint-methods-2.4.0.tgz
Source20: https://registry.npmjs.org/@octokit/request/-/request-5.6.3.tgz
Source21: https://registry.npmjs.org/@octokit/request-error/-/request-error-1.2.1.tgz
Source22: https://registry.npmjs.org/@octokit/request-error/-/request-error-2.1.0.tgz
Source23: https://registry.npmjs.org/@octokit/rest/-/rest-16.43.2.tgz
Source24: https://registry.npmjs.org/@octokit/types/-/types-2.16.2.tgz
Source25: https://registry.npmjs.org/@octokit/types/-/types-6.41.0.tgz
Source26: https://registry.npmjs.org/@semantic-release/commit-analyzer/-/commit-analyzer-6.3.3.tgz
Source27: https://registry.npmjs.org/@semantic-release/error/-/error-2.2.0.tgz
Source28: https://registry.npmjs.org/@semantic-release/github/-/github-5.5.8.tgz
Source29: https://registry.npmjs.org/@semantic-release/npm/-/npm-5.3.5.tgz
Source30: https://registry.npmjs.org/@semantic-release/release-notes-generator/-/release-notes-generator-7.3.5.tgz
Source31: https://registry.npmjs.org/@types/c3/-/c3-0.6.4.tgz
Source32: https://registry.npmjs.org/@types/conventional-commits-parser/-/conventional-commits-parser-5.0.1.tgz
Source33: https://registry.npmjs.org/@types/d3/-/d3-4.13.15.tgz
Source34: https://registry.npmjs.org/@types/d3-array/-/d3-array-1.2.12.tgz
Source35: https://registry.npmjs.org/@types/d3-axis/-/d3-axis-1.0.19.tgz
Source36: https://registry.npmjs.org/@types/d3-brush/-/d3-brush-1.1.8.tgz
Source37: https://registry.npmjs.org/@types/d3-chord/-/d3-chord-1.0.14.tgz
Source38: https://registry.npmjs.org/@types/d3-collection/-/d3-collection-1.0.13.tgz
Source39: https://registry.npmjs.org/@types/d3-color/-/d3-color-1.4.5.tgz
Source40: https://registry.npmjs.org/@types/d3-dispatch/-/d3-dispatch-1.0.12.tgz
Source41: https://registry.npmjs.org/@types/d3-drag/-/d3-drag-1.2.8.tgz
Source42: https://registry.npmjs.org/@types/d3-dsv/-/d3-dsv-1.2.8.tgz
Source43: https://registry.npmjs.org/@types/d3-ease/-/d3-ease-1.0.13.tgz
Source44: https://registry.npmjs.org/@types/d3-force/-/d3-force-1.2.7.tgz
Source45: https://registry.npmjs.org/@types/d3-format/-/d3-format-1.4.5.tgz
Source46: https://registry.npmjs.org/@types/d3-geo/-/d3-geo-1.12.7.tgz
Source47: https://registry.npmjs.org/@types/d3-hierarchy/-/d3-hierarchy-1.1.11.tgz
Source48: https://registry.npmjs.org/@types/d3-interpolate/-/d3-interpolate-1.4.5.tgz
Source49: https://registry.npmjs.org/@types/d3-path/-/d3-path-1.0.11.tgz
Source50: https://registry.npmjs.org/@types/d3-polygon/-/d3-polygon-1.0.10.tgz
Source51: https://registry.npmjs.org/@types/d3-quadtree/-/d3-quadtree-1.0.13.tgz
Source52: https://registry.npmjs.org/@types/d3-queue/-/d3-queue-3.0.10.tgz
Source53: https://registry.npmjs.org/@types/d3-random/-/d3-random-1.1.5.tgz
Source54: https://registry.npmjs.org/@types/d3-request/-/d3-request-1.0.9.tgz
Source55: https://registry.npmjs.org/@types/d3-scale/-/d3-scale-1.0.22.tgz
Source56: https://registry.npmjs.org/@types/d3-selection/-/d3-selection-1.4.7.tgz
Source57: https://registry.npmjs.org/@types/d3-shape/-/d3-shape-1.3.12.tgz
Source58: https://registry.npmjs.org/@types/d3-time/-/d3-time-1.1.4.tgz
Source59: https://registry.npmjs.org/@types/d3-time-format/-/d3-time-format-2.3.4.tgz
Source60: https://registry.npmjs.org/@types/d3-timer/-/d3-timer-1.0.12.tgz
Source61: https://registry.npmjs.org/@types/d3-transition/-/d3-transition-1.3.6.tgz
Source62: https://registry.npmjs.org/@types/d3-voronoi/-/d3-voronoi-1.1.12.tgz
Source63: https://registry.npmjs.org/@types/d3-zoom/-/d3-zoom-1.8.7.tgz
Source64: https://registry.npmjs.org/@types/geojson/-/geojson-7946.0.16.tgz
Source65: https://registry.npmjs.org/@types/glob/-/glob-7.2.0.tgz
Source66: https://registry.npmjs.org/@types/minimatch/-/minimatch-5.1.2.tgz
Source67: https://registry.npmjs.org/@types/minimist/-/minimist-1.2.5.tgz
Source68: https://registry.npmjs.org/@types/node/-/node-24.0.2.tgz
Source69: https://registry.npmjs.org/@types/normalize-package-data/-/normalize-package-data-2.4.4.tgz
Source70: https://registry.npmjs.org/@types/react/-/react-19.1.8.tgz
Source71: https://registry.npmjs.org/@types/retry/-/retry-0.12.0.tgz
Source72: https://registry.npmjs.org/abbrev/-/abbrev-1.1.1.tgz
Source73: https://registry.npmjs.org/agent-base/-/agent-base-4.2.1.tgz
Source74: https://registry.npmjs.org/agent-base/-/agent-base-4.3.0.tgz
Source75: https://registry.npmjs.org/agent-base/-/agent-base-5.1.1.tgz
Source76: https://registry.npmjs.org/agentkeepalive/-/agentkeepalive-3.5.3.tgz
Source77: https://registry.npmjs.org/aggregate-error/-/aggregate-error-3.1.0.tgz
Source78: https://registry.npmjs.org/ajv/-/ajv-6.12.6.tgz
Source79: https://registry.npmjs.org/ajv/-/ajv-8.17.1.tgz
Source80: https://registry.npmjs.org/ansi-align/-/ansi-align-2.0.0.tgz
Source81: https://registry.npmjs.org/ansi-escapes/-/ansi-escapes-3.2.0.tgz
Source82: https://registry.npmjs.org/ansi-escapes/-/ansi-escapes-4.3.2.tgz
Source83: https://registry.npmjs.org/ansi-regex/-/ansi-regex-2.1.1.tgz
Source84: https://registry.npmjs.org/ansi-regex/-/ansi-regex-3.0.1.tgz
Source85: https://registry.npmjs.org/ansi-regex/-/ansi-regex-4.1.1.tgz
Source86: https://registry.npmjs.org/ansi-regex/-/ansi-regex-5.0.1.tgz
Source87: https://registry.npmjs.org/ansi-styles/-/ansi-styles-3.2.1.tgz
Source88: https://registry.npmjs.org/ansi-styles/-/ansi-styles-4.3.0.tgz
Source89: https://registry.npmjs.org/ansicolors/-/ansicolors-0.3.2.tgz
Source90: https://registry.npmjs.org/ansistyles/-/ansistyles-0.1.3.tgz
Source91: https://registry.npmjs.org/aproba/-/aproba-1.2.0.tgz
Source92: https://registry.npmjs.org/aproba/-/aproba-2.0.0.tgz
Source93: https://registry.npmjs.org/archy/-/archy-1.0.0.tgz
Source94: https://registry.npmjs.org/are-we-there-yet/-/are-we-there-yet-1.1.7.tgz
Source95: https://registry.npmjs.org/argparse/-/argparse-2.0.1.tgz
Source96: https://registry.npmjs.org/argv-formatter/-/argv-formatter-1.0.0.tgz
Source97: https://registry.npmjs.org/array-buffer-byte-length/-/array-buffer-byte-length-1.0.2.tgz
Source98: https://registry.npmjs.org/array-ify/-/array-ify-1.0.0.tgz
Source99: https://registry.npmjs.org/array-union/-/array-union-2.1.0.tgz
Source100: https://registry.npmjs.org/array.prototype.reduce/-/array.prototype.reduce-1.0.8.tgz
Source101: https://registry.npmjs.org/arraybuffer.prototype.slice/-/arraybuffer.prototype.slice-1.0.4.tgz
Source102: https://registry.npmjs.org/arrify/-/arrify-1.0.1.tgz
Source103: https://registry.npmjs.org/asap/-/asap-2.0.6.tgz
Source104: https://registry.npmjs.org/asn1/-/asn1-0.2.6.tgz
Source105: https://registry.npmjs.org/assert-plus/-/assert-plus-1.0.0.tgz
Source106: https://registry.npmjs.org/async-function/-/async-function-1.0.0.tgz
Source107: https://registry.npmjs.org/asynckit/-/asynckit-0.4.0.tgz
Source108: https://registry.npmjs.org/at-least-node/-/at-least-node-1.0.0.tgz
Source109: https://registry.npmjs.org/atob-lite/-/atob-lite-2.0.0.tgz
Source110: https://registry.npmjs.org/available-typed-arrays/-/available-typed-arrays-1.0.7.tgz
Source111: https://registry.npmjs.org/aws-sign2/-/aws-sign2-0.7.0.tgz
Source112: https://registry.npmjs.org/aws4/-/aws4-1.13.2.tgz
Source113: https://registry.npmjs.org/balanced-match/-/balanced-match-1.0.2.tgz
Source114: https://registry.npmjs.org/base64-js/-/base64-js-1.5.1.tgz
Source115: https://registry.npmjs.org/bcrypt-pbkdf/-/bcrypt-pbkdf-1.0.2.tgz
Source116: https://registry.npmjs.org/before-after-hook/-/before-after-hook-2.2.3.tgz
Source117: https://registry.npmjs.org/bin-links/-/bin-links-1.1.8.tgz
Source118: https://registry.npmjs.org/bl/-/bl-4.1.0.tgz
Source119: https://registry.npmjs.org/bluebird/-/bluebird-3.7.2.tgz
Source120: https://registry.npmjs.org/bootstrap/-/bootstrap-3.4.1.tgz
Source121: https://registry.npmjs.org/bootstrap-datepicker/-/bootstrap-datepicker-1.10.0.tgz
Source122: https://registry.npmjs.org/bootstrap-sass/-/bootstrap-sass-3.4.3.tgz
Source123: https://registry.npmjs.org/bootstrap-select/-/bootstrap-select-1.12.2.tgz
Source124: https://registry.npmjs.org/bootstrap-slider/-/bootstrap-slider-9.10.0.tgz
Source125: https://registry.npmjs.org/bootstrap-slider-without-jquery/-/bootstrap-slider-without-jquery-10.0.0.tgz
Source126: https://registry.npmjs.org/bootstrap-switch/-/bootstrap-switch-3.3.4.tgz
Source127: https://registry.npmjs.org/bootstrap-touchspin/-/bootstrap-touchspin-3.1.1.tgz
Source128: https://registry.npmjs.org/bottleneck/-/bottleneck-2.19.5.tgz
Source129: https://registry.npmjs.org/boxen/-/boxen-1.3.0.tgz
Source130: https://registry.npmjs.org/brace-expansion/-/brace-expansion-1.1.12.tgz
Source131: https://registry.npmjs.org/braces/-/braces-3.0.3.tgz
Source132: https://registry.npmjs.org/breakjs/-/breakjs-1.0.0.tgz
Source133: https://registry.npmjs.org/btoa-lite/-/btoa-lite-1.0.0.tgz
Source134: https://registry.npmjs.org/buffer/-/buffer-5.7.1.tgz
Source135: https://registry.npmjs.org/buffer-from/-/buffer-from-1.1.2.tgz
Source136: https://registry.npmjs.org/builtins/-/builtins-1.0.3.tgz
Source137: https://registry.npmjs.org/byline/-/byline-5.0.0.tgz
Source138: https://registry.npmjs.org/byte-size/-/byte-size-5.0.1.tgz
Source139: https://registry.npmjs.org/c3/-/c3-0.4.24.tgz
Source140: https://registry.npmjs.org/cacache/-/cacache-12.0.4.tgz
Source141: https://registry.npmjs.org/cachedir/-/cachedir-2.3.0.tgz
Source142: https://registry.npmjs.org/call-bind/-/call-bind-1.0.8.tgz
Source143: https://registry.npmjs.org/call-bind-apply-helpers/-/call-bind-apply-helpers-1.0.2.tgz
Source144: https://registry.npmjs.org/call-bound/-/call-bound-1.0.4.tgz
Source145: https://registry.npmjs.org/call-limit/-/call-limit-1.1.1.tgz
Source146: https://registry.npmjs.org/callsites/-/callsites-3.1.0.tgz
Source147: https://registry.npmjs.org/camelcase/-/camelcase-4.1.0.tgz
Source148: https://registry.npmjs.org/camelcase/-/camelcase-5.3.1.tgz
Source149: https://registry.npmjs.org/camelcase-keys/-/camelcase-keys-6.2.2.tgz
Source150: https://registry.npmjs.org/capture-stack-trace/-/capture-stack-trace-1.0.2.tgz
Source151: https://registry.npmjs.org/cardinal/-/cardinal-2.1.1.tgz
Source152: https://registry.npmjs.org/caseless/-/caseless-0.12.0.tgz
Source153: https://registry.npmjs.org/chalk/-/chalk-2.4.2.tgz
Source154: https://registry.npmjs.org/chalk/-/chalk-4.1.2.tgz
Source155: https://registry.npmjs.org/chalk/-/chalk-5.4.1.tgz
Source156: https://registry.npmjs.org/change-emitter/-/change-emitter-0.1.6.tgz
Source157: https://registry.npmjs.org/chardet/-/chardet-0.7.0.tgz
Source158: https://registry.npmjs.org/chownr/-/chownr-1.1.4.tgz
Source159: https://registry.npmjs.org/ci-info/-/ci-info-1.6.0.tgz
Source160: https://registry.npmjs.org/ci-info/-/ci-info-2.0.0.tgz
Source161: https://registry.npmjs.org/cidr-regex/-/cidr-regex-2.0.10.tgz
Source162: https://registry.npmjs.org/classnames/-/classnames-2.5.1.tgz
Source163: https://registry.npmjs.org/clean-stack/-/clean-stack-2.2.0.tgz
Source164: https://registry.npmjs.org/cli-boxes/-/cli-boxes-1.0.0.tgz
Source165: https://registry.npmjs.org/cli-columns/-/cli-columns-3.1.2.tgz
Source166: https://registry.npmjs.org/cli-cursor/-/cli-cursor-3.1.0.tgz
Source167: https://registry.npmjs.org/cli-spinners/-/cli-spinners-2.9.2.tgz
Source168: https://registry.npmjs.org/cli-table/-/cli-table-0.3.11.tgz
Source169: https://registry.npmjs.org/cli-table3/-/cli-table3-0.5.1.tgz
Source170: https://registry.npmjs.org/cli-width/-/cli-width-3.0.0.tgz
Source171: https://registry.npmjs.org/cliui/-/cliui-5.0.0.tgz
Source172: https://registry.npmjs.org/cliui/-/cliui-6.0.0.tgz
Source173: https://registry.npmjs.org/clone/-/clone-1.0.4.tgz
Source174: https://registry.npmjs.org/clsx/-/clsx-1.2.1.tgz
Source175: https://registry.npmjs.org/cmd-shim/-/cmd-shim-3.0.3.tgz
Source176: https://registry.npmjs.org/code-point-at/-/code-point-at-1.1.0.tgz
Source177: https://registry.npmjs.org/color-convert/-/color-convert-1.9.3.tgz
Source178: https://registry.npmjs.org/color-convert/-/color-convert-2.0.1.tgz
Source179: https://registry.npmjs.org/color-name/-/color-name-1.1.3.tgz
Source180: https://registry.npmjs.org/color-name/-/color-name-1.1.4.tgz
Source181: https://registry.npmjs.org/colors/-/colors-1.0.3.tgz
Source182: https://registry.npmjs.org/colors/-/colors-1.4.0.tgz
Source183: https://registry.npmjs.org/columnify/-/columnify-1.5.4.tgz
Source184: https://registry.npmjs.org/combined-stream/-/combined-stream-1.0.8.tgz
Source185: https://registry.npmjs.org/commitizen/-/commitizen-4.3.1.tgz
Source186: https://registry.npmjs.org/compare-func/-/compare-func-2.0.0.tgz
Source187: https://registry.npmjs.org/concat-map/-/concat-map-0.0.1.tgz
Source188: https://registry.npmjs.org/concat-stream/-/concat-stream-1.6.2.tgz
Source189: https://registry.npmjs.org/config-chain/-/config-chain-1.1.13.tgz
Source190: https://registry.npmjs.org/configstore/-/configstore-3.1.5.tgz
Source191: https://registry.npmjs.org/console-control-strings/-/console-control-strings-1.1.0.tgz
Source192: https://registry.npmjs.org/conventional-changelog-angular/-/conventional-changelog-angular-5.0.13.tgz
Source193: https://registry.npmjs.org/conventional-changelog-writer/-/conventional-changelog-writer-4.1.0.tgz
Source194: https://registry.npmjs.org/conventional-commit-types/-/conventional-commit-types-3.0.0.tgz
Source195: https://registry.npmjs.org/conventional-commits-filter/-/conventional-commits-filter-2.0.7.tgz
Source196: https://registry.npmjs.org/conventional-commits-parser/-/conventional-commits-parser-3.2.4.tgz
Source197: https://registry.npmjs.org/copy-concurrently/-/copy-concurrently-1.0.5.tgz
Source198: https://registry.npmjs.org/core-js/-/core-js-2.6.12.tgz
Source199: https://registry.npmjs.org/core-util-is/-/core-util-is-1.0.2.tgz
Source200: https://registry.npmjs.org/core-util-is/-/core-util-is-1.0.3.tgz
Source201: https://registry.npmjs.org/cosmiconfig/-/cosmiconfig-6.0.0.tgz
Source202: https://registry.npmjs.org/cosmiconfig/-/cosmiconfig-9.0.0.tgz
Source203: https://registry.npmjs.org/cosmiconfig-typescript-loader/-/cosmiconfig-typescript-loader-6.1.0.tgz
Source204: https://registry.npmjs.org/create-error-class/-/create-error-class-3.0.2.tgz
Source205: https://registry.npmjs.org/create-react-context/-/create-react-context-0.3.0.tgz
Source206: https://registry.npmjs.org/cross-spawn/-/cross-spawn-5.1.0.tgz
Source207: https://registry.npmjs.org/cross-spawn/-/cross-spawn-6.0.6.tgz
Source208: https://registry.npmjs.org/cross-spawn/-/cross-spawn-7.0.6.tgz
Source209: https://registry.npmjs.org/crypto-random-string/-/crypto-random-string-1.0.0.tgz
Source210: https://registry.npmjs.org/css-element-queries/-/css-element-queries-1.2.3.tgz
Source211: https://registry.npmjs.org/csstype/-/csstype-3.1.3.tgz
Source212: https://registry.npmjs.org/cyclist/-/cyclist-1.0.2.tgz
Source213: https://registry.npmjs.org/cz-conventional-changelog/-/cz-conventional-changelog-3.3.0.tgz
Source214: https://registry.npmjs.org/d3/-/d3-3.5.17.tgz
Source215: https://registry.npmjs.org/dashdash/-/dashdash-1.14.1.tgz
Source216: https://registry.npmjs.org/data-view-buffer/-/data-view-buffer-1.0.2.tgz
Source217: https://registry.npmjs.org/data-view-byte-length/-/data-view-byte-length-1.0.2.tgz
Source218: https://registry.npmjs.org/data-view-byte-offset/-/data-view-byte-offset-1.0.1.tgz
Source219: https://registry.npmjs.org/datatables.net/-/datatables.net-1.13.11.tgz
Source220: https://registry.npmjs.org/datatables.net/-/datatables.net-2.3.2.tgz
Source221: https://registry.npmjs.org/datatables.net-bs/-/datatables.net-bs-2.3.2.tgz
Source222: https://registry.npmjs.org/datatables.net-colreorder/-/datatables.net-colreorder-1.7.2.tgz
Source223: https://registry.npmjs.org/datatables.net-colreorder/-/datatables.net-colreorder-2.1.1.tgz
Source224: https://registry.npmjs.org/datatables.net-colreorder-bs/-/datatables.net-colreorder-bs-1.3.3.tgz
Source225: https://registry.npmjs.org/datatables.net-select/-/datatables.net-select-1.2.7.tgz
Source226: https://registry.npmjs.org/dateformat/-/dateformat-3.0.3.tgz
Source227: https://registry.npmjs.org/debug/-/debug-3.1.0.tgz
Source228: https://registry.npmjs.org/debug/-/debug-3.2.7.tgz
Source229: https://registry.npmjs.org/debug/-/debug-4.4.1.tgz
Source230: https://registry.npmjs.org/debuglog/-/debuglog-1.0.1.tgz
Source231: https://registry.npmjs.org/decamelize/-/decamelize-1.2.0.tgz
Source232: https://registry.npmjs.org/decamelize-keys/-/decamelize-keys-1.1.1.tgz
Source233: https://registry.npmjs.org/decode-uri-component/-/decode-uri-component-0.2.2.tgz
Source234: https://registry.npmjs.org/dedent/-/dedent-0.7.0.tgz
Source235: https://registry.npmjs.org/deep-equal/-/deep-equal-1.1.2.tgz
Source236: https://registry.npmjs.org/deep-extend/-/deep-extend-0.6.0.tgz
Source237: https://registry.npmjs.org/defaults/-/defaults-1.0.4.tgz
Source238: https://registry.npmjs.org/define-data-property/-/define-data-property-1.1.4.tgz
Source239: https://registry.npmjs.org/define-properties/-/define-properties-1.2.1.tgz
Source240: https://registry.npmjs.org/delayed-stream/-/delayed-stream-1.0.0.tgz
Source241: https://registry.npmjs.org/delegates/-/delegates-1.0.0.tgz
Source242: https://registry.npmjs.org/deprecation/-/deprecation-2.3.1.tgz
Source243: https://registry.npmjs.org/detect-file/-/detect-file-1.0.0.tgz
Source244: https://registry.npmjs.org/detect-indent/-/detect-indent-5.0.0.tgz
Source245: https://registry.npmjs.org/detect-indent/-/detect-indent-6.1.0.tgz
Source246: https://registry.npmjs.org/detect-newline/-/detect-newline-2.1.0.tgz
Source247: https://registry.npmjs.org/dezalgo/-/dezalgo-1.0.4.tgz
Source248: https://registry.npmjs.org/diff/-/diff-5.2.0.tgz
Source249: https://registry.npmjs.org/dir-glob/-/dir-glob-3.0.1.tgz
Source250: https://registry.npmjs.org/dom-helpers/-/dom-helpers-3.4.0.tgz
Source251: https://registry.npmjs.org/dom-helpers/-/dom-helpers-5.2.1.tgz
Source252: https://registry.npmjs.org/dot-prop/-/dot-prop-4.2.1.tgz
Source253: https://registry.npmjs.org/dot-prop/-/dot-prop-5.3.0.tgz
Source254: https://registry.npmjs.org/dotenv/-/dotenv-5.0.1.tgz
Source255: https://registry.npmjs.org/drmonty-datatables-colvis/-/drmonty-datatables-colvis-1.1.2.tgz
Source256: https://registry.npmjs.org/dunder-proto/-/dunder-proto-1.0.1.tgz
Source257: https://registry.npmjs.org/duplexer3/-/duplexer3-0.1.5.tgz
Source258: https://registry.npmjs.org/duplexify/-/duplexify-3.7.1.tgz
Source259: https://registry.npmjs.org/ecc-jsbn/-/ecc-jsbn-0.1.2.tgz
Source260: https://registry.npmjs.org/editor/-/editor-1.0.0.tgz
Source261: https://registry.npmjs.org/emoji-regex/-/emoji-regex-7.0.3.tgz
Source262: https://registry.npmjs.org/emoji-regex/-/emoji-regex-8.0.0.tgz
Source263: https://registry.npmjs.org/encoding/-/encoding-0.1.13.tgz
Source264: https://registry.npmjs.org/end-of-stream/-/end-of-stream-1.4.4.tgz
Source265: https://registry.npmjs.org/env-ci/-/env-ci-4.5.2.tgz
Source266: https://registry.npmjs.org/env-paths/-/env-paths-2.2.1.tgz
Source267: https://registry.npmjs.org/eonasdan-bootstrap-datetimepicker/-/eonasdan-bootstrap-datetimepicker-4.17.49.tgz
Source268: https://registry.npmjs.org/err-code/-/err-code-1.1.2.tgz
Source269: https://registry.npmjs.org/errno/-/errno-0.1.8.tgz
Source270: https://registry.npmjs.org/error-ex/-/error-ex-1.3.2.tgz
Source271: https://registry.npmjs.org/es-abstract/-/es-abstract-1.24.0.tgz
Source272: https://registry.npmjs.org/es-array-method-boxes-properly/-/es-array-method-boxes-properly-1.0.0.tgz
Source273: https://registry.npmjs.org/es-define-property/-/es-define-property-1.0.1.tgz
Source274: https://registry.npmjs.org/es-errors/-/es-errors-1.3.0.tgz
Source275: https://registry.npmjs.org/es-object-atoms/-/es-object-atoms-1.1.1.tgz
Source276: https://registry.npmjs.org/es-set-tostringtag/-/es-set-tostringtag-2.1.0.tgz
Source277: https://registry.npmjs.org/es-to-primitive/-/es-to-primitive-1.3.0.tgz
Source278: https://registry.npmjs.org/es6-promise/-/es6-promise-4.2.8.tgz
Source279: https://registry.npmjs.org/es6-promisify/-/es6-promisify-5.0.0.tgz
Source280: https://registry.npmjs.org/escape-string-regexp/-/escape-string-regexp-1.0.5.tgz
Source281: https://registry.npmjs.org/esprima/-/esprima-4.0.1.tgz
Source282: https://registry.npmjs.org/execa/-/execa-0.7.0.tgz
Source283: https://registry.npmjs.org/execa/-/execa-1.0.0.tgz
Source284: https://registry.npmjs.org/execa/-/execa-3.4.0.tgz
Source285: https://registry.npmjs.org/expand-tilde/-/expand-tilde-2.0.2.tgz
Source286: https://registry.npmjs.org/extend/-/extend-3.0.2.tgz
Source287: https://registry.npmjs.org/external-editor/-/external-editor-3.1.0.tgz
Source288: https://registry.npmjs.org/extsprintf/-/extsprintf-1.3.0.tgz
Source289: https://registry.npmjs.org/extsprintf/-/extsprintf-1.4.1.tgz
Source290: https://registry.npmjs.org/fast-deep-equal/-/fast-deep-equal-3.1.3.tgz
Source291: https://registry.npmjs.org/fast-glob/-/fast-glob-3.3.3.tgz
Source292: https://registry.npmjs.org/fast-json-stable-stringify/-/fast-json-stable-stringify-2.1.0.tgz
Source293: https://registry.npmjs.org/fast-uri/-/fast-uri-3.0.6.tgz
Source294: https://registry.npmjs.org/fastq/-/fastq-1.19.1.tgz
Source295: https://registry.npmjs.org/figgy-pudding/-/figgy-pudding-3.5.2.tgz
Source296: https://registry.npmjs.org/figures/-/figures-2.0.0.tgz
Source297: https://registry.npmjs.org/figures/-/figures-3.2.0.tgz
Source298: https://registry.npmjs.org/fill-range/-/fill-range-7.1.1.tgz
Source299: https://registry.npmjs.org/filter-obj/-/filter-obj-1.1.0.tgz
Source300: https://registry.npmjs.org/find-node-modules/-/find-node-modules-2.1.3.tgz
Source301: https://registry.npmjs.org/find-npm-prefix/-/find-npm-prefix-1.0.2.tgz
Source302: https://registry.npmjs.org/find-root/-/find-root-1.1.0.tgz
Source303: https://registry.npmjs.org/find-up/-/find-up-2.1.0.tgz
Source304: https://registry.npmjs.org/find-up/-/find-up-3.0.0.tgz
Source305: https://registry.npmjs.org/find-up/-/find-up-4.1.0.tgz
Source306: https://registry.npmjs.org/find-versions/-/find-versions-3.2.0.tgz
Source307: https://registry.npmjs.org/findup-sync/-/findup-sync-4.0.0.tgz
Source308: https://registry.npmjs.org/flush-write-stream/-/flush-write-stream-1.1.1.tgz
Source309: https://registry.npmjs.org/font-awesome/-/font-awesome-4.7.0.tgz
Source310: https://registry.npmjs.org/font-awesome-sass/-/font-awesome-sass-4.7.0.tgz
Source311: https://registry.npmjs.org/for-each/-/for-each-0.3.5.tgz
Source312: https://registry.npmjs.org/forever-agent/-/forever-agent-0.6.1.tgz
Source313: https://registry.npmjs.org/form-data/-/form-data-2.3.3.tgz
Source314: https://registry.npmjs.org/from2/-/from2-1.3.0.tgz
Source315: https://registry.npmjs.org/from2/-/from2-2.3.0.tgz
Source316: https://registry.npmjs.org/fs-extra/-/fs-extra-8.1.0.tgz
Source317: https://registry.npmjs.org/fs-extra/-/fs-extra-9.1.0.tgz
Source318: https://registry.npmjs.org/fs-minipass/-/fs-minipass-1.2.7.tgz
Source319: https://registry.npmjs.org/fs-vacuum/-/fs-vacuum-1.2.10.tgz
Source320: https://registry.npmjs.org/fs-write-stream-atomic/-/fs-write-stream-atomic-1.0.10.tgz
Source321: https://registry.npmjs.org/fs.realpath/-/fs.realpath-1.0.0.tgz
Source322: https://registry.npmjs.org/function-bind/-/function-bind-1.1.2.tgz
Source323: https://registry.npmjs.org/function.prototype.name/-/function.prototype.name-1.1.8.tgz
Source324: https://registry.npmjs.org/functions-have-names/-/functions-have-names-1.2.3.tgz
Source325: https://registry.npmjs.org/gauge/-/gauge-2.7.4.tgz
Source326: https://registry.npmjs.org/genfun/-/genfun-5.0.0.tgz
Source327: https://registry.npmjs.org/gentle-fs/-/gentle-fs-2.3.1.tgz
Source328: https://registry.npmjs.org/get-caller-file/-/get-caller-file-2.0.5.tgz
Source329: https://registry.npmjs.org/get-intrinsic/-/get-intrinsic-1.3.0.tgz
Source330: https://registry.npmjs.org/get-proto/-/get-proto-1.0.1.tgz
Source331: https://registry.npmjs.org/get-stream/-/get-stream-3.0.0.tgz
Source332: https://registry.npmjs.org/get-stream/-/get-stream-4.1.0.tgz
Source333: https://registry.npmjs.org/get-stream/-/get-stream-5.2.0.tgz
Source334: https://registry.npmjs.org/get-symbol-description/-/get-symbol-description-1.1.0.tgz
Source335: https://registry.npmjs.org/getpass/-/getpass-0.1.7.tgz
Source336: https://registry.npmjs.org/git-log-parser/-/git-log-parser-1.2.1.tgz
Source337: https://registry.npmjs.org/gitdiff-parser/-/gitdiff-parser-0.1.2.tgz
Source338: https://registry.npmjs.org/glob/-/glob-7.2.3.tgz
Source339: https://registry.npmjs.org/glob-parent/-/glob-parent-5.1.2.tgz
Source340: https://registry.npmjs.org/global-directory/-/global-directory-4.0.1.tgz
Source341: https://registry.npmjs.org/global-dirs/-/global-dirs-0.1.1.tgz
Source342: https://registry.npmjs.org/global-modules/-/global-modules-1.0.0.tgz
Source343: https://registry.npmjs.org/global-prefix/-/global-prefix-1.0.2.tgz
Source344: https://registry.npmjs.org/globalthis/-/globalthis-1.0.4.tgz
Source345: https://registry.npmjs.org/globby/-/globby-10.0.2.tgz
Source346: https://registry.npmjs.org/google-code-prettify/-/google-code-prettify-1.0.5.tgz
Source347: https://registry.npmjs.org/gopd/-/gopd-1.2.0.tgz
Source348: https://registry.npmjs.org/got/-/got-6.7.1.tgz
Source349: https://registry.npmjs.org/graceful-fs/-/graceful-fs-4.2.11.tgz
Source350: https://registry.npmjs.org/gud/-/gud-1.0.0.tgz
Source351: https://registry.npmjs.org/handlebars/-/handlebars-4.7.8.tgz
Source352: https://registry.npmjs.org/har-schema/-/har-schema-2.0.0.tgz
Source353: https://registry.npmjs.org/har-validator/-/har-validator-5.1.5.tgz
Source354: https://registry.npmjs.org/hard-rejection/-/hard-rejection-2.1.0.tgz
Source355: https://registry.npmjs.org/has-bigints/-/has-bigints-1.1.0.tgz
Source356: https://registry.npmjs.org/has-flag/-/has-flag-2.0.0.tgz
Source357: https://registry.npmjs.org/has-flag/-/has-flag-3.0.0.tgz
Source358: https://registry.npmjs.org/has-flag/-/has-flag-4.0.0.tgz
Source359: https://registry.npmjs.org/has-property-descriptors/-/has-property-descriptors-1.0.2.tgz
Source360: https://registry.npmjs.org/has-proto/-/has-proto-1.2.0.tgz
Source361: https://registry.npmjs.org/has-symbols/-/has-symbols-1.1.0.tgz
Source362: https://registry.npmjs.org/has-tostringtag/-/has-tostringtag-1.0.2.tgz
Source363: https://registry.npmjs.org/has-unicode/-/has-unicode-2.0.1.tgz
Source364: https://registry.npmjs.org/hasown/-/hasown-2.0.2.tgz
Source365: https://registry.npmjs.org/hoist-non-react-statics/-/hoist-non-react-statics-2.5.5.tgz
Source366: https://registry.npmjs.org/homedir-polyfill/-/homedir-polyfill-1.0.3.tgz
Source367: https://registry.npmjs.org/hook-std/-/hook-std-2.0.0.tgz
Source368: https://registry.npmjs.org/hosted-git-info/-/hosted-git-info-2.8.9.tgz
Source369: https://registry.npmjs.org/hosted-git-info/-/hosted-git-info-3.0.8.tgz
Source370: https://registry.npmjs.org/hosted-git-info/-/hosted-git-info-4.1.0.tgz
Source371: https://registry.npmjs.org/http-cache-semantics/-/http-cache-semantics-3.8.1.tgz
Source372: https://registry.npmjs.org/http-proxy-agent/-/http-proxy-agent-2.1.0.tgz
Source373: https://registry.npmjs.org/http-proxy-agent/-/http-proxy-agent-3.0.0.tgz
Source374: https://registry.npmjs.org/http-signature/-/http-signature-1.2.0.tgz
Source375: https://registry.npmjs.org/https-proxy-agent/-/https-proxy-agent-2.2.4.tgz
Source376: https://registry.npmjs.org/https-proxy-agent/-/https-proxy-agent-4.0.0.tgz
Source377: https://registry.npmjs.org/human-signals/-/human-signals-1.1.1.tgz
Source378: https://registry.npmjs.org/humanize-ms/-/humanize-ms-1.2.1.tgz
Source379: https://registry.npmjs.org/iconv-lite/-/iconv-lite-0.4.24.tgz
Source380: https://registry.npmjs.org/iconv-lite/-/iconv-lite-0.6.3.tgz
Source381: https://registry.npmjs.org/ieee754/-/ieee754-1.2.1.tgz
Source382: https://registry.npmjs.org/iferr/-/iferr-0.1.5.tgz
Source383: https://registry.npmjs.org/iferr/-/iferr-1.0.2.tgz
Source384: https://registry.npmjs.org/ignore/-/ignore-5.3.2.tgz
Source385: https://registry.npmjs.org/ignore-walk/-/ignore-walk-3.0.4.tgz
Source386: https://registry.npmjs.org/import-fresh/-/import-fresh-3.3.1.tgz
Source387: https://registry.npmjs.org/import-from/-/import-from-3.0.0.tgz
Source388: https://registry.npmjs.org/import-lazy/-/import-lazy-2.1.0.tgz
Source389: https://registry.npmjs.org/import-meta-resolve/-/import-meta-resolve-4.1.0.tgz
Source390: https://registry.npmjs.org/imurmurhash/-/imurmurhash-0.1.4.tgz
Source391: https://registry.npmjs.org/indent-string/-/indent-string-4.0.0.tgz
Source392: https://registry.npmjs.org/infer-owner/-/infer-owner-1.0.4.tgz
Source393: https://registry.npmjs.org/inflight/-/inflight-1.0.6.tgz
Source394: https://registry.npmjs.org/inherits/-/inherits-2.0.4.tgz
Source395: https://registry.npmjs.org/ini/-/ini-1.3.8.tgz
Source396: https://registry.npmjs.org/ini/-/ini-4.1.1.tgz
Source397: https://registry.npmjs.org/init-package-json/-/init-package-json-1.10.3.tgz
Source398: https://registry.npmjs.org/inquirer/-/inquirer-8.2.5.tgz
Source399: https://registry.npmjs.org/internal-slot/-/internal-slot-1.1.0.tgz
Source400: https://registry.npmjs.org/into-stream/-/into-stream-5.1.1.tgz
Source401: https://registry.npmjs.org/invariant/-/invariant-2.2.4.tgz
Source402: https://registry.npmjs.org/ip/-/ip-1.1.5.tgz
Source403: https://registry.npmjs.org/ip-regex/-/ip-regex-2.1.0.tgz
Source404: https://registry.npmjs.org/is-arguments/-/is-arguments-1.2.0.tgz
Source405: https://registry.npmjs.org/is-array-buffer/-/is-array-buffer-3.0.5.tgz
Source406: https://registry.npmjs.org/is-arrayish/-/is-arrayish-0.2.1.tgz
Source407: https://registry.npmjs.org/is-async-function/-/is-async-function-2.1.1.tgz
Source408: https://registry.npmjs.org/is-bigint/-/is-bigint-1.1.0.tgz
Source409: https://registry.npmjs.org/is-boolean-object/-/is-boolean-object-1.2.2.tgz
Source410: https://registry.npmjs.org/is-callable/-/is-callable-1.2.7.tgz
Source411: https://registry.npmjs.org/is-ci/-/is-ci-1.2.1.tgz
Source412: https://registry.npmjs.org/is-cidr/-/is-cidr-3.1.1.tgz
Source413: https://registry.npmjs.org/is-core-module/-/is-core-module-2.16.1.tgz
Source414: https://registry.npmjs.org/is-data-view/-/is-data-view-1.0.2.tgz
Source415: https://registry.npmjs.org/is-date-object/-/is-date-object-1.1.0.tgz
Source416: https://registry.npmjs.org/is-extglob/-/is-extglob-2.1.1.tgz
Source417: https://registry.npmjs.org/is-finalizationregistry/-/is-finalizationregistry-1.1.1.tgz
Source418: https://registry.npmjs.org/is-fullwidth-code-point/-/is-fullwidth-code-point-1.0.0.tgz
Source419: https://registry.npmjs.org/is-fullwidth-code-point/-/is-fullwidth-code-point-2.0.0.tgz
Source420: https://registry.npmjs.org/is-fullwidth-code-point/-/is-fullwidth-code-point-3.0.0.tgz
Source421: https://registry.npmjs.org/is-generator-function/-/is-generator-function-1.1.0.tgz
Source422: https://registry.npmjs.org/is-glob/-/is-glob-4.0.3.tgz
Source423: https://registry.npmjs.org/is-installed-globally/-/is-installed-globally-0.1.0.tgz
Source424: https://registry.npmjs.org/is-interactive/-/is-interactive-1.0.0.tgz
Source425: https://registry.npmjs.org/is-map/-/is-map-2.0.3.tgz
Source426: https://registry.npmjs.org/is-negative-zero/-/is-negative-zero-2.0.3.tgz
Source427: https://registry.npmjs.org/is-npm/-/is-npm-1.0.0.tgz
Source428: https://registry.npmjs.org/is-number/-/is-number-7.0.0.tgz
Source429: https://registry.npmjs.org/is-number-object/-/is-number-object-1.1.1.tgz
Source430: https://registry.npmjs.org/is-obj/-/is-obj-1.0.1.tgz
Source431: https://registry.npmjs.org/is-obj/-/is-obj-2.0.0.tgz
Source432: https://registry.npmjs.org/is-path-inside/-/is-path-inside-1.0.1.tgz
Source433: https://registry.npmjs.org/is-plain-obj/-/is-plain-obj-1.1.0.tgz
Source434: https://registry.npmjs.org/is-plain-object/-/is-plain-object-5.0.0.tgz
Source435: https://registry.npmjs.org/is-redirect/-/is-redirect-1.0.0.tgz
Source436: https://registry.npmjs.org/is-regex/-/is-regex-1.2.1.tgz
Source437: https://registry.npmjs.org/is-retry-allowed/-/is-retry-allowed-1.2.0.tgz
Source438: https://registry.npmjs.org/is-set/-/is-set-2.0.3.tgz
Source439: https://registry.npmjs.org/is-shared-array-buffer/-/is-shared-array-buffer-1.0.4.tgz
Source440: https://registry.npmjs.org/is-stream/-/is-stream-1.1.0.tgz
Source441: https://registry.npmjs.org/is-stream/-/is-stream-2.0.1.tgz
Source442: https://registry.npmjs.org/is-string/-/is-string-1.1.1.tgz
Source443: https://registry.npmjs.org/is-symbol/-/is-symbol-1.1.1.tgz
Source444: https://registry.npmjs.org/is-text-path/-/is-text-path-1.0.1.tgz
Source445: https://registry.npmjs.org/is-typed-array/-/is-typed-array-1.1.15.tgz
Source446: https://registry.npmjs.org/is-typedarray/-/is-typedarray-1.0.0.tgz
Source447: https://registry.npmjs.org/is-unicode-supported/-/is-unicode-supported-0.1.0.tgz
Source448: https://registry.npmjs.org/is-utf8/-/is-utf8-0.2.1.tgz
Source449: https://registry.npmjs.org/is-weakmap/-/is-weakmap-2.0.2.tgz
Source450: https://registry.npmjs.org/is-weakref/-/is-weakref-1.1.1.tgz
Source451: https://registry.npmjs.org/is-weakset/-/is-weakset-2.0.4.tgz
Source452: https://registry.npmjs.org/is-windows/-/is-windows-1.0.2.tgz
Source453: https://registry.npmjs.org/isarray/-/isarray-0.0.1.tgz
Source454: https://registry.npmjs.org/isarray/-/isarray-1.0.0.tgz
Source455: https://registry.npmjs.org/isarray/-/isarray-2.0.5.tgz
Source456: https://registry.npmjs.org/isexe/-/isexe-2.0.0.tgz
Source457: https://registry.npmjs.org/isstream/-/isstream-0.1.2.tgz
Source458: https://registry.npmjs.org/issue-parser/-/issue-parser-5.0.0.tgz
Source459: https://registry.npmjs.org/java-properties/-/java-properties-1.0.2.tgz
Source460: https://registry.npmjs.org/jiti/-/jiti-2.4.2.tgz
Source461: https://registry.npmjs.org/jquery/-/jquery-3.4.1.tgz
Source462: https://registry.npmjs.org/jquery/-/jquery-3.7.1.tgz
Source463: https://registry.npmjs.org/jquery-match-height/-/jquery-match-height-0.7.2.tgz
Source464: https://registry.npmjs.org/js-tokens/-/js-tokens-4.0.0.tgz
Source465: https://registry.npmjs.org/js-yaml/-/js-yaml-4.1.0.tgz
Source466: https://registry.npmjs.org/jsbn/-/jsbn-0.1.1.tgz
Source467: https://registry.npmjs.org/json-parse-better-errors/-/json-parse-better-errors-1.0.2.tgz
Source468: https://registry.npmjs.org/json-parse-even-better-errors/-/json-parse-even-better-errors-2.3.1.tgz
Source469: https://registry.npmjs.org/json-schema/-/json-schema-0.4.0.tgz
Source470: https://registry.npmjs.org/json-schema-traverse/-/json-schema-traverse-0.4.1.tgz
Source471: https://registry.npmjs.org/json-schema-traverse/-/json-schema-traverse-1.0.0.tgz
Source472: https://registry.npmjs.org/json-stringify-safe/-/json-stringify-safe-5.0.1.tgz
Source473: https://registry.npmjs.org/jsonfile/-/jsonfile-4.0.0.tgz
Source474: https://registry.npmjs.org/jsonfile/-/jsonfile-6.1.0.tgz
Source475: https://registry.npmjs.org/jsonparse/-/jsonparse-1.3.1.tgz
Source476: https://registry.npmjs.org/JSONStream/-/JSONStream-1.3.5.tgz
Source477: https://registry.npmjs.org/jsprim/-/jsprim-1.4.2.tgz
Source478: https://registry.npmjs.org/keycode/-/keycode-2.2.1.tgz
Source479: https://registry.npmjs.org/kind-of/-/kind-of-6.0.3.tgz
Source480: https://registry.npmjs.org/latest-version/-/latest-version-3.1.0.tgz
Source481: https://registry.npmjs.org/lazy-property/-/lazy-property-1.0.0.tgz
Source482: https://registry.npmjs.org/leven/-/leven-2.1.0.tgz
Source483: https://registry.npmjs.org/libcipm/-/libcipm-4.0.8.tgz
Source484: https://registry.npmjs.org/libnpm/-/libnpm-3.0.1.tgz
Source485: https://registry.npmjs.org/libnpmaccess/-/libnpmaccess-3.0.2.tgz
Source486: https://registry.npmjs.org/libnpmconfig/-/libnpmconfig-1.2.1.tgz
Source487: https://registry.npmjs.org/libnpmhook/-/libnpmhook-5.0.3.tgz
Source488: https://registry.npmjs.org/libnpmorg/-/libnpmorg-1.0.1.tgz
Source489: https://registry.npmjs.org/libnpmpublish/-/libnpmpublish-1.1.3.tgz
Source490: https://registry.npmjs.org/libnpmsearch/-/libnpmsearch-2.0.2.tgz
Source491: https://registry.npmjs.org/libnpmteam/-/libnpmteam-1.0.2.tgz
Source492: https://registry.npmjs.org/libnpx/-/libnpx-10.2.4.tgz
Source493: https://registry.npmjs.org/lines-and-columns/-/lines-and-columns-1.2.4.tgz
Source494: https://registry.npmjs.org/load-json-file/-/load-json-file-4.0.0.tgz
Source495: https://registry.npmjs.org/locate-path/-/locate-path-2.0.0.tgz
Source496: https://registry.npmjs.org/locate-path/-/locate-path-3.0.0.tgz
Source497: https://registry.npmjs.org/locate-path/-/locate-path-5.0.0.tgz
Source498: https://registry.npmjs.org/lock-verify/-/lock-verify-2.2.2.tgz
Source499: https://registry.npmjs.org/lockfile/-/lockfile-1.0.4.tgz
Source500: https://registry.npmjs.org/lodash/-/lodash-4.17.21.tgz
Source501: https://registry.npmjs.org/lodash._baseindexof/-/lodash._baseindexof-3.1.0.tgz
Source502: https://registry.npmjs.org/lodash._baseuniq/-/lodash._baseuniq-4.6.0.tgz
Source503: https://registry.npmjs.org/lodash._bindcallback/-/lodash._bindcallback-3.0.1.tgz
Source504: https://registry.npmjs.org/lodash._cacheindexof/-/lodash._cacheindexof-3.0.2.tgz
Source505: https://registry.npmjs.org/lodash._createcache/-/lodash._createcache-3.1.2.tgz
Source506: https://registry.npmjs.org/lodash._createset/-/lodash._createset-4.0.3.tgz
Source507: https://registry.npmjs.org/lodash._getnative/-/lodash._getnative-3.9.1.tgz
Source508: https://registry.npmjs.org/lodash._root/-/lodash._root-3.0.1.tgz
Source509: https://registry.npmjs.org/lodash.capitalize/-/lodash.capitalize-4.2.1.tgz
Source510: https://registry.npmjs.org/lodash.clonedeep/-/lodash.clonedeep-4.5.0.tgz
Source511: https://registry.npmjs.org/lodash.debounce/-/lodash.debounce-4.0.8.tgz
Source512: https://registry.npmjs.org/lodash.escape/-/lodash.escape-4.0.1.tgz
Source513: https://registry.npmjs.org/lodash.escaperegexp/-/lodash.escaperegexp-4.1.2.tgz
Source514: https://registry.npmjs.org/lodash.findlastindex/-/lodash.findlastindex-4.6.0.tgz
Source515: https://registry.npmjs.org/lodash.get/-/lodash.get-4.4.2.tgz
Source516: https://registry.npmjs.org/lodash.ismatch/-/lodash.ismatch-4.4.0.tgz
Source517: https://registry.npmjs.org/lodash.isplainobject/-/lodash.isplainobject-4.0.6.tgz
Source518: https://registry.npmjs.org/lodash.isstring/-/lodash.isstring-4.0.1.tgz
Source519: https://registry.npmjs.org/lodash.map/-/lodash.map-4.6.0.tgz
Source520: https://registry.npmjs.org/lodash.mapvalues/-/lodash.mapvalues-4.6.0.tgz
Source521: https://registry.npmjs.org/lodash.merge/-/lodash.merge-4.6.2.tgz
Source522: https://registry.npmjs.org/lodash.mergewith/-/lodash.mergewith-4.6.2.tgz
Source523: https://registry.npmjs.org/lodash.restparam/-/lodash.restparam-3.6.1.tgz
Source524: https://registry.npmjs.org/lodash.set/-/lodash.set-4.3.2.tgz
Source525: https://registry.npmjs.org/lodash.union/-/lodash.union-4.6.0.tgz
Source526: https://registry.npmjs.org/lodash.uniq/-/lodash.uniq-4.5.0.tgz
Source527: https://registry.npmjs.org/lodash.uniqby/-/lodash.uniqby-4.7.0.tgz
Source528: https://registry.npmjs.org/lodash.without/-/lodash.without-4.4.0.tgz
Source529: https://registry.npmjs.org/log-symbols/-/log-symbols-4.1.0.tgz
Source530: https://registry.npmjs.org/longest/-/longest-2.0.1.tgz
Source531: https://registry.npmjs.org/loose-envify/-/loose-envify-1.4.0.tgz
Source532: https://registry.npmjs.org/lowercase-keys/-/lowercase-keys-1.0.1.tgz
Source533: https://registry.npmjs.org/lru-cache/-/lru-cache-4.1.5.tgz
Source534: https://registry.npmjs.org/lru-cache/-/lru-cache-5.1.1.tgz
Source535: https://registry.npmjs.org/lru-cache/-/lru-cache-6.0.0.tgz
Source536: https://registry.npmjs.org/macos-release/-/macos-release-2.5.1.tgz
Source537: https://registry.npmjs.org/make-dir/-/make-dir-1.3.0.tgz
Source538: https://registry.npmjs.org/make-fetch-happen/-/make-fetch-happen-5.0.2.tgz
Source539: https://registry.npmjs.org/map-obj/-/map-obj-1.0.1.tgz
Source540: https://registry.npmjs.org/map-obj/-/map-obj-4.3.0.tgz
Source541: https://registry.npmjs.org/marked/-/marked-0.7.0.tgz
Source542: https://registry.npmjs.org/marked-terminal/-/marked-terminal-3.3.0.tgz
Source543: https://registry.npmjs.org/math-intrinsics/-/math-intrinsics-1.1.0.tgz
Source544: https://registry.npmjs.org/meant/-/meant-1.0.3.tgz
Source545: https://registry.npmjs.org/meow/-/meow-8.1.2.tgz
Source546: https://registry.npmjs.org/merge/-/merge-2.1.1.tgz
Source547: https://registry.npmjs.org/merge-stream/-/merge-stream-2.0.0.tgz
Source548: https://registry.npmjs.org/merge2/-/merge2-1.4.1.tgz
Source549: https://registry.npmjs.org/micromatch/-/micromatch-4.0.8.tgz
Source550: https://registry.npmjs.org/mime/-/mime-2.6.0.tgz
Source551: https://registry.npmjs.org/mime-db/-/mime-db-1.52.0.tgz
Source552: https://registry.npmjs.org/mime-types/-/mime-types-2.1.35.tgz
Source553: https://registry.npmjs.org/mimic-fn/-/mimic-fn-2.1.0.tgz
Source554: https://registry.npmjs.org/min-indent/-/min-indent-1.0.1.tgz
Source555: https://registry.npmjs.org/minimatch/-/minimatch-3.1.2.tgz
Source556: https://registry.npmjs.org/minimist/-/minimist-1.2.7.tgz
Source557: https://registry.npmjs.org/minimist/-/minimist-1.2.8.tgz
Source558: https://registry.npmjs.org/minimist-options/-/minimist-options-4.1.0.tgz
Source559: https://registry.npmjs.org/minipass/-/minipass-2.9.0.tgz
Source560: https://registry.npmjs.org/minizlib/-/minizlib-1.3.3.tgz
Source561: https://registry.npmjs.org/mississippi/-/mississippi-3.0.0.tgz
Source562: https://registry.npmjs.org/mkdirp/-/mkdirp-0.5.6.tgz
Source563: https://registry.npmjs.org/modify-values/-/modify-values-1.0.1.tgz
Source564: https://registry.npmjs.org/moment/-/moment-2.30.1.tgz
Source565: https://registry.npmjs.org/moment-timezone/-/moment-timezone-0.4.1.tgz
Source566: https://registry.npmjs.org/move-concurrently/-/move-concurrently-1.0.1.tgz
Source567: https://registry.npmjs.org/ms/-/ms-2.0.0.tgz
Source568: https://registry.npmjs.org/ms/-/ms-2.1.3.tgz
Source569: https://registry.npmjs.org/mute-stream/-/mute-stream-0.0.8.tgz
Source570: https://registry.npmjs.org/neo-async/-/neo-async-2.6.2.tgz
Source571: https://registry.npmjs.org/nerf-dart/-/nerf-dart-1.0.0.tgz
Source572: https://registry.npmjs.org/nice-try/-/nice-try-1.0.5.tgz
Source573: https://registry.npmjs.org/node-emoji/-/node-emoji-1.11.0.tgz
Source574: https://registry.npmjs.org/node-fetch/-/node-fetch-2.7.0.tgz
Source575: https://registry.npmjs.org/node-fetch-npm/-/node-fetch-npm-2.0.4.tgz
Source576: https://registry.npmjs.org/node-gyp/-/node-gyp-5.1.1.tgz
Source577: https://registry.npmjs.org/nopt/-/nopt-4.0.3.tgz
Source578: https://registry.npmjs.org/normalize-package-data/-/normalize-package-data-2.5.0.tgz
Source579: https://registry.npmjs.org/normalize-package-data/-/normalize-package-data-3.0.3.tgz
Source580: https://registry.npmjs.org/normalize-url/-/normalize-url-4.5.1.tgz
Source581: https://registry.npmjs.org/npm/-/npm-6.14.18.tgz
Source582: https://registry.npmjs.org/npm-audit-report/-/npm-audit-report-1.3.3.tgz
Source583: https://registry.npmjs.org/npm-bundled/-/npm-bundled-1.1.2.tgz
Source584: https://registry.npmjs.org/npm-cache-filename/-/npm-cache-filename-1.0.2.tgz
Source585: https://registry.npmjs.org/npm-install-checks/-/npm-install-checks-3.0.2.tgz
Source586: https://registry.npmjs.org/npm-lifecycle/-/npm-lifecycle-3.1.5.tgz
Source587: https://registry.npmjs.org/npm-logical-tree/-/npm-logical-tree-1.2.1.tgz
Source588: https://registry.npmjs.org/npm-normalize-package-bin/-/npm-normalize-package-bin-1.0.1.tgz
Source589: https://registry.npmjs.org/npm-package-arg/-/npm-package-arg-6.1.1.tgz
Source590: https://registry.npmjs.org/npm-packlist/-/npm-packlist-1.4.8.tgz
Source591: https://registry.npmjs.org/npm-pick-manifest/-/npm-pick-manifest-3.0.2.tgz
Source592: https://registry.npmjs.org/npm-profile/-/npm-profile-4.0.4.tgz
Source593: https://registry.npmjs.org/npm-registry-fetch/-/npm-registry-fetch-4.0.7.tgz
Source594: https://registry.npmjs.org/npm-run-path/-/npm-run-path-2.0.2.tgz
Source595: https://registry.npmjs.org/npm-run-path/-/npm-run-path-4.0.1.tgz
Source596: https://registry.npmjs.org/npm-user-validate/-/npm-user-validate-1.0.1.tgz
Source597: https://registry.npmjs.org/npmlog/-/npmlog-4.1.2.tgz
Source598: https://registry.npmjs.org/number-is-nan/-/number-is-nan-1.0.1.tgz
Source599: https://registry.npmjs.org/oauth-sign/-/oauth-sign-0.9.0.tgz
Source600: https://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz
Source601: https://registry.npmjs.org/object-inspect/-/object-inspect-1.13.4.tgz
Source602: https://registry.npmjs.org/object-is/-/object-is-1.1.6.tgz
Source603: https://registry.npmjs.org/object-keys/-/object-keys-1.1.1.tgz
Source604: https://registry.npmjs.org/object.assign/-/object.assign-4.1.7.tgz
Source605: https://registry.npmjs.org/object.getownpropertydescriptors/-/object.getownpropertydescriptors-2.1.8.tgz
Source606: https://registry.npmjs.org/octokit-pagination-methods/-/octokit-pagination-methods-1.1.0.tgz
Source607: https://registry.npmjs.org/once/-/once-1.4.0.tgz
Source608: https://registry.npmjs.org/onetime/-/onetime-5.1.2.tgz
Source609: https://registry.npmjs.org/opener/-/opener-1.5.2.tgz
Source610: https://registry.npmjs.org/ora/-/ora-5.4.1.tgz
Source611: https://registry.npmjs.org/os-homedir/-/os-homedir-1.0.2.tgz
Source612: https://registry.npmjs.org/os-name/-/os-name-3.1.0.tgz
Source613: https://registry.npmjs.org/os-tmpdir/-/os-tmpdir-1.0.2.tgz
Source614: https://registry.npmjs.org/osenv/-/osenv-0.1.5.tgz
Source615: https://registry.npmjs.org/own-keys/-/own-keys-1.0.1.tgz
Source616: https://registry.npmjs.org/p-filter/-/p-filter-2.1.0.tgz
Source617: https://registry.npmjs.org/p-finally/-/p-finally-1.0.0.tgz
Source618: https://registry.npmjs.org/p-finally/-/p-finally-2.0.1.tgz
Source619: https://registry.npmjs.org/p-is-promise/-/p-is-promise-3.0.0.tgz
Source620: https://registry.npmjs.org/p-limit/-/p-limit-1.3.0.tgz
Source621: https://registry.npmjs.org/p-limit/-/p-limit-2.3.0.tgz
Source622: https://registry.npmjs.org/p-locate/-/p-locate-2.0.0.tgz
Source623: https://registry.npmjs.org/p-locate/-/p-locate-3.0.0.tgz
Source624: https://registry.npmjs.org/p-locate/-/p-locate-4.1.0.tgz
Source625: https://registry.npmjs.org/p-map/-/p-map-2.1.0.tgz
Source626: https://registry.npmjs.org/p-reduce/-/p-reduce-2.1.0.tgz
Source627: https://registry.npmjs.org/p-retry/-/p-retry-4.6.2.tgz
Source628: https://registry.npmjs.org/p-try/-/p-try-1.0.0.tgz
Source629: https://registry.npmjs.org/p-try/-/p-try-2.2.0.tgz
Source630: https://registry.npmjs.org/package-json/-/package-json-4.0.1.tgz
Source631: https://registry.npmjs.org/pacote/-/pacote-9.5.12.tgz
Source632: https://registry.npmjs.org/parallel-transform/-/parallel-transform-1.2.0.tgz
Source633: https://registry.npmjs.org/parent-module/-/parent-module-1.0.1.tgz
Source634: https://registry.npmjs.org/parse-json/-/parse-json-4.0.0.tgz
Source635: https://registry.npmjs.org/parse-json/-/parse-json-5.2.0.tgz
Source636: https://registry.npmjs.org/parse-passwd/-/parse-passwd-1.0.0.tgz
Source637: https://registry.npmjs.org/path-exists/-/path-exists-3.0.0.tgz
Source638: https://registry.npmjs.org/path-exists/-/path-exists-4.0.0.tgz
Source639: https://registry.npmjs.org/path-is-absolute/-/path-is-absolute-1.0.1.tgz
Source640: https://registry.npmjs.org/path-is-inside/-/path-is-inside-1.0.2.tgz
Source641: https://registry.npmjs.org/path-key/-/path-key-2.0.1.tgz
Source642: https://registry.npmjs.org/path-key/-/path-key-3.1.1.tgz
Source643: https://registry.npmjs.org/path-parse/-/path-parse-1.0.7.tgz
Source644: https://registry.npmjs.org/path-type/-/path-type-4.0.0.tgz
Source645: https://registry.npmjs.org/patternfly/-/patternfly-3.59.5.tgz
Source646: https://registry.npmjs.org/patternfly-bootstrap-combobox/-/patternfly-bootstrap-combobox-1.1.7.tgz
Source647: https://registry.npmjs.org/patternfly-bootstrap-treeview/-/patternfly-bootstrap-treeview-2.1.10.tgz
Source648: https://registry.npmjs.org/patternfly-react/-/patternfly-react-2.40.0.tgz
Source649: https://registry.npmjs.org/patternfly-react-extensions/-/patternfly-react-extensions-3.0.15.tgz
Source650: https://registry.npmjs.org/performance-now/-/performance-now-0.2.0.tgz
Source651: https://registry.npmjs.org/performance-now/-/performance-now-2.1.0.tgz
Source652: https://registry.npmjs.org/picocolors/-/picocolors-1.1.1.tgz
Source653: https://registry.npmjs.org/picomatch/-/picomatch-2.3.1.tgz
Source654: https://registry.npmjs.org/pify/-/pify-3.0.0.tgz
Source655: https://registry.npmjs.org/pkg-conf/-/pkg-conf-2.1.0.tgz
Source656: https://registry.npmjs.org/popper.js/-/popper.js-1.16.1.tgz
Source657: https://registry.npmjs.org/possible-typed-array-names/-/possible-typed-array-names-1.1.0.tgz
Source658: https://registry.npmjs.org/prepend-http/-/prepend-http-1.0.4.tgz
Source659: https://registry.npmjs.org/process-nextick-args/-/process-nextick-args-2.0.1.tgz
Source660: https://registry.npmjs.org/promise-inflight/-/promise-inflight-1.0.1.tgz
Source661: https://registry.npmjs.org/promise-retry/-/promise-retry-1.1.1.tgz
Source662: https://registry.npmjs.org/promzard/-/promzard-0.3.0.tgz
Source663: https://registry.npmjs.org/prop-types/-/prop-types-15.8.1.tgz
Source664: https://registry.npmjs.org/prop-types-extra/-/prop-types-extra-1.1.1.tgz
Source665: https://registry.npmjs.org/proto-list/-/proto-list-1.2.4.tgz
Source666: https://registry.npmjs.org/protoduck/-/protoduck-5.0.1.tgz
Source667: https://registry.npmjs.org/prr/-/prr-1.0.1.tgz
Source668: https://registry.npmjs.org/pseudomap/-/pseudomap-1.0.2.tgz
Source669: https://registry.npmjs.org/psl/-/psl-1.15.0.tgz
Source670: https://registry.npmjs.org/pump/-/pump-2.0.1.tgz
Source671: https://registry.npmjs.org/pump/-/pump-3.0.2.tgz
Source672: https://registry.npmjs.org/pumpify/-/pumpify-1.5.1.tgz
Source673: https://registry.npmjs.org/punycode/-/punycode-2.3.1.tgz
Source674: https://registry.npmjs.org/q/-/q-1.5.1.tgz
Source675: https://registry.npmjs.org/qrcode-terminal/-/qrcode-terminal-0.12.0.tgz
Source676: https://registry.npmjs.org/qs/-/qs-6.5.3.tgz
Source677: https://registry.npmjs.org/query-string/-/query-string-6.14.1.tgz
Source678: https://registry.npmjs.org/queue-microtask/-/queue-microtask-1.2.3.tgz
Source679: https://registry.npmjs.org/quick-lru/-/quick-lru-4.0.1.tgz
Source680: https://registry.npmjs.org/qw/-/qw-1.0.2.tgz
Source681: https://registry.npmjs.org/raf/-/raf-3.4.1.tgz
Source682: https://registry.npmjs.org/rc/-/rc-1.2.8.tgz
Source683: https://registry.npmjs.org/react-bootstrap/-/react-bootstrap-0.33.1.tgz
Source684: https://registry.npmjs.org/react-bootstrap-switch/-/react-bootstrap-switch-15.5.3.tgz
Source685: https://registry.npmjs.org/react-bootstrap-typeahead/-/react-bootstrap-typeahead-3.4.7.tgz
Source686: https://registry.npmjs.org/react-c3js/-/react-c3js-0.1.20.tgz
Source687: https://registry.npmjs.org/react-click-outside/-/react-click-outside-3.0.1.tgz
Source688: https://registry.npmjs.org/react-collapse/-/react-collapse-4.0.3.tgz
Source689: https://registry.npmjs.org/react-debounce-input/-/react-debounce-input-3.3.0.tgz
Source690: https://registry.npmjs.org/react-diff-view/-/react-diff-view-1.8.1.tgz
Source691: https://registry.npmjs.org/react-ellipsis-with-tooltip/-/react-ellipsis-with-tooltip-1.1.1.tgz
Source692: https://registry.npmjs.org/react-fontawesome/-/react-fontawesome-1.7.1.tgz
Source693: https://registry.npmjs.org/react-is/-/react-is-16.13.1.tgz
Source694: https://registry.npmjs.org/react-lifecycles-compat/-/react-lifecycles-compat-3.0.4.tgz
Source695: https://registry.npmjs.org/react-motion/-/react-motion-0.5.2.tgz
Source696: https://registry.npmjs.org/react-overlays/-/react-overlays-0.8.3.tgz
Source697: https://registry.npmjs.org/react-overlays/-/react-overlays-0.9.3.tgz
Source698: https://registry.npmjs.org/react-popper/-/react-popper-1.3.11.tgz
Source699: https://registry.npmjs.org/react-prop-types/-/react-prop-types-0.4.0.tgz
Source700: https://registry.npmjs.org/react-recompose/-/react-recompose-0.31.2.tgz
Source701: https://registry.npmjs.org/react-transition-group/-/react-transition-group-2.9.0.tgz
Source702: https://registry.npmjs.org/react-virtualized/-/react-virtualized-9.22.6.tgz
Source703: https://registry.npmjs.org/reactabular-table/-/reactabular-table-8.14.0.tgz
Source704: https://registry.npmjs.org/read/-/read-1.0.7.tgz
Source705: https://registry.npmjs.org/read-cmd-shim/-/read-cmd-shim-1.0.5.tgz
Source706: https://registry.npmjs.org/read-installed/-/read-installed-4.0.3.tgz
Source707: https://registry.npmjs.org/read-package-json/-/read-package-json-2.1.2.tgz
Source708: https://registry.npmjs.org/read-package-tree/-/read-package-tree-5.3.1.tgz
Source709: https://registry.npmjs.org/read-pkg/-/read-pkg-5.2.0.tgz
Source710: https://registry.npmjs.org/read-pkg-up/-/read-pkg-up-7.0.1.tgz
Source711: https://registry.npmjs.org/readable-stream/-/readable-stream-1.1.14.tgz
Source712: https://registry.npmjs.org/readable-stream/-/readable-stream-2.3.8.tgz
Source713: https://registry.npmjs.org/readable-stream/-/readable-stream-3.6.2.tgz
Source714: https://registry.npmjs.org/readdir-scoped-modules/-/readdir-scoped-modules-1.1.0.tgz
Source715: https://registry.npmjs.org/redent/-/redent-3.0.0.tgz
Source716: https://registry.npmjs.org/redeyed/-/redeyed-2.1.1.tgz
Source717: https://registry.npmjs.org/reflect.getprototypeof/-/reflect.getprototypeof-1.0.10.tgz
Source718: https://registry.npmjs.org/regexp.prototype.flags/-/regexp.prototype.flags-1.5.4.tgz
Source719: https://registry.npmjs.org/registry-auth-token/-/registry-auth-token-3.4.0.tgz
Source720: https://registry.npmjs.org/registry-auth-token/-/registry-auth-token-4.2.2.tgz
Source721: https://registry.npmjs.org/registry-url/-/registry-url-3.1.0.tgz
Source722: https://registry.npmjs.org/request/-/request-2.88.2.tgz
Source723: https://registry.npmjs.org/require-directory/-/require-directory-2.1.1.tgz
Source724: https://registry.npmjs.org/require-from-string/-/require-from-string-2.0.2.tgz
Source725: https://registry.npmjs.org/require-main-filename/-/require-main-filename-2.0.0.tgz
Source726: https://registry.npmjs.org/resolve/-/resolve-1.22.10.tgz
Source727: https://registry.npmjs.org/resolve-dir/-/resolve-dir-1.0.1.tgz
Source728: https://registry.npmjs.org/resolve-from/-/resolve-from-4.0.0.tgz
Source729: https://registry.npmjs.org/resolve-from/-/resolve-from-5.0.0.tgz
Source730: https://registry.npmjs.org/restore-cursor/-/restore-cursor-3.1.0.tgz
Source731: https://registry.npmjs.org/retry/-/retry-0.10.1.tgz
Source732: https://registry.npmjs.org/retry/-/retry-0.12.0.tgz
Source733: https://registry.npmjs.org/retry/-/retry-0.13.1.tgz
Source734: https://registry.npmjs.org/reusify/-/reusify-1.1.0.tgz
Source735: https://registry.npmjs.org/rimraf/-/rimraf-2.7.1.tgz
Source736: https://registry.npmjs.org/run-async/-/run-async-2.4.1.tgz
Source737: https://registry.npmjs.org/run-parallel/-/run-parallel-1.2.0.tgz
Source738: https://registry.npmjs.org/run-queue/-/run-queue-1.0.3.tgz
Source739: https://registry.npmjs.org/rxjs/-/rxjs-7.8.2.tgz
Source740: https://registry.npmjs.org/safe-array-concat/-/safe-array-concat-1.1.3.tgz
Source741: https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.1.2.tgz
Source742: https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.2.1.tgz
Source743: https://registry.npmjs.org/safe-push-apply/-/safe-push-apply-1.0.0.tgz
Source744: https://registry.npmjs.org/safe-regex-test/-/safe-regex-test-1.1.0.tgz
Source745: https://registry.npmjs.org/safer-buffer/-/safer-buffer-2.1.2.tgz
Source746: https://registry.npmjs.org/semantic-release/-/semantic-release-15.14.0.tgz
Source747: https://registry.npmjs.org/semver/-/semver-5.7.2.tgz
Source748: https://registry.npmjs.org/semver/-/semver-6.3.1.tgz
Source749: https://registry.npmjs.org/semver/-/semver-7.7.2.tgz
Source750: https://registry.npmjs.org/semver-diff/-/semver-diff-2.1.0.tgz
Source751: https://registry.npmjs.org/semver-regex/-/semver-regex-2.0.0.tgz
Source752: https://registry.npmjs.org/set-blocking/-/set-blocking-2.0.0.tgz
Source753: https://registry.npmjs.org/set-function-length/-/set-function-length-1.2.2.tgz
Source754: https://registry.npmjs.org/set-function-name/-/set-function-name-2.0.2.tgz
Source755: https://registry.npmjs.org/set-proto/-/set-proto-1.0.0.tgz
Source756: https://registry.npmjs.org/sha/-/sha-3.0.0.tgz
Source757: https://registry.npmjs.org/shebang-command/-/shebang-command-1.2.0.tgz
Source758: https://registry.npmjs.org/shebang-command/-/shebang-command-2.0.0.tgz
Source759: https://registry.npmjs.org/shebang-regex/-/shebang-regex-1.0.0.tgz
Source760: https://registry.npmjs.org/shebang-regex/-/shebang-regex-3.0.0.tgz
Source761: https://registry.npmjs.org/side-channel/-/side-channel-1.1.0.tgz
Source762: https://registry.npmjs.org/side-channel-list/-/side-channel-list-1.0.0.tgz
Source763: https://registry.npmjs.org/side-channel-map/-/side-channel-map-1.0.1.tgz
Source764: https://registry.npmjs.org/side-channel-weakmap/-/side-channel-weakmap-1.0.2.tgz
Source765: https://registry.npmjs.org/signal-exit/-/signal-exit-3.0.7.tgz
Source766: https://registry.npmjs.org/signale/-/signale-1.4.0.tgz
Source767: https://registry.npmjs.org/slash/-/slash-3.0.0.tgz
Source768: https://registry.npmjs.org/slide/-/slide-1.1.6.tgz
Source769: https://registry.npmjs.org/smart-buffer/-/smart-buffer-4.2.0.tgz
Source770: https://registry.npmjs.org/socks/-/socks-2.3.3.tgz
Source771: https://registry.npmjs.org/socks-proxy-agent/-/socks-proxy-agent-4.0.2.tgz
Source772: https://registry.npmjs.org/sortabular/-/sortabular-1.6.0.tgz
Source773: https://registry.npmjs.org/sorted-object/-/sorted-object-2.0.1.tgz
Source774: https://registry.npmjs.org/sorted-union-stream/-/sorted-union-stream-2.1.3.tgz
Source775: https://registry.npmjs.org/source-map/-/source-map-0.6.1.tgz
Source776: https://registry.npmjs.org/spawn-error-forwarder/-/spawn-error-forwarder-1.0.0.tgz
Source777: https://registry.npmjs.org/spdx-correct/-/spdx-correct-3.2.0.tgz
Source778: https://registry.npmjs.org/spdx-exceptions/-/spdx-exceptions-2.5.0.tgz
Source779: https://registry.npmjs.org/spdx-expression-parse/-/spdx-expression-parse-3.0.1.tgz
Source780: https://registry.npmjs.org/spdx-license-ids/-/spdx-license-ids-3.0.21.tgz
Source781: https://registry.npmjs.org/split/-/split-1.0.1.tgz
Source782: https://registry.npmjs.org/split-on-first/-/split-on-first-1.1.0.tgz
Source783: https://registry.npmjs.org/split2/-/split2-1.0.0.tgz
Source784: https://registry.npmjs.org/split2/-/split2-3.2.2.tgz
Source785: https://registry.npmjs.org/sshpk/-/sshpk-1.18.0.tgz
Source786: https://registry.npmjs.org/ssri/-/ssri-6.0.2.tgz
Source787: https://registry.npmjs.org/stop-iteration-iterator/-/stop-iteration-iterator-1.1.0.tgz
Source788: https://registry.npmjs.org/stream-each/-/stream-each-1.2.3.tgz
Source789: https://registry.npmjs.org/stream-iterate/-/stream-iterate-1.2.0.tgz
Source790: https://registry.npmjs.org/stream-shift/-/stream-shift-1.0.3.tgz
Source791: https://registry.npmjs.org/strict-uri-encode/-/strict-uri-encode-2.0.0.tgz
Source792: https://registry.npmjs.org/string_decoder/-/string_decoder-0.10.31.tgz
Source793: https://registry.npmjs.org/string_decoder/-/string_decoder-1.1.1.tgz
Source794: https://registry.npmjs.org/string_decoder/-/string_decoder-1.3.0.tgz
Source795: https://registry.npmjs.org/string-width/-/string-width-1.0.2.tgz
Source796: https://registry.npmjs.org/string-width/-/string-width-2.1.1.tgz
Source797: https://registry.npmjs.org/string-width/-/string-width-3.1.0.tgz
Source798: https://registry.npmjs.org/string-width/-/string-width-4.2.3.tgz
Source799: https://registry.npmjs.org/string.prototype.trim/-/string.prototype.trim-1.2.10.tgz
Source800: https://registry.npmjs.org/string.prototype.trimend/-/string.prototype.trimend-1.0.9.tgz
Source801: https://registry.npmjs.org/string.prototype.trimstart/-/string.prototype.trimstart-1.0.8.tgz
Source802: https://registry.npmjs.org/stringify-package/-/stringify-package-1.0.1.tgz
Source803: https://registry.npmjs.org/strip-ansi/-/strip-ansi-3.0.1.tgz
Source804: https://registry.npmjs.org/strip-ansi/-/strip-ansi-4.0.0.tgz
Source805: https://registry.npmjs.org/strip-ansi/-/strip-ansi-5.2.0.tgz
Source806: https://registry.npmjs.org/strip-ansi/-/strip-ansi-6.0.1.tgz
Source807: https://registry.npmjs.org/strip-bom/-/strip-bom-3.0.0.tgz
Source808: https://registry.npmjs.org/strip-bom/-/strip-bom-4.0.0.tgz
Source809: https://registry.npmjs.org/strip-eof/-/strip-eof-1.0.0.tgz
Source810: https://registry.npmjs.org/strip-final-newline/-/strip-final-newline-2.0.0.tgz
Source811: https://registry.npmjs.org/strip-indent/-/strip-indent-3.0.0.tgz
Source812: https://registry.npmjs.org/strip-json-comments/-/strip-json-comments-2.0.1.tgz
Source813: https://registry.npmjs.org/strip-json-comments/-/strip-json-comments-3.1.1.tgz
Source814: https://registry.npmjs.org/supports-color/-/supports-color-5.5.0.tgz
Source815: https://registry.npmjs.org/supports-color/-/supports-color-7.2.0.tgz
Source816: https://registry.npmjs.org/supports-hyperlinks/-/supports-hyperlinks-1.0.1.tgz
Source817: https://registry.npmjs.org/supports-preserve-symlinks-flag/-/supports-preserve-symlinks-flag-1.0.0.tgz
Source818: https://registry.npmjs.org/symbol-observable/-/symbol-observable-1.2.0.tgz
Source819: https://registry.npmjs.org/table-resolver/-/table-resolver-3.3.0.tgz
Source820: https://registry.npmjs.org/tar/-/tar-4.4.19.tgz
Source821: https://registry.npmjs.org/temp-dir/-/temp-dir-1.0.0.tgz
Source822: https://registry.npmjs.org/tempy/-/tempy-0.3.0.tgz
Source823: https://registry.npmjs.org/term-size/-/term-size-1.2.0.tgz
Source824: https://registry.npmjs.org/text-extensions/-/text-extensions-1.9.0.tgz
Source825: https://registry.npmjs.org/text-table/-/text-table-0.2.0.tgz
Source826: https://registry.npmjs.org/through/-/through-2.3.8.tgz
Source827: https://registry.npmjs.org/through2/-/through2-2.0.5.tgz
Source828: https://registry.npmjs.org/through2/-/through2-4.0.2.tgz
Source829: https://registry.npmjs.org/timed-out/-/timed-out-4.0.1.tgz
Source830: https://registry.npmjs.org/tiny-relative-date/-/tiny-relative-date-1.3.0.tgz
Source831: https://registry.npmjs.org/tmp/-/tmp-0.0.33.tgz
Source832: https://registry.npmjs.org/to-regex-range/-/to-regex-range-5.0.1.tgz
Source833: https://registry.npmjs.org/tough-cookie/-/tough-cookie-2.5.0.tgz
Source834: https://registry.npmjs.org/tr46/-/tr46-0.0.3.tgz
Source835: https://registry.npmjs.org/traverse/-/traverse-0.6.8.tgz
Source836: https://registry.npmjs.org/trim-newlines/-/trim-newlines-3.0.1.tgz
Source837: https://registry.npmjs.org/tslib/-/tslib-2.8.1.tgz
Source838: https://registry.npmjs.org/tunnel-agent/-/tunnel-agent-0.6.0.tgz
Source839: https://registry.npmjs.org/tweetnacl/-/tweetnacl-0.14.5.tgz
Source840: https://registry.npmjs.org/type-fest/-/type-fest-0.18.1.tgz
Source841: https://registry.npmjs.org/type-fest/-/type-fest-0.21.3.tgz
Source842: https://registry.npmjs.org/type-fest/-/type-fest-0.3.1.tgz
Source843: https://registry.npmjs.org/type-fest/-/type-fest-0.6.0.tgz
Source844: https://registry.npmjs.org/type-fest/-/type-fest-0.8.1.tgz
Source845: https://registry.npmjs.org/typed-array-buffer/-/typed-array-buffer-1.0.3.tgz
Source846: https://registry.npmjs.org/typed-array-byte-length/-/typed-array-byte-length-1.0.3.tgz
Source847: https://registry.npmjs.org/typed-array-byte-offset/-/typed-array-byte-offset-1.0.4.tgz
Source848: https://registry.npmjs.org/typed-array-length/-/typed-array-length-1.0.7.tgz
Source849: https://registry.npmjs.org/typed-styles/-/typed-styles-0.0.7.tgz
Source850: https://registry.npmjs.org/typedarray/-/typedarray-0.0.6.tgz
Source851: https://registry.npmjs.org/uglify-js/-/uglify-js-3.19.3.tgz
Source852: https://registry.npmjs.org/uid-number/-/uid-number-0.0.6.tgz
Source853: https://registry.npmjs.org/umask/-/umask-1.1.0.tgz
Source854: https://registry.npmjs.org/unbox-primitive/-/unbox-primitive-1.1.0.tgz
Source855: https://registry.npmjs.org/uncontrollable/-/uncontrollable-7.2.1.tgz
Source856: https://registry.npmjs.org/undici-types/-/undici-types-7.8.0.tgz
Source857: https://registry.npmjs.org/unidiff/-/unidiff-1.0.4.tgz
Source858: https://registry.npmjs.org/unique-filename/-/unique-filename-1.1.1.tgz
Source859: https://registry.npmjs.org/unique-slug/-/unique-slug-2.0.2.tgz
Source860: https://registry.npmjs.org/unique-string/-/unique-string-1.0.0.tgz
Source861: https://registry.npmjs.org/universal-user-agent/-/universal-user-agent-4.0.1.tgz
Source862: https://registry.npmjs.org/universal-user-agent/-/universal-user-agent-6.0.1.tgz
Source863: https://registry.npmjs.org/universalify/-/universalify-0.1.2.tgz
Source864: https://registry.npmjs.org/universalify/-/universalify-2.0.1.tgz
Source865: https://registry.npmjs.org/unpipe/-/unpipe-1.0.0.tgz
Source866: https://registry.npmjs.org/unzip-response/-/unzip-response-2.0.1.tgz
Source867: https://registry.npmjs.org/update-notifier/-/update-notifier-2.5.0.tgz
Source868: https://registry.npmjs.org/uri-js/-/uri-js-4.4.1.tgz
Source869: https://registry.npmjs.org/url-join/-/url-join-4.0.1.tgz
Source870: https://registry.npmjs.org/url-parse-lax/-/url-parse-lax-1.0.0.tgz
Source871: https://registry.npmjs.org/util-deprecate/-/util-deprecate-1.0.2.tgz
Source872: https://registry.npmjs.org/util-extend/-/util-extend-1.0.3.tgz
Source873: https://registry.npmjs.org/util-promisify/-/util-promisify-2.1.0.tgz
Source874: https://registry.npmjs.org/uuid/-/uuid-3.4.0.tgz
Source875: https://registry.npmjs.org/validate-npm-package-license/-/validate-npm-package-license-3.0.4.tgz
Source876: https://registry.npmjs.org/validate-npm-package-name/-/validate-npm-package-name-3.0.0.tgz
Source877: https://registry.npmjs.org/verror/-/verror-1.10.0.tgz
Source878: https://registry.npmjs.org/warning/-/warning-3.0.0.tgz
Source879: https://registry.npmjs.org/warning/-/warning-4.0.3.tgz
Source880: https://registry.npmjs.org/wcwidth/-/wcwidth-1.0.1.tgz
Source881: https://registry.npmjs.org/webidl-conversions/-/webidl-conversions-3.0.1.tgz
Source882: https://registry.npmjs.org/whatwg-url/-/whatwg-url-5.0.0.tgz
Source883: https://registry.npmjs.org/which/-/which-1.3.1.tgz
Source884: https://registry.npmjs.org/which/-/which-2.0.2.tgz
Source885: https://registry.npmjs.org/which-boxed-primitive/-/which-boxed-primitive-1.1.1.tgz
Source886: https://registry.npmjs.org/which-builtin-type/-/which-builtin-type-1.2.1.tgz
Source887: https://registry.npmjs.org/which-collection/-/which-collection-1.0.2.tgz
Source888: https://registry.npmjs.org/which-module/-/which-module-2.0.1.tgz
Source889: https://registry.npmjs.org/which-typed-array/-/which-typed-array-1.1.19.tgz
Source890: https://registry.npmjs.org/wide-align/-/wide-align-1.1.5.tgz
Source891: https://registry.npmjs.org/widest-line/-/widest-line-2.0.1.tgz
Source892: https://registry.npmjs.org/windows-release/-/windows-release-3.3.3.tgz
Source893: https://registry.npmjs.org/word-wrap/-/word-wrap-1.2.5.tgz
Source894: https://registry.npmjs.org/wordwrap/-/wordwrap-1.0.0.tgz
Source895: https://registry.npmjs.org/worker-farm/-/worker-farm-1.7.0.tgz
Source896: https://registry.npmjs.org/wrap-ansi/-/wrap-ansi-5.1.0.tgz
Source897: https://registry.npmjs.org/wrap-ansi/-/wrap-ansi-6.2.0.tgz
Source898: https://registry.npmjs.org/wrap-ansi/-/wrap-ansi-7.0.0.tgz
Source899: https://registry.npmjs.org/wrappy/-/wrappy-1.0.2.tgz
Source900: https://registry.npmjs.org/write-file-atomic/-/write-file-atomic-2.4.3.tgz
Source901: https://registry.npmjs.org/xdg-basedir/-/xdg-basedir-3.0.0.tgz
Source902: https://registry.npmjs.org/xtend/-/xtend-4.0.2.tgz
Source903: https://registry.npmjs.org/y18n/-/y18n-4.0.3.tgz
Source904: https://registry.npmjs.org/yallist/-/yallist-2.1.2.tgz
Source905: https://registry.npmjs.org/yallist/-/yallist-3.1.1.tgz
Source906: https://registry.npmjs.org/yallist/-/yallist-4.0.0.tgz
Source907: https://registry.npmjs.org/yaml/-/yaml-1.10.2.tgz
Source908: https://registry.npmjs.org/yargs/-/yargs-14.2.3.tgz
Source909: https://registry.npmjs.org/yargs/-/yargs-15.4.1.tgz
Source910: https://registry.npmjs.org/yargs-parser/-/yargs-parser-15.0.3.tgz
Source911: https://registry.npmjs.org/yargs-parser/-/yargs-parser-18.1.3.tgz
Source912: https://registry.npmjs.org/yargs-parser/-/yargs-parser-20.2.9.tgz
Source913: nodejs-patternfly-react-extensions-%{version}-registry.npmjs.org.tgz
BuildRequires: %{?scl_prefix_nodejs}npm
%if 0%{!?scl:1}
BuildRequires: nodejs-packaging
%endif
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}
Provides: bundled(npm(@babel/code-frame)) = 7.27.1
Provides: bundled(npm(@babel/helper-validator-identifier)) = 7.27.1
Provides: bundled(npm(@babel/runtime)) = 7.27.6
Provides: bundled(npm(@babel/runtime-corejs2)) = 7.27.6
Provides: bundled(npm(@commitlint/config-validator)) = 19.8.1
Provides: bundled(npm(@commitlint/execute-rule)) = 19.8.1
Provides: bundled(npm(@commitlint/load)) = 19.8.1
Provides: bundled(npm(@commitlint/resolve-extends)) = 19.8.1
Provides: bundled(npm(@commitlint/types)) = 19.8.1
Provides: bundled(npm(@hypnosphi/create-react-context)) = 0.3.1
Provides: bundled(npm(@iarna/cli)) = 2.2.0
Provides: bundled(npm(@nodelib/fs.scandir)) = 2.1.5
Provides: bundled(npm(@nodelib/fs.stat)) = 2.0.5
Provides: bundled(npm(@nodelib/fs.walk)) = 1.2.8
Provides: bundled(npm(@octokit/auth-token)) = 2.5.0
Provides: bundled(npm(@octokit/endpoint)) = 6.0.12
Provides: bundled(npm(@octokit/openapi-types)) = 12.11.0
Provides: bundled(npm(@octokit/plugin-paginate-rest)) = 1.1.2
Provides: bundled(npm(@octokit/plugin-request-log)) = 1.0.4
Provides: bundled(npm(@octokit/plugin-rest-endpoint-methods)) = 2.4.0
Provides: bundled(npm(@octokit/request)) = 5.6.3
Provides: bundled(npm(@octokit/request-error)) = 1.2.1
Provides: bundled(npm(@octokit/request-error)) = 2.1.0
Provides: bundled(npm(@octokit/rest)) = 16.43.2
Provides: bundled(npm(@octokit/types)) = 2.16.2
Provides: bundled(npm(@octokit/types)) = 6.41.0
Provides: bundled(npm(@semantic-release/commit-analyzer)) = 6.3.3
Provides: bundled(npm(@semantic-release/error)) = 2.2.0
Provides: bundled(npm(@semantic-release/github)) = 5.5.8
Provides: bundled(npm(@semantic-release/npm)) = 5.3.5
Provides: bundled(npm(@semantic-release/release-notes-generator)) = 7.3.5
Provides: bundled(npm(@types/c3)) = 0.6.4
Provides: bundled(npm(@types/conventional-commits-parser)) = 5.0.1
Provides: bundled(npm(@types/d3)) = 4.13.15
Provides: bundled(npm(@types/d3-array)) = 1.2.12
Provides: bundled(npm(@types/d3-axis)) = 1.0.19
Provides: bundled(npm(@types/d3-brush)) = 1.1.8
Provides: bundled(npm(@types/d3-chord)) = 1.0.14
Provides: bundled(npm(@types/d3-collection)) = 1.0.13
Provides: bundled(npm(@types/d3-color)) = 1.4.5
Provides: bundled(npm(@types/d3-dispatch)) = 1.0.12
Provides: bundled(npm(@types/d3-drag)) = 1.2.8
Provides: bundled(npm(@types/d3-dsv)) = 1.2.8
Provides: bundled(npm(@types/d3-ease)) = 1.0.13
Provides: bundled(npm(@types/d3-force)) = 1.2.7
Provides: bundled(npm(@types/d3-format)) = 1.4.5
Provides: bundled(npm(@types/d3-geo)) = 1.12.7
Provides: bundled(npm(@types/d3-hierarchy)) = 1.1.11
Provides: bundled(npm(@types/d3-interpolate)) = 1.4.5
Provides: bundled(npm(@types/d3-path)) = 1.0.11
Provides: bundled(npm(@types/d3-polygon)) = 1.0.10
Provides: bundled(npm(@types/d3-quadtree)) = 1.0.13
Provides: bundled(npm(@types/d3-queue)) = 3.0.10
Provides: bundled(npm(@types/d3-random)) = 1.1.5
Provides: bundled(npm(@types/d3-request)) = 1.0.9
Provides: bundled(npm(@types/d3-scale)) = 1.0.22
Provides: bundled(npm(@types/d3-selection)) = 1.4.7
Provides: bundled(npm(@types/d3-shape)) = 1.3.12
Provides: bundled(npm(@types/d3-time)) = 1.1.4
Provides: bundled(npm(@types/d3-time-format)) = 2.3.4
Provides: bundled(npm(@types/d3-timer)) = 1.0.12
Provides: bundled(npm(@types/d3-transition)) = 1.3.6
Provides: bundled(npm(@types/d3-voronoi)) = 1.1.12
Provides: bundled(npm(@types/d3-zoom)) = 1.8.7
Provides: bundled(npm(@types/geojson)) = 7946.0.16
Provides: bundled(npm(@types/glob)) = 7.2.0
Provides: bundled(npm(@types/minimatch)) = 5.1.2
Provides: bundled(npm(@types/minimist)) = 1.2.5
Provides: bundled(npm(@types/node)) = 24.0.2
Provides: bundled(npm(@types/normalize-package-data)) = 2.4.4
Provides: bundled(npm(@types/react)) = 19.1.8
Provides: bundled(npm(@types/retry)) = 0.12.0
Provides: bundled(npm(abbrev)) = 1.1.1
Provides: bundled(npm(agent-base)) = 4.2.1
Provides: bundled(npm(agent-base)) = 4.3.0
Provides: bundled(npm(agent-base)) = 5.1.1
Provides: bundled(npm(agentkeepalive)) = 3.5.3
Provides: bundled(npm(aggregate-error)) = 3.1.0
Provides: bundled(npm(ajv)) = 6.12.6
Provides: bundled(npm(ajv)) = 8.17.1
Provides: bundled(npm(ansi-align)) = 2.0.0
Provides: bundled(npm(ansi-escapes)) = 3.2.0
Provides: bundled(npm(ansi-escapes)) = 4.3.2
Provides: bundled(npm(ansi-regex)) = 2.1.1
Provides: bundled(npm(ansi-regex)) = 3.0.1
Provides: bundled(npm(ansi-regex)) = 4.1.1
Provides: bundled(npm(ansi-regex)) = 5.0.1
Provides: bundled(npm(ansi-styles)) = 3.2.1
Provides: bundled(npm(ansi-styles)) = 4.3.0
Provides: bundled(npm(ansicolors)) = 0.3.2
Provides: bundled(npm(ansistyles)) = 0.1.3
Provides: bundled(npm(aproba)) = 1.2.0
Provides: bundled(npm(aproba)) = 2.0.0
Provides: bundled(npm(archy)) = 1.0.0
Provides: bundled(npm(are-we-there-yet)) = 1.1.7
Provides: bundled(npm(argparse)) = 2.0.1
Provides: bundled(npm(argv-formatter)) = 1.0.0
Provides: bundled(npm(array-buffer-byte-length)) = 1.0.2
Provides: bundled(npm(array-ify)) = 1.0.0
Provides: bundled(npm(array-union)) = 2.1.0
Provides: bundled(npm(array.prototype.reduce)) = 1.0.8
Provides: bundled(npm(arraybuffer.prototype.slice)) = 1.0.4
Provides: bundled(npm(arrify)) = 1.0.1
Provides: bundled(npm(asap)) = 2.0.6
Provides: bundled(npm(asn1)) = 0.2.6
Provides: bundled(npm(assert-plus)) = 1.0.0
Provides: bundled(npm(async-function)) = 1.0.0
Provides: bundled(npm(asynckit)) = 0.4.0
Provides: bundled(npm(at-least-node)) = 1.0.0
Provides: bundled(npm(atob-lite)) = 2.0.0
Provides: bundled(npm(available-typed-arrays)) = 1.0.7
Provides: bundled(npm(aws-sign2)) = 0.7.0
Provides: bundled(npm(aws4)) = 1.13.2
Provides: bundled(npm(balanced-match)) = 1.0.2
Provides: bundled(npm(base64-js)) = 1.5.1
Provides: bundled(npm(bcrypt-pbkdf)) = 1.0.2
Provides: bundled(npm(before-after-hook)) = 2.2.3
Provides: bundled(npm(bin-links)) = 1.1.8
Provides: bundled(npm(bl)) = 4.1.0
Provides: bundled(npm(bluebird)) = 3.7.2
Provides: bundled(npm(bootstrap)) = 3.4.1
Provides: bundled(npm(bootstrap-datepicker)) = 1.10.0
Provides: bundled(npm(bootstrap-sass)) = 3.4.3
Provides: bundled(npm(bootstrap-select)) = 1.12.2
Provides: bundled(npm(bootstrap-slider)) = 9.10.0
Provides: bundled(npm(bootstrap-slider-without-jquery)) = 10.0.0
Provides: bundled(npm(bootstrap-switch)) = 3.3.4
Provides: bundled(npm(bootstrap-touchspin)) = 3.1.1
Provides: bundled(npm(bottleneck)) = 2.19.5
Provides: bundled(npm(boxen)) = 1.3.0
Provides: bundled(npm(brace-expansion)) = 1.1.12
Provides: bundled(npm(braces)) = 3.0.3
Provides: bundled(npm(breakjs)) = 1.0.0
Provides: bundled(npm(btoa-lite)) = 1.0.0
Provides: bundled(npm(buffer)) = 5.7.1
Provides: bundled(npm(buffer-from)) = 1.1.2
Provides: bundled(npm(builtins)) = 1.0.3
Provides: bundled(npm(byline)) = 5.0.0
Provides: bundled(npm(byte-size)) = 5.0.1
Provides: bundled(npm(c3)) = 0.4.24
Provides: bundled(npm(cacache)) = 12.0.4
Provides: bundled(npm(cachedir)) = 2.3.0
Provides: bundled(npm(call-bind)) = 1.0.8
Provides: bundled(npm(call-bind-apply-helpers)) = 1.0.2
Provides: bundled(npm(call-bound)) = 1.0.4
Provides: bundled(npm(call-limit)) = 1.1.1
Provides: bundled(npm(callsites)) = 3.1.0
Provides: bundled(npm(camelcase)) = 4.1.0
Provides: bundled(npm(camelcase)) = 5.3.1
Provides: bundled(npm(camelcase-keys)) = 6.2.2
Provides: bundled(npm(capture-stack-trace)) = 1.0.2
Provides: bundled(npm(cardinal)) = 2.1.1
Provides: bundled(npm(caseless)) = 0.12.0
Provides: bundled(npm(chalk)) = 2.4.2
Provides: bundled(npm(chalk)) = 4.1.2
Provides: bundled(npm(chalk)) = 5.4.1
Provides: bundled(npm(change-emitter)) = 0.1.6
Provides: bundled(npm(chardet)) = 0.7.0
Provides: bundled(npm(chownr)) = 1.1.4
Provides: bundled(npm(ci-info)) = 1.6.0
Provides: bundled(npm(ci-info)) = 2.0.0
Provides: bundled(npm(cidr-regex)) = 2.0.10
Provides: bundled(npm(classnames)) = 2.5.1
Provides: bundled(npm(clean-stack)) = 2.2.0
Provides: bundled(npm(cli-boxes)) = 1.0.0
Provides: bundled(npm(cli-columns)) = 3.1.2
Provides: bundled(npm(cli-cursor)) = 3.1.0
Provides: bundled(npm(cli-spinners)) = 2.9.2
Provides: bundled(npm(cli-table)) = 0.3.11
Provides: bundled(npm(cli-table3)) = 0.5.1
Provides: bundled(npm(cli-width)) = 3.0.0
Provides: bundled(npm(cliui)) = 5.0.0
Provides: bundled(npm(cliui)) = 6.0.0
Provides: bundled(npm(clone)) = 1.0.4
Provides: bundled(npm(clsx)) = 1.2.1
Provides: bundled(npm(cmd-shim)) = 3.0.3
Provides: bundled(npm(code-point-at)) = 1.1.0
Provides: bundled(npm(color-convert)) = 1.9.3
Provides: bundled(npm(color-convert)) = 2.0.1
Provides: bundled(npm(color-name)) = 1.1.3
Provides: bundled(npm(color-name)) = 1.1.4
Provides: bundled(npm(colors)) = 1.0.3
Provides: bundled(npm(colors)) = 1.4.0
Provides: bundled(npm(columnify)) = 1.5.4
Provides: bundled(npm(combined-stream)) = 1.0.8
Provides: bundled(npm(commitizen)) = 4.3.1
Provides: bundled(npm(compare-func)) = 2.0.0
Provides: bundled(npm(concat-map)) = 0.0.1
Provides: bundled(npm(concat-stream)) = 1.6.2
Provides: bundled(npm(config-chain)) = 1.1.13
Provides: bundled(npm(configstore)) = 3.1.5
Provides: bundled(npm(console-control-strings)) = 1.1.0
Provides: bundled(npm(conventional-changelog-angular)) = 5.0.13
Provides: bundled(npm(conventional-changelog-writer)) = 4.1.0
Provides: bundled(npm(conventional-commit-types)) = 3.0.0
Provides: bundled(npm(conventional-commits-filter)) = 2.0.7
Provides: bundled(npm(conventional-commits-parser)) = 3.2.4
Provides: bundled(npm(copy-concurrently)) = 1.0.5
Provides: bundled(npm(core-js)) = 2.6.12
Provides: bundled(npm(core-util-is)) = 1.0.2
Provides: bundled(npm(core-util-is)) = 1.0.3
Provides: bundled(npm(cosmiconfig)) = 6.0.0
Provides: bundled(npm(cosmiconfig)) = 9.0.0
Provides: bundled(npm(cosmiconfig-typescript-loader)) = 6.1.0
Provides: bundled(npm(create-error-class)) = 3.0.2
Provides: bundled(npm(create-react-context)) = 0.3.0
Provides: bundled(npm(cross-spawn)) = 5.1.0
Provides: bundled(npm(cross-spawn)) = 6.0.6
Provides: bundled(npm(cross-spawn)) = 7.0.6
Provides: bundled(npm(crypto-random-string)) = 1.0.0
Provides: bundled(npm(css-element-queries)) = 1.2.3
Provides: bundled(npm(csstype)) = 3.1.3
Provides: bundled(npm(cyclist)) = 1.0.2
Provides: bundled(npm(cz-conventional-changelog)) = 3.3.0
Provides: bundled(npm(d3)) = 3.5.17
Provides: bundled(npm(dashdash)) = 1.14.1
Provides: bundled(npm(data-view-buffer)) = 1.0.2
Provides: bundled(npm(data-view-byte-length)) = 1.0.2
Provides: bundled(npm(data-view-byte-offset)) = 1.0.1
Provides: bundled(npm(datatables.net)) = 1.13.11
Provides: bundled(npm(datatables.net)) = 2.3.2
Provides: bundled(npm(datatables.net-bs)) = 2.3.2
Provides: bundled(npm(datatables.net-colreorder)) = 1.7.2
Provides: bundled(npm(datatables.net-colreorder)) = 2.1.1
Provides: bundled(npm(datatables.net-colreorder-bs)) = 1.3.3
Provides: bundled(npm(datatables.net-select)) = 1.2.7
Provides: bundled(npm(dateformat)) = 3.0.3
Provides: bundled(npm(debug)) = 3.1.0
Provides: bundled(npm(debug)) = 3.2.7
Provides: bundled(npm(debug)) = 4.4.1
Provides: bundled(npm(debuglog)) = 1.0.1
Provides: bundled(npm(decamelize)) = 1.2.0
Provides: bundled(npm(decamelize-keys)) = 1.1.1
Provides: bundled(npm(decode-uri-component)) = 0.2.2
Provides: bundled(npm(dedent)) = 0.7.0
Provides: bundled(npm(deep-equal)) = 1.1.2
Provides: bundled(npm(deep-extend)) = 0.6.0
Provides: bundled(npm(defaults)) = 1.0.4
Provides: bundled(npm(define-data-property)) = 1.1.4
Provides: bundled(npm(define-properties)) = 1.2.1
Provides: bundled(npm(delayed-stream)) = 1.0.0
Provides: bundled(npm(delegates)) = 1.0.0
Provides: bundled(npm(deprecation)) = 2.3.1
Provides: bundled(npm(detect-file)) = 1.0.0
Provides: bundled(npm(detect-indent)) = 5.0.0
Provides: bundled(npm(detect-indent)) = 6.1.0
Provides: bundled(npm(detect-newline)) = 2.1.0
Provides: bundled(npm(dezalgo)) = 1.0.4
Provides: bundled(npm(diff)) = 5.2.0
Provides: bundled(npm(dir-glob)) = 3.0.1
Provides: bundled(npm(dom-helpers)) = 3.4.0
Provides: bundled(npm(dom-helpers)) = 5.2.1
Provides: bundled(npm(dot-prop)) = 4.2.1
Provides: bundled(npm(dot-prop)) = 5.3.0
Provides: bundled(npm(dotenv)) = 5.0.1
Provides: bundled(npm(drmonty-datatables-colvis)) = 1.1.2
Provides: bundled(npm(dunder-proto)) = 1.0.1
Provides: bundled(npm(duplexer3)) = 0.1.5
Provides: bundled(npm(duplexify)) = 3.7.1
Provides: bundled(npm(ecc-jsbn)) = 0.1.2
Provides: bundled(npm(editor)) = 1.0.0
Provides: bundled(npm(emoji-regex)) = 7.0.3
Provides: bundled(npm(emoji-regex)) = 8.0.0
Provides: bundled(npm(encoding)) = 0.1.13
Provides: bundled(npm(end-of-stream)) = 1.4.4
Provides: bundled(npm(env-ci)) = 4.5.2
Provides: bundled(npm(env-paths)) = 2.2.1
Provides: bundled(npm(eonasdan-bootstrap-datetimepicker)) = 4.17.49
Provides: bundled(npm(err-code)) = 1.1.2
Provides: bundled(npm(errno)) = 0.1.8
Provides: bundled(npm(error-ex)) = 1.3.2
Provides: bundled(npm(es-abstract)) = 1.24.0
Provides: bundled(npm(es-array-method-boxes-properly)) = 1.0.0
Provides: bundled(npm(es-define-property)) = 1.0.1
Provides: bundled(npm(es-errors)) = 1.3.0
Provides: bundled(npm(es-object-atoms)) = 1.1.1
Provides: bundled(npm(es-set-tostringtag)) = 2.1.0
Provides: bundled(npm(es-to-primitive)) = 1.3.0
Provides: bundled(npm(es6-promise)) = 4.2.8
Provides: bundled(npm(es6-promisify)) = 5.0.0
Provides: bundled(npm(escape-string-regexp)) = 1.0.5
Provides: bundled(npm(esprima)) = 4.0.1
Provides: bundled(npm(execa)) = 0.7.0
Provides: bundled(npm(execa)) = 1.0.0
Provides: bundled(npm(execa)) = 3.4.0
Provides: bundled(npm(expand-tilde)) = 2.0.2
Provides: bundled(npm(extend)) = 3.0.2
Provides: bundled(npm(external-editor)) = 3.1.0
Provides: bundled(npm(extsprintf)) = 1.3.0
Provides: bundled(npm(extsprintf)) = 1.4.1
Provides: bundled(npm(fast-deep-equal)) = 3.1.3
Provides: bundled(npm(fast-glob)) = 3.3.3
Provides: bundled(npm(fast-json-stable-stringify)) = 2.1.0
Provides: bundled(npm(fast-uri)) = 3.0.6
Provides: bundled(npm(fastq)) = 1.19.1
Provides: bundled(npm(figgy-pudding)) = 3.5.2
Provides: bundled(npm(figures)) = 2.0.0
Provides: bundled(npm(figures)) = 3.2.0
Provides: bundled(npm(fill-range)) = 7.1.1
Provides: bundled(npm(filter-obj)) = 1.1.0
Provides: bundled(npm(find-node-modules)) = 2.1.3
Provides: bundled(npm(find-npm-prefix)) = 1.0.2
Provides: bundled(npm(find-root)) = 1.1.0
Provides: bundled(npm(find-up)) = 2.1.0
Provides: bundled(npm(find-up)) = 3.0.0
Provides: bundled(npm(find-up)) = 4.1.0
Provides: bundled(npm(find-versions)) = 3.2.0
Provides: bundled(npm(findup-sync)) = 4.0.0
Provides: bundled(npm(flush-write-stream)) = 1.1.1
Provides: bundled(npm(font-awesome)) = 4.7.0
Provides: bundled(npm(font-awesome-sass)) = 4.7.0
Provides: bundled(npm(for-each)) = 0.3.5
Provides: bundled(npm(forever-agent)) = 0.6.1
Provides: bundled(npm(form-data)) = 2.3.3
Provides: bundled(npm(from2)) = 1.3.0
Provides: bundled(npm(from2)) = 2.3.0
Provides: bundled(npm(fs-extra)) = 8.1.0
Provides: bundled(npm(fs-extra)) = 9.1.0
Provides: bundled(npm(fs-minipass)) = 1.2.7
Provides: bundled(npm(fs-vacuum)) = 1.2.10
Provides: bundled(npm(fs-write-stream-atomic)) = 1.0.10
Provides: bundled(npm(fs.realpath)) = 1.0.0
Provides: bundled(npm(function-bind)) = 1.1.2
Provides: bundled(npm(function.prototype.name)) = 1.1.8
Provides: bundled(npm(functions-have-names)) = 1.2.3
Provides: bundled(npm(gauge)) = 2.7.4
Provides: bundled(npm(genfun)) = 5.0.0
Provides: bundled(npm(gentle-fs)) = 2.3.1
Provides: bundled(npm(get-caller-file)) = 2.0.5
Provides: bundled(npm(get-intrinsic)) = 1.3.0
Provides: bundled(npm(get-proto)) = 1.0.1
Provides: bundled(npm(get-stream)) = 3.0.0
Provides: bundled(npm(get-stream)) = 4.1.0
Provides: bundled(npm(get-stream)) = 5.2.0
Provides: bundled(npm(get-symbol-description)) = 1.1.0
Provides: bundled(npm(getpass)) = 0.1.7
Provides: bundled(npm(git-log-parser)) = 1.2.1
Provides: bundled(npm(gitdiff-parser)) = 0.1.2
Provides: bundled(npm(glob)) = 7.2.3
Provides: bundled(npm(glob-parent)) = 5.1.2
Provides: bundled(npm(global-directory)) = 4.0.1
Provides: bundled(npm(global-dirs)) = 0.1.1
Provides: bundled(npm(global-modules)) = 1.0.0
Provides: bundled(npm(global-prefix)) = 1.0.2
Provides: bundled(npm(globalthis)) = 1.0.4
Provides: bundled(npm(globby)) = 10.0.2
Provides: bundled(npm(google-code-prettify)) = 1.0.5
Provides: bundled(npm(gopd)) = 1.2.0
Provides: bundled(npm(got)) = 6.7.1
Provides: bundled(npm(graceful-fs)) = 4.2.11
Provides: bundled(npm(gud)) = 1.0.0
Provides: bundled(npm(handlebars)) = 4.7.8
Provides: bundled(npm(har-schema)) = 2.0.0
Provides: bundled(npm(har-validator)) = 5.1.5
Provides: bundled(npm(hard-rejection)) = 2.1.0
Provides: bundled(npm(has-bigints)) = 1.1.0
Provides: bundled(npm(has-flag)) = 2.0.0
Provides: bundled(npm(has-flag)) = 3.0.0
Provides: bundled(npm(has-flag)) = 4.0.0
Provides: bundled(npm(has-property-descriptors)) = 1.0.2
Provides: bundled(npm(has-proto)) = 1.2.0
Provides: bundled(npm(has-symbols)) = 1.1.0
Provides: bundled(npm(has-tostringtag)) = 1.0.2
Provides: bundled(npm(has-unicode)) = 2.0.1
Provides: bundled(npm(hasown)) = 2.0.2
Provides: bundled(npm(hoist-non-react-statics)) = 2.5.5
Provides: bundled(npm(homedir-polyfill)) = 1.0.3
Provides: bundled(npm(hook-std)) = 2.0.0
Provides: bundled(npm(hosted-git-info)) = 2.8.9
Provides: bundled(npm(hosted-git-info)) = 3.0.8
Provides: bundled(npm(hosted-git-info)) = 4.1.0
Provides: bundled(npm(http-cache-semantics)) = 3.8.1
Provides: bundled(npm(http-proxy-agent)) = 2.1.0
Provides: bundled(npm(http-proxy-agent)) = 3.0.0
Provides: bundled(npm(http-signature)) = 1.2.0
Provides: bundled(npm(https-proxy-agent)) = 2.2.4
Provides: bundled(npm(https-proxy-agent)) = 4.0.0
Provides: bundled(npm(human-signals)) = 1.1.1
Provides: bundled(npm(humanize-ms)) = 1.2.1
Provides: bundled(npm(iconv-lite)) = 0.4.24
Provides: bundled(npm(iconv-lite)) = 0.6.3
Provides: bundled(npm(ieee754)) = 1.2.1
Provides: bundled(npm(iferr)) = 0.1.5
Provides: bundled(npm(iferr)) = 1.0.2
Provides: bundled(npm(ignore)) = 5.3.2
Provides: bundled(npm(ignore-walk)) = 3.0.4
Provides: bundled(npm(import-fresh)) = 3.3.1
Provides: bundled(npm(import-from)) = 3.0.0
Provides: bundled(npm(import-lazy)) = 2.1.0
Provides: bundled(npm(import-meta-resolve)) = 4.1.0
Provides: bundled(npm(imurmurhash)) = 0.1.4
Provides: bundled(npm(indent-string)) = 4.0.0
Provides: bundled(npm(infer-owner)) = 1.0.4
Provides: bundled(npm(inflight)) = 1.0.6
Provides: bundled(npm(inherits)) = 2.0.4
Provides: bundled(npm(ini)) = 1.3.8
Provides: bundled(npm(ini)) = 4.1.1
Provides: bundled(npm(init-package-json)) = 1.10.3
Provides: bundled(npm(inquirer)) = 8.2.5
Provides: bundled(npm(internal-slot)) = 1.1.0
Provides: bundled(npm(into-stream)) = 5.1.1
Provides: bundled(npm(invariant)) = 2.2.4
Provides: bundled(npm(ip)) = 1.1.5
Provides: bundled(npm(ip-regex)) = 2.1.0
Provides: bundled(npm(is-arguments)) = 1.2.0
Provides: bundled(npm(is-array-buffer)) = 3.0.5
Provides: bundled(npm(is-arrayish)) = 0.2.1
Provides: bundled(npm(is-async-function)) = 2.1.1
Provides: bundled(npm(is-bigint)) = 1.1.0
Provides: bundled(npm(is-boolean-object)) = 1.2.2
Provides: bundled(npm(is-callable)) = 1.2.7
Provides: bundled(npm(is-ci)) = 1.2.1
Provides: bundled(npm(is-cidr)) = 3.1.1
Provides: bundled(npm(is-core-module)) = 2.16.1
Provides: bundled(npm(is-data-view)) = 1.0.2
Provides: bundled(npm(is-date-object)) = 1.1.0
Provides: bundled(npm(is-extglob)) = 2.1.1
Provides: bundled(npm(is-finalizationregistry)) = 1.1.1
Provides: bundled(npm(is-fullwidth-code-point)) = 1.0.0
Provides: bundled(npm(is-fullwidth-code-point)) = 2.0.0
Provides: bundled(npm(is-fullwidth-code-point)) = 3.0.0
Provides: bundled(npm(is-generator-function)) = 1.1.0
Provides: bundled(npm(is-glob)) = 4.0.3
Provides: bundled(npm(is-installed-globally)) = 0.1.0
Provides: bundled(npm(is-interactive)) = 1.0.0
Provides: bundled(npm(is-map)) = 2.0.3
Provides: bundled(npm(is-negative-zero)) = 2.0.3
Provides: bundled(npm(is-npm)) = 1.0.0
Provides: bundled(npm(is-number)) = 7.0.0
Provides: bundled(npm(is-number-object)) = 1.1.1
Provides: bundled(npm(is-obj)) = 1.0.1
Provides: bundled(npm(is-obj)) = 2.0.0
Provides: bundled(npm(is-path-inside)) = 1.0.1
Provides: bundled(npm(is-plain-obj)) = 1.1.0
Provides: bundled(npm(is-plain-object)) = 5.0.0
Provides: bundled(npm(is-redirect)) = 1.0.0
Provides: bundled(npm(is-regex)) = 1.2.1
Provides: bundled(npm(is-retry-allowed)) = 1.2.0
Provides: bundled(npm(is-set)) = 2.0.3
Provides: bundled(npm(is-shared-array-buffer)) = 1.0.4
Provides: bundled(npm(is-stream)) = 1.1.0
Provides: bundled(npm(is-stream)) = 2.0.1
Provides: bundled(npm(is-string)) = 1.1.1
Provides: bundled(npm(is-symbol)) = 1.1.1
Provides: bundled(npm(is-text-path)) = 1.0.1
Provides: bundled(npm(is-typed-array)) = 1.1.15
Provides: bundled(npm(is-typedarray)) = 1.0.0
Provides: bundled(npm(is-unicode-supported)) = 0.1.0
Provides: bundled(npm(is-utf8)) = 0.2.1
Provides: bundled(npm(is-weakmap)) = 2.0.2
Provides: bundled(npm(is-weakref)) = 1.1.1
Provides: bundled(npm(is-weakset)) = 2.0.4
Provides: bundled(npm(is-windows)) = 1.0.2
Provides: bundled(npm(isarray)) = 0.0.1
Provides: bundled(npm(isarray)) = 1.0.0
Provides: bundled(npm(isarray)) = 2.0.5
Provides: bundled(npm(isexe)) = 2.0.0
Provides: bundled(npm(isstream)) = 0.1.2
Provides: bundled(npm(issue-parser)) = 5.0.0
Provides: bundled(npm(java-properties)) = 1.0.2
Provides: bundled(npm(jiti)) = 2.4.2
Provides: bundled(npm(jquery)) = 3.4.1
Provides: bundled(npm(jquery)) = 3.7.1
Provides: bundled(npm(jquery-match-height)) = 0.7.2
Provides: bundled(npm(js-tokens)) = 4.0.0
Provides: bundled(npm(js-yaml)) = 4.1.0
Provides: bundled(npm(jsbn)) = 0.1.1
Provides: bundled(npm(json-parse-better-errors)) = 1.0.2
Provides: bundled(npm(json-parse-even-better-errors)) = 2.3.1
Provides: bundled(npm(json-schema)) = 0.4.0
Provides: bundled(npm(json-schema-traverse)) = 0.4.1
Provides: bundled(npm(json-schema-traverse)) = 1.0.0
Provides: bundled(npm(json-stringify-safe)) = 5.0.1
Provides: bundled(npm(jsonfile)) = 4.0.0
Provides: bundled(npm(jsonfile)) = 6.1.0
Provides: bundled(npm(jsonparse)) = 1.3.1
Provides: bundled(npm(JSONStream)) = 1.3.5
Provides: bundled(npm(jsprim)) = 1.4.2
Provides: bundled(npm(keycode)) = 2.2.1
Provides: bundled(npm(kind-of)) = 6.0.3
Provides: bundled(npm(latest-version)) = 3.1.0
Provides: bundled(npm(lazy-property)) = 1.0.0
Provides: bundled(npm(leven)) = 2.1.0
Provides: bundled(npm(libcipm)) = 4.0.8
Provides: bundled(npm(libnpm)) = 3.0.1
Provides: bundled(npm(libnpmaccess)) = 3.0.2
Provides: bundled(npm(libnpmconfig)) = 1.2.1
Provides: bundled(npm(libnpmhook)) = 5.0.3
Provides: bundled(npm(libnpmorg)) = 1.0.1
Provides: bundled(npm(libnpmpublish)) = 1.1.3
Provides: bundled(npm(libnpmsearch)) = 2.0.2
Provides: bundled(npm(libnpmteam)) = 1.0.2
Provides: bundled(npm(libnpx)) = 10.2.4
Provides: bundled(npm(lines-and-columns)) = 1.2.4
Provides: bundled(npm(load-json-file)) = 4.0.0
Provides: bundled(npm(locate-path)) = 2.0.0
Provides: bundled(npm(locate-path)) = 3.0.0
Provides: bundled(npm(locate-path)) = 5.0.0
Provides: bundled(npm(lock-verify)) = 2.2.2
Provides: bundled(npm(lockfile)) = 1.0.4
Provides: bundled(npm(lodash)) = 4.17.21
Provides: bundled(npm(lodash._baseindexof)) = 3.1.0
Provides: bundled(npm(lodash._baseuniq)) = 4.6.0
Provides: bundled(npm(lodash._bindcallback)) = 3.0.1
Provides: bundled(npm(lodash._cacheindexof)) = 3.0.2
Provides: bundled(npm(lodash._createcache)) = 3.1.2
Provides: bundled(npm(lodash._createset)) = 4.0.3
Provides: bundled(npm(lodash._getnative)) = 3.9.1
Provides: bundled(npm(lodash._root)) = 3.0.1
Provides: bundled(npm(lodash.capitalize)) = 4.2.1
Provides: bundled(npm(lodash.clonedeep)) = 4.5.0
Provides: bundled(npm(lodash.debounce)) = 4.0.8
Provides: bundled(npm(lodash.escape)) = 4.0.1
Provides: bundled(npm(lodash.escaperegexp)) = 4.1.2
Provides: bundled(npm(lodash.findlastindex)) = 4.6.0
Provides: bundled(npm(lodash.get)) = 4.4.2
Provides: bundled(npm(lodash.ismatch)) = 4.4.0
Provides: bundled(npm(lodash.isplainobject)) = 4.0.6
Provides: bundled(npm(lodash.isstring)) = 4.0.1
Provides: bundled(npm(lodash.map)) = 4.6.0
Provides: bundled(npm(lodash.mapvalues)) = 4.6.0
Provides: bundled(npm(lodash.merge)) = 4.6.2
Provides: bundled(npm(lodash.mergewith)) = 4.6.2
Provides: bundled(npm(lodash.restparam)) = 3.6.1
Provides: bundled(npm(lodash.set)) = 4.3.2
Provides: bundled(npm(lodash.union)) = 4.6.0
Provides: bundled(npm(lodash.uniq)) = 4.5.0
Provides: bundled(npm(lodash.uniqby)) = 4.7.0
Provides: bundled(npm(lodash.without)) = 4.4.0
Provides: bundled(npm(log-symbols)) = 4.1.0
Provides: bundled(npm(longest)) = 2.0.1
Provides: bundled(npm(loose-envify)) = 1.4.0
Provides: bundled(npm(lowercase-keys)) = 1.0.1
Provides: bundled(npm(lru-cache)) = 4.1.5
Provides: bundled(npm(lru-cache)) = 5.1.1
Provides: bundled(npm(lru-cache)) = 6.0.0
Provides: bundled(npm(macos-release)) = 2.5.1
Provides: bundled(npm(make-dir)) = 1.3.0
Provides: bundled(npm(make-fetch-happen)) = 5.0.2
Provides: bundled(npm(map-obj)) = 1.0.1
Provides: bundled(npm(map-obj)) = 4.3.0
Provides: bundled(npm(marked)) = 0.7.0
Provides: bundled(npm(marked-terminal)) = 3.3.0
Provides: bundled(npm(math-intrinsics)) = 1.1.0
Provides: bundled(npm(meant)) = 1.0.3
Provides: bundled(npm(meow)) = 8.1.2
Provides: bundled(npm(merge)) = 2.1.1
Provides: bundled(npm(merge-stream)) = 2.0.0
Provides: bundled(npm(merge2)) = 1.4.1
Provides: bundled(npm(micromatch)) = 4.0.8
Provides: bundled(npm(mime)) = 2.6.0
Provides: bundled(npm(mime-db)) = 1.52.0
Provides: bundled(npm(mime-types)) = 2.1.35
Provides: bundled(npm(mimic-fn)) = 2.1.0
Provides: bundled(npm(min-indent)) = 1.0.1
Provides: bundled(npm(minimatch)) = 3.1.2
Provides: bundled(npm(minimist)) = 1.2.7
Provides: bundled(npm(minimist)) = 1.2.8
Provides: bundled(npm(minimist-options)) = 4.1.0
Provides: bundled(npm(minipass)) = 2.9.0
Provides: bundled(npm(minizlib)) = 1.3.3
Provides: bundled(npm(mississippi)) = 3.0.0
Provides: bundled(npm(mkdirp)) = 0.5.6
Provides: bundled(npm(modify-values)) = 1.0.1
Provides: bundled(npm(moment)) = 2.30.1
Provides: bundled(npm(moment-timezone)) = 0.4.1
Provides: bundled(npm(move-concurrently)) = 1.0.1
Provides: bundled(npm(ms)) = 2.0.0
Provides: bundled(npm(ms)) = 2.1.3
Provides: bundled(npm(mute-stream)) = 0.0.8
Provides: bundled(npm(neo-async)) = 2.6.2
Provides: bundled(npm(nerf-dart)) = 1.0.0
Provides: bundled(npm(nice-try)) = 1.0.5
Provides: bundled(npm(node-emoji)) = 1.11.0
Provides: bundled(npm(node-fetch)) = 2.7.0
Provides: bundled(npm(node-fetch-npm)) = 2.0.4
Provides: bundled(npm(node-gyp)) = 5.1.1
Provides: bundled(npm(nopt)) = 4.0.3
Provides: bundled(npm(normalize-package-data)) = 2.5.0
Provides: bundled(npm(normalize-package-data)) = 3.0.3
Provides: bundled(npm(normalize-url)) = 4.5.1
Provides: bundled(npm(npm)) = 6.14.18
Provides: bundled(npm(npm-audit-report)) = 1.3.3
Provides: bundled(npm(npm-bundled)) = 1.1.2
Provides: bundled(npm(npm-cache-filename)) = 1.0.2
Provides: bundled(npm(npm-install-checks)) = 3.0.2
Provides: bundled(npm(npm-lifecycle)) = 3.1.5
Provides: bundled(npm(npm-logical-tree)) = 1.2.1
Provides: bundled(npm(npm-normalize-package-bin)) = 1.0.1
Provides: bundled(npm(npm-package-arg)) = 6.1.1
Provides: bundled(npm(npm-packlist)) = 1.4.8
Provides: bundled(npm(npm-pick-manifest)) = 3.0.2
Provides: bundled(npm(npm-profile)) = 4.0.4
Provides: bundled(npm(npm-registry-fetch)) = 4.0.7
Provides: bundled(npm(npm-run-path)) = 2.0.2
Provides: bundled(npm(npm-run-path)) = 4.0.1
Provides: bundled(npm(npm-user-validate)) = 1.0.1
Provides: bundled(npm(npmlog)) = 4.1.2
Provides: bundled(npm(number-is-nan)) = 1.0.1
Provides: bundled(npm(oauth-sign)) = 0.9.0
Provides: bundled(npm(object-assign)) = 4.1.1
Provides: bundled(npm(object-inspect)) = 1.13.4
Provides: bundled(npm(object-is)) = 1.1.6
Provides: bundled(npm(object-keys)) = 1.1.1
Provides: bundled(npm(object.assign)) = 4.1.7
Provides: bundled(npm(object.getownpropertydescriptors)) = 2.1.8
Provides: bundled(npm(octokit-pagination-methods)) = 1.1.0
Provides: bundled(npm(once)) = 1.4.0
Provides: bundled(npm(onetime)) = 5.1.2
Provides: bundled(npm(opener)) = 1.5.2
Provides: bundled(npm(ora)) = 5.4.1
Provides: bundled(npm(os-homedir)) = 1.0.2
Provides: bundled(npm(os-name)) = 3.1.0
Provides: bundled(npm(os-tmpdir)) = 1.0.2
Provides: bundled(npm(osenv)) = 0.1.5
Provides: bundled(npm(own-keys)) = 1.0.1
Provides: bundled(npm(p-filter)) = 2.1.0
Provides: bundled(npm(p-finally)) = 1.0.0
Provides: bundled(npm(p-finally)) = 2.0.1
Provides: bundled(npm(p-is-promise)) = 3.0.0
Provides: bundled(npm(p-limit)) = 1.3.0
Provides: bundled(npm(p-limit)) = 2.3.0
Provides: bundled(npm(p-locate)) = 2.0.0
Provides: bundled(npm(p-locate)) = 3.0.0
Provides: bundled(npm(p-locate)) = 4.1.0
Provides: bundled(npm(p-map)) = 2.1.0
Provides: bundled(npm(p-reduce)) = 2.1.0
Provides: bundled(npm(p-retry)) = 4.6.2
Provides: bundled(npm(p-try)) = 1.0.0
Provides: bundled(npm(p-try)) = 2.2.0
Provides: bundled(npm(package-json)) = 4.0.1
Provides: bundled(npm(pacote)) = 9.5.12
Provides: bundled(npm(parallel-transform)) = 1.2.0
Provides: bundled(npm(parent-module)) = 1.0.1
Provides: bundled(npm(parse-json)) = 4.0.0
Provides: bundled(npm(parse-json)) = 5.2.0
Provides: bundled(npm(parse-passwd)) = 1.0.0
Provides: bundled(npm(path-exists)) = 3.0.0
Provides: bundled(npm(path-exists)) = 4.0.0
Provides: bundled(npm(path-is-absolute)) = 1.0.1
Provides: bundled(npm(path-is-inside)) = 1.0.2
Provides: bundled(npm(path-key)) = 2.0.1
Provides: bundled(npm(path-key)) = 3.1.1
Provides: bundled(npm(path-parse)) = 1.0.7
Provides: bundled(npm(path-type)) = 4.0.0
Provides: bundled(npm(patternfly)) = 3.59.5
Provides: bundled(npm(patternfly-bootstrap-combobox)) = 1.1.7
Provides: bundled(npm(patternfly-bootstrap-treeview)) = 2.1.10
Provides: bundled(npm(patternfly-react)) = 2.40.0
Provides: bundled(npm(patternfly-react-extensions)) = 3.0.15
Provides: bundled(npm(performance-now)) = 0.2.0
Provides: bundled(npm(performance-now)) = 2.1.0
Provides: bundled(npm(picocolors)) = 1.1.1
Provides: bundled(npm(picomatch)) = 2.3.1
Provides: bundled(npm(pify)) = 3.0.0
Provides: bundled(npm(pkg-conf)) = 2.1.0
Provides: bundled(npm(popper.js)) = 1.16.1
Provides: bundled(npm(possible-typed-array-names)) = 1.1.0
Provides: bundled(npm(prepend-http)) = 1.0.4
Provides: bundled(npm(process-nextick-args)) = 2.0.1
Provides: bundled(npm(promise-inflight)) = 1.0.1
Provides: bundled(npm(promise-retry)) = 1.1.1
Provides: bundled(npm(promzard)) = 0.3.0
Provides: bundled(npm(prop-types)) = 15.8.1
Provides: bundled(npm(prop-types-extra)) = 1.1.1
Provides: bundled(npm(proto-list)) = 1.2.4
Provides: bundled(npm(protoduck)) = 5.0.1
Provides: bundled(npm(prr)) = 1.0.1
Provides: bundled(npm(pseudomap)) = 1.0.2
Provides: bundled(npm(psl)) = 1.15.0
Provides: bundled(npm(pump)) = 2.0.1
Provides: bundled(npm(pump)) = 3.0.2
Provides: bundled(npm(pumpify)) = 1.5.1
Provides: bundled(npm(punycode)) = 2.3.1
Provides: bundled(npm(q)) = 1.5.1
Provides: bundled(npm(qrcode-terminal)) = 0.12.0
Provides: bundled(npm(qs)) = 6.5.3
Provides: bundled(npm(query-string)) = 6.14.1
Provides: bundled(npm(queue-microtask)) = 1.2.3
Provides: bundled(npm(quick-lru)) = 4.0.1
Provides: bundled(npm(qw)) = 1.0.2
Provides: bundled(npm(raf)) = 3.4.1
Provides: bundled(npm(rc)) = 1.2.8
Provides: bundled(npm(react-bootstrap)) = 0.33.1
Provides: bundled(npm(react-bootstrap-switch)) = 15.5.3
Provides: bundled(npm(react-bootstrap-typeahead)) = 3.4.7
Provides: bundled(npm(react-c3js)) = 0.1.20
Provides: bundled(npm(react-click-outside)) = 3.0.1
Provides: bundled(npm(react-collapse)) = 4.0.3
Provides: bundled(npm(react-debounce-input)) = 3.3.0
Provides: bundled(npm(react-diff-view)) = 1.8.1
Provides: bundled(npm(react-ellipsis-with-tooltip)) = 1.1.1
Provides: bundled(npm(react-fontawesome)) = 1.7.1
Provides: bundled(npm(react-is)) = 16.13.1
Provides: bundled(npm(react-lifecycles-compat)) = 3.0.4
Provides: bundled(npm(react-motion)) = 0.5.2
Provides: bundled(npm(react-overlays)) = 0.8.3
Provides: bundled(npm(react-overlays)) = 0.9.3
Provides: bundled(npm(react-popper)) = 1.3.11
Provides: bundled(npm(react-prop-types)) = 0.4.0
Provides: bundled(npm(react-recompose)) = 0.31.2
Provides: bundled(npm(react-transition-group)) = 2.9.0
Provides: bundled(npm(react-virtualized)) = 9.22.6
Provides: bundled(npm(reactabular-table)) = 8.14.0
Provides: bundled(npm(read)) = 1.0.7
Provides: bundled(npm(read-cmd-shim)) = 1.0.5
Provides: bundled(npm(read-installed)) = 4.0.3
Provides: bundled(npm(read-package-json)) = 2.1.2
Provides: bundled(npm(read-package-tree)) = 5.3.1
Provides: bundled(npm(read-pkg)) = 5.2.0
Provides: bundled(npm(read-pkg-up)) = 7.0.1
Provides: bundled(npm(readable-stream)) = 1.1.14
Provides: bundled(npm(readable-stream)) = 2.3.8
Provides: bundled(npm(readable-stream)) = 3.6.2
Provides: bundled(npm(readdir-scoped-modules)) = 1.1.0
Provides: bundled(npm(redent)) = 3.0.0
Provides: bundled(npm(redeyed)) = 2.1.1
Provides: bundled(npm(reflect.getprototypeof)) = 1.0.10
Provides: bundled(npm(regexp.prototype.flags)) = 1.5.4
Provides: bundled(npm(registry-auth-token)) = 3.4.0
Provides: bundled(npm(registry-auth-token)) = 4.2.2
Provides: bundled(npm(registry-url)) = 3.1.0
Provides: bundled(npm(request)) = 2.88.2
Provides: bundled(npm(require-directory)) = 2.1.1
Provides: bundled(npm(require-from-string)) = 2.0.2
Provides: bundled(npm(require-main-filename)) = 2.0.0
Provides: bundled(npm(resolve)) = 1.22.10
Provides: bundled(npm(resolve-dir)) = 1.0.1
Provides: bundled(npm(resolve-from)) = 4.0.0
Provides: bundled(npm(resolve-from)) = 5.0.0
Provides: bundled(npm(restore-cursor)) = 3.1.0
Provides: bundled(npm(retry)) = 0.10.1
Provides: bundled(npm(retry)) = 0.12.0
Provides: bundled(npm(retry)) = 0.13.1
Provides: bundled(npm(reusify)) = 1.1.0
Provides: bundled(npm(rimraf)) = 2.7.1
Provides: bundled(npm(run-async)) = 2.4.1
Provides: bundled(npm(run-parallel)) = 1.2.0
Provides: bundled(npm(run-queue)) = 1.0.3
Provides: bundled(npm(rxjs)) = 7.8.2
Provides: bundled(npm(safe-array-concat)) = 1.1.3
Provides: bundled(npm(safe-buffer)) = 5.1.2
Provides: bundled(npm(safe-buffer)) = 5.2.1
Provides: bundled(npm(safe-push-apply)) = 1.0.0
Provides: bundled(npm(safe-regex-test)) = 1.1.0
Provides: bundled(npm(safer-buffer)) = 2.1.2
Provides: bundled(npm(semantic-release)) = 15.14.0
Provides: bundled(npm(semver)) = 5.7.2
Provides: bundled(npm(semver)) = 6.3.1
Provides: bundled(npm(semver)) = 7.7.2
Provides: bundled(npm(semver-diff)) = 2.1.0
Provides: bundled(npm(semver-regex)) = 2.0.0
Provides: bundled(npm(set-blocking)) = 2.0.0
Provides: bundled(npm(set-function-length)) = 1.2.2
Provides: bundled(npm(set-function-name)) = 2.0.2
Provides: bundled(npm(set-proto)) = 1.0.0
Provides: bundled(npm(sha)) = 3.0.0
Provides: bundled(npm(shebang-command)) = 1.2.0
Provides: bundled(npm(shebang-command)) = 2.0.0
Provides: bundled(npm(shebang-regex)) = 1.0.0
Provides: bundled(npm(shebang-regex)) = 3.0.0
Provides: bundled(npm(side-channel)) = 1.1.0
Provides: bundled(npm(side-channel-list)) = 1.0.0
Provides: bundled(npm(side-channel-map)) = 1.0.1
Provides: bundled(npm(side-channel-weakmap)) = 1.0.2
Provides: bundled(npm(signal-exit)) = 3.0.7
Provides: bundled(npm(signale)) = 1.4.0
Provides: bundled(npm(slash)) = 3.0.0
Provides: bundled(npm(slide)) = 1.1.6
Provides: bundled(npm(smart-buffer)) = 4.2.0
Provides: bundled(npm(socks)) = 2.3.3
Provides: bundled(npm(socks-proxy-agent)) = 4.0.2
Provides: bundled(npm(sortabular)) = 1.6.0
Provides: bundled(npm(sorted-object)) = 2.0.1
Provides: bundled(npm(sorted-union-stream)) = 2.1.3
Provides: bundled(npm(source-map)) = 0.6.1
Provides: bundled(npm(spawn-error-forwarder)) = 1.0.0
Provides: bundled(npm(spdx-correct)) = 3.2.0
Provides: bundled(npm(spdx-exceptions)) = 2.5.0
Provides: bundled(npm(spdx-expression-parse)) = 3.0.1
Provides: bundled(npm(spdx-license-ids)) = 3.0.21
Provides: bundled(npm(split)) = 1.0.1
Provides: bundled(npm(split-on-first)) = 1.1.0
Provides: bundled(npm(split2)) = 1.0.0
Provides: bundled(npm(split2)) = 3.2.2
Provides: bundled(npm(sshpk)) = 1.18.0
Provides: bundled(npm(ssri)) = 6.0.2
Provides: bundled(npm(stop-iteration-iterator)) = 1.1.0
Provides: bundled(npm(stream-each)) = 1.2.3
Provides: bundled(npm(stream-iterate)) = 1.2.0
Provides: bundled(npm(stream-shift)) = 1.0.3
Provides: bundled(npm(strict-uri-encode)) = 2.0.0
Provides: bundled(npm(string_decoder)) = 0.10.31
Provides: bundled(npm(string_decoder)) = 1.1.1
Provides: bundled(npm(string_decoder)) = 1.3.0
Provides: bundled(npm(string-width)) = 1.0.2
Provides: bundled(npm(string-width)) = 2.1.1
Provides: bundled(npm(string-width)) = 3.1.0
Provides: bundled(npm(string-width)) = 4.2.3
Provides: bundled(npm(string.prototype.trim)) = 1.2.10
Provides: bundled(npm(string.prototype.trimend)) = 1.0.9
Provides: bundled(npm(string.prototype.trimstart)) = 1.0.8
Provides: bundled(npm(stringify-package)) = 1.0.1
Provides: bundled(npm(strip-ansi)) = 3.0.1
Provides: bundled(npm(strip-ansi)) = 4.0.0
Provides: bundled(npm(strip-ansi)) = 5.2.0
Provides: bundled(npm(strip-ansi)) = 6.0.1
Provides: bundled(npm(strip-bom)) = 3.0.0
Provides: bundled(npm(strip-bom)) = 4.0.0
Provides: bundled(npm(strip-eof)) = 1.0.0
Provides: bundled(npm(strip-final-newline)) = 2.0.0
Provides: bundled(npm(strip-indent)) = 3.0.0
Provides: bundled(npm(strip-json-comments)) = 2.0.1
Provides: bundled(npm(strip-json-comments)) = 3.1.1
Provides: bundled(npm(supports-color)) = 5.5.0
Provides: bundled(npm(supports-color)) = 7.2.0
Provides: bundled(npm(supports-hyperlinks)) = 1.0.1
Provides: bundled(npm(supports-preserve-symlinks-flag)) = 1.0.0
Provides: bundled(npm(symbol-observable)) = 1.2.0
Provides: bundled(npm(table-resolver)) = 3.3.0
Provides: bundled(npm(tar)) = 4.4.19
Provides: bundled(npm(temp-dir)) = 1.0.0
Provides: bundled(npm(tempy)) = 0.3.0
Provides: bundled(npm(term-size)) = 1.2.0
Provides: bundled(npm(text-extensions)) = 1.9.0
Provides: bundled(npm(text-table)) = 0.2.0
Provides: bundled(npm(through)) = 2.3.8
Provides: bundled(npm(through2)) = 2.0.5
Provides: bundled(npm(through2)) = 4.0.2
Provides: bundled(npm(timed-out)) = 4.0.1
Provides: bundled(npm(tiny-relative-date)) = 1.3.0
Provides: bundled(npm(tmp)) = 0.0.33
Provides: bundled(npm(to-regex-range)) = 5.0.1
Provides: bundled(npm(tough-cookie)) = 2.5.0
Provides: bundled(npm(tr46)) = 0.0.3
Provides: bundled(npm(traverse)) = 0.6.8
Provides: bundled(npm(trim-newlines)) = 3.0.1
Provides: bundled(npm(tslib)) = 2.8.1
Provides: bundled(npm(tunnel-agent)) = 0.6.0
Provides: bundled(npm(tweetnacl)) = 0.14.5
Provides: bundled(npm(type-fest)) = 0.18.1
Provides: bundled(npm(type-fest)) = 0.21.3
Provides: bundled(npm(type-fest)) = 0.3.1
Provides: bundled(npm(type-fest)) = 0.6.0
Provides: bundled(npm(type-fest)) = 0.8.1
Provides: bundled(npm(typed-array-buffer)) = 1.0.3
Provides: bundled(npm(typed-array-byte-length)) = 1.0.3
Provides: bundled(npm(typed-array-byte-offset)) = 1.0.4
Provides: bundled(npm(typed-array-length)) = 1.0.7
Provides: bundled(npm(typed-styles)) = 0.0.7
Provides: bundled(npm(typedarray)) = 0.0.6
Provides: bundled(npm(uglify-js)) = 3.19.3
Provides: bundled(npm(uid-number)) = 0.0.6
Provides: bundled(npm(umask)) = 1.1.0
Provides: bundled(npm(unbox-primitive)) = 1.1.0
Provides: bundled(npm(uncontrollable)) = 7.2.1
Provides: bundled(npm(undici-types)) = 7.8.0
Provides: bundled(npm(unidiff)) = 1.0.4
Provides: bundled(npm(unique-filename)) = 1.1.1
Provides: bundled(npm(unique-slug)) = 2.0.2
Provides: bundled(npm(unique-string)) = 1.0.0
Provides: bundled(npm(universal-user-agent)) = 4.0.1
Provides: bundled(npm(universal-user-agent)) = 6.0.1
Provides: bundled(npm(universalify)) = 0.1.2
Provides: bundled(npm(universalify)) = 2.0.1
Provides: bundled(npm(unpipe)) = 1.0.0
Provides: bundled(npm(unzip-response)) = 2.0.1
Provides: bundled(npm(update-notifier)) = 2.5.0
Provides: bundled(npm(uri-js)) = 4.4.1
Provides: bundled(npm(url-join)) = 4.0.1
Provides: bundled(npm(url-parse-lax)) = 1.0.0
Provides: bundled(npm(util-deprecate)) = 1.0.2
Provides: bundled(npm(util-extend)) = 1.0.3
Provides: bundled(npm(util-promisify)) = 2.1.0
Provides: bundled(npm(uuid)) = 3.4.0
Provides: bundled(npm(validate-npm-package-license)) = 3.0.4
Provides: bundled(npm(validate-npm-package-name)) = 3.0.0
Provides: bundled(npm(verror)) = 1.10.0
Provides: bundled(npm(warning)) = 3.0.0
Provides: bundled(npm(warning)) = 4.0.3
Provides: bundled(npm(wcwidth)) = 1.0.1
Provides: bundled(npm(webidl-conversions)) = 3.0.1
Provides: bundled(npm(whatwg-url)) = 5.0.0
Provides: bundled(npm(which)) = 1.3.1
Provides: bundled(npm(which)) = 2.0.2
Provides: bundled(npm(which-boxed-primitive)) = 1.1.1
Provides: bundled(npm(which-builtin-type)) = 1.2.1
Provides: bundled(npm(which-collection)) = 1.0.2
Provides: bundled(npm(which-module)) = 2.0.1
Provides: bundled(npm(which-typed-array)) = 1.1.19
Provides: bundled(npm(wide-align)) = 1.1.5
Provides: bundled(npm(widest-line)) = 2.0.1
Provides: bundled(npm(windows-release)) = 3.3.3
Provides: bundled(npm(word-wrap)) = 1.2.5
Provides: bundled(npm(wordwrap)) = 1.0.0
Provides: bundled(npm(worker-farm)) = 1.7.0
Provides: bundled(npm(wrap-ansi)) = 5.1.0
Provides: bundled(npm(wrap-ansi)) = 6.2.0
Provides: bundled(npm(wrap-ansi)) = 7.0.0
Provides: bundled(npm(wrappy)) = 1.0.2
Provides: bundled(npm(write-file-atomic)) = 2.4.3
Provides: bundled(npm(xdg-basedir)) = 3.0.0
Provides: bundled(npm(xtend)) = 4.0.2
Provides: bundled(npm(y18n)) = 4.0.3
Provides: bundled(npm(yallist)) = 2.1.2
Provides: bundled(npm(yallist)) = 3.1.1
Provides: bundled(npm(yallist)) = 4.0.0
Provides: bundled(npm(yaml)) = 1.10.2
Provides: bundled(npm(yargs)) = 14.2.3
Provides: bundled(npm(yargs)) = 15.4.1
Provides: bundled(npm(yargs-parser)) = 15.0.3
Provides: bundled(npm(yargs-parser)) = 18.1.3
Provides: bundled(npm(yargs-parser)) = 20.2.9
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

%setup -T -q -a 913 -D -n %{npm_cache_dir}

%build
%{?scl:scl enable %{?scl_nodejs} - << \end_of_scl}
npm install --legacy-peer-deps --cache-min Infinity --cache %{?scl:../}%{npm_cache_dir} --no-shrinkwrap --no-optional --global-style true %{npm_name}@%{version}
%{?scl:end_of_scl}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/dist %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%doc node_modules/%{npm_name}/CHANGELOG.md
%doc node_modules/%{npm_name}/README.md

%changelog
* Mon Jun 16 2025 MariaAga <mariaaga@redhat.com> 3.0.15-1
- Add nodejs-patternfly-react-extensions generated by npm2rpm using the bundle strategy

