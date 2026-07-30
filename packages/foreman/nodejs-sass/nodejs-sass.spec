%global npm_name sass

Name: nodejs-sass
Version: 1.60.0
Release: 4%{?dist}
Summary: A pure JavaScript implementation of Sass
License: MIT
Group: Development/Libraries
URL: https://github.com/sass/dart-sass
Source0: https://registry.npmjs.org/anymatch/-/anymatch-3.1.3.tgz
Source1: https://registry.npmjs.org/binary-extensions/-/binary-extensions-2.3.0.tgz
Source2: https://registry.npmjs.org/braces/-/braces-3.0.3.tgz
Source3: https://registry.npmjs.org/chokidar/-/chokidar-3.6.0.tgz
Source4: https://registry.npmjs.org/fill-range/-/fill-range-7.1.1.tgz
Source5: https://registry.npmjs.org/glob-parent/-/glob-parent-5.1.2.tgz
Source6: https://registry.npmjs.org/immutable/-/immutable-4.3.9.tgz
Source7: https://registry.npmjs.org/is-binary-path/-/is-binary-path-2.1.0.tgz
Source8: https://registry.npmjs.org/is-extglob/-/is-extglob-2.1.1.tgz
Source9: https://registry.npmjs.org/is-glob/-/is-glob-4.0.3.tgz
Source10: https://registry.npmjs.org/is-number/-/is-number-7.0.0.tgz
Source11: https://registry.npmjs.org/normalize-path/-/normalize-path-3.0.0.tgz
Source12: https://registry.npmjs.org/picomatch/-/picomatch-2.3.2.tgz
Source13: https://registry.npmjs.org/readdirp/-/readdirp-3.6.0.tgz
Source14: https://registry.npmjs.org/sass/-/sass-1.60.0.tgz
Source15: https://registry.npmjs.org/source-map-js/-/source-map-js-1.2.1.tgz
Source16: https://registry.npmjs.org/to-regex-range/-/to-regex-range-5.0.1.tgz
Source17: nodejs-sass-%{version}-package-lock.json
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
Provides: bundled(npm(anymatch)) = 3.1.3
Provides: bundled(npm(binary-extensions)) = 2.3.0
Provides: bundled(npm(braces)) = 3.0.3
Provides: bundled(npm(chokidar)) = 3.6.0
Provides: bundled(npm(fill-range)) = 7.1.1
Provides: bundled(npm(glob-parent)) = 5.1.2
Provides: bundled(npm(immutable)) = 4.3.9
Provides: bundled(npm(is-binary-path)) = 2.1.0
Provides: bundled(npm(is-extglob)) = 2.1.1
Provides: bundled(npm(is-glob)) = 4.0.3
Provides: bundled(npm(is-number)) = 7.0.0
Provides: bundled(npm(normalize-path)) = 3.0.0
Provides: bundled(npm(picomatch)) = 2.3.2
Provides: bundled(npm(readdirp)) = 3.6.0
Provides: bundled(npm(sass)) = 1.60.0
Provides: bundled(npm(source-map-js)) = 1.2.1
Provides: bundled(npm(to-regex-range)) = 5.0.1
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
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/sass.dart.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/sass.default.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/sass.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/types %{buildroot}%{nodejs_sitelib}/%{npm_name}

mkdir -p %{buildroot}%{_bindir}/
chmod 0755 %{buildroot}%{nodejs_sitelib}/%{npm_name}/sass.js
ln -sf %{nodejs_sitelib}/%{npm_name}/sass.js %{buildroot}%{_bindir}/sass

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%{_bindir}/sass
%license node_modules/%{npm_name}/LICENSE
%doc node_modules/%{npm_name}/README.md

%changelog
* Thu Jul 30 2026 Zach Huntington-Meath <zhunting@redhat.com> 1.60.0-4
- Update to 1.60.0

* Tue Dec 23 2025 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 1.60.0-3
- Rebuild vendor cache for NodeJS 22

* Thu Feb 01 2024 Eric D. Helms <ericdhelms@gmail.com> - 1.60.0-2
- Use --legacy-peer-deps during npm install

* Tue Jan 30 2024 Evgeni Golov 1.60.0-1
- Add nodejs-sass generated by npm2rpm using the bundle strategy
