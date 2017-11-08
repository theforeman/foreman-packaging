%global npm_name react-bootstrap
%global enable_tests 0

Name: nodejs-%{npm_name}
Version: 0.31.5
Release: 1%{?dist}
Summary: Bootstrap 3 components built with React
License: MIT
URL: https://react-bootstrap.github.io/
Source0: http://registry.npmjs.org/react-bootstrap/-/react-bootstrap-0.31.5.tgz
Source1: http://registry.npmjs.org/invariant/-/invariant-2.2.2.tgz
Source2: http://registry.npmjs.org/keycode/-/keycode-2.1.9.tgz
Source3: http://registry.npmjs.org/classnames/-/classnames-2.2.5.tgz
Source4: http://registry.npmjs.org/babel-runtime/-/babel-runtime-6.26.0.tgz
Source5: http://registry.npmjs.org/loose-envify/-/loose-envify-1.3.1.tgz
Source6: http://registry.npmjs.org/prop-types-extra/-/prop-types-extra-1.0.1.tgz
Source7: http://registry.npmjs.org/react-overlays/-/react-overlays-0.7.4.tgz
Source8: http://registry.npmjs.org/regenerator-runtime/-/regenerator-runtime-0.11.0.tgz
Source9: http://registry.npmjs.org/uncontrollable/-/uncontrollable-4.1.0.tgz
Source10: http://registry.npmjs.org/core-js/-/core-js-2.5.1.tgz
Source11: http://registry.npmjs.org/warning/-/warning-3.0.0.tgz
Source12: http://registry.npmjs.org/dom-helpers/-/dom-helpers-3.2.1.tgz
Source13: http://registry.npmjs.org/prop-types/-/prop-types-15.6.0.tgz
Source14: http://registry.npmjs.org/js-tokens/-/js-tokens-3.0.2.tgz
Source15: http://registry.npmjs.org/fbjs/-/fbjs-0.8.16.tgz
Source16: http://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz
Source17: http://registry.npmjs.org/promise/-/promise-7.3.1.tgz
Source18: http://registry.npmjs.org/isomorphic-fetch/-/isomorphic-fetch-2.2.1.tgz
Source19: http://registry.npmjs.org/ua-parser-js/-/ua-parser-js-0.7.17.tgz
Source20: http://registry.npmjs.org/core-js/-/core-js-1.2.7.tgz
Source21: http://registry.npmjs.org/asap/-/asap-2.0.6.tgz
Source22: http://registry.npmjs.org/node-fetch/-/node-fetch-1.7.3.tgz
Source23: http://registry.npmjs.org/whatwg-fetch/-/whatwg-fetch-2.0.3.tgz
Source24: http://registry.npmjs.org/is-stream/-/is-stream-1.1.0.tgz
Source25: http://registry.npmjs.org/encoding/-/encoding-0.1.12.tgz
Source26: http://registry.npmjs.org/iconv-lite/-/iconv-lite-0.4.19.tgz
Source27: http://registry.npmjs.org/setimmediate/-/setimmediate-1.0.5.tgz
Source28: react-bootstrap-0.31.5-registry.npmjs.org.tgz
BuildRequires: nodejs-packaging
BuildRequires: npm(react) >= 15.3.0
BuildRequires: npm(react-dom) >= 15.3.0
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: npm(%{npm_name}) = %{version}
Provides: bundled-npm(react-bootstrap) = 0.31.5
Provides: bundled-npm(invariant) = 2.2.2
Provides: bundled-npm(keycode) = 2.1.9
Provides: bundled-npm(classnames) = 2.2.5
Provides: bundled-npm(babel-runtime) = 6.26.0
Provides: bundled-npm(loose-envify) = 1.3.1
Provides: bundled-npm(prop-types-extra) = 1.0.1
Provides: bundled-npm(react-overlays) = 0.7.4
Provides: bundled-npm(regenerator-runtime) = 0.11.0
Provides: bundled-npm(uncontrollable) = 4.1.0
Provides: bundled-npm(core-js) = 2.5.1
Provides: bundled-npm(warning) = 3.0.0
Provides: bundled-npm(dom-helpers) = 3.2.1
Provides: bundled-npm(prop-types) = 15.6.0
Provides: bundled-npm(js-tokens) = 3.0.2
Provides: bundled-npm(fbjs) = 0.8.16
Provides: bundled-npm(object-assign) = 4.1.1
Provides: bundled-npm(promise) = 7.3.1
Provides: bundled-npm(isomorphic-fetch) = 2.2.1
Provides: bundled-npm(ua-parser-js) = 0.7.17
Provides: bundled-npm(core-js) = 1.2.7
Provides: bundled-npm(asap) = 2.0.6
Provides: bundled-npm(node-fetch) = 1.7.3
Provides: bundled-npm(whatwg-fetch) = 2.0.3
Provides: bundled-npm(is-stream) = 1.1.0
Provides: bundled-npm(encoding) = 0.1.12
Provides: bundled-npm(iconv-lite) = 0.4.19
Provides: bundled-npm(setimmediate) = 1.0.5
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

%setup -T -q -a 28 -D -n %{npm_cache_dir}

%build
mkdir node_modules
ln -s %{nodejs_sitelib}/{react,react-dom} node_modules/
npm install --cache-min Infinity --cache %{npm_cache_dir} --no-optional --global-style true %{npm_name}@%{version}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cd node_modules/react-bootstrap
cp -pfr CHANGELOG.md LICENSE README.md dist es lib package.json node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pf CHANGELOG.md README.md LICENSE ../../

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%endif

%files
%{nodejs_sitelib}/%{npm_name}

%license LICENSE
%doc CHANGELOG.md
%doc README.md

%changelog
* Wed Nov 08 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.31.5-1
- Bump nodejs-react-bootstrap to 0.31.5 (#1936) (github@kohlvanwijngaarden.nl)

* Thu May 11 2017 Dominic Cleal <dominic@cleal.org> 0.31.0-1
- Update react-bootstrap to 0.31.0 (dominic@cleal.org)

* Fri Oct 14 2016 Dominic Cleal <dominic@cleal.org> 0.30.5-2
- Use existing react, react-dom peer dependencies (dominic@cleal.org)

* Fri Oct 14 2016 Dominic Cleal <dominic@cleal.org> 0.30.5-1
- new package built with tito

