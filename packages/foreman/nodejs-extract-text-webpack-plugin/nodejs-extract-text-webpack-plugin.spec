%global npm_name extract-text-webpack-plugin

%{?nodejs_find_provides_and_requires}

Name: nodejs-%{npm_name}
Version: 3.0.0
Release: 1%{?dist}
Summary: Extract text from bundle into a file
License: MIT
URL: https://github.com/webpack-contrib/extract-text-webpack-plugin
Source0: http://registry.npmjs.org/extract-text-webpack-plugin/-/extract-text-webpack-plugin-3.0.0.tgz
Source1: http://registry.npmjs.org/schema-utils/-/schema-utils-0.3.0.tgz
Source2: http://registry.npmjs.org/webpack-sources/-/webpack-sources-1.0.1.tgz
Source3: http://registry.npmjs.org/loader-utils/-/loader-utils-1.1.0.tgz
Source4: http://registry.npmjs.org/async/-/async-2.5.0.tgz
Source5: http://registry.npmjs.org/emojis-list/-/emojis-list-2.1.0.tgz
Source6: http://registry.npmjs.org/source-list-map/-/source-list-map-2.0.0.tgz
Source7: http://registry.npmjs.org/big.js/-/big.js-3.1.3.tgz
Source8: http://registry.npmjs.org/json5/-/json5-0.5.1.tgz
Source9: http://registry.npmjs.org/source-map/-/source-map-0.5.6.tgz
Source10: http://registry.npmjs.org/ajv/-/ajv-5.2.2.tgz
Source11: http://registry.npmjs.org/lodash/-/lodash-4.17.4.tgz
Source12: http://registry.npmjs.org/json-schema-traverse/-/json-schema-traverse-0.3.1.tgz
Source13: http://registry.npmjs.org/fast-deep-equal/-/fast-deep-equal-1.0.0.tgz
Source14: http://registry.npmjs.org/json-stable-stringify/-/json-stable-stringify-1.0.1.tgz
Source15: http://registry.npmjs.org/co/-/co-4.6.0.tgz
Source16: http://registry.npmjs.org/jsonify/-/jsonify-0.0.0.tgz
Source17: extract-text-webpack-plugin-3.0.0-registry.npmjs.org.tgz
BuildRequires: nodejs-packaging
BuildRequires: npm
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch
Provides: npm(%{npm_name}) = %{version}
Provides: bundled-npm(extract-text-webpack-plugin) = 3.0.0
Provides: bundled-npm(schema-utils) = 0.3.0
Provides: bundled-npm(webpack-sources) = 1.0.1
Provides: bundled-npm(loader-utils) = 1.1.0
Provides: bundled-npm(async) = 2.5.0
Provides: bundled-npm(emojis-list) = 2.1.0
Provides: bundled-npm(source-list-map) = 2.0.0
Provides: bundled-npm(big.js) = 3.1.3
Provides: bundled-npm(json5) = 0.5.1
Provides: bundled-npm(source-map) = 0.5.6
Provides: bundled-npm(ajv) = 5.2.2
Provides: bundled-npm(lodash) = 4.17.4
Provides: bundled-npm(json-schema-traverse) = 0.3.1
Provides: bundled-npm(fast-deep-equal) = 1.0.0
Provides: bundled-npm(json-stable-stringify) = 1.0.1
Provides: bundled-npm(co) = 4.6.0
Provides: bundled-npm(jsonify) = 0.0.0
AutoReq: no
AutoProv: no


%description
%{summary}

%prep
mkdir -p npm_cache
for tgz in %{sources}; do
  echo $tgz | grep -q registry.npmjs.org || npm cache add --cache ./npm_cache $tgz
done

%setup -T -q -a 17 -D -n npm_cache

%build
npm install --cache-min Infinity --cache . --no-optional --global-style true %{npm_name}@%{version}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cd node_modules/extract-text-webpack-plugin
cp -pfr CHANGELOG.md LICENSE README.md dist package.json schema node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pf CHANGELOG.md README.md LICENSE ../../
# If any binaries are included, symlink them to bindir here

%files
%{nodejs_sitelib}/%{npm_name}
%doc LICENSE
%doc CHANGELOG.md
%doc README.md

%changelog
* Wed Jul 26 2017 Eric D. Helms <ericdhelms@gmail.com> 3.0.0-1
- Update nodejs-extract-text-webpack to 3.0 (me@daniellobato.me)

* Sat Jul 15 2017 Eric D. Helms <ericdhelms@gmail.com> 2.1.2-2
- Add back missing Provides: npm (ericdhelms@gmail.com)

* Sat Jul 15 2017 Eric D. Helms <ericdhelms@gmail.com> 2.1.2-1
- update webpack to v3.0 (ohadlevy@gmail.com)

* Sat Jul 15 2017 Eric D. Helms <ericdhelms@gmail.com>
- update webpack to v3.0 (ohadlevy@gmail.com)

* Sat Jul 15 2017 Eric D. Helms <ericdhelms@gmail.com>
- update webpack to v3.0 (ohadlevy@gmail.com)
