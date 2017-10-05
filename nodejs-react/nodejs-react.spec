%global npm_name react
%global enable_tests 0

%{?nodejs_find_provides_and_requires}

Name: nodejs-%{npm_name}
Version: 15.6.2
Release: 1%{?dist}
Summary: React is a JavaScript library for building user interfaces
License: MIT
URL: https://facebook.github.io/react/
Source0: http://registry.npmjs.org/react/-/react-15.6.2.tgz
Source1: http://registry.npmjs.org/loose-envify/-/loose-envify-1.3.1.tgz
Source2: http://registry.npmjs.org/create-react-class/-/create-react-class-15.6.2.tgz
Source3: http://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz
Source4: http://registry.npmjs.org/prop-types/-/prop-types-15.6.0.tgz
Source5: http://registry.npmjs.org/fbjs/-/fbjs-0.8.16.tgz
Source6: http://registry.npmjs.org/js-tokens/-/js-tokens-3.0.2.tgz
Source7: http://registry.npmjs.org/isomorphic-fetch/-/isomorphic-fetch-2.2.1.tgz
Source8: http://registry.npmjs.org/setimmediate/-/setimmediate-1.0.5.tgz
Source9: http://registry.npmjs.org/promise/-/promise-7.3.1.tgz
Source10: http://registry.npmjs.org/core-js/-/core-js-1.2.7.tgz
Source11: http://registry.npmjs.org/ua-parser-js/-/ua-parser-js-0.7.14.tgz
Source12: http://registry.npmjs.org/whatwg-fetch/-/whatwg-fetch-2.0.3.tgz
Source13: http://registry.npmjs.org/asap/-/asap-2.0.6.tgz
Source14: http://registry.npmjs.org/node-fetch/-/node-fetch-1.7.3.tgz
Source15: http://registry.npmjs.org/encoding/-/encoding-0.1.12.tgz
Source16: http://registry.npmjs.org/is-stream/-/is-stream-1.1.0.tgz
Source17: http://registry.npmjs.org/iconv-lite/-/iconv-lite-0.4.19.tgz
Source18: react-15.6.2-registry.npmjs.org.tgz
BuildRequires: nodejs-packaging
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: npm(%{npm_name}) = %{version}
Provides: bundled-npm(react) = 15.6.2
Provides: bundled-npm(loose-envify) = 1.3.1
Provides: bundled-npm(create-react-class) = 15.6.2
Provides: bundled-npm(object-assign) = 4.1.1
Provides: bundled-npm(prop-types) = 15.6.0
Provides: bundled-npm(fbjs) = 0.8.16
Provides: bundled-npm(js-tokens) = 3.0.2
Provides: bundled-npm(isomorphic-fetch) = 2.2.1
Provides: bundled-npm(setimmediate) = 1.0.5
Provides: bundled-npm(promise) = 7.3.1
Provides: bundled-npm(core-js) = 1.2.7
Provides: bundled-npm(ua-parser-js) = 0.7.14
Provides: bundled-npm(whatwg-fetch) = 2.0.3
Provides: bundled-npm(asap) = 2.0.6
Provides: bundled-npm(node-fetch) = 1.7.3
Provides: bundled-npm(encoding) = 0.1.12
Provides: bundled-npm(is-stream) = 1.1.0
Provides: bundled-npm(iconv-lite) = 0.4.19
AutoReq: no
AutoProv: no

%description
%{summary}

%prep
mkdir -p npm_cache
for tgz in %{sources}; do
  echo $tgz | grep -q registry.npmjs.org || npm cache add --cache ./npm_cache $tgz
done

%setup -T -q -a 18 -D -n npm_cache

%build
npm install --cache-min Infinity --cache . --no-optional --global-style true %{npm_name}@%{version}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cd node_modules/react
cp -pfr LICENSE README.md dist lib package.json react.js node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pf README.md LICENSE ../../

%clean
rm -rf %{buildroot} npm_cache

%files
%{nodejs_sitelib}/%{npm_name}

%doc LICENSE
%doc README.md

%changelog
* Thu Oct 05 2017 Eric D. Helms <ericdhelms@gmail.com> 15.6.2-1
- Update React to 15.6.2 (me@daniellobato.me)

* Fri Oct 14 2016 Dominic Cleal <dominic@cleal.org> 15.3.2-1
- new package built with tito
