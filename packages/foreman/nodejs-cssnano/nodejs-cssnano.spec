%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name cssnano

Name: %{?scl_prefix}nodejs-cssnano
Version: 5.1.15
Release: 1%{?dist}
Summary: A modular minifier, built on top of the PostCSS ecosystem
License: MIT
Group: Development/Libraries
URL: https://github.com/cssnano/cssnano
Source0: https://registry.npmjs.org/@trysound/sax/-/sax-0.2.0.tgz
Source1: https://registry.npmjs.org/boolbase/-/boolbase-1.0.0.tgz
Source2: https://registry.npmjs.org/browserslist/-/browserslist-4.22.2.tgz
Source3: https://registry.npmjs.org/caniuse-api/-/caniuse-api-3.0.0.tgz
Source4: https://registry.npmjs.org/caniuse-lite/-/caniuse-lite-1.0.30001570.tgz
Source5: https://registry.npmjs.org/colord/-/colord-2.9.3.tgz
Source6: https://registry.npmjs.org/commander/-/commander-7.2.0.tgz
Source7: https://registry.npmjs.org/css-declaration-sorter/-/css-declaration-sorter-6.4.1.tgz
Source8: https://registry.npmjs.org/css-select/-/css-select-4.3.0.tgz
Source9: https://registry.npmjs.org/css-tree/-/css-tree-1.1.3.tgz
Source10: https://registry.npmjs.org/css-what/-/css-what-6.1.0.tgz
Source11: https://registry.npmjs.org/cssesc/-/cssesc-3.0.0.tgz
Source12: https://registry.npmjs.org/cssnano/-/cssnano-5.1.15.tgz
Source13: https://registry.npmjs.org/cssnano-preset-default/-/cssnano-preset-default-5.2.14.tgz
Source14: https://registry.npmjs.org/cssnano-utils/-/cssnano-utils-3.1.0.tgz
Source15: https://registry.npmjs.org/csso/-/csso-4.2.0.tgz
Source16: https://registry.npmjs.org/dom-serializer/-/dom-serializer-1.4.1.tgz
Source17: https://registry.npmjs.org/domelementtype/-/domelementtype-2.3.0.tgz
Source18: https://registry.npmjs.org/domhandler/-/domhandler-4.3.1.tgz
Source19: https://registry.npmjs.org/domutils/-/domutils-2.8.0.tgz
Source20: https://registry.npmjs.org/electron-to-chromium/-/electron-to-chromium-1.4.611.tgz
Source21: https://registry.npmjs.org/entities/-/entities-2.2.0.tgz
Source22: https://registry.npmjs.org/escalade/-/escalade-3.1.1.tgz
Source23: https://registry.npmjs.org/lilconfig/-/lilconfig-2.1.0.tgz
Source24: https://registry.npmjs.org/lodash.memoize/-/lodash.memoize-4.1.2.tgz
Source25: https://registry.npmjs.org/lodash.uniq/-/lodash.uniq-4.5.0.tgz
Source26: https://registry.npmjs.org/mdn-data/-/mdn-data-2.0.14.tgz
Source27: https://registry.npmjs.org/node-releases/-/node-releases-2.0.14.tgz
Source28: https://registry.npmjs.org/normalize-url/-/normalize-url-6.1.0.tgz
Source29: https://registry.npmjs.org/nth-check/-/nth-check-2.1.1.tgz
Source30: https://registry.npmjs.org/picocolors/-/picocolors-1.0.0.tgz
Source31: https://registry.npmjs.org/postcss-calc/-/postcss-calc-8.2.4.tgz
Source32: https://registry.npmjs.org/postcss-colormin/-/postcss-colormin-5.3.1.tgz
Source33: https://registry.npmjs.org/postcss-convert-values/-/postcss-convert-values-5.1.3.tgz
Source34: https://registry.npmjs.org/postcss-discard-comments/-/postcss-discard-comments-5.1.2.tgz
Source35: https://registry.npmjs.org/postcss-discard-duplicates/-/postcss-discard-duplicates-5.1.0.tgz
Source36: https://registry.npmjs.org/postcss-discard-empty/-/postcss-discard-empty-5.1.1.tgz
Source37: https://registry.npmjs.org/postcss-discard-overridden/-/postcss-discard-overridden-5.1.0.tgz
Source38: https://registry.npmjs.org/postcss-merge-longhand/-/postcss-merge-longhand-5.1.7.tgz
Source39: https://registry.npmjs.org/postcss-merge-rules/-/postcss-merge-rules-5.1.4.tgz
Source40: https://registry.npmjs.org/postcss-minify-font-values/-/postcss-minify-font-values-5.1.0.tgz
Source41: https://registry.npmjs.org/postcss-minify-gradients/-/postcss-minify-gradients-5.1.1.tgz
Source42: https://registry.npmjs.org/postcss-minify-params/-/postcss-minify-params-5.1.4.tgz
Source43: https://registry.npmjs.org/postcss-minify-selectors/-/postcss-minify-selectors-5.2.1.tgz
Source44: https://registry.npmjs.org/postcss-normalize-charset/-/postcss-normalize-charset-5.1.0.tgz
Source45: https://registry.npmjs.org/postcss-normalize-display-values/-/postcss-normalize-display-values-5.1.0.tgz
Source46: https://registry.npmjs.org/postcss-normalize-positions/-/postcss-normalize-positions-5.1.1.tgz
Source47: https://registry.npmjs.org/postcss-normalize-repeat-style/-/postcss-normalize-repeat-style-5.1.1.tgz
Source48: https://registry.npmjs.org/postcss-normalize-string/-/postcss-normalize-string-5.1.0.tgz
Source49: https://registry.npmjs.org/postcss-normalize-timing-functions/-/postcss-normalize-timing-functions-5.1.0.tgz
Source50: https://registry.npmjs.org/postcss-normalize-unicode/-/postcss-normalize-unicode-5.1.1.tgz
Source51: https://registry.npmjs.org/postcss-normalize-url/-/postcss-normalize-url-5.1.0.tgz
Source52: https://registry.npmjs.org/postcss-normalize-whitespace/-/postcss-normalize-whitespace-5.1.1.tgz
Source53: https://registry.npmjs.org/postcss-ordered-values/-/postcss-ordered-values-5.1.3.tgz
Source54: https://registry.npmjs.org/postcss-reduce-initial/-/postcss-reduce-initial-5.1.2.tgz
Source55: https://registry.npmjs.org/postcss-reduce-transforms/-/postcss-reduce-transforms-5.1.0.tgz
Source56: https://registry.npmjs.org/postcss-selector-parser/-/postcss-selector-parser-6.0.13.tgz
Source57: https://registry.npmjs.org/postcss-svgo/-/postcss-svgo-5.1.0.tgz
Source58: https://registry.npmjs.org/postcss-unique-selectors/-/postcss-unique-selectors-5.1.1.tgz
Source59: https://registry.npmjs.org/postcss-value-parser/-/postcss-value-parser-4.2.0.tgz
Source60: https://registry.npmjs.org/source-map/-/source-map-0.6.1.tgz
Source61: https://registry.npmjs.org/stable/-/stable-0.1.8.tgz
Source62: https://registry.npmjs.org/stylehacks/-/stylehacks-5.1.1.tgz
Source63: https://registry.npmjs.org/svgo/-/svgo-2.8.0.tgz
Source64: https://registry.npmjs.org/update-browserslist-db/-/update-browserslist-db-1.0.13.tgz
Source65: https://registry.npmjs.org/util-deprecate/-/util-deprecate-1.0.2.tgz
Source66: https://registry.npmjs.org/yaml/-/yaml-1.10.2.tgz
Source67: nodejs-cssnano-%{version}-registry.npmjs.org.tgz
BuildRequires: %{?scl_prefix_nodejs}npm
%if 0%{!?scl:1}
BuildRequires: nodejs-packaging
%endif
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}
Provides: bundled(npm(@trysound/sax)) = 0.2.0
Provides: bundled(npm(boolbase)) = 1.0.0
Provides: bundled(npm(browserslist)) = 4.22.2
Provides: bundled(npm(caniuse-api)) = 3.0.0
Provides: bundled(npm(caniuse-lite)) = 1.0.30001570
Provides: bundled(npm(colord)) = 2.9.3
Provides: bundled(npm(commander)) = 7.2.0
Provides: bundled(npm(css-declaration-sorter)) = 6.4.1
Provides: bundled(npm(css-select)) = 4.3.0
Provides: bundled(npm(css-tree)) = 1.1.3
Provides: bundled(npm(css-what)) = 6.1.0
Provides: bundled(npm(cssesc)) = 3.0.0
Provides: bundled(npm(cssnano)) = 5.1.15
Provides: bundled(npm(cssnano-preset-default)) = 5.2.14
Provides: bundled(npm(cssnano-utils)) = 3.1.0
Provides: bundled(npm(csso)) = 4.2.0
Provides: bundled(npm(dom-serializer)) = 1.4.1
Provides: bundled(npm(domelementtype)) = 2.3.0
Provides: bundled(npm(domhandler)) = 4.3.1
Provides: bundled(npm(domutils)) = 2.8.0
Provides: bundled(npm(electron-to-chromium)) = 1.4.611
Provides: bundled(npm(entities)) = 2.2.0
Provides: bundled(npm(escalade)) = 3.1.1
Provides: bundled(npm(lilconfig)) = 2.1.0
Provides: bundled(npm(lodash.memoize)) = 4.1.2
Provides: bundled(npm(lodash.uniq)) = 4.5.0
Provides: bundled(npm(mdn-data)) = 2.0.14
Provides: bundled(npm(node-releases)) = 2.0.14
Provides: bundled(npm(normalize-url)) = 6.1.0
Provides: bundled(npm(nth-check)) = 2.1.1
Provides: bundled(npm(picocolors)) = 1.0.0
Provides: bundled(npm(postcss-calc)) = 8.2.4
Provides: bundled(npm(postcss-colormin)) = 5.3.1
Provides: bundled(npm(postcss-convert-values)) = 5.1.3
Provides: bundled(npm(postcss-discard-comments)) = 5.1.2
Provides: bundled(npm(postcss-discard-duplicates)) = 5.1.0
Provides: bundled(npm(postcss-discard-empty)) = 5.1.1
Provides: bundled(npm(postcss-discard-overridden)) = 5.1.0
Provides: bundled(npm(postcss-merge-longhand)) = 5.1.7
Provides: bundled(npm(postcss-merge-rules)) = 5.1.4
Provides: bundled(npm(postcss-minify-font-values)) = 5.1.0
Provides: bundled(npm(postcss-minify-gradients)) = 5.1.1
Provides: bundled(npm(postcss-minify-params)) = 5.1.4
Provides: bundled(npm(postcss-minify-selectors)) = 5.2.1
Provides: bundled(npm(postcss-normalize-charset)) = 5.1.0
Provides: bundled(npm(postcss-normalize-display-values)) = 5.1.0
Provides: bundled(npm(postcss-normalize-positions)) = 5.1.1
Provides: bundled(npm(postcss-normalize-repeat-style)) = 5.1.1
Provides: bundled(npm(postcss-normalize-string)) = 5.1.0
Provides: bundled(npm(postcss-normalize-timing-functions)) = 5.1.0
Provides: bundled(npm(postcss-normalize-unicode)) = 5.1.1
Provides: bundled(npm(postcss-normalize-url)) = 5.1.0
Provides: bundled(npm(postcss-normalize-whitespace)) = 5.1.1
Provides: bundled(npm(postcss-ordered-values)) = 5.1.3
Provides: bundled(npm(postcss-reduce-initial)) = 5.1.2
Provides: bundled(npm(postcss-reduce-transforms)) = 5.1.0
Provides: bundled(npm(postcss-selector-parser)) = 6.0.13
Provides: bundled(npm(postcss-svgo)) = 5.1.0
Provides: bundled(npm(postcss-unique-selectors)) = 5.1.1
Provides: bundled(npm(postcss-value-parser)) = 4.2.0
Provides: bundled(npm(source-map)) = 0.6.1
Provides: bundled(npm(stable)) = 0.1.8
Provides: bundled(npm(stylehacks)) = 5.1.1
Provides: bundled(npm(svgo)) = 2.8.0
Provides: bundled(npm(update-browserslist-db)) = 1.0.13
Provides: bundled(npm(util-deprecate)) = 1.0.2
Provides: bundled(npm(yaml)) = 1.10.2
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

%setup -T -q -a 67 -D -n %{npm_cache_dir}

%build
%{?scl:scl enable %{?scl_nodejs} - << \end_of_scl}
npm install --cache-min Infinity --cache %{?scl:../}%{npm_cache_dir} --no-shrinkwrap --no-optional --global-style true %{npm_name}@%{version}
%{?scl:end_of_scl}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/src %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/types %{buildroot}%{nodejs_sitelib}/%{npm_name}

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%license node_modules/%{npm_name}/LICENSE-MIT
%doc node_modules/%{npm_name}/README.md

%changelog
* Wed Dec 13 2023 Evgeni Golov 5.1.15-1
- Update to 5.1.15

* Thu May 04 2023 Eric D. Helms <ericdhelms@gmail.com> 4.1.11-1
- Update to 4.1.11

* Wed Jun 02 2021 Amir Feferkuchen <afeferku@redhat.com> 4.1.10-1
- Add nodejs-cssnano generated by npm2rpm using the bundle strategy
