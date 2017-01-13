%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name flux

%{?nodejs_find_provides_and_requires}

Name: %{?scl_prefix}nodejs-%{npm_name}
Version: 2.1.1
Release: 1%{?dist}
Summary: An application architecture based on a unidirectional data flow
License: BSD
URL: http://facebook.github.io/flux/
Source0: http://registry.npmjs.org/flux/-/flux-2.1.1.tgz
Source1: http://registry.npmjs.org/fbemitter/-/fbemitter-2.1.1.tgz
Source2: http://registry.npmjs.org/immutable/-/immutable-3.8.1.tgz
Source3: http://registry.npmjs.org/fbjs/-/fbjs-0.8.5.tgz
Source4: http://registry.npmjs.org/fbjs/-/fbjs-0.1.0-alpha.7.tgz
Source5: http://registry.npmjs.org/loose-envify/-/loose-envify-1.2.0.tgz
Source6: http://registry.npmjs.org/object-assign/-/object-assign-4.1.0.tgz
Source7: http://registry.npmjs.org/promise/-/promise-7.1.1.tgz
Source8: http://registry.npmjs.org/core-js/-/core-js-1.2.7.tgz
Source9: http://registry.npmjs.org/js-tokens/-/js-tokens-1.0.3.tgz
Source10: http://registry.npmjs.org/whatwg-fetch/-/whatwg-fetch-0.9.0.tgz
Source11: http://registry.npmjs.org/asap/-/asap-2.0.5.tgz
Source12: http://registry.npmjs.org/ua-parser-js/-/ua-parser-js-0.7.10.tgz
Source13: http://registry.npmjs.org/isomorphic-fetch/-/isomorphic-fetch-2.2.1.tgz
Source14: http://registry.npmjs.org/whatwg-fetch/-/whatwg-fetch-1.0.0.tgz
Source15: http://registry.npmjs.org/node-fetch/-/node-fetch-1.6.3.tgz
Source16: http://registry.npmjs.org/is-stream/-/is-stream-1.1.0.tgz
Source17: http://registry.npmjs.org/encoding/-/encoding-0.1.12.tgz
Source18: http://registry.npmjs.org/iconv-lite/-/iconv-lite-0.4.13.tgz
Source19: flux-2.1.1-registry.npmjs.org.tgz
Requires: %{?scl_prefix_nodejs}nodejs(engine)
BuildRequires: %{?scl_prefix_nodejs}npm
BuildArch:  noarch

%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}
Provides: bundled-npm(flux) = 2.1.1
Provides: bundled-npm(fbemitter) = 2.1.1
Provides: bundled-npm(immutable) = 3.8.1
Provides: bundled-npm(fbjs) = 0.8.5
Provides: bundled-npm(fbjs) = 0.1.0-alpha.7
Provides: bundled-npm(loose-envify) = 1.2.0
Provides: bundled-npm(object-assign) = 4.1.0
Provides: bundled-npm(promise) = 7.1.1
Provides: bundled-npm(core-js) = 1.2.7
Provides: bundled-npm(js-tokens) = 1.0.3
Provides: bundled-npm(whatwg-fetch) = 0.9.0
Provides: bundled-npm(asap) = 2.0.5
Provides: bundled-npm(ua-parser-js) = 0.7.10
Provides: bundled-npm(isomorphic-fetch) = 2.2.1
Provides: bundled-npm(whatwg-fetch) = 1.0.0
Provides: bundled-npm(node-fetch) = 1.6.3
Provides: bundled-npm(is-stream) = 1.1.0
Provides: bundled-npm(encoding) = 0.1.12
Provides: bundled-npm(iconv-lite) = 0.4.13
AutoReq: no
AutoProv: no

%description
%{summary}

%prep
mkdir npm_cache
for tgz in %{sources}; do
  if [ $(echo $tgz | grep -q registry.npmjs.org) ];then
%{?scl:scl enable %{scl} - <<EOF}
npm cache add --cache ./npm_cache $tgz
%{?scl:EOF}
  fi
done

%setup -T -q -a 19 -D -n npm_cache

%build
%{?scl:scl enable %{scl} - <<EOF}
npm install --cache-min Infinity --cache . --global-style true %{npm_name}@%{version}
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cd node_modules/flux
cp -pfr LICENSE PATENTS README.md dist flow index.js lib package.json utils.js node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pf LICENSE PATENTS README.md ../../

%files
%{nodejs_sitelib}/%{npm_name}
%doc LICENSE
%doc PATENTS
%doc README.md

%changelog
* Fri Oct 14 2016 Dominic Cleal <dominic@cleal.org> 2.1.1-1
- new package built with tito

