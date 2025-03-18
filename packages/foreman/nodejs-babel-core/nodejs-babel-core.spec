%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name @babel/core

Name: %{?scl_prefix}nodejs-babel-core
Version: 7.26.10
Release: 1%{?dist}
Summary: Babel compiler core
License: MIT
Group: Development/Libraries
URL: https://babel.dev/docs/en/next/babel-core
Source0: https://registry.npmjs.org/@ampproject/remapping/-/remapping-2.3.0.tgz
Source1: https://registry.npmjs.org/@babel/code-frame/-/code-frame-7.26.2.tgz
Source2: https://registry.npmjs.org/@babel/compat-data/-/compat-data-7.26.8.tgz
Source3: https://registry.npmjs.org/@babel/core/-/core-7.26.10.tgz
Source4: https://registry.npmjs.org/@babel/generator/-/generator-7.26.10.tgz
Source5: https://registry.npmjs.org/@babel/helper-compilation-targets/-/helper-compilation-targets-7.26.5.tgz
Source6: https://registry.npmjs.org/@babel/helper-module-imports/-/helper-module-imports-7.25.9.tgz
Source7: https://registry.npmjs.org/@babel/helper-module-transforms/-/helper-module-transforms-7.26.0.tgz
Source8: https://registry.npmjs.org/@babel/helper-string-parser/-/helper-string-parser-7.25.9.tgz
Source9: https://registry.npmjs.org/@babel/helper-validator-identifier/-/helper-validator-identifier-7.25.9.tgz
Source10: https://registry.npmjs.org/@babel/helper-validator-option/-/helper-validator-option-7.25.9.tgz
Source11: https://registry.npmjs.org/@babel/helpers/-/helpers-7.26.10.tgz
Source12: https://registry.npmjs.org/@babel/parser/-/parser-7.26.10.tgz
Source13: https://registry.npmjs.org/@babel/template/-/template-7.26.9.tgz
Source14: https://registry.npmjs.org/@babel/traverse/-/traverse-7.26.10.tgz
Source15: https://registry.npmjs.org/@babel/types/-/types-7.26.10.tgz
Source16: https://registry.npmjs.org/@jridgewell/gen-mapping/-/gen-mapping-0.3.8.tgz
Source17: https://registry.npmjs.org/@jridgewell/resolve-uri/-/resolve-uri-3.1.2.tgz
Source18: https://registry.npmjs.org/@jridgewell/set-array/-/set-array-1.2.1.tgz
Source19: https://registry.npmjs.org/@jridgewell/sourcemap-codec/-/sourcemap-codec-1.5.0.tgz
Source20: https://registry.npmjs.org/@jridgewell/trace-mapping/-/trace-mapping-0.3.25.tgz
Source21: https://registry.npmjs.org/browserslist/-/browserslist-4.24.4.tgz
Source22: https://registry.npmjs.org/caniuse-lite/-/caniuse-lite-1.0.30001706.tgz
Source23: https://registry.npmjs.org/convert-source-map/-/convert-source-map-2.0.0.tgz
Source24: https://registry.npmjs.org/debug/-/debug-4.4.0.tgz
Source25: https://registry.npmjs.org/electron-to-chromium/-/electron-to-chromium-1.5.120.tgz
Source26: https://registry.npmjs.org/escalade/-/escalade-3.2.0.tgz
Source27: https://registry.npmjs.org/gensync/-/gensync-1.0.0-beta.2.tgz
Source28: https://registry.npmjs.org/globals/-/globals-11.12.0.tgz
Source29: https://registry.npmjs.org/js-tokens/-/js-tokens-4.0.0.tgz
Source30: https://registry.npmjs.org/jsesc/-/jsesc-3.1.0.tgz
Source31: https://registry.npmjs.org/json5/-/json5-2.2.3.tgz
Source32: https://registry.npmjs.org/lru-cache/-/lru-cache-5.1.1.tgz
Source33: https://registry.npmjs.org/ms/-/ms-2.1.3.tgz
Source34: https://registry.npmjs.org/node-releases/-/node-releases-2.0.19.tgz
Source35: https://registry.npmjs.org/picocolors/-/picocolors-1.1.1.tgz
Source36: https://registry.npmjs.org/semver/-/semver-6.3.1.tgz
Source37: https://registry.npmjs.org/update-browserslist-db/-/update-browserslist-db-1.1.3.tgz
Source38: https://registry.npmjs.org/yallist/-/yallist-3.1.1.tgz
Source39: nodejs-babel-core-%{version}-registry.npmjs.org.tgz
BuildRequires: %{?scl_prefix_nodejs}npm
%if 0%{!?scl:1}
BuildRequires: nodejs-packaging
%endif
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}
Provides: bundled(npm(@ampproject/remapping)) = 2.3.0
Provides: bundled(npm(@babel/code-frame)) = 7.26.2
Provides: bundled(npm(@babel/compat-data)) = 7.26.8
Provides: bundled(npm(@babel/core)) = 7.26.10
Provides: bundled(npm(@babel/generator)) = 7.26.10
Provides: bundled(npm(@babel/helper-compilation-targets)) = 7.26.5
Provides: bundled(npm(@babel/helper-module-imports)) = 7.25.9
Provides: bundled(npm(@babel/helper-module-transforms)) = 7.26.0
Provides: bundled(npm(@babel/helper-string-parser)) = 7.25.9
Provides: bundled(npm(@babel/helper-validator-identifier)) = 7.25.9
Provides: bundled(npm(@babel/helper-validator-option)) = 7.25.9
Provides: bundled(npm(@babel/helpers)) = 7.26.10
Provides: bundled(npm(@babel/parser)) = 7.26.10
Provides: bundled(npm(@babel/template)) = 7.26.9
Provides: bundled(npm(@babel/traverse)) = 7.26.10
Provides: bundled(npm(@babel/types)) = 7.26.10
Provides: bundled(npm(@jridgewell/gen-mapping)) = 0.3.8
Provides: bundled(npm(@jridgewell/resolve-uri)) = 3.1.2
Provides: bundled(npm(@jridgewell/set-array)) = 1.2.1
Provides: bundled(npm(@jridgewell/sourcemap-codec)) = 1.5.0
Provides: bundled(npm(@jridgewell/trace-mapping)) = 0.3.25
Provides: bundled(npm(browserslist)) = 4.24.4
Provides: bundled(npm(caniuse-lite)) = 1.0.30001706
Provides: bundled(npm(convert-source-map)) = 2.0.0
Provides: bundled(npm(debug)) = 4.4.0
Provides: bundled(npm(electron-to-chromium)) = 1.5.120
Provides: bundled(npm(escalade)) = 3.2.0
Provides: bundled(npm(gensync)) = 1.0.0-beta.2
Provides: bundled(npm(globals)) = 11.12.0
Provides: bundled(npm(js-tokens)) = 4.0.0
Provides: bundled(npm(jsesc)) = 3.1.0
Provides: bundled(npm(json5)) = 2.2.3
Provides: bundled(npm(lru-cache)) = 5.1.1
Provides: bundled(npm(ms)) = 2.1.3
Provides: bundled(npm(node-releases)) = 2.0.19
Provides: bundled(npm(picocolors)) = 1.1.1
Provides: bundled(npm(semver)) = 6.3.1
Provides: bundled(npm(update-browserslist-db)) = 1.1.3
Provides: bundled(npm(yallist)) = 3.1.1
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

%setup -T -q -a 39 -D -n %{npm_cache_dir}

%build
%{?scl:scl enable %{?scl_nodejs} - << \end_of_scl}
npm install --legacy-peer-deps --cache-min Infinity --cache %{?scl:../}%{npm_cache_dir} --no-shrinkwrap --no-optional --global-style true %{npm_name}@%{version}
%{?scl:end_of_scl}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/cjs-proxy.cjs %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/lib %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/src %{buildroot}%{nodejs_sitelib}/%{npm_name}

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%license node_modules/%{npm_name}/LICENSE
%doc node_modules/%{npm_name}/README.md

%changelog
* Tue Mar 18 2025 Foreman Packaging Automation <packaging@theforeman.org> 7.26.10-1
- Update to 7.26.10

* Wed Feb 12 2025 Foreman Packaging Automation <packaging@theforeman.org> 7.26.8-1
- Update to 7.26.8

* Sun Jan 26 2025 Foreman Packaging Automation <packaging@theforeman.org> 7.26.7-1
- Update to 7.26.7

* Fri Dec 13 2024 Foreman Packaging Automation <packaging@theforeman.org> 7.26.0-1
- Update to 7.26.0

* Thu Feb 01 2024 Eric D. Helms <ericdhelms@gmail.com> - 7.23.9-2
- Use --legacy-peer-deps during npm install

* Sun Jan 28 2024 Foreman Packaging Automation <packaging@theforeman.org> 7.23.9-1
- Update to 7.23.9

* Tue Jan 02 2024 Foreman Packaging Automation <packaging@theforeman.org> 7.23.7-1
- Update to 7.23.7

* Sun Dec 17 2023 Foreman Packaging Automation <packaging@theforeman.org> 7.23.6-1
- Update to 7.23.6

* Sun Dec 03 2023 Foreman Packaging Automation <packaging@theforeman.org> 7.23.5-1
- Update to 7.23.5

* Thu Nov 16 2023 Foreman Packaging Automation <packaging@theforeman.org> 7.23.3-1
- Update to 7.23.3

* Sun Oct 15 2023 Foreman Packaging Automation <packaging@theforeman.org> 7.23.2-1
- Update to 7.23.2

* Mon Oct 09 2023 Foreman Packaging Automation <packaging@theforeman.org> 7.23.0-1
- Update to 7.23.0

* Wed Sep 13 2023 Foreman Packaging Automation <packaging@theforeman.org> 7.22.17-1
- Update to 7.22.17

* Wed Sep 06 2023 Foreman Packaging Automation <packaging@theforeman.org> 7.22.11-1
- Update to 7.22.11

* Fri Aug 11 2023 Foreman Packaging Automation <packaging@theforeman.org> 7.22.10-1
- Update to 7.22.10

* Tue Mar 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 7.7.4-2
- Bump packages to build for el8

* Thu Nov 28 2019 Evgeni Golov 7.7.4-1
- Update to 7.7.4

* Mon Oct 21 2019 Eric D. Helms <ericdhelms@gmail.com> - 6.26.3-3
- Build for SCL

* Fri Oct 04 2019 Eric D. Helms <ericdhelms@gmail.com> - 6.26.3-2
- Update specs to handle SCL

* Wed May 09 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 6.26.3-1
- Update to 6.26.3

* Wed Nov 01 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 6.26.0-1
- Release babel-core 6.26.0 (ericdhelms@gmail.com)
- Bump releases (frostyx@email.cz)
- Fix cannot stat 'node_modules' for el7 (jkadlcik@redhat.com)

* Sat Sep 24 2016 Eric D Helms <ericdhelms@gmail.com> 6.7.7-3
- Fix ExclusiveArch for nodejs packages on EL6 (ericdhelms@gmail.com)

* Sat Sep 24 2016 Eric D Helms <ericdhelms@gmail.com> 6.7.7-2
-

* Thu Aug 11 2016 Dominic Cleal <dominic@cleal.org> 6.7.7-1
- new package built with tito
