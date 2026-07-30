%global npm_name @apollo/client

Name: nodejs-apollo-client
Version: 3.14.1
Release: 2%{?dist}
Summary: A fully-featured caching GraphQL client
License: MIT
Group: Development/Libraries
URL: https://www.apollographql.com/docs/react/
Source0: https://registry.npmjs.org/@apollo/client/-/client-3.14.1.tgz
Source1: https://registry.npmjs.org/@graphql-typed-document-node/core/-/core-3.2.0.tgz
Source2: https://registry.npmjs.org/@wry/caches/-/caches-1.0.1.tgz
Source3: https://registry.npmjs.org/@wry/context/-/context-0.7.4.tgz
Source4: https://registry.npmjs.org/@wry/equality/-/equality-0.5.7.tgz
Source5: https://registry.npmjs.org/@wry/trie/-/trie-0.5.0.tgz
Source6: https://registry.npmjs.org/graphql-tag/-/graphql-tag-2.12.7.tgz
Source7: https://registry.npmjs.org/hoist-non-react-statics/-/hoist-non-react-statics-3.3.2.tgz
Source8: https://registry.npmjs.org/js-tokens/-/js-tokens-4.0.0.tgz
Source9: https://registry.npmjs.org/loose-envify/-/loose-envify-1.4.0.tgz
Source10: https://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz
Source11: https://registry.npmjs.org/optimism/-/optimism-0.18.1.tgz
Source12: https://registry.npmjs.org/prop-types/-/prop-types-15.8.1.tgz
Source13: https://registry.npmjs.org/react-is/-/react-is-16.13.1.tgz
Source14: https://registry.npmjs.org/rehackt/-/rehackt-0.1.0.tgz
Source15: https://registry.npmjs.org/symbol-observable/-/symbol-observable-4.0.0.tgz
Source16: https://registry.npmjs.org/ts-invariant/-/ts-invariant-0.10.3.tgz
Source17: https://registry.npmjs.org/tslib/-/tslib-2.8.1.tgz
Source18: https://registry.npmjs.org/zen-observable/-/zen-observable-0.8.15.tgz
Source19: https://registry.npmjs.org/zen-observable-ts/-/zen-observable-ts-1.2.5.tgz
Source20: nodejs-apollo-client-%{version}-package-lock.json
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
Provides: bundled(npm(@apollo/client)) = 3.14.1
Provides: bundled(npm(@graphql-typed-document-node/core)) = 3.2.0
Provides: bundled(npm(@wry/caches)) = 1.0.1
Provides: bundled(npm(@wry/context)) = 0.7.4
Provides: bundled(npm(@wry/equality)) = 0.5.7
Provides: bundled(npm(@wry/trie)) = 0.5.0
Provides: bundled(npm(graphql-tag)) = 2.12.7
Provides: bundled(npm(hoist-non-react-statics)) = 3.3.2
Provides: bundled(npm(js-tokens)) = 4.0.0
Provides: bundled(npm(loose-envify)) = 1.4.0
Provides: bundled(npm(object-assign)) = 4.1.1
Provides: bundled(npm(optimism)) = 0.18.1
Provides: bundled(npm(prop-types)) = 15.8.1
Provides: bundled(npm(react-is)) = 16.13.1
Provides: bundled(npm(rehackt)) = 0.1.0
Provides: bundled(npm(symbol-observable)) = 4.0.0
Provides: bundled(npm(ts-invariant)) = 0.10.3
Provides: bundled(npm(tslib)) = 2.8.1
Provides: bundled(npm(zen-observable)) = 0.8.15
Provides: bundled(npm(zen-observable-ts)) = 1.2.5
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
cp -pfr node_modules/%{npm_name}/apollo-client.cjs %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/apollo-client.cjs.map %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/apollo-client.min.cjs %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/cache %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/config %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/core %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/dev %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/errors %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/index.d.ts %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/index.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/index.js.map %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/invariantErrorCodes.d.ts %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/invariantErrorCodes.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/invariantErrorCodes.js.map %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/link %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/main.cjs %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/main.cjs.map %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/main.cjs.native.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/main.d.cts %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/masking %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/react %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/testing %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/utilities %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/version.d.ts %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/version.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/version.js.map %{buildroot}%{nodejs_sitelib}/%{npm_name}

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%license node_modules/%{npm_name}/LICENSE
%doc node_modules/%{npm_name}/CHANGELOG.md
%doc node_modules/%{npm_name}/README.md

%changelog
* Thu Jul 30 2026 Zach Huntington-Meath <zhunting@redhat.com> 3.14.1-2
- Update to 3.14.1

* Wed Mar 18 2026 Foreman Packaging Automation <packaging@theforeman.org> 3.14.1-1
- Update to 3.14.1

* Wed Aug 27 2025 Foreman Packaging Automation <packaging@theforeman.org> 3.14.0-1
- Update to 3.14.0

* Thu Jun 19 2025 MariaAga <mariaaga@redhat.com> 3.3.7-1
- Add nodejs-apollo-client generated by npm2rpm using the bundle strategy

