# FIXME
# Remove nodejs_symlink_deps if installing bundled module with NPM

%global npm_name babel-loader
%global enable_tests 0

%{?nodejs_find_provides_and_requires}

Name: nodejs-%{npm_name}
Version: 7.1.1
Release: 3%{?dist}
Summary: babel module loader for webpack
License: MIT
URL: https://github.com/babel/babel-loader
Source0: http://registry.npmjs.org/babel-loader/-/babel-loader-7.1.1.tgz
Source1: http://registry.npmjs.org/find-cache-dir/-/find-cache-dir-1.0.0.tgz
Source2: http://registry.npmjs.org/mkdirp/-/mkdirp-0.5.1.tgz
Source3: http://registry.npmjs.org/loader-utils/-/loader-utils-1.1.0.tgz
Source4: http://registry.npmjs.org/pkg-dir/-/pkg-dir-2.0.0.tgz
Source5: http://registry.npmjs.org/commondir/-/commondir-1.0.1.tgz
Source6: http://registry.npmjs.org/minimist/-/minimist-0.0.8.tgz
Source7: http://registry.npmjs.org/emojis-list/-/emojis-list-2.1.0.tgz
Source8: http://registry.npmjs.org/big.js/-/big.js-3.1.3.tgz
Source9: http://registry.npmjs.org/find-up/-/find-up-2.1.0.tgz
Source10: http://registry.npmjs.org/make-dir/-/make-dir-1.0.0.tgz
Source11: http://registry.npmjs.org/json5/-/json5-0.5.1.tgz
Source12: http://registry.npmjs.org/pify/-/pify-2.3.0.tgz
Source13: http://registry.npmjs.org/locate-path/-/locate-path-2.0.0.tgz
Source14: http://registry.npmjs.org/path-exists/-/path-exists-3.0.0.tgz
Source15: http://registry.npmjs.org/p-locate/-/p-locate-2.0.0.tgz
Source16: http://registry.npmjs.org/p-limit/-/p-limit-1.1.0.tgz
Source17: babel-loader-7.1.1-registry.npmjs.org.tgz
BuildRequires: npm
BuildRequires: nodejs-packaging
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: npm(%{npm_name}) = %{version}
Provides: bundled(npm(babel-loader)) = 7.1.1
Provides: bundled(npm(find-cache-dir)) = 1.0.0
Provides: bundled(npm(mkdirp)) = 0.5.1
Provides: bundled(npm(loader-utils)) = 1.1.0
Provides: bundled(npm(pkg-dir)) = 2.0.0
Provides: bundled(npm(commondir)) = 1.0.1
Provides: bundled(npm(minimist)) = 0.0.8
Provides: bundled(npm(emojis-list)) = 2.1.0
Provides: bundled(npm(big.js)) = 3.1.3
Provides: bundled(npm(find-up)) = 2.1.0
Provides: bundled(npm(make-dir)) = 1.0.0
Provides: bundled(npm(json5)) = 0.5.1
Provides: bundled(npm(pify)) = 2.3.0
Provides: bundled(npm(locate-path)) = 2.0.0
Provides: bundled(npm(path-exists)) = 3.0.0
Provides: bundled(npm(p-locate)) = 2.0.0
Provides: bundled(npm(p-limit)) = 1.1.0
AutoReq: no
AutoProv: no


%description
%{summary}

%prep
mkdir npm_cache
for tgz in %{sources}; do
  echo $tgz | grep -q registry.npmjs.org || npm cache add --cache ./npm_cache $tgz
done

%setup -T -q -a 17 -D -n npm_cache

%build
npm install --cache-min Infinity --cache . --global-style true %{npm_name}@%{version}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cd node_modules/babel-loader
cp -pfr CHANGELOG.md README.md lib package.json node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pf CHANGELOG.md README.md ../../
# If any binaries are included, symlink them to bindir here


%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
#$CHECK
%endif

%files
%{nodejs_sitelib}/%{npm_name}

%doc CHANGELOG.md
%doc README.md

%changelog
* Tue Jul 25 2017 Michael Moll <kvedulv@kvedulv.de> 7.1.1-2
- Add missing provides to nodejs-babel-loader (eric.d.helms@gmail.com)

* Tue Jul 25 2017 Michael Moll <kvedulv@kvedulv.de> 7.1.1-1
- Bump babel-loader to 7.1.1 (eric.d.helms@gmail.com)

* Sat Sep 24 2016 Eric D Helms <ericdhelms@gmail.com> 6.2.4-2
- Fix ExclusiveArch for nodejs packages on EL6 (ericdhelms@gmail.com)

* Thu Aug 11 2016 Dominic Cleal <dominic@cleal.org> 6.2.4-1
- new package built with tito
