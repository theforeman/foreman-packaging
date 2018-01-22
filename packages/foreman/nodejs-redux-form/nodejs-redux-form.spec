%global npm_name redux-form
%global enable_tests 0

Name: nodejs-%{npm_name}
Version: 7.2.0
Release: 1%{?dist}
Summary: A higher order component decorator for forms using Redux and React
License: MIT
URL: https://redux-form.com/
Source0: http://registry.npmjs.org/redux-form/-/redux-form-7.2.0.tgz
Source1: http://registry.npmjs.org/deep-equal/-/deep-equal-1.0.1.tgz
Source2: http://registry.npmjs.org/is-promise/-/is-promise-2.1.0.tgz
Source3: http://registry.npmjs.org/invariant/-/invariant-2.2.2.tgz
Source4: http://registry.npmjs.org/prop-types/-/prop-types-15.6.0.tgz
Source5: http://registry.npmjs.org/lodash/-/lodash-4.17.4.tgz
Source6: http://registry.npmjs.org/loose-envify/-/loose-envify-1.3.1.tgz
Source7: http://registry.npmjs.org/js-tokens/-/js-tokens-3.0.2.tgz
Source8: http://registry.npmjs.org/fbjs/-/fbjs-0.8.16.tgz
Source9: http://registry.npmjs.org/isomorphic-fetch/-/isomorphic-fetch-2.2.1.tgz
Source10: http://registry.npmjs.org/core-js/-/core-js-1.2.7.tgz
Source11: http://registry.npmjs.org/promise/-/promise-7.3.1.tgz
Source12: http://registry.npmjs.org/setimmediate/-/setimmediate-1.0.5.tgz
Source13: http://registry.npmjs.org/node-fetch/-/node-fetch-1.7.3.tgz
Source14: http://registry.npmjs.org/whatwg-fetch/-/whatwg-fetch-2.0.3.tgz
Source15: http://registry.npmjs.org/ua-parser-js/-/ua-parser-js-0.7.17.tgz
Source16: http://registry.npmjs.org/encoding/-/encoding-0.1.12.tgz
Source17: http://registry.npmjs.org/asap/-/asap-2.0.6.tgz
Source18: http://registry.npmjs.org/iconv-lite/-/iconv-lite-0.4.19.tgz
Source19: http://registry.npmjs.org/hoist-non-react-statics/-/hoist-non-react-statics-2.3.1.tgz
Source20: http://registry.npmjs.org/es6-error/-/es6-error-4.0.2.tgz
Source21: http://registry.npmjs.org/lodash-es/-/lodash-es-4.17.4.tgz
Source22: http://registry.npmjs.org/is-stream/-/is-stream-1.1.0.tgz
Source23: http://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz
Source24: redux-form-7.2.0-registry.npmjs.org.tgz
BuildRequires: nodejs-packaging
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: npm(%{npm_name}) = %{version}
Provides: bundled(npm(redux-form)) = 7.2.0
Provides: bundled(npm(deep-equal)) = 1.0.1
Provides: bundled(npm(is-promise)) = 2.1.0
Provides: bundled(npm(invariant)) = 2.2.2
Provides: bundled(npm(prop-types)) = 15.6.0
Provides: bundled(npm(lodash)) = 4.17.4
Provides: bundled(npm(loose-envify)) = 1.3.1
Provides: bundled(npm(js-tokens)) = 3.0.2
Provides: bundled(npm(fbjs)) = 0.8.16
Provides: bundled(npm(isomorphic-fetch)) = 2.2.1
Provides: bundled(npm(core-js)) = 1.2.7
Provides: bundled(npm(promise)) = 7.3.1
Provides: bundled(npm(setimmediate)) = 1.0.5
Provides: bundled(npm(node-fetch)) = 1.7.3
Provides: bundled(npm(whatwg-fetch)) = 2.0.3
Provides: bundled(npm(ua-parser-js)) = 0.7.17
Provides: bundled(npm(encoding)) = 0.1.12
Provides: bundled(npm(asap)) = 2.0.6
Provides: bundled(npm(iconv-lite)) = 0.4.19
Provides: bundled(npm(hoist-non-react-statics)) = 2.3.1
Provides: bundled(npm(es6-error)) = 4.0.2
Provides: bundled(npm(lodash-es)) = 4.17.4
Provides: bundled(npm(is-stream)) = 1.1.0
Provides: bundled(npm(object-assign)) = 4.1.1
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

%setup -T -q -a 24 -D -n %{npm_cache_dir}

%build
npm install --cache-min Infinity --cache %{npm_cache_dir} --no-optional --global-style true %{npm_name}@%{version}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cd node_modules/redux-form
cp -pfr CHANGELOG.md LICENSE README.md dist es immutable.js lib package.json node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pf CHANGELOG.md README.md LICENSE ../../

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}

%license LICENSE
%doc CHANGELOG.md
%doc README.md

%changelog
* Thu Jan 04 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 7.2.0-1
- Update redux-form to 7.1.2 (me@daniellobato.me)

* Tue Nov 07 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 7.1.2-1
- new package built with tito

