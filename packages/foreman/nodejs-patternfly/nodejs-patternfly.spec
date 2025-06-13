%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name patternfly

Name: %{?scl_prefix}nodejs-patternfly
Version: 3.59.5
Release: 1%{?dist}
Summary: This reference implementation of PatternFly is based on [Bootstrap v3](http://getbootstrap
License: MIT
Group: Development/Libraries
URL: https://github.com/patternfly/patternfly-3
Source0: https://registry.npmjs.org/@types/c3/-/c3-0.6.4.tgz
Source1: https://registry.npmjs.org/@types/d3/-/d3-4.13.15.tgz
Source2: https://registry.npmjs.org/@types/d3-array/-/d3-array-1.2.12.tgz
Source3: https://registry.npmjs.org/@types/d3-axis/-/d3-axis-1.0.19.tgz
Source4: https://registry.npmjs.org/@types/d3-brush/-/d3-brush-1.1.8.tgz
Source5: https://registry.npmjs.org/@types/d3-chord/-/d3-chord-1.0.14.tgz
Source6: https://registry.npmjs.org/@types/d3-collection/-/d3-collection-1.0.13.tgz
Source7: https://registry.npmjs.org/@types/d3-color/-/d3-color-1.4.5.tgz
Source8: https://registry.npmjs.org/@types/d3-dispatch/-/d3-dispatch-1.0.12.tgz
Source9: https://registry.npmjs.org/@types/d3-drag/-/d3-drag-1.2.8.tgz
Source10: https://registry.npmjs.org/@types/d3-dsv/-/d3-dsv-1.2.8.tgz
Source11: https://registry.npmjs.org/@types/d3-ease/-/d3-ease-1.0.13.tgz
Source12: https://registry.npmjs.org/@types/d3-force/-/d3-force-1.2.7.tgz
Source13: https://registry.npmjs.org/@types/d3-format/-/d3-format-1.4.5.tgz
Source14: https://registry.npmjs.org/@types/d3-geo/-/d3-geo-1.12.7.tgz
Source15: https://registry.npmjs.org/@types/d3-hierarchy/-/d3-hierarchy-1.1.11.tgz
Source16: https://registry.npmjs.org/@types/d3-interpolate/-/d3-interpolate-1.4.5.tgz
Source17: https://registry.npmjs.org/@types/d3-path/-/d3-path-1.0.11.tgz
Source18: https://registry.npmjs.org/@types/d3-polygon/-/d3-polygon-1.0.10.tgz
Source19: https://registry.npmjs.org/@types/d3-quadtree/-/d3-quadtree-1.0.13.tgz
Source20: https://registry.npmjs.org/@types/d3-queue/-/d3-queue-3.0.10.tgz
Source21: https://registry.npmjs.org/@types/d3-random/-/d3-random-1.1.5.tgz
Source22: https://registry.npmjs.org/@types/d3-request/-/d3-request-1.0.9.tgz
Source23: https://registry.npmjs.org/@types/d3-scale/-/d3-scale-1.0.22.tgz
Source24: https://registry.npmjs.org/@types/d3-selection/-/d3-selection-1.4.7.tgz
Source25: https://registry.npmjs.org/@types/d3-shape/-/d3-shape-1.3.12.tgz
Source26: https://registry.npmjs.org/@types/d3-time/-/d3-time-1.1.4.tgz
Source27: https://registry.npmjs.org/@types/d3-time-format/-/d3-time-format-2.3.4.tgz
Source28: https://registry.npmjs.org/@types/d3-timer/-/d3-timer-1.0.12.tgz
Source29: https://registry.npmjs.org/@types/d3-transition/-/d3-transition-1.3.6.tgz
Source30: https://registry.npmjs.org/@types/d3-voronoi/-/d3-voronoi-1.1.12.tgz
Source31: https://registry.npmjs.org/@types/d3-zoom/-/d3-zoom-1.8.7.tgz
Source32: https://registry.npmjs.org/@types/geojson/-/geojson-7946.0.16.tgz
Source33: https://registry.npmjs.org/bootstrap/-/bootstrap-3.4.1.tgz
Source34: https://registry.npmjs.org/bootstrap-datepicker/-/bootstrap-datepicker-1.10.0.tgz
Source35: https://registry.npmjs.org/bootstrap-sass/-/bootstrap-sass-3.4.3.tgz
Source36: https://registry.npmjs.org/bootstrap-select/-/bootstrap-select-1.12.2.tgz
Source37: https://registry.npmjs.org/bootstrap-slider/-/bootstrap-slider-9.10.0.tgz
Source38: https://registry.npmjs.org/bootstrap-switch/-/bootstrap-switch-3.3.4.tgz
Source39: https://registry.npmjs.org/bootstrap-touchspin/-/bootstrap-touchspin-3.1.1.tgz
Source40: https://registry.npmjs.org/c3/-/c3-0.4.24.tgz
Source41: https://registry.npmjs.org/d3/-/d3-3.5.17.tgz
Source42: https://registry.npmjs.org/datatables.net/-/datatables.net-1.13.11.tgz
Source43: https://registry.npmjs.org/datatables.net/-/datatables.net-2.3.2.tgz
Source44: https://registry.npmjs.org/datatables.net-bs/-/datatables.net-bs-2.3.2.tgz
Source45: https://registry.npmjs.org/datatables.net-colreorder/-/datatables.net-colreorder-1.7.2.tgz
Source46: https://registry.npmjs.org/datatables.net-colreorder/-/datatables.net-colreorder-2.1.1.tgz
Source47: https://registry.npmjs.org/datatables.net-colreorder-bs/-/datatables.net-colreorder-bs-1.3.3.tgz
Source48: https://registry.npmjs.org/datatables.net-select/-/datatables.net-select-1.2.7.tgz
Source49: https://registry.npmjs.org/drmonty-datatables-colvis/-/drmonty-datatables-colvis-1.1.2.tgz
Source50: https://registry.npmjs.org/eonasdan-bootstrap-datetimepicker/-/eonasdan-bootstrap-datetimepicker-4.17.49.tgz
Source51: https://registry.npmjs.org/font-awesome/-/font-awesome-4.7.0.tgz
Source52: https://registry.npmjs.org/font-awesome-sass/-/font-awesome-sass-4.7.0.tgz
Source53: https://registry.npmjs.org/google-code-prettify/-/google-code-prettify-1.0.5.tgz
Source54: https://registry.npmjs.org/jquery/-/jquery-3.4.1.tgz
Source55: https://registry.npmjs.org/jquery/-/jquery-3.7.1.tgz
Source56: https://registry.npmjs.org/jquery-match-height/-/jquery-match-height-0.7.2.tgz
Source57: https://registry.npmjs.org/moment/-/moment-2.30.1.tgz
Source58: https://registry.npmjs.org/moment-timezone/-/moment-timezone-0.4.1.tgz
Source59: https://registry.npmjs.org/patternfly/-/patternfly-3.59.5.tgz
Source60: https://registry.npmjs.org/patternfly-bootstrap-combobox/-/patternfly-bootstrap-combobox-1.1.7.tgz
Source61: https://registry.npmjs.org/patternfly-bootstrap-treeview/-/patternfly-bootstrap-treeview-2.1.10.tgz
Source62: nodejs-patternfly-%{version}-registry.npmjs.org.tgz
BuildRequires: %{?scl_prefix_nodejs}npm
%if 0%{!?scl:1}
BuildRequires: nodejs-packaging
%endif
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}
Provides: bundled(npm(@types/c3)) = 0.6.4
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
Provides: bundled(npm(bootstrap)) = 3.4.1
Provides: bundled(npm(bootstrap-datepicker)) = 1.10.0
Provides: bundled(npm(bootstrap-sass)) = 3.4.3
Provides: bundled(npm(bootstrap-select)) = 1.12.2
Provides: bundled(npm(bootstrap-slider)) = 9.10.0
Provides: bundled(npm(bootstrap-switch)) = 3.3.4
Provides: bundled(npm(bootstrap-touchspin)) = 3.1.1
Provides: bundled(npm(c3)) = 0.4.24
Provides: bundled(npm(d3)) = 3.5.17
Provides: bundled(npm(datatables.net)) = 1.13.11
Provides: bundled(npm(datatables.net)) = 2.3.2
Provides: bundled(npm(datatables.net-bs)) = 2.3.2
Provides: bundled(npm(datatables.net-colreorder)) = 1.7.2
Provides: bundled(npm(datatables.net-colreorder)) = 2.1.1
Provides: bundled(npm(datatables.net-colreorder-bs)) = 1.3.3
Provides: bundled(npm(datatables.net-select)) = 1.2.7
Provides: bundled(npm(drmonty-datatables-colvis)) = 1.1.2
Provides: bundled(npm(eonasdan-bootstrap-datetimepicker)) = 4.17.49
Provides: bundled(npm(font-awesome)) = 4.7.0
Provides: bundled(npm(font-awesome-sass)) = 4.7.0
Provides: bundled(npm(google-code-prettify)) = 1.0.5
Provides: bundled(npm(jquery)) = 3.4.1
Provides: bundled(npm(jquery)) = 3.7.1
Provides: bundled(npm(jquery-match-height)) = 0.7.2
Provides: bundled(npm(moment)) = 2.30.1
Provides: bundled(npm(moment-timezone)) = 0.4.1
Provides: bundled(npm(patternfly)) = 3.59.5
Provides: bundled(npm(patternfly-bootstrap-combobox)) = 1.1.7
Provides: bundled(npm(patternfly-bootstrap-treeview)) = 2.1.10
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

%setup -T -q -a 62 -D -n %{npm_cache_dir}

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
%license node_modules/%{npm_name}/LICENSE.txt
%doc node_modules/%{npm_name}/README.md

%changelog
* Fri Jun 13 2025 MariaAga <mariaaga@redhat.com> 3.59.5-1
- Add nodejs-patternfly generated by npm2rpm using the bundle strategy

