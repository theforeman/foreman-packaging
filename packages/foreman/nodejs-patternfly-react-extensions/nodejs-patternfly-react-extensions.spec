%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name patternfly-react-extensions

Name: %{?scl_prefix}nodejs-patternfly-react-extensions
Version: 3.0.15
Release: 2%{?dist}
Summary: This library provides an extended set of React components for use with the PatternFly reference implementation
License: MIT
Group: Development/Libraries
URL: https://github.com/patternfly/patternfly-react/blob/master/packages/patternfly-react-extensions/README.md
Source0: https://registry.npmjs.org/@babel/runtime/-/runtime-7.27.6.tgz
Source1: https://registry.npmjs.org/@babel/runtime-corejs2/-/runtime-corejs2-7.27.6.tgz
Source2: https://registry.npmjs.org/@hypnosphi/create-react-context/-/create-react-context-0.3.1.tgz
Source3: https://registry.npmjs.org/@types/react/-/react-19.1.8.tgz
Source4: https://registry.npmjs.org/bootstrap/-/bootstrap-3.4.1.tgz
Source5: https://registry.npmjs.org/bootstrap-slider-without-jquery/-/bootstrap-slider-without-jquery-10.0.0.tgz
Source6: https://registry.npmjs.org/breakjs/-/breakjs-1.0.0.tgz
Source7: https://registry.npmjs.org/c3/-/c3-0.4.24.tgz
Source8: https://registry.npmjs.org/call-bind/-/call-bind-1.0.8.tgz
Source9: https://registry.npmjs.org/call-bind-apply-helpers/-/call-bind-apply-helpers-1.0.2.tgz
Source10: https://registry.npmjs.org/call-bound/-/call-bound-1.0.4.tgz
Source11: https://registry.npmjs.org/change-emitter/-/change-emitter-0.1.6.tgz
Source12: https://registry.npmjs.org/classnames/-/classnames-2.5.1.tgz
Source13: https://registry.npmjs.org/clsx/-/clsx-1.2.1.tgz
Source14: https://registry.npmjs.org/core-js/-/core-js-2.6.12.tgz
Source15: https://registry.npmjs.org/create-react-context/-/create-react-context-0.3.0.tgz
Source16: https://registry.npmjs.org/css-element-queries/-/css-element-queries-1.2.3.tgz
Source17: https://registry.npmjs.org/csstype/-/csstype-3.1.3.tgz
Source18: https://registry.npmjs.org/d3/-/d3-3.5.17.tgz
Source19: https://registry.npmjs.org/deep-equal/-/deep-equal-1.1.2.tgz
Source20: https://registry.npmjs.org/define-data-property/-/define-data-property-1.1.4.tgz
Source21: https://registry.npmjs.org/define-properties/-/define-properties-1.2.1.tgz
Source22: https://registry.npmjs.org/diff/-/diff-5.2.0.tgz
Source23: https://registry.npmjs.org/dom-helpers/-/dom-helpers-3.4.0.tgz
Source24: https://registry.npmjs.org/dom-helpers/-/dom-helpers-5.2.1.tgz
Source25: https://registry.npmjs.org/dunder-proto/-/dunder-proto-1.0.1.tgz
Source26: https://registry.npmjs.org/es-define-property/-/es-define-property-1.0.1.tgz
Source27: https://registry.npmjs.org/es-errors/-/es-errors-1.3.0.tgz
Source28: https://registry.npmjs.org/es-object-atoms/-/es-object-atoms-1.1.1.tgz
Source29: https://registry.npmjs.org/escape-string-regexp/-/escape-string-regexp-1.0.5.tgz
Source30: https://registry.npmjs.org/font-awesome/-/font-awesome-4.7.0.tgz
Source31: https://registry.npmjs.org/function-bind/-/function-bind-1.1.2.tgz
Source32: https://registry.npmjs.org/functions-have-names/-/functions-have-names-1.2.3.tgz
Source33: https://registry.npmjs.org/get-intrinsic/-/get-intrinsic-1.3.0.tgz
Source34: https://registry.npmjs.org/get-proto/-/get-proto-1.0.1.tgz
Source35: https://registry.npmjs.org/gitdiff-parser/-/gitdiff-parser-0.1.2.tgz
Source36: https://registry.npmjs.org/gopd/-/gopd-1.2.0.tgz
Source37: https://registry.npmjs.org/gud/-/gud-1.0.0.tgz
Source38: https://registry.npmjs.org/has-property-descriptors/-/has-property-descriptors-1.0.2.tgz
Source39: https://registry.npmjs.org/has-symbols/-/has-symbols-1.1.0.tgz
Source40: https://registry.npmjs.org/has-tostringtag/-/has-tostringtag-1.0.2.tgz
Source41: https://registry.npmjs.org/hasown/-/hasown-2.0.2.tgz
Source42: https://registry.npmjs.org/hoist-non-react-statics/-/hoist-non-react-statics-2.5.5.tgz
Source43: https://registry.npmjs.org/invariant/-/invariant-2.2.4.tgz
Source44: https://registry.npmjs.org/is-arguments/-/is-arguments-1.2.0.tgz
Source45: https://registry.npmjs.org/is-date-object/-/is-date-object-1.1.0.tgz
Source46: https://registry.npmjs.org/is-regex/-/is-regex-1.2.1.tgz
Source47: https://registry.npmjs.org/jquery/-/jquery-3.4.1.tgz
Source48: https://registry.npmjs.org/js-tokens/-/js-tokens-4.0.0.tgz
Source49: https://registry.npmjs.org/keycode/-/keycode-2.2.1.tgz
Source50: https://registry.npmjs.org/leven/-/leven-2.1.0.tgz
Source51: https://registry.npmjs.org/lodash/-/lodash-4.17.21.tgz
Source52: https://registry.npmjs.org/lodash.debounce/-/lodash.debounce-4.0.8.tgz
Source53: https://registry.npmjs.org/lodash.escape/-/lodash.escape-4.0.1.tgz
Source54: https://registry.npmjs.org/lodash.findlastindex/-/lodash.findlastindex-4.6.0.tgz
Source55: https://registry.npmjs.org/lodash.mapvalues/-/lodash.mapvalues-4.6.0.tgz
Source56: https://registry.npmjs.org/loose-envify/-/loose-envify-1.4.0.tgz
Source57: https://registry.npmjs.org/math-intrinsics/-/math-intrinsics-1.1.0.tgz
Source58: https://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz
Source59: https://registry.npmjs.org/object-is/-/object-is-1.1.6.tgz
Source60: https://registry.npmjs.org/object-keys/-/object-keys-1.1.1.tgz
Source61: https://registry.npmjs.org/patternfly/-/patternfly-3.59.5.tgz
Source62: https://registry.npmjs.org/patternfly-react/-/patternfly-react-2.40.0.tgz
Source63: https://registry.npmjs.org/patternfly-react-extensions/-/patternfly-react-extensions-3.0.15.tgz
Source64: https://registry.npmjs.org/performance-now/-/performance-now-0.2.0.tgz
Source65: https://registry.npmjs.org/performance-now/-/performance-now-2.1.0.tgz
Source66: https://registry.npmjs.org/popper.js/-/popper.js-1.16.1.tgz
Source67: https://registry.npmjs.org/prop-types/-/prop-types-15.8.1.tgz
Source68: https://registry.npmjs.org/prop-types-extra/-/prop-types-extra-1.1.1.tgz
Source69: https://registry.npmjs.org/raf/-/raf-3.4.1.tgz
Source70: https://registry.npmjs.org/react-bootstrap/-/react-bootstrap-0.33.1.tgz
Source71: https://registry.npmjs.org/react-bootstrap-switch/-/react-bootstrap-switch-15.5.3.tgz
Source72: https://registry.npmjs.org/react-bootstrap-typeahead/-/react-bootstrap-typeahead-3.4.7.tgz
Source73: https://registry.npmjs.org/react-c3js/-/react-c3js-0.1.20.tgz
Source74: https://registry.npmjs.org/react-click-outside/-/react-click-outside-3.0.1.tgz
Source75: https://registry.npmjs.org/react-collapse/-/react-collapse-4.0.3.tgz
Source76: https://registry.npmjs.org/react-debounce-input/-/react-debounce-input-3.3.0.tgz
Source77: https://registry.npmjs.org/react-diff-view/-/react-diff-view-1.8.1.tgz
Source78: https://registry.npmjs.org/react-ellipsis-with-tooltip/-/react-ellipsis-with-tooltip-1.1.1.tgz
Source79: https://registry.npmjs.org/react-fontawesome/-/react-fontawesome-1.7.1.tgz
Source80: https://registry.npmjs.org/react-is/-/react-is-16.13.1.tgz
Source81: https://registry.npmjs.org/react-lifecycles-compat/-/react-lifecycles-compat-3.0.4.tgz
Source82: https://registry.npmjs.org/react-motion/-/react-motion-0.5.2.tgz
Source83: https://registry.npmjs.org/react-overlays/-/react-overlays-0.8.3.tgz
Source84: https://registry.npmjs.org/react-overlays/-/react-overlays-0.9.3.tgz
Source85: https://registry.npmjs.org/react-popper/-/react-popper-1.3.11.tgz
Source86: https://registry.npmjs.org/react-prop-types/-/react-prop-types-0.4.0.tgz
Source87: https://registry.npmjs.org/react-recompose/-/react-recompose-0.31.2.tgz
Source88: https://registry.npmjs.org/react-transition-group/-/react-transition-group-2.9.0.tgz
Source89: https://registry.npmjs.org/react-virtualized/-/react-virtualized-9.22.6.tgz
Source90: https://registry.npmjs.org/reactabular-table/-/reactabular-table-8.14.0.tgz
Source91: https://registry.npmjs.org/regexp.prototype.flags/-/regexp.prototype.flags-1.5.4.tgz
Source92: https://registry.npmjs.org/set-function-length/-/set-function-length-1.2.2.tgz
Source93: https://registry.npmjs.org/set-function-name/-/set-function-name-2.0.2.tgz
Source94: https://registry.npmjs.org/symbol-observable/-/symbol-observable-1.2.0.tgz
Source95: https://registry.npmjs.org/typed-styles/-/typed-styles-0.0.7.tgz
Source96: https://registry.npmjs.org/uncontrollable/-/uncontrollable-7.2.1.tgz
Source97: https://registry.npmjs.org/unidiff/-/unidiff-1.0.4.tgz
Source98: https://registry.npmjs.org/uuid/-/uuid-3.4.0.tgz
Source99: https://registry.npmjs.org/warning/-/warning-3.0.0.tgz
Source100: https://registry.npmjs.org/warning/-/warning-4.0.3.tgz
Source101: nodejs-patternfly-react-extensions-%{version}-registry.npmjs.org.tgz
BuildRequires: %{?scl_prefix_nodejs}npm
%if 0%{!?scl:1}
BuildRequires: nodejs-packaging
%endif
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}
Provides: bundled(npm(@babel/runtime)) = 7.27.6
Provides: bundled(npm(@babel/runtime-corejs2)) = 7.27.6
Provides: bundled(npm(@hypnosphi/create-react-context)) = 0.3.1
Provides: bundled(npm(@types/react)) = 19.1.8
Provides: bundled(npm(bootstrap)) = 3.4.1
Provides: bundled(npm(bootstrap-slider-without-jquery)) = 10.0.0
Provides: bundled(npm(breakjs)) = 1.0.0
Provides: bundled(npm(c3)) = 0.4.24
Provides: bundled(npm(call-bind)) = 1.0.8
Provides: bundled(npm(call-bind-apply-helpers)) = 1.0.2
Provides: bundled(npm(call-bound)) = 1.0.4
Provides: bundled(npm(change-emitter)) = 0.1.6
Provides: bundled(npm(classnames)) = 2.5.1
Provides: bundled(npm(clsx)) = 1.2.1
Provides: bundled(npm(core-js)) = 2.6.12
Provides: bundled(npm(create-react-context)) = 0.3.0
Provides: bundled(npm(css-element-queries)) = 1.2.3
Provides: bundled(npm(csstype)) = 3.1.3
Provides: bundled(npm(d3)) = 3.5.17
Provides: bundled(npm(deep-equal)) = 1.1.2
Provides: bundled(npm(define-data-property)) = 1.1.4
Provides: bundled(npm(define-properties)) = 1.2.1
Provides: bundled(npm(diff)) = 5.2.0
Provides: bundled(npm(dom-helpers)) = 3.4.0
Provides: bundled(npm(dom-helpers)) = 5.2.1
Provides: bundled(npm(dunder-proto)) = 1.0.1
Provides: bundled(npm(es-define-property)) = 1.0.1
Provides: bundled(npm(es-errors)) = 1.3.0
Provides: bundled(npm(es-object-atoms)) = 1.1.1
Provides: bundled(npm(escape-string-regexp)) = 1.0.5
Provides: bundled(npm(font-awesome)) = 4.7.0
Provides: bundled(npm(function-bind)) = 1.1.2
Provides: bundled(npm(functions-have-names)) = 1.2.3
Provides: bundled(npm(get-intrinsic)) = 1.3.0
Provides: bundled(npm(get-proto)) = 1.0.1
Provides: bundled(npm(gitdiff-parser)) = 0.1.2
Provides: bundled(npm(gopd)) = 1.2.0
Provides: bundled(npm(gud)) = 1.0.0
Provides: bundled(npm(has-property-descriptors)) = 1.0.2
Provides: bundled(npm(has-symbols)) = 1.1.0
Provides: bundled(npm(has-tostringtag)) = 1.0.2
Provides: bundled(npm(hasown)) = 2.0.2
Provides: bundled(npm(hoist-non-react-statics)) = 2.5.5
Provides: bundled(npm(invariant)) = 2.2.4
Provides: bundled(npm(is-arguments)) = 1.2.0
Provides: bundled(npm(is-date-object)) = 1.1.0
Provides: bundled(npm(is-regex)) = 1.2.1
Provides: bundled(npm(jquery)) = 3.4.1
Provides: bundled(npm(js-tokens)) = 4.0.0
Provides: bundled(npm(keycode)) = 2.2.1
Provides: bundled(npm(leven)) = 2.1.0
Provides: bundled(npm(lodash)) = 4.17.21
Provides: bundled(npm(lodash.debounce)) = 4.0.8
Provides: bundled(npm(lodash.escape)) = 4.0.1
Provides: bundled(npm(lodash.findlastindex)) = 4.6.0
Provides: bundled(npm(lodash.mapvalues)) = 4.6.0
Provides: bundled(npm(loose-envify)) = 1.4.0
Provides: bundled(npm(math-intrinsics)) = 1.1.0
Provides: bundled(npm(object-assign)) = 4.1.1
Provides: bundled(npm(object-is)) = 1.1.6
Provides: bundled(npm(object-keys)) = 1.1.1
Provides: bundled(npm(patternfly)) = 3.59.5
Provides: bundled(npm(patternfly-react)) = 2.40.0
Provides: bundled(npm(patternfly-react-extensions)) = 3.0.15
Provides: bundled(npm(performance-now)) = 0.2.0
Provides: bundled(npm(performance-now)) = 2.1.0
Provides: bundled(npm(popper.js)) = 1.16.1
Provides: bundled(npm(prop-types)) = 15.8.1
Provides: bundled(npm(prop-types-extra)) = 1.1.1
Provides: bundled(npm(raf)) = 3.4.1
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
Provides: bundled(npm(regexp.prototype.flags)) = 1.5.4
Provides: bundled(npm(set-function-length)) = 1.2.2
Provides: bundled(npm(set-function-name)) = 2.0.2
Provides: bundled(npm(symbol-observable)) = 1.2.0
Provides: bundled(npm(typed-styles)) = 0.0.7
Provides: bundled(npm(uncontrollable)) = 7.2.1
Provides: bundled(npm(unidiff)) = 1.0.4
Provides: bundled(npm(uuid)) = 3.4.0
Provides: bundled(npm(warning)) = 3.0.0
Provides: bundled(npm(warning)) = 4.0.3
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

%setup -T -q -a 101 -D -n %{npm_cache_dir}

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
* Wed Jun 25 2025 Evgeni Golov 3.0.15-2
- Trim down the list of bundled packages

* Mon Jun 16 2025 MariaAga <mariaaga@redhat.com> 3.0.15-1
- Add nodejs-patternfly-react-extensions generated by npm2rpm using the bundle strategy

