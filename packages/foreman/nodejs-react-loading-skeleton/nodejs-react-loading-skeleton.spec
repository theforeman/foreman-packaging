%global npm_name react-loading-skeleton

Name: nodejs-react-loading-skeleton
Version: 1.1.2
Release: 1%{?dist}
Summary: FIXME
License: MIT
Group: Development/Libraries
URL: https://github.com/dvtng/react-loading-skeleton#readme
Source0: https://registry.npmjs.org/react-loading-skeleton/-/react-loading-skeleton-1.1.2.tgz
Source1: https://registry.npmjs.org/emotion/-/emotion-9.2.12.tgz
Source2: https://registry.npmjs.org/create-emotion/-/create-emotion-9.2.12.tgz
Source3: https://registry.npmjs.org/stylis-rule-sheet/-/stylis-rule-sheet-0.0.10.tgz
Source4: https://registry.npmjs.org/stylis/-/stylis-3.5.4.tgz
Source5: https://registry.npmjs.org/babel-plugin-emotion/-/babel-plugin-emotion-9.2.11.tgz
Source6: https://registry.npmjs.org/@babel/helper-module-imports/-/@babel/helper-module-imports-7.0.0.tgz
Source7: https://registry.npmjs.org/@emotion/stylis/-/@emotion/stylis-0.7.1.tgz
Source8: https://registry.npmjs.org/csstype/-/csstype-2.6.5.tgz
Source9: https://registry.npmjs.org/@emotion/unitless/-/@emotion/unitless-0.6.7.tgz
Source10: https://registry.npmjs.org/@emotion/memoize/-/@emotion/memoize-0.6.6.tgz
Source11: https://registry.npmjs.org/convert-source-map/-/convert-source-map-1.6.0.tgz
Source12: https://registry.npmjs.org/babel-plugin-syntax-jsx/-/babel-plugin-syntax-jsx-6.18.0.tgz
Source13: https://registry.npmjs.org/find-root/-/find-root-1.1.0.tgz
Source14: https://registry.npmjs.org/mkdirp/-/mkdirp-0.5.1.tgz
Source15: https://registry.npmjs.org/@emotion/hash/-/@emotion/hash-0.6.6.tgz
Source16: https://registry.npmjs.org/touch/-/touch-2.0.2.tgz
Source17: https://registry.npmjs.org/source-map/-/source-map-0.5.7.tgz
Source18: https://registry.npmjs.org/@babel/types/-/@babel/types-7.5.0.tgz
Source19: https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.1.2.tgz
Source20: https://registry.npmjs.org/minimist/-/minimist-0.0.8.tgz
Source21: https://registry.npmjs.org/nopt/-/nopt-1.0.10.tgz
Source22: https://registry.npmjs.org/to-fast-properties/-/to-fast-properties-2.0.0.tgz
Source23: https://registry.npmjs.org/abbrev/-/abbrev-1.1.1.tgz
Source24: https://registry.npmjs.org/esutils/-/esutils-2.0.2.tgz
Source25: https://registry.npmjs.org/lodash/-/lodash-4.17.11.tgz
Source26: https://registry.npmjs.org/babel-plugin-macros/-/babel-plugin-macros-2.6.1.tgz
Source27: https://registry.npmjs.org/resolve/-/resolve-1.11.1.tgz
Source28: https://registry.npmjs.org/cosmiconfig/-/cosmiconfig-5.2.1.tgz
Source29: https://registry.npmjs.org/@emotion/babel-utils/-/@emotion/babel-utils-0.6.10.tgz
Source30: https://registry.npmjs.org/path-parse/-/path-parse-1.0.6.tgz
Source31: https://registry.npmjs.org/is-directory/-/is-directory-0.3.1.tgz
Source32: https://registry.npmjs.org/parse-json/-/parse-json-4.0.0.tgz
Source33: https://registry.npmjs.org/js-yaml/-/js-yaml-3.13.1.tgz
Source34: https://registry.npmjs.org/import-fresh/-/import-fresh-2.0.0.tgz
Source35: https://registry.npmjs.org/error-ex/-/error-ex-1.3.2.tgz
Source36: https://registry.npmjs.org/json-parse-better-errors/-/json-parse-better-errors-1.0.2.tgz
Source37: https://registry.npmjs.org/esprima/-/esprima-4.0.1.tgz
Source38: https://registry.npmjs.org/caller-path/-/caller-path-2.0.0.tgz
Source39: https://registry.npmjs.org/resolve-from/-/resolve-from-3.0.0.tgz
Source40: https://registry.npmjs.org/argparse/-/argparse-1.0.10.tgz
Source41: https://registry.npmjs.org/source-map/-/source-map-0.7.3.tgz
Source42: https://registry.npmjs.org/is-arrayish/-/is-arrayish-0.2.1.tgz
Source43: https://registry.npmjs.org/caller-callsite/-/caller-callsite-2.0.0.tgz
Source44: https://registry.npmjs.org/sprintf-js/-/sprintf-js-1.0.3.tgz
Source45: https://registry.npmjs.org/@emotion/serialize/-/@emotion/serialize-0.9.1.tgz
Source46: https://registry.npmjs.org/callsites/-/callsites-2.0.0.tgz
Source47: https://registry.npmjs.org/@emotion/utils/-/@emotion/utils-0.8.2.tgz
Source48: https://registry.npmjs.org/@babel/runtime/-/@babel/runtime-7.5.1.tgz
Source49: https://registry.npmjs.org/regenerator-runtime/-/regenerator-runtime-0.13.2.tgz
Source50: %{name}-%{version}-registry.npmjs.org.tgz
BuildRequires: nodejs-packaging
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: npm(%{npm_name}) = %{version}
Provides: bundled(npm(@babel/helper-module-imports)) = 7.0.0
Provides: bundled(npm(@babel/runtime)) = 7.5.1
Provides: bundled(npm(@babel/types)) = 7.5.0
Provides: bundled(npm(@emotion/babel-utils)) = 0.6.10
Provides: bundled(npm(@emotion/hash)) = 0.6.6
Provides: bundled(npm(@emotion/memoize)) = 0.6.6
Provides: bundled(npm(@emotion/serialize)) = 0.9.1
Provides: bundled(npm(@emotion/stylis)) = 0.7.1
Provides: bundled(npm(@emotion/unitless)) = 0.6.7
Provides: bundled(npm(@emotion/utils)) = 0.8.2
Provides: bundled(npm(abbrev)) = 1.1.1
Provides: bundled(npm(argparse)) = 1.0.10
Provides: bundled(npm(babel-plugin-emotion)) = 9.2.11
Provides: bundled(npm(babel-plugin-macros)) = 2.6.1
Provides: bundled(npm(babel-plugin-syntax-jsx)) = 6.18.0
Provides: bundled(npm(caller-callsite)) = 2.0.0
Provides: bundled(npm(caller-path)) = 2.0.0
Provides: bundled(npm(callsites)) = 2.0.0
Provides: bundled(npm(convert-source-map)) = 1.6.0
Provides: bundled(npm(cosmiconfig)) = 5.2.1
Provides: bundled(npm(create-emotion)) = 9.2.12
Provides: bundled(npm(csstype)) = 2.6.5
Provides: bundled(npm(emotion)) = 9.2.12
Provides: bundled(npm(error-ex)) = 1.3.2
Provides: bundled(npm(esprima)) = 4.0.1
Provides: bundled(npm(esutils)) = 2.0.2
Provides: bundled(npm(find-root)) = 1.1.0
Provides: bundled(npm(import-fresh)) = 2.0.0
Provides: bundled(npm(is-arrayish)) = 0.2.1
Provides: bundled(npm(is-directory)) = 0.3.1
Provides: bundled(npm(js-yaml)) = 3.13.1
Provides: bundled(npm(json-parse-better-errors)) = 1.0.2
Provides: bundled(npm(lodash)) = 4.17.11
Provides: bundled(npm(minimist)) = 0.0.8
Provides: bundled(npm(mkdirp)) = 0.5.1
Provides: bundled(npm(nopt)) = 1.0.10
Provides: bundled(npm(parse-json)) = 4.0.0
Provides: bundled(npm(path-parse)) = 1.0.6
Provides: bundled(npm(react-loading-skeleton)) = 1.1.2
Provides: bundled(npm(regenerator-runtime)) = 0.13.2
Provides: bundled(npm(resolve)) = 1.11.1
Provides: bundled(npm(resolve-from)) = 3.0.0
Provides: bundled(npm(safe-buffer)) = 5.1.2
Provides: bundled(npm(source-map)) = 0.7.3
Provides: bundled(npm(source-map)) = 0.5.7
Provides: bundled(npm(sprintf-js)) = 1.0.3
Provides: bundled(npm(stylis)) = 3.5.4
Provides: bundled(npm(stylis-rule-sheet)) = 0.0.10
Provides: bundled(npm(to-fast-properties)) = 2.0.0
Provides: bundled(npm(touch)) = 2.0.2
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
%setup -T -q -a 50 -D -n %{npm_cache_dir}

%build
npm install --cache-min Infinity --cache %{npm_cache_dir} --no-shrinkwrap --no-optional --global-style true %{npm_name}@%{version}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/dist %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%license node_modules/%{npm_name}/LICENSE.md
%doc node_modules/%{npm_name}/README.md

%changelog
* Sun Jul 07 2019 Gilad Lekner <glekner@redhat.com> 1.1.2-1
- Add nodejs-react-loading-skeleton generated by npm2rpm using the bundle strategy

