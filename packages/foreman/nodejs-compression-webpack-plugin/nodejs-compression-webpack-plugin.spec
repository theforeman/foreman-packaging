%global npm_name compression-webpack-plugin

Name: nodejs-%{npm_name}
Version: 0.3.2
Release: 2%{?dist}
Summary: Prepare compressed versions of assets to serve them with Content-Encoding
License: MIT
URL: https://github.com/webpack/compression-webpack-plugin
Source0: http://registry.npmjs.org/compression-webpack-plugin/-/compression-webpack-plugin-0.3.2.tgz
Source1: http://registry.npmjs.org/async/-/async-0.2.10.tgz
Source2: http://registry.npmjs.org/webpack-sources/-/webpack-sources-0.1.4.tgz
Source3: http://registry.npmjs.org/source-list-map/-/source-list-map-0.1.8.tgz
Source4: http://registry.npmjs.org/source-map/-/source-map-0.5.6.tgz
Source5: compression-webpack-plugin-0.3.2-registry.npmjs.org.tgz
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
Provides: bundled(npm(compression-webpack-plugin)) = 0.3.2
Provides: bundled(npm(async)) = 0.2.10
Provides: bundled(npm(webpack-sources)) = 0.1.4
Provides: bundled(npm(source-list-map)) = 0.1.8
Provides: bundled(npm(source-map)) = 0.5.6
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
npm install --cache-min Infinity --cache . --no-optional --global-style true %{npm_name}@%{version}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cd node_modules/%{npm_name}
cp -pfr .gitattributes .npmignore README.md index.js package.json node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pf README.md ../../

%files
%{nodejs_sitelib}/%{npm_name}

%doc README.md

%changelog
* Thu Jan 26 2017 Dominic Cleal <dominic@cleal.org> 0.3.2-2
- Fix missing provides npm(name) (dominic@cleal.org)

* Thu Jan 26 2017 Dominic Cleal <dominic@cleal.org> 0.3.2-1
- new package built with tito

