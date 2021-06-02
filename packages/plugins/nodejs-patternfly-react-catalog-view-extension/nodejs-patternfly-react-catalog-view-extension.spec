%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name @patternfly/react-catalog-view-extension

Name: %{?scl_prefix}nodejs-patternfly-react-catalog-view-extension
Version: 4.11.25
Release: 1%{?dist}
Summary: This library provides catalog view extensions for PatternFly 4 React
License: MIT
Group: Development/Libraries
URL: https://github.com/patternfly/patternfly-react/blob/master/packages/react-catalog-view-extension/README.md
Source0: https://registry.npmjs.org/@patternfly/patternfly/-/patternfly-4.103.6.tgz
Source1: https://registry.npmjs.org/@patternfly/react-catalog-view-extension/-/react-catalog-view-extension-4.11.25.tgz
Source2: https://registry.npmjs.org/@patternfly/react-core/-/react-core-4.121.1.tgz
Source3: https://registry.npmjs.org/@patternfly/react-icons/-/react-icons-4.10.7.tgz
Source4: https://registry.npmjs.org/@patternfly/react-styles/-/react-styles-4.10.7.tgz
Source5: https://registry.npmjs.org/@patternfly/react-tokens/-/react-tokens-4.11.8.tgz
Source6: https://registry.npmjs.org/@types/c3/-/c3-0.6.4.tgz
Source7: https://registry.npmjs.org/@types/d3/-/d3-4.13.12.tgz
Source8: https://registry.npmjs.org/@types/d3-array/-/d3-array-1.2.8.tgz
Source9: https://registry.npmjs.org/@types/d3-axis/-/d3-axis-1.0.14.tgz
Source10: https://registry.npmjs.org/@types/d3-brush/-/d3-brush-1.1.4.tgz
Source11: https://registry.npmjs.org/@types/d3-chord/-/d3-chord-1.0.10.tgz
Source12: https://registry.npmjs.org/@types/d3-collection/-/d3-collection-1.0.10.tgz
Source13: https://registry.npmjs.org/@types/d3-color/-/d3-color-1.4.1.tgz
Source14: https://registry.npmjs.org/@types/d3-dispatch/-/d3-dispatch-1.0.9.tgz
Source15: https://registry.npmjs.org/@types/d3-drag/-/d3-drag-1.2.5.tgz
Source16: https://registry.npmjs.org/@types/d3-dsv/-/d3-dsv-1.2.1.tgz
Source17: https://registry.npmjs.org/@types/d3-ease/-/d3-ease-1.0.10.tgz
Source18: https://registry.npmjs.org/@types/d3-force/-/d3-force-1.2.2.tgz
Source19: https://registry.npmjs.org/@types/d3-format/-/d3-format-1.4.1.tgz
Source20: https://registry.npmjs.org/@types/d3-geo/-/d3-geo-1.12.1.tgz
Source21: https://registry.npmjs.org/@types/d3-hierarchy/-/d3-hierarchy-1.1.7.tgz
Source22: https://registry.npmjs.org/@types/d3-interpolate/-/d3-interpolate-1.4.2.tgz
Source23: https://registry.npmjs.org/@types/d3-path/-/d3-path-1.0.9.tgz
Source24: https://registry.npmjs.org/@types/d3-polygon/-/d3-polygon-1.0.8.tgz
Source25: https://registry.npmjs.org/@types/d3-quadtree/-/d3-quadtree-1.0.8.tgz
Source26: https://registry.npmjs.org/@types/d3-queue/-/d3-queue-3.0.8.tgz
Source27: https://registry.npmjs.org/@types/d3-random/-/d3-random-1.1.3.tgz
Source28: https://registry.npmjs.org/@types/d3-request/-/d3-request-1.0.6.tgz
Source29: https://registry.npmjs.org/@types/d3-scale/-/d3-scale-1.0.15.tgz
Source30: https://registry.npmjs.org/@types/d3-selection/-/d3-selection-1.4.3.tgz
Source31: https://registry.npmjs.org/@types/d3-shape/-/d3-shape-1.3.5.tgz
Source32: https://registry.npmjs.org/@types/d3-time/-/d3-time-1.1.1.tgz
Source33: https://registry.npmjs.org/@types/d3-time-format/-/d3-time-format-2.3.1.tgz
Source34: https://registry.npmjs.org/@types/d3-timer/-/d3-timer-1.0.10.tgz
Source35: https://registry.npmjs.org/@types/d3-transition/-/d3-transition-1.3.1.tgz
Source36: https://registry.npmjs.org/@types/d3-voronoi/-/d3-voronoi-1.1.9.tgz
Source37: https://registry.npmjs.org/@types/d3-zoom/-/d3-zoom-1.8.2.tgz
Source38: https://registry.npmjs.org/@types/geojson/-/geojson-7946.0.7.tgz
Source39: https://registry.npmjs.org/attr-accept/-/attr-accept-1.1.3.tgz
Source40: https://registry.npmjs.org/bootstrap/-/bootstrap-3.4.1.tgz
Source41: https://registry.npmjs.org/bootstrap-datepicker/-/bootstrap-datepicker-1.9.0.tgz
Source42: https://registry.npmjs.org/bootstrap-sass/-/bootstrap-sass-3.4.1.tgz
Source43: https://registry.npmjs.org/bootstrap-select/-/bootstrap-select-1.12.2.tgz
Source44: https://registry.npmjs.org/bootstrap-slider/-/bootstrap-slider-9.10.0.tgz
Source45: https://registry.npmjs.org/bootstrap-switch/-/bootstrap-switch-3.3.4.tgz
Source46: https://registry.npmjs.org/bootstrap-touchspin/-/bootstrap-touchspin-3.1.1.tgz
Source47: https://registry.npmjs.org/c3/-/c3-0.4.24.tgz
Source48: https://registry.npmjs.org/classnames/-/classnames-2.3.1.tgz
Source49: https://registry.npmjs.org/core-js/-/core-js-2.6.12.tgz
Source50: https://registry.npmjs.org/d3/-/d3-3.5.17.tgz
Source51: https://registry.npmjs.org/datatables.net/-/datatables.net-1.10.24.tgz
Source52: https://registry.npmjs.org/datatables.net/-/datatables.net-2.1.1.tgz
Source53: https://registry.npmjs.org/datatables.net-bs/-/datatables.net-bs-2.1.1.tgz
Source54: https://registry.npmjs.org/datatables.net-colreorder/-/datatables.net-colreorder-1.5.3.tgz
Source55: https://registry.npmjs.org/datatables.net-colreorder-bs/-/datatables.net-colreorder-bs-1.3.3.tgz
Source56: https://registry.npmjs.org/datatables.net-select/-/datatables.net-select-1.2.7.tgz
Source57: https://registry.npmjs.org/drmonty-datatables-colvis/-/drmonty-datatables-colvis-1.1.2.tgz
Source58: https://registry.npmjs.org/eonasdan-bootstrap-datetimepicker/-/eonasdan-bootstrap-datetimepicker-4.17.49.tgz
Source59: https://registry.npmjs.org/file-selector/-/file-selector-0.1.19.tgz
Source60: https://registry.npmjs.org/focus-trap/-/focus-trap-6.2.2.tgz
Source61: https://registry.npmjs.org/font-awesome/-/font-awesome-4.7.0.tgz
Source62: https://registry.npmjs.org/font-awesome-sass/-/font-awesome-sass-4.7.0.tgz
Source63: https://registry.npmjs.org/google-code-prettify/-/google-code-prettify-1.0.5.tgz
Source64: https://registry.npmjs.org/jquery/-/jquery-3.4.1.tgz
Source65: https://registry.npmjs.org/jquery/-/jquery-3.6.0.tgz
Source66: https://registry.npmjs.org/jquery-match-height/-/jquery-match-height-0.7.2.tgz
Source67: https://registry.npmjs.org/js-tokens/-/js-tokens-4.0.0.tgz
Source68: https://registry.npmjs.org/loose-envify/-/loose-envify-1.4.0.tgz
Source69: https://registry.npmjs.org/moment/-/moment-2.29.1.tgz
Source70: https://registry.npmjs.org/moment-timezone/-/moment-timezone-0.4.1.tgz
Source71: https://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz
Source72: https://registry.npmjs.org/patternfly/-/patternfly-3.59.5.tgz
Source73: https://registry.npmjs.org/patternfly-bootstrap-combobox/-/patternfly-bootstrap-combobox-1.1.7.tgz
Source74: https://registry.npmjs.org/patternfly-bootstrap-treeview/-/patternfly-bootstrap-treeview-2.1.10.tgz
Source75: https://registry.npmjs.org/popper.js/-/popper.js-1.16.1.tgz
Source76: https://registry.npmjs.org/prop-types/-/prop-types-15.7.2.tgz
Source77: https://registry.npmjs.org/prop-types-extra/-/prop-types-extra-1.1.1.tgz
Source78: https://registry.npmjs.org/react-dropzone/-/react-dropzone-9.0.0.tgz
Source79: https://registry.npmjs.org/react-is/-/react-is-16.13.1.tgz
Source80: https://registry.npmjs.org/tabbable/-/tabbable-5.2.0.tgz
Source81: https://registry.npmjs.org/tippy.js/-/tippy.js-5.1.2.tgz
Source82: https://registry.npmjs.org/tslib/-/tslib-1.13.0.tgz
Source83: https://registry.npmjs.org/tslib/-/tslib-2.2.0.tgz
Source84: https://registry.npmjs.org/warning/-/warning-4.0.3.tgz
Source85: nodejs-patternfly-react-catalog-view-extension-%{version}-registry.npmjs.org.tgz
BuildRequires: %{?scl_prefix_nodejs}npm
%if 0%{!?scl:1}
BuildRequires: nodejs-packaging
%endif
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}
Provides: bundled(npm(@patternfly/patternfly)) = 4.103.6
Provides: bundled(npm(@patternfly/react-catalog-view-extension)) = 4.11.25
Provides: bundled(npm(@patternfly/react-core)) = 4.121.1
Provides: bundled(npm(@patternfly/react-icons)) = 4.10.7
Provides: bundled(npm(@patternfly/react-styles)) = 4.10.7
Provides: bundled(npm(@patternfly/react-tokens)) = 4.11.8
Provides: bundled(npm(@types/c3)) = 0.6.4
Provides: bundled(npm(@types/d3)) = 4.13.12
Provides: bundled(npm(@types/d3-array)) = 1.2.8
Provides: bundled(npm(@types/d3-axis)) = 1.0.14
Provides: bundled(npm(@types/d3-brush)) = 1.1.4
Provides: bundled(npm(@types/d3-chord)) = 1.0.10
Provides: bundled(npm(@types/d3-collection)) = 1.0.10
Provides: bundled(npm(@types/d3-color)) = 1.4.1
Provides: bundled(npm(@types/d3-dispatch)) = 1.0.9
Provides: bundled(npm(@types/d3-drag)) = 1.2.5
Provides: bundled(npm(@types/d3-dsv)) = 1.2.1
Provides: bundled(npm(@types/d3-ease)) = 1.0.10
Provides: bundled(npm(@types/d3-force)) = 1.2.2
Provides: bundled(npm(@types/d3-format)) = 1.4.1
Provides: bundled(npm(@types/d3-geo)) = 1.12.1
Provides: bundled(npm(@types/d3-hierarchy)) = 1.1.7
Provides: bundled(npm(@types/d3-interpolate)) = 1.4.2
Provides: bundled(npm(@types/d3-path)) = 1.0.9
Provides: bundled(npm(@types/d3-polygon)) = 1.0.8
Provides: bundled(npm(@types/d3-quadtree)) = 1.0.8
Provides: bundled(npm(@types/d3-queue)) = 3.0.8
Provides: bundled(npm(@types/d3-random)) = 1.1.3
Provides: bundled(npm(@types/d3-request)) = 1.0.6
Provides: bundled(npm(@types/d3-scale)) = 1.0.15
Provides: bundled(npm(@types/d3-selection)) = 1.4.3
Provides: bundled(npm(@types/d3-shape)) = 1.3.5
Provides: bundled(npm(@types/d3-time)) = 1.1.1
Provides: bundled(npm(@types/d3-time-format)) = 2.3.1
Provides: bundled(npm(@types/d3-timer)) = 1.0.10
Provides: bundled(npm(@types/d3-transition)) = 1.3.1
Provides: bundled(npm(@types/d3-voronoi)) = 1.1.9
Provides: bundled(npm(@types/d3-zoom)) = 1.8.2
Provides: bundled(npm(@types/geojson)) = 7946.0.7
Provides: bundled(npm(attr-accept)) = 1.1.3
Provides: bundled(npm(bootstrap)) = 3.4.1
Provides: bundled(npm(bootstrap-datepicker)) = 1.9.0
Provides: bundled(npm(bootstrap-sass)) = 3.4.1
Provides: bundled(npm(bootstrap-select)) = 1.12.2
Provides: bundled(npm(bootstrap-slider)) = 9.10.0
Provides: bundled(npm(bootstrap-switch)) = 3.3.4
Provides: bundled(npm(bootstrap-touchspin)) = 3.1.1
Provides: bundled(npm(c3)) = 0.4.24
Provides: bundled(npm(classnames)) = 2.3.1
Provides: bundled(npm(core-js)) = 2.6.12
Provides: bundled(npm(d3)) = 3.5.17
Provides: bundled(npm(datatables.net)) = 1.10.24
Provides: bundled(npm(datatables.net)) = 2.1.1
Provides: bundled(npm(datatables.net-bs)) = 2.1.1
Provides: bundled(npm(datatables.net-colreorder)) = 1.5.3
Provides: bundled(npm(datatables.net-colreorder-bs)) = 1.3.3
Provides: bundled(npm(datatables.net-select)) = 1.2.7
Provides: bundled(npm(drmonty-datatables-colvis)) = 1.1.2
Provides: bundled(npm(eonasdan-bootstrap-datetimepicker)) = 4.17.49
Provides: bundled(npm(file-selector)) = 0.1.19
Provides: bundled(npm(focus-trap)) = 6.2.2
Provides: bundled(npm(font-awesome)) = 4.7.0
Provides: bundled(npm(font-awesome-sass)) = 4.7.0
Provides: bundled(npm(google-code-prettify)) = 1.0.5
Provides: bundled(npm(jquery)) = 3.4.1
Provides: bundled(npm(jquery)) = 3.6.0
Provides: bundled(npm(jquery-match-height)) = 0.7.2
Provides: bundled(npm(js-tokens)) = 4.0.0
Provides: bundled(npm(loose-envify)) = 1.4.0
Provides: bundled(npm(moment)) = 2.29.1
Provides: bundled(npm(moment-timezone)) = 0.4.1
Provides: bundled(npm(object-assign)) = 4.1.1
Provides: bundled(npm(patternfly)) = 3.59.5
Provides: bundled(npm(patternfly-bootstrap-combobox)) = 1.1.7
Provides: bundled(npm(patternfly-bootstrap-treeview)) = 2.1.10
Provides: bundled(npm(popper.js)) = 1.16.1
Provides: bundled(npm(prop-types)) = 15.7.2
Provides: bundled(npm(prop-types-extra)) = 1.1.1
Provides: bundled(npm(react-dropzone)) = 9.0.0
Provides: bundled(npm(react-is)) = 16.13.1
Provides: bundled(npm(tabbable)) = 5.2.0
Provides: bundled(npm(tippy.js)) = 5.1.2
Provides: bundled(npm(tslib)) = 1.13.0
Provides: bundled(npm(tslib)) = 2.2.0
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

%setup -T -q -a 85 -D -n %{npm_cache_dir}

%build
%{?scl:scl enable %{?scl_nodejs} - << \end_of_scl}
npm install --cache-min Infinity --cache %{?scl:../}%{npm_cache_dir} --no-shrinkwrap --no-optional --global-style true %{npm_name}@%{version}
%{?scl:end_of_scl}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/dist %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/node-sass-patternfly-importer.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/sass %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/src %{buildroot}%{nodejs_sitelib}/%{npm_name}

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%license node_modules/%{npm_name}/LICENSE
%doc node_modules/%{npm_name}/CHANGELOG.md
%doc node_modules/%{npm_name}/README.md

%changelog
* Wed May 19 2021 Evgeni Golov 4.11.25-1
- Add nodejs-patternfly-react-catalog-view-extension generated by npm2rpm using the bundle strategy

