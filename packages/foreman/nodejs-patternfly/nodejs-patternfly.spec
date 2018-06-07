%global npm_name patternfly

Name: nodejs-%{npm_name}
Version: 3.48.3
Release: 1%{?dist}
Summary: This reference implementation of PatternFly is based on [Bootstrap v3](http://getbootstrap
License: Apache-2.0
Group: Development/Libraries
URL: https://github.com/patternfly/patternfly
Source0: https://registry.npmjs.org/patternfly/-/patternfly-3.48.3.tgz
Source1: https://registry.npmjs.org/font-awesome/-/font-awesome-4.7.0.tgz
Source2: https://registry.npmjs.org//-/-types/c3.tgz
Source3: https://registry.npmjs.org/jquery/-/jquery-3.2.1.tgz
Source4: https://registry.npmjs.org/bootstrap-select/-/bootstrap-select-1.12.2.tgz
Source5: https://registry.npmjs.org/bootstrap-sass/-/bootstrap-sass-3.3.7.tgz
Source6: https://registry.npmjs.org/bootstrap-datepicker/-/bootstrap-datepicker-1.8.0.tgz
Source7: https://registry.npmjs.org/bootstrap-slider/-/bootstrap-slider-9.10.0.tgz
Source8: https://registry.npmjs.org/bootstrap/-/bootstrap-3.3.7.tgz
Source9: https://registry.npmjs.org/bootstrap-switch/-/bootstrap-switch-3.3.4.tgz
Source10: https://registry.npmjs.org/datatables.net-colreorder/-/datatables.net-colreorder-1.4.1.tgz
Source11: https://registry.npmjs.org/bootstrap-touchspin/-/bootstrap-touchspin-3.1.1.tgz
Source12: https://registry.npmjs.org/c3/-/c3-0.4.23.tgz
Source13: https://registry.npmjs.org/datatables.net-colreorder-bs/-/datatables.net-colreorder-bs-1.3.3.tgz
Source14: https://registry.npmjs.org/datatables.net/-/datatables.net-1.10.16.tgz
Source15: https://registry.npmjs.org/drmonty-datatables-colvis/-/drmonty-datatables-colvis-1.1.2.tgz
Source16: https://registry.npmjs.org/google-code-prettify/-/google-code-prettify-1.0.5.tgz
Source17: https://registry.npmjs.org/datatables.net-select/-/datatables.net-select-1.2.5.tgz
Source18: https://registry.npmjs.org/jquery-match-height/-/jquery-match-height-0.7.2.tgz
Source19: https://registry.npmjs.org/eonasdan-bootstrap-datetimepicker/-/eonasdan-bootstrap-datetimepicker-4.17.47.tgz
Source20: https://registry.npmjs.org/font-awesome-sass/-/font-awesome-sass-4.7.0.tgz
Source21: https://registry.npmjs.org/d3/-/d3-3.5.17.tgz
Source22: https://registry.npmjs.org/moment-timezone/-/moment-timezone-0.4.1.tgz
Source23: https://registry.npmjs.org/patternfly-bootstrap-treeview/-/patternfly-bootstrap-treeview-2.1.5.tgz
Source24: https://registry.npmjs.org/moment/-/moment-2.22.2.tgz
Source25: https://registry.npmjs.org/patternfly-bootstrap-combobox/-/patternfly-bootstrap-combobox-1.1.7.tgz
Source26: https://registry.npmjs.org//-/-types/d3.tgz
Source27: https://registry.npmjs.org/jquery/-/jquery-3.3.1.tgz
Source28: https://registry.npmjs.org/datatables.net-bs/-/datatables.net-bs-2.1.1.tgz
Source29: https://registry.npmjs.org//-/-types/d3-axis.tgz
Source30: https://registry.npmjs.org//-/-types/d3-scale.tgz
Source31: https://registry.npmjs.org//-/-types/d3-array.tgz
Source32: https://registry.npmjs.org//-/-types/d3-collection.tgz
Source33: https://registry.npmjs.org//-/-types/d3-dispatch.tgz
Source34: https://registry.npmjs.org//-/-types/d3-chord.tgz
Source35: https://registry.npmjs.org//-/-types/d3-brush.tgz
Source36: https://registry.npmjs.org//-/-types/d3-drag.tgz
Source37: https://registry.npmjs.org//-/-types/d3-dsv.tgz
Source38: https://registry.npmjs.org//-/-types/d3-ease.tgz
Source39: https://registry.npmjs.org//-/-types/d3-force.tgz
Source40: https://registry.npmjs.org//-/-types/d3-hierarchy.tgz
Source41: https://registry.npmjs.org//-/-types/d3-format.tgz
Source42: https://registry.npmjs.org//-/-types/d3-interpolate.tgz
Source43: https://registry.npmjs.org//-/-types/d3-geo.tgz
Source44: https://registry.npmjs.org//-/-types/d3-path.tgz
Source45: https://registry.npmjs.org//-/-types/d3-quadtree.tgz
Source46: https://registry.npmjs.org//-/-types/d3-random.tgz
Source47: https://registry.npmjs.org//-/-types/d3-queue.tgz
Source48: https://registry.npmjs.org//-/-types/d3-polygon.tgz
Source49: https://registry.npmjs.org//-/-types/d3-request.tgz
Source50: https://registry.npmjs.org//-/-types/d3-selection.tgz
Source51: https://registry.npmjs.org//-/-types/d3-time-format.tgz
Source52: https://registry.npmjs.org//-/-types/d3-transition.tgz
Source53: https://registry.npmjs.org//-/-types/d3-shape.tgz
Source54: https://registry.npmjs.org//-/-types/d3-timer.tgz
Source55: https://registry.npmjs.org//-/-types/d3-voronoi.tgz
Source56: https://registry.npmjs.org//-/-types/d3-time.tgz
Source57: https://registry.npmjs.org/datatables.net/-/datatables.net-2.1.1.tgz
Source58: https://registry.npmjs.org//-/-types/d3-zoom.tgz
Source59: https://registry.npmjs.org//-/-types/geojson.tgz
Source60: https://registry.npmjs.org//-/-types/d3-color.tgz
Source61: %{npm_name}-%{version}-registry.npmjs.org.tgz
BuildRequires: nodejs-packaging
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: npm(%{npm_name}) = %{version}
Provides: bundled(npm()) = types/d3-scale
Provides: bundled(npm()) = types/d3-color
Provides: bundled(npm()) = types/c3
Provides: bundled(npm()) = types/geojson
Provides: bundled(npm()) = types/d3-zoom
Provides: bundled(npm()) = types/d3-time
Provides: bundled(npm()) = types/d3-voronoi
Provides: bundled(npm()) = types/d3-timer
Provides: bundled(npm()) = types/d3-shape
Provides: bundled(npm()) = types/d3-transition
Provides: bundled(npm()) = types/d3-time-format
Provides: bundled(npm()) = types/d3-selection
Provides: bundled(npm()) = types/d3-request
Provides: bundled(npm()) = types/d3-polygon
Provides: bundled(npm()) = types/d3-queue
Provides: bundled(npm()) = types/d3-random
Provides: bundled(npm()) = types/d3-quadtree
Provides: bundled(npm()) = types/d3-path
Provides: bundled(npm()) = types/d3-geo
Provides: bundled(npm()) = types/d3-interpolate
Provides: bundled(npm()) = types/d3-format
Provides: bundled(npm()) = types/d3-hierarchy
Provides: bundled(npm()) = types/d3-force
Provides: bundled(npm()) = types/d3-ease
Provides: bundled(npm()) = types/d3-dsv
Provides: bundled(npm()) = types/d3-drag
Provides: bundled(npm()) = types/d3
Provides: bundled(npm()) = types/d3-brush
Provides: bundled(npm()) = types/d3-chord
Provides: bundled(npm()) = types/d3-axis
Provides: bundled(npm()) = types/d3-dispatch
Provides: bundled(npm()) = types/d3-array
Provides: bundled(npm()) = types/d3-collection
Provides: bundled(npm(bootstrap)) = 3.3.7
Provides: bundled(npm(bootstrap-datepicker)) = 1.8.0
Provides: bundled(npm(bootstrap-sass)) = 3.3.7
Provides: bundled(npm(bootstrap-select)) = 1.12.2
Provides: bundled(npm(bootstrap-slider)) = 9.10.0
Provides: bundled(npm(bootstrap-switch)) = 3.3.4
Provides: bundled(npm(bootstrap-touchspin)) = 3.1.1
Provides: bundled(npm(c3)) = 0.4.23
Provides: bundled(npm(d3)) = 3.5.17
Provides: bundled(npm(datatables.net)) = 1.10.16
Provides: bundled(npm(datatables.net)) = 2.1.1
Provides: bundled(npm(datatables.net-bs)) = 2.1.1
Provides: bundled(npm(datatables.net-colreorder)) = 1.4.1
Provides: bundled(npm(datatables.net-colreorder-bs)) = 1.3.3
Provides: bundled(npm(datatables.net-select)) = 1.2.5
Provides: bundled(npm(drmonty-datatables-colvis)) = 1.1.2
Provides: bundled(npm(eonasdan-bootstrap-datetimepicker)) = 4.17.47
Provides: bundled(npm(font-awesome)) = 4.7.0
Provides: bundled(npm(font-awesome-sass)) = 4.7.0
Provides: bundled(npm(google-code-prettify)) = 1.0.5
Provides: bundled(npm(jquery)) = 3.3.1
Provides: bundled(npm(jquery)) = 3.2.1
Provides: bundled(npm(jquery-match-height)) = 0.7.2
Provides: bundled(npm(moment)) = 2.22.2
Provides: bundled(npm(moment-timezone)) = 0.4.1
Provides: bundled(npm(patternfly)) = 3.48.3
Provides: bundled(npm(patternfly-bootstrap-combobox)) = 1.1.7
Provides: bundled(npm(patternfly-bootstrap-treeview)) = 2.1.5
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
%setup -T -q -a 61 -D -n %{npm_cache_dir}

%build
npm install --cache-min Infinity --cache %{npm_cache_dir} --no-shrinkwrap --no-optional --global-style true %{npm_name}@%{version}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/dist %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/tests %{buildroot}%{nodejs_sitelib}/%{npm_name}

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%license node_modules/%{npm_name}/LICENSE.txt
%doc node_modules/%{npm_name}/README.md

%changelog
* Thu Jun 07 2018 Tomas Strachota <tstrachota@redhat.com> 3.48.3-1
- Update to 3.48.3

* Tue May 01 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 3.45.0-1
- Update to 3.45.0

* Tue Apr 03 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 3.41.6-1
- Update to 3.41.6

* Thu Feb 22 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 3.40.0-1
- Bump nodejs-patternfly to 3.40.0 (ewoud@kohlvanwijngaarden.nl)

* Wed Feb 21 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 3.39.0-1
- Bump nodejs-patternfly to 3.39.0 (ewoud@kohlvanwijngaarden.nl)
- Restructure foreman packages to prepare for obal (pcreech@redhat.com)

* Thu Jan 11 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 3.35.1-1
- Bump nodejs-patternfly to 3.35.1 (ewoud@kohlvanwijngaarden.nl)

* Thu Jan 04 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 3.32.1-1
- Update nodejs-patternfly to 3.32.1 (me@daniellobato.me)
- Correct nodejs spec filenames (github@kohlvanwijngaarden.nl)

* Wed Nov 08 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 3.29.13-1
- new package built with tito

