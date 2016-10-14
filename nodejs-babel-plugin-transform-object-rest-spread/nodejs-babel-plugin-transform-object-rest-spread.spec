%global npm_name babel-plugin-transform-object-rest-spread

%{?nodejs_find_provides_and_requires}

Name: nodejs-%{npm_name}
Version: 6.16.0
Release: 1%{?dist}
Summary: Compile object rest and spread to ES5
License: MIT
URL: http://babeljs.io/
Source0: http://registry.npmjs.org/babel-plugin-transform-object-rest-spread/-/babel-plugin-transform-object-rest-spread-6.16.0.tgz
Source1: http://registry.npmjs.org/babel-plugin-syntax-object-rest-spread/-/babel-plugin-syntax-object-rest-spread-6.13.0.tgz
Source2: http://registry.npmjs.org/babel-runtime/-/babel-runtime-6.11.6.tgz
Source3: http://registry.npmjs.org/regenerator-runtime/-/regenerator-runtime-0.9.5.tgz
Source4: http://registry.npmjs.org/core-js/-/core-js-2.4.1.tgz
Source5: babel-plugin-transform-object-rest-spread-6.16.0-registry.npmjs.org.tgz
Requires: nodejs(engine)
BuildRequires: nodejs-packaging
BuildRequires: npm
BuildArch:  noarch

%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

Provides: npm(%{npm_name}) = %{version}
Provides: bundled-npm(babel-plugin-transform-object-rest-spread) = 6.16.0
Provides: bundled-npm(babel-plugin-syntax-object-rest-spread) = 6.13.0
Provides: bundled-npm(babel-runtime) = 6.11.6
Provides: bundled-npm(regenerator-runtime) = 0.9.5
Provides: bundled-npm(core-js) = 2.4.1
AutoReq: no
AutoProv: no

%description
%{summary}

%prep
mkdir npm_cache
for tgz in %{sources}; do
  echo $tgz | grep -q registry.npmjs.org || npm cache add --cache ./npm_cache $tgz
done

%setup -T -q -a 5 -D -n npm_cache

%build
npm install --cache-min Infinity --cache . --global-style true %{npm_name}@%{version}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cd node_modules/babel-plugin-transform-object-rest-spread
cp -pfr .npmignore README.md lib package.json node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pf README.md ../../

%files
%{nodejs_sitelib}/%{npm_name}
%doc README.md

%changelog
* Fri Oct 14 2016 Dominic Cleal <dominic@cleal.org> 6.16.0-1
- new package built with tito

