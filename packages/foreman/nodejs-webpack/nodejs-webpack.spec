%global npm_name webpack

Name: nodejs-webpack
Version: 5.109.2
Release: 1%{?dist}
Summary: Packs ECMAScript/CommonJs/AMD modules for the browser
License: MIT
Group: Development/Libraries
URL: https://github.com/webpack/webpack
Source0: https://registry.npmjs.org/@jridgewell/gen-mapping/-/gen-mapping-0.3.13.tgz
Source1: https://registry.npmjs.org/@jridgewell/resolve-uri/-/resolve-uri-3.1.2.tgz
Source2: https://registry.npmjs.org/@jridgewell/source-map/-/source-map-0.3.11.tgz
Source3: https://registry.npmjs.org/@jridgewell/sourcemap-codec/-/sourcemap-codec-1.5.5.tgz
Source4: https://registry.npmjs.org/@jridgewell/trace-mapping/-/trace-mapping-0.3.31.tgz
Source5: https://registry.npmjs.org/@types/estree/-/estree-1.0.9.tgz
Source6: https://registry.npmjs.org/@types/json-schema/-/json-schema-7.0.15.tgz
Source7: https://registry.npmjs.org/@types/node/-/node-26.1.2.tgz
Source8: https://registry.npmjs.org/@webassemblyjs/ast/-/ast-1.14.1.tgz
Source9: https://registry.npmjs.org/@webassemblyjs/floating-point-hex-parser/-/floating-point-hex-parser-1.13.2.tgz
Source10: https://registry.npmjs.org/@webassemblyjs/helper-api-error/-/helper-api-error-1.13.2.tgz
Source11: https://registry.npmjs.org/@webassemblyjs/helper-buffer/-/helper-buffer-1.14.1.tgz
Source12: https://registry.npmjs.org/@webassemblyjs/helper-numbers/-/helper-numbers-1.13.2.tgz
Source13: https://registry.npmjs.org/@webassemblyjs/helper-wasm-bytecode/-/helper-wasm-bytecode-1.13.2.tgz
Source14: https://registry.npmjs.org/@webassemblyjs/helper-wasm-section/-/helper-wasm-section-1.14.1.tgz
Source15: https://registry.npmjs.org/@webassemblyjs/ieee754/-/ieee754-1.13.2.tgz
Source16: https://registry.npmjs.org/@webassemblyjs/leb128/-/leb128-1.13.2.tgz
Source17: https://registry.npmjs.org/@webassemblyjs/utf8/-/utf8-1.13.2.tgz
Source18: https://registry.npmjs.org/@webassemblyjs/wasm-edit/-/wasm-edit-1.14.1.tgz
Source19: https://registry.npmjs.org/@webassemblyjs/wasm-gen/-/wasm-gen-1.14.1.tgz
Source20: https://registry.npmjs.org/@webassemblyjs/wasm-opt/-/wasm-opt-1.14.1.tgz
Source21: https://registry.npmjs.org/@webassemblyjs/wasm-parser/-/wasm-parser-1.14.1.tgz
Source22: https://registry.npmjs.org/@webassemblyjs/wast-printer/-/wast-printer-1.14.1.tgz
Source23: https://registry.npmjs.org/@xtuc/ieee754/-/ieee754-1.2.0.tgz
Source24: https://registry.npmjs.org/@xtuc/long/-/long-4.2.2.tgz
Source25: https://registry.npmjs.org/acorn/-/acorn-8.18.0.tgz
Source26: https://registry.npmjs.org/ajv/-/ajv-8.20.0.tgz
Source27: https://registry.npmjs.org/ajv-formats/-/ajv-formats-2.1.1.tgz
Source28: https://registry.npmjs.org/ajv-keywords/-/ajv-keywords-5.1.0.tgz
Source29: https://registry.npmjs.org/baseline-browser-mapping/-/baseline-browser-mapping-2.11.7.tgz
Source30: https://registry.npmjs.org/browserslist/-/browserslist-4.28.7.tgz
Source31: https://registry.npmjs.org/buffer-from/-/buffer-from-1.1.2.tgz
Source32: https://registry.npmjs.org/caniuse-lite/-/caniuse-lite-1.0.30001806.tgz
Source33: https://registry.npmjs.org/chrome-trace-event/-/chrome-trace-event-1.0.4.tgz
Source34: https://registry.npmjs.org/commander/-/commander-2.20.3.tgz
Source35: https://registry.npmjs.org/electron-to-chromium/-/electron-to-chromium-1.5.398.tgz
Source36: https://registry.npmjs.org/enhanced-resolve/-/enhanced-resolve-5.24.4.tgz
Source37: https://registry.npmjs.org/es-module-lexer/-/es-module-lexer-2.3.1.tgz
Source38: https://registry.npmjs.org/escalade/-/escalade-3.2.0.tgz
Source39: https://registry.npmjs.org/eslint-scope/-/eslint-scope-5.1.1.tgz
Source40: https://registry.npmjs.org/esrecurse/-/esrecurse-4.3.0.tgz
Source41: https://registry.npmjs.org/estraverse/-/estraverse-4.3.0.tgz
Source42: https://registry.npmjs.org/estraverse/-/estraverse-5.3.0.tgz
Source43: https://registry.npmjs.org/events/-/events-3.3.0.tgz
Source44: https://registry.npmjs.org/fast-deep-equal/-/fast-deep-equal-3.1.3.tgz
Source45: https://registry.npmjs.org/fast-uri/-/fast-uri-3.1.4.tgz
Source46: https://registry.npmjs.org/graceful-fs/-/graceful-fs-4.2.11.tgz
Source47: https://registry.npmjs.org/has-flag/-/has-flag-4.0.0.tgz
Source48: https://registry.npmjs.org/jest-worker/-/jest-worker-27.5.1.tgz
Source49: https://registry.npmjs.org/json-schema-traverse/-/json-schema-traverse-1.0.0.tgz
Source50: https://registry.npmjs.org/merge-stream/-/merge-stream-2.0.0.tgz
Source51: https://registry.npmjs.org/mime-db/-/mime-db-1.54.0.tgz
Source52: https://registry.npmjs.org/minimizer-webpack-plugin/-/minimizer-webpack-plugin-5.6.1.tgz
Source53: https://registry.npmjs.org/neo-async/-/neo-async-2.6.2.tgz
Source54: https://registry.npmjs.org/node-releases/-/node-releases-2.0.51.tgz
Source55: https://registry.npmjs.org/picocolors/-/picocolors-1.1.1.tgz
Source56: https://registry.npmjs.org/require-from-string/-/require-from-string-2.0.2.tgz
Source57: https://registry.npmjs.org/schema-utils/-/schema-utils-4.3.3.tgz
Source58: https://registry.npmjs.org/source-map/-/source-map-0.6.1.tgz
Source59: https://registry.npmjs.org/source-map-support/-/source-map-support-0.5.21.tgz
Source60: https://registry.npmjs.org/supports-color/-/supports-color-8.1.1.tgz
Source61: https://registry.npmjs.org/tapable/-/tapable-2.3.3.tgz
Source62: https://registry.npmjs.org/terser/-/terser-5.49.0.tgz
Source63: https://registry.npmjs.org/undici-types/-/undici-types-8.3.0.tgz
Source64: https://registry.npmjs.org/update-browserslist-db/-/update-browserslist-db-1.2.3.tgz
Source65: https://registry.npmjs.org/watchpack/-/watchpack-2.5.2.tgz
Source66: https://registry.npmjs.org/webpack/-/webpack-5.109.2.tgz
Source67: https://registry.npmjs.org/webpack-sources/-/webpack-sources-3.5.1.tgz
BuildRequires: npm >= 7
BuildRequires: nodejs-packaging
%if 0%{?rhel} == 10
# https://issues.redhat.com/browse/RHEL-137712 is fixed in RHEL 10.3
BuildRequires: /usr/bin/node
%endif
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: npm(%{npm_name}) = %{version}
Provides: bundled(npm(@jridgewell/gen-mapping)) = 0.3.13
Provides: bundled(npm(@jridgewell/resolve-uri)) = 3.1.2
Provides: bundled(npm(@jridgewell/source-map)) = 0.3.11
Provides: bundled(npm(@jridgewell/sourcemap-codec)) = 1.5.5
Provides: bundled(npm(@jridgewell/trace-mapping)) = 0.3.31
Provides: bundled(npm(@types/estree)) = 1.0.9
Provides: bundled(npm(@types/json-schema)) = 7.0.15
Provides: bundled(npm(@types/node)) = 26.1.2
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
Provides: bundled(npm(acorn)) = 8.18.0
Provides: bundled(npm(ajv)) = 8.20.0
Provides: bundled(npm(ajv-formats)) = 2.1.1
Provides: bundled(npm(ajv-keywords)) = 5.1.0
Provides: bundled(npm(baseline-browser-mapping)) = 2.11.7
Provides: bundled(npm(browserslist)) = 4.28.7
Provides: bundled(npm(buffer-from)) = 1.1.2
Provides: bundled(npm(caniuse-lite)) = 1.0.30001806
Provides: bundled(npm(chrome-trace-event)) = 1.0.4
Provides: bundled(npm(commander)) = 2.20.3
Provides: bundled(npm(electron-to-chromium)) = 1.5.398
Provides: bundled(npm(enhanced-resolve)) = 5.24.4
Provides: bundled(npm(es-module-lexer)) = 2.3.1
Provides: bundled(npm(escalade)) = 3.2.0
Provides: bundled(npm(eslint-scope)) = 5.1.1
Provides: bundled(npm(esrecurse)) = 4.3.0
Provides: bundled(npm(estraverse)) = 4.3.0
Provides: bundled(npm(estraverse)) = 5.3.0
Provides: bundled(npm(events)) = 3.3.0
Provides: bundled(npm(fast-deep-equal)) = 3.1.3
Provides: bundled(npm(fast-uri)) = 3.1.4
Provides: bundled(npm(graceful-fs)) = 4.2.11
Provides: bundled(npm(has-flag)) = 4.0.0
Provides: bundled(npm(jest-worker)) = 27.5.1
Provides: bundled(npm(json-schema-traverse)) = 1.0.0
Provides: bundled(npm(merge-stream)) = 2.0.0
Provides: bundled(npm(mime-db)) = 1.54.0
Provides: bundled(npm(minimizer-webpack-plugin)) = 5.6.1
Provides: bundled(npm(neo-async)) = 2.6.2
Provides: bundled(npm(node-releases)) = 2.0.51
Provides: bundled(npm(picocolors)) = 1.1.1
Provides: bundled(npm(require-from-string)) = 2.0.2
Provides: bundled(npm(schema-utils)) = 4.3.3
Provides: bundled(npm(source-map)) = 0.6.1
Provides: bundled(npm(source-map-support)) = 0.5.21
Provides: bundled(npm(supports-color)) = 8.1.1
Provides: bundled(npm(tapable)) = 2.3.3
Provides: bundled(npm(terser)) = 5.49.0
Provides: bundled(npm(undici-types)) = 8.3.0
Provides: bundled(npm(update-browserslist-db)) = 1.2.3
Provides: bundled(npm(watchpack)) = 2.5.2
Provides: bundled(npm(webpack)) = 5.109.2
Provides: bundled(npm(webpack-sources)) = 3.5.1
AutoReq: no
AutoProv: no

%define npm_cache_dir npm_cache_%{name}-%{version}-%{release}

%description
%{summary}

%prep
mkdir -p %{npm_cache_dir}
for tgz in %{sources}; do
  npm cache add --cache %{npm_cache_dir} $tgz
done

# Synthesize registry packuments from source tarballs so npm can resolve
# the dependency tree offline without a pre-built cache tarball.
node - %{npm_cache_dir} %{sources} << 'EOF_SYNTHESIZE'
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const { execSync } = require('child_process');

const cacheDir = path.resolve(process.argv[2]);
const tarballs = process.argv.slice(3);
const cacacheDir = path.join(cacheDir, '_cacache');

const packuments = {};

for (const tgz of tarballs) {
  let pkgJson;
  try {
    // maxBuffer must be raised: the default 1MiB is exceeded by large packages
    // (@patternfly/react-tokens lists 22k entries, ~1.3MB), and the resulting
    // ENOBUFS would otherwise drop the package from the packuments silently.
    const listing = execSync(`tar tf "${tgz}"`, {encoding: 'utf-8', maxBuffer: Infinity});
    const pkgPath = listing.split('\n').find(l => /^[^/]+\/package\.json$/.test(l));
    if (!pkgPath) throw new Error('no top-level package.json in tarball');
    const raw = execSync(`tar xf "${tgz}" --to-stdout "${pkgPath}"`, {encoding: 'utf-8', maxBuffer: Infinity});
    pkgJson = JSON.parse(raw);
  } catch (e) {
    // Every Source must yield a packument entry; skipping one surfaces later as
    // an unrelated ENOTCACHED for whichever package depended on it.
    throw new Error(`failed to read package.json from ${tgz}: ${e.message}`);
  }

  const tgzData = fs.readFileSync(tgz);
  const integrity = 'sha512-' + crypto.createHash('sha512').update(tgzData).digest('base64');
  const shasum = crypto.createHash('sha1').update(tgzData).digest('hex');

  const encodedName = pkgJson.name.replace('/', '%2f');
  const versionEntry = Object.assign({}, pkgJson, {
    dist: {
      tarball: 'https://registry.npmjs.org/' + encodedName + '/-/' + pkgJson.name.split('/').pop() + '-' + pkgJson.version + '.tgz',
      integrity: integrity,
      shasum: shasum
    },
    _hasShrinkwrap: false
  });

  if (!packuments[pkgJson.name]) {
    packuments[pkgJson.name] = {
      _id: pkgJson.name,
      name: pkgJson.name,
      'dist-tags': {latest: pkgJson.version},
      versions: {}
    };
  }
  packuments[pkgJson.name].versions[pkgJson.version] = versionEntry;
}

for (const [name, packument] of Object.entries(packuments)) {
  const packBuf = Buffer.from(JSON.stringify(packument));
  const contentHash = crypto.createHash('sha512').update(packBuf).digest('hex');
  const contentIntegrity = 'sha512-' + crypto.createHash('sha512').update(packBuf).digest('base64');

  const contentDir = path.join(cacacheDir, 'content-v2', 'sha512', contentHash.slice(0, 2), contentHash.slice(2, 4));
  fs.mkdirSync(contentDir, {recursive: true});
  fs.writeFileSync(path.join(contentDir, contentHash.slice(4)), packBuf);

  const encodedName = name.replace('/', '%2f');
  const cacheKey = 'make-fetch-happen:request-cache:https://registry.npmjs.org/' + encodedName;
  const keyHash = crypto.createHash('sha256').update(cacheKey).digest('hex');
  const indexDir = path.join(cacacheDir, 'index-v5', keyHash.slice(0, 2), keyHash.slice(2, 4));
  fs.mkdirSync(indexDir, {recursive: true});

  const indexEntry = JSON.stringify({
    key: cacheKey,
    integrity: contentIntegrity,
    time: 0,
    size: packBuf.length,
    metadata: {
      time: 0,
      url: 'https://registry.npmjs.org/' + encodedName,
      reqHeaders: {accept: 'application/json'},
      resHeaders: {'cache-control': 'public, max-age=300', 'content-type': 'application/json'},
      options: {}
    }
  });
  const entryHash = crypto.createHash('sha1').update(indexEntry).digest('hex');
  fs.writeFileSync(path.join(indexDir, keyHash.slice(4)), entryHash + '\t' + indexEntry + '\n');
}
EOF_SYNTHESIZE

%build
npm install --legacy-peer-deps --offline --cache %{_builddir}/%{npm_cache_dir} --package-lock false --omit optional --install-strategy shallow %{npm_name}@%{version}

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

%files
%{nodejs_sitelib}/%{npm_name}
%{_bindir}/webpack
%license node_modules/%{npm_name}/LICENSE
%doc node_modules/%{npm_name}/README.md

%changelog
* Wed Jul 29 2026 Zach Huntington-Meath <zhunting@redhat.com> 5.109.2-1
- Update to 5.109.2

* Sun Jul 05 2026 Foreman Packaging Automation <packaging@theforeman.org> 5.108.4-1
- Update to 5.108.4

* Wed Jul 01 2026 Foreman Packaging Automation <packaging@theforeman.org> 5.108.3-1
- Update to 5.108.3

* Sun Jun 07 2026 Foreman Packaging Automation <packaging@theforeman.org> 5.107.2-1
- Update to 5.107.2

* Thu Apr 23 2026 Foreman Packaging Automation <packaging@theforeman.org> 5.106.2-1
- Update to 5.106.2

* Sun Apr 12 2026 Foreman Packaging Automation <packaging@theforeman.org> 5.106.1-1
- Update to 5.106.1

* Sun Mar 08 2026 Foreman Packaging Automation <packaging@theforeman.org> 5.105.4-1
- Update to 5.105.4

* Sun Feb 15 2026 Foreman Packaging Automation <packaging@theforeman.org> 5.105.2-1
- Update to 5.105.2

* Wed Jan 14 2026 Foreman Packaging Automation <packaging@theforeman.org> 5.104.1-1
- Update to 5.104.1

* Wed Dec 17 2025 Foreman Packaging Automation <packaging@theforeman.org> 5.104.0-1
- Update to 5.104.0

* Wed Oct 08 2025 Foreman Packaging Automation <packaging@theforeman.org> 5.102.1-1
- Update to 5.102.1

* Sun Oct 05 2025 Foreman Packaging Automation <packaging@theforeman.org> 5.102.0-1
- Update to 5.102.0

* Wed Aug 20 2025 Foreman Packaging Automation <packaging@theforeman.org> 5.101.3-1
- Update to 5.101.3

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
