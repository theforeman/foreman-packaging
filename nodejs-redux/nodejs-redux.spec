%global npm_name redux

%{?nodejs_find_provides_and_requires}

Name: nodejs-%{npm_name}
Version: 3.6.0
Release: 1%{?dist}
Summary: Predictable state container for JavaScript apps
License: MIT
URL: http://redux.js.org
Source0: http://registry.npmjs.org/redux/-/redux-3.6.0.tgz
Source1: http://registry.npmjs.org/loose-envify/-/loose-envify-1.3.1.tgz
Source2: http://registry.npmjs.org/lodash-es/-/lodash-es-4.17.4.tgz
Source3: http://registry.npmjs.org/symbol-observable/-/symbol-observable-1.0.4.tgz
Source4: http://registry.npmjs.org/lodash/-/lodash-4.17.4.tgz
Source5: http://registry.npmjs.org/js-tokens/-/js-tokens-3.0.1.tgz
Source6: redux-3.6.0-registry.npmjs.org.tgz
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
Provides: bundled-npm(redux) = 3.6.0
Provides: bundled-npm(loose-envify) = 1.3.1
Provides: bundled-npm(lodash-es) = 4.17.4
Provides: bundled-npm(symbol-observable) = 1.0.4
Provides: bundled-npm(lodash) = 4.17.4
Provides: bundled-npm(js-tokens) = 3.0.1
AutoReq: no
AutoProv: no

%description
%{summary}

%prep
mkdir npm_cache
for tgz in %{sources}; do
  echo $tgz | grep -q registry.npmjs.org || npm cache add --cache ./npm_cache $tgz
done

%setup -T -q -a 6 -D -n npm_cache

%build
npm install --cache-min Infinity --cache . --no-optional --global-style true %{npm_name}@%{version}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cd node_modules/redux
cp -pfr CHANGELOG.md LICENSE.md README.md dist es index.d.ts lib package.json src node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pf CHANGELOG.md LICENSE.md README.md ../../

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE.md
%doc CHANGELOG.md
%doc README.md

%changelog
* Thu Feb 16 2017 Dominic Cleal <dominic@cleal.org> 3.6.0-1
- new package built with tito

