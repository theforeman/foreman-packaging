%global npm_name @babel/preset-react

Name: nodejs-babel-preset-react
Version: 7.29.7
Release: 1%{?dist}
Summary: Babel preset for all React plugins
License: MIT
Group: Development/Libraries
URL: https://babel.dev/docs/en/next/babel-preset-react
Source0: https://registry.npmjs.org/@babel/code-frame/-/code-frame-7.29.7.tgz
Source1: https://registry.npmjs.org/@babel/generator/-/generator-7.29.8.tgz
Source2: https://registry.npmjs.org/@babel/helper-annotate-as-pure/-/helper-annotate-as-pure-7.29.7.tgz
Source3: https://registry.npmjs.org/@babel/helper-globals/-/helper-globals-7.29.7.tgz
Source4: https://registry.npmjs.org/@babel/helper-module-imports/-/helper-module-imports-7.29.7.tgz
Source5: https://registry.npmjs.org/@babel/helper-plugin-utils/-/helper-plugin-utils-7.29.7.tgz
Source6: https://registry.npmjs.org/@babel/helper-string-parser/-/helper-string-parser-7.29.7.tgz
Source7: https://registry.npmjs.org/@babel/helper-validator-identifier/-/helper-validator-identifier-7.29.7.tgz
Source8: https://registry.npmjs.org/@babel/helper-validator-option/-/helper-validator-option-7.29.7.tgz
Source9: https://registry.npmjs.org/@babel/parser/-/parser-7.29.8.tgz
Source10: https://registry.npmjs.org/@babel/plugin-syntax-jsx/-/plugin-syntax-jsx-7.29.7.tgz
Source11: https://registry.npmjs.org/@babel/plugin-transform-react-display-name/-/plugin-transform-react-display-name-7.29.7.tgz
Source12: https://registry.npmjs.org/@babel/plugin-transform-react-jsx/-/plugin-transform-react-jsx-7.29.7.tgz
Source13: https://registry.npmjs.org/@babel/plugin-transform-react-jsx-development/-/plugin-transform-react-jsx-development-7.29.7.tgz
Source14: https://registry.npmjs.org/@babel/plugin-transform-react-pure-annotations/-/plugin-transform-react-pure-annotations-7.29.7.tgz
Source15: https://registry.npmjs.org/@babel/preset-react/-/preset-react-7.29.7.tgz
Source16: https://registry.npmjs.org/@babel/template/-/template-7.29.7.tgz
Source17: https://registry.npmjs.org/@babel/traverse/-/traverse-7.29.8.tgz
Source18: https://registry.npmjs.org/@babel/types/-/types-7.29.8.tgz
Source19: https://registry.npmjs.org/@jridgewell/gen-mapping/-/gen-mapping-0.3.13.tgz
Source20: https://registry.npmjs.org/@jridgewell/resolve-uri/-/resolve-uri-3.1.2.tgz
Source21: https://registry.npmjs.org/@jridgewell/sourcemap-codec/-/sourcemap-codec-1.5.5.tgz
Source22: https://registry.npmjs.org/@jridgewell/trace-mapping/-/trace-mapping-0.3.31.tgz
Source23: https://registry.npmjs.org/debug/-/debug-4.4.3.tgz
Source24: https://registry.npmjs.org/js-tokens/-/js-tokens-4.0.0.tgz
Source25: https://registry.npmjs.org/jsesc/-/jsesc-3.1.0.tgz
Source26: https://registry.npmjs.org/ms/-/ms-2.1.3.tgz
Source27: https://registry.npmjs.org/picocolors/-/picocolors-1.1.1.tgz
Source28: nodejs-babel-preset-react-%{version}-package-lock.json
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
Provides: bundled(npm(@babel/code-frame)) = 7.29.7
Provides: bundled(npm(@babel/generator)) = 7.29.8
Provides: bundled(npm(@babel/helper-annotate-as-pure)) = 7.29.7
Provides: bundled(npm(@babel/helper-globals)) = 7.29.7
Provides: bundled(npm(@babel/helper-module-imports)) = 7.29.7
Provides: bundled(npm(@babel/helper-plugin-utils)) = 7.29.7
Provides: bundled(npm(@babel/helper-string-parser)) = 7.29.7
Provides: bundled(npm(@babel/helper-validator-identifier)) = 7.29.7
Provides: bundled(npm(@babel/helper-validator-option)) = 7.29.7
Provides: bundled(npm(@babel/parser)) = 7.29.8
Provides: bundled(npm(@babel/plugin-syntax-jsx)) = 7.29.7
Provides: bundled(npm(@babel/plugin-transform-react-display-name)) = 7.29.7
Provides: bundled(npm(@babel/plugin-transform-react-jsx)) = 7.29.7
Provides: bundled(npm(@babel/plugin-transform-react-jsx-development)) = 7.29.7
Provides: bundled(npm(@babel/plugin-transform-react-pure-annotations)) = 7.29.7
Provides: bundled(npm(@babel/preset-react)) = 7.29.7
Provides: bundled(npm(@babel/template)) = 7.29.7
Provides: bundled(npm(@babel/traverse)) = 7.29.8
Provides: bundled(npm(@babel/types)) = 7.29.8
Provides: bundled(npm(@jridgewell/gen-mapping)) = 0.3.13
Provides: bundled(npm(@jridgewell/resolve-uri)) = 3.1.2
Provides: bundled(npm(@jridgewell/sourcemap-codec)) = 1.5.5
Provides: bundled(npm(@jridgewell/trace-mapping)) = 0.3.31
Provides: bundled(npm(debug)) = 4.4.3
Provides: bundled(npm(js-tokens)) = 4.0.0
Provides: bundled(npm(jsesc)) = 3.1.0
Provides: bundled(npm(ms)) = 2.1.3
Provides: bundled(npm(picocolors)) = 1.1.1
AutoReq: no
AutoProv: no

%define npm_cache_dir npm_cache_%{name}-%{version}-%{release}

%description
%{summary}

%prep
# There is deliberately no setup section: every Source is consumed explicitly
# below, so the build runs in the top-level build directory. Do not name the
# setup macro here even in a comment - rpm expands macros inside comments, and
# on rpm 6 that runs it, unpacking Source0 and cd-ing into a directory that
# does not exist.
mkdir -p %{npm_cache_dir}
# npm ci installs the tree recorded in the lockfile: every entry carries a
# resolved URL and an integrity hash, and npm serves the tarballs from the
# cache primed here by content hash. No registry access is needed.
for src in %{sources}; do
  case "$src" in
    *.tgz) npm cache add --cache %{npm_cache_dir} "$src" ;;
    *-package-lock.json) cp "$src" package-lock.json ;;
    *) echo "unexpected Source, do not know how to handle it: $src" >&2; exit 1 ;;
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
%doc node_modules/%{npm_name}/README.md

%changelog
* Thu Aug 06 2026 MariaAga <mariaaga@redhat.com> 7.29.7-1
- Add nodejs-babel-preset-react generated by npm2rpm using the bundle strategy

