%global npm_name @theforeman/vendor
%global release 1
%global prerelease beta.5

Name: nodejs-theforeman-vendor
Version: 0.1.0
Release: %{?prerelease:0.}%{release}%{?prerelease:.}%{?prerelease}%{?nightly}%{?dist}
Summary: foreman supported 3rd-party node_modules
License: MIT
Group: Development/Libraries
URL: https://github.com/sharvit/foreman-vendor#readme
Source0: https://registry.npmjs.org/@theforeman/vendor/-/@theforeman/vendor-0.1.0-beta.5.tgz
Source1: https://registry.npmjs.org/classnames/-/classnames-2.2.6.tgz
Source2: https://registry.npmjs.org/bootstrap-sass/-/bootstrap-sass-3.4.1.tgz
Source3: https://registry.npmjs.org/babel-plugin-transform-rename-import/-/babel-plugin-transform-rename-import-2.3.0.tgz
Source4: https://registry.npmjs.org/babel-polyfill/-/babel-polyfill-6.26.0.tgz
Source5: https://registry.npmjs.org/copy-webpack-plugin/-/copy-webpack-plugin-4.6.0.tgz
Source6: https://registry.npmjs.org/axios/-/axios-0.17.1.tgz
Source7: https://registry.npmjs.org/datatables.net/-/datatables.net-1.10.19.tgz
Source8: https://registry.npmjs.org/eslint-import-resolver-alias/-/eslint-import-resolver-alias-1.1.2.tgz
Source9: https://registry.npmjs.org/diff/-/diff-3.0.1.tgz
Source10: https://registry.npmjs.org/ipaddr.js/-/ipaddr.js-1.2.0.tgz
Source11: https://registry.npmjs.org/isomorphic-fetch/-/isomorphic-fetch-2.2.1.tgz
Source12: https://registry.npmjs.org/jquery/-/jquery-2.2.4.tgz
Source13: https://registry.npmjs.org/jstz/-/jstz-1.0.11.tgz
Source14: https://registry.npmjs.org/lodash/-/lodash-4.17.11.tgz
Source15: https://registry.npmjs.org/brace/-/brace-0.10.0.tgz
Source16: https://registry.npmjs.org/datatables.net-bs/-/datatables.net-bs-1.10.19.tgz
Source17: https://registry.npmjs.org/jquery.cookie/-/jquery.cookie-1.4.1.tgz
Source18: https://registry.npmjs.org/jquery-ujs/-/jquery-ujs-1.2.2.tgz
Source19: https://registry.npmjs.org/jquery-flot/-/jquery-flot-0.8.3.tgz
Source20: https://registry.npmjs.org/prop-types/-/prop-types-15.7.2.tgz
Source21: https://registry.npmjs.org/multiselect/-/multiselect-0.9.12.tgz
Source22: https://registry.npmjs.org/number_helpers/-/number_helpers-0.1.1.tgz
Source23: https://registry.npmjs.org/react/-/react-16.8.4.tgz
Source24: https://registry.npmjs.org/react-bootstrap/-/react-bootstrap-0.32.1.tgz
Source25: https://registry.npmjs.org/react-dom/-/react-dom-16.8.4.tgz
Source26: https://registry.npmjs.org/react-onclickoutside/-/react-onclickoutside-6.8.0.tgz
Source27: https://registry.npmjs.org/patternfly/-/patternfly-3.59.1.tgz
Source28: https://registry.npmjs.org/@novnc/novnc/-/@novnc/novnc-1.0.0.tgz
Source29: https://registry.npmjs.org/react-redux/-/react-redux-5.1.1.tgz
Source30: https://registry.npmjs.org/redux/-/redux-3.7.2.tgz
Source31: https://registry.npmjs.org/react-numeric-input/-/react-numeric-input-2.2.3.tgz
Source32: https://registry.npmjs.org/react-diff-view/-/react-diff-view-1.8.1.tgz
Source33: https://registry.npmjs.org/react-debounce-input/-/react-debounce-input-3.2.0.tgz
Source34: https://registry.npmjs.org/redux-form/-/redux-form-7.2.0.tgz
Source35: https://registry.npmjs.org/redux-logger/-/redux-logger-2.10.2.tgz
Source36: https://registry.npmjs.org/redux-thunk/-/redux-thunk-2.3.0.tgz
Source37: https://registry.npmjs.org/uuid/-/uuid-3.3.2.tgz
Source38: https://registry.npmjs.org/urijs/-/urijs-1.19.1.tgz
Source39: https://registry.npmjs.org/react-ellipsis-with-tooltip/-/react-ellipsis-with-tooltip-1.0.8.tgz
Source40: https://registry.npmjs.org/react-password-strength/-/react-password-strength-2.3.1.tgz
Source41: https://registry.npmjs.org/babel-runtime/-/babel-runtime-6.26.0.tgz
Source42: https://registry.npmjs.org/regenerator-runtime/-/regenerator-runtime-0.10.5.tgz
Source43: https://registry.npmjs.org/core-js/-/core-js-2.6.5.tgz
Source44: https://registry.npmjs.org/globby/-/globby-7.1.1.tgz
Source45: https://registry.npmjs.org/find-cache-dir/-/find-cache-dir-1.0.0.tgz
Source46: https://registry.npmjs.org/serialize-javascript/-/serialize-javascript-1.6.1.tgz
Source47: https://registry.npmjs.org/cacache/-/cacache-10.0.4.tgz
Source48: https://registry.npmjs.org/is-glob/-/is-glob-4.0.0.tgz
Source49: https://registry.npmjs.org/loader-utils/-/loader-utils-1.2.3.tgz
Source50: https://registry.npmjs.org/p-limit/-/p-limit-1.3.0.tgz
Source51: https://registry.npmjs.org/minimatch/-/minimatch-3.0.4.tgz
Source52: https://registry.npmjs.org/follow-redirects/-/follow-redirects-1.7.0.tgz
Source53: https://registry.npmjs.org/is-buffer/-/is-buffer-1.1.6.tgz
Source54: https://registry.npmjs.org/jquery/-/jquery-3.3.1.tgz
Source55: https://registry.npmjs.org/whatwg-fetch/-/whatwg-fetch-3.0.0.tgz
Source56: https://registry.npmjs.org/node-fetch/-/node-fetch-1.7.3.tgz
Source57: https://registry.npmjs.org/loose-envify/-/loose-envify-1.4.0.tgz
Source58: https://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz
Source59: https://registry.npmjs.org/scheduler/-/scheduler-0.13.4.tgz
Source60: https://registry.npmjs.org/dom-helpers/-/dom-helpers-3.4.0.tgz
Source61: https://registry.npmjs.org/invariant/-/invariant-2.2.4.tgz
Source62: https://registry.npmjs.org/keycode/-/keycode-2.2.0.tgz
Source63: https://registry.npmjs.org/prop-types-extra/-/prop-types-extra-1.1.0.tgz
Source64: https://registry.npmjs.org/react-overlays/-/react-overlays-0.8.3.tgz
Source65: https://registry.npmjs.org/react-prop-types/-/react-prop-types-0.4.0.tgz
Source66: https://registry.npmjs.org/react-transition-group/-/react-transition-group-2.6.0.tgz
Source67: https://registry.npmjs.org/uncontrollable/-/uncontrollable-4.1.0.tgz
Source68: https://registry.npmjs.org/warning/-/warning-3.0.0.tgz
Source69: https://registry.npmjs.org/seamless-immutable/-/seamless-immutable-7.1.4.tgz
Source70: https://registry.npmjs.org/select2/-/select2-3.5.2-browserify.tgz
Source71: https://registry.npmjs.org/redux-form-validators/-/redux-form-validators-2.7.5.tgz
Source72: https://registry.npmjs.org/font-awesome/-/font-awesome-4.7.0.tgz
Source73: https://registry.npmjs.org/jquery/-/jquery-3.2.1.tgz
Source74: https://registry.npmjs.org/bootstrap/-/bootstrap-3.4.1.tgz
Source75: https://registry.npmjs.org/bootstrap-select/-/bootstrap-select-1.12.2.tgz
Source76: https://registry.npmjs.org/bootstrap-touchspin/-/bootstrap-touchspin-3.1.1.tgz
Source77: https://registry.npmjs.org/patternfly-react/-/patternfly-react-2.30.6.tgz
Source78: https://registry.npmjs.org/c3/-/c3-0.4.23.tgz
Source79: https://registry.npmjs.org/w3c-blob/-/w3c-blob-0.0.1.tgz
Source80: https://registry.npmjs.org/react-is/-/react-is-16.8.4.tgz
Source81: https://registry.npmjs.org/bootstrap-datepicker/-/bootstrap-datepicker-1.8.0.tgz
Source82: https://registry.npmjs.org/@types/c3/-/@types/c3-0.6.3.tgz
Source83: https://registry.npmjs.org/bootstrap-switch/-/bootstrap-switch-3.3.4.tgz
Source84: https://registry.npmjs.org/eonasdan-bootstrap-datetimepicker/-/eonasdan-bootstrap-datetimepicker-4.17.47.tgz
Source85: https://registry.npmjs.org/bootstrap-slider/-/bootstrap-slider-9.10.0.tgz
Source86: https://registry.npmjs.org/google-code-prettify/-/google-code-prettify-1.0.5.tgz
Source87: https://registry.npmjs.org/d3/-/d3-3.5.17.tgz
Source88: https://registry.npmjs.org/moment/-/moment-2.24.0.tgz
Source89: https://registry.npmjs.org/moment-timezone/-/moment-timezone-0.4.1.tgz
Source90: https://registry.npmjs.org/datatables.net-colreorder/-/datatables.net-colreorder-1.5.1.tgz
Source91: https://registry.npmjs.org/datatables.net-colreorder-bs/-/datatables.net-colreorder-bs-1.3.3.tgz
Source92: https://registry.npmjs.org/hoist-non-react-statics/-/hoist-non-react-statics-3.3.0.tgz
Source93: https://registry.npmjs.org/datatables.net-select/-/datatables.net-select-1.2.7.tgz
Source94: https://registry.npmjs.org/@babel/runtime/-/@babel/runtime-7.3.4.tgz
Source95: https://registry.npmjs.org/react-lifecycles-compat/-/react-lifecycles-compat-3.0.4.tgz
Source96: https://registry.npmjs.org/lodash-es/-/lodash-es-4.17.11.tgz
Source97: https://registry.npmjs.org/symbol-observable/-/symbol-observable-1.2.0.tgz
Source98: https://registry.npmjs.org/leven/-/leven-2.1.0.tgz
Source99: https://registry.npmjs.org/lodash.escape/-/lodash.escape-4.0.1.tgz
Source100: https://registry.npmjs.org/drmonty-datatables-colvis/-/drmonty-datatables-colvis-1.1.2.tgz
Source101: https://registry.npmjs.org/font-awesome-sass/-/font-awesome-sass-4.7.0.tgz
Source102: https://registry.npmjs.org/warning/-/warning-4.0.3.tgz
Source103: https://registry.npmjs.org/jquery-match-height/-/jquery-match-height-0.7.2.tgz
Source104: https://registry.npmjs.org/lodash.debounce/-/lodash.debounce-4.0.8.tgz
Source105: https://registry.npmjs.org/deep-equal/-/deep-equal-1.0.1.tgz
Source106: https://registry.npmjs.org/patternfly-bootstrap-combobox/-/patternfly-bootstrap-combobox-1.1.7.tgz
Source107: https://registry.npmjs.org/es6-error/-/es6-error-4.1.1.tgz
Source108: https://registry.npmjs.org/hoist-non-react-statics/-/hoist-non-react-statics-2.5.5.tgz
Source109: https://registry.npmjs.org/patternfly-bootstrap-treeview/-/patternfly-bootstrap-treeview-2.1.8.tgz
Source110: https://registry.npmjs.org/is-promise/-/is-promise-2.1.0.tgz
Source111: https://registry.npmjs.org/deep-diff/-/deep-diff-0.3.4.tgz
Source112: https://registry.npmjs.org/regenerator-runtime/-/regenerator-runtime-0.11.1.tgz
Source113: https://registry.npmjs.org/array-union/-/array-union-1.0.2.tgz
Source114: https://registry.npmjs.org/dir-glob/-/dir-glob-2.2.2.tgz
Source115: https://registry.npmjs.org/pify/-/pify-3.0.0.tgz
Source116: https://registry.npmjs.org/ignore/-/ignore-3.3.10.tgz
Source117: https://registry.npmjs.org/glob/-/glob-7.1.3.tgz
Source118: https://registry.npmjs.org/commondir/-/commondir-1.0.1.tgz
Source119: https://registry.npmjs.org/slash/-/slash-1.0.0.tgz
Source120: https://registry.npmjs.org/make-dir/-/make-dir-1.3.0.tgz
Source121: https://registry.npmjs.org/pkg-dir/-/pkg-dir-2.0.0.tgz
Source122: https://registry.npmjs.org/chownr/-/chownr-1.1.1.tgz
Source123: https://registry.npmjs.org/gitdiff-parser/-/gitdiff-parser-0.1.2.tgz
Source124: https://registry.npmjs.org/bluebird/-/bluebird-3.5.3.tgz
Source125: https://registry.npmjs.org/mississippi/-/mississippi-2.0.0.tgz
Source126: https://registry.npmjs.org/graceful-fs/-/graceful-fs-4.1.15.tgz
Source127: https://registry.npmjs.org/lru-cache/-/lru-cache-4.1.5.tgz
Source128: https://registry.npmjs.org/lodash.mapvalues/-/lodash.mapvalues-4.6.0.tgz
Source129: https://registry.npmjs.org/lodash.findlastindex/-/lodash.findlastindex-4.6.0.tgz
Source130: https://registry.npmjs.org/move-concurrently/-/move-concurrently-1.0.1.tgz
Source131: https://registry.npmjs.org/promise-inflight/-/promise-inflight-1.0.1.tgz
Source132: https://registry.npmjs.org/rimraf/-/rimraf-2.6.3.tgz
Source133: https://registry.npmjs.org/unique-filename/-/unique-filename-1.1.1.tgz
Source134: https://registry.npmjs.org/mkdirp/-/mkdirp-0.5.1.tgz
Source135: https://registry.npmjs.org/ssri/-/ssri-5.3.0.tgz
Source136: https://registry.npmjs.org/y18n/-/y18n-4.0.0.tgz
Source137: https://registry.npmjs.org/is-extglob/-/is-extglob-2.1.1.tgz
Source138: https://registry.npmjs.org/big.js/-/big.js-5.2.2.tgz
Source139: https://registry.npmjs.org/emojis-list/-/emojis-list-2.1.0.tgz
Source140: https://registry.npmjs.org/p-try/-/p-try-1.0.0.tgz
Source141: https://registry.npmjs.org/json5/-/json5-1.0.1.tgz
Source142: https://registry.npmjs.org/brace-expansion/-/brace-expansion-1.1.11.tgz
Source143: https://registry.npmjs.org/debug/-/debug-3.2.6.tgz
Source144: https://registry.npmjs.org/is-stream/-/is-stream-1.1.0.tgz
Source145: https://registry.npmjs.org/encoding/-/encoding-0.1.12.tgz
Source146: https://registry.npmjs.org/js-tokens/-/js-tokens-4.0.0.tgz
Source147: https://registry.npmjs.org/react-bootstrap/-/react-bootstrap-0.32.4.tgz
Source148: https://registry.npmjs.org/react-bootstrap-typeahead/-/react-bootstrap-typeahead-3.4.1.tgz
Source149: https://registry.npmjs.org/zxcvbn/-/zxcvbn-4.4.2.tgz
Source150: https://registry.npmjs.org/breakjs/-/breakjs-1.0.0.tgz
Source151: https://registry.npmjs.org/css-element-queries/-/css-element-queries-1.1.1.tgz
Source152: https://registry.npmjs.org/bootstrap-slider-without-jquery/-/bootstrap-slider-without-jquery-10.0.0.tgz
Source153: https://registry.npmjs.org/react-bootstrap-switch/-/react-bootstrap-switch-15.5.3.tgz
Source154: https://registry.npmjs.org/react-motion/-/react-motion-0.5.2.tgz
Source155: https://registry.npmjs.org/recompose/-/recompose-0.26.0.tgz
Source156: https://registry.npmjs.org/react-c3js/-/react-c3js-0.1.20.tgz
Source157: https://registry.npmjs.org/react-click-outside/-/react-click-outside-3.0.1.tgz
Source158: https://registry.npmjs.org/react-collapse/-/react-collapse-4.0.3.tgz
Source159: https://registry.npmjs.org/@types/d3/-/@types/d3-4.13.1.tgz
Source160: https://registry.npmjs.org/datatables.net-bs/-/datatables.net-bs-2.1.1.tgz
Source161: https://registry.npmjs.org/regenerator-runtime/-/regenerator-runtime-0.12.1.tgz
Source162: https://registry.npmjs.org/react-fontawesome/-/react-fontawesome-1.6.1.tgz
Source163: https://registry.npmjs.org/array-uniq/-/array-uniq-1.0.3.tgz
Source164: https://registry.npmjs.org/fs.realpath/-/fs.realpath-1.0.0.tgz
Source165: https://registry.npmjs.org/path-type/-/path-type-3.0.0.tgz
Source166: https://registry.npmjs.org/inflight/-/inflight-1.0.6.tgz
Source167: https://registry.npmjs.org/inherits/-/inherits-2.0.3.tgz
Source168: https://registry.npmjs.org/once/-/once-1.4.0.tgz
Source169: https://registry.npmjs.org/path-is-absolute/-/path-is-absolute-1.0.1.tgz
Source170: https://registry.npmjs.org/find-up/-/find-up-2.1.0.tgz
Source171: https://registry.npmjs.org/duplexify/-/duplexify-3.7.1.tgz
Source172: https://registry.npmjs.org/concat-stream/-/concat-stream-1.6.2.tgz
Source173: https://registry.npmjs.org/end-of-stream/-/end-of-stream-1.4.1.tgz
Source174: https://registry.npmjs.org/flush-write-stream/-/flush-write-stream-1.1.1.tgz
Source175: https://registry.npmjs.org/from2/-/from2-2.3.0.tgz
Source176: https://registry.npmjs.org/pump/-/pump-2.0.1.tgz
Source177: https://registry.npmjs.org/parallel-transform/-/parallel-transform-1.1.0.tgz
Source178: https://registry.npmjs.org/pumpify/-/pumpify-1.5.1.tgz
Source179: https://registry.npmjs.org/stream-each/-/stream-each-1.2.3.tgz
Source180: https://registry.npmjs.org/through2/-/through2-2.0.5.tgz
Source181: https://registry.npmjs.org/copy-concurrently/-/copy-concurrently-1.0.5.tgz
Source182: https://registry.npmjs.org/yallist/-/yallist-2.1.2.tgz
Source183: https://registry.npmjs.org/aproba/-/aproba-1.2.0.tgz
Source184: https://registry.npmjs.org/fs-write-stream-atomic/-/fs-write-stream-atomic-1.0.10.tgz
Source185: https://registry.npmjs.org/unique-slug/-/unique-slug-2.0.1.tgz
Source186: https://registry.npmjs.org/minimist/-/minimist-0.0.8.tgz
Source187: https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.1.2.tgz
Source188: https://registry.npmjs.org/minimist/-/minimist-1.2.0.tgz
Source189: https://registry.npmjs.org/run-queue/-/run-queue-1.0.3.tgz
Source190: https://registry.npmjs.org/balanced-match/-/balanced-match-1.0.0.tgz
Source191: https://registry.npmjs.org/ms/-/ms-2.1.1.tgz
Source192: https://registry.npmjs.org/concat-map/-/concat-map-0.0.1.tgz
Source193: https://registry.npmjs.org/iconv-lite/-/iconv-lite-0.4.24.tgz
Source194: https://registry.npmjs.org/@babel/runtime-corejs2/-/@babel/runtime-corejs2-7.3.4.tgz
Source195: https://registry.npmjs.org/uncontrollable/-/uncontrollable-5.1.0.tgz
Source196: https://registry.npmjs.org/escape-string-regexp/-/escape-string-regexp-1.0.5.tgz
Source197: https://registry.npmjs.org/create-react-context/-/create-react-context-0.2.3.tgz
Source198: https://registry.npmjs.org/reactabular-table/-/reactabular-table-8.14.0.tgz
Source199: https://registry.npmjs.org/sortabular/-/sortabular-1.6.0.tgz
Source200: https://registry.npmjs.org/table-resolver/-/table-resolver-3.3.0.tgz
Source201: https://registry.npmjs.org/performance-now/-/performance-now-0.2.0.tgz
Source202: https://registry.npmjs.org/change-emitter/-/change-emitter-0.1.6.tgz
Source203: https://registry.npmjs.org/fbjs/-/fbjs-0.8.17.tgz
Source204: https://registry.npmjs.org/raf/-/raf-3.4.1.tgz
Source205: https://registry.npmjs.org/@types/d3-array/-/@types/d3-array-1.2.6.tgz
Source206: https://registry.npmjs.org/@types/d3-scale/-/@types/d3-scale-1.0.14.tgz
Source207: https://registry.npmjs.org/@types/d3-brush/-/@types/d3-brush-1.0.10.tgz
Source208: https://registry.npmjs.org/@types/d3-axis/-/@types/d3-axis-1.0.12.tgz
Source209: https://registry.npmjs.org/@types/d3-chord/-/@types/d3-chord-1.0.9.tgz
Source210: https://registry.npmjs.org/@types/d3-collection/-/@types/d3-collection-1.0.8.tgz
Source211: https://registry.npmjs.org/@types/d3-color/-/@types/d3-color-1.2.2.tgz
Source212: https://registry.npmjs.org/@types/d3-dispatch/-/@types/d3-dispatch-1.0.7.tgz
Source213: https://registry.npmjs.org/@types/d3-drag/-/@types/d3-drag-1.2.3.tgz
Source214: https://registry.npmjs.org/@types/d3-dsv/-/@types/d3-dsv-1.0.36.tgz
Source215: https://registry.npmjs.org/@types/d3-ease/-/@types/d3-ease-1.0.8.tgz
Source216: https://registry.npmjs.org/@types/d3-format/-/@types/d3-format-1.3.1.tgz
Source217: https://registry.npmjs.org/@types/d3-force/-/@types/d3-force-1.2.1.tgz
Source218: https://registry.npmjs.org/@types/d3-geo/-/@types/d3-geo-1.11.1.tgz
Source219: https://registry.npmjs.org/@types/d3-interpolate/-/@types/d3-interpolate-1.3.1.tgz
Source220: https://registry.npmjs.org/@types/d3-path/-/@types/d3-path-1.0.8.tgz
Source221: https://registry.npmjs.org/@types/d3-hierarchy/-/@types/d3-hierarchy-1.1.6.tgz
Source222: https://registry.npmjs.org/@types/d3-polygon/-/@types/d3-polygon-1.0.7.tgz
Source223: https://registry.npmjs.org/@types/d3-quadtree/-/@types/d3-quadtree-1.0.7.tgz
Source224: https://registry.npmjs.org/@types/d3-queue/-/@types/d3-queue-3.0.8.tgz
Source225: https://registry.npmjs.org/@types/d3-random/-/@types/d3-random-1.1.2.tgz
Source226: https://registry.npmjs.org/@types/d3-request/-/@types/d3-request-1.0.5.tgz
Source227: https://registry.npmjs.org/@types/d3-shape/-/@types/d3-shape-1.3.1.tgz
Source228: https://registry.npmjs.org/@types/d3-selection/-/@types/d3-selection-1.4.1.tgz
Source229: https://registry.npmjs.org/@types/d3-time/-/@types/d3-time-1.0.10.tgz
Source230: https://registry.npmjs.org/@types/d3-time-format/-/@types/d3-time-format-2.1.1.tgz
Source231: https://registry.npmjs.org/@types/d3-timer/-/@types/d3-timer-1.0.9.tgz
Source232: https://registry.npmjs.org/@types/d3-voronoi/-/@types/d3-voronoi-1.1.9.tgz
Source233: https://registry.npmjs.org/datatables.net/-/datatables.net-2.1.1.tgz
Source234: https://registry.npmjs.org/@types/d3-transition/-/@types/d3-transition-1.1.4.tgz
Source235: https://registry.npmjs.org/@types/d3-zoom/-/@types/d3-zoom-1.7.4.tgz
Source236: https://registry.npmjs.org/wrappy/-/wrappy-1.0.2.tgz
Source237: https://registry.npmjs.org/locate-path/-/locate-path-2.0.0.tgz
Source238: https://registry.npmjs.org/readable-stream/-/readable-stream-2.3.6.tgz
Source239: https://registry.npmjs.org/buffer-from/-/buffer-from-1.1.1.tgz
Source240: https://registry.npmjs.org/stream-shift/-/stream-shift-1.0.0.tgz
Source241: https://registry.npmjs.org/typedarray/-/typedarray-0.0.6.tgz
Source242: https://registry.npmjs.org/cyclist/-/cyclist-0.2.2.tgz
Source243: https://registry.npmjs.org/xtend/-/xtend-4.0.1.tgz
Source244: https://registry.npmjs.org/iferr/-/iferr-0.1.5.tgz
Source245: https://registry.npmjs.org/imurmurhash/-/imurmurhash-0.1.4.tgz
Source246: https://registry.npmjs.org/safer-buffer/-/safer-buffer-2.1.2.tgz
Source247: https://registry.npmjs.org/gud/-/gud-1.0.0.tgz
Source248: https://registry.npmjs.org/core-js/-/core-js-1.2.7.tgz
Source249: https://registry.npmjs.org/promise/-/promise-7.3.1.tgz
Source250: https://registry.npmjs.org/setimmediate/-/setimmediate-1.0.5.tgz
Source251: https://registry.npmjs.org/performance-now/-/performance-now-2.1.0.tgz
Source252: https://registry.npmjs.org/ua-parser-js/-/ua-parser-js-0.7.19.tgz
Source253: https://registry.npmjs.org/p-locate/-/p-locate-2.0.0.tgz
Source254: https://registry.npmjs.org/react-popper/-/react-popper-1.3.3.tgz
Source255: https://registry.npmjs.org/core-util-is/-/core-util-is-1.0.2.tgz
Source256: https://registry.npmjs.org/path-exists/-/path-exists-3.0.0.tgz
Source257: https://registry.npmjs.org/isarray/-/isarray-1.0.0.tgz
Source258: https://registry.npmjs.org/process-nextick-args/-/process-nextick-args-2.0.0.tgz
Source259: https://registry.npmjs.org/util-deprecate/-/util-deprecate-1.0.2.tgz
Source260: https://registry.npmjs.org/string_decoder/-/string_decoder-1.1.1.tgz
Source261: https://registry.npmjs.org/asap/-/asap-2.0.6.tgz
Source262: https://registry.npmjs.org/create-react-context/-/create-react-context-0.2.2.tgz
Source263: https://registry.npmjs.org/popper.js/-/popper.js-1.14.7.tgz
Source264: https://registry.npmjs.org/@types/geojson/-/@types/geojson-7946.0.6.tgz
Source265: https://registry.npmjs.org/typed-styles/-/typed-styles-0.0.7.tgz
Source266: https://registry.npmjs.org/pseudomap/-/pseudomap-1.0.2.tgz
Source267: %{name}-%{version}%{?prerelease:-}%{?prerelease}-registry.npmjs.org.tgz
BuildRequires: nodejs-packaging
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: npm(%{npm_name}) = %{version}
Provides: bundled(npm(@babel/runtime)) = 7.3.4
Provides: bundled(npm(@babel/runtime-corejs2)) = 7.3.4
Provides: bundled(npm(@novnc/novnc)) = 1.0.0
Provides: bundled(npm(@theforeman/vendor)) = 0.1.0-beta.5
Provides: bundled(npm(@types/c3)) = 0.6.3
Provides: bundled(npm(@types/d3)) = 4.13.1
Provides: bundled(npm(@types/d3-array)) = 1.2.6
Provides: bundled(npm(@types/d3-axis)) = 1.0.12
Provides: bundled(npm(@types/d3-brush)) = 1.0.10
Provides: bundled(npm(@types/d3-chord)) = 1.0.9
Provides: bundled(npm(@types/d3-collection)) = 1.0.8
Provides: bundled(npm(@types/d3-color)) = 1.2.2
Provides: bundled(npm(@types/d3-dispatch)) = 1.0.7
Provides: bundled(npm(@types/d3-drag)) = 1.2.3
Provides: bundled(npm(@types/d3-dsv)) = 1.0.36
Provides: bundled(npm(@types/d3-ease)) = 1.0.8
Provides: bundled(npm(@types/d3-force)) = 1.2.1
Provides: bundled(npm(@types/d3-format)) = 1.3.1
Provides: bundled(npm(@types/d3-geo)) = 1.11.1
Provides: bundled(npm(@types/d3-hierarchy)) = 1.1.6
Provides: bundled(npm(@types/d3-interpolate)) = 1.3.1
Provides: bundled(npm(@types/d3-path)) = 1.0.8
Provides: bundled(npm(@types/d3-polygon)) = 1.0.7
Provides: bundled(npm(@types/d3-quadtree)) = 1.0.7
Provides: bundled(npm(@types/d3-queue)) = 3.0.8
Provides: bundled(npm(@types/d3-random)) = 1.1.2
Provides: bundled(npm(@types/d3-request)) = 1.0.5
Provides: bundled(npm(@types/d3-scale)) = 1.0.14
Provides: bundled(npm(@types/d3-selection)) = 1.4.1
Provides: bundled(npm(@types/d3-shape)) = 1.3.1
Provides: bundled(npm(@types/d3-time)) = 1.0.10
Provides: bundled(npm(@types/d3-time-format)) = 2.1.1
Provides: bundled(npm(@types/d3-timer)) = 1.0.9
Provides: bundled(npm(@types/d3-transition)) = 1.1.4
Provides: bundled(npm(@types/d3-voronoi)) = 1.1.9
Provides: bundled(npm(@types/d3-zoom)) = 1.7.4
Provides: bundled(npm(@types/geojson)) = 7946.0.6
Provides: bundled(npm(aproba)) = 1.2.0
Provides: bundled(npm(array-union)) = 1.0.2
Provides: bundled(npm(array-uniq)) = 1.0.3
Provides: bundled(npm(asap)) = 2.0.6
Provides: bundled(npm(axios)) = 0.17.1
Provides: bundled(npm(babel-plugin-transform-rename-import)) = 2.3.0
Provides: bundled(npm(babel-polyfill)) = 6.26.0
Provides: bundled(npm(babel-runtime)) = 6.26.0
Provides: bundled(npm(balanced-match)) = 1.0.0
Provides: bundled(npm(big.js)) = 5.2.2
Provides: bundled(npm(bluebird)) = 3.5.3
Provides: bundled(npm(bootstrap)) = 3.4.1
Provides: bundled(npm(bootstrap-datepicker)) = 1.8.0
Provides: bundled(npm(bootstrap-sass)) = 3.4.1
Provides: bundled(npm(bootstrap-select)) = 1.12.2
Provides: bundled(npm(bootstrap-slider)) = 9.10.0
Provides: bundled(npm(bootstrap-slider-without-jquery)) = 10.0.0
Provides: bundled(npm(bootstrap-switch)) = 3.3.4
Provides: bundled(npm(bootstrap-touchspin)) = 3.1.1
Provides: bundled(npm(brace)) = 0.10.0
Provides: bundled(npm(brace-expansion)) = 1.1.11
Provides: bundled(npm(breakjs)) = 1.0.0
Provides: bundled(npm(buffer-from)) = 1.1.1
Provides: bundled(npm(c3)) = 0.4.23
Provides: bundled(npm(cacache)) = 10.0.4
Provides: bundled(npm(change-emitter)) = 0.1.6
Provides: bundled(npm(chownr)) = 1.1.1
Provides: bundled(npm(classnames)) = 2.2.6
Provides: bundled(npm(commondir)) = 1.0.1
Provides: bundled(npm(concat-map)) = 0.0.1
Provides: bundled(npm(concat-stream)) = 1.6.2
Provides: bundled(npm(copy-concurrently)) = 1.0.5
Provides: bundled(npm(copy-webpack-plugin)) = 4.6.0
Provides: bundled(npm(core-js)) = 1.2.7
Provides: bundled(npm(core-js)) = 2.6.5
Provides: bundled(npm(core-util-is)) = 1.0.2
Provides: bundled(npm(create-react-context)) = 0.2.3
Provides: bundled(npm(create-react-context)) = 0.2.2
Provides: bundled(npm(css-element-queries)) = 1.1.1
Provides: bundled(npm(cyclist)) = 0.2.2
Provides: bundled(npm(d3)) = 3.5.17
Provides: bundled(npm(datatables.net)) = 2.1.1
Provides: bundled(npm(datatables.net)) = 1.10.19
Provides: bundled(npm(datatables.net-bs)) = 1.10.19
Provides: bundled(npm(datatables.net-bs)) = 2.1.1
Provides: bundled(npm(datatables.net-colreorder)) = 1.5.1
Provides: bundled(npm(datatables.net-colreorder-bs)) = 1.3.3
Provides: bundled(npm(datatables.net-select)) = 1.2.7
Provides: bundled(npm(debug)) = 3.2.6
Provides: bundled(npm(deep-diff)) = 0.3.4
Provides: bundled(npm(deep-equal)) = 1.0.1
Provides: bundled(npm(diff)) = 3.0.1
Provides: bundled(npm(dir-glob)) = 2.2.2
Provides: bundled(npm(dom-helpers)) = 3.4.0
Provides: bundled(npm(drmonty-datatables-colvis)) = 1.1.2
Provides: bundled(npm(duplexify)) = 3.7.1
Provides: bundled(npm(emojis-list)) = 2.1.0
Provides: bundled(npm(encoding)) = 0.1.12
Provides: bundled(npm(end-of-stream)) = 1.4.1
Provides: bundled(npm(eonasdan-bootstrap-datetimepicker)) = 4.17.47
Provides: bundled(npm(es6-error)) = 4.1.1
Provides: bundled(npm(escape-string-regexp)) = 1.0.5
Provides: bundled(npm(eslint-import-resolver-alias)) = 1.1.2
Provides: bundled(npm(fbjs)) = 0.8.17
Provides: bundled(npm(find-cache-dir)) = 1.0.0
Provides: bundled(npm(find-up)) = 2.1.0
Provides: bundled(npm(flush-write-stream)) = 1.1.1
Provides: bundled(npm(follow-redirects)) = 1.7.0
Provides: bundled(npm(font-awesome)) = 4.7.0
Provides: bundled(npm(font-awesome-sass)) = 4.7.0
Provides: bundled(npm(from2)) = 2.3.0
Provides: bundled(npm(fs-write-stream-atomic)) = 1.0.10
Provides: bundled(npm(fs.realpath)) = 1.0.0
Provides: bundled(npm(gitdiff-parser)) = 0.1.2
Provides: bundled(npm(glob)) = 7.1.3
Provides: bundled(npm(globby)) = 7.1.1
Provides: bundled(npm(google-code-prettify)) = 1.0.5
Provides: bundled(npm(graceful-fs)) = 4.1.15
Provides: bundled(npm(gud)) = 1.0.0
Provides: bundled(npm(hoist-non-react-statics)) = 2.5.5
Provides: bundled(npm(hoist-non-react-statics)) = 3.3.0
Provides: bundled(npm(iconv-lite)) = 0.4.24
Provides: bundled(npm(iferr)) = 0.1.5
Provides: bundled(npm(ignore)) = 3.3.10
Provides: bundled(npm(imurmurhash)) = 0.1.4
Provides: bundled(npm(inflight)) = 1.0.6
Provides: bundled(npm(inherits)) = 2.0.3
Provides: bundled(npm(invariant)) = 2.2.4
Provides: bundled(npm(ipaddr.js)) = 1.2.0
Provides: bundled(npm(is-buffer)) = 1.1.6
Provides: bundled(npm(is-extglob)) = 2.1.1
Provides: bundled(npm(is-glob)) = 4.0.0
Provides: bundled(npm(is-promise)) = 2.1.0
Provides: bundled(npm(is-stream)) = 1.1.0
Provides: bundled(npm(isarray)) = 1.0.0
Provides: bundled(npm(isomorphic-fetch)) = 2.2.1
Provides: bundled(npm(jquery)) = 3.3.1
Provides: bundled(npm(jquery)) = 2.2.4
Provides: bundled(npm(jquery)) = 3.2.1
Provides: bundled(npm(jquery-flot)) = 0.8.3
Provides: bundled(npm(jquery-match-height)) = 0.7.2
Provides: bundled(npm(jquery-ujs)) = 1.2.2
Provides: bundled(npm(jquery.cookie)) = 1.4.1
Provides: bundled(npm(js-tokens)) = 4.0.0
Provides: bundled(npm(json5)) = 1.0.1
Provides: bundled(npm(jstz)) = 1.0.11
Provides: bundled(npm(keycode)) = 2.2.0
Provides: bundled(npm(leven)) = 2.1.0
Provides: bundled(npm(loader-utils)) = 1.2.3
Provides: bundled(npm(locate-path)) = 2.0.0
Provides: bundled(npm(lodash)) = 4.17.11
Provides: bundled(npm(lodash-es)) = 4.17.11
Provides: bundled(npm(lodash.debounce)) = 4.0.8
Provides: bundled(npm(lodash.escape)) = 4.0.1
Provides: bundled(npm(lodash.findlastindex)) = 4.6.0
Provides: bundled(npm(lodash.mapvalues)) = 4.6.0
Provides: bundled(npm(loose-envify)) = 1.4.0
Provides: bundled(npm(lru-cache)) = 4.1.5
Provides: bundled(npm(make-dir)) = 1.3.0
Provides: bundled(npm(minimatch)) = 3.0.4
Provides: bundled(npm(minimist)) = 0.0.8
Provides: bundled(npm(minimist)) = 1.2.0
Provides: bundled(npm(mississippi)) = 2.0.0
Provides: bundled(npm(mkdirp)) = 0.5.1
Provides: bundled(npm(moment)) = 2.24.0
Provides: bundled(npm(moment-timezone)) = 0.4.1
Provides: bundled(npm(move-concurrently)) = 1.0.1
Provides: bundled(npm(ms)) = 2.1.1
Provides: bundled(npm(multiselect)) = 0.9.12
Provides: bundled(npm(node-fetch)) = 1.7.3
Provides: bundled(npm(number_helpers)) = 0.1.1
Provides: bundled(npm(object-assign)) = 4.1.1
Provides: bundled(npm(once)) = 1.4.0
Provides: bundled(npm(p-limit)) = 1.3.0
Provides: bundled(npm(p-locate)) = 2.0.0
Provides: bundled(npm(p-try)) = 1.0.0
Provides: bundled(npm(parallel-transform)) = 1.1.0
Provides: bundled(npm(path-exists)) = 3.0.0
Provides: bundled(npm(path-is-absolute)) = 1.0.1
Provides: bundled(npm(path-type)) = 3.0.0
Provides: bundled(npm(patternfly)) = 3.59.1
Provides: bundled(npm(patternfly-bootstrap-combobox)) = 1.1.7
Provides: bundled(npm(patternfly-bootstrap-treeview)) = 2.1.8
Provides: bundled(npm(patternfly-react)) = 2.30.6
Provides: bundled(npm(performance-now)) = 2.1.0
Provides: bundled(npm(performance-now)) = 0.2.0
Provides: bundled(npm(pify)) = 3.0.0
Provides: bundled(npm(pkg-dir)) = 2.0.0
Provides: bundled(npm(popper.js)) = 1.14.7
Provides: bundled(npm(process-nextick-args)) = 2.0.0
Provides: bundled(npm(promise)) = 7.3.1
Provides: bundled(npm(promise-inflight)) = 1.0.1
Provides: bundled(npm(prop-types)) = 15.7.2
Provides: bundled(npm(prop-types-extra)) = 1.1.0
Provides: bundled(npm(pseudomap)) = 1.0.2
Provides: bundled(npm(pump)) = 2.0.1
Provides: bundled(npm(pumpify)) = 1.5.1
Provides: bundled(npm(raf)) = 3.4.1
Provides: bundled(npm(react)) = 16.8.4
Provides: bundled(npm(react-bootstrap)) = 0.32.1
Provides: bundled(npm(react-bootstrap)) = 0.32.4
Provides: bundled(npm(react-bootstrap-switch)) = 15.5.3
Provides: bundled(npm(react-bootstrap-typeahead)) = 3.4.1
Provides: bundled(npm(react-c3js)) = 0.1.20
Provides: bundled(npm(react-click-outside)) = 3.0.1
Provides: bundled(npm(react-collapse)) = 4.0.3
Provides: bundled(npm(react-debounce-input)) = 3.2.0
Provides: bundled(npm(react-diff-view)) = 1.8.1
Provides: bundled(npm(react-dom)) = 16.8.4
Provides: bundled(npm(react-ellipsis-with-tooltip)) = 1.0.8
Provides: bundled(npm(react-fontawesome)) = 1.6.1
Provides: bundled(npm(react-is)) = 16.8.4
Provides: bundled(npm(react-lifecycles-compat)) = 3.0.4
Provides: bundled(npm(react-motion)) = 0.5.2
Provides: bundled(npm(react-numeric-input)) = 2.2.3
Provides: bundled(npm(react-onclickoutside)) = 6.8.0
Provides: bundled(npm(react-overlays)) = 0.8.3
Provides: bundled(npm(react-password-strength)) = 2.3.1
Provides: bundled(npm(react-popper)) = 1.3.3
Provides: bundled(npm(react-prop-types)) = 0.4.0
Provides: bundled(npm(react-redux)) = 5.1.1
Provides: bundled(npm(react-transition-group)) = 2.6.0
Provides: bundled(npm(reactabular-table)) = 8.14.0
Provides: bundled(npm(readable-stream)) = 2.3.6
Provides: bundled(npm(recompose)) = 0.26.0
Provides: bundled(npm(redux)) = 3.7.2
Provides: bundled(npm(redux-form)) = 7.2.0
Provides: bundled(npm(redux-form-validators)) = 2.7.5
Provides: bundled(npm(redux-logger)) = 2.10.2
Provides: bundled(npm(redux-thunk)) = 2.3.0
Provides: bundled(npm(regenerator-runtime)) = 0.11.1
Provides: bundled(npm(regenerator-runtime)) = 0.10.5
Provides: bundled(npm(regenerator-runtime)) = 0.12.1
Provides: bundled(npm(rimraf)) = 2.6.3
Provides: bundled(npm(run-queue)) = 1.0.3
Provides: bundled(npm(safe-buffer)) = 5.1.2
Provides: bundled(npm(safer-buffer)) = 2.1.2
Provides: bundled(npm(scheduler)) = 0.13.4
Provides: bundled(npm(seamless-immutable)) = 7.1.4
Provides: bundled(npm(select2)) = 3.5.2-browserify
Provides: bundled(npm(serialize-javascript)) = 1.6.1
Provides: bundled(npm(setimmediate)) = 1.0.5
Provides: bundled(npm(slash)) = 1.0.0
Provides: bundled(npm(sortabular)) = 1.6.0
Provides: bundled(npm(ssri)) = 5.3.0
Provides: bundled(npm(stream-each)) = 1.2.3
Provides: bundled(npm(stream-shift)) = 1.0.0
Provides: bundled(npm(string_decoder)) = 1.1.1
Provides: bundled(npm(symbol-observable)) = 1.2.0
Provides: bundled(npm(table-resolver)) = 3.3.0
Provides: bundled(npm(through2)) = 2.0.5
Provides: bundled(npm(typed-styles)) = 0.0.7
Provides: bundled(npm(typedarray)) = 0.0.6
Provides: bundled(npm(ua-parser-js)) = 0.7.19
Provides: bundled(npm(uncontrollable)) = 5.1.0
Provides: bundled(npm(uncontrollable)) = 4.1.0
Provides: bundled(npm(unique-filename)) = 1.1.1
Provides: bundled(npm(unique-slug)) = 2.0.1
Provides: bundled(npm(urijs)) = 1.19.1
Provides: bundled(npm(util-deprecate)) = 1.0.2
Provides: bundled(npm(uuid)) = 3.3.2
Provides: bundled(npm(w3c-blob)) = 0.0.1
Provides: bundled(npm(warning)) = 4.0.3
Provides: bundled(npm(warning)) = 3.0.0
Provides: bundled(npm(whatwg-fetch)) = 3.0.0
Provides: bundled(npm(wrappy)) = 1.0.2
Provides: bundled(npm(xtend)) = 4.0.1
Provides: bundled(npm(y18n)) = 4.0.0
Provides: bundled(npm(yallist)) = 2.1.2
Provides: bundled(npm(zxcvbn)) = 4.4.2
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
%setup -T -q -a 267 -D -n %{npm_cache_dir}

%build
npm install --cache-min Infinity --cache %{npm_cache_dir} --no-shrinkwrap --no-optional --global-style true %{npm_name}@%{version}%{?prerelease:-}%{?prerelease}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/babel.preset.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/dist %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/eslint.extends.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/lib %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/scss %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/webpack.plugin.js %{buildroot}%{nodejs_sitelib}/%{npm_name}

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%license node_modules/%{npm_name}/license
%doc node_modules/%{npm_name}/readme.md

%changelog
* Wed Mar 13 2019 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.1.0-beta.5-1
- Add nodejs-theforeman-vendor generated by npm2rpm using the bundle strategy

