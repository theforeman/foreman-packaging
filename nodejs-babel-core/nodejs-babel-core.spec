%global npm_name babel-core

Name: nodejs-%{npm_name}
Version: 6.7.7
Release: 2%{?dist}
Summary: Babel compiler core
License: MIT
Group: Development/Libraries
URL: https://babeljs.io/
Source0: http://registry.npmjs.org/babel-core/-/babel-core-6.7.7.tgz
Source1: http://registry.npmjs.org/babel-messages/-/babel-messages-6.8.0.tgz
Source2: http://registry.npmjs.org/babel-traverse/-/babel-traverse-6.12.0.tgz
Source3: http://registry.npmjs.org/babel-code-frame/-/babel-code-frame-6.11.0.tgz
Source4: http://registry.npmjs.org/babel-template/-/babel-template-6.9.0.tgz
Source5: http://registry.npmjs.org/babel-helpers/-/babel-helpers-6.8.0.tgz
Source6: http://registry.npmjs.org/babel-register/-/babel-register-6.11.6.tgz
Source7: http://registry.npmjs.org/babel-runtime/-/babel-runtime-5.8.38.tgz
Source8: http://registry.npmjs.org/babylon/-/babylon-6.8.4.tgz
Source9: http://registry.npmjs.org/json5/-/json5-0.4.0.tgz
Source10: http://registry.npmjs.org/convert-source-map/-/convert-source-map-1.3.0.tgz
Source11: http://registry.npmjs.org/babel-generator/-/babel-generator-6.11.4.tgz
Source12: http://registry.npmjs.org/babel-types/-/babel-types-6.11.1.tgz
Source13: http://registry.npmjs.org/path-is-absolute/-/path-is-absolute-1.0.0.tgz
Source14: http://registry.npmjs.org/path-exists/-/path-exists-1.0.0.tgz
Source15: http://registry.npmjs.org/minimatch/-/minimatch-2.0.10.tgz
Source16: http://registry.npmjs.org/debug/-/debug-2.2.0.tgz
Source17: http://registry.npmjs.org/shebang-regex/-/shebang-regex-1.0.0.tgz
Source18: http://registry.npmjs.org/private/-/private-0.1.6.tgz
Source19: http://registry.npmjs.org/lodash/-/lodash-3.10.1.tgz
Source20: http://registry.npmjs.org/babel-runtime/-/babel-runtime-6.11.6.tgz
Source21: http://registry.npmjs.org/source-map/-/source-map-0.5.6.tgz
Source22: http://registry.npmjs.org/slash/-/slash-1.0.0.tgz
Source23: http://registry.npmjs.org/invariant/-/invariant-2.2.1.tgz
Source24: http://registry.npmjs.org/globals/-/globals-8.18.0.tgz
Source25: http://registry.npmjs.org/lodash/-/lodash-4.14.0.tgz
Source26: http://registry.npmjs.org/chalk/-/chalk-1.1.3.tgz
Source27: http://registry.npmjs.org/esutils/-/esutils-2.0.2.tgz
Source28: http://registry.npmjs.org/js-tokens/-/js-tokens-2.0.0.tgz
Source29: http://registry.npmjs.org/core-js/-/core-js-2.4.1.tgz
Source30: http://registry.npmjs.org/home-or-tmp/-/home-or-tmp-1.0.0.tgz
Source31: http://registry.npmjs.org/mkdirp/-/mkdirp-0.5.1.tgz
Source32: http://registry.npmjs.org/core-js/-/core-js-1.2.7.tgz
Source33: http://registry.npmjs.org/detect-indent/-/detect-indent-3.0.1.tgz
Source34: http://registry.npmjs.org/babel-core/-/babel-core-6.11.4.tgz
Source35: http://registry.npmjs.org/to-fast-properties/-/to-fast-properties-1.0.2.tgz
Source36: http://registry.npmjs.org/source-map-support/-/source-map-support-0.2.10.tgz
Source37: http://registry.npmjs.org/ms/-/ms-0.7.1.tgz
Source38: http://registry.npmjs.org/regenerator-runtime/-/regenerator-runtime-0.9.5.tgz
Source39: http://registry.npmjs.org/brace-expansion/-/brace-expansion-1.1.6.tgz
Source40: http://registry.npmjs.org/ansi-styles/-/ansi-styles-2.2.1.tgz
Source41: http://registry.npmjs.org/has-ansi/-/has-ansi-2.0.0.tgz
Source42: http://registry.npmjs.org/strip-ansi/-/strip-ansi-3.0.1.tgz
Source43: http://registry.npmjs.org/supports-color/-/supports-color-2.0.0.tgz
Source44: http://registry.npmjs.org/user-home/-/user-home-1.1.1.tgz
Source45: http://registry.npmjs.org/os-tmpdir/-/os-tmpdir-1.0.1.tgz
Source46: http://registry.npmjs.org/get-stdin/-/get-stdin-4.0.1.tgz
Source47: http://registry.npmjs.org/minimist/-/minimist-0.0.8.tgz
Source48: http://registry.npmjs.org/loose-envify/-/loose-envify-1.2.0.tgz
Source49: http://registry.npmjs.org/repeating/-/repeating-1.1.3.tgz
Source50: http://registry.npmjs.org/minimist/-/minimist-1.2.0.tgz
Source51: http://registry.npmjs.org/escape-string-regexp/-/escape-string-regexp-1.0.5.tgz
Source52: http://registry.npmjs.org/minimatch/-/minimatch-3.0.2.tgz
Source53: http://registry.npmjs.org/concat-map/-/concat-map-0.0.1.tgz
Source54: http://registry.npmjs.org/ansi-regex/-/ansi-regex-2.0.0.tgz
Source55: http://registry.npmjs.org/source-map/-/source-map-0.1.32.tgz
Source56: http://registry.npmjs.org/js-tokens/-/js-tokens-1.0.3.tgz
Source57: http://registry.npmjs.org/is-finite/-/is-finite-1.0.1.tgz
Source58: http://registry.npmjs.org/amdefine/-/amdefine-1.0.0.tgz
Source59: http://registry.npmjs.org/balanced-match/-/balanced-match-0.4.2.tgz
Source60: http://registry.npmjs.org/number-is-nan/-/number-is-nan-1.0.0.tgz
Source61: babel-core-6.7.7-registry.npmjs.org.tgz
Requires: nodejs(engine)
BuildRequires: nodejs-devel
BuildRequires: nodejs-packaging
BuildRequires: npm
BuildArch: noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif
Provides: npm(%{npm_name}) = %{version}
Provides: bundled-npm(babel-core) = 6.7.7
Provides: bundled-npm(babel-messages) = 6.8.0
Provides: bundled-npm(babel-traverse) = 6.12.0
Provides: bundled-npm(babel-code-frame) = 6.11.0
Provides: bundled-npm(babel-template) = 6.9.0
Provides: bundled-npm(babel-helpers) = 6.8.0
Provides: bundled-npm(babel-register) = 6.11.6
Provides: bundled-npm(babel-runtime) = 5.8.38
Provides: bundled-npm(babylon) = 6.8.4
Provides: bundled-npm(json5) = 0.4.0
Provides: bundled-npm(convert-source-map) = 1.3.0
Provides: bundled-npm(babel-generator) = 6.11.4
Provides: bundled-npm(babel-types) = 6.11.1
Provides: bundled-npm(path-is-absolute) = 1.0.0
Provides: bundled-npm(path-exists) = 1.0.0
Provides: bundled-npm(minimatch) = 2.0.10
Provides: bundled-npm(debug) = 2.2.0
Provides: bundled-npm(shebang-regex) = 1.0.0
Provides: bundled-npm(private) = 0.1.6
Provides: bundled-npm(lodash) = 3.10.1
Provides: bundled-npm(babel-runtime) = 6.11.6
Provides: bundled-npm(source-map) = 0.5.6
Provides: bundled-npm(slash) = 1.0.0
Provides: bundled-npm(invariant) = 2.2.1
Provides: bundled-npm(globals) = 8.18.0
Provides: bundled-npm(lodash) = 4.14.0
Provides: bundled-npm(chalk) = 1.1.3
Provides: bundled-npm(esutils) = 2.0.2
Provides: bundled-npm(js-tokens) = 2.0.0
Provides: bundled-npm(core-js) = 2.4.1
Provides: bundled-npm(home-or-tmp) = 1.0.0
Provides: bundled-npm(mkdirp) = 0.5.1
Provides: bundled-npm(core-js) = 1.2.7
Provides: bundled-npm(detect-indent) = 3.0.1
Provides: bundled-npm(babel-core) = 6.11.4
Provides: bundled-npm(to-fast-properties) = 1.0.2
Provides: bundled-npm(source-map-support) = 0.2.10
Provides: bundled-npm(ms) = 0.7.1
Provides: bundled-npm(regenerator-runtime) = 0.9.5
Provides: bundled-npm(brace-expansion) = 1.1.6
Provides: bundled-npm(ansi-styles) = 2.2.1
Provides: bundled-npm(has-ansi) = 2.0.0
Provides: bundled-npm(strip-ansi) = 3.0.1
Provides: bundled-npm(supports-color) = 2.0.0
Provides: bundled-npm(user-home) = 1.1.1
Provides: bundled-npm(os-tmpdir) = 1.0.1
Provides: bundled-npm(get-stdin) = 4.0.1
Provides: bundled-npm(minimist) = 0.0.8
Provides: bundled-npm(loose-envify) = 1.2.0
Provides: bundled-npm(repeating) = 1.1.3
Provides: bundled-npm(minimist) = 1.2.0
Provides: bundled-npm(escape-string-regexp) = 1.0.5
Provides: bundled-npm(minimatch) = 3.0.2
Provides: bundled-npm(concat-map) = 0.0.1
Provides: bundled-npm(ansi-regex) = 2.0.0
Provides: bundled-npm(source-map) = 0.1.32
Provides: bundled-npm(js-tokens) = 1.0.3
Provides: bundled-npm(is-finite) = 1.0.1
Provides: bundled-npm(amdefine) = 1.0.0
Provides: bundled-npm(balanced-match) = 0.4.2
Provides: bundled-npm(number-is-nan) = 1.0.0
AutoReq: no
AutoProv: no


%description
Babel compiler core.

%package doc
Summary: Documentation for nodejs-%{npm_name}
Group: Documentation
Requires: nodejs-%{npm_name} = %{version}-%{release}
BuildArch: noarch

%description doc
This package contains documentation for nodejs-%{npm_name}

%prep
mkdir npm_cache
for tgz in %{sources}; do
  echo $tgz | grep -q registry.npmjs.org || npm cache add --cache ./npm_cache $tgz
done

%setup -T -q -a 61 -D -n npm_cache

%build
npm install %{npm_name}@%{version} --cache-min Infinity --cache .

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cd node_modules/babel-core
cp -pfr README.md ../../
cp -pfr index.js lib package.json register.js node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}

%check

%files
%{nodejs_sitelib}/%{npm_name}

%files doc
%doc README.md

%changelog
* Sat Sep 24 2016 Eric D Helms <ericdhelms@gmail.com> 6.7.7-2
- 

* Thu Aug 11 2016 Dominic Cleal <dominic@cleal.org> 6.7.7-1
- new package built with tito

