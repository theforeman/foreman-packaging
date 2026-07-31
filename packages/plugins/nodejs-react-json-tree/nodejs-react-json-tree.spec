%global npm_name react-json-tree

Name: nodejs-react-json-tree
Version: 0.18.0
Release: 2%{?dist}
Summary: React JSON Viewer Component, Extracted from redux-devtools
License: MIT
Group: Development/Libraries
URL: https://github.com/reduxjs/redux-devtools/tree/master/packages/react-json-tree
Source0: https://registry.npmjs.org/@babel/runtime/-/runtime-7.29.7.tgz
Source1: https://registry.npmjs.org/@types/base16/-/base16-1.0.5.tgz
Source2: https://registry.npmjs.org/@types/lodash/-/lodash-4.17.24.tgz
Source3: https://registry.npmjs.org/base16/-/base16-1.0.0.tgz
Source4: https://registry.npmjs.org/color/-/color-3.2.1.tgz
Source5: https://registry.npmjs.org/color-convert/-/color-convert-1.9.3.tgz
Source6: https://registry.npmjs.org/color-name/-/color-name-1.1.3.tgz
Source7: https://registry.npmjs.org/color-string/-/color-string-1.9.1.tgz
Source8: https://registry.npmjs.org/csstype/-/csstype-3.2.3.tgz
Source9: https://registry.npmjs.org/is-arrayish/-/is-arrayish-0.3.4.tgz
Source10: https://registry.npmjs.org/lodash.curry/-/lodash.curry-4.1.1.tgz
Source11: https://registry.npmjs.org/react-base16-styling/-/react-base16-styling-0.9.1.tgz
Source12: https://registry.npmjs.org/react-json-tree/-/react-json-tree-0.18.0.tgz
Source13: https://registry.npmjs.org/simple-swizzle/-/simple-swizzle-0.2.4.tgz
Source14: nodejs-react-json-tree-%{version}-package-lock.json
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
Provides: bundled(npm(@babel/runtime)) = 7.29.7
Provides: bundled(npm(@types/base16)) = 1.0.5
Provides: bundled(npm(@types/lodash)) = 4.17.24
Provides: bundled(npm(base16)) = 1.0.0
Provides: bundled(npm(color)) = 3.2.1
Provides: bundled(npm(color-convert)) = 1.9.3
Provides: bundled(npm(color-name)) = 1.1.3
Provides: bundled(npm(color-string)) = 1.9.1
Provides: bundled(npm(csstype)) = 3.2.3
Provides: bundled(npm(is-arrayish)) = 0.3.4
Provides: bundled(npm(lodash.curry)) = 4.1.1
Provides: bundled(npm(react-base16-styling)) = 0.9.1
Provides: bundled(npm(react-json-tree)) = 0.18.0
Provides: bundled(npm(simple-swizzle)) = 0.2.4
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
cp -pfr node_modules/%{npm_name}/src %{buildroot}%{nodejs_sitelib}/%{npm_name}

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%license node_modules/%{npm_name}/LICENSE.md
%doc node_modules/%{npm_name}/README.md

%changelog
* Fri Jul 31 2026 Zach Huntington-Meath <zhunting@redhat.com> - 0.18.0-2
- Rebuild for EL10

* Thu Jul 30 2026 Zach Huntington-Meath <zhunting@redhat.com> 0.18.0-1
- Update to 0.18.0

* Thu Jul 30 2026 Zach Huntington-Meath <zhunting@redhat.com> 0.18.0-6
- Update to 0.18.0

* Thu Jul 30 2026 Zach Huntington-Meath <zhunting@redhat.com> 0.18.0-2
- Update to 0.18.0

* Sat Feb 03 2024 Evgeni Golov - 0.11.0-5
- Use legacy-peer-deps

* Mon Apr 20 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.11.0-4
- Add npm to buildrequires for el8

* Tue Oct 22 2019 Eric D. Helms <ericdhelms@gmail.com> - 0.11.0-3
- Build for SCL

* Sun Oct 06 2019 Eric D. Helms <ericdhelms@gmail.com> - 0.11.0-2
- Update to allow building for SCL

* Wed Apr 18 2018 Daniel Lobato Garcia <me@daniellobato.me> 0.11.0-1
- Add nodejs-react-json-tree generated by npm2rpm using the bundle strategy
