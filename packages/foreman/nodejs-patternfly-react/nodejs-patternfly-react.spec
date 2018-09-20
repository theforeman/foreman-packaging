%global npm_name patternfly-react
%global enable_tests 1

Name: nodejs-%{npm_name}
Version: 2.18.0
Release: 1%{?dist}
Summary: This library provides a set of common React components for use with the PatternFly reference implementation
License: ASL 2.0
Group: Development/Libraries
URL: https://github.com/patternfly/patternfly-react#readme
Source0: https://registry.npmjs.org/patternfly-react/-/patternfly-react-2.18.0.tgz
Source1: https://registry.npmjs.org/classnames/-/classnames-2.2.6.tgz
Source2: https://registry.npmjs.org/react-bootstrap/-/react-bootstrap-0.32.4.tgz
Source3: https://registry.npmjs.org/css-element-queries/-/css-element-queries-1.0.2.tgz
Source4: https://registry.npmjs.org/breakjs/-/breakjs-1.0.0.tgz
Source5: https://registry.npmjs.org/bootstrap-slider-without-jquery/-/bootstrap-slider-without-jquery-10.0.0.tgz
Source6: https://registry.npmjs.org/patternfly/-/patternfly-3.54.8.tgz
Source7: https://registry.npmjs.org/react-bootstrap-switch/-/react-bootstrap-switch-15.5.3.tgz
Source8: https://registry.npmjs.org/react-c3js/-/react-c3js-0.1.20.tgz
Source9: https://registry.npmjs.org/react-motion/-/react-motion-0.5.2.tgz
Source10: https://registry.npmjs.org/react-bootstrap-typeahead/-/react-bootstrap-typeahead-3.2.3.tgz
Source11: https://registry.npmjs.org/react-click-outside/-/react-click-outside-3.0.1.tgz
Source12: https://registry.npmjs.org/recompose/-/recompose-0.26.0.tgz
Source13: https://registry.npmjs.org/@babel/runtime-corejs2/-/@babel/runtime-corejs2-7.0.0.tgz
Source14: https://registry.npmjs.org/dom-helpers/-/dom-helpers-3.3.1.tgz
Source15: https://registry.npmjs.org/invariant/-/invariant-2.2.4.tgz
Source16: https://registry.npmjs.org/prop-types/-/prop-types-15.6.2.tgz
Source17: https://registry.npmjs.org/react-overlays/-/react-overlays-0.8.3.tgz
Source18: https://registry.npmjs.org/react-fontawesome/-/react-fontawesome-1.6.1.tgz
Source19: https://registry.npmjs.org/react-collapse/-/react-collapse-4.0.3.tgz
Source20: https://registry.npmjs.org/reactabular-table/-/reactabular-table-8.14.0.tgz
Source21: https://registry.npmjs.org/react-transition-group/-/react-transition-group-2.4.0.tgz
Source22: https://registry.npmjs.org/warning/-/warning-3.0.0.tgz
Source23: https://registry.npmjs.org/bootstrap/-/bootstrap-3.3.7.tgz
Source24: https://registry.npmjs.org/font-awesome/-/font-awesome-4.7.0.tgz
Source25: https://registry.npmjs.org/table-resolver/-/table-resolver-3.3.0.tgz
Source26: https://registry.npmjs.org/keycode/-/keycode-2.2.0.tgz
Source27: https://registry.npmjs.org/sortabular/-/sortabular-1.6.0.tgz
Source28: https://registry.npmjs.org/jquery/-/jquery-3.2.1.tgz
Source29: https://registry.npmjs.org/@types/c3/-/@types/c3-0.6.2.tgz
Source30: https://registry.npmjs.org/bootstrap-sass/-/bootstrap-sass-3.3.7.tgz
Source31: https://registry.npmjs.org/bootstrap-select/-/bootstrap-select-1.12.2.tgz
Source32: https://registry.npmjs.org/prop-types-extra/-/prop-types-extra-1.1.0.tgz
Source33: https://registry.npmjs.org/bootstrap-switch/-/bootstrap-switch-3.3.4.tgz
Source34: https://registry.npmjs.org/c3/-/c3-0.4.23.tgz
Source35: https://registry.npmjs.org/d3/-/d3-3.5.17.tgz
Source36: https://registry.npmjs.org/react-prop-types/-/react-prop-types-0.4.0.tgz
Source37: https://registry.npmjs.org/uncontrollable/-/uncontrollable-5.1.0.tgz
Source38: https://registry.npmjs.org/bootstrap-datepicker/-/bootstrap-datepicker-1.8.0.tgz
Source39: https://registry.npmjs.org/bootstrap-touchspin/-/bootstrap-touchspin-3.1.1.tgz
Source40: https://registry.npmjs.org/bootstrap-slider/-/bootstrap-slider-9.10.0.tgz
Source41: https://registry.npmjs.org/datatables.net-colreorder/-/datatables.net-colreorder-1.5.1.tgz
Source42: https://registry.npmjs.org/datatables.net/-/datatables.net-1.10.19.tgz
Source43: https://registry.npmjs.org/datatables.net-colreorder-bs/-/datatables.net-colreorder-bs-1.3.3.tgz
Source44: https://registry.npmjs.org/moment/-/moment-2.22.2.tgz
Source45: https://registry.npmjs.org/moment-timezone/-/moment-timezone-0.4.1.tgz
Source46: https://registry.npmjs.org/datatables.net-select/-/datatables.net-select-1.2.7.tgz
Source47: https://registry.npmjs.org/performance-now/-/performance-now-0.2.0.tgz
Source48: https://registry.npmjs.org/raf/-/raf-3.4.0.tgz
Source49: https://registry.npmjs.org/escape-string-regexp/-/escape-string-regexp-1.0.5.tgz
Source50: https://registry.npmjs.org/lodash/-/lodash-4.17.11.tgz
Source51: https://registry.npmjs.org/drmonty-datatables-colvis/-/drmonty-datatables-colvis-1.1.2.tgz
Source52: https://registry.npmjs.org/eonasdan-bootstrap-datetimepicker/-/eonasdan-bootstrap-datetimepicker-4.17.47.tgz
Source53: https://registry.npmjs.org/font-awesome-sass/-/font-awesome-sass-4.7.0.tgz
Source54: https://registry.npmjs.org/jquery-match-height/-/jquery-match-height-0.7.2.tgz
Source55: https://registry.npmjs.org/warning/-/warning-4.0.2.tgz
Source56: https://registry.npmjs.org/hoist-non-react-statics/-/hoist-non-react-statics-2.5.5.tgz
Source57: https://registry.npmjs.org/google-code-prettify/-/google-code-prettify-1.0.5.tgz
Source58: https://registry.npmjs.org/patternfly-bootstrap-combobox/-/patternfly-bootstrap-combobox-1.1.7.tgz
Source59: https://registry.npmjs.org/patternfly-bootstrap-treeview/-/patternfly-bootstrap-treeview-2.1.5.tgz
Source60: https://registry.npmjs.org/fbjs/-/fbjs-0.8.17.tgz
Source61: https://registry.npmjs.org/symbol-observable/-/symbol-observable-1.2.0.tgz
Source62: https://registry.npmjs.org/core-js/-/core-js-2.5.7.tgz
Source63: https://registry.npmjs.org/regenerator-runtime/-/regenerator-runtime-0.12.1.tgz
Source64: https://registry.npmjs.org/loose-envify/-/loose-envify-1.4.0.tgz
Source65: https://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz
Source66: https://registry.npmjs.org/react-lifecycles-compat/-/react-lifecycles-compat-3.0.4.tgz
Source67: https://registry.npmjs.org/@types/d3/-/@types/d3-4.13.0.tgz
Source68: https://registry.npmjs.org/jquery/-/jquery-3.3.1.tgz
Source69: https://registry.npmjs.org/react-is/-/react-is-16.5.2.tgz
Source70: https://registry.npmjs.org/performance-now/-/performance-now-2.1.0.tgz
Source71: https://registry.npmjs.org/react-onclickoutside/-/react-onclickoutside-6.7.1.tgz
Source72: https://registry.npmjs.org/core-js/-/core-js-1.2.7.tgz
Source73: https://registry.npmjs.org/promise/-/promise-7.3.1.tgz
Source74: https://registry.npmjs.org/setimmediate/-/setimmediate-1.0.5.tgz
Source75: https://registry.npmjs.org/ua-parser-js/-/ua-parser-js-0.7.18.tgz
Source76: https://registry.npmjs.org/js-tokens/-/js-tokens-4.0.0.tgz
Source77: https://registry.npmjs.org/@types/d3-scale/-/@types/d3-scale-1.0.13.tgz
Source78: https://registry.npmjs.org/react-popper/-/react-popper-1.0.2.tgz
Source79: https://registry.npmjs.org/@types/d3-array/-/@types/d3-array-1.2.1.tgz
Source80: https://registry.npmjs.org/change-emitter/-/change-emitter-0.1.6.tgz
Source81: https://registry.npmjs.org/datatables.net-bs/-/datatables.net-bs-2.1.1.tgz
Source82: https://registry.npmjs.org/isomorphic-fetch/-/isomorphic-fetch-2.2.1.tgz
Source83: https://registry.npmjs.org/@types/d3-axis/-/@types/d3-axis-1.0.10.tgz
Source84: https://registry.npmjs.org/@types/d3-chord/-/@types/d3-chord-1.0.7.tgz
Source85: https://registry.npmjs.org/@types/d3-brush/-/@types/d3-brush-1.0.8.tgz
Source86: https://registry.npmjs.org/@types/d3-color/-/@types/d3-color-1.2.1.tgz
Source87: https://registry.npmjs.org/@types/d3-collection/-/@types/d3-collection-1.0.7.tgz
Source88: https://registry.npmjs.org/@types/d3-dispatch/-/@types/d3-dispatch-1.0.6.tgz
Source89: https://registry.npmjs.org/@types/d3-drag/-/@types/d3-drag-1.2.1.tgz
Source90: https://registry.npmjs.org/@types/d3-path/-/@types/d3-path-1.0.7.tgz
Source91: https://registry.npmjs.org/@types/d3-dsv/-/@types/d3-dsv-1.0.33.tgz
Source92: https://registry.npmjs.org/@types/d3-force/-/@types/d3-force-1.1.1.tgz
Source93: https://registry.npmjs.org/@types/d3-ease/-/@types/d3-ease-1.0.7.tgz
Source94: https://registry.npmjs.org/@types/d3-format/-/@types/d3-format-1.3.0.tgz
Source95: https://registry.npmjs.org/@types/d3-hierarchy/-/@types/d3-hierarchy-1.1.4.tgz
Source96: https://registry.npmjs.org/@types/d3-geo/-/@types/d3-geo-1.10.3.tgz
Source97: https://registry.npmjs.org/@types/d3-shape/-/@types/d3-shape-1.2.4.tgz
Source98: https://registry.npmjs.org/@types/d3-time/-/@types/d3-time-1.0.9.tgz
Source99: https://registry.npmjs.org/@types/d3-interpolate/-/@types/d3-interpolate-1.2.0.tgz
Source100: https://registry.npmjs.org/@types/d3-timer/-/@types/d3-timer-1.0.8.tgz
Source101: https://registry.npmjs.org/@types/d3-polygon/-/@types/d3-polygon-1.0.6.tgz
Source102: https://registry.npmjs.org/@types/d3-quadtree/-/@types/d3-quadtree-1.0.6.tgz
Source103: https://registry.npmjs.org/@types/d3-queue/-/@types/d3-queue-3.0.7.tgz
Source104: https://registry.npmjs.org/@types/d3-random/-/@types/d3-random-1.1.1.tgz
Source105: https://registry.npmjs.org/asap/-/asap-2.0.6.tgz
Source106: https://registry.npmjs.org/babel-runtime/-/babel-runtime-6.26.0.tgz
Source107: https://registry.npmjs.org/@types/d3-request/-/@types/d3-request-1.0.3.tgz
Source108: https://registry.npmjs.org/popper.js/-/popper.js-1.14.4.tgz
Source109: https://registry.npmjs.org/@types/d3-selection/-/@types/d3-selection-1.3.2.tgz
Source110: https://registry.npmjs.org/datatables.net/-/datatables.net-2.1.1.tgz
Source111: https://registry.npmjs.org/node-fetch/-/node-fetch-1.7.3.tgz
Source112: https://registry.npmjs.org/whatwg-fetch/-/whatwg-fetch-3.0.0.tgz
Source113: https://registry.npmjs.org/@types/d3-time-format/-/@types/d3-time-format-2.1.0.tgz
Source114: https://registry.npmjs.org/regenerator-runtime/-/regenerator-runtime-0.11.1.tgz
Source115: https://registry.npmjs.org/encoding/-/encoding-0.1.12.tgz
Source116: https://registry.npmjs.org/is-stream/-/is-stream-1.1.0.tgz
Source117: https://registry.npmjs.org/iconv-lite/-/iconv-lite-0.4.24.tgz
Source118: https://registry.npmjs.org/safer-buffer/-/safer-buffer-2.1.2.tgz
Source119: https://registry.npmjs.org/@types/d3-transition/-/@types/d3-transition-1.1.2.tgz
Source120: https://registry.npmjs.org/@types/d3-voronoi/-/@types/d3-voronoi-1.1.8.tgz
Source121: https://registry.npmjs.org/@types/d3-zoom/-/@types/d3-zoom-1.7.1.tgz
Source122: https://registry.npmjs.org/create-react-context/-/create-react-context-0.2.3.tgz
Source123: https://registry.npmjs.org/typed-styles/-/typed-styles-0.0.5.tgz
Source124: https://registry.npmjs.org/@types/geojson/-/@types/geojson-7946.0.4.tgz
Source125: https://registry.npmjs.org/gud/-/gud-1.0.0.tgz
Source126: %{npm_name}-%{version}-registry.npmjs.org.tgz
BuildRequires: nodejs-packaging
Requires: npm(bootstrap-slider-without-jquery) >= 10.0.0
Requires: npm(bootstrap-slider-without-jquery) < 11.0.0
Requires: npm(breakjs) >= 1.0.0
Requires: npm(breakjs) < 2.0.0
Requires: npm(classnames) >= 2.2.5
Requires: npm(classnames) < 3.0.0
Requires: npm(css-element-queries) >= 1.0.1
Requires: npm(css-element-queries) < 2.0.0
Requires: npm(patternfly) >= 3.48.0
Requires: npm(patternfly) < 4.0.0
Requires: npm(react-bootstrap) >= 0.32.1
Requires: npm(react-bootstrap) < 1.0.0
Requires: npm(react-bootstrap-switch) >= 15.5.3
Requires: npm(react-bootstrap-switch) < 16.0.0
Requires: npm(react-c3js) >= 0.1.20
Requires: npm(react-c3js) < 1.0.0
Requires: npm(react-fontawesome) >= 1.6.1
Requires: npm(react-fontawesome) < 2.0.0
Requires: npm(reactabular-table) >= 8.14.0
Requires: npm(reactabular-table) < 9.0.0
Requires: npm(recompose) >= 0.26.0
Requires: npm(recompose) < 1.0.0
Requires: npm(sortabular) >= 1.5.1
Requires: npm(sortabular) < 2.0.0
Requires: npm(table-resolver) >= 3.2.0
Requires: npm(table-resolver) < 4.0.0
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: npm(%{npm_name}) = %{version}
Provides: bundled(npm(@babel/runtime-corejs2)) = 7.0.0
Provides: bundled(npm(@types/c3)) = 0.6.2
Provides: bundled(npm(@types/d3)) = 4.13.0
Provides: bundled(npm(@types/d3-array)) = 1.2.1
Provides: bundled(npm(@types/d3-axis)) = 1.0.10
Provides: bundled(npm(@types/d3-brush)) = 1.0.8
Provides: bundled(npm(@types/d3-chord)) = 1.0.7
Provides: bundled(npm(@types/d3-collection)) = 1.0.7
Provides: bundled(npm(@types/d3-color)) = 1.2.1
Provides: bundled(npm(@types/d3-dispatch)) = 1.0.6
Provides: bundled(npm(@types/d3-drag)) = 1.2.1
Provides: bundled(npm(@types/d3-dsv)) = 1.0.33
Provides: bundled(npm(@types/d3-ease)) = 1.0.7
Provides: bundled(npm(@types/d3-force)) = 1.1.1
Provides: bundled(npm(@types/d3-format)) = 1.3.0
Provides: bundled(npm(@types/d3-geo)) = 1.10.3
Provides: bundled(npm(@types/d3-hierarchy)) = 1.1.4
Provides: bundled(npm(@types/d3-interpolate)) = 1.2.0
Provides: bundled(npm(@types/d3-path)) = 1.0.7
Provides: bundled(npm(@types/d3-polygon)) = 1.0.6
Provides: bundled(npm(@types/d3-quadtree)) = 1.0.6
Provides: bundled(npm(@types/d3-queue)) = 3.0.7
Provides: bundled(npm(@types/d3-random)) = 1.1.1
Provides: bundled(npm(@types/d3-request)) = 1.0.3
Provides: bundled(npm(@types/d3-scale)) = 1.0.13
Provides: bundled(npm(@types/d3-selection)) = 1.3.2
Provides: bundled(npm(@types/d3-shape)) = 1.2.4
Provides: bundled(npm(@types/d3-time)) = 1.0.9
Provides: bundled(npm(@types/d3-time-format)) = 2.1.0
Provides: bundled(npm(@types/d3-timer)) = 1.0.8
Provides: bundled(npm(@types/d3-transition)) = 1.1.2
Provides: bundled(npm(@types/d3-voronoi)) = 1.1.8
Provides: bundled(npm(@types/d3-zoom)) = 1.7.1
Provides: bundled(npm(@types/geojson)) = 7946.0.4
Provides: bundled(npm(asap)) = 2.0.6
Provides: bundled(npm(babel-runtime)) = 6.26.0
Provides: bundled(npm(bootstrap)) = 3.3.7
Provides: bundled(npm(bootstrap-datepicker)) = 1.8.0
Provides: bundled(npm(bootstrap-sass)) = 3.3.7
Provides: bundled(npm(bootstrap-select)) = 1.12.2
Provides: bundled(npm(bootstrap-slider)) = 9.10.0
Provides: bundled(npm(bootstrap-slider-without-jquery)) = 10.0.0
Provides: bundled(npm(bootstrap-switch)) = 3.3.4
Provides: bundled(npm(bootstrap-touchspin)) = 3.1.1
Provides: bundled(npm(breakjs)) = 1.0.0
Provides: bundled(npm(c3)) = 0.4.23
Provides: bundled(npm(change-emitter)) = 0.1.6
Provides: bundled(npm(classnames)) = 2.2.6
Provides: bundled(npm(core-js)) = 2.5.7
Provides: bundled(npm(core-js)) = 1.2.7
Provides: bundled(npm(create-react-context)) = 0.2.3
Provides: bundled(npm(css-element-queries)) = 1.0.2
Provides: bundled(npm(d3)) = 3.5.17
Provides: bundled(npm(datatables.net)) = 2.1.1
Provides: bundled(npm(datatables.net)) = 1.10.19
Provides: bundled(npm(datatables.net-bs)) = 2.1.1
Provides: bundled(npm(datatables.net-colreorder)) = 1.5.1
Provides: bundled(npm(datatables.net-colreorder-bs)) = 1.3.3
Provides: bundled(npm(datatables.net-select)) = 1.2.7
Provides: bundled(npm(dom-helpers)) = 3.3.1
Provides: bundled(npm(drmonty-datatables-colvis)) = 1.1.2
Provides: bundled(npm(encoding)) = 0.1.12
Provides: bundled(npm(eonasdan-bootstrap-datetimepicker)) = 4.17.47
Provides: bundled(npm(escape-string-regexp)) = 1.0.5
Provides: bundled(npm(fbjs)) = 0.8.17
Provides: bundled(npm(font-awesome)) = 4.7.0
Provides: bundled(npm(font-awesome-sass)) = 4.7.0
Provides: bundled(npm(google-code-prettify)) = 1.0.5
Provides: bundled(npm(gud)) = 1.0.0
Provides: bundled(npm(hoist-non-react-statics)) = 2.5.5
Provides: bundled(npm(iconv-lite)) = 0.4.24
Provides: bundled(npm(invariant)) = 2.2.4
Provides: bundled(npm(is-stream)) = 1.1.0
Provides: bundled(npm(isomorphic-fetch)) = 2.2.1
Provides: bundled(npm(jquery)) = 3.2.1
Provides: bundled(npm(jquery)) = 3.3.1
Provides: bundled(npm(jquery-match-height)) = 0.7.2
Provides: bundled(npm(js-tokens)) = 4.0.0
Provides: bundled(npm(keycode)) = 2.2.0
Provides: bundled(npm(lodash)) = 4.17.11
Provides: bundled(npm(loose-envify)) = 1.4.0
Provides: bundled(npm(moment)) = 2.22.2
Provides: bundled(npm(moment-timezone)) = 0.4.1
Provides: bundled(npm(node-fetch)) = 1.7.3
Provides: bundled(npm(object-assign)) = 4.1.1
Provides: bundled(npm(patternfly)) = 3.54.8
Provides: bundled(npm(patternfly-bootstrap-combobox)) = 1.1.7
Provides: bundled(npm(patternfly-bootstrap-treeview)) = 2.1.5
Provides: bundled(npm(patternfly-react)) = 2.18.0
Provides: bundled(npm(performance-now)) = 0.2.0
Provides: bundled(npm(performance-now)) = 2.1.0
Provides: bundled(npm(popper.js)) = 1.14.4
Provides: bundled(npm(promise)) = 7.3.1
Provides: bundled(npm(prop-types)) = 15.6.2
Provides: bundled(npm(prop-types-extra)) = 1.1.0
Provides: bundled(npm(raf)) = 3.4.0
Provides: bundled(npm(react-bootstrap)) = 0.32.4
Provides: bundled(npm(react-bootstrap-switch)) = 15.5.3
Provides: bundled(npm(react-bootstrap-typeahead)) = 3.2.3
Provides: bundled(npm(react-c3js)) = 0.1.20
Provides: bundled(npm(react-click-outside)) = 3.0.1
Provides: bundled(npm(react-collapse)) = 4.0.3
Provides: bundled(npm(react-fontawesome)) = 1.6.1
Provides: bundled(npm(react-is)) = 16.5.2
Provides: bundled(npm(react-lifecycles-compat)) = 3.0.4
Provides: bundled(npm(react-motion)) = 0.5.2
Provides: bundled(npm(react-onclickoutside)) = 6.7.1
Provides: bundled(npm(react-overlays)) = 0.8.3
Provides: bundled(npm(react-popper)) = 1.0.2
Provides: bundled(npm(react-prop-types)) = 0.4.0
Provides: bundled(npm(react-transition-group)) = 2.4.0
Provides: bundled(npm(reactabular-table)) = 8.14.0
Provides: bundled(npm(recompose)) = 0.26.0
Provides: bundled(npm(regenerator-runtime)) = 0.12.1
Provides: bundled(npm(regenerator-runtime)) = 0.11.1
Provides: bundled(npm(safer-buffer)) = 2.1.2
Provides: bundled(npm(setimmediate)) = 1.0.5
Provides: bundled(npm(sortabular)) = 1.6.0
Provides: bundled(npm(symbol-observable)) = 1.2.0
Provides: bundled(npm(table-resolver)) = 3.3.0
Provides: bundled(npm(typed-styles)) = 0.0.5
Provides: bundled(npm(ua-parser-js)) = 0.7.18
Provides: bundled(npm(uncontrollable)) = 5.1.0
Provides: bundled(npm(warning)) = 4.0.2
Provides: bundled(npm(warning)) = 3.0.0
Provides: bundled(npm(whatwg-fetch)) = 3.0.0
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
%setup -T -q -a 126 -D -n %{npm_cache_dir}

%build
npm install --cache-min Infinity --cache %{npm_cache_dir} --no-shrinkwrap --no-optional --global-style true %{npm_name}@%{version}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/__mocks__ %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/dist %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%doc node_modules/%{npm_name}/CHANGELOG.md
%doc node_modules/%{npm_name}/README.md

%changelog
* Thu Sep 20 2018 Ohad Levy <ohadlevy@gmail.com> 2.18.0-1
- Update to 2.18.0

* Wed Sep 12 2018 Bryan Kearney <bryan.kearney@gmail.com> - 2.5.1-2
- Use ASL 2.0 instead of Apache 2.0 or Apache-2.0

* Wed Jun 06 2018 Eric D. Helms <ericdhelms@gmail.com> 2.5.1-1
- Update to 2.5.1

* Tue May 22 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 2.3.4-1
- Update to 2.3.4

* Tue May 01 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 2.2.1-1
- Update to 2.2.1

* Tue Apr 03 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.16.4-1
- Update to 1.16.4

* Thu Mar 01 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.11.0-1
- Refs #22724 - Bump nodejs-patternfly-react to 1.11.0
  (ewoud@kohlvanwijngaarden.nl)

* Mon Feb 26 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.10.0-1
- Bump nodejs-patternfly-react to 1.10.0 (ewoud@kohlvanwijngaarden.nl)

* Wed Feb 21 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.6.0-1
- Bump nodejs-patternfly-react to 1.6.0 (ewoud@kohlvanwijngaarden.nl)
- Restructure foreman packages to prepare for obal (pcreech@redhat.com)

* Tue Jan 16 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.26.0-1
- Bump nodejs-patternfly-react to 0.26.0 (ewoud@kohlvanwijngaarden.nl)

* Tue Dec 19 2017 Daniel Lobato Garcia <me@daniellobato.me> 0.19.2-1
- Update nodejs-patternfly-react to 0.19.2 (github@kohlvanwijngaarden.nl)

* Thu Dec 14 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.13.0-1
- Update patternfly-react to 0.13.0 (oprazak@redhat.com)

* Sun Nov 19 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.10.0-1
- Update nodejs-patternfly-react to 0.10.0 (ewoud@kohlvanwijngaarden.nl)

* Wed Nov 08 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.9.0-1
- new package built with tito
