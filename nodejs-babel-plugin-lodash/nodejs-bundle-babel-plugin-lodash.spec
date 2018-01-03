%global npm_name babel-plugin-lodash

%{?nodejs_find_provides_and_requires}

Name: nodejs-%{npm_name}
Version: 3.3.2
Release: 1%{?dist}
Summary: Modular Lodash builds without the hassle
License: MIT
Source0: http://registry.npmjs.org/babel-plugin-lodash/-/babel-plugin-lodash-3.3.2.tgz
Source1: http://registry.npmjs.org/babel-types/-/babel-types-6.26.0.tgz
Source2: http://registry.npmjs.org/glob/-/glob-7.1.2.tgz
Source3: http://registry.npmjs.org/lodash/-/lodash-4.17.4.tgz
Source4: http://registry.npmjs.org/require-package-name/-/require-package-name-2.0.1.tgz
Source5: http://registry.npmjs.org/to-fast-properties/-/to-fast-properties-1.0.3.tgz
Source6: http://registry.npmjs.org/inflight/-/inflight-1.0.6.tgz
Source7: http://registry.npmjs.org/fs.realpath/-/fs.realpath-1.0.0.tgz
Source8: http://registry.npmjs.org/esutils/-/esutils-2.0.2.tgz
Source9: http://registry.npmjs.org/babel-helper-module-imports/-/babel-helper-module-imports-7.0.0-beta.3.tgz
Source10: http://registry.npmjs.org/inherits/-/inherits-2.0.3.tgz
Source11: http://registry.npmjs.org/babel-runtime/-/babel-runtime-6.26.0.tgz
Source12: http://registry.npmjs.org/once/-/once-1.4.0.tgz
Source13: http://registry.npmjs.org/path-is-absolute/-/path-is-absolute-1.0.1.tgz
Source14: http://registry.npmjs.org/wrappy/-/wrappy-1.0.2.tgz
Source15: http://registry.npmjs.org/minimatch/-/minimatch-3.0.4.tgz
Source16: http://registry.npmjs.org/babel-types/-/babel-types-7.0.0-beta.3.tgz
Source17: http://registry.npmjs.org/brace-expansion/-/brace-expansion-1.1.8.tgz
Source18: http://registry.npmjs.org/core-js/-/core-js-2.5.3.tgz
Source19: http://registry.npmjs.org/to-fast-properties/-/to-fast-properties-2.0.0.tgz
Source20: http://registry.npmjs.org/concat-map/-/concat-map-0.0.1.tgz
Source21: http://registry.npmjs.org/regenerator-runtime/-/regenerator-runtime-0.11.1.tgz
Source22: http://registry.npmjs.org/balanced-match/-/balanced-match-1.0.0.tgz
Source23: babel-plugin-lodash-3.3.2-registry.npmjs.org.tgz
BuildRequires: nodejs-packaging
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: npm(%{npm_name}) = %{version}
Provides: bundled-npm(babel-plugin-lodash) = 3.3.2
Provides: bundled-npm(babel-types) = 6.26.0
Provides: bundled-npm(glob) = 7.1.2
Provides: bundled-npm(lodash) = 4.17.4
Provides: bundled-npm(require-package-name) = 2.0.1
Provides: bundled-npm(to-fast-properties) = 1.0.3
Provides: bundled-npm(inflight) = 1.0.6
Provides: bundled-npm(fs.realpath) = 1.0.0
Provides: bundled-npm(esutils) = 2.0.2
Provides: bundled-npm(babel-helper-module-imports) = 7.0.0-beta.3
Provides: bundled-npm(inherits) = 2.0.3
Provides: bundled-npm(babel-runtime) = 6.26.0
Provides: bundled-npm(once) = 1.4.0
Provides: bundled-npm(path-is-absolute) = 1.0.1
Provides: bundled-npm(wrappy) = 1.0.2
Provides: bundled-npm(minimatch) = 3.0.4
Provides: bundled-npm(babel-types) = 7.0.0-beta.3
Provides: bundled-npm(brace-expansion) = 1.1.8
Provides: bundled-npm(core-js) = 2.5.3
Provides: bundled-npm(to-fast-properties) = 2.0.0
Provides: bundled-npm(concat-map) = 0.0.1
Provides: bundled-npm(regenerator-runtime) = 0.11.1
Provides: bundled-npm(balanced-match) = 1.0.0
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

%setup -T -q -a 23 -D -n %{npm_cache_dir}

%build
npm install --cache-min Infinity --cache . --no-optional --global-style true %{npm_name}@%{version}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cd node_modules/babel-plugin-lodash
cp -pfr LICENSE README.md lib package.json node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pf README.md LICENSE ../../
# If any binaries are included, symlink them to bindir here

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}

%license LICENSE
%doc README.md

%changelog
* Wed Jan 03 2018 Daniel Lobato Garcia <me@daniellobato.me> 3.3.2-1
- new package built with tito

