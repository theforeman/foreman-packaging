%global npm_name react-bootstrap

Name: nodejs-%{npm_name}
Version: 0.32.1
Release: 1%{?dist}
Summary: Bootstrap 3 components built with React
License: MIT
Group: Development/Libraries
URL: https://react-bootstrap.github.io/
Source0: https://registry.npmjs.org/react-bootstrap/-/react-bootstrap-0.32.1.tgz
Source1: https://registry.npmjs.org/prop-types-extra/-/prop-types-extra-1.0.1.tgz
Source2: https://registry.npmjs.org/invariant/-/invariant-2.2.4.tgz
Source3: https://registry.npmjs.org/keycode/-/keycode-2.2.0.tgz
Source4: https://registry.npmjs.org/classnames/-/classnames-2.2.5.tgz
Source5: https://registry.npmjs.org/dom-helpers/-/dom-helpers-3.3.1.tgz
Source6: https://registry.npmjs.org/prop-types/-/prop-types-15.6.1.tgz
Source7: https://registry.npmjs.org/babel-runtime/-/babel-runtime-6.26.0.tgz
Source8: https://registry.npmjs.org/react-overlays/-/react-overlays-0.8.3.tgz
Source9: https://registry.npmjs.org/warning/-/warning-3.0.0.tgz
Source10: https://registry.npmjs.org/loose-envify/-/loose-envify-1.3.1.tgz
Source11: https://registry.npmjs.org/react-transition-group/-/react-transition-group-2.3.1.tgz
Source12: https://registry.npmjs.org/uncontrollable/-/uncontrollable-4.1.0.tgz
Source13: https://registry.npmjs.org/fbjs/-/fbjs-0.8.16.tgz
Source14: https://registry.npmjs.org/react-prop-types/-/react-prop-types-0.4.0.tgz
Source15: https://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz
Source16: https://registry.npmjs.org/core-js/-/core-js-2.5.5.tgz
Source17: https://registry.npmjs.org/regenerator-runtime/-/regenerator-runtime-0.11.1.tgz
Source18: https://registry.npmjs.org/isomorphic-fetch/-/isomorphic-fetch-2.2.1.tgz
Source19: https://registry.npmjs.org/core-js/-/core-js-1.2.7.tgz
Source20: https://registry.npmjs.org/setimmediate/-/setimmediate-1.0.5.tgz
Source21: https://registry.npmjs.org/js-tokens/-/js-tokens-3.0.2.tgz
Source22: https://registry.npmjs.org/promise/-/promise-7.3.1.tgz
Source23: https://registry.npmjs.org/ua-parser-js/-/ua-parser-js-0.7.17.tgz
Source24: https://registry.npmjs.org/node-fetch/-/node-fetch-1.7.3.tgz
Source25: https://registry.npmjs.org/whatwg-fetch/-/whatwg-fetch-2.0.4.tgz
Source26: https://registry.npmjs.org/asap/-/asap-2.0.6.tgz
Source27: https://registry.npmjs.org/encoding/-/encoding-0.1.12.tgz
Source28: https://registry.npmjs.org/is-stream/-/is-stream-1.1.0.tgz
Source29: https://registry.npmjs.org/iconv-lite/-/iconv-lite-0.4.21.tgz
Source30: https://registry.npmjs.org/safer-buffer/-/safer-buffer-2.1.2.tgz
Source31: %{npm_name}-%{version}-registry.npmjs.org.tgz
BuildRequires: nodejs-packaging
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: npm(%{npm_name}) = %{version}
Provides: bundled(npm(asap)) = 2.0.6
Provides: bundled(npm(babel-runtime)) = 6.26.0
Provides: bundled(npm(classnames)) = 2.2.5
Provides: bundled(npm(core-js)) = 1.2.7
Provides: bundled(npm(core-js)) = 2.5.5
Provides: bundled(npm(dom-helpers)) = 3.3.1
Provides: bundled(npm(encoding)) = 0.1.12
Provides: bundled(npm(fbjs)) = 0.8.16
Provides: bundled(npm(iconv-lite)) = 0.4.21
Provides: bundled(npm(invariant)) = 2.2.4
Provides: bundled(npm(is-stream)) = 1.1.0
Provides: bundled(npm(isomorphic-fetch)) = 2.2.1
Provides: bundled(npm(js-tokens)) = 3.0.2
Provides: bundled(npm(keycode)) = 2.2.0
Provides: bundled(npm(loose-envify)) = 1.3.1
Provides: bundled(npm(node-fetch)) = 1.7.3
Provides: bundled(npm(object-assign)) = 4.1.1
Provides: bundled(npm(promise)) = 7.3.1
Provides: bundled(npm(prop-types)) = 15.6.1
Provides: bundled(npm(prop-types-extra)) = 1.0.1
Provides: bundled(npm(react-bootstrap)) = 0.32.1
Provides: bundled(npm(react-overlays)) = 0.8.3
Provides: bundled(npm(react-prop-types)) = 0.4.0
Provides: bundled(npm(react-transition-group)) = 2.3.1
Provides: bundled(npm(regenerator-runtime)) = 0.11.1
Provides: bundled(npm(safer-buffer)) = 2.1.2
Provides: bundled(npm(setimmediate)) = 1.0.5
Provides: bundled(npm(ua-parser-js)) = 0.7.17
Provides: bundled(npm(uncontrollable)) = 4.1.0
Provides: bundled(npm(warning)) = 3.0.0
Provides: bundled(npm(whatwg-fetch)) = 2.0.4
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
%setup -T -q -a 31 -D -n %{npm_cache_dir}

%build
npm install --cache-min Infinity --cache %{npm_cache_dir} --no-shrinkwrap --no-optional --global-style true %{npm_name}@%{version}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/dist %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/es %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/lib %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%license node_modules/%{npm_name}/LICENSE
%doc node_modules/%{npm_name}/CHANGELOG.md
%doc node_modules/%{npm_name}/README.md

%changelog
* Tue May 01 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.32.1-1
- Update to 0.32.1

* Wed Nov 08 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 0.31.5-1
- Bump nodejs-react-bootstrap to 0.31.5 (#1936) (github@kohlvanwijngaarden.nl)

* Thu May 11 2017 Dominic Cleal <dominic@cleal.org> 0.31.0-1
- Update react-bootstrap to 0.31.0 (dominic@cleal.org)

* Fri Oct 14 2016 Dominic Cleal <dominic@cleal.org> 0.30.5-2
- Use existing react, react-dom peer dependencies (dominic@cleal.org)

* Fri Oct 14 2016 Dominic Cleal <dominic@cleal.org> 0.30.5-1
- new package built with tito

