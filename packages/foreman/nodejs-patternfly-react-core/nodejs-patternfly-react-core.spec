%global npm_name @patternfly/react-core

Name: nodejs-patternfly-react-core
Version: 5.4.14
Release: 2%{?dist}
Summary: This library provides a set of common React components for use with the PatternFly reference implementation
License: MIT
Group: Development/Libraries
URL: https://github.com/patternfly/patternfly-react#readme
Source0: https://registry.npmjs.org/@patternfly/react-core/-/react-core-5.4.14.tgz
Source1: https://registry.npmjs.org/@patternfly/react-icons/-/react-icons-5.4.2.tgz
Source2: https://registry.npmjs.org/@patternfly/react-styles/-/react-styles-5.4.1.tgz
Source3: https://registry.npmjs.org/@patternfly/react-tokens/-/react-tokens-5.4.1.tgz
Source4: https://registry.npmjs.org/attr-accept/-/attr-accept-2.2.5.tgz
Source5: https://registry.npmjs.org/file-selector/-/file-selector-2.1.2.tgz
Source6: https://registry.npmjs.org/focus-trap/-/focus-trap-7.6.2.tgz
Source7: https://registry.npmjs.org/js-tokens/-/js-tokens-4.0.0.tgz
Source8: https://registry.npmjs.org/loose-envify/-/loose-envify-1.4.0.tgz
Source9: https://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz
Source10: https://registry.npmjs.org/prop-types/-/prop-types-15.8.1.tgz
Source11: https://registry.npmjs.org/react-dropzone/-/react-dropzone-14.4.1.tgz
Source12: https://registry.npmjs.org/react-is/-/react-is-16.13.1.tgz
Source13: https://registry.npmjs.org/tabbable/-/tabbable-6.5.0.tgz
Source14: https://registry.npmjs.org/tslib/-/tslib-2.8.1.tgz
Source15: nodejs-patternfly-react-core-%{version}-package-lock.json
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
Provides: bundled(npm(@patternfly/react-core)) = 5.4.14
Provides: bundled(npm(@patternfly/react-icons)) = 5.4.2
Provides: bundled(npm(@patternfly/react-styles)) = 5.4.1
Provides: bundled(npm(@patternfly/react-tokens)) = 5.4.1
Provides: bundled(npm(attr-accept)) = 2.2.5
Provides: bundled(npm(file-selector)) = 2.1.2
Provides: bundled(npm(focus-trap)) = 7.6.2
Provides: bundled(npm(js-tokens)) = 4.0.0
Provides: bundled(npm(loose-envify)) = 1.4.0
Provides: bundled(npm(object-assign)) = 4.1.1
Provides: bundled(npm(prop-types)) = 15.8.1
Provides: bundled(npm(react-dropzone)) = 14.4.1
Provides: bundled(npm(react-is)) = 16.13.1
Provides: bundled(npm(tabbable)) = 6.5.0
Provides: bundled(npm(tslib)) = 2.8.1
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
cp -pfr node_modules/%{npm_name}/components %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/deprecated %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/dist %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/helpers %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/layouts %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/next %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/scripts %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/single-packages.config.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/src %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/subpaths.config.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%license node_modules/%{npm_name}/LICENSE
%doc node_modules/%{npm_name}/CHANGELOG.md
%doc node_modules/%{npm_name}/CONTRIBUTING.md
%doc node_modules/%{npm_name}/README.md

%changelog
* Thu Jul 30 2026 Zach Huntington-Meath <zhunting@redhat.com> 5.4.14-2
- Update to 5.4.14

* Sun Aug 31 2025 Foreman Packaging Automation <packaging@theforeman.org> 5.4.14-1
- Update to 5.4.14

* Thu Jun 19 2025 MariaAga <mariaaga@redhat.com> 5.2.0-1
- Add nodejs-patternfly-react-core generated by npm2rpm using the bundle strategy

