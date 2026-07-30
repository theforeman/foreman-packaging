%global npm_name @patternfly/react-charts

Name: nodejs-patternfly-react-charts
Version: 7.4.9
Release: 3%{?dist}
Summary: This library provides a set of React chart components for use with the PatternFly reference implementation
License: MIT
Group: Development/Libraries
URL: https://github.com/patternfly/patternfly-react#readme
Source0: https://registry.npmjs.org/@patternfly/react-charts/-/react-charts-7.4.9.tgz
Source1: https://registry.npmjs.org/@patternfly/react-styles/-/react-styles-5.4.1.tgz
Source2: https://registry.npmjs.org/@patternfly/react-tokens/-/react-tokens-5.4.1.tgz
Source3: https://registry.npmjs.org/@types/d3-array/-/d3-array-3.2.2.tgz
Source4: https://registry.npmjs.org/@types/d3-color/-/d3-color-3.1.3.tgz
Source5: https://registry.npmjs.org/@types/d3-ease/-/d3-ease-3.0.2.tgz
Source6: https://registry.npmjs.org/@types/d3-interpolate/-/d3-interpolate-3.0.4.tgz
Source7: https://registry.npmjs.org/@types/d3-path/-/d3-path-3.1.1.tgz
Source8: https://registry.npmjs.org/@types/d3-scale/-/d3-scale-4.0.9.tgz
Source9: https://registry.npmjs.org/@types/d3-shape/-/d3-shape-3.1.8.tgz
Source10: https://registry.npmjs.org/@types/d3-time/-/d3-time-3.0.4.tgz
Source11: https://registry.npmjs.org/@types/d3-timer/-/d3-timer-3.0.2.tgz
Source12: https://registry.npmjs.org/d3-array/-/d3-array-3.2.4.tgz
Source13: https://registry.npmjs.org/d3-color/-/d3-color-3.1.0.tgz
Source14: https://registry.npmjs.org/d3-ease/-/d3-ease-3.0.1.tgz
Source15: https://registry.npmjs.org/d3-format/-/d3-format-3.1.2.tgz
Source16: https://registry.npmjs.org/d3-interpolate/-/d3-interpolate-3.0.1.tgz
Source17: https://registry.npmjs.org/d3-path/-/d3-path-3.1.0.tgz
Source18: https://registry.npmjs.org/d3-scale/-/d3-scale-4.0.2.tgz
Source19: https://registry.npmjs.org/d3-shape/-/d3-shape-3.2.0.tgz
Source20: https://registry.npmjs.org/d3-time/-/d3-time-3.1.0.tgz
Source21: https://registry.npmjs.org/d3-time-format/-/d3-time-format-4.1.0.tgz
Source22: https://registry.npmjs.org/d3-timer/-/d3-timer-3.0.1.tgz
Source23: https://registry.npmjs.org/delaunator/-/delaunator-4.0.1.tgz
Source24: https://registry.npmjs.org/delaunay-find/-/delaunay-find-0.0.6.tgz
Source25: https://registry.npmjs.org/hoist-non-react-statics/-/hoist-non-react-statics-3.3.2.tgz
Source26: https://registry.npmjs.org/internmap/-/internmap-2.0.3.tgz
Source27: https://registry.npmjs.org/json-stringify-safe/-/json-stringify-safe-5.0.1.tgz
Source28: https://registry.npmjs.org/lodash/-/lodash-4.18.1.tgz
Source29: https://registry.npmjs.org/react-fast-compare/-/react-fast-compare-3.2.2.tgz
Source30: https://registry.npmjs.org/react-is/-/react-is-16.13.1.tgz
Source31: https://registry.npmjs.org/tslib/-/tslib-2.8.1.tgz
Source32: https://registry.npmjs.org/victory-area/-/victory-area-37.3.6.tgz
Source33: https://registry.npmjs.org/victory-axis/-/victory-axis-37.3.6.tgz
Source34: https://registry.npmjs.org/victory-bar/-/victory-bar-37.3.6.tgz
Source35: https://registry.npmjs.org/victory-box-plot/-/victory-box-plot-37.3.6.tgz
Source36: https://registry.npmjs.org/victory-brush-container/-/victory-brush-container-37.3.6.tgz
Source37: https://registry.npmjs.org/victory-chart/-/victory-chart-37.3.6.tgz
Source38: https://registry.npmjs.org/victory-core/-/victory-core-37.3.6.tgz
Source39: https://registry.npmjs.org/victory-create-container/-/victory-create-container-37.3.6.tgz
Source40: https://registry.npmjs.org/victory-cursor-container/-/victory-cursor-container-37.3.6.tgz
Source41: https://registry.npmjs.org/victory-group/-/victory-group-37.3.6.tgz
Source42: https://registry.npmjs.org/victory-legend/-/victory-legend-37.3.6.tgz
Source43: https://registry.npmjs.org/victory-line/-/victory-line-37.3.6.tgz
Source44: https://registry.npmjs.org/victory-pie/-/victory-pie-37.3.6.tgz
Source45: https://registry.npmjs.org/victory-polar-axis/-/victory-polar-axis-37.3.6.tgz
Source46: https://registry.npmjs.org/victory-scatter/-/victory-scatter-37.3.6.tgz
Source47: https://registry.npmjs.org/victory-selection-container/-/victory-selection-container-37.3.6.tgz
Source48: https://registry.npmjs.org/victory-shared-events/-/victory-shared-events-37.3.6.tgz
Source49: https://registry.npmjs.org/victory-stack/-/victory-stack-37.3.6.tgz
Source50: https://registry.npmjs.org/victory-tooltip/-/victory-tooltip-37.3.6.tgz
Source51: https://registry.npmjs.org/victory-vendor/-/victory-vendor-37.3.6.tgz
Source52: https://registry.npmjs.org/victory-voronoi-container/-/victory-voronoi-container-37.3.6.tgz
Source53: https://registry.npmjs.org/victory-zoom-container/-/victory-zoom-container-37.3.6.tgz
Source54: nodejs-patternfly-react-charts-%{version}-package-lock.json
BuildRequires: npm >= 7
BuildRequires: nodejs-packaging
# The prep section runs node directly, so this is needed unconditionally. It
# also works around https://issues.redhat.com/browse/RHEL-137712 on RHEL 10
# before 10.3, where the nodejs major version macro does not resolve without
# node in the buildroot.
BuildRequires: /usr/bin/node
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: npm(%{npm_name}) = %{version}
Provides: bundled(npm(@patternfly/react-charts)) = 7.4.9
Provides: bundled(npm(@patternfly/react-styles)) = 5.4.1
Provides: bundled(npm(@patternfly/react-tokens)) = 5.4.1
Provides: bundled(npm(@types/d3-array)) = 3.2.2
Provides: bundled(npm(@types/d3-color)) = 3.1.3
Provides: bundled(npm(@types/d3-ease)) = 3.0.2
Provides: bundled(npm(@types/d3-interpolate)) = 3.0.4
Provides: bundled(npm(@types/d3-path)) = 3.1.1
Provides: bundled(npm(@types/d3-scale)) = 4.0.9
Provides: bundled(npm(@types/d3-shape)) = 3.1.8
Provides: bundled(npm(@types/d3-time)) = 3.0.4
Provides: bundled(npm(@types/d3-timer)) = 3.0.2
Provides: bundled(npm(d3-array)) = 3.2.4
Provides: bundled(npm(d3-color)) = 3.1.0
Provides: bundled(npm(d3-ease)) = 3.0.1
Provides: bundled(npm(d3-format)) = 3.1.2
Provides: bundled(npm(d3-interpolate)) = 3.0.1
Provides: bundled(npm(d3-path)) = 3.1.0
Provides: bundled(npm(d3-scale)) = 4.0.2
Provides: bundled(npm(d3-shape)) = 3.2.0
Provides: bundled(npm(d3-time)) = 3.1.0
Provides: bundled(npm(d3-time-format)) = 4.1.0
Provides: bundled(npm(d3-timer)) = 3.0.1
Provides: bundled(npm(delaunator)) = 4.0.1
Provides: bundled(npm(delaunay-find)) = 0.0.6
Provides: bundled(npm(hoist-non-react-statics)) = 3.3.2
Provides: bundled(npm(internmap)) = 2.0.3
Provides: bundled(npm(json-stringify-safe)) = 5.0.1
Provides: bundled(npm(lodash)) = 4.18.1
Provides: bundled(npm(react-fast-compare)) = 3.2.2
Provides: bundled(npm(react-is)) = 16.13.1
Provides: bundled(npm(tslib)) = 2.8.1
Provides: bundled(npm(victory-area)) = 37.3.6
Provides: bundled(npm(victory-axis)) = 37.3.6
Provides: bundled(npm(victory-bar)) = 37.3.6
Provides: bundled(npm(victory-box-plot)) = 37.3.6
Provides: bundled(npm(victory-brush-container)) = 37.3.6
Provides: bundled(npm(victory-chart)) = 37.3.6
Provides: bundled(npm(victory-core)) = 37.3.6
Provides: bundled(npm(victory-create-container)) = 37.3.6
Provides: bundled(npm(victory-cursor-container)) = 37.3.6
Provides: bundled(npm(victory-group)) = 37.3.6
Provides: bundled(npm(victory-legend)) = 37.3.6
Provides: bundled(npm(victory-line)) = 37.3.6
Provides: bundled(npm(victory-pie)) = 37.3.6
Provides: bundled(npm(victory-polar-axis)) = 37.3.6
Provides: bundled(npm(victory-scatter)) = 37.3.6
Provides: bundled(npm(victory-selection-container)) = 37.3.6
Provides: bundled(npm(victory-shared-events)) = 37.3.6
Provides: bundled(npm(victory-stack)) = 37.3.6
Provides: bundled(npm(victory-tooltip)) = 37.3.6
Provides: bundled(npm(victory-vendor)) = 37.3.6
Provides: bundled(npm(victory-voronoi-container)) = 37.3.6
Provides: bundled(npm(victory-zoom-container)) = 37.3.6
AutoReq: no
AutoProv: no

%define npm_cache_dir npm_cache_%{name}-%{version}-%{release}

%description
%{summary}

%prep
mkdir -p %{npm_cache_dir}
# npm ci installs the tree recorded in the lockfile: every entry carries a
# resolved URL and an integrity hash, and npm serves the tarballs from the
# cache primed here by content hash. No registry access is needed.
for src in %{sources}; do
  case "$src" in
    *.tgz) npm cache add --cache %{npm_cache_dir} "$src" ;;
    *-package-lock.json) cp "$src" package-lock.json ;;
  esac
done

# Derive package.json from the lockfile so the two cannot disagree.
node -e '
const fs = require("fs");
const lock = JSON.parse(fs.readFileSync("package-lock.json"));
fs.writeFileSync("package.json", JSON.stringify({
  name: lock.name,
  version: lock.version,
  dependencies: lock.packages[""].dependencies
}, null, 2) + "\n");
'

%build
npm ci --legacy-peer-deps --offline --cache %{_builddir}/%{npm_cache_dir} --omit optional

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
# npm creates a scope directory for every scope named in the lockfile, including
# scopes whose packages were all omitted, which leaves empty dirs behind.
# -delete implies -depth, so nested empties go bottom-up in a single pass.
find %{buildroot}%{nodejs_sitelib}/%{npm_name} -type d -empty -delete
cp -pfr node_modules/%{npm_name}/dist %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/single-packages.config.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/src %{buildroot}%{nodejs_sitelib}/%{npm_name}

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%license node_modules/%{npm_name}/LICENSE
%doc node_modules/%{npm_name}/CHANGELOG.md
%doc node_modules/%{npm_name}/README.md

%changelog
* Thu Jul 30 2026 Zach Huntington-Meath <zhunting@redhat.com> 7.4.9-3
- Update to 7.4.9

* Tue Mar 03 2026 Evgeni Golov 7.4.9-2
- Rebuild @patternfly/react-charts to update vendored dependencies

* Thu Jul 17 2025 Evgeni Golov 7.4.9-1
- Update to 7.4.9

* Thu Jun 19 2025 MariaAga <mariaaga@redhat.com> 6.94.15-1
- Add nodejs-patternfly-react-charts generated by npm2rpm using the bundle strategy

