%global npm_name fbjs
%global enable_tests 0

%{?nodejs_find_provides_and_requires}

Name: nodejs-%{npm_name}
Version: 0.8.12
Release: 1%{?dist}
Summary: A collection of utility libraries used by other Facebook JS projects
License: BSD-3-Clause
URL: FIXME
Source0: http://registry.npmjs.org/fbjs/-/fbjs-0.8.12.tgz
Source1: http://registry.npmjs.org/loose-envify/-/loose-envify-1.3.1.tgz
Source2: http://registry.npmjs.org/setimmediate/-/setimmediate-1.0.5.tgz
Source3: http://registry.npmjs.org/promise/-/promise-7.3.1.tgz
Source4: http://registry.npmjs.org/isomorphic-fetch/-/isomorphic-fetch-2.2.1.tgz
Source5: http://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz
Source6: http://registry.npmjs.org/ua-parser-js/-/ua-parser-js-0.7.13.tgz
Source7: http://registry.npmjs.org/core-js/-/core-js-1.2.7.tgz
Source8: http://registry.npmjs.org/whatwg-fetch/-/whatwg-fetch-2.0.3.tgz
Source9: http://registry.npmjs.org/js-tokens/-/js-tokens-3.0.1.tgz
Source10: http://registry.npmjs.org/asap/-/asap-2.0.5.tgz
Source11: http://registry.npmjs.org/node-fetch/-/node-fetch-1.7.1.tgz
Source12: http://registry.npmjs.org/is-stream/-/is-stream-1.1.0.tgz
Source13: http://registry.npmjs.org/encoding/-/encoding-0.1.12.tgz
Source14: http://registry.npmjs.org/iconv-lite/-/iconv-lite-0.4.18.tgz
Source15: fbjs-0.8.12-registry.npmjs.org.tgz
BuildRequires: nodejs-packaging
BuildRequires: npm
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: bundled-npm(fbjs) = 0.8.12
Provides: bundled-npm(loose-envify) = 1.3.1
Provides: bundled-npm(setimmediate) = 1.0.5
Provides: bundled-npm(promise) = 7.3.1
Provides: bundled-npm(isomorphic-fetch) = 2.2.1
Provides: bundled-npm(object-assign) = 4.1.1
Provides: bundled-npm(ua-parser-js) = 0.7.13
Provides: bundled-npm(core-js) = 1.2.7
Provides: bundled-npm(whatwg-fetch) = 2.0.3
Provides: bundled-npm(js-tokens) = 3.0.1
Provides: bundled-npm(asap) = 2.0.5
Provides: bundled-npm(node-fetch) = 1.7.1
Provides: bundled-npm(is-stream) = 1.1.0
Provides: bundled-npm(encoding) = 0.1.12
Provides: bundled-npm(iconv-lite) = 0.4.18
AutoReq: no
AutoProv: no


%description
%{summary}

%prep
mkdir npm_cache
for tgz in %{sources}; do
  echo $tgz | grep -q registry.npmjs.org || npm cache add --cache ./npm_cache $tgz
done

%setup -T -q -a 15 -D -n npm_cache

%build
npm install --cache-min Infinity --cache . --no-optional --global-style true %{npm_name}@%{version}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cd node_modules/fbjs
cp -pfr CHANGELOG.md PATENTS README.md flow index.js lib module-map.json package.json node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pf CHANGELOG.md README.md ../../
# If any binaries are included, symlink them to bindir here

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
#$CHECK
%endif

%files
%{nodejs_sitelib}/%{npm_name}

%doc CHANGELOG.md
%doc README.md

%changelog
