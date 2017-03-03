%global npm_name node-gyp

%{?nodejs_find_provides_and_requires}

Name: nodejs-%{npm_name}
Version: 3.3.1
Release: 1%{?dist}
Summary: Node
License: MIT
URL: https://github.com/nodejs/node-gyp
Source0: http://registry.npmjs.org/node-gyp/-/node-gyp-3.3.1.tgz
Source1: http://registry.npmjs.org/graceful-fs/-/graceful-fs-4.1.11.tgz
Source2: http://registry.npmjs.org/fstream/-/fstream-1.0.10.tgz
Source3: http://registry.npmjs.org/minimatch/-/minimatch-1.0.0.tgz
Source4: http://registry.npmjs.org/nopt/-/nopt-3.0.6.tgz
Source5: http://registry.npmjs.org/glob/-/glob-4.5.3.tgz
Source6: http://registry.npmjs.org/path-array/-/path-array-1.0.1.tgz
Source7: http://registry.npmjs.org/semver/-/semver-5.3.0.tgz
Source8: http://registry.npmjs.org/rimraf/-/rimraf-2.6.1.tgz
Source9: http://registry.npmjs.org/tar/-/tar-2.2.1.tgz
Source10: http://registry.npmjs.org/osenv/-/osenv-0.1.4.tgz
Source11: http://registry.npmjs.org/which/-/which-1.2.12.tgz
Source12: http://registry.npmjs.org/inherits/-/inherits-2.0.3.tgz
Source13: http://registry.npmjs.org/mkdirp/-/mkdirp-0.5.1.tgz
Source14: http://registry.npmjs.org/npmlog/-/npmlog-2.0.4.tgz
Source15: http://registry.npmjs.org/abbrev/-/abbrev-1.1.0.tgz
Source16: http://registry.npmjs.org/lru-cache/-/lru-cache-2.7.3.tgz
Source17: http://registry.npmjs.org/inflight/-/inflight-1.0.6.tgz
Source18: http://registry.npmjs.org/sigmund/-/sigmund-1.0.1.tgz
Source19: http://registry.npmjs.org/once/-/once-1.4.0.tgz
Source20: http://registry.npmjs.org/request/-/request-2.79.0.tgz
Source21: http://registry.npmjs.org/minimatch/-/minimatch-2.0.10.tgz
Source22: http://registry.npmjs.org/block-stream/-/block-stream-0.0.9.tgz
Source23: http://registry.npmjs.org/array-index/-/array-index-1.0.0.tgz
Source24: http://registry.npmjs.org/os-homedir/-/os-homedir-1.0.2.tgz
Source25: http://registry.npmjs.org/isexe/-/isexe-1.1.2.tgz
Source26: http://registry.npmjs.org/os-tmpdir/-/os-tmpdir-1.0.2.tgz
Source27: http://registry.npmjs.org/glob/-/glob-7.1.1.tgz
Source28: http://registry.npmjs.org/minimist/-/minimist-0.0.8.tgz
Source29: http://registry.npmjs.org/ansi/-/ansi-0.3.1.tgz
Source30: http://registry.npmjs.org/are-we-there-yet/-/are-we-there-yet-1.1.2.tgz
Source31: http://registry.npmjs.org/wrappy/-/wrappy-1.0.2.tgz
Source32: http://registry.npmjs.org/aws-sign2/-/aws-sign2-0.6.0.tgz
Source33: http://registry.npmjs.org/gauge/-/gauge-1.2.7.tgz
Source34: http://registry.npmjs.org/forever-agent/-/forever-agent-0.6.1.tgz
Source35: http://registry.npmjs.org/extend/-/extend-3.0.0.tgz
Source36: http://registry.npmjs.org/caseless/-/caseless-0.11.0.tgz
Source37: http://registry.npmjs.org/combined-stream/-/combined-stream-1.0.5.tgz
Source38: http://registry.npmjs.org/form-data/-/form-data-2.1.2.tgz
Source39: http://registry.npmjs.org/har-validator/-/har-validator-2.0.6.tgz
Source40: http://registry.npmjs.org/isstream/-/isstream-0.1.2.tgz
Source41: http://registry.npmjs.org/is-typedarray/-/is-typedarray-1.0.0.tgz
Source42: http://registry.npmjs.org/hawk/-/hawk-3.1.3.tgz
Source43: http://registry.npmjs.org/http-signature/-/http-signature-1.1.1.tgz
Source44: http://registry.npmjs.org/json-stringify-safe/-/json-stringify-safe-5.0.1.tgz
Source45: http://registry.npmjs.org/oauth-sign/-/oauth-sign-0.8.2.tgz
Source46: http://registry.npmjs.org/stringstream/-/stringstream-0.0.5.tgz
Source47: http://registry.npmjs.org/mime-types/-/mime-types-2.1.14.tgz
Source48: http://registry.npmjs.org/tunnel-agent/-/tunnel-agent-0.4.3.tgz
Source49: http://registry.npmjs.org/qs/-/qs-6.3.1.tgz
Source50: http://registry.npmjs.org/uuid/-/uuid-3.0.1.tgz
Source51: http://registry.npmjs.org/brace-expansion/-/brace-expansion-1.1.6.tgz
Source52: http://registry.npmjs.org/tough-cookie/-/tough-cookie-2.3.2.tgz
Source53: http://registry.npmjs.org/debug/-/debug-2.6.1.tgz
Source54: http://registry.npmjs.org/aws4/-/aws4-1.6.0.tgz
Source55: http://registry.npmjs.org/fs.realpath/-/fs.realpath-1.0.0.tgz
Source56: http://registry.npmjs.org/es6-symbol/-/es6-symbol-3.1.0.tgz
Source57: http://registry.npmjs.org/minimatch/-/minimatch-3.0.3.tgz
Source58: http://registry.npmjs.org/path-is-absolute/-/path-is-absolute-1.0.1.tgz
Source59: http://registry.npmjs.org/has-unicode/-/has-unicode-2.0.1.tgz
Source60: http://registry.npmjs.org/delegates/-/delegates-1.0.0.tgz
Source61: http://registry.npmjs.org/lodash.pad/-/lodash.pad-4.5.1.tgz
Source62: http://registry.npmjs.org/lodash.padend/-/lodash.padend-4.6.1.tgz
Source63: http://registry.npmjs.org/readable-stream/-/readable-stream-2.2.3.tgz
Source64: http://registry.npmjs.org/delayed-stream/-/delayed-stream-1.0.0.tgz
Source65: http://registry.npmjs.org/asynckit/-/asynckit-0.4.0.tgz
Source66: http://registry.npmjs.org/lodash.padstart/-/lodash.padstart-4.6.1.tgz
Source67: http://registry.npmjs.org/chalk/-/chalk-1.1.3.tgz
Source68: http://registry.npmjs.org/pinkie-promise/-/pinkie-promise-2.0.1.tgz
Source69: http://registry.npmjs.org/commander/-/commander-2.9.0.tgz
Source70: http://registry.npmjs.org/is-my-json-valid/-/is-my-json-valid-2.16.0.tgz
Source71: http://registry.npmjs.org/cryptiles/-/cryptiles-2.0.5.tgz
Source72: http://registry.npmjs.org/hoek/-/hoek-2.16.3.tgz
Source73: http://registry.npmjs.org/boom/-/boom-2.10.1.tgz
Source74: http://registry.npmjs.org/sntp/-/sntp-1.0.9.tgz
Source75: http://registry.npmjs.org/assert-plus/-/assert-plus-0.2.0.tgz
Source76: http://registry.npmjs.org/jsprim/-/jsprim-1.3.1.tgz
Source77: http://registry.npmjs.org/concat-map/-/concat-map-0.0.1.tgz
Source78: http://registry.npmjs.org/balanced-match/-/balanced-match-0.4.2.tgz
Source79: http://registry.npmjs.org/mime-db/-/mime-db-1.26.0.tgz
Source80: http://registry.npmjs.org/punycode/-/punycode-1.4.1.tgz
Source81: http://registry.npmjs.org/ms/-/ms-0.7.2.tgz
Source82: http://registry.npmjs.org/d/-/d-0.1.1.tgz
Source83: http://registry.npmjs.org/core-util-is/-/core-util-is-1.0.2.tgz
Source84: http://registry.npmjs.org/isarray/-/isarray-1.0.0.tgz
Source85: http://registry.npmjs.org/buffer-shims/-/buffer-shims-1.0.0.tgz
Source86: http://registry.npmjs.org/es5-ext/-/es5-ext-0.10.12.tgz
Source87: http://registry.npmjs.org/process-nextick-args/-/process-nextick-args-1.0.7.tgz
Source88: http://registry.npmjs.org/sshpk/-/sshpk-1.11.0.tgz
Source89: http://registry.npmjs.org/string_decoder/-/string_decoder-0.10.31.tgz
Source90: http://registry.npmjs.org/util-deprecate/-/util-deprecate-1.0.2.tgz
Source91: http://registry.npmjs.org/escape-string-regexp/-/escape-string-regexp-1.0.5.tgz
Source92: http://registry.npmjs.org/ansi-styles/-/ansi-styles-2.2.1.tgz
Source93: http://registry.npmjs.org/has-ansi/-/has-ansi-2.0.0.tgz
Source94: http://registry.npmjs.org/strip-ansi/-/strip-ansi-3.0.1.tgz
Source95: http://registry.npmjs.org/graceful-readlink/-/graceful-readlink-1.0.1.tgz
Source96: http://registry.npmjs.org/pinkie/-/pinkie-2.0.4.tgz
Source97: http://registry.npmjs.org/generate-object-property/-/generate-object-property-1.2.0.tgz
Source98: http://registry.npmjs.org/generate-function/-/generate-function-2.0.0.tgz
Source99: http://registry.npmjs.org/supports-color/-/supports-color-2.0.0.tgz
Source100: http://registry.npmjs.org/jsonpointer/-/jsonpointer-4.0.1.tgz
Source101: http://registry.npmjs.org/xtend/-/xtend-4.0.1.tgz
Source102: http://registry.npmjs.org/extsprintf/-/extsprintf-1.0.2.tgz
Source103: http://registry.npmjs.org/json-schema/-/json-schema-0.2.3.tgz
Source104: http://registry.npmjs.org/verror/-/verror-1.3.6.tgz
Source105: http://registry.npmjs.org/es6-iterator/-/es6-iterator-2.0.0.tgz
Source106: http://registry.npmjs.org/asn1/-/asn1-0.2.3.tgz
Source107: http://registry.npmjs.org/assert-plus/-/assert-plus-1.0.0.tgz
Source108: http://registry.npmjs.org/getpass/-/getpass-0.1.6.tgz
Source109: http://registry.npmjs.org/jsbn/-/jsbn-0.1.1.tgz
Source110: http://registry.npmjs.org/jodid25519/-/jodid25519-1.0.2.tgz
Source111: http://registry.npmjs.org/ecc-jsbn/-/ecc-jsbn-0.1.1.tgz
Source112: http://registry.npmjs.org/dashdash/-/dashdash-1.14.1.tgz
Source113: http://registry.npmjs.org/ansi-regex/-/ansi-regex-2.1.1.tgz
Source114: http://registry.npmjs.org/bcrypt-pbkdf/-/bcrypt-pbkdf-1.0.1.tgz
Source115: http://registry.npmjs.org/tweetnacl/-/tweetnacl-0.14.5.tgz
Source116: http://registry.npmjs.org/is-property/-/is-property-1.0.2.tgz
Source117: node-gyp-3.3.1-registry.npmjs.org.tgz
Source118: addon-rpm.gypi
# use RPM installed headers by default instead of downloading a source tree
# for the currently running node version
Patch1: node-gyp-addon-gypi.patch
Requires: nodejs(engine)
# this is the standard set of headers expected to build any node native module
Requires: nodejs-devel libuv-devel http-parser-devel
# we also need a C++ compiler to actually build stuff ;-)
Requires: gcc-c++
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
Provides: bundled(gyp)
Provides: bundled-npm(fstream) = 1.0.10
Provides: bundled-npm(minimatch) = 1.0.0
Provides: bundled-npm(nopt) = 3.0.6
Provides: bundled-npm(glob) = 4.5.3
Provides: bundled-npm(path-array) = 1.0.1
Provides: bundled-npm(semver) = 5.3.0
Provides: bundled-npm(rimraf) = 2.6.1
Provides: bundled-npm(tar) = 2.2.1
Provides: bundled-npm(osenv) = 0.1.4
Provides: bundled-npm(which) = 1.2.12
Provides: bundled-npm(inherits) = 2.0.3
Provides: bundled-npm(mkdirp) = 0.5.1
Provides: bundled-npm(npmlog) = 2.0.4
Provides: bundled-npm(abbrev) = 1.1.0
Provides: bundled-npm(lru-cache) = 2.7.3
Provides: bundled-npm(inflight) = 1.0.6
Provides: bundled-npm(sigmund) = 1.0.1
Provides: bundled-npm(once) = 1.4.0
Provides: bundled-npm(request) = 2.79.0
Provides: bundled-npm(minimatch) = 2.0.10
Provides: bundled-npm(block-stream) = 0.0.9
Provides: bundled-npm(array-index) = 1.0.0
Provides: bundled-npm(os-homedir) = 1.0.2
Provides: bundled-npm(isexe) = 1.1.2
Provides: bundled-npm(os-tmpdir) = 1.0.2
Provides: bundled-npm(glob) = 7.1.1
Provides: bundled-npm(minimist) = 0.0.8
Provides: bundled-npm(ansi) = 0.3.1
Provides: bundled-npm(are-we-there-yet) = 1.1.2
Provides: bundled-npm(wrappy) = 1.0.2
Provides: bundled-npm(aws-sign2) = 0.6.0
Provides: bundled-npm(gauge) = 1.2.7
Provides: bundled-npm(forever-agent) = 0.6.1
Provides: bundled-npm(extend) = 3.0.0
Provides: bundled-npm(caseless) = 0.11.0
Provides: bundled-npm(combined-stream) = 1.0.5
Provides: bundled-npm(form-data) = 2.1.2
Provides: bundled-npm(har-validator) = 2.0.6
Provides: bundled-npm(isstream) = 0.1.2
Provides: bundled-npm(is-typedarray) = 1.0.0
Provides: bundled-npm(hawk) = 3.1.3
Provides: bundled-npm(http-signature) = 1.1.1
Provides: bundled-npm(json-stringify-safe) = 5.0.1
Provides: bundled-npm(oauth-sign) = 0.8.2
Provides: bundled-npm(stringstream) = 0.0.5
Provides: bundled-npm(mime-types) = 2.1.14
Provides: bundled-npm(tunnel-agent) = 0.4.3
Provides: bundled-npm(qs) = 6.3.1
Provides: bundled-npm(uuid) = 3.0.1
Provides: bundled-npm(brace-expansion) = 1.1.6
Provides: bundled-npm(tough-cookie) = 2.3.2
Provides: bundled-npm(debug) = 2.6.1
Provides: bundled-npm(aws4) = 1.6.0
Provides: bundled-npm(fs.realpath) = 1.0.0
Provides: bundled-npm(es6-symbol) = 3.1.0
Provides: bundled-npm(minimatch) = 3.0.3
Provides: bundled-npm(path-is-absolute) = 1.0.1
Provides: bundled-npm(has-unicode) = 2.0.1
Provides: bundled-npm(delegates) = 1.0.0
Provides: bundled-npm(lodash.pad) = 4.5.1
Provides: bundled-npm(lodash.padend) = 4.6.1
Provides: bundled-npm(readable-stream) = 2.2.3
Provides: bundled-npm(delayed-stream) = 1.0.0
Provides: bundled-npm(asynckit) = 0.4.0
Provides: bundled-npm(lodash.padstart) = 4.6.1
Provides: bundled-npm(chalk) = 1.1.3
Provides: bundled-npm(pinkie-promise) = 2.0.1
Provides: bundled-npm(commander) = 2.9.0
Provides: bundled-npm(is-my-json-valid) = 2.16.0
Provides: bundled-npm(cryptiles) = 2.0.5
Provides: bundled-npm(hoek) = 2.16.3
Provides: bundled-npm(boom) = 2.10.1
Provides: bundled-npm(sntp) = 1.0.9
Provides: bundled-npm(assert-plus) = 0.2.0
Provides: bundled-npm(jsprim) = 1.3.1
Provides: bundled-npm(concat-map) = 0.0.1
Provides: bundled-npm(balanced-match) = 0.4.2
Provides: bundled-npm(mime-db) = 1.26.0
Provides: bundled-npm(punycode) = 1.4.1
Provides: bundled-npm(ms) = 0.7.2
Provides: bundled-npm(d) = 0.1.1
Provides: bundled-npm(core-util-is) = 1.0.2
Provides: bundled-npm(isarray) = 1.0.0
Provides: bundled-npm(buffer-shims) = 1.0.0
Provides: bundled-npm(es5-ext) = 0.10.12
Provides: bundled-npm(process-nextick-args) = 1.0.7
Provides: bundled-npm(sshpk) = 1.11.0
Provides: bundled-npm(string_decoder) = 0.10.31
Provides: bundled-npm(util-deprecate) = 1.0.2
Provides: bundled-npm(escape-string-regexp) = 1.0.5
Provides: bundled-npm(ansi-styles) = 2.2.1
Provides: bundled-npm(has-ansi) = 2.0.0
Provides: bundled-npm(strip-ansi) = 3.0.1
Provides: bundled-npm(graceful-readlink) = 1.0.1
Provides: bundled-npm(pinkie) = 2.0.4
Provides: bundled-npm(generate-object-property) = 1.2.0
Provides: bundled-npm(generate-function) = 2.0.0
Provides: bundled-npm(supports-color) = 2.0.0
Provides: bundled-npm(jsonpointer) = 4.0.1
Provides: bundled-npm(xtend) = 4.0.1
Provides: bundled-npm(extsprintf) = 1.0.2
Provides: bundled-npm(json-schema) = 0.2.3
Provides: bundled-npm(verror) = 1.3.6
Provides: bundled-npm(es6-iterator) = 2.0.0
Provides: bundled-npm(asn1) = 0.2.3
Provides: bundled-npm(assert-plus) = 1.0.0
Provides: bundled-npm(getpass) = 0.1.6
Provides: bundled-npm(jsbn) = 0.1.1
Provides: bundled-npm(jodid25519) = 1.0.2
Provides: bundled-npm(ecc-jsbn) = 0.1.1
Provides: bundled-npm(dashdash) = 1.14.1
Provides: bundled-npm(ansi-regex) = 2.1.1
Provides: bundled-npm(bcrypt-pbkdf) = 1.0.1
Provides: bundled-npm(tweetnacl) = 0.14.5
Provides: bundled-npm(is-property) = 1.0.2
AutoReq: no
AutoProv: no


%description
%{summary}

%prep
mkdir npm_cache
for tgz in %{sources}; do
  echo $tgz | egrep -q "registry.npmjs.org|\.gypi" || npm cache add --cache ./npm_cache $tgz
done

%setup -T -q -a 117 -D -n npm_cache

%build
npm install --cache-min Infinity --cache . --no-optional --global-style true %{npm_name}@%{version}

pushd node_modules/%{npm_name}
%__patch -p1 < %PATCH1
popd

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cd node_modules/node-gyp
cp -pfr .jshintrc .npmignore CHANGELOG.md History.md LICENSE README.md addon.gypi bin gyp lib package.json src test node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -p %{SOURCE118} %{buildroot}%{nodejs_sitelib}/node-gyp/addon-rpm.gypi
cp -pf CHANGELOG.md History.md LICENSE README.md ../../
# If any binaries are included, symlink them to bindir here
mkdir -p %{buildroot}%{nodejs_sitelib}/${npm_name}/bin
mkdir -p %{buildroot}%{_bindir}/
install -p -D -m0755 bin/node-gyp.js %{buildroot}%{nodejs_sitelib}/%{npm_name}/bin/node-gyp.js
ln -sf %{nodejs_sitelib}/%{npm_name}/bin/node-gyp.js %{buildroot}%{_bindir}/node-gyp.js

%files
%{nodejs_sitelib}/%{npm_name}
%{_bindir}/node-gyp.js
%license LICENSE
%doc CHANGELOG.md
%doc History.md
%doc README.md

%changelog
* Fri Mar 03 2017 Dominic Cleal <dominic@cleal.org> 3.3.1-1
- Update node-gyp to 3.3.1 (dominic@cleal.org)

* Thu Mar 02 2017 Dominic Cleal <dominic@cleal.org> 3.2.1-1
- new package built with tito

