%global npm_name react-redux

%{?nodejs_find_provides_and_requires}

Name: nodejs-%{npm_name}
Version: 5.0.2
Release: 1%{?dist}
Summary: Official React bindings for Redux
License: MIT
URL: https://github.com/gaearon/react-redux
Source0: http://registry.npmjs.org/react-redux/-/react-redux-5.0.2.tgz
Source1: http://registry.npmjs.org/loose-envify/-/loose-envify-1.3.1.tgz
Source2: http://registry.npmjs.org/invariant/-/invariant-2.2.2.tgz
Source3: http://registry.npmjs.org/lodash/-/lodash-4.17.4.tgz
Source4: http://registry.npmjs.org/lodash-es/-/lodash-es-4.17.4.tgz
Source5: http://registry.npmjs.org/js-tokens/-/js-tokens-3.0.1.tgz
Source6: http://registry.npmjs.org/hoist-non-react-statics/-/hoist-non-react-statics-1.2.0.tgz
Source7: react-redux-5.0.2-registry.npmjs.org.tgz
Requires: nodejs(engine)
BuildRequires: nodejs-devel
BuildRequires: nodejs-packaging
BuildRequires: npm(react) >= 0.14.0
BuildRequires: npm(react) < 16.0.0
BuildRequires: npm(redux) >= 2.0.0
BuildRequires: npm(redux) < 4.0.0
BuildRequires: npm
BuildArch: noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif
Provides: npm(%{npm_name}) = %{version}
Provides: bundled-npm(react-redux) = 5.0.2
Provides: bundled-npm(loose-envify) = 1.3.1
Provides: bundled-npm(invariant) = 2.2.2
Provides: bundled-npm(lodash) = 4.17.4
Provides: bundled-npm(lodash-es) = 4.17.4
Provides: bundled-npm(js-tokens) = 3.0.1
Provides: bundled-npm(hoist-non-react-statics) = 1.2.0
AutoReq: no
AutoProv: no

%description
%{summary}

%prep
mkdir npm_cache
for tgz in %{sources}; do
  echo $tgz | grep -q registry.npmjs.org || npm cache add --cache ./npm_cache $tgz
done

%setup -T -q -a 7 -D -n npm_cache

%build
mkdir node_modules
ln -s %{nodejs_sitelib}/{react,redux} node_modules/
npm install --cache-min Infinity --cache . --no-optional --global-style true %{npm_name}@%{version}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cd node_modules/react-redux
cp -pfr CHANGELOG.md LICENSE.md README.md dist es lib package.json src node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pf CHANGELOG.md LICENSE.md README.md ../../

%files
%{nodejs_sitelib}/%{npm_name}
%doc CHANGELOG.md
%license LICENSE.md
%doc README.md

%changelog
* Thu Feb 16 2017 Dominic Cleal <dominic@cleal.org> 5.0.2-1
- new package built with tito

