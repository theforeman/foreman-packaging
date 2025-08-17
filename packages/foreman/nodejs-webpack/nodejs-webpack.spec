%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name webpack

Name: %{?scl_prefix}nodejs-webpack
Version: 5.101.2
Release: 1%{?dist}
Summary: Packs ECMAScript/CommonJs/AMD modules for the browser
License: MIT
Group: Development/Libraries
URL: https://github.com/webpack/webpack
Source0: https://registry.npmjs.org/@jridgewell/gen-mapping/-/gen-mapping-0.3.13.tgz
Source1: https://registry.npmjs.org/@jridgewell/resolve-uri/-/resolve-uri-3.1.2.tgz
Source2: https://registry.npmjs.org/@jridgewell/source-map/-/source-map-0.3.11.tgz
Source3: https://registry.npmjs.org/@jridgewell/sourcemap-codec/-/sourcemap-codec-1.5.5.tgz
Source4: https://registry.npmjs.org/@jridgewell/trace-mapping/-/trace-mapping-0.3.30.tgz
Source5: https://registry.npmjs.org/@types/eslint/-/eslint-9.6.1.tgz
Source6: https://registry.npmjs.org/@types/eslint-scope/-/eslint-scope-3.7.7.tgz
Source7: https://registry.npmjs.org/@types/estree/-/estree-1.0.8.tgz
Source8: https://registry.npmjs.org/@types/json-schema/-/json-schema-7.0.15.tgz
Source9: https://registry.npmjs.org/@types/node/-/node-24.3.0.tgz
Source10: https://registry.npmjs.org/@webassemblyjs/ast/-/ast-1.14.1.tgz
Source11: https://registry.npmjs.org/@webassemblyjs/floating-point-hex-parser/-/floating-point-hex-parser-1.13.2.tgz
Source12: https://registry.npmjs.org/@webassemblyjs/helper-api-error/-/helper-api-error-1.13.2.tgz
Source13: https://registry.npmjs.org/@webassemblyjs/helper-buffer/-/helper-buffer-1.14.1.tgz
Source14: https://registry.npmjs.org/@webassemblyjs/helper-numbers/-/helper-numbers-1.13.2.tgz
Source15: https://registry.npmjs.org/@webassemblyjs/helper-wasm-bytecode/-/helper-wasm-bytecode-1.13.2.tgz
Source16: https://registry.npmjs.org/@webassemblyjs/helper-wasm-section/-/helper-wasm-section-1.14.1.tgz
Source17: https://registry.npmjs.org/@webassemblyjs/ieee754/-/ieee754-1.13.2.tgz
Source18: https://registry.npmjs.org/@webassemblyjs/leb128/-/leb128-1.13.2.tgz
Source19: https://registry.npmjs.org/@webassemblyjs/utf8/-/utf8-1.13.2.tgz
Source20: https://registry.npmjs.org/@webassemblyjs/wasm-edit/-/wasm-edit-1.14.1.tgz
Source21: https://registry.npmjs.org/@webassemblyjs/wasm-gen/-/wasm-gen-1.14.1.tgz
Source22: https://registry.npmjs.org/@webassemblyjs/wasm-opt/-/wasm-opt-1.14.1.tgz
Source23: https://registry.npmjs.org/@webassemblyjs/wasm-parser/-/wasm-parser-1.14.1.tgz
Source24: https://registry.npmjs.org/@webassemblyjs/wast-printer/-/wast-printer-1.14.1.tgz
Source25: https://registry.npmjs.org/@xtuc/ieee754/-/ieee754-1.2.0.tgz
Source26: https://registry.npmjs.org/@xtuc/long/-/long-4.2.2.tgz
Source27: https://registry.npmjs.org/acorn/-/acorn-8.15.0.tgz
Source28: https://registry.npmjs.org/acorn-import-phases/-/acorn-import-phases-1.0.4.tgz
Source29: https://registry.npmjs.org/ajv/-/ajv-8.17.1.tgz
Source30: https://registry.npmjs.org/ajv-formats/-/ajv-formats-2.1.1.tgz
Source31: https://registry.npmjs.org/ajv-keywords/-/ajv-keywords-5.1.0.tgz
Source32: https://registry.npmjs.org/browserslist/-/browserslist-4.25.2.tgz
Source33: https://registry.npmjs.org/buffer-from/-/buffer-from-1.1.2.tgz
Source34: https://registry.npmjs.org/caniuse-lite/-/caniuse-lite-1.0.30001735.tgz
Source35: https://registry.npmjs.org/chrome-trace-event/-/chrome-trace-event-1.0.4.tgz
Source36: https://registry.npmjs.org/commander/-/commander-2.20.3.tgz
Source37: https://registry.npmjs.org/electron-to-chromium/-/electron-to-chromium-1.5.203.tgz
Source38: https://registry.npmjs.org/enhanced-resolve/-/enhanced-resolve-5.18.3.tgz
Source39: https://registry.npmjs.org/es-module-lexer/-/es-module-lexer-1.7.0.tgz
Source40: https://registry.npmjs.org/escalade/-/escalade-3.2.0.tgz
Source41: https://registry.npmjs.org/eslint-scope/-/eslint-scope-5.1.1.tgz
Source42: https://registry.npmjs.org/esrecurse/-/esrecurse-4.3.0.tgz
Source43: https://registry.npmjs.org/estraverse/-/estraverse-4.3.0.tgz
Source44: https://registry.npmjs.org/estraverse/-/estraverse-5.3.0.tgz
Source45: https://registry.npmjs.org/events/-/events-3.3.0.tgz
Source46: https://registry.npmjs.org/fast-deep-equal/-/fast-deep-equal-3.1.3.tgz
Source47: https://registry.npmjs.org/fast-uri/-/fast-uri-3.0.6.tgz
Source48: https://registry.npmjs.org/glob-to-regexp/-/glob-to-regexp-0.4.1.tgz
Source49: https://registry.npmjs.org/graceful-fs/-/graceful-fs-4.2.11.tgz
Source50: https://registry.npmjs.org/has-flag/-/has-flag-4.0.0.tgz
Source51: https://registry.npmjs.org/jest-worker/-/jest-worker-27.5.1.tgz
Source52: https://registry.npmjs.org/json-parse-even-better-errors/-/json-parse-even-better-errors-2.3.1.tgz
Source53: https://registry.npmjs.org/json-schema-traverse/-/json-schema-traverse-1.0.0.tgz
Source54: https://registry.npmjs.org/loader-runner/-/loader-runner-4.3.0.tgz
Source55: https://registry.npmjs.org/merge-stream/-/merge-stream-2.0.0.tgz
Source56: https://registry.npmjs.org/mime-db/-/mime-db-1.52.0.tgz
Source57: https://registry.npmjs.org/mime-types/-/mime-types-2.1.35.tgz
Source58: https://registry.npmjs.org/neo-async/-/neo-async-2.6.2.tgz
Source59: https://registry.npmjs.org/node-releases/-/node-releases-2.0.19.tgz
Source60: https://registry.npmjs.org/picocolors/-/picocolors-1.1.1.tgz
Source61: https://registry.npmjs.org/randombytes/-/randombytes-2.1.0.tgz
Source62: https://registry.npmjs.org/require-from-string/-/require-from-string-2.0.2.tgz
Source63: https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.2.1.tgz
Source64: https://registry.npmjs.org/schema-utils/-/schema-utils-4.3.2.tgz
Source65: https://registry.npmjs.org/serialize-javascript/-/serialize-javascript-6.0.2.tgz
Source66: https://registry.npmjs.org/source-map/-/source-map-0.6.1.tgz
Source67: https://registry.npmjs.org/source-map-support/-/source-map-support-0.5.21.tgz
Source68: https://registry.npmjs.org/supports-color/-/supports-color-8.1.1.tgz
Source69: https://registry.npmjs.org/tapable/-/tapable-2.2.2.tgz
Source70: https://registry.npmjs.org/terser/-/terser-5.43.1.tgz
Source71: https://registry.npmjs.org/terser-webpack-plugin/-/terser-webpack-plugin-5.3.14.tgz
Source72: https://registry.npmjs.org/undici-types/-/undici-types-7.10.0.tgz
Source73: https://registry.npmjs.org/update-browserslist-db/-/update-browserslist-db-1.1.3.tgz
Source74: https://registry.npmjs.org/watchpack/-/watchpack-2.4.4.tgz
Source75: https://registry.npmjs.org/webpack/-/webpack-5.101.2.tgz
Source76: https://registry.npmjs.org/webpack-sources/-/webpack-sources-3.3.3.tgz
Source77: nodejs-webpack-%{version}-registry.npmjs.org.tgz
BuildRequires: %{?scl_prefix_nodejs}npm
%if 0%{!?scl:1}
BuildRequires: nodejs-packaging
%endif
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}
Provides: bundled(npm(@jridgewell/gen-mapping)) = 0.3.13
Provides: bundled(npm(@jridgewell/resolve-uri)) = 3.1.2
Provides: bundled(npm(@jridgewell/source-map)) = 0.3.11
Provides: bundled(npm(@jridgewell/sourcemap-codec)) = 1.5.5
Provides: bundled(npm(@jridgewell/trace-mapping)) = 0.3.30
Provides: bundled(npm(@types/eslint)) = 9.6.1
Provides: bundled(npm(@types/eslint-scope)) = 3.7.7
Provides: bundled(npm(@types/estree)) = 1.0.8
Provides: bundled(npm(@types/json-schema)) = 7.0.15
Provides: bundled(npm(@types/node)) = 24.3.0
Provides: bundled(npm(@webassemblyjs/ast)) = 1.14.1
Provides: bundled(npm(@webassemblyjs/floating-point-hex-parser)) = 1.13.2
Provides: bundled(npm(@webassemblyjs/helper-api-error)) = 1.13.2
Provides: bundled(npm(@webassemblyjs/helper-buffer)) = 1.14.1
Provides: bundled(npm(@webassemblyjs/helper-numbers)) = 1.13.2
Provides: bundled(npm(@webassemblyjs/helper-wasm-bytecode)) = 1.13.2
Provides: bundled(npm(@webassemblyjs/helper-wasm-section)) = 1.14.1
Provides: bundled(npm(@webassemblyjs/ieee754)) = 1.13.2
Provides: bundled(npm(@webassemblyjs/leb128)) = 1.13.2
Provides: bundled(npm(@webassemblyjs/utf8)) = 1.13.2
Provides: bundled(npm(@webassemblyjs/wasm-edit)) = 1.14.1
Provides: bundled(npm(@webassemblyjs/wasm-gen)) = 1.14.1
Provides: bundled(npm(@webassemblyjs/wasm-opt)) = 1.14.1
Provides: bundled(npm(@webassemblyjs/wasm-parser)) = 1.14.1
Provides: bundled(npm(@webassemblyjs/wast-printer)) = 1.14.1
Provides: bundled(npm(@xtuc/ieee754)) = 1.2.0
Provides: bundled(npm(@xtuc/long)) = 4.2.2
Provides: bundled(npm(acorn)) = 8.15.0
Provides: bundled(npm(acorn-import-phases)) = 1.0.4
Provides: bundled(npm(ajv)) = 8.17.1
Provides: bundled(npm(ajv-formats)) = 2.1.1
Provides: bundled(npm(ajv-keywords)) = 5.1.0
Provides: bundled(npm(browserslist)) = 4.25.2
Provides: bundled(npm(buffer-from)) = 1.1.2
Provides: bundled(npm(caniuse-lite)) = 1.0.30001735
Provides: bundled(npm(chrome-trace-event)) = 1.0.4
Provides: bundled(npm(commander)) = 2.20.3
Provides: bundled(npm(electron-to-chromium)) = 1.5.203
Provides: bundled(npm(enhanced-resolve)) = 5.18.3
Provides: bundled(npm(es-module-lexer)) = 1.7.0
Provides: bundled(npm(escalade)) = 3.2.0
Provides: bundled(npm(eslint-scope)) = 5.1.1
Provides: bundled(npm(esrecurse)) = 4.3.0
Provides: bundled(npm(estraverse)) = 4.3.0
Provides: bundled(npm(estraverse)) = 5.3.0
Provides: bundled(npm(events)) = 3.3.0
Provides: bundled(npm(fast-deep-equal)) = 3.1.3
Provides: bundled(npm(fast-uri)) = 3.0.6
Provides: bundled(npm(glob-to-regexp)) = 0.4.1
Provides: bundled(npm(graceful-fs)) = 4.2.11
Provides: bundled(npm(has-flag)) = 4.0.0
Provides: bundled(npm(jest-worker)) = 27.5.1
Provides: bundled(npm(json-parse-even-better-errors)) = 2.3.1
Provides: bundled(npm(json-schema-traverse)) = 1.0.0
Provides: bundled(npm(loader-runner)) = 4.3.0
Provides: bundled(npm(merge-stream)) = 2.0.0
Provides: bundled(npm(mime-db)) = 1.52.0
Provides: bundled(npm(mime-types)) = 2.1.35
Provides: bundled(npm(neo-async)) = 2.6.2
Provides: bundled(npm(node-releases)) = 2.0.19
Provides: bundled(npm(picocolors)) = 1.1.1
Provides: bundled(npm(randombytes)) = 2.1.0
Provides: bundled(npm(require-from-string)) = 2.0.2
Provides: bundled(npm(safe-buffer)) = 5.2.1
Provides: bundled(npm(schema-utils)) = 4.3.2
Provides: bundled(npm(serialize-javascript)) = 6.0.2
Provides: bundled(npm(source-map)) = 0.6.1
Provides: bundled(npm(source-map-support)) = 0.5.21
Provides: bundled(npm(supports-color)) = 8.1.1
Provides: bundled(npm(tapable)) = 2.2.2
Provides: bundled(npm(terser)) = 5.43.1
Provides: bundled(npm(terser-webpack-plugin)) = 5.3.14
Provides: bundled(npm(undici-types)) = 7.10.0
Provides: bundled(npm(update-browserslist-db)) = 1.1.3
Provides: bundled(npm(watchpack)) = 2.4.4
Provides: bundled(npm(webpack)) = 5.101.2
Provides: bundled(npm(webpack-sources)) = 3.3.3
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

%setup -T -q -a 77 -D -n %{npm_cache_dir}

%build
%{?scl:scl enable %{?scl_nodejs} - << \end_of_scl}
npm install --legacy-peer-deps --cache-min Infinity --cache %{?scl:../}%{npm_cache_dir} --no-shrinkwrap --no-optional --global-style true %{npm_name}@%{version}
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
* Sun Aug 17 2025 Foreman Packaging Automation <packaging@theforeman.org> 5.101.2-1
- Update to 5.101.2

* Wed Aug 13 2025 Foreman Packaging Automation <packaging@theforeman.org> 5.101.1-1
- Update to 5.101.1

* Sun Aug 03 2025 Foreman Packaging Automation <packaging@theforeman.org> 5.101.0-1
- Update to 5.101.0

* Wed Jul 16 2025 Foreman Packaging Automation <packaging@theforeman.org> 5.100.2-1
- Update to 5.100.2

* Sun Jul 13 2025 Foreman Packaging Automation <packaging@theforeman.org> 5.100.1-1
- Update to 5.100.1

* Wed May 21 2025 Foreman Packaging Automation <packaging@theforeman.org> 5.99.9-1
- Update to 5.99.9

* Wed May 07 2025 Foreman Packaging Automation <packaging@theforeman.org> 5.99.8-1
- Update to 5.99.8

* Sun Apr 27 2025 Foreman Packaging Automation <packaging@theforeman.org> 5.99.7-1
- Update to 5.99.7

* Sun Apr 20 2025 Foreman Packaging Automation <packaging@theforeman.org> 5.99.6-1
- Update to 5.99.6

* Wed Apr 09 2025 Foreman Packaging Automation <packaging@theforeman.org> 5.99.5-1
- Update to 5.99.5

* Tue Mar 18 2025 Foreman Packaging Automation <packaging@theforeman.org> 5.98.0-1
- Update to 5.98.0

* Fri Dec 13 2024 Foreman Packaging Automation <packaging@theforeman.org> 5.97.1-1
- Update to 5.97.1

* Thu Feb 01 2024 Eric D. Helms <ericdhelms@gmail.com> - 5.90.0-2
- Use --legacy-peer-deps during npm install

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
