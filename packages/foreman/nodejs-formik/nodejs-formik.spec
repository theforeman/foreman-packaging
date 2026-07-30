%global npm_name formik

Name: nodejs-formik
Version: 1.5.8
Release: 3%{?dist}
Summary: Forms in React, without tears
License: MIT
Group: Development/Libraries
URL: https://github.com/jaredpalmer/formik#readme
Source0: https://registry.npmjs.org/asap/-/asap-2.0.6.tgz
Source1: https://registry.npmjs.org/core-js/-/core-js-1.2.7.tgz
Source2: https://registry.npmjs.org/create-react-context/-/create-react-context-0.2.3.tgz
Source3: https://registry.npmjs.org/deepmerge/-/deepmerge-2.2.1.tgz
Source4: https://registry.npmjs.org/encoding/-/encoding-0.1.13.tgz
Source5: https://registry.npmjs.org/fbjs/-/fbjs-0.8.18.tgz
Source6: https://registry.npmjs.org/formik/-/formik-1.5.8.tgz
Source7: https://registry.npmjs.org/gud/-/gud-1.0.0.tgz
Source8: https://registry.npmjs.org/hoist-non-react-statics/-/hoist-non-react-statics-3.3.2.tgz
Source9: https://registry.npmjs.org/iconv-lite/-/iconv-lite-0.6.3.tgz
Source10: https://registry.npmjs.org/is-stream/-/is-stream-1.1.0.tgz
Source11: https://registry.npmjs.org/isomorphic-fetch/-/isomorphic-fetch-2.2.1.tgz
Source12: https://registry.npmjs.org/js-tokens/-/js-tokens-4.0.0.tgz
Source13: https://registry.npmjs.org/lodash/-/lodash-4.18.1.tgz
Source14: https://registry.npmjs.org/lodash-es/-/lodash-es-4.18.1.tgz
Source15: https://registry.npmjs.org/loose-envify/-/loose-envify-1.4.0.tgz
Source16: https://registry.npmjs.org/node-fetch/-/node-fetch-1.7.3.tgz
Source17: https://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz
Source18: https://registry.npmjs.org/promise/-/promise-7.3.1.tgz
Source19: https://registry.npmjs.org/prop-types/-/prop-types-15.8.1.tgz
Source20: https://registry.npmjs.org/react-fast-compare/-/react-fast-compare-2.0.4.tgz
Source21: https://registry.npmjs.org/react-is/-/react-is-16.13.1.tgz
Source22: https://registry.npmjs.org/safer-buffer/-/safer-buffer-2.1.2.tgz
Source23: https://registry.npmjs.org/setimmediate/-/setimmediate-1.0.5.tgz
Source24: https://registry.npmjs.org/tiny-warning/-/tiny-warning-1.0.3.tgz
Source25: https://registry.npmjs.org/tslib/-/tslib-1.14.1.tgz
Source26: https://registry.npmjs.org/ua-parser-js/-/ua-parser-js-0.7.41.tgz
Source27: https://registry.npmjs.org/whatwg-fetch/-/whatwg-fetch-3.6.20.tgz
Source28: nodejs-formik-%{version}-package-lock.json
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
Provides: bundled(npm(asap)) = 2.0.6
Provides: bundled(npm(core-js)) = 1.2.7
Provides: bundled(npm(create-react-context)) = 0.2.3
Provides: bundled(npm(deepmerge)) = 2.2.1
Provides: bundled(npm(encoding)) = 0.1.13
Provides: bundled(npm(fbjs)) = 0.8.18
Provides: bundled(npm(formik)) = 1.5.8
Provides: bundled(npm(gud)) = 1.0.0
Provides: bundled(npm(hoist-non-react-statics)) = 3.3.2
Provides: bundled(npm(iconv-lite)) = 0.6.3
Provides: bundled(npm(is-stream)) = 1.1.0
Provides: bundled(npm(isomorphic-fetch)) = 2.2.1
Provides: bundled(npm(js-tokens)) = 4.0.0
Provides: bundled(npm(lodash)) = 4.18.1
Provides: bundled(npm(lodash-es)) = 4.18.1
Provides: bundled(npm(loose-envify)) = 1.4.0
Provides: bundled(npm(node-fetch)) = 1.7.3
Provides: bundled(npm(object-assign)) = 4.1.1
Provides: bundled(npm(promise)) = 7.3.1
Provides: bundled(npm(prop-types)) = 15.8.1
Provides: bundled(npm(react-fast-compare)) = 2.0.4
Provides: bundled(npm(react-is)) = 16.13.1
Provides: bundled(npm(safer-buffer)) = 2.1.2
Provides: bundled(npm(setimmediate)) = 1.0.5
Provides: bundled(npm(tiny-warning)) = 1.0.3
Provides: bundled(npm(tslib)) = 1.14.1
Provides: bundled(npm(ua-parser-js)) = 0.7.41
Provides: bundled(npm(whatwg-fetch)) = 3.6.20
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
cp -pfr node_modules/%{npm_name}/dist %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%license node_modules/%{npm_name}/LICENSE
%doc node_modules/%{npm_name}/README.md

%changelog
* Thu Jul 30 2026 Zach Huntington-Meath <zhunting@redhat.com> 1.5.8-3
- Update to 1.5.8

* Tue Mar 03 2026 Evgeni Golov 1.5.8-2
- Rebuild nodejs-formik with updated vendored dependencies

* Thu Jun 19 2025 MariaAga <mariaaga@redhat.com> 1.5.8-1
- Add nodejs-formik generated by npm2rpm using the bundle strategy

