%global npm_name babel-plugin-transform-object-assign

%{?nodejs_find_provides_and_requires}

Name: nodejs-%{npm_name}
Version: 6.8.0
Release: 1%{?dist}
Summary: Replace Object.assign with an inline helper
License: MIT
URL: http://babeljs.io/
Source0: http://registry.npmjs.org/babel-plugin-transform-object-assign/-/babel-plugin-transform-object-assign-6.8.0.tgz
Source1: http://registry.npmjs.org/babel-runtime/-/babel-runtime-6.11.6.tgz
Source2: http://registry.npmjs.org/regenerator-runtime/-/regenerator-runtime-0.9.5.tgz
Source3: http://registry.npmjs.org/core-js/-/core-js-2.4.1.tgz
Source4: babel-plugin-transform-object-assign-6.8.0-registry.npmjs.org.tgz
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
Provides: bundled(npm(babel-plugin-transform-object-assign)) = 6.8.0
Provides: bundled(npm(babel-runtime)) = 6.11.6
Provides: bundled(npm(regenerator-runtime)) = 0.9.5
Provides: bundled(npm(core-js)) = 2.4.1
AutoReq: no
AutoProv: no

%description
%{summary}

%prep
mkdir npm_cache
for tgz in %{sources}; do
  echo $tgz | grep -q registry.npmjs.org || npm cache add --cache ./npm_cache $tgz
done

%setup -T -q -a 4 -D -n npm_cache

%build
npm install --cache-min Infinity --cache . --global-style true %{npm_name}@%{version}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cd node_modules/babel-plugin-transform-object-assign
cp -pfr .npmignore LICENSE README.md lib package.json node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pf LICENSE README.md ../../

%files
%{nodejs_sitelib}/%{npm_name}

%doc LICENSE
%doc README.md

%changelog
* Fri Oct 14 2016 Dominic Cleal <dominic@cleal.org> 6.8.0-1
- new package built with tito

