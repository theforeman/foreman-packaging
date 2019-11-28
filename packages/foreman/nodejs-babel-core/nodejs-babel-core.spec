%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name @babel/core

Name: %{?scl_prefix}nodejs-babel-core
Version: 7.7.4
Release: 1%{?dist}
Summary: Babel compiler core
License: MIT
Group: Development/Libraries
URL: https://babeljs.io/
Source0: https://registry.npmjs.org/@babel/code-frame/-/@babel/code-frame-7.5.5.tgz
Source1: https://registry.npmjs.org/@babel/core/-/@babel/core-7.7.4.tgz
Source2: https://registry.npmjs.org/@babel/generator/-/@babel/generator-7.7.4.tgz
Source3: https://registry.npmjs.org/@babel/helper-function-name/-/@babel/helper-function-name-7.7.4.tgz
Source4: https://registry.npmjs.org/@babel/helper-get-function-arity/-/@babel/helper-get-function-arity-7.7.4.tgz
Source5: https://registry.npmjs.org/@babel/helper-split-export-declaration/-/@babel/helper-split-export-declaration-7.7.4.tgz
Source6: https://registry.npmjs.org/@babel/helpers/-/@babel/helpers-7.7.4.tgz
Source7: https://registry.npmjs.org/@babel/highlight/-/@babel/highlight-7.5.0.tgz
Source8: https://registry.npmjs.org/@babel/parser/-/@babel/parser-7.7.4.tgz
Source9: https://registry.npmjs.org/@babel/template/-/@babel/template-7.7.4.tgz
Source10: https://registry.npmjs.org/@babel/traverse/-/@babel/traverse-7.7.4.tgz
Source11: https://registry.npmjs.org/@babel/types/-/@babel/types-7.7.4.tgz
Source12: https://registry.npmjs.org/ansi-styles/-/ansi-styles-3.2.1.tgz
Source13: https://registry.npmjs.org/chalk/-/chalk-2.4.2.tgz
Source14: https://registry.npmjs.org/color-convert/-/color-convert-1.9.3.tgz
Source15: https://registry.npmjs.org/color-name/-/color-name-1.1.3.tgz
Source16: https://registry.npmjs.org/convert-source-map/-/convert-source-map-1.7.0.tgz
Source17: https://registry.npmjs.org/debug/-/debug-4.1.1.tgz
Source18: https://registry.npmjs.org/escape-string-regexp/-/escape-string-regexp-1.0.5.tgz
Source19: https://registry.npmjs.org/esutils/-/esutils-2.0.3.tgz
Source20: https://registry.npmjs.org/globals/-/globals-11.12.0.tgz
Source21: https://registry.npmjs.org/has-flag/-/has-flag-3.0.0.tgz
Source22: https://registry.npmjs.org/js-tokens/-/js-tokens-4.0.0.tgz
Source23: https://registry.npmjs.org/jsesc/-/jsesc-2.5.2.tgz
Source24: https://registry.npmjs.org/json5/-/json5-2.1.1.tgz
Source25: https://registry.npmjs.org/lodash/-/lodash-4.17.15.tgz
Source26: https://registry.npmjs.org/minimist/-/minimist-1.2.0.tgz
Source27: https://registry.npmjs.org/ms/-/ms-2.1.2.tgz
Source28: https://registry.npmjs.org/path-parse/-/path-parse-1.0.6.tgz
Source29: https://registry.npmjs.org/resolve/-/resolve-1.13.1.tgz
Source30: https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.1.2.tgz
Source31: https://registry.npmjs.org/semver/-/semver-5.7.1.tgz
Source32: https://registry.npmjs.org/source-map/-/source-map-0.5.7.tgz
Source33: https://registry.npmjs.org/supports-color/-/supports-color-5.5.0.tgz
Source34: https://registry.npmjs.org/to-fast-properties/-/to-fast-properties-2.0.0.tgz
Source35: nodejs-babel-core-%{version}-registry.npmjs.org.tgz
%if 0%{?scl:1}
BuildRequires: %{?scl_prefix_nodejs}npm
%else
BuildRequires: nodejs-packaging
%endif
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}
Provides: bundled(npm(@babel/code-frame)) = 7.5.5
Provides: bundled(npm(@babel/core)) = 7.7.4
Provides: bundled(npm(@babel/generator)) = 7.7.4
Provides: bundled(npm(@babel/helper-function-name)) = 7.7.4
Provides: bundled(npm(@babel/helper-get-function-arity)) = 7.7.4
Provides: bundled(npm(@babel/helper-split-export-declaration)) = 7.7.4
Provides: bundled(npm(@babel/helpers)) = 7.7.4
Provides: bundled(npm(@babel/highlight)) = 7.5.0
Provides: bundled(npm(@babel/parser)) = 7.7.4
Provides: bundled(npm(@babel/template)) = 7.7.4
Provides: bundled(npm(@babel/traverse)) = 7.7.4
Provides: bundled(npm(@babel/types)) = 7.7.4
Provides: bundled(npm(ansi-styles)) = 3.2.1
Provides: bundled(npm(chalk)) = 2.4.2
Provides: bundled(npm(color-convert)) = 1.9.3
Provides: bundled(npm(color-name)) = 1.1.3
Provides: bundled(npm(convert-source-map)) = 1.7.0
Provides: bundled(npm(debug)) = 4.1.1
Provides: bundled(npm(escape-string-regexp)) = 1.0.5
Provides: bundled(npm(esutils)) = 2.0.3
Provides: bundled(npm(globals)) = 11.12.0
Provides: bundled(npm(has-flag)) = 3.0.0
Provides: bundled(npm(js-tokens)) = 4.0.0
Provides: bundled(npm(jsesc)) = 2.5.2
Provides: bundled(npm(json5)) = 2.1.1
Provides: bundled(npm(lodash)) = 4.17.15
Provides: bundled(npm(minimist)) = 1.2.0
Provides: bundled(npm(ms)) = 2.1.2
Provides: bundled(npm(path-parse)) = 1.0.6
Provides: bundled(npm(resolve)) = 1.13.1
Provides: bundled(npm(safe-buffer)) = 5.1.2
Provides: bundled(npm(semver)) = 5.7.1
Provides: bundled(npm(source-map)) = 0.5.7
Provides: bundled(npm(supports-color)) = 5.5.0
Provides: bundled(npm(to-fast-properties)) = 2.0.0
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

%setup -T -q -a 35 -D -n %{npm_cache_dir}

%build
%{?scl:scl enable %{?scl_nodejs} - << \end_of_scl}
npm install --cache-min Infinity --cache %{?scl:../}%{npm_cache_dir} --no-shrinkwrap --no-optional --global-style true %{npm_name}@%{version}
%{?scl:end_of_scl}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/lib %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%license node_modules/%{npm_name}/LICENSE
%doc node_modules/%{npm_name}/README.md

%changelog
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
