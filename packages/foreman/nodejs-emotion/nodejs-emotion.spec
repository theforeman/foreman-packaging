%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name emotion

Name: %{?scl_prefix}nodejs-emotion
Version: 10.0.27
Release: 1%{?dist}
Summary: The Next Generation of CSS-in-JS
License: MIT
Group: Development/Libraries
URL: https://emotion.sh
Source0: https://registry.npmjs.org/@babel/code-frame/-/code-frame-7.27.1.tgz
Source1: https://registry.npmjs.org/@babel/generator/-/generator-7.28.0.tgz
Source2: https://registry.npmjs.org/@babel/helper-globals/-/helper-globals-7.28.0.tgz
Source3: https://registry.npmjs.org/@babel/helper-module-imports/-/helper-module-imports-7.27.1.tgz
Source4: https://registry.npmjs.org/@babel/helper-string-parser/-/helper-string-parser-7.27.1.tgz
Source5: https://registry.npmjs.org/@babel/helper-validator-identifier/-/helper-validator-identifier-7.27.1.tgz
Source6: https://registry.npmjs.org/@babel/parser/-/parser-7.28.0.tgz
Source7: https://registry.npmjs.org/@babel/runtime/-/runtime-7.27.6.tgz
Source8: https://registry.npmjs.org/@babel/template/-/template-7.27.2.tgz
Source9: https://registry.npmjs.org/@babel/traverse/-/traverse-7.28.0.tgz
Source10: https://registry.npmjs.org/@babel/types/-/types-7.28.0.tgz
Source11: https://registry.npmjs.org/@emotion/cache/-/cache-10.0.29.tgz
Source12: https://registry.npmjs.org/@emotion/hash/-/hash-0.8.0.tgz
Source13: https://registry.npmjs.org/@emotion/memoize/-/memoize-0.7.4.tgz
Source14: https://registry.npmjs.org/@emotion/serialize/-/serialize-0.11.16.tgz
Source15: https://registry.npmjs.org/@emotion/sheet/-/sheet-0.9.4.tgz
Source16: https://registry.npmjs.org/@emotion/stylis/-/stylis-0.8.5.tgz
Source17: https://registry.npmjs.org/@emotion/unitless/-/unitless-0.7.5.tgz
Source18: https://registry.npmjs.org/@emotion/utils/-/utils-0.11.3.tgz
Source19: https://registry.npmjs.org/@emotion/weak-memoize/-/weak-memoize-0.2.5.tgz
Source20: https://registry.npmjs.org/@jridgewell/gen-mapping/-/gen-mapping-0.3.12.tgz
Source21: https://registry.npmjs.org/@jridgewell/resolve-uri/-/resolve-uri-3.1.2.tgz
Source22: https://registry.npmjs.org/@jridgewell/sourcemap-codec/-/sourcemap-codec-1.5.4.tgz
Source23: https://registry.npmjs.org/@jridgewell/trace-mapping/-/trace-mapping-0.3.29.tgz
Source24: https://registry.npmjs.org/@types/parse-json/-/parse-json-4.0.2.tgz
Source25: https://registry.npmjs.org/babel-plugin-emotion/-/babel-plugin-emotion-10.2.2.tgz
Source26: https://registry.npmjs.org/babel-plugin-macros/-/babel-plugin-macros-2.8.0.tgz
Source27: https://registry.npmjs.org/babel-plugin-syntax-jsx/-/babel-plugin-syntax-jsx-6.18.0.tgz
Source28: https://registry.npmjs.org/callsites/-/callsites-3.1.0.tgz
Source29: https://registry.npmjs.org/convert-source-map/-/convert-source-map-1.9.0.tgz
Source30: https://registry.npmjs.org/cosmiconfig/-/cosmiconfig-6.0.0.tgz
Source31: https://registry.npmjs.org/create-emotion/-/create-emotion-10.0.27.tgz
Source32: https://registry.npmjs.org/csstype/-/csstype-2.6.21.tgz
Source33: https://registry.npmjs.org/debug/-/debug-4.4.1.tgz
Source34: https://registry.npmjs.org/emotion/-/emotion-10.0.27.tgz
Source35: https://registry.npmjs.org/error-ex/-/error-ex-1.3.2.tgz
Source36: https://registry.npmjs.org/escape-string-regexp/-/escape-string-regexp-1.0.5.tgz
Source37: https://registry.npmjs.org/find-root/-/find-root-1.1.0.tgz
Source38: https://registry.npmjs.org/function-bind/-/function-bind-1.1.2.tgz
Source39: https://registry.npmjs.org/hasown/-/hasown-2.0.2.tgz
Source40: https://registry.npmjs.org/import-fresh/-/import-fresh-3.3.1.tgz
Source41: https://registry.npmjs.org/is-arrayish/-/is-arrayish-0.2.1.tgz
Source42: https://registry.npmjs.org/is-core-module/-/is-core-module-2.16.1.tgz
Source43: https://registry.npmjs.org/js-tokens/-/js-tokens-4.0.0.tgz
Source44: https://registry.npmjs.org/jsesc/-/jsesc-3.1.0.tgz
Source45: https://registry.npmjs.org/json-parse-even-better-errors/-/json-parse-even-better-errors-2.3.1.tgz
Source46: https://registry.npmjs.org/lines-and-columns/-/lines-and-columns-1.2.4.tgz
Source47: https://registry.npmjs.org/ms/-/ms-2.1.3.tgz
Source48: https://registry.npmjs.org/parent-module/-/parent-module-1.0.1.tgz
Source49: https://registry.npmjs.org/parse-json/-/parse-json-5.2.0.tgz
Source50: https://registry.npmjs.org/path-parse/-/path-parse-1.0.7.tgz
Source51: https://registry.npmjs.org/path-type/-/path-type-4.0.0.tgz
Source52: https://registry.npmjs.org/picocolors/-/picocolors-1.1.1.tgz
Source53: https://registry.npmjs.org/resolve/-/resolve-1.22.10.tgz
Source54: https://registry.npmjs.org/resolve-from/-/resolve-from-4.0.0.tgz
Source55: https://registry.npmjs.org/source-map/-/source-map-0.5.7.tgz
Source56: https://registry.npmjs.org/supports-preserve-symlinks-flag/-/supports-preserve-symlinks-flag-1.0.0.tgz
Source57: https://registry.npmjs.org/yaml/-/yaml-1.10.2.tgz
Source58: nodejs-emotion-%{version}-registry.npmjs.org.tgz
BuildRequires: %{?scl_prefix_nodejs}npm
%if 0%{!?scl:1}
BuildRequires: nodejs-packaging
%endif
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}
Provides: bundled(npm(@babel/code-frame)) = 7.27.1
Provides: bundled(npm(@babel/generator)) = 7.28.0
Provides: bundled(npm(@babel/helper-globals)) = 7.28.0
Provides: bundled(npm(@babel/helper-module-imports)) = 7.27.1
Provides: bundled(npm(@babel/helper-string-parser)) = 7.27.1
Provides: bundled(npm(@babel/helper-validator-identifier)) = 7.27.1
Provides: bundled(npm(@babel/parser)) = 7.28.0
Provides: bundled(npm(@babel/runtime)) = 7.27.6
Provides: bundled(npm(@babel/template)) = 7.27.2
Provides: bundled(npm(@babel/traverse)) = 7.28.0
Provides: bundled(npm(@babel/types)) = 7.28.0
Provides: bundled(npm(@emotion/cache)) = 10.0.29
Provides: bundled(npm(@emotion/hash)) = 0.8.0
Provides: bundled(npm(@emotion/memoize)) = 0.7.4
Provides: bundled(npm(@emotion/serialize)) = 0.11.16
Provides: bundled(npm(@emotion/sheet)) = 0.9.4
Provides: bundled(npm(@emotion/stylis)) = 0.8.5
Provides: bundled(npm(@emotion/unitless)) = 0.7.5
Provides: bundled(npm(@emotion/utils)) = 0.11.3
Provides: bundled(npm(@emotion/weak-memoize)) = 0.2.5
Provides: bundled(npm(@jridgewell/gen-mapping)) = 0.3.12
Provides: bundled(npm(@jridgewell/resolve-uri)) = 3.1.2
Provides: bundled(npm(@jridgewell/sourcemap-codec)) = 1.5.4
Provides: bundled(npm(@jridgewell/trace-mapping)) = 0.3.29
Provides: bundled(npm(@types/parse-json)) = 4.0.2
Provides: bundled(npm(babel-plugin-emotion)) = 10.2.2
Provides: bundled(npm(babel-plugin-macros)) = 2.8.0
Provides: bundled(npm(babel-plugin-syntax-jsx)) = 6.18.0
Provides: bundled(npm(callsites)) = 3.1.0
Provides: bundled(npm(convert-source-map)) = 1.9.0
Provides: bundled(npm(cosmiconfig)) = 6.0.0
Provides: bundled(npm(create-emotion)) = 10.0.27
Provides: bundled(npm(csstype)) = 2.6.21
Provides: bundled(npm(debug)) = 4.4.1
Provides: bundled(npm(emotion)) = 10.0.27
Provides: bundled(npm(error-ex)) = 1.3.2
Provides: bundled(npm(escape-string-regexp)) = 1.0.5
Provides: bundled(npm(find-root)) = 1.1.0
Provides: bundled(npm(function-bind)) = 1.1.2
Provides: bundled(npm(hasown)) = 2.0.2
Provides: bundled(npm(import-fresh)) = 3.3.1
Provides: bundled(npm(is-arrayish)) = 0.2.1
Provides: bundled(npm(is-core-module)) = 2.16.1
Provides: bundled(npm(js-tokens)) = 4.0.0
Provides: bundled(npm(jsesc)) = 3.1.0
Provides: bundled(npm(json-parse-even-better-errors)) = 2.3.1
Provides: bundled(npm(lines-and-columns)) = 1.2.4
Provides: bundled(npm(ms)) = 2.1.3
Provides: bundled(npm(parent-module)) = 1.0.1
Provides: bundled(npm(parse-json)) = 5.2.0
Provides: bundled(npm(path-parse)) = 1.0.7
Provides: bundled(npm(path-type)) = 4.0.0
Provides: bundled(npm(picocolors)) = 1.1.1
Provides: bundled(npm(resolve)) = 1.22.10
Provides: bundled(npm(resolve-from)) = 4.0.0
Provides: bundled(npm(source-map)) = 0.5.7
Provides: bundled(npm(supports-preserve-symlinks-flag)) = 1.0.0
Provides: bundled(npm(yaml)) = 1.10.2
AutoReq: no
AutoProv: no

%if 0%{?scl:1}
%define npm_cache_dir npm_cache
%else
%define npm_cache_dir /tmp/npm_cache_%{name}-%{version}-%{release}
%endif

%description
%{summary}

%prep
mkdir -p %{npm_cache_dir}
%{?scl:scl enable %{?scl_nodejs} - << \end_of_scl}
for tgz in %{sources}; do
  echo $tgz | grep -q registry.npmjs.org || npm cache add --cache %{npm_cache_dir} $tgz
done
%{?scl:end_of_scl}

%setup -T -q -a 58 -D -n %{npm_cache_dir}

%build
%{?scl:scl enable %{?scl_nodejs} - << \end_of_scl}
npm install --legacy-peer-deps --cache-min Infinity --cache %{?scl:../}%{npm_cache_dir} --no-shrinkwrap --no-optional --global-style true %{npm_name}@%{version}
%{?scl:end_of_scl}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/dist %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/macro.d.ts %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/macro.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/macro.js.flow %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/src %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/types %{buildroot}%{nodejs_sitelib}/%{npm_name}

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%license node_modules/%{npm_name}/LICENSE
%doc node_modules/%{npm_name}/CHANGELOG.md
%doc node_modules/%{npm_name}/README.md

%changelog
* Wed Jul 09 2025 Foreman Packaging Automation <packaging@theforeman.org> 10.0.27-1
- Update to 10.0.27

* Thu Jul 03 2025 root <root> 9.2.12-1
- Add nodejs-emotion generated by npm2rpm using the bundle strategy

