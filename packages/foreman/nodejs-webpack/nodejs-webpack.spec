%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name webpack

Name: %{?scl_prefix}nodejs-webpack
Version: 5.90.0
Release: 1%{?dist}
Summary: Packs ECMAScript/CommonJs/AMD modules for the browser
License: MIT
Group: Development/Libraries
URL: https://github.com/webpack/webpack
Source0: https://registry.npmjs.org/@jridgewell/gen-mapping/-/gen-mapping-0.3.3.tgz
Source1: https://registry.npmjs.org/@jridgewell/resolve-uri/-/resolve-uri-3.1.1.tgz
Source2: https://registry.npmjs.org/@jridgewell/set-array/-/set-array-1.1.2.tgz
Source3: https://registry.npmjs.org/@jridgewell/source-map/-/source-map-0.3.5.tgz
Source4: https://registry.npmjs.org/@jridgewell/sourcemap-codec/-/sourcemap-codec-1.4.15.tgz
Source5: https://registry.npmjs.org/@jridgewell/trace-mapping/-/trace-mapping-0.3.22.tgz
Source6: https://registry.npmjs.org/@types/eslint/-/eslint-8.56.2.tgz
Source7: https://registry.npmjs.org/@types/eslint-scope/-/eslint-scope-3.7.7.tgz
Source8: https://registry.npmjs.org/@types/estree/-/estree-1.0.5.tgz
Source9: https://registry.npmjs.org/@types/json-schema/-/json-schema-7.0.15.tgz
Source10: https://registry.npmjs.org/@types/node/-/node-20.11.7.tgz
Source11: https://registry.npmjs.org/@webassemblyjs/ast/-/ast-1.11.6.tgz
Source12: https://registry.npmjs.org/@webassemblyjs/floating-point-hex-parser/-/floating-point-hex-parser-1.11.6.tgz
Source13: https://registry.npmjs.org/@webassemblyjs/helper-api-error/-/helper-api-error-1.11.6.tgz
Source14: https://registry.npmjs.org/@webassemblyjs/helper-buffer/-/helper-buffer-1.11.6.tgz
Source15: https://registry.npmjs.org/@webassemblyjs/helper-numbers/-/helper-numbers-1.11.6.tgz
Source16: https://registry.npmjs.org/@webassemblyjs/helper-wasm-bytecode/-/helper-wasm-bytecode-1.11.6.tgz
Source17: https://registry.npmjs.org/@webassemblyjs/helper-wasm-section/-/helper-wasm-section-1.11.6.tgz
Source18: https://registry.npmjs.org/@webassemblyjs/ieee754/-/ieee754-1.11.6.tgz
Source19: https://registry.npmjs.org/@webassemblyjs/leb128/-/leb128-1.11.6.tgz
Source20: https://registry.npmjs.org/@webassemblyjs/utf8/-/utf8-1.11.6.tgz
Source21: https://registry.npmjs.org/@webassemblyjs/wasm-edit/-/wasm-edit-1.11.6.tgz
Source22: https://registry.npmjs.org/@webassemblyjs/wasm-gen/-/wasm-gen-1.11.6.tgz
Source23: https://registry.npmjs.org/@webassemblyjs/wasm-opt/-/wasm-opt-1.11.6.tgz
Source24: https://registry.npmjs.org/@webassemblyjs/wasm-parser/-/wasm-parser-1.11.6.tgz
Source25: https://registry.npmjs.org/@webassemblyjs/wast-printer/-/wast-printer-1.11.6.tgz
Source26: https://registry.npmjs.org/@xtuc/ieee754/-/ieee754-1.2.0.tgz
Source27: https://registry.npmjs.org/@xtuc/long/-/long-4.2.2.tgz
Source28: https://registry.npmjs.org/acorn/-/acorn-8.11.3.tgz
Source29: https://registry.npmjs.org/acorn-import-assertions/-/acorn-import-assertions-1.9.0.tgz
Source30: https://registry.npmjs.org/ajv/-/ajv-6.12.6.tgz
Source31: https://registry.npmjs.org/ajv-keywords/-/ajv-keywords-3.5.2.tgz
Source32: https://registry.npmjs.org/browserslist/-/browserslist-4.22.2.tgz
Source33: https://registry.npmjs.org/buffer-from/-/buffer-from-1.1.2.tgz
Source34: https://registry.npmjs.org/caniuse-lite/-/caniuse-lite-1.0.30001580.tgz
Source35: https://registry.npmjs.org/chrome-trace-event/-/chrome-trace-event-1.0.3.tgz
Source36: https://registry.npmjs.org/commander/-/commander-2.20.3.tgz
Source37: https://registry.npmjs.org/electron-to-chromium/-/electron-to-chromium-1.4.647.tgz
Source38: https://registry.npmjs.org/enhanced-resolve/-/enhanced-resolve-5.15.0.tgz
Source39: https://registry.npmjs.org/es-module-lexer/-/es-module-lexer-1.4.1.tgz
Source40: https://registry.npmjs.org/escalade/-/escalade-3.1.1.tgz
Source41: https://registry.npmjs.org/eslint-scope/-/eslint-scope-5.1.1.tgz
Source42: https://registry.npmjs.org/esrecurse/-/esrecurse-4.3.0.tgz
Source43: https://registry.npmjs.org/estraverse/-/estraverse-4.3.0.tgz
Source44: https://registry.npmjs.org/estraverse/-/estraverse-5.3.0.tgz
Source45: https://registry.npmjs.org/events/-/events-3.3.0.tgz
Source46: https://registry.npmjs.org/fast-deep-equal/-/fast-deep-equal-3.1.3.tgz
Source47: https://registry.npmjs.org/fast-json-stable-stringify/-/fast-json-stable-stringify-2.1.0.tgz
Source48: https://registry.npmjs.org/glob-to-regexp/-/glob-to-regexp-0.4.1.tgz
Source49: https://registry.npmjs.org/graceful-fs/-/graceful-fs-4.2.11.tgz
Source50: https://registry.npmjs.org/has-flag/-/has-flag-4.0.0.tgz
Source51: https://registry.npmjs.org/jest-worker/-/jest-worker-27.5.1.tgz
Source52: https://registry.npmjs.org/json-parse-even-better-errors/-/json-parse-even-better-errors-2.3.1.tgz
Source53: https://registry.npmjs.org/json-schema-traverse/-/json-schema-traverse-0.4.1.tgz
Source54: https://registry.npmjs.org/loader-runner/-/loader-runner-4.3.0.tgz
Source55: https://registry.npmjs.org/merge-stream/-/merge-stream-2.0.0.tgz
Source56: https://registry.npmjs.org/mime-db/-/mime-db-1.52.0.tgz
Source57: https://registry.npmjs.org/mime-types/-/mime-types-2.1.35.tgz
Source58: https://registry.npmjs.org/neo-async/-/neo-async-2.6.2.tgz
Source59: https://registry.npmjs.org/node-releases/-/node-releases-2.0.14.tgz
Source60: https://registry.npmjs.org/picocolors/-/picocolors-1.0.0.tgz
Source61: https://registry.npmjs.org/punycode/-/punycode-2.3.1.tgz
Source62: https://registry.npmjs.org/randombytes/-/randombytes-2.1.0.tgz
Source63: https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.2.1.tgz
Source64: https://registry.npmjs.org/schema-utils/-/schema-utils-3.3.0.tgz
Source65: https://registry.npmjs.org/serialize-javascript/-/serialize-javascript-6.0.2.tgz
Source66: https://registry.npmjs.org/source-map/-/source-map-0.6.1.tgz
Source67: https://registry.npmjs.org/source-map-support/-/source-map-support-0.5.21.tgz
Source68: https://registry.npmjs.org/supports-color/-/supports-color-8.1.1.tgz
Source69: https://registry.npmjs.org/tapable/-/tapable-2.2.1.tgz
Source70: https://registry.npmjs.org/terser/-/terser-5.27.0.tgz
Source71: https://registry.npmjs.org/terser-webpack-plugin/-/terser-webpack-plugin-5.3.10.tgz
Source72: https://registry.npmjs.org/undici-types/-/undici-types-5.26.5.tgz
Source73: https://registry.npmjs.org/update-browserslist-db/-/update-browserslist-db-1.0.13.tgz
Source74: https://registry.npmjs.org/uri-js/-/uri-js-4.4.1.tgz
Source75: https://registry.npmjs.org/watchpack/-/watchpack-2.4.0.tgz
Source76: https://registry.npmjs.org/webpack/-/webpack-5.90.0.tgz
Source77: https://registry.npmjs.org/webpack-sources/-/webpack-sources-3.2.3.tgz
Source78: nodejs-webpack-%{version}-registry.npmjs.org.tgz
BuildRequires: %{?scl_prefix_nodejs}npm
%if 0%{!?scl:1}
BuildRequires: nodejs-packaging
%endif
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}
Provides: bundled(npm(@jridgewell/gen-mapping)) = 0.3.3
Provides: bundled(npm(@jridgewell/resolve-uri)) = 3.1.1
Provides: bundled(npm(@jridgewell/set-array)) = 1.1.2
Provides: bundled(npm(@jridgewell/source-map)) = 0.3.5
Provides: bundled(npm(@jridgewell/sourcemap-codec)) = 1.4.15
Provides: bundled(npm(@jridgewell/trace-mapping)) = 0.3.22
Provides: bundled(npm(@types/eslint)) = 8.56.2
Provides: bundled(npm(@types/eslint-scope)) = 3.7.7
Provides: bundled(npm(@types/estree)) = 1.0.5
Provides: bundled(npm(@types/json-schema)) = 7.0.15
Provides: bundled(npm(@types/node)) = 20.11.7
Provides: bundled(npm(@webassemblyjs/ast)) = 1.11.6
Provides: bundled(npm(@webassemblyjs/floating-point-hex-parser)) = 1.11.6
Provides: bundled(npm(@webassemblyjs/helper-api-error)) = 1.11.6
Provides: bundled(npm(@webassemblyjs/helper-buffer)) = 1.11.6
Provides: bundled(npm(@webassemblyjs/helper-numbers)) = 1.11.6
Provides: bundled(npm(@webassemblyjs/helper-wasm-bytecode)) = 1.11.6
Provides: bundled(npm(@webassemblyjs/helper-wasm-section)) = 1.11.6
Provides: bundled(npm(@webassemblyjs/ieee754)) = 1.11.6
Provides: bundled(npm(@webassemblyjs/leb128)) = 1.11.6
Provides: bundled(npm(@webassemblyjs/utf8)) = 1.11.6
Provides: bundled(npm(@webassemblyjs/wasm-edit)) = 1.11.6
Provides: bundled(npm(@webassemblyjs/wasm-gen)) = 1.11.6
Provides: bundled(npm(@webassemblyjs/wasm-opt)) = 1.11.6
Provides: bundled(npm(@webassemblyjs/wasm-parser)) = 1.11.6
Provides: bundled(npm(@webassemblyjs/wast-printer)) = 1.11.6
Provides: bundled(npm(@xtuc/ieee754)) = 1.2.0
Provides: bundled(npm(@xtuc/long)) = 4.2.2
Provides: bundled(npm(acorn)) = 8.11.3
Provides: bundled(npm(acorn-import-assertions)) = 1.9.0
Provides: bundled(npm(ajv)) = 6.12.6
Provides: bundled(npm(ajv-keywords)) = 3.5.2
Provides: bundled(npm(browserslist)) = 4.22.2
Provides: bundled(npm(buffer-from)) = 1.1.2
Provides: bundled(npm(caniuse-lite)) = 1.0.30001580
Provides: bundled(npm(chrome-trace-event)) = 1.0.3
Provides: bundled(npm(commander)) = 2.20.3
Provides: bundled(npm(electron-to-chromium)) = 1.4.647
Provides: bundled(npm(enhanced-resolve)) = 5.15.0
Provides: bundled(npm(es-module-lexer)) = 1.4.1
Provides: bundled(npm(escalade)) = 3.1.1
Provides: bundled(npm(eslint-scope)) = 5.1.1
Provides: bundled(npm(esrecurse)) = 4.3.0
Provides: bundled(npm(estraverse)) = 4.3.0
Provides: bundled(npm(estraverse)) = 5.3.0
Provides: bundled(npm(events)) = 3.3.0
Provides: bundled(npm(fast-deep-equal)) = 3.1.3
Provides: bundled(npm(fast-json-stable-stringify)) = 2.1.0
Provides: bundled(npm(glob-to-regexp)) = 0.4.1
Provides: bundled(npm(graceful-fs)) = 4.2.11
Provides: bundled(npm(has-flag)) = 4.0.0
Provides: bundled(npm(jest-worker)) = 27.5.1
Provides: bundled(npm(json-parse-even-better-errors)) = 2.3.1
Provides: bundled(npm(json-schema-traverse)) = 0.4.1
Provides: bundled(npm(loader-runner)) = 4.3.0
Provides: bundled(npm(merge-stream)) = 2.0.0
Provides: bundled(npm(mime-db)) = 1.52.0
Provides: bundled(npm(mime-types)) = 2.1.35
Provides: bundled(npm(neo-async)) = 2.6.2
Provides: bundled(npm(node-releases)) = 2.0.14
Provides: bundled(npm(picocolors)) = 1.0.0
Provides: bundled(npm(punycode)) = 2.3.1
Provides: bundled(npm(randombytes)) = 2.1.0
Provides: bundled(npm(safe-buffer)) = 5.2.1
Provides: bundled(npm(schema-utils)) = 3.3.0
Provides: bundled(npm(serialize-javascript)) = 6.0.2
Provides: bundled(npm(source-map)) = 0.6.1
Provides: bundled(npm(source-map-support)) = 0.5.21
Provides: bundled(npm(supports-color)) = 8.1.1
Provides: bundled(npm(tapable)) = 2.2.1
Provides: bundled(npm(terser)) = 5.27.0
Provides: bundled(npm(terser-webpack-plugin)) = 5.3.10
Provides: bundled(npm(undici-types)) = 5.26.5
Provides: bundled(npm(update-browserslist-db)) = 1.0.13
Provides: bundled(npm(uri-js)) = 4.4.1
Provides: bundled(npm(watchpack)) = 2.4.0
Provides: bundled(npm(webpack)) = 5.90.0
Provides: bundled(npm(webpack-sources)) = 3.2.3
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

%setup -T -q -a 78 -D -n %{npm_cache_dir}

%build
%{?scl:scl enable %{?scl_nodejs} - << \end_of_scl}
npm install --cache-min Infinity --cache %{?scl:../}%{npm_cache_dir} --no-shrinkwrap --no-optional --global-style true %{npm_name}@%{version}
%{?scl:end_of_scl}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/bin %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/hot %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/lib %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/module.d.ts %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/schemas %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/types.d.ts %{buildroot}%{nodejs_sitelib}/%{npm_name}

mkdir -p %{buildroot}%{_bindir}/
chmod 0755 %{buildroot}%{nodejs_sitelib}/%{npm_name}/bin/webpack.js
ln -sf %{nodejs_sitelib}/%{npm_name}/bin/webpack.js %{buildroot}%{_bindir}/webpack

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%{_bindir}/webpack
%license node_modules/%{npm_name}/LICENSE
%doc node_modules/%{npm_name}/README.md
%doc node_modules/%{npm_name}/SECURITY.md

%changelog
* Fri Jan 26 2024 Foreman Packaging Automation <packaging@theforeman.org> 5.90.0-1
- Update to 5.90.0

* Fri Jan 26 2024 Evgeni Golov 5.75.0-1
- Update to 5.75.0

* Fri Jan 12 2024 Eric D. Helms <ericdhelms@gmail.com> - 3.12.0-6
- Update bundle dependencies

* Fri Oct 06 2023 Eric D. Helms <ericdhelms@gmail.com> - 3.12.0-5
- Bump dependencies

* Tue Mar 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.12.0-4
- Bump packages to build for el8

* Tue Oct 22 2019 Eric D. Helms <ericdhelms@gmail.com> - 3.12.0-3
- Build for SCL

* Fri Oct 04 2019 Eric D. Helms <ericdhelms@gmail.com> - 3.12.0-2
- Update specs to handle SCL

* Wed Jun 06 2018 Eric D. Helms <ericdhelms@gmail.com> 3.12.0-1
- Update to 3.12.0

* Wed Nov 22 2017 Daniel Lobato Garcia <me@daniellobato.me> 3.4.1-3
- Install webpack binary without the .js extension
  (github@kohlvanwijngaarden.nl)

* Sat Oct 14 2017 Eric D. Helms <ericdhelms@gmail.com> 3.4.1-2
- Bump release to rebuild

* Mon Aug 07 2017 Eric D. Helms <ericdhelms@gmail.com> 3.4.1-1
- Update nodejs-weebpack to 3.4.1 (me@daniellobato.me)

* Sat Jul 15 2017 Eric D. Helms <ericdhelms@gmail.com> 3.0.0-2
- Add back missing Provides: npm (ericdhelms@gmail.com)

* Wed Jul 12 2017 Eric D. Helms <ericdhelms@gmail.com> 3.0.0-1
- update webpack to v3.0 (ohadlevy@gmail.com)
