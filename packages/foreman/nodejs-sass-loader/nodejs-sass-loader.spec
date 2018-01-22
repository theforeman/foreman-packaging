%global npm_name sass-loader
%global enable_tests 0

%{?nodejs_find_provides_and_requires}

Name: nodejs-%{npm_name}
Version: 6.0.6
Release: 1%{?dist}
Summary: Sass loader for webpack
License: MIT
URL: https://github.com/webpack-contrib/sass-loader
Source0: http://registry.npmjs.org/sass-loader/-/sass-loader-6.0.6.tgz
Source1: http://registry.npmjs.org/async/-/async-2.6.0.tgz
Source2: http://registry.npmjs.org/lodash/-/lodash-4.17.4.tgz
Source3: http://registry.npmjs.org/lodash.tail/-/lodash.tail-4.1.1.tgz
Source4: http://registry.npmjs.org/pify/-/pify-3.0.0.tgz
Source5: http://registry.npmjs.org/clone-deep/-/clone-deep-0.3.0.tgz
Source6: http://registry.npmjs.org/loader-utils/-/loader-utils-1.1.0.tgz
Source7: http://registry.npmjs.org/kind-of/-/kind-of-3.2.2.tgz
Source8: http://registry.npmjs.org/emojis-list/-/emojis-list-2.1.0.tgz
Source9: http://registry.npmjs.org/is-buffer/-/is-buffer-1.1.6.tgz
Source10: http://registry.npmjs.org/is-plain-object/-/is-plain-object-2.0.4.tgz
Source11: http://registry.npmjs.org/isobject/-/isobject-3.0.1.tgz
Source12: http://registry.npmjs.org/json5/-/json5-0.5.1.tgz
Source13: http://registry.npmjs.org/for-own/-/for-own-1.0.0.tgz
Source14: http://registry.npmjs.org/for-in/-/for-in-1.0.2.tgz
Source15: http://registry.npmjs.org/big.js/-/big.js-3.2.0.tgz
Source16: http://registry.npmjs.org/shallow-clone/-/shallow-clone-0.1.2.tgz
Source17: http://registry.npmjs.org/lazy-cache/-/lazy-cache-0.2.7.tgz
Source18: http://registry.npmjs.org/kind-of/-/kind-of-2.0.1.tgz
Source19: http://registry.npmjs.org/is-extendable/-/is-extendable-0.1.1.tgz
Source20: http://registry.npmjs.org/mixin-object/-/mixin-object-2.0.1.tgz
Source21: http://registry.npmjs.org/for-in/-/for-in-0.1.8.tgz
Source22: sass-loader-6.0.6-registry.npmjs.org.tgz
BuildRequires: nodejs-packaging
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: npm(%{npm_name}) = %{version}
Provides: bundled(npm(sass-loader)) = 6.0.6
Provides: bundled(npm(async)) = 2.6.0
Provides: bundled(npm(lodash)) = 4.17.4
Provides: bundled(npm(lodash.tail)) = 4.1.1
Provides: bundled(npm(pify)) = 3.0.0
Provides: bundled(npm(clone-deep)) = 0.3.0
Provides: bundled(npm(loader-utils)) = 1.1.0
Provides: bundled(npm(kind-of)) = 3.2.2
Provides: bundled(npm(emojis-list)) = 2.1.0
Provides: bundled(npm(is-buffer)) = 1.1.6
Provides: bundled(npm(is-plain-object)) = 2.0.4
Provides: bundled(npm(isobject)) = 3.0.1
Provides: bundled(npm(json5)) = 0.5.1
Provides: bundled(npm(for-own)) = 1.0.0
Provides: bundled(npm(for-in)) = 1.0.2
Provides: bundled(npm(big.js)) = 3.2.0
Provides: bundled(npm(shallow-clone)) = 0.1.2
Provides: bundled(npm(lazy-cache)) = 0.2.7
Provides: bundled(npm(kind-of)) = 2.0.1
Provides: bundled(npm(is-extendable)) = 0.1.1
Provides: bundled(npm(mixin-object)) = 2.0.1
Provides: bundled(npm(for-in)) = 0.1.8
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

%setup -T -q -a 22 -D -n %{npm_cache_dir}

%build
npm install --cache-min Infinity --cache %{npm_cache_dir} --no-optional --global-style true %{npm_name}@%{version}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cd node_modules/sass-loader
cp -pfr CHANGELOG.md LICENSE README.md lib package.json node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pf CHANGELOG.md README.md LICENSE ../../

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%endif

%files
%{nodejs_sitelib}/%{npm_name}

%license LICENSE
%doc CHANGELOG.md
%doc README.md

%changelog
* Tue Nov 07 2017 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 6.0.6-1
- Update nodejs-sass-loader to 6.0.6 (ewoud@kohlvanwijngaarden.nl)

* Tue Feb 28 2017 Dominic Cleal <dominic@cleal.org> 4.1.1-1
- new package built with tito
