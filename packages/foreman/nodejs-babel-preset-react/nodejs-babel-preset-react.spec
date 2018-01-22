%global npm_name babel-preset-react

%{?nodejs_find_provides_and_requires}

Name: nodejs-%{npm_name}
Version: 6.16.0
Release: 1%{?dist}
Summary: Babel preset for all React plugins
License: MIT
URL: https://babeljs.io/
Source0: http://registry.npmjs.org/babel-preset-react/-/babel-preset-react-6.16.0.tgz
Source1: http://registry.npmjs.org/babel-plugin-transform-react-display-name/-/babel-plugin-transform-react-display-name-6.8.0.tgz
Source2: http://registry.npmjs.org/babel-plugin-transform-react-jsx-self/-/babel-plugin-transform-react-jsx-self-6.11.0.tgz
Source3: http://registry.npmjs.org/babel-plugin-syntax-jsx/-/babel-plugin-syntax-jsx-6.13.0.tgz
Source4: http://registry.npmjs.org/babel-plugin-transform-flow-strip-types/-/babel-plugin-transform-flow-strip-types-6.14.0.tgz
Source5: http://registry.npmjs.org/babel-plugin-transform-react-jsx/-/babel-plugin-transform-react-jsx-6.8.0.tgz
Source6: http://registry.npmjs.org/babel-plugin-transform-react-jsx-source/-/babel-plugin-transform-react-jsx-source-6.9.0.tgz
Source7: http://registry.npmjs.org/babel-plugin-syntax-flow/-/babel-plugin-syntax-flow-6.13.0.tgz
Source8: http://registry.npmjs.org/babel-runtime/-/babel-runtime-6.11.6.tgz
Source9: http://registry.npmjs.org/core-js/-/core-js-2.4.1.tgz
Source10: http://registry.npmjs.org/babel-helper-builder-react-jsx/-/babel-helper-builder-react-jsx-6.9.0.tgz
Source11: http://registry.npmjs.org/esutils/-/esutils-2.0.2.tgz
Source12: http://registry.npmjs.org/regenerator-runtime/-/regenerator-runtime-0.9.5.tgz
Source13: http://registry.npmjs.org/babel-types/-/babel-types-6.16.0.tgz
Source14: http://registry.npmjs.org/lodash/-/lodash-4.16.4.tgz
Source15: http://registry.npmjs.org/to-fast-properties/-/to-fast-properties-1.0.2.tgz
Source16: babel-preset-react-6.16.0-registry.npmjs.org.tgz
Requires: nodejs(engine)
BuildRequires: npm
BuildRequires: nodejs-packaging
BuildArch:  noarch

%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

Provides: npm(%{npm_name}) = %{version}
Provides: bundled(npm(babel-preset-react)) = 6.16.0
Provides: bundled(npm(babel-plugin-transform-react-display-name)) = 6.8.0
Provides: bundled(npm(babel-plugin-transform-react-jsx-self)) = 6.11.0
Provides: bundled(npm(babel-plugin-syntax-jsx)) = 6.13.0
Provides: bundled(npm(babel-plugin-transform-flow-strip-types)) = 6.14.0
Provides: bundled(npm(babel-plugin-transform-react-jsx)) = 6.8.0
Provides: bundled(npm(babel-plugin-transform-react-jsx-source)) = 6.9.0
Provides: bundled(npm(babel-plugin-syntax-flow)) = 6.13.0
Provides: bundled(npm(babel-runtime)) = 6.11.6
Provides: bundled(npm(core-js)) = 2.4.1
Provides: bundled(npm(babel-helper-builder-react-jsx)) = 6.9.0
Provides: bundled(npm(esutils)) = 2.0.2
Provides: bundled(npm(regenerator-runtime)) = 0.9.5
Provides: bundled(npm(babel-types)) = 6.16.0
Provides: bundled(npm(lodash)) = 4.16.4
Provides: bundled(npm(to-fast-properties)) = 1.0.2
AutoReq: no
AutoProv: no

%description
%{summary}

%prep
mkdir npm_cache
for tgz in %{sources}; do
  echo $tgz | grep -q registry.npmjs.org || npm cache add --cache ./npm_cache $tgz
done

%setup -T -q -a 16 -D -n npm_cache

%build
npm install --cache-min Infinity --cache . --global-style true %{npm_name}@%{version}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cd node_modules/babel-preset-react
cp -pfr .npmignore README.md lib package.json node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pf README.md ../../

%files
%{nodejs_sitelib}/%{npm_name}
%doc README.md

%changelog
* Fri Oct 14 2016 Dominic Cleal <dominic@cleal.org> 6.16.0-1
- new package built with tito

