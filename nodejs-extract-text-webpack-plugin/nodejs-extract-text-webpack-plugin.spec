%global npm_name extract-text-webpack-plugin

Name: nodejs-%{npm_name}
Version: 1.0.1
Release: 1%{?dist}
Summary: Extract text from bundle into a file
License: MIT
Group: Development/Libraries
URL: http://github.com/webpack/extract-text-webpack-plugin
Source0: http://registry.npmjs.org/extract-text-webpack-plugin/-/extract-text-webpack-plugin-1.0.1.tgz
Source1: http://registry.npmjs.org/loader-utils/-/loader-utils-0.2.15.tgz
Source2: http://registry.npmjs.org/async/-/async-1.5.2.tgz
Source3: http://registry.npmjs.org/emojis-list/-/emojis-list-2.0.1.tgz
Source4: http://registry.npmjs.org/big.js/-/big.js-3.1.3.tgz
Source5: http://registry.npmjs.org/json5/-/json5-0.5.0.tgz
Source6: http://registry.npmjs.org/object-assign/-/object-assign-4.1.0.tgz
Source7: http://registry.npmjs.org/webpack-sources/-/webpack-sources-0.1.2.tgz
Source8: http://registry.npmjs.org/source-list-map/-/source-list-map-0.1.6.tgz
Source9: http://registry.npmjs.org/source-map/-/source-map-0.5.6.tgz
Source10: extract-text-webpack-plugin-1.0.1-registry.npmjs.org.tgz
Requires: nodejs(engine)
Requires: npm(webpack)
BuildRequires: nodejs-devel
BuildRequires: nodejs-packaging
BuildRequires: npm
BuildRequires: npm(webpack)
BuildArch: noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif
Provides: npm(%{npm_name}) = %{version}
Provides: bundled-npm(extract-text-webpack-plugin) = 1.0.1
Provides: bundled-npm(loader-utils) = 0.2.15
Provides: bundled-npm(async) = 1.5.2
Provides: bundled-npm(emojis-list) = 2.0.1
Provides: bundled-npm(big.js) = 3.1.3
Provides: bundled-npm(json5) = 0.5.0
Provides: bundled-npm(object-assign) = 4.1.0
Provides: bundled-npm(webpack-sources) = 0.1.2
Provides: bundled-npm(source-list-map) = 0.1.6
Provides: bundled-npm(source-map) = 0.5.6
AutoReq: no
AutoProv: no


%description
Extract text from bundle into a file.

%prep
mkdir npm_cache
for tgz in %{sources}; do
  echo $tgz | grep -q registry.npmjs.org || npm cache add --cache ./npm_cache $tgz
done

%setup -T -q -a 10 -D -n npm_cache

%build
mkdir node_modules
# Notice I make regular symlinks instead of running npm link, as the latter will ask for
# root permissions
ln -s %{nodejs_sitelib}/* node_modules/
npm install --cache-min Infinity --cache . extract-text-webpack-plugin@1.0.1

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cd node_modules/extract-text-webpack-plugin
cp -pfr .editorconfig .eslintrc .npmignore .travis.yml ExtractedModule.js OrderUndefinedError.js index.js loader.js package.json node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}

%check

%files
%{nodejs_sitelib}/%{npm_name}

%changelog
* Wed Aug 31 2016 Dominic Cleal <dominic@cleal.org> 1.0.1-1
- new package built with tito

