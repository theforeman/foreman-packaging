%global npm_name babel-loader

Name: nodejs-babel-loader
Version: 8.4.1
Release: 2%{?dist}
Summary: babel module loader for webpack
License: MIT
Group: Development/Libraries
URL: https://github.com/babel/babel-loader
Source0: https://registry.npmjs.org/@types/json-schema/-/json-schema-7.0.15.tgz
Source1: https://registry.npmjs.org/ajv/-/ajv-6.15.0.tgz
Source2: https://registry.npmjs.org/ajv-keywords/-/ajv-keywords-3.5.2.tgz
Source3: https://registry.npmjs.org/babel-loader/-/babel-loader-8.4.1.tgz
Source4: https://registry.npmjs.org/big.js/-/big.js-5.2.2.tgz
Source5: https://registry.npmjs.org/commondir/-/commondir-1.0.1.tgz
Source6: https://registry.npmjs.org/emojis-list/-/emojis-list-3.0.0.tgz
Source7: https://registry.npmjs.org/fast-deep-equal/-/fast-deep-equal-3.1.3.tgz
Source8: https://registry.npmjs.org/fast-json-stable-stringify/-/fast-json-stable-stringify-2.1.0.tgz
Source9: https://registry.npmjs.org/find-cache-dir/-/find-cache-dir-3.3.2.tgz
Source10: https://registry.npmjs.org/find-up/-/find-up-4.1.0.tgz
Source11: https://registry.npmjs.org/json-schema-traverse/-/json-schema-traverse-0.4.1.tgz
Source12: https://registry.npmjs.org/json5/-/json5-2.2.3.tgz
Source13: https://registry.npmjs.org/loader-utils/-/loader-utils-2.0.4.tgz
Source14: https://registry.npmjs.org/locate-path/-/locate-path-5.0.0.tgz
Source15: https://registry.npmjs.org/make-dir/-/make-dir-3.1.0.tgz
Source16: https://registry.npmjs.org/p-limit/-/p-limit-2.3.0.tgz
Source17: https://registry.npmjs.org/p-locate/-/p-locate-4.1.0.tgz
Source18: https://registry.npmjs.org/p-try/-/p-try-2.2.0.tgz
Source19: https://registry.npmjs.org/path-exists/-/path-exists-4.0.0.tgz
Source20: https://registry.npmjs.org/pkg-dir/-/pkg-dir-4.2.0.tgz
Source21: https://registry.npmjs.org/punycode/-/punycode-2.3.1.tgz
Source22: https://registry.npmjs.org/schema-utils/-/schema-utils-2.7.1.tgz
Source23: https://registry.npmjs.org/semver/-/semver-6.3.1.tgz
Source24: https://registry.npmjs.org/uri-js/-/uri-js-4.4.1.tgz
Source25: nodejs-babel-loader-%{version}-package-lock.json
BuildRequires: npm >= 7
BuildRequires: nodejs-packaging
# The prep section runs node directly, so this is needed unconditionally. It
# also works around https://issues.redhat.com/browse/RHEL-137712 on RHEL 10
# before 10.3, where the nodejs major version macro does not resolve without
# node in the buildroot.
BuildRequires: /usr/bin/node
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: npm(%{npm_name}) = %{version}
Provides: bundled(npm(@types/json-schema)) = 7.0.15
Provides: bundled(npm(ajv)) = 6.15.0
Provides: bundled(npm(ajv-keywords)) = 3.5.2
Provides: bundled(npm(babel-loader)) = 8.4.1
Provides: bundled(npm(big.js)) = 5.2.2
Provides: bundled(npm(commondir)) = 1.0.1
Provides: bundled(npm(emojis-list)) = 3.0.0
Provides: bundled(npm(fast-deep-equal)) = 3.1.3
Provides: bundled(npm(fast-json-stable-stringify)) = 2.1.0
Provides: bundled(npm(find-cache-dir)) = 3.3.2
Provides: bundled(npm(find-up)) = 4.1.0
Provides: bundled(npm(json-schema-traverse)) = 0.4.1
Provides: bundled(npm(json5)) = 2.2.3
Provides: bundled(npm(loader-utils)) = 2.0.4
Provides: bundled(npm(locate-path)) = 5.0.0
Provides: bundled(npm(make-dir)) = 3.1.0
Provides: bundled(npm(p-limit)) = 2.3.0
Provides: bundled(npm(p-locate)) = 4.1.0
Provides: bundled(npm(p-try)) = 2.2.0
Provides: bundled(npm(path-exists)) = 4.0.0
Provides: bundled(npm(pkg-dir)) = 4.2.0
Provides: bundled(npm(punycode)) = 2.3.1
Provides: bundled(npm(schema-utils)) = 2.7.1
Provides: bundled(npm(semver)) = 6.3.1
Provides: bundled(npm(uri-js)) = 4.4.1
AutoReq: no
AutoProv: no

%define npm_cache_dir npm_cache_%{name}-%{version}-%{release}

%description
%{summary}

%prep
mkdir -p %{npm_cache_dir}
# npm ci installs the tree recorded in the lockfile: every entry carries a
# resolved URL and an integrity hash, and npm serves the tarballs from the
# cache primed here by content hash. No registry access is needed.
for src in %{sources}; do
  case "$src" in
    *.tgz) npm cache add --cache %{npm_cache_dir} "$src" ;;
    *-package-lock.json) cp "$src" package-lock.json ;;
  esac
done

# Derive package.json from the lockfile so the two cannot disagree.
node -e '
const fs = require("fs");
const lock = JSON.parse(fs.readFileSync("package-lock.json"));
fs.writeFileSync("package.json", JSON.stringify({
  name: lock.name,
  version: lock.version,
  dependencies: lock.packages[""].dependencies
}, null, 2) + "\n");
'

%build
npm ci --legacy-peer-deps --offline --cache %{_builddir}/%{npm_cache_dir} --omit optional

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
# npm creates a scope directory for every scope named in the lockfile, including
# scopes whose packages were all omitted, which leaves empty dirs behind.
# -delete implies -depth, so nested empties go bottom-up in a single pass.
find %{buildroot}%{nodejs_sitelib}/%{npm_name} -type d -empty -delete
cp -pfr node_modules/%{npm_name}/lib %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%license node_modules/%{npm_name}/LICENSE
%doc node_modules/%{npm_name}/CHANGELOG.md
%doc node_modules/%{npm_name}/README.md

%changelog
* Thu Jul 30 2026 Zach Huntington-Meath <zhunting@redhat.com> - 8.4.1-2
- Regenerate with correct npm2rpm strategy

* Thu Jul 30 2026 Zach Huntington-Meath <zhunting@redhat.com> 8.4.1-1
- Update to 8.4.1

* Thu Jul 30 2026 Zach Huntington-Meath <zhunting@redhat.com> 8.4.1-2
- Update to 8.4.1

* Fri Dec 13 2024 Foreman Packaging Automation <packaging@theforeman.org> 8.4.1-1
- Update to 8.4.1

* Thu Feb 01 2024 Eric D. Helms <ericdhelms@gmail.com> - 8.3.0-2
- Use --legacy-peer-deps during npm install

* Fri Aug 11 2023 Foreman Packaging Automation <packaging@theforeman.org> 8.3.0-1
- Update to 8.3.0

* Tue Mar 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 8.0.6-2
- Bump packages to build for el8

* Wed Nov 27 2019 Evgeni Golov 8.0.6-1
- Update to 8.0.6

* Mon Oct 21 2019 Eric D. Helms <ericdhelms@gmail.com> - 7.1.4-3
- Build for SCL

* Fri Oct 04 2019 Eric D. Helms <ericdhelms@gmail.com> - 7.1.4-2
- Update specs to handle SCL

* Wed Jun 06 2018 Eric D. Helms <ericdhelms@gmail.com> 7.1.4-1
- Update to 7.1.4

* Tue Jul 25 2017 Michael Moll <kvedulv@kvedulv.de> 7.1.1-2
- Add missing provides to nodejs-babel-loader (eric.d.helms@gmail.com)

* Tue Jul 25 2017 Michael Moll <kvedulv@kvedulv.de> 7.1.1-1
- Bump babel-loader to 7.1.1 (eric.d.helms@gmail.com)

* Sat Sep 24 2016 Eric D Helms <ericdhelms@gmail.com> 6.2.4-2
- Fix ExclusiveArch for nodejs packages on EL6 (ericdhelms@gmail.com)

* Thu Aug 11 2016 Dominic Cleal <dominic@cleal.org> 6.2.4-1
- new package built with tito
