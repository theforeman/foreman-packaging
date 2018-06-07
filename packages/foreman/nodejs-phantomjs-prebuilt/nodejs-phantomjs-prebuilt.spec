%global npm_name phantomjs-prebuilt

Name: nodejs-%{npm_name}
Version: 2.1.16
Release: 1%{?dist}
Summary: Headless WebKit with JS API
License: Apache-2.0
Group: Development/Libraries
URL: https://github.com/Medium/phantomjs
Source0: https://registry.npmjs.org/phantomjs-prebuilt/-/phantomjs-prebuilt-2.1.16.tgz
Source1: https://registry.npmjs.org/hasha/-/hasha-2.2.0.tgz
Source2: https://registry.npmjs.org/es6-promise/-/es6-promise-4.2.4.tgz
Source3: https://registry.npmjs.org/extract-zip/-/extract-zip-1.6.7.tgz
Source4: https://registry.npmjs.org/progress/-/progress-1.1.8.tgz
Source5: https://registry.npmjs.org/request-progress/-/request-progress-2.0.1.tgz
Source6: https://registry.npmjs.org/fs-extra/-/fs-extra-1.0.0.tgz
Source7: https://registry.npmjs.org/kew/-/kew-0.7.0.tgz
Source8: https://registry.npmjs.org/request/-/request-2.87.0.tgz
Source9: https://registry.npmjs.org/concat-stream/-/concat-stream-1.6.2.tgz
Source10: https://registry.npmjs.org/which/-/which-1.3.1.tgz
Source11: https://registry.npmjs.org/is-stream/-/is-stream-1.1.0.tgz
Source12: https://registry.npmjs.org/yauzl/-/yauzl-2.4.1.tgz
Source13: https://registry.npmjs.org/mkdirp/-/mkdirp-0.5.1.tgz
Source14: https://registry.npmjs.org/pinkie-promise/-/pinkie-promise-2.0.1.tgz
Source15: https://registry.npmjs.org/debug/-/debug-2.6.9.tgz
Source16: https://registry.npmjs.org/throttleit/-/throttleit-1.0.0.tgz
Source17: https://registry.npmjs.org/aws-sign2/-/aws-sign2-0.7.0.tgz
Source18: https://registry.npmjs.org/combined-stream/-/combined-stream-1.0.6.tgz
Source19: https://registry.npmjs.org/aws4/-/aws4-1.7.0.tgz
Source20: https://registry.npmjs.org/jsonfile/-/jsonfile-2.4.0.tgz
Source21: https://registry.npmjs.org/klaw/-/klaw-1.3.1.tgz
Source22: https://registry.npmjs.org/graceful-fs/-/graceful-fs-4.1.11.tgz
Source23: https://registry.npmjs.org/caseless/-/caseless-0.12.0.tgz
Source24: https://registry.npmjs.org/forever-agent/-/forever-agent-0.6.1.tgz
Source25: https://registry.npmjs.org/extend/-/extend-3.0.1.tgz
Source26: https://registry.npmjs.org/is-typedarray/-/is-typedarray-1.0.0.tgz
Source27: https://registry.npmjs.org/json-stringify-safe/-/json-stringify-safe-5.0.1.tgz
Source28: https://registry.npmjs.org/isstream/-/isstream-0.1.2.tgz
Source29: https://registry.npmjs.org/form-data/-/form-data-2.3.2.tgz
Source30: https://registry.npmjs.org/http-signature/-/http-signature-1.2.0.tgz
Source31: https://registry.npmjs.org/har-validator/-/har-validator-5.0.3.tgz
Source32: https://registry.npmjs.org/oauth-sign/-/oauth-sign-0.8.2.tgz
Source33: https://registry.npmjs.org/tunnel-agent/-/tunnel-agent-0.6.0.tgz
Source34: https://registry.npmjs.org/performance-now/-/performance-now-2.1.0.tgz
Source35: https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.1.2.tgz
Source36: https://registry.npmjs.org/mime-types/-/mime-types-2.1.18.tgz
Source37: https://registry.npmjs.org/qs/-/qs-6.5.2.tgz
Source38: https://registry.npmjs.org/tough-cookie/-/tough-cookie-2.3.4.tgz
Source39: https://registry.npmjs.org/uuid/-/uuid-3.2.1.tgz
Source40: https://registry.npmjs.org/buffer-from/-/buffer-from-1.1.0.tgz
Source41: https://registry.npmjs.org/typedarray/-/typedarray-0.0.6.tgz
Source42: https://registry.npmjs.org/isexe/-/isexe-2.0.0.tgz
Source43: https://registry.npmjs.org/fd-slicer/-/fd-slicer-1.0.1.tgz
Source44: https://registry.npmjs.org/minimist/-/minimist-0.0.8.tgz
Source45: https://registry.npmjs.org/pinkie/-/pinkie-2.0.4.tgz
Source46: https://registry.npmjs.org/inherits/-/inherits-2.0.3.tgz
Source47: https://registry.npmjs.org/delayed-stream/-/delayed-stream-1.0.0.tgz
Source48: https://registry.npmjs.org/asynckit/-/asynckit-0.4.0.tgz
Source49: https://registry.npmjs.org/ms/-/ms-2.0.0.tgz
Source50: https://registry.npmjs.org/readable-stream/-/readable-stream-2.3.6.tgz
Source51: https://registry.npmjs.org/assert-plus/-/assert-plus-1.0.0.tgz
Source52: https://registry.npmjs.org/har-schema/-/har-schema-2.0.0.tgz
Source53: https://registry.npmjs.org/jsprim/-/jsprim-1.4.1.tgz
Source54: https://registry.npmjs.org/sshpk/-/sshpk-1.14.2.tgz
Source55: https://registry.npmjs.org/punycode/-/punycode-1.4.1.tgz
Source56: https://registry.npmjs.org/mime-db/-/mime-db-1.33.0.tgz
Source57: https://registry.npmjs.org/pend/-/pend-1.2.0.tgz
Source58: https://registry.npmjs.org/isarray/-/isarray-1.0.0.tgz
Source59: https://registry.npmjs.org/core-util-is/-/core-util-is-1.0.2.tgz
Source60: https://registry.npmjs.org/string_decoder/-/string_decoder-1.1.1.tgz
Source61: https://registry.npmjs.org/process-nextick-args/-/process-nextick-args-2.0.0.tgz
Source62: https://registry.npmjs.org/extsprintf/-/extsprintf-1.3.0.tgz
Source63: https://registry.npmjs.org/util-deprecate/-/util-deprecate-1.0.2.tgz
Source64: https://registry.npmjs.org/ajv/-/ajv-5.5.2.tgz
Source65: https://registry.npmjs.org/json-schema/-/json-schema-0.2.3.tgz
Source66: https://registry.npmjs.org/verror/-/verror-1.10.0.tgz
Source67: https://registry.npmjs.org/asn1/-/asn1-0.2.3.tgz
Source68: https://registry.npmjs.org/getpass/-/getpass-0.1.7.tgz
Source69: https://registry.npmjs.org/jsbn/-/jsbn-0.1.1.tgz
Source70: https://registry.npmjs.org/dashdash/-/dashdash-1.14.1.tgz
Source71: https://registry.npmjs.org/safer-buffer/-/safer-buffer-2.1.2.tgz
Source72: https://registry.npmjs.org/tweetnacl/-/tweetnacl-0.14.5.tgz
Source73: https://registry.npmjs.org/ecc-jsbn/-/ecc-jsbn-0.1.1.tgz
Source74: https://registry.npmjs.org/bcrypt-pbkdf/-/bcrypt-pbkdf-1.0.1.tgz
Source75: https://registry.npmjs.org/fast-deep-equal/-/fast-deep-equal-1.1.0.tgz
Source76: https://registry.npmjs.org/fast-json-stable-stringify/-/fast-json-stable-stringify-2.0.0.tgz
Source77: https://registry.npmjs.org/co/-/co-4.6.0.tgz
Source78: https://registry.npmjs.org/json-schema-traverse/-/json-schema-traverse-0.3.1.tgz
Source79: https://registry.npmjs.org/extsprintf/-/extsprintf-1.4.0.tgz
Source80: %{npm_name}-%{version}-registry.npmjs.org.tgz
BuildRequires: nodejs-packaging
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: npm(%{npm_name}) = %{version}
Provides: bundled(npm(ajv)) = 5.5.2
Provides: bundled(npm(asn1)) = 0.2.3
Provides: bundled(npm(assert-plus)) = 1.0.0
Provides: bundled(npm(asynckit)) = 0.4.0
Provides: bundled(npm(aws-sign2)) = 0.7.0
Provides: bundled(npm(aws4)) = 1.7.0
Provides: bundled(npm(bcrypt-pbkdf)) = 1.0.1
Provides: bundled(npm(buffer-from)) = 1.1.0
Provides: bundled(npm(caseless)) = 0.12.0
Provides: bundled(npm(co)) = 4.6.0
Provides: bundled(npm(combined-stream)) = 1.0.6
Provides: bundled(npm(concat-stream)) = 1.6.2
Provides: bundled(npm(core-util-is)) = 1.0.2
Provides: bundled(npm(dashdash)) = 1.14.1
Provides: bundled(npm(debug)) = 2.6.9
Provides: bundled(npm(delayed-stream)) = 1.0.0
Provides: bundled(npm(ecc-jsbn)) = 0.1.1
Provides: bundled(npm(es6-promise)) = 4.2.4
Provides: bundled(npm(extend)) = 3.0.1
Provides: bundled(npm(extract-zip)) = 1.6.7
Provides: bundled(npm(extsprintf)) = 1.4.0
Provides: bundled(npm(extsprintf)) = 1.3.0
Provides: bundled(npm(fast-deep-equal)) = 1.1.0
Provides: bundled(npm(fast-json-stable-stringify)) = 2.0.0
Provides: bundled(npm(fd-slicer)) = 1.0.1
Provides: bundled(npm(forever-agent)) = 0.6.1
Provides: bundled(npm(form-data)) = 2.3.2
Provides: bundled(npm(fs-extra)) = 1.0.0
Provides: bundled(npm(getpass)) = 0.1.7
Provides: bundled(npm(graceful-fs)) = 4.1.11
Provides: bundled(npm(har-schema)) = 2.0.0
Provides: bundled(npm(har-validator)) = 5.0.3
Provides: bundled(npm(hasha)) = 2.2.0
Provides: bundled(npm(http-signature)) = 1.2.0
Provides: bundled(npm(inherits)) = 2.0.3
Provides: bundled(npm(is-stream)) = 1.1.0
Provides: bundled(npm(is-typedarray)) = 1.0.0
Provides: bundled(npm(isarray)) = 1.0.0
Provides: bundled(npm(isexe)) = 2.0.0
Provides: bundled(npm(isstream)) = 0.1.2
Provides: bundled(npm(jsbn)) = 0.1.1
Provides: bundled(npm(json-schema)) = 0.2.3
Provides: bundled(npm(json-schema-traverse)) = 0.3.1
Provides: bundled(npm(json-stringify-safe)) = 5.0.1
Provides: bundled(npm(jsonfile)) = 2.4.0
Provides: bundled(npm(jsprim)) = 1.4.1
Provides: bundled(npm(kew)) = 0.7.0
Provides: bundled(npm(klaw)) = 1.3.1
Provides: bundled(npm(mime-db)) = 1.33.0
Provides: bundled(npm(mime-types)) = 2.1.18
Provides: bundled(npm(minimist)) = 0.0.8
Provides: bundled(npm(mkdirp)) = 0.5.1
Provides: bundled(npm(ms)) = 2.0.0
Provides: bundled(npm(oauth-sign)) = 0.8.2
Provides: bundled(npm(pend)) = 1.2.0
Provides: bundled(npm(performance-now)) = 2.1.0
Provides: bundled(npm(phantomjs-prebuilt)) = 2.1.16
Provides: bundled(npm(pinkie)) = 2.0.4
Provides: bundled(npm(pinkie-promise)) = 2.0.1
Provides: bundled(npm(process-nextick-args)) = 2.0.0
Provides: bundled(npm(progress)) = 1.1.8
Provides: bundled(npm(punycode)) = 1.4.1
Provides: bundled(npm(qs)) = 6.5.2
Provides: bundled(npm(readable-stream)) = 2.3.6
Provides: bundled(npm(request)) = 2.87.0
Provides: bundled(npm(request-progress)) = 2.0.1
Provides: bundled(npm(safe-buffer)) = 5.1.2
Provides: bundled(npm(safer-buffer)) = 2.1.2
Provides: bundled(npm(sshpk)) = 1.14.2
Provides: bundled(npm(string_decoder)) = 1.1.1
Provides: bundled(npm(throttleit)) = 1.0.0
Provides: bundled(npm(tough-cookie)) = 2.3.4
Provides: bundled(npm(tunnel-agent)) = 0.6.0
Provides: bundled(npm(tweetnacl)) = 0.14.5
Provides: bundled(npm(typedarray)) = 0.0.6
Provides: bundled(npm(util-deprecate)) = 1.0.2
Provides: bundled(npm(uuid)) = 3.2.1
Provides: bundled(npm(verror)) = 1.10.0
Provides: bundled(npm(which)) = 1.3.1
Provides: bundled(npm(yauzl)) = 2.4.1
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
%setup -T -q -a 80 -D -n %{npm_cache_dir}

%build
npm install --cache-min Infinity --cache %{npm_cache_dir} --no-shrinkwrap --no-optional --global-style true %{npm_name}@%{version}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/bin %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/install.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/lib %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/test %{buildroot}%{nodejs_sitelib}/%{npm_name}

mkdir -p %{buildroot}%{_bindir}/
chmod 0755 %{buildroot}%{nodejs_sitelib}/%{npm_name}/bin/phantomjs
ln -sf %{nodejs_sitelib}/%{npm_name}/bin/phantomjs %{buildroot}%{_bindir}/phantomjs

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%{_bindir}/phantomjs
%license node_modules/%{npm_name}/LICENSE.txt
%doc node_modules/%{npm_name}/README.md

%changelog
* Thu Jun 07 2018 Tomas Strachota <tstrachota@redhat.com> 2.1.16-1
- Add nodejs-phantomjs-prebuilt generated by npm2rpm using the bundle strategy

