%global npm_name jsdom
%global enable_tests 0

Name: nodejs-%{npm_name}
Version: 9.12.0
Release: 1%{?dist}
Summary: A JavaScript implementation of the DOM and HTML standards
License: MIT
URL: https://github.com/tmpvar/jsdom
Source0: http://registry.npmjs.org/jsdom/-/jsdom-9.12.0.tgz
Source1: http://registry.npmjs.org/array-equal/-/array-equal-1.0.0.tgz
Source2: http://registry.npmjs.org/escodegen/-/escodegen-1.9.0.tgz
Source3: http://registry.npmjs.org/content-type-parser/-/content-type-parser-1.0.2.tgz
Source4: http://registry.npmjs.org/cssstyle/-/cssstyle-0.2.37.tgz
Source5: http://registry.npmjs.org/html-encoding-sniffer/-/html-encoding-sniffer-1.0.2.tgz
Source6: http://registry.npmjs.org/parse5/-/parse5-1.5.1.tgz
Source7: http://registry.npmjs.org/nwmatcher/-/nwmatcher-1.4.3.tgz
Source8: http://registry.npmjs.org/request/-/request-2.83.0.tgz
Source9: http://registry.npmjs.org/sax/-/sax-1.2.4.tgz
Source10: http://registry.npmjs.org/abab/-/abab-1.0.4.tgz
Source11: http://registry.npmjs.org/cssom/-/cssom-0.3.2.tgz
Source12: http://registry.npmjs.org/tough-cookie/-/tough-cookie-2.3.3.tgz
Source13: http://registry.npmjs.org/acorn-globals/-/acorn-globals-3.1.0.tgz
Source14: http://registry.npmjs.org/webidl-conversions/-/webidl-conversions-4.0.2.tgz
Source15: http://registry.npmjs.org/symbol-tree/-/symbol-tree-3.2.2.tgz
Source16: http://registry.npmjs.org/acorn/-/acorn-4.0.13.tgz
Source17: http://registry.npmjs.org/esutils/-/esutils-2.0.2.tgz
Source18: http://registry.npmjs.org/estraverse/-/estraverse-4.2.0.tgz
Source19: http://registry.npmjs.org/esprima/-/esprima-3.1.3.tgz
Source20: http://registry.npmjs.org/aws-sign2/-/aws-sign2-0.7.0.tgz
Source21: http://registry.npmjs.org/optionator/-/optionator-0.8.2.tgz
Source22: http://registry.npmjs.org/caseless/-/caseless-0.12.0.tgz
Source23: http://registry.npmjs.org/source-map/-/source-map-0.5.7.tgz
Source24: http://registry.npmjs.org/aws4/-/aws4-1.6.0.tgz
Source25: http://registry.npmjs.org/combined-stream/-/combined-stream-1.0.5.tgz
Source26: http://registry.npmjs.org/forever-agent/-/forever-agent-0.6.1.tgz
Source27: http://registry.npmjs.org/extend/-/extend-3.0.1.tgz
Source28: http://registry.npmjs.org/form-data/-/form-data-2.3.1.tgz
Source29: http://registry.npmjs.org/har-validator/-/har-validator-5.0.3.tgz
Source30: http://registry.npmjs.org/xml-name-validator/-/xml-name-validator-2.0.1.tgz
Source31: http://registry.npmjs.org/is-typedarray/-/is-typedarray-1.0.0.tgz
Source32: http://registry.npmjs.org/isstream/-/isstream-0.1.2.tgz
Source33: http://registry.npmjs.org/json-stringify-safe/-/json-stringify-safe-5.0.1.tgz
Source34: http://registry.npmjs.org/http-signature/-/http-signature-1.2.0.tgz
Source35: http://registry.npmjs.org/hawk/-/hawk-6.0.2.tgz
Source36: http://registry.npmjs.org/oauth-sign/-/oauth-sign-0.8.2.tgz
Source37: http://registry.npmjs.org/mime-types/-/mime-types-2.1.17.tgz
Source38: http://registry.npmjs.org/performance-now/-/performance-now-2.1.0.tgz
Source39: http://registry.npmjs.org/safe-buffer/-/safe-buffer-5.1.1.tgz
Source40: http://registry.npmjs.org/qs/-/qs-6.5.1.tgz
Source41: http://registry.npmjs.org/stringstream/-/stringstream-0.0.5.tgz
Source42: http://registry.npmjs.org/tunnel-agent/-/tunnel-agent-0.6.0.tgz
Source43: http://registry.npmjs.org/uuid/-/uuid-3.1.0.tgz
Source44: http://registry.npmjs.org/punycode/-/punycode-1.4.1.tgz
Source45: http://registry.npmjs.org/prelude-ls/-/prelude-ls-1.1.2.tgz
Source46: http://registry.npmjs.org/deep-is/-/deep-is-0.1.3.tgz
Source47: http://registry.npmjs.org/wordwrap/-/wordwrap-1.0.0.tgz
Source48: http://registry.npmjs.org/type-check/-/type-check-0.3.2.tgz
Source49: http://registry.npmjs.org/levn/-/levn-0.3.0.tgz
Source50: http://registry.npmjs.org/delayed-stream/-/delayed-stream-1.0.0.tgz
Source51: http://registry.npmjs.org/fast-levenshtein/-/fast-levenshtein-2.0.6.tgz
Source52: http://registry.npmjs.org/asynckit/-/asynckit-0.4.0.tgz
Source53: http://registry.npmjs.org/assert-plus/-/assert-plus-1.0.0.tgz
Source54: http://registry.npmjs.org/har-schema/-/har-schema-2.0.0.tgz
Source55: http://registry.npmjs.org/whatwg-url/-/whatwg-url-4.8.0.tgz
Source56: http://registry.npmjs.org/jsprim/-/jsprim-1.4.1.tgz
Source57: http://registry.npmjs.org/sshpk/-/sshpk-1.13.1.tgz
Source58: http://registry.npmjs.org/cryptiles/-/cryptiles-3.1.2.tgz
Source59: http://registry.npmjs.org/sntp/-/sntp-2.1.0.tgz
Source60: http://registry.npmjs.org/boom/-/boom-4.3.1.tgz
Source61: http://registry.npmjs.org/hoek/-/hoek-4.2.0.tgz
Source62: http://registry.npmjs.org/mime-db/-/mime-db-1.30.0.tgz
Source63: http://registry.npmjs.org/extsprintf/-/extsprintf-1.3.0.tgz
Source64: http://registry.npmjs.org/webidl-conversions/-/webidl-conversions-3.0.1.tgz
Source65: http://registry.npmjs.org/asn1/-/asn1-0.2.3.tgz
Source66: http://registry.npmjs.org/verror/-/verror-1.10.0.tgz
Source67: http://registry.npmjs.org/tr46/-/tr46-0.0.3.tgz
Source68: http://registry.npmjs.org/json-schema/-/json-schema-0.2.3.tgz
Source69: http://registry.npmjs.org/whatwg-encoding/-/whatwg-encoding-1.0.3.tgz
Source70: http://registry.npmjs.org/getpass/-/getpass-0.1.7.tgz
Source71: http://registry.npmjs.org/jsbn/-/jsbn-0.1.1.tgz
Source72: http://registry.npmjs.org/dashdash/-/dashdash-1.14.1.tgz
Source73: http://registry.npmjs.org/ecc-jsbn/-/ecc-jsbn-0.1.1.tgz
Source74: http://registry.npmjs.org/bcrypt-pbkdf/-/bcrypt-pbkdf-1.0.1.tgz
Source75: http://registry.npmjs.org/tweetnacl/-/tweetnacl-0.14.5.tgz
Source76: http://registry.npmjs.org/boom/-/boom-5.2.0.tgz
Source77: http://registry.npmjs.org/core-util-is/-/core-util-is-1.0.2.tgz
Source78: http://registry.npmjs.org/iconv-lite/-/iconv-lite-0.4.19.tgz
Source79: http://registry.npmjs.org/ajv/-/ajv-5.3.0.tgz
Source80: http://registry.npmjs.org/fast-deep-equal/-/fast-deep-equal-1.0.0.tgz
Source81: http://registry.npmjs.org/json-schema-traverse/-/json-schema-traverse-0.3.1.tgz
Source82: http://registry.npmjs.org/fast-json-stable-stringify/-/fast-json-stable-stringify-2.0.0.tgz
Source83: http://registry.npmjs.org/co/-/co-4.6.0.tgz
Source84: jsdom-9.12.0-registry.npmjs.org.tgz
BuildRequires: nodejs-packaging
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: npm(%{npm_name}) = %{version}
Provides: bundled(npm(jsdom)) = 9.12.0
Provides: bundled(npm(array-equal)) = 1.0.0
Provides: bundled(npm(escodegen)) = 1.9.0
Provides: bundled(npm(content-type-parser)) = 1.0.2
Provides: bundled(npm(cssstyle)) = 0.2.37
Provides: bundled(npm(html-encoding-sniffer)) = 1.0.2
Provides: bundled(npm(parse5)) = 1.5.1
Provides: bundled(npm(nwmatcher)) = 1.4.3
Provides: bundled(npm(request)) = 2.83.0
Provides: bundled(npm(sax)) = 1.2.4
Provides: bundled(npm(abab)) = 1.0.4
Provides: bundled(npm(cssom)) = 0.3.2
Provides: bundled(npm(tough-cookie)) = 2.3.3
Provides: bundled(npm(acorn-globals)) = 3.1.0
Provides: bundled(npm(webidl-conversions)) = 4.0.2
Provides: bundled(npm(symbol-tree)) = 3.2.2
Provides: bundled(npm(acorn)) = 4.0.13
Provides: bundled(npm(esutils)) = 2.0.2
Provides: bundled(npm(estraverse)) = 4.2.0
Provides: bundled(npm(esprima)) = 3.1.3
Provides: bundled(npm(aws-sign2)) = 0.7.0
Provides: bundled(npm(optionator)) = 0.8.2
Provides: bundled(npm(caseless)) = 0.12.0
Provides: bundled(npm(source-map)) = 0.5.7
Provides: bundled(npm(aws4)) = 1.6.0
Provides: bundled(npm(combined-stream)) = 1.0.5
Provides: bundled(npm(forever-agent)) = 0.6.1
Provides: bundled(npm(extend)) = 3.0.1
Provides: bundled(npm(form-data)) = 2.3.1
Provides: bundled(npm(har-validator)) = 5.0.3
Provides: bundled(npm(xml-name-validator)) = 2.0.1
Provides: bundled(npm(is-typedarray)) = 1.0.0
Provides: bundled(npm(isstream)) = 0.1.2
Provides: bundled(npm(json-stringify-safe)) = 5.0.1
Provides: bundled(npm(http-signature)) = 1.2.0
Provides: bundled(npm(hawk)) = 6.0.2
Provides: bundled(npm(oauth-sign)) = 0.8.2
Provides: bundled(npm(mime-types)) = 2.1.17
Provides: bundled(npm(performance-now)) = 2.1.0
Provides: bundled(npm(safe-buffer)) = 5.1.1
Provides: bundled(npm(qs)) = 6.5.1
Provides: bundled(npm(stringstream)) = 0.0.5
Provides: bundled(npm(tunnel-agent)) = 0.6.0
Provides: bundled(npm(uuid)) = 3.1.0
Provides: bundled(npm(punycode)) = 1.4.1
Provides: bundled(npm(prelude-ls)) = 1.1.2
Provides: bundled(npm(deep-is)) = 0.1.3
Provides: bundled(npm(wordwrap)) = 1.0.0
Provides: bundled(npm(type-check)) = 0.3.2
Provides: bundled(npm(levn)) = 0.3.0
Provides: bundled(npm(delayed-stream)) = 1.0.0
Provides: bundled(npm(fast-levenshtein)) = 2.0.6
Provides: bundled(npm(asynckit)) = 0.4.0
Provides: bundled(npm(assert-plus)) = 1.0.0
Provides: bundled(npm(har-schema)) = 2.0.0
Provides: bundled(npm(whatwg-url)) = 4.8.0
Provides: bundled(npm(jsprim)) = 1.4.1
Provides: bundled(npm(sshpk)) = 1.13.1
Provides: bundled(npm(cryptiles)) = 3.1.2
Provides: bundled(npm(sntp)) = 2.1.0
Provides: bundled(npm(boom)) = 4.3.1
Provides: bundled(npm(hoek)) = 4.2.0
Provides: bundled(npm(mime-db)) = 1.30.0
Provides: bundled(npm(extsprintf)) = 1.3.0
Provides: bundled(npm(webidl-conversions)) = 3.0.1
Provides: bundled(npm(asn1)) = 0.2.3
Provides: bundled(npm(verror)) = 1.10.0
Provides: bundled(npm(tr46)) = 0.0.3
Provides: bundled(npm(json-schema)) = 0.2.3
Provides: bundled(npm(whatwg-encoding)) = 1.0.3
Provides: bundled(npm(getpass)) = 0.1.7
Provides: bundled(npm(jsbn)) = 0.1.1
Provides: bundled(npm(dashdash)) = 1.14.1
Provides: bundled(npm(ecc-jsbn)) = 0.1.1
Provides: bundled(npm(bcrypt-pbkdf)) = 1.0.1
Provides: bundled(npm(tweetnacl)) = 0.14.5
Provides: bundled(npm(boom)) = 5.2.0
Provides: bundled(npm(core-util-is)) = 1.0.2
Provides: bundled(npm(iconv-lite)) = 0.4.19
Provides: bundled(npm(ajv)) = 5.3.0
Provides: bundled(npm(fast-deep-equal)) = 1.0.0
Provides: bundled(npm(json-schema-traverse)) = 0.3.1
Provides: bundled(npm(fast-json-stable-stringify)) = 2.0.0
Provides: bundled(npm(co)) = 4.6.0
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

%setup -T -q -a 84 -D -n %{npm_cache_dir}

%build
npm install --cache-min Infinity --cache %{npm_cache_dir} --no-optional --global-style true %{npm_name}@%{version}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cd node_modules/jsdom
cp -pfr Changelog.md LICENSE.txt README.md lib package.json node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pf Changelog.md LICENSE.txt README.md LICENSE.txt ../../

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%endif

%files
%{nodejs_sitelib}/%{npm_name}

%license LICENSE.txt
%doc Changelog.md
%doc LICENSE.txt
%doc README.md

%changelog
* Tue Nov 07 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 9.12.0-1
- new package built with tito

