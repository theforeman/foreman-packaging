%global npm_name webpack

Name: nodejs-%{npm_name}
Version: 1.13.1
Release: 1%{?dist}
Summary: Packs CommonJs/AMD modules for the browser. Allows to split your codebase into multiple bundles, which can be loaded on demand. Support loaders to preprocess files, i.e. json, jade, coffee, css, less, ... and your custom stuff.
License: MIT
Group: Development/Libraries
URL: https://github.com/webpack/webpack.git
Source0: http://registry.npmjs.org/webpack/-/webpack-1.13.1.tgz
Requires: nodejs(engine)
BuildRequires: nodejs-devel
BuildRequires: nodejs-packaging
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch
Provides: npm(%{npm_name}) = %{version}
Provides: bundled-npm(package) = 1.13.1
Provides: bundled-npm(async) = 0.2.10
Provides: bundled-npm(uglify-js) = 2.6.4
Provides: bundled-npm(yargs) = 3.10.0
Provides: bundled-npm(optimist) = 0.6.1
Provides: bundled-npm(wordwrap) = 0.0.3
Provides: bundled-npm(window-size) = 0.1.0
Provides: bundled-npm(source-map) = 0.4.4
Provides: bundled-npm(webpack-core) = 0.6.8
Provides: bundled-npm(async) = 0.9.2
Provides: bundled-npm(watchpack) = 0.2.9
Provides: bundled-npm(readable-stream) = 1.1.14
Provides: bundled-npm(isarray) = 0.0.1
Provides: bundled-npm(node-libs-browser) = 0.5.3
Provides: bundled-npm(vm-browserify) = 0.0.4
Provides: bundled-npm(memory-fs) = 0.3.0
Provides: bundled-npm(chokidar) = 1.6.0
Provides: bundled-npm(readdirp) = 2.1.0
Provides: bundled-npm(examples) = 0.0.0
Provides: bundled-npm(readable-stream) = 2.1.4
Provides: bundled-npm(util-deprecate) = 1.0.2
Provides: bundled-npm(assert) = 1.4.1
Provides: bundled-npm(util) = 0.10.3
Provides: bundled-npm(punycode) = 1.3.2
Provides: bundled-npm(url) = 0.10.3
Provides: bundled-npm(uglify-to-browserify) = 1.0.2
Provides: bundled-npm(tty-browserify) = 0.0.0
Provides: bundled-npm(timers-browserify) = 1.4.2
Provides: bundled-npm(memory-fs) = 0.2.0
Provides: bundled-npm(enhanced-resolve) = 0.9.1
Provides: bundled-npm(tapable) = 0.1.10
Provides: bundled-npm(supports-color) = 3.1.2
Provides: bundled-npm(readable-stream) = 1.1.14
Provides: bundled-npm(isarray) = 0.0.1
Provides: bundled-npm(stream-browserify) = 1.0.0
Provides: bundled-npm(string_decoder) = 0.10.31
Provides: bundled-npm(source-map) = 0.5.6
Provides: bundled-npm(source-list-map) = 0.1.6
Provides: bundled-npm(crypto-browserify) = 3.2.8
Provides: bundled-npm(sha.js) = 2.2.6
Provides: bundled-npm(set-immediate-shim) = 1.0.1
Provides: bundled-npm(ripemd160) = 0.2.0
Provides: bundled-npm(wordwrap) = 0.0.2
Provides: bundled-npm(cliui) = 2.1.0
Provides: bundled-npm(right-align) = 0.1.3
Provides: bundled-npm(center-align) = 0.1.3
Provides: bundled-npm(align-text) = 0.1.4
Provides: bundled-npm(anymatch) = 1.3.0
Provides: bundled-npm(micromatch) = 2.3.10
Provides: bundled-npm(braces) = 1.8.5
Provides: bundled-npm(expand-range) = 1.8.2
Provides: bundled-npm(fill-range) = 2.2.3
Provides: bundled-npm(repeat-string) = 1.5.4
Provides: bundled-npm(repeat-element) = 1.1.2
Provides: bundled-npm(regex-cache) = 0.4.3
Provides: bundled-npm(randomatic) = 1.1.5
Provides: bundled-npm(querystring-es3) = 0.2.1
Provides: bundled-npm(querystring) = 0.2.0
Provides: bundled-npm(punycode) = 1.4.1
Provides: bundled-npm(errno) = 0.1.4
Provides: bundled-npm(prr) = 0.0.0
Provides: bundled-npm(process-nextick-args) = 1.0.7
Provides: bundled-npm(process) = 0.11.5
Provides: bundled-npm(preserve) = 0.2.0
Provides: bundled-npm(pbkdf2-compat) = 2.0.1
Provides: bundled-npm(path-is-absolute) = 1.0.0
Provides: bundled-npm(path-browserify) = 0.0.0
Provides: bundled-npm(parse-glob) = 3.0.4
Provides: bundled-npm(browserify-zlib) = 0.1.4
Provides: bundled-npm(pako) = 0.2.8
Provides: bundled-npm(os-browserify) = 0.1.2
Provides: bundled-npm(object.omit) = 2.0.0
Provides: bundled-npm(loader-utils) = 0.2.15
Provides: bundled-npm(object-assign) = 4.1.0
Provides: bundled-npm(normalize-path) = 2.0.1
Provides: bundled-npm(mkdirp) = 0.5.1
Provides: bundled-npm(minimist) = 0.0.8
Provides: bundled-npm(minimatch) = 3.0.2
Provides: bundled-npm(longest) = 1.0.1
Provides: bundled-npm(lazy-cache) = 1.0.4
Provides: bundled-npm(is-number) = 2.1.0
Provides: bundled-npm(kind-of) = 3.0.3
Provides: bundled-npm(json5) = 0.5.0
Provides: bundled-npm(isobject) = 2.1.0
Provides: bundled-npm(buffer) = 3.6.0
Provides: bundled-npm(isarray) = 1.0.0
Provides: bundled-npm(is-equal-shallow) = 0.1.3
Provides: bundled-npm(is-primitive) = 2.0.0
Provides: bundled-npm(expand-brackets) = 0.1.5
Provides: bundled-npm(is-posix-bracket) = 0.1.1
Provides: bundled-npm(glob-base) = 0.3.0
Provides: bundled-npm(glob-parent) = 2.0.0
Provides: bundled-npm(is-glob) = 2.0.1
Provides: bundled-npm(extglob) = 0.3.2
Provides: bundled-npm(is-extglob) = 1.0.0
Provides: bundled-npm(is-extendable) = 0.1.1
Provides: bundled-npm(is-dotfile) = 1.0.2
Provides: bundled-npm(is-buffer) = 1.1.3
Provides: bundled-npm(is-binary-path) = 1.0.1
Provides: bundled-npm(interpret) = 0.6.6
Provides: bundled-npm(http-browserify) = 1.7.0
Provides: bundled-npm(inherits) = 2.0.1
Provides: bundled-npm(indexof) = 0.0.1
Provides: bundled-npm(ieee754) = 1.1.6
Provides: bundled-npm(https-browserify) = 0.0.0
Provides: bundled-npm(has-flag) = 1.0.0
Provides: bundled-npm(graceful-fs) = 4.1.4
Provides: bundled-npm(for-own) = 0.1.4
Provides: bundled-npm(for-in) = 0.1.5
Provides: bundled-npm(filename-regex) = 2.0.0
Provides: bundled-npm(events) = 1.1.1
Provides: bundled-npm(emojis-list) = 2.0.1
Provides: bundled-npm(domain-browser) = 1.1.7
Provides: bundled-npm(decamelize) = 1.2.0
Provides: bundled-npm(console-browserify) = 1.1.0
Provides: bundled-npm(date-now) = 0.1.4
Provides: bundled-npm(core-util-is) = 1.0.2
Provides: bundled-npm(constants-browserify) = 0.0.1
Provides: bundled-npm(brace-expansion) = 1.1.5
Provides: bundled-npm(concat-map) = 0.0.1
Provides: bundled-npm(clone) = 1.0.2
Provides: bundled-npm(camelcase) = 1.2.1
Provides: bundled-npm(buffer-shims) = 1.0.0
Provides: bundled-npm(binary-extensions) = 1.5.0
Provides: bundled-npm(big.js) = 3.1.3
Provides: bundled-npm(base64-js) = 0.0.8
Provides: bundled-npm(balanced-match) = 0.4.1
Provides: bundled-npm(async-each) = 1.0.0
Provides: bundled-npm(async) = 1.5.2
Provides: bundled-npm(arrify) = 1.0.1
Provides: bundled-npm(array-unique) = 0.2.1
Provides: bundled-npm(arr-diff) = 2.0.0
Provides: bundled-npm(arr-flatten) = 1.0.1
Provides: bundled-npm(amdefine) = 1.0.0
Provides: bundled-npm(acorn) = 3.2.0
Provides: bundled-npm(Base64) = 0.2.1
Provides: npm(webpack) = 1.13.1

%description
Packs CommonJs/AMD modules for the browser. Allows to split your codebase into multiple bundles, which can be loaded on demand. Support loaders to preprocess files, i.e. json, jade, coffee, css, less, ... and your custom stuff.

%package doc
Summary: Documentation for nodejs-%{npm_name}
Group: Documentation
Requires: nodejs-%{npm_name} = %{version}-%{release}
BuildArch: noarch

%description doc
This package contains documentation for nodejs-%{npm_name}

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr bin buildin hot lib web_modules  *.json *.md node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
#if any binaries are included, symlink them to bindir here
mkdir -p %{buildroot}%{_bindir}
ln -s %{nodejs_sitelib}/webpack/bin/config-optimist.js %{buildroot}%{_bindir}/config-optimist.js
ln -s %{nodejs_sitelib}/webpack/bin/convert-argv.js %{buildroot}%{_bindir}/convert-argv.js
ln -s %{nodejs_sitelib}/webpack/bin/webpack.js %{buildroot}%{_bindir}/webpack.js

%files
%{nodejs_sitelib}/%{npm_name}
%{_bindir}/config-optimist.js
%{_bindir}/convert-argv.js
%{_bindir}/webpack.js
%doc README.md

%files doc
%doc LICENSE

%changelog
