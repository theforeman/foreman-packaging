%global npm_name react-bootstrap

%{?nodejs_find_provides_and_requires}

Name: nodejs-%{npm_name}
Version: 0.30.5
Release: 2%{?dist}
Summary: Bootstrap 3 components built with React
License: MIT
URL: https://react-bootstrap.github.io/
Source0: http://registry.npmjs.org/react-bootstrap/-/react-bootstrap-0.30.5.tgz
Source1: http://registry.npmjs.org/invariant/-/invariant-2.2.1.tgz
Source2: http://registry.npmjs.org/classnames/-/classnames-2.2.5.tgz
Source3: http://registry.npmjs.org/babel-runtime/-/babel-runtime-6.11.6.tgz
Source4: http://registry.npmjs.org/loose-envify/-/loose-envify-1.2.0.tgz
Source5: http://registry.npmjs.org/regenerator-runtime/-/regenerator-runtime-0.9.5.tgz
Source6: http://registry.npmjs.org/core-js/-/core-js-2.4.1.tgz
Source7: http://registry.npmjs.org/js-tokens/-/js-tokens-1.0.3.tgz
Source8: http://registry.npmjs.org/react-overlays/-/react-overlays-0.6.10.tgz
Source9: http://registry.npmjs.org/dom-helpers/-/dom-helpers-2.4.0.tgz
Source10: http://registry.npmjs.org/react-prop-types/-/react-prop-types-0.4.0.tgz
Source11: http://registry.npmjs.org/keycode/-/keycode-2.1.7.tgz
Source12: http://registry.npmjs.org/warning/-/warning-3.0.0.tgz
Source13: http://registry.npmjs.org/uncontrollable/-/uncontrollable-4.0.3.tgz
Source14: react-bootstrap-0.30.5-registry.npmjs.org.tgz
Requires: nodejs(engine)
BuildRequires: npm
BuildRequires: nodejs-packaging
BuildRequires: npm(react) >= 0.14.0
BuildRequires: npm(react-dom) >= 0.14.0
BuildArch:  noarch

%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

Provides: npm(%{npm_name}) = %{version}
Provides: bundled-npm(react-bootstrap) = 0.30.5
Provides: bundled-npm(invariant) = 2.2.1
Provides: bundled-npm(classnames) = 2.2.5
Provides: bundled-npm(babel-runtime) = 6.11.6
Provides: bundled-npm(loose-envify) = 1.2.0
Provides: bundled-npm(regenerator-runtime) = 0.9.5
Provides: bundled-npm(core-js) = 2.4.1
Provides: bundled-npm(js-tokens) = 1.0.3
Provides: bundled-npm(react-overlays) = 0.6.10
Provides: bundled-npm(dom-helpers) = 2.4.0
Provides: bundled-npm(react-prop-types) = 0.4.0
Provides: bundled-npm(keycode) = 2.1.7
Provides: bundled-npm(warning) = 3.0.0
Provides: bundled-npm(uncontrollable) = 4.0.3
AutoReq: no
AutoProv: no

%description
%{summary}

%prep
mkdir npm_cache
for tgz in %{sources}; do
  echo $tgz | grep -q registry.npmjs.org || npm cache add --cache ./npm_cache $tgz
done

%setup -T -q -a 14 -D -n npm_cache

%build
mkdir node_modules
ln -s %{nodejs_sitelib}/{react,react-dom} node_modules/
npm install --cache-min Infinity --cache . --global-style true %{npm_name}@%{version}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cd node_modules/react-bootstrap
cp -pfr CHANGELOG.md LICENSE README.md dist es lib package.json node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pf CHANGELOG.md LICENSE README.md ../../

%files
%{nodejs_sitelib}/%{npm_name}
%doc LICENSE
%doc CHANGELOG.md
%doc README.md

%changelog
* Fri Oct 14 2016 Dominic Cleal <dominic@cleal.org> 0.30.5-2
- Use existing react, react-dom peer dependencies (dominic@cleal.org)

* Fri Oct 14 2016 Dominic Cleal <dominic@cleal.org> 0.30.5-1
- new package built with tito

