%global npm_name react-redux

Name: nodejs-%{npm_name}
Version: 5.0.6
Release: 1%{?dist}
Summary: Official React bindings for Redux
License: MIT
Group: Development/Libraries
URL: https://github.com/gaearon/react-redux
Source0: https://registry.npmjs.org/react-redux/-/react-redux-5.0.6.tgz
Source1: https://registry.npmjs.org/loose-envify/-/loose-envify-1.3.1.tgz
Source2: https://registry.npmjs.org/invariant/-/invariant-2.2.2.tgz
Source3: https://registry.npmjs.org/lodash/-/lodash-4.17.4.tgz
Source4: https://registry.npmjs.org/hoist-non-react-statics/-/hoist-non-react-statics-2.3.1.tgz
Source5: https://registry.npmjs.org/prop-types/-/prop-types-15.6.0.tgz
Source6: https://registry.npmjs.org/lodash-es/-/lodash-es-4.17.4.tgz
Source7: https://registry.npmjs.org/js-tokens/-/js-tokens-3.0.2.tgz
Source8: https://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz
Source9: https://registry.npmjs.org/fbjs/-/fbjs-0.8.16.tgz
Source10: https://registry.npmjs.org/promise/-/promise-7.3.1.tgz
Source11: https://registry.npmjs.org/setimmediate/-/setimmediate-1.0.5.tgz
Source12: https://registry.npmjs.org/isomorphic-fetch/-/isomorphic-fetch-2.2.1.tgz
Source13: https://registry.npmjs.org/core-js/-/core-js-1.2.7.tgz
Source14: https://registry.npmjs.org/asap/-/asap-2.0.6.tgz
Source15: https://registry.npmjs.org/node-fetch/-/node-fetch-1.7.3.tgz
Source16: https://registry.npmjs.org/is-stream/-/is-stream-1.1.0.tgz
Source17: https://registry.npmjs.org/ua-parser-js/-/ua-parser-js-0.7.17.tgz
Source18: https://registry.npmjs.org/encoding/-/encoding-0.1.12.tgz
Source19: https://registry.npmjs.org/whatwg-fetch/-/whatwg-fetch-2.0.3.tgz
Source20: https://registry.npmjs.org/iconv-lite/-/iconv-lite-0.4.19.tgz
Source21: %{npm_name}-%{version}-registry.npmjs.org.tgz
BuildRequires: nodejs-packaging
BuildRequires: npm(react) >= 15.0.0
BuildRequires: npm(react) < 17.0.0
BuildRequires: npm(redux) >= 2.0.0
BuildRequires: npm(redux) < 4.0.0
Requires: npm(react) >= 15.0.0
Requires: npm(react) < 17.0.0
Requires: npm(redux) >= 2.0.0
Requires: npm(redux) < 4.0.0
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: npm(%{npm_name}) = %{version}
Provides: bundled(npm(promise)) = 7.3.1
Provides: bundled(npm(react-redux)) = 5.0.6
Provides: bundled(npm(invariant)) = 2.2.2
Provides: bundled(npm(lodash)) = 4.17.4
Provides: bundled(npm(hoist-non-react-statics)) = 2.3.1
Provides: bundled(npm(prop-types)) = 15.6.0
Provides: bundled(npm(lodash-es)) = 4.17.4
Provides: bundled(npm(js-tokens)) = 3.0.2
Provides: bundled(npm(object-assign)) = 4.1.1
Provides: bundled(npm(fbjs)) = 0.8.16
Provides: bundled(npm(loose-envify)) = 1.3.1
Provides: bundled(npm(setimmediate)) = 1.0.5
Provides: bundled(npm(isomorphic-fetch)) = 2.2.1
Provides: bundled(npm(core-js)) = 1.2.7
Provides: bundled(npm(asap)) = 2.0.6
Provides: bundled(npm(node-fetch)) = 1.7.3
Provides: bundled(npm(is-stream)) = 1.1.0
Provides: bundled(npm(ua-parser-js)) = 0.7.17
Provides: bundled(npm(encoding)) = 0.1.12
Provides: bundled(npm(whatwg-fetch)) = 2.0.3
Provides: bundled(npm(iconv-lite)) = 0.4.19
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
%setup -T -q -a 21 -D -n %{npm_cache_dir}

%build
mkdir node_modules
ln -s %{nodejs_sitelib}/{react,redux} node_modules/
npm install --cache-min Infinity --cache %{npm_cache_dir} --no-optional --global-style true %{npm_name}@%{version}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cd node_modules/react-redux
cp -pfr CHANGELOG.md LICENSE.md README.md dist es lib package.json src node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pf CHANGELOG.md LICENSE.md README.md ../../

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE.md
%doc CHANGELOG.md
%doc README.md

%changelog
* Fri Nov 17 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 5.0.6-1
- Bump nodejs-react-redux to 5.0.6 (ewoud@kohlvanwijngaarden.nl)

* Thu Feb 16 2017 Dominic Cleal <dominic@cleal.org> 5.0.2-2
- Use existing react, redux peer dependencies (dominic@cleal.org)

* Thu Feb 16 2017 Dominic Cleal <dominic@cleal.org> 5.0.2-1
- new package built with tito

