%global npm_name history

Name: nodejs-history
Version: 4.10.1
Release: 2%{?dist}
Summary: Manage session history with JavaScript
License: MIT
Group: Development/Libraries
URL: https://github.com/ReactTraining/history#readme
Source0: https://registry.npmjs.org/@babel/runtime/-/runtime-7.29.7.tgz
Source1: https://registry.npmjs.org/history/-/history-4.10.1.tgz
Source2: https://registry.npmjs.org/js-tokens/-/js-tokens-4.0.0.tgz
Source3: https://registry.npmjs.org/loose-envify/-/loose-envify-1.4.0.tgz
Source4: https://registry.npmjs.org/resolve-pathname/-/resolve-pathname-3.0.0.tgz
Source5: https://registry.npmjs.org/tiny-invariant/-/tiny-invariant-1.3.3.tgz
Source6: https://registry.npmjs.org/tiny-warning/-/tiny-warning-1.0.3.tgz
Source7: https://registry.npmjs.org/value-equal/-/value-equal-1.0.1.tgz
Source8: nodejs-history-%{version}-package-lock.json
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
Provides: bundled(npm(history)) = 4.10.1
Provides: bundled(npm(js-tokens)) = 4.0.0
Provides: bundled(npm(loose-envify)) = 1.4.0
Provides: bundled(npm(resolve-pathname)) = 3.0.0
Provides: bundled(npm(tiny-invariant)) = 1.3.3
Provides: bundled(npm(tiny-warning)) = 1.0.3
Provides: bundled(npm(value-equal)) = 1.0.1
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
cp -pfr node_modules/%{npm_name}/DOMUtils.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/ExecutionEnvironment.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/LocationUtils.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/PathUtils.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/cjs %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/createBrowserHistory.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/createHashHistory.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/createMemoryHistory.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/createTransitionManager.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/es %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/esm %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/index.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/umd %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/warnAboutDeprecatedCJSRequire.js %{buildroot}%{nodejs_sitelib}/%{npm_name}

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%license node_modules/%{npm_name}/LICENSE
%doc node_modules/%{npm_name}/README.md

%changelog
* Thu Jul 30 2026 Zach Huntington-Meath <zhunting@redhat.com> - 4.10.1-2
- Regenerate with correct npm2rpm strategy

* Thu Jul 30 2026 Zach Huntington-Meath <zhunting@redhat.com> 4.10.1-1
- Update to 4.10.1

* Thu Jul 30 2026 Zach Huntington-Meath <zhunting@redhat.com> 4.10.1-2
- Update to 4.10.1

* Wed Jul 16 2025 Foreman Packaging Automation <packaging@theforeman.org> 4.10.1-1
- Update to 4.10.1

* Tue Jul 08 2025 root <root> 4.7.2-1
- Add nodejs-history generated by npm2rpm using the bundle strategy

