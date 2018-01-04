%global npm_name isomorphic-fetch

Name: nodejs-%{npm_name}
Version: 2.2.1
Release: 1%{?dist}
Summary: Isomorphic WHATWG Fetch API, for Node & Browserify
License: MIT
Group: Development/Libraries
URL: https://github.com/matthew-andrews/isomorphic-fetch/issues
Source0: https://registry.npmjs.org/isomorphic-fetch/-/isomorphic-fetch-2.2.1.tgz
Source1: https://registry.npmjs.org/node-fetch/-/node-fetch-1.7.3.tgz
Source2: https://registry.npmjs.org/whatwg-fetch/-/whatwg-fetch-2.0.3.tgz
Source3: https://registry.npmjs.org/encoding/-/encoding-0.1.12.tgz
Source4: https://registry.npmjs.org/is-stream/-/is-stream-1.1.0.tgz
Source5: https://registry.npmjs.org/iconv-lite/-/iconv-lite-0.4.19.tgz
Source6: isomorphic-fetch-2.2.1-registry.npmjs.org.tgz
BuildRequires: nodejs-packaging
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: npm(%{npm_name}) = %{version}
Provides: bundled-npm(isomorphic-fetch) = 2.2.1
Provides: bundled-npm(node-fetch) = 1.7.3
Provides: bundled-npm(whatwg-fetch) = 2.0.3
Provides: bundled-npm(encoding) = 0.1.12
Provides: bundled-npm(is-stream) = 1.1.0
Provides: bundled-npm(iconv-lite) = 0.4.19
AutoReq: no
AutoProv: no

%define npm_cache_dir /tmp/npm_cache_%{name}-%{version}-%{release}
%description
%{summary}

%prep
mkdir -p %{npm_cache_dir}
for tgz in %{sources}; do
  echo $tgz | grep -q registry.npmjs.org || npm cache add --cache %{npm_cache_dir} $tgz
done

%setup -T -q -a 6 -D -n %{npm_cache_dir}

%build
npm install --cache-min Infinity --cache %{npm_cache_dir} --no-optional --global-style true %{npm_name}@%{version}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cd node_modules/isomorphic-fetch
cp -pfr .editorconfig .jshintrc .npmignore .travis.yml LICENSE README.md bower.json fetch-bower.js fetch-npm-browserify.js fetch-npm-node.js package.json test node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pf README.md LICENSE ../../

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}

%license LICENSE
%doc README.md

%changelog
* Thu Jan 04 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 2.2.1-1
- new package built with tito

