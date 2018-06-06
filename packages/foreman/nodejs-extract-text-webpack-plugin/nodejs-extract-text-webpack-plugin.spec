%global npm_name extract-text-webpack-plugin

Name: nodejs-%{npm_name}
Version: 3.0.2
Release: 1%{?dist}
Summary: Extract text from bundle into a file
License: MIT
Group: Development/Libraries
URL: http://github.com/webpack-contrib/extract-text-webpack-plugin
Source0: https://registry.npmjs.org/extract-text-webpack-plugin/-/extract-text-webpack-plugin-3.0.2.tgz
Source1: https://registry.npmjs.org/webpack-sources/-/webpack-sources-1.1.0.tgz
Source2: https://registry.npmjs.org/loader-utils/-/loader-utils-1.1.0.tgz
Source3: https://registry.npmjs.org/async/-/async-2.6.1.tgz
Source4: https://registry.npmjs.org/schema-utils/-/schema-utils-0.3.0.tgz
Source5: https://registry.npmjs.org/big.js/-/big.js-3.2.0.tgz
Source6: https://registry.npmjs.org/source-list-map/-/source-list-map-2.0.0.tgz
Source7: https://registry.npmjs.org/emojis-list/-/emojis-list-2.1.0.tgz
Source8: https://registry.npmjs.org/json5/-/json5-0.5.1.tgz
Source9: https://registry.npmjs.org/source-map/-/source-map-0.6.1.tgz
Source10: https://registry.npmjs.org/lodash/-/lodash-4.17.10.tgz
Source11: https://registry.npmjs.org/ajv/-/ajv-5.5.2.tgz
Source12: https://registry.npmjs.org/fast-json-stable-stringify/-/fast-json-stable-stringify-2.0.0.tgz
Source13: https://registry.npmjs.org/fast-deep-equal/-/fast-deep-equal-1.1.0.tgz
Source14: https://registry.npmjs.org/co/-/co-4.6.0.tgz
Source15: https://registry.npmjs.org/json-schema-traverse/-/json-schema-traverse-0.3.1.tgz
Source16: %{npm_name}-%{version}-registry.npmjs.org.tgz
BuildRequires: nodejs-packaging
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: npm(%{npm_name}) = %{version}
Provides: bundled(npm(ajv)) = 5.5.2
Provides: bundled(npm(async)) = 2.6.1
Provides: bundled(npm(big.js)) = 3.2.0
Provides: bundled(npm(co)) = 4.6.0
Provides: bundled(npm(emojis-list)) = 2.1.0
Provides: bundled(npm(extract-text-webpack-plugin)) = 3.0.2
Provides: bundled(npm(fast-deep-equal)) = 1.1.0
Provides: bundled(npm(fast-json-stable-stringify)) = 2.0.0
Provides: bundled(npm(json-schema-traverse)) = 0.3.1
Provides: bundled(npm(json5)) = 0.5.1
Provides: bundled(npm(loader-utils)) = 1.1.0
Provides: bundled(npm(lodash)) = 4.17.10
Provides: bundled(npm(schema-utils)) = 0.3.0
Provides: bundled(npm(source-list-map)) = 2.0.0
Provides: bundled(npm(source-map)) = 0.6.1
Provides: bundled(npm(webpack-sources)) = 1.1.0
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
%setup -T -q -a 16 -D -n %{npm_cache_dir}

%build
npm install --cache-min Infinity --cache %{npm_cache_dir} --no-shrinkwrap --no-optional --global-style true %{npm_name}@%{version}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/dist %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/schema %{buildroot}%{nodejs_sitelib}/%{npm_name}

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%license node_modules/%{npm_name}/LICENSE
%doc node_modules/%{npm_name}/CHANGELOG.md
%doc node_modules/%{npm_name}/README.md

%changelog
* Wed Jun 06 2018 Eric D. Helms <ericdhelms@gmail.com> 3.0.2-1
- Update to 3.0.2

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
