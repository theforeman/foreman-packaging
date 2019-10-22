%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name node-gyp

Name: %{?scl_prefix}nodejs-node-gyp
Version: 3.3.1
Release: 4%{?dist}
Summary: Node
License: MIT
Group: Development/Libraries
URL: https://github.com/nodejs/node-gyp#readme
Source0: https://registry.npmjs.org/abbrev/-/abbrev-1.1.1.tgz
Source1: https://registry.npmjs.org/ajv/-/ajv-6.10.2.tgz
Source2: https://registry.npmjs.org/ansi/-/ansi-0.3.1.tgz
Source3: https://registry.npmjs.org/are-we-there-yet/-/are-we-there-yet-1.1.5.tgz
Source4: https://registry.npmjs.org/array-index/-/array-index-1.0.0.tgz
Source5: https://registry.npmjs.org/asn1/-/asn1-0.2.4.tgz
Source6: https://registry.npmjs.org/assert-plus/-/assert-plus-1.0.0.tgz
Source7: https://registry.npmjs.org/asynckit/-/asynckit-0.4.0.tgz
Source8: https://registry.npmjs.org/aws-sign2/-/aws-sign2-0.7.0.tgz
Source9: https://registry.npmjs.org/aws4/-/aws4-1.8.0.tgz
Source10: https://registry.npmjs.org/balanced-match/-/balanced-match-1.0.0.tgz
Source11: https://registry.npmjs.org/bcrypt-pbkdf/-/bcrypt-pbkdf-1.0.2.tgz
Source12: https://registry.npmjs.org/block-stream/-/block-stream-0.0.9.tgz
Source13: https://registry.npmjs.org/brace-expansion/-/brace-expansion-1.1.11.tgz
Source14: https://registry.npmjs.org/caseless/-/caseless-0.12.0.tgz
Source15: https://registry.npmjs.org/combined-stream/-/combined-stream-1.0.8.tgz
Source16: https://registry.npmjs.org/concat-map/-/concat-map-0.0.1.tgz
Source17: https://registry.npmjs.org/core-util-is/-/core-util-is-1.0.2.tgz
Source18: https://registry.npmjs.org/d/-/d-1.0.1.tgz
Source19: https://registry.npmjs.org/dashdash/-/dashdash-1.14.1.tgz
Source20: https://registry.npmjs.org/debug/-/debug-2.6.9.tgz
Source21: https://registry.npmjs.org/delayed-stream/-/delayed-stream-1.0.0.tgz
Source22: https://registry.npmjs.org/delegates/-/delegates-1.0.0.tgz
Source23: https://registry.npmjs.org/ecc-jsbn/-/ecc-jsbn-0.1.2.tgz
Source24: https://registry.npmjs.org/es5-ext/-/es5-ext-0.10.51.tgz
Source25: https://registry.npmjs.org/es6-iterator/-/es6-iterator-2.0.3.tgz
Source26: https://registry.npmjs.org/es6-symbol/-/es6-symbol-3.1.2.tgz
Source27: https://registry.npmjs.org/extend/-/extend-3.0.2.tgz
Source28: https://registry.npmjs.org/extsprintf/-/extsprintf-1.3.0.tgz
Source29: https://registry.npmjs.org/extsprintf/-/extsprintf-1.4.0.tgz
Source30: https://registry.npmjs.org/fast-deep-equal/-/fast-deep-equal-2.0.1.tgz
Source31: https://registry.npmjs.org/fast-json-stable-stringify/-/fast-json-stable-stringify-2.0.0.tgz
Source32: https://registry.npmjs.org/forever-agent/-/forever-agent-0.6.1.tgz
Source33: https://registry.npmjs.org/form-data/-/form-data-2.3.3.tgz
Source34: https://registry.npmjs.org/fs.realpath/-/fs.realpath-1.0.0.tgz
Source35: https://registry.npmjs.org/fstream/-/fstream-1.0.12.tgz
Source36: https://registry.npmjs.org/gauge/-/gauge-1.2.7.tgz
Source37: https://registry.npmjs.org/getpass/-/getpass-0.1.7.tgz
Source38: https://registry.npmjs.org/glob/-/glob-4.5.3.tgz
Source39: https://registry.npmjs.org/glob/-/glob-7.1.4.tgz
Source40: https://registry.npmjs.org/graceful-fs/-/graceful-fs-4.2.2.tgz
Source41: https://registry.npmjs.org/har-schema/-/har-schema-2.0.0.tgz
Source42: https://registry.npmjs.org/har-validator/-/har-validator-5.1.3.tgz
Source43: https://registry.npmjs.org/has-unicode/-/has-unicode-2.0.1.tgz
Source44: https://registry.npmjs.org/http-signature/-/http-signature-1.2.0.tgz
Source45: https://registry.npmjs.org/inflight/-/inflight-1.0.6.tgz
Source46: https://registry.npmjs.org/inherits/-/inherits-2.0.4.tgz
Source47: https://registry.npmjs.org/is-typedarray/-/is-typedarray-1.0.0.tgz
Source48: https://registry.npmjs.org/isarray/-/isarray-1.0.0.tgz
Source49: https://registry.npmjs.org/isexe/-/isexe-2.0.0.tgz
Source50: https://registry.npmjs.org/isstream/-/isstream-0.1.2.tgz
Source51: https://registry.npmjs.org/jsbn/-/jsbn-0.1.1.tgz
Source52: https://registry.npmjs.org/json-schema/-/json-schema-0.2.3.tgz
Source53: https://registry.npmjs.org/json-schema-traverse/-/json-schema-traverse-0.4.1.tgz
Source54: https://registry.npmjs.org/json-stringify-safe/-/json-stringify-safe-5.0.1.tgz
Source55: https://registry.npmjs.org/jsprim/-/jsprim-1.4.1.tgz
Source56: https://registry.npmjs.org/lodash.pad/-/lodash.pad-4.5.1.tgz
Source57: https://registry.npmjs.org/lodash.padend/-/lodash.padend-4.6.1.tgz
Source58: https://registry.npmjs.org/lodash.padstart/-/lodash.padstart-4.6.1.tgz
Source59: https://registry.npmjs.org/lru-cache/-/lru-cache-2.7.3.tgz
Source60: https://registry.npmjs.org/mime-db/-/mime-db-1.40.0.tgz
Source61: https://registry.npmjs.org/mime-types/-/mime-types-2.1.24.tgz
Source62: https://registry.npmjs.org/minimatch/-/minimatch-1.0.0.tgz
Source63: https://registry.npmjs.org/minimatch/-/minimatch-2.0.10.tgz
Source64: https://registry.npmjs.org/minimatch/-/minimatch-3.0.4.tgz
Source65: https://registry.npmjs.org/minimist/-/minimist-0.0.8.tgz
Source66: https://registry.npmjs.org/mkdirp/-/mkdirp-0.5.1.tgz
Source67: https://registry.npmjs.org/ms/-/ms-2.0.0.tgz
Source68: https://registry.npmjs.org/next-tick/-/next-tick-1.0.0.tgz
Source69: https://registry.npmjs.org/node-gyp/-/node-gyp-3.3.1.tgz
Source70: https://registry.npmjs.org/nopt/-/nopt-3.0.6.tgz
Source71: https://registry.npmjs.org/npmlog/-/npmlog-2.0.4.tgz
Source72: https://registry.npmjs.org/oauth-sign/-/oauth-sign-0.9.0.tgz
Source73: https://registry.npmjs.org/once/-/once-1.4.0.tgz
Source74: https://registry.npmjs.org/os-homedir/-/os-homedir-1.0.2.tgz
Source75: https://registry.npmjs.org/os-tmpdir/-/os-tmpdir-1.0.2.tgz
Source76: https://registry.npmjs.org/osenv/-/osenv-0.1.5.tgz
Source77: https://registry.npmjs.org/path-array/-/path-array-1.0.1.tgz
Source78: https://registry.npmjs.org/path-is-absolute/-/path-is-absolute-1.0.1.tgz
Source79: https://registry.npmjs.org/performance-now/-/performance-now-2.1.0.tgz
Source80: https://registry.npmjs.org/process-nextick-args/-/process-nextick-args-2.0.1.tgz
Source81: https://registry.npmjs.org/psl/-/psl-1.4.0.tgz
Source82: https://registry.npmjs.org/punycode/-/punycode-1.4.1.tgz
Source83: https://registry.npmjs.org/punycode/-/punycode-2.1.1.tgz
Source84: https://registry.npmjs.org/qs/-/qs-6.5.2.tgz
Source85: https://registry.npmjs.org/readable-stream/-/readable-stream-2.3.6.tgz
Source86: https://registry.npmjs.org/request/-/request-2.88.0.tgz
Source87: https://registry.npmjs.org/rimraf/-/rimraf-2.7.1.tgz
Source88: https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.1.2.tgz
Source89: https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.2.0.tgz
Source90: https://registry.npmjs.org/safer-buffer/-/safer-buffer-2.1.2.tgz
Source91: https://registry.npmjs.org/semver/-/semver-5.7.1.tgz
Source92: https://registry.npmjs.org/sigmund/-/sigmund-1.0.1.tgz
Source93: https://registry.npmjs.org/sshpk/-/sshpk-1.16.1.tgz
Source94: https://registry.npmjs.org/string_decoder/-/string_decoder-1.1.1.tgz
Source95: https://registry.npmjs.org/tar/-/tar-2.2.2.tgz
Source96: https://registry.npmjs.org/tough-cookie/-/tough-cookie-2.4.3.tgz
Source97: https://registry.npmjs.org/tunnel-agent/-/tunnel-agent-0.6.0.tgz
Source98: https://registry.npmjs.org/tweetnacl/-/tweetnacl-0.14.5.tgz
Source99: https://registry.npmjs.org/type/-/type-1.2.0.tgz
Source100: https://registry.npmjs.org/uri-js/-/uri-js-4.2.2.tgz
Source101: https://registry.npmjs.org/util-deprecate/-/util-deprecate-1.0.2.tgz
Source102: https://registry.npmjs.org/uuid/-/uuid-3.3.3.tgz
Source103: https://registry.npmjs.org/verror/-/verror-1.10.0.tgz
Source104: https://registry.npmjs.org/which/-/which-1.3.1.tgz
Source105: https://registry.npmjs.org/wrappy/-/wrappy-1.0.2.tgz
Source106: nodejs-node-gyp-%{version}-registry.npmjs.org.tgz
Source107: addon-rpm.gypi

Patch1: node-gyp-node-dirs.patch

Requires:   gyp
Requires:   %{?scl_prefix_nodejs}nodejs-devel
Requires:   libuv-devel
Requires:   http-parser-devel
Requires:   gcc-c++
Requires:   python-devel
Requires:   make

BuildRequires: %{?scl_prefix_nodejs}nodejs-devel
%if 0%{!?scl:1}
BuildRequires: nodejs-packaging
%endif

BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}
Provides: bundled(npm(abbrev)) = 1.1.1
Provides: bundled(npm(ajv)) = 6.10.2
Provides: bundled(npm(ansi)) = 0.3.1
Provides: bundled(npm(are-we-there-yet)) = 1.1.5
Provides: bundled(npm(array-index)) = 1.0.0
Provides: bundled(npm(asn1)) = 0.2.4
Provides: bundled(npm(assert-plus)) = 1.0.0
Provides: bundled(npm(asynckit)) = 0.4.0
Provides: bundled(npm(aws-sign2)) = 0.7.0
Provides: bundled(npm(aws4)) = 1.8.0
Provides: bundled(npm(balanced-match)) = 1.0.0
Provides: bundled(npm(bcrypt-pbkdf)) = 1.0.2
Provides: bundled(npm(block-stream)) = 0.0.9
Provides: bundled(npm(brace-expansion)) = 1.1.11
Provides: bundled(npm(caseless)) = 0.12.0
Provides: bundled(npm(combined-stream)) = 1.0.8
Provides: bundled(npm(concat-map)) = 0.0.1
Provides: bundled(npm(core-util-is)) = 1.0.2
Provides: bundled(npm(d)) = 1.0.1
Provides: bundled(npm(dashdash)) = 1.14.1
Provides: bundled(npm(debug)) = 2.6.9
Provides: bundled(npm(delayed-stream)) = 1.0.0
Provides: bundled(npm(delegates)) = 1.0.0
Provides: bundled(npm(ecc-jsbn)) = 0.1.2
Provides: bundled(npm(es5-ext)) = 0.10.51
Provides: bundled(npm(es6-iterator)) = 2.0.3
Provides: bundled(npm(es6-symbol)) = 3.1.2
Provides: bundled(npm(extend)) = 3.0.2
Provides: bundled(npm(extsprintf)) = 1.3.0
Provides: bundled(npm(extsprintf)) = 1.4.0
Provides: bundled(npm(fast-deep-equal)) = 2.0.1
Provides: bundled(npm(fast-json-stable-stringify)) = 2.0.0
Provides: bundled(npm(forever-agent)) = 0.6.1
Provides: bundled(npm(form-data)) = 2.3.3
Provides: bundled(npm(fs.realpath)) = 1.0.0
Provides: bundled(npm(fstream)) = 1.0.12
Provides: bundled(npm(gauge)) = 1.2.7
Provides: bundled(npm(getpass)) = 0.1.7
Provides: bundled(npm(glob)) = 4.5.3
Provides: bundled(npm(glob)) = 7.1.4
Provides: bundled(npm(graceful-fs)) = 4.2.2
Provides: bundled(npm(har-schema)) = 2.0.0
Provides: bundled(npm(har-validator)) = 5.1.3
Provides: bundled(npm(has-unicode)) = 2.0.1
Provides: bundled(npm(http-signature)) = 1.2.0
Provides: bundled(npm(inflight)) = 1.0.6
Provides: bundled(npm(inherits)) = 2.0.4
Provides: bundled(npm(is-typedarray)) = 1.0.0
Provides: bundled(npm(isarray)) = 1.0.0
Provides: bundled(npm(isexe)) = 2.0.0
Provides: bundled(npm(isstream)) = 0.1.2
Provides: bundled(npm(jsbn)) = 0.1.1
Provides: bundled(npm(json-schema)) = 0.2.3
Provides: bundled(npm(json-schema-traverse)) = 0.4.1
Provides: bundled(npm(json-stringify-safe)) = 5.0.1
Provides: bundled(npm(jsprim)) = 1.4.1
Provides: bundled(npm(lodash.pad)) = 4.5.1
Provides: bundled(npm(lodash.padend)) = 4.6.1
Provides: bundled(npm(lodash.padstart)) = 4.6.1
Provides: bundled(npm(lru-cache)) = 2.7.3
Provides: bundled(npm(mime-db)) = 1.40.0
Provides: bundled(npm(mime-types)) = 2.1.24
Provides: bundled(npm(minimatch)) = 1.0.0
Provides: bundled(npm(minimatch)) = 2.0.10
Provides: bundled(npm(minimatch)) = 3.0.4
Provides: bundled(npm(minimist)) = 0.0.8
Provides: bundled(npm(mkdirp)) = 0.5.1
Provides: bundled(npm(ms)) = 2.0.0
Provides: bundled(npm(next-tick)) = 1.0.0
Provides: bundled(npm(node-gyp)) = 3.3.1
Provides: bundled(npm(nopt)) = 3.0.6
Provides: bundled(npm(npmlog)) = 2.0.4
Provides: bundled(npm(oauth-sign)) = 0.9.0
Provides: bundled(npm(once)) = 1.4.0
Provides: bundled(npm(os-homedir)) = 1.0.2
Provides: bundled(npm(os-tmpdir)) = 1.0.2
Provides: bundled(npm(osenv)) = 0.1.5
Provides: bundled(npm(path-array)) = 1.0.1
Provides: bundled(npm(path-is-absolute)) = 1.0.1
Provides: bundled(npm(performance-now)) = 2.1.0
Provides: bundled(npm(process-nextick-args)) = 2.0.1
Provides: bundled(npm(psl)) = 1.4.0
Provides: bundled(npm(punycode)) = 1.4.1
Provides: bundled(npm(punycode)) = 2.1.1
Provides: bundled(npm(qs)) = 6.5.2
Provides: bundled(npm(readable-stream)) = 2.3.6
Provides: bundled(npm(request)) = 2.88.0
Provides: bundled(npm(rimraf)) = 2.7.1
Provides: bundled(npm(safe-buffer)) = 5.1.2
Provides: bundled(npm(safe-buffer)) = 5.2.0
Provides: bundled(npm(safer-buffer)) = 2.1.2
Provides: bundled(npm(semver)) = 5.7.1
Provides: bundled(npm(sigmund)) = 1.0.1
Provides: bundled(npm(sshpk)) = 1.16.1
Provides: bundled(npm(string_decoder)) = 1.1.1
Provides: bundled(npm(tar)) = 2.2.2
Provides: bundled(npm(tough-cookie)) = 2.4.3
Provides: bundled(npm(tunnel-agent)) = 0.6.0
Provides: bundled(npm(tweetnacl)) = 0.14.5
Provides: bundled(npm(type)) = 1.2.0
Provides: bundled(npm(uri-js)) = 4.2.2
Provides: bundled(npm(util-deprecate)) = 1.0.2
Provides: bundled(npm(uuid)) = 3.3.3
Provides: bundled(npm(verror)) = 1.10.0
Provides: bundled(npm(which)) = 1.3.1
Provides: bundled(npm(wrappy)) = 1.0.2
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
  echo $tgz | grep -q -E "registry.npmjs.org|\.gypi" || npm cache add --cache %{npm_cache_dir} $tgz
done
%{?scl:end_of_scl}

%setup -T -q -a 106 -D -n %{npm_cache_dir}

%build
%{?scl:scl enable %{?scl_nodejs} - << \end_of_scl}
npm install --cache-min Infinity --cache %{?scl:../}%{npm_cache_dir} --no-shrinkwrap --no-optional --global-style true %{npm_name}@%{version}
%{?scl:end_of_scl}

pushd node_modules/%{npm_name}
%__patch -p1 < %PATCH1
popd

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/0001-gyp-always-install-into-PRODUCT_DIR.patch %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/0002-gyp-apply-https-codereview.chromium.org-11361103.patch %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/0003-gyp-don-t-use-links-at-all-just-copy-the-files-inste.patch %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/addon.gypi %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/bin %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/gyp %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/lib %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/src %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/test %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -p %{SOURCE107} %{buildroot}%{nodejs_sitelib}/node-gyp/addon-rpm.gypi

mkdir -p %{buildroot}%{_bindir}/
chmod 0755 %{buildroot}%{nodejs_sitelib}/%{npm_name}/bin/node-gyp.js
ln -sf %{nodejs_sitelib}/%{npm_name}/bin/node-gyp.js %{buildroot}%{_bindir}/node-gyp

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%{_bindir}/node-gyp
%license node_modules/%{npm_name}/LICENSE
%doc node_modules/%{npm_name}/CHANGELOG.md
%doc node_modules/%{npm_name}/History.md
%doc node_modules/%{npm_name}/README.md

%changelog
* Tue Oct 22 2019 Eric D. Helms <ericdhelms@gmail.com> - 3.3.1-4
- Fix broken SCL include directories

* Mon Oct 21 2019 Eric D. Helms <ericdhelms@gmail.com> - 3.3.1-3
- Build for SCL

* Fri Oct 04 2019 Eric D. Helms <ericdhelms@gmail.com> - 3.3.1-2
- Update specs to handle SCL

* Fri Mar 03 2017 Dominic Cleal <dominic@cleal.org> 3.3.1-1
- Update node-gyp to 3.3.1 (dominic@cleal.org)

* Thu Mar 02 2017 Dominic Cleal <dominic@cleal.org> 3.2.1-1
- new package built with tito
