%global npm_name node-gyp

Name: nodejs-node-gyp
Version: 6.1.0
Release: 11%{?dist}
Summary: Node
License: MIT
Group: Development/Libraries
URL: https://github.com/nodejs/node-gyp#readme
Source0: https://registry.npmjs.org/abbrev/-/abbrev-1.1.1.tgz
Source1: https://registry.npmjs.org/ajv/-/ajv-6.12.6.tgz
Source2: https://registry.npmjs.org/ansi-regex/-/ansi-regex-2.1.1.tgz
Source3: https://registry.npmjs.org/ansi-regex/-/ansi-regex-5.0.1.tgz
Source4: https://registry.npmjs.org/aproba/-/aproba-1.2.0.tgz
Source5: https://registry.npmjs.org/are-we-there-yet/-/are-we-there-yet-1.1.7.tgz
Source6: https://registry.npmjs.org/asn1/-/asn1-0.2.6.tgz
Source7: https://registry.npmjs.org/assert-plus/-/assert-plus-1.0.0.tgz
Source8: https://registry.npmjs.org/asynckit/-/asynckit-0.4.0.tgz
Source9: https://registry.npmjs.org/aws-sign2/-/aws-sign2-0.7.0.tgz
Source10: https://registry.npmjs.org/aws4/-/aws4-1.12.0.tgz
Source11: https://registry.npmjs.org/balanced-match/-/balanced-match-1.0.2.tgz
Source12: https://registry.npmjs.org/bcrypt-pbkdf/-/bcrypt-pbkdf-1.0.2.tgz
Source13: https://registry.npmjs.org/brace-expansion/-/brace-expansion-1.1.11.tgz
Source14: https://registry.npmjs.org/caseless/-/caseless-0.12.0.tgz
Source15: https://registry.npmjs.org/chownr/-/chownr-1.1.4.tgz
Source16: https://registry.npmjs.org/code-point-at/-/code-point-at-1.1.0.tgz
Source17: https://registry.npmjs.org/combined-stream/-/combined-stream-1.0.8.tgz
Source18: https://registry.npmjs.org/concat-map/-/concat-map-0.0.1.tgz
Source19: https://registry.npmjs.org/console-control-strings/-/console-control-strings-1.1.0.tgz
Source20: https://registry.npmjs.org/core-util-is/-/core-util-is-1.0.2.tgz
Source21: https://registry.npmjs.org/core-util-is/-/core-util-is-1.0.3.tgz
Source22: https://registry.npmjs.org/dashdash/-/dashdash-1.14.1.tgz
Source23: https://registry.npmjs.org/delayed-stream/-/delayed-stream-1.0.0.tgz
Source24: https://registry.npmjs.org/delegates/-/delegates-1.0.0.tgz
Source25: https://registry.npmjs.org/ecc-jsbn/-/ecc-jsbn-0.1.2.tgz
Source26: https://registry.npmjs.org/emoji-regex/-/emoji-regex-8.0.0.tgz
Source27: https://registry.npmjs.org/env-paths/-/env-paths-2.2.1.tgz
Source28: https://registry.npmjs.org/extend/-/extend-3.0.2.tgz
Source29: https://registry.npmjs.org/extsprintf/-/extsprintf-1.3.0.tgz
Source30: https://registry.npmjs.org/extsprintf/-/extsprintf-1.4.1.tgz
Source31: https://registry.npmjs.org/fast-deep-equal/-/fast-deep-equal-3.1.3.tgz
Source32: https://registry.npmjs.org/fast-json-stable-stringify/-/fast-json-stable-stringify-2.1.0.tgz
Source33: https://registry.npmjs.org/forever-agent/-/forever-agent-0.6.1.tgz
Source34: https://registry.npmjs.org/form-data/-/form-data-2.3.3.tgz
Source35: https://registry.npmjs.org/fs-minipass/-/fs-minipass-1.2.7.tgz
Source36: https://registry.npmjs.org/fs.realpath/-/fs.realpath-1.0.0.tgz
Source37: https://registry.npmjs.org/gauge/-/gauge-2.7.4.tgz
Source38: https://registry.npmjs.org/getpass/-/getpass-0.1.7.tgz
Source39: https://registry.npmjs.org/glob/-/glob-7.2.3.tgz
Source40: https://registry.npmjs.org/graceful-fs/-/graceful-fs-4.2.11.tgz
Source41: https://registry.npmjs.org/har-schema/-/har-schema-2.0.0.tgz
Source42: https://registry.npmjs.org/har-validator/-/har-validator-5.1.5.tgz
Source43: https://registry.npmjs.org/has-unicode/-/has-unicode-2.0.1.tgz
Source44: https://registry.npmjs.org/http-signature/-/http-signature-1.2.0.tgz
Source45: https://registry.npmjs.org/inflight/-/inflight-1.0.6.tgz
Source46: https://registry.npmjs.org/inherits/-/inherits-2.0.4.tgz
Source47: https://registry.npmjs.org/is-fullwidth-code-point/-/is-fullwidth-code-point-1.0.0.tgz
Source48: https://registry.npmjs.org/is-fullwidth-code-point/-/is-fullwidth-code-point-3.0.0.tgz
Source49: https://registry.npmjs.org/is-typedarray/-/is-typedarray-1.0.0.tgz
Source50: https://registry.npmjs.org/isarray/-/isarray-1.0.0.tgz
Source51: https://registry.npmjs.org/isexe/-/isexe-2.0.0.tgz
Source52: https://registry.npmjs.org/isstream/-/isstream-0.1.2.tgz
Source53: https://registry.npmjs.org/jsbn/-/jsbn-0.1.1.tgz
Source54: https://registry.npmjs.org/json-schema/-/json-schema-0.4.0.tgz
Source55: https://registry.npmjs.org/json-schema-traverse/-/json-schema-traverse-0.4.1.tgz
Source56: https://registry.npmjs.org/json-stringify-safe/-/json-stringify-safe-5.0.1.tgz
Source57: https://registry.npmjs.org/jsprim/-/jsprim-1.4.2.tgz
Source58: https://registry.npmjs.org/mime-db/-/mime-db-1.52.0.tgz
Source59: https://registry.npmjs.org/mime-types/-/mime-types-2.1.35.tgz
Source60: https://registry.npmjs.org/minimatch/-/minimatch-3.1.2.tgz
Source61: https://registry.npmjs.org/minimist/-/minimist-1.2.8.tgz
Source62: https://registry.npmjs.org/minipass/-/minipass-2.9.0.tgz
Source63: https://registry.npmjs.org/minizlib/-/minizlib-1.3.3.tgz
Source64: https://registry.npmjs.org/mkdirp/-/mkdirp-0.5.6.tgz
Source65: https://registry.npmjs.org/node-gyp/-/node-gyp-6.1.0.tgz
Source66: https://registry.npmjs.org/nopt/-/nopt-4.0.3.tgz
Source67: https://registry.npmjs.org/npmlog/-/npmlog-4.1.2.tgz
Source68: https://registry.npmjs.org/number-is-nan/-/number-is-nan-1.0.1.tgz
Source69: https://registry.npmjs.org/oauth-sign/-/oauth-sign-0.9.0.tgz
Source70: https://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz
Source71: https://registry.npmjs.org/once/-/once-1.4.0.tgz
Source72: https://registry.npmjs.org/os-homedir/-/os-homedir-1.0.2.tgz
Source73: https://registry.npmjs.org/os-tmpdir/-/os-tmpdir-1.0.2.tgz
Source74: https://registry.npmjs.org/osenv/-/osenv-0.1.5.tgz
Source75: https://registry.npmjs.org/path-is-absolute/-/path-is-absolute-1.0.1.tgz
Source76: https://registry.npmjs.org/performance-now/-/performance-now-2.1.0.tgz
Source77: https://registry.npmjs.org/process-nextick-args/-/process-nextick-args-2.0.1.tgz
Source78: https://registry.npmjs.org/psl/-/psl-1.9.0.tgz
Source79: https://registry.npmjs.org/punycode/-/punycode-2.3.1.tgz
Source80: https://registry.npmjs.org/qs/-/qs-6.5.3.tgz
Source81: https://registry.npmjs.org/readable-stream/-/readable-stream-2.3.8.tgz
Source82: https://registry.npmjs.org/request/-/request-2.88.2.tgz
Source83: https://registry.npmjs.org/rimraf/-/rimraf-2.7.1.tgz
Source84: https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.1.2.tgz
Source85: https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.2.1.tgz
Source86: https://registry.npmjs.org/safer-buffer/-/safer-buffer-2.1.2.tgz
Source87: https://registry.npmjs.org/semver/-/semver-5.7.2.tgz
Source88: https://registry.npmjs.org/set-blocking/-/set-blocking-2.0.0.tgz
Source89: https://registry.npmjs.org/signal-exit/-/signal-exit-3.0.7.tgz
Source90: https://registry.npmjs.org/sshpk/-/sshpk-1.18.0.tgz
Source91: https://registry.npmjs.org/string_decoder/-/string_decoder-1.1.1.tgz
Source92: https://registry.npmjs.org/string-width/-/string-width-1.0.2.tgz
Source93: https://registry.npmjs.org/string-width/-/string-width-4.2.3.tgz
Source94: https://registry.npmjs.org/strip-ansi/-/strip-ansi-3.0.1.tgz
Source95: https://registry.npmjs.org/strip-ansi/-/strip-ansi-6.0.1.tgz
Source96: https://registry.npmjs.org/tar/-/tar-4.4.19.tgz
Source97: https://registry.npmjs.org/tough-cookie/-/tough-cookie-2.5.0.tgz
Source98: https://registry.npmjs.org/tunnel-agent/-/tunnel-agent-0.6.0.tgz
Source99: https://registry.npmjs.org/tweetnacl/-/tweetnacl-0.14.5.tgz
Source100: https://registry.npmjs.org/uri-js/-/uri-js-4.4.1.tgz
Source101: https://registry.npmjs.org/util-deprecate/-/util-deprecate-1.0.2.tgz
Source102: https://registry.npmjs.org/uuid/-/uuid-3.4.0.tgz
Source103: https://registry.npmjs.org/verror/-/verror-1.10.0.tgz
Source104: https://registry.npmjs.org/which/-/which-1.3.1.tgz
Source105: https://registry.npmjs.org/wide-align/-/wide-align-1.1.5.tgz
Source106: https://registry.npmjs.org/wrappy/-/wrappy-1.0.2.tgz
Source107: https://registry.npmjs.org/yallist/-/yallist-3.1.1.tgz
Source108: nodejs-node-gyp-%{version}-registry.npmjs.org.tgz
Source109: addon-rpm-el8.gypi

Patch1: node-gyp-node-dirs.patch

BuildRequires: npm
BuildRequires: nodejs-packaging

BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: npm(%{npm_name}) = %{version}
Provides: bundled(npm(abbrev)) = 1.1.1
Provides: bundled(npm(ajv)) = 6.12.6
Provides: bundled(npm(ansi-regex)) = 2.1.1
Provides: bundled(npm(ansi-regex)) = 5.0.1
Provides: bundled(npm(aproba)) = 1.2.0
Provides: bundled(npm(are-we-there-yet)) = 1.1.7
Provides: bundled(npm(asn1)) = 0.2.6
Provides: bundled(npm(assert-plus)) = 1.0.0
Provides: bundled(npm(asynckit)) = 0.4.0
Provides: bundled(npm(aws-sign2)) = 0.7.0
Provides: bundled(npm(aws4)) = 1.12.0
Provides: bundled(npm(balanced-match)) = 1.0.2
Provides: bundled(npm(bcrypt-pbkdf)) = 1.0.2
Provides: bundled(npm(brace-expansion)) = 1.1.11
Provides: bundled(npm(caseless)) = 0.12.0
Provides: bundled(npm(chownr)) = 1.1.4
Provides: bundled(npm(code-point-at)) = 1.1.0
Provides: bundled(npm(combined-stream)) = 1.0.8
Provides: bundled(npm(concat-map)) = 0.0.1
Provides: bundled(npm(console-control-strings)) = 1.1.0
Provides: bundled(npm(core-util-is)) = 1.0.2
Provides: bundled(npm(core-util-is)) = 1.0.3
Provides: bundled(npm(dashdash)) = 1.14.1
Provides: bundled(npm(delayed-stream)) = 1.0.0
Provides: bundled(npm(delegates)) = 1.0.0
Provides: bundled(npm(ecc-jsbn)) = 0.1.2
Provides: bundled(npm(emoji-regex)) = 8.0.0
Provides: bundled(npm(env-paths)) = 2.2.1
Provides: bundled(npm(extend)) = 3.0.2
Provides: bundled(npm(extsprintf)) = 1.3.0
Provides: bundled(npm(extsprintf)) = 1.4.1
Provides: bundled(npm(fast-deep-equal)) = 3.1.3
Provides: bundled(npm(fast-json-stable-stringify)) = 2.1.0
Provides: bundled(npm(forever-agent)) = 0.6.1
Provides: bundled(npm(form-data)) = 2.3.3
Provides: bundled(npm(fs-minipass)) = 1.2.7
Provides: bundled(npm(fs.realpath)) = 1.0.0
Provides: bundled(npm(gauge)) = 2.7.4
Provides: bundled(npm(getpass)) = 0.1.7
Provides: bundled(npm(glob)) = 7.2.3
Provides: bundled(npm(graceful-fs)) = 4.2.11
Provides: bundled(npm(har-schema)) = 2.0.0
Provides: bundled(npm(har-validator)) = 5.1.5
Provides: bundled(npm(has-unicode)) = 2.0.1
Provides: bundled(npm(http-signature)) = 1.2.0
Provides: bundled(npm(inflight)) = 1.0.6
Provides: bundled(npm(inherits)) = 2.0.4
Provides: bundled(npm(is-fullwidth-code-point)) = 1.0.0
Provides: bundled(npm(is-fullwidth-code-point)) = 3.0.0
Provides: bundled(npm(is-typedarray)) = 1.0.0
Provides: bundled(npm(isarray)) = 1.0.0
Provides: bundled(npm(isexe)) = 2.0.0
Provides: bundled(npm(isstream)) = 0.1.2
Provides: bundled(npm(jsbn)) = 0.1.1
Provides: bundled(npm(json-schema)) = 0.4.0
Provides: bundled(npm(json-schema-traverse)) = 0.4.1
Provides: bundled(npm(json-stringify-safe)) = 5.0.1
Provides: bundled(npm(jsprim)) = 1.4.2
Provides: bundled(npm(mime-db)) = 1.52.0
Provides: bundled(npm(mime-types)) = 2.1.35
Provides: bundled(npm(minimatch)) = 3.1.2
Provides: bundled(npm(minimist)) = 1.2.8
Provides: bundled(npm(minipass)) = 2.9.0
Provides: bundled(npm(minizlib)) = 1.3.3
Provides: bundled(npm(mkdirp)) = 0.5.6
Provides: bundled(npm(node-gyp)) = 6.1.0
Provides: bundled(npm(nopt)) = 4.0.3
Provides: bundled(npm(npmlog)) = 4.1.2
Provides: bundled(npm(number-is-nan)) = 1.0.1
Provides: bundled(npm(oauth-sign)) = 0.9.0
Provides: bundled(npm(object-assign)) = 4.1.1
Provides: bundled(npm(once)) = 1.4.0
Provides: bundled(npm(os-homedir)) = 1.0.2
Provides: bundled(npm(os-tmpdir)) = 1.0.2
Provides: bundled(npm(osenv)) = 0.1.5
Provides: bundled(npm(path-is-absolute)) = 1.0.1
Provides: bundled(npm(performance-now)) = 2.1.0
Provides: bundled(npm(process-nextick-args)) = 2.0.1
Provides: bundled(npm(psl)) = 1.9.0
Provides: bundled(npm(punycode)) = 2.3.1
Provides: bundled(npm(qs)) = 6.5.3
Provides: bundled(npm(readable-stream)) = 2.3.8
Provides: bundled(npm(request)) = 2.88.2
Provides: bundled(npm(rimraf)) = 2.7.1
Provides: bundled(npm(safe-buffer)) = 5.1.2
Provides: bundled(npm(safe-buffer)) = 5.2.1
Provides: bundled(npm(safer-buffer)) = 2.1.2
Provides: bundled(npm(semver)) = 5.7.2
Provides: bundled(npm(set-blocking)) = 2.0.0
Provides: bundled(npm(signal-exit)) = 3.0.7
Provides: bundled(npm(sshpk)) = 1.18.0
Provides: bundled(npm(string_decoder)) = 1.1.1
Provides: bundled(npm(string-width)) = 1.0.2
Provides: bundled(npm(string-width)) = 4.2.3
Provides: bundled(npm(strip-ansi)) = 3.0.1
Provides: bundled(npm(strip-ansi)) = 6.0.1
Provides: bundled(npm(tar)) = 4.4.19
Provides: bundled(npm(tough-cookie)) = 2.5.0
Provides: bundled(npm(tunnel-agent)) = 0.6.0
Provides: bundled(npm(tweetnacl)) = 0.14.5
Provides: bundled(npm(uri-js)) = 4.4.1
Provides: bundled(npm(util-deprecate)) = 1.0.2
Provides: bundled(npm(uuid)) = 3.4.0
Provides: bundled(npm(verror)) = 1.10.0
Provides: bundled(npm(which)) = 1.3.1
Provides: bundled(npm(wide-align)) = 1.1.5
Provides: bundled(npm(wrappy)) = 1.0.2
Provides: bundled(npm(yallist)) = 3.1.1
AutoReq: no
AutoProv: no

%define npm_cache_dir /tmp/npm_cache_%{name}-%{version}-%{release}

%description
%{summary}

%prep
mkdir -p %{npm_cache_dir}
for tgz in %{sources}; do
  echo $tgz | grep -q -E "registry.npmjs.org|\.gypi" || npm cache add --cache %{npm_cache_dir} $tgz
done

%setup -T -q -a 108 -D -n %{npm_cache_dir}

%build
npm install --cache-min Infinity --cache %{npm_cache_dir} --no-shrinkwrap --no-optional --global-style true %{npm_name}@%{version}

pushd node_modules/%{npm_name}
%__patch -p1 < %PATCH1
popd

%install
grep -lr '#!/usr/bin/env python' node_modules/%{npm_name}/gyp | xargs sed -i 's/#!\/usr\/bin\/env python/#!\/usr\/bin\/env python3/g'
grep -lr '#!/usr/bin/python' node_modules/%{npm_name}/gyp | xargs sed -i 's/#!\/usr\/bin\/python/#!\/usr\/bin\/python3/g'

mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
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
%doc node_modules/%{npm_name}/CONTRIBUTING.md
%doc node_modules/%{npm_name}/README.md
%doc node_modules/%{npm_name}/macOS_Catalina.md

%changelog
* Fri Jan 12 2024 Eric D. Helms <ericdhelms@gmail.com> - 6.1.0-11
- Update bundle dependencies

* Wed Aug 02 2023 Eric D. Helms <ericdhelms@gmail.com> 6.1.0-10
- Drop SCL from nodejs-node-gyp spec

* Wed Apr 1 2020 Zach Huntington-Meath <zhunting@redhat.com> 6.1.0-9
- Update patch more

* Mon Mar 30 2020 Zach Huntington-Meath <zhunting@redhat.com> 6.1.0-8
- Update patch more

* Mon Mar 30 2020 Zach Huntington-Meath <zhunting@redhat.com> 6.1.0-7
- Update patch

* Mon Mar 30 2020 Zach Huntington-Meath <zhunting@redhat.com> 6.1.0-6
- Update patching logic

* Mon Mar 30 2020 Zach Huntington-Meath <zhunting@redhat.com> 6.1.0-5
- fix addon.gypi

* Mon Mar 30 2020 Zach Huntington-Meath <zhunting@redhat.com> 6.1.0-4
- fix patch usage

* Fri Mar 27 2020 Zach Huntington-Meath <zhunting@redhat.com> 6.1.0-3
- update patch usage

* Wed Mar 25 2020 Zach Huntington-Meath <zhunting@redhat.com> 6.1.0-2
- update to use more recent spec changes

* Wed Mar 25 2020 Zach Huntington-Meath <zhunting@redhat.com> 6.1.0-1
- Add nodejs-node-gyp generated by npm2rpm using the bundle strategy
