%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name css-loader

Name: %{?scl_prefix}nodejs-css-loader
Version: 6.8.1
Release: 1%{?dist}
Summary: css loader module for webpack
License: MIT
Group: Development/Libraries
URL: https://github.com/webpack-contrib/css-loader
Source0: https://registry.npmjs.org/css-loader/-/css-loader-6.8.1.tgz
Source1: https://registry.npmjs.org/cssesc/-/cssesc-3.0.0.tgz
Source2: https://registry.npmjs.org/icss-utils/-/icss-utils-5.1.0.tgz
Source3: https://registry.npmjs.org/lru-cache/-/lru-cache-6.0.0.tgz
Source4: https://registry.npmjs.org/nanoid/-/nanoid-3.3.7.tgz
Source5: https://registry.npmjs.org/picocolors/-/picocolors-1.0.0.tgz
Source6: https://registry.npmjs.org/postcss/-/postcss-8.4.32.tgz
Source7: https://registry.npmjs.org/postcss-modules-extract-imports/-/postcss-modules-extract-imports-3.0.0.tgz
Source8: https://registry.npmjs.org/postcss-modules-local-by-default/-/postcss-modules-local-by-default-4.0.3.tgz
Source9: https://registry.npmjs.org/postcss-modules-scope/-/postcss-modules-scope-3.0.0.tgz
Source10: https://registry.npmjs.org/postcss-modules-values/-/postcss-modules-values-4.0.0.tgz
Source11: https://registry.npmjs.org/postcss-selector-parser/-/postcss-selector-parser-6.0.13.tgz
Source12: https://registry.npmjs.org/postcss-value-parser/-/postcss-value-parser-4.2.0.tgz
Source13: https://registry.npmjs.org/semver/-/semver-7.5.4.tgz
Source14: https://registry.npmjs.org/source-map-js/-/source-map-js-1.0.2.tgz
Source15: https://registry.npmjs.org/util-deprecate/-/util-deprecate-1.0.2.tgz
Source16: https://registry.npmjs.org/yallist/-/yallist-4.0.0.tgz
Source17: nodejs-css-loader-%{version}-registry.npmjs.org.tgz
BuildRequires: %{?scl_prefix_nodejs}npm
%if 0%{!?scl:1}
BuildRequires: nodejs-packaging
%endif
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}
Provides: bundled(npm(css-loader)) = 6.8.1
Provides: bundled(npm(cssesc)) = 3.0.0
Provides: bundled(npm(icss-utils)) = 5.1.0
Provides: bundled(npm(lru-cache)) = 6.0.0
Provides: bundled(npm(nanoid)) = 3.3.7
Provides: bundled(npm(picocolors)) = 1.0.0
Provides: bundled(npm(postcss)) = 8.4.32
Provides: bundled(npm(postcss-modules-extract-imports)) = 3.0.0
Provides: bundled(npm(postcss-modules-local-by-default)) = 4.0.3
Provides: bundled(npm(postcss-modules-scope)) = 3.0.0
Provides: bundled(npm(postcss-modules-values)) = 4.0.0
Provides: bundled(npm(postcss-selector-parser)) = 6.0.13
Provides: bundled(npm(postcss-value-parser)) = 4.2.0
Provides: bundled(npm(semver)) = 7.5.4
Provides: bundled(npm(source-map-js)) = 1.0.2
Provides: bundled(npm(util-deprecate)) = 1.0.2
Provides: bundled(npm(yallist)) = 4.0.0
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

%setup -T -q -a 17 -D -n %{npm_cache_dir}

%build
%{?scl:scl enable %{?scl_nodejs} - << \end_of_scl}
npm install --cache-min Infinity --cache %{?scl:../}%{npm_cache_dir} --no-shrinkwrap --no-optional --global-style true %{npm_name}@%{version}
%{?scl:end_of_scl}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/dist %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%license node_modules/%{npm_name}/LICENSE
%doc node_modules/%{npm_name}/README.md

%changelog
* Wed Dec 13 2023 Evgeni Golov 6.8.1-1
- Update to 6.8.1

* Tue Mar 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.23.1-5
- Bump packages to build for el8

* Mon Oct 21 2019 Eric D. Helms <ericdhelms@gmail.com> - 0.23.1-4
- Build for SCL

* Fri Oct 04 2019 Eric D. Helms <ericdhelms@gmail.com> - 0.23.1-3
- Update specs to handle SCL

* Thu Sep 01 2016 Dominic Cleal <dominic@cleal.org> 0.23.1-1
- new package built with tito
