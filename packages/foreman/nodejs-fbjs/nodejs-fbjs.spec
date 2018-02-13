%global npm_name fbjs

Name: nodejs-%{npm_name}
Version: 0.8.16
Release: 1%{?dist}
Summary: A collection of utility libraries used by other Facebook JS projects
License: MIT
Group: Development/Libraries
URL: https://github.com/facebook/fbjs
Source0: https://registry.npmjs.org/fbjs/-/fbjs-0.8.16.tgz
Source1: https://registry.npmjs.org/isomorphic-fetch/-/isomorphic-fetch-2.2.1.tgz
Source2: https://registry.npmjs.org/promise/-/promise-7.3.1.tgz
Source3: https://registry.npmjs.org/setimmediate/-/setimmediate-1.0.5.tgz
Source4: https://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz
Source5: https://registry.npmjs.org/ua-parser-js/-/ua-parser-js-0.7.17.tgz
Source6: https://registry.npmjs.org/core-js/-/core-js-1.2.7.tgz
Source7: https://registry.npmjs.org/whatwg-fetch/-/whatwg-fetch-2.0.3.tgz
Source8: https://registry.npmjs.org/node-fetch/-/node-fetch-1.7.3.tgz
Source9: https://registry.npmjs.org/asap/-/asap-2.0.6.tgz
Source10: https://registry.npmjs.org/loose-envify/-/loose-envify-1.3.1.tgz
Source11: https://registry.npmjs.org/is-stream/-/is-stream-1.1.0.tgz
Source12: https://registry.npmjs.org/encoding/-/encoding-0.1.12.tgz
Source13: https://registry.npmjs.org/js-tokens/-/js-tokens-3.0.2.tgz
Source14: https://registry.npmjs.org/iconv-lite/-/iconv-lite-0.4.19.tgz
Source15: %{npm_name}-%{version}-registry.npmjs.org.tgz
BuildRequires: nodejs-packaging
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: npm(%{npm_name}) = %{version}
Provides: bundled-npm(whatwg-fetch) = 2.0.3
Provides: bundled-npm(fbjs) = 0.8.16
Provides: bundled-npm(promise) = 7.3.1
Provides: bundled-npm(setimmediate) = 1.0.5
Provides: bundled-npm(object-assign) = 4.1.1
Provides: bundled-npm(ua-parser-js) = 0.7.17
Provides: bundled-npm(core-js) = 1.2.7
Provides: bundled-npm(isomorphic-fetch) = 2.2.1
Provides: bundled-npm(node-fetch) = 1.7.3
Provides: bundled-npm(asap) = 2.0.6
Provides: bundled-npm(loose-envify) = 1.3.1
Provides: bundled-npm(is-stream) = 1.1.0
Provides: bundled-npm(encoding) = 0.1.12
Provides: bundled-npm(js-tokens) = 3.0.2
Provides: bundled-npm(iconv-lite) = 0.4.19
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
%setup -T -q -a 15 -D -n %{npm_cache_dir}

%build
npm install --cache-min Infinity --cache %{npm_cache_dir} --no-optional --global-style true %{npm_name}@%{version}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cd node_modules/fbjs
cp -pfr CHANGELOG.md LICENSE README.md flow index.js lib module-map.json package.json node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr CHANGELOG.md LICENSE README.md ../../

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE
%doc CHANGELOG.md
%doc README.md

%changelog
* Fri Nov 24 2017 Daniel Lobato Garcia <me@daniellobato.me> 0.8.16-1
- Bump nodejs-fbjs to 0.8.16 (github@kohlvanwijngaarden.nl)

* Sat Jul 15 2017 Eric D. Helms <ericdhelms@gmail.com> 0.8.12-2
- Add back missing Provides: npm (ericdhelms@gmail.com)

* Sat Jul 15 2017 Eric D. Helms <ericdhelms@gmail.com> 0.8.12-1
- new package built with tito

