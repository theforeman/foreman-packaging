%global npm_name sass-loader

%{?nodejs_find_provides_and_requires}

Name: nodejs-%{npm_name}
Version: 4.1.1
Release: 1%{?dist}
Summary: Sass loader for webpack
License: MIT
URL: https://github.com/jtangelder/sass-loader
Source0: http://registry.npmjs.org/sass-loader/-/sass-loader-4.1.1.tgz
Source1: http://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz
Source2: http://registry.npmjs.org/loader-utils/-/loader-utils-0.2.17.tgz
Source3: http://registry.npmjs.org/async/-/async-2.1.5.tgz
Source4: http://registry.npmjs.org/emojis-list/-/emojis-list-2.1.0.tgz
Source5: http://registry.npmjs.org/big.js/-/big.js-3.1.3.tgz
Source6: http://registry.npmjs.org/json5/-/json5-0.5.1.tgz
Source7: http://registry.npmjs.org/lodash/-/lodash-4.17.4.tgz
Source8: sass-loader-4.1.1-registry.npmjs.org.tgz
Requires: nodejs(engine)
BuildRequires: nodejs-devel
BuildRequires: nodejs-packaging
BuildRequires: npm
BuildRequires: npm(node-sass) >= 3.4.2
BuildRequires: npm(node-sass) < 5
BuildRequires: npm(webpack) >= 1.12.6
BuildRequires: npm(webpack) < 3
BuildArch: noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif
Provides: npm(%{npm_name}) = %{version}
Provides: bundled-npm(sass-loader) = 4.1.1
Provides: bundled-npm(object-assign) = 4.1.1
Provides: bundled-npm(loader-utils) = 0.2.17
Provides: bundled-npm(async) = 2.1.5
Provides: bundled-npm(emojis-list) = 2.1.0
Provides: bundled-npm(big.js) = 3.1.3
Provides: bundled-npm(json5) = 0.5.1
Provides: bundled-npm(lodash) = 4.17.4
AutoReq: no
AutoProv: no


%description
%{summary}

%prep
mkdir npm_cache
for tgz in %{sources}; do
  echo $tgz | grep -q registry.npmjs.org || npm cache add --cache ./npm_cache $tgz
done

%setup -T -q -a 8 -D -n npm_cache

%build
mkdir node_modules
ln -s %{nodejs_sitelib}/{node-sass,webpack} node_modules/
npm install --cache-min Infinity --cache . --no-optional --global-style true %{npm_name}@%{version}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cd node_modules/sass-loader
cp -pfr .editorconfig .jshintignore .jshintrc .npmignore .travis.yml CHANGELOG.md LICENSE README.md index.js package.json node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pf CHANGELOG.md LICENSE README.md ../../

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE
%doc CHANGELOG.md
%doc README.md

%changelog
