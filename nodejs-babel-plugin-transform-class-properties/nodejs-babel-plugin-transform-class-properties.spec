%global npm_name babel-plugin-transform-class-properties
%global enable_tests 0

Name: nodejs-%{npm_name}
Version: 6.24.1
Release: 1%{?dist}
Summary: This plugin transforms static class properties as well as properties declared with the property initializer syntax
License: MIT
URL: https://github.com/babel/babel/tree/master/packages/babel-plugin-proposal-class-properties
Source0: http://registry.npmjs.org/babel-plugin-transform-class-properties/-/babel-plugin-transform-class-properties-6.24.1.tgz
Source1: http://registry.npmjs.org/babel-template/-/babel-template-6.26.0.tgz
Source2: http://registry.npmjs.org/babel-traverse/-/babel-traverse-6.26.0.tgz
Source3: http://registry.npmjs.org/babel-types/-/babel-types-6.26.0.tgz
Source4: http://registry.npmjs.org/lodash/-/lodash-4.17.4.tgz
Source5: http://registry.npmjs.org/babylon/-/babylon-6.18.0.tgz
Source6: http://registry.npmjs.org/babel-runtime/-/babel-runtime-6.26.0.tgz
Source7: http://registry.npmjs.org/babel-helper-function-name/-/babel-helper-function-name-6.24.1.tgz
Source8: http://registry.npmjs.org/babel-plugin-syntax-class-properties/-/babel-plugin-syntax-class-properties-6.13.0.tgz
Source9: http://registry.npmjs.org/globals/-/globals-9.18.0.tgz
Source10: http://registry.npmjs.org/babel-messages/-/babel-messages-6.23.0.tgz
Source11: http://registry.npmjs.org/debug/-/debug-2.6.9.tgz
Source12: http://registry.npmjs.org/invariant/-/invariant-2.2.2.tgz
Source13: http://registry.npmjs.org/to-fast-properties/-/to-fast-properties-1.0.3.tgz
Source14: http://registry.npmjs.org/esutils/-/esutils-2.0.2.tgz
Source15: http://registry.npmjs.org/regenerator-runtime/-/regenerator-runtime-0.11.0.tgz
Source16: http://registry.npmjs.org/babel-helper-get-function-arity/-/babel-helper-get-function-arity-6.24.1.tgz
Source17: http://registry.npmjs.org/babel-code-frame/-/babel-code-frame-6.26.0.tgz
Source18: http://registry.npmjs.org/loose-envify/-/loose-envify-1.3.1.tgz
Source19: http://registry.npmjs.org/ms/-/ms-2.0.0.tgz
Source20: http://registry.npmjs.org/core-js/-/core-js-2.5.1.tgz
Source21: http://registry.npmjs.org/js-tokens/-/js-tokens-3.0.2.tgz
Source22: http://registry.npmjs.org/chalk/-/chalk-1.1.3.tgz
Source23: http://registry.npmjs.org/escape-string-regexp/-/escape-string-regexp-1.0.5.tgz
Source24: http://registry.npmjs.org/strip-ansi/-/strip-ansi-3.0.1.tgz
Source25: http://registry.npmjs.org/has-ansi/-/has-ansi-2.0.0.tgz
Source26: http://registry.npmjs.org/supports-color/-/supports-color-2.0.0.tgz
Source27: http://registry.npmjs.org/ansi-styles/-/ansi-styles-2.2.1.tgz
Source28: http://registry.npmjs.org/ansi-regex/-/ansi-regex-2.1.1.tgz
Source29: babel-plugin-transform-class-properties-6.24.1-registry.npmjs.org.tgz
BuildRequires: nodejs-packaging
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: npm(%{npm_name}) = %{version}
Provides: bundled-npm(babel-plugin-transform-class-properties) = 6.24.1
Provides: bundled-npm(babel-template) = 6.26.0
Provides: bundled-npm(babel-traverse) = 6.26.0
Provides: bundled-npm(babel-types) = 6.26.0
Provides: bundled-npm(lodash) = 4.17.4
Provides: bundled-npm(babylon) = 6.18.0
Provides: bundled-npm(babel-runtime) = 6.26.0
Provides: bundled-npm(babel-helper-function-name) = 6.24.1
Provides: bundled-npm(babel-plugin-syntax-class-properties) = 6.13.0
Provides: bundled-npm(globals) = 9.18.0
Provides: bundled-npm(babel-messages) = 6.23.0
Provides: bundled-npm(debug) = 2.6.9
Provides: bundled-npm(invariant) = 2.2.2
Provides: bundled-npm(to-fast-properties) = 1.0.3
Provides: bundled-npm(esutils) = 2.0.2
Provides: bundled-npm(regenerator-runtime) = 0.11.0
Provides: bundled-npm(babel-helper-get-function-arity) = 6.24.1
Provides: bundled-npm(babel-code-frame) = 6.26.0
Provides: bundled-npm(loose-envify) = 1.3.1
Provides: bundled-npm(ms) = 2.0.0
Provides: bundled-npm(core-js) = 2.5.1
Provides: bundled-npm(js-tokens) = 3.0.2
Provides: bundled-npm(chalk) = 1.1.3
Provides: bundled-npm(escape-string-regexp) = 1.0.5
Provides: bundled-npm(strip-ansi) = 3.0.1
Provides: bundled-npm(has-ansi) = 2.0.0
Provides: bundled-npm(supports-color) = 2.0.0
Provides: bundled-npm(ansi-styles) = 2.2.1
Provides: bundled-npm(ansi-regex) = 2.1.1
AutoReq: no
AutoProv: no


%define npm_cache_dir /tmp/npm_cache_%{name}-%{version}-%{release}
%description
%{summary}

%prep
mkdir -p %{npm_cache_dir}
for tgz in %{sources}; do
  echo $tgz | grep -q registry.npmjs.org || npm cache add --cache %{npm_cache_dir} $tgz
done

%setup -T -q -a 29 -D -n %{npm_cache_dir}

%build
npm install --cache-min Infinity --cache %{npm_cache_dir} --no-optional --global-style true %{npm_name}@%{version}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cd node_modules/babel-plugin-transform-class-properties
cp -pfr .npmignore README.md lib package.json node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pf README.md  ../../

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%endif

%files
%{nodejs_sitelib}/%{npm_name}

%doc README.md

%changelog
* Tue Nov 07 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 6.24.1-1
- new package built with tito

