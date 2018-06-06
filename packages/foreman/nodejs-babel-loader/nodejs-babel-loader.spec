%global npm_name babel-loader

Name: nodejs-%{npm_name}
Version: 7.1.4
Release: 1%{?dist}
Summary: babel module loader for webpack
License: MIT
Group: Development/Libraries
URL: https://github.com/babel/babel-loader
Source0: https://registry.npmjs.org/babel-loader/-/babel-loader-7.1.4.tgz
Source1: https://registry.npmjs.org/loader-utils/-/loader-utils-1.1.0.tgz
Source2: https://registry.npmjs.org/find-cache-dir/-/find-cache-dir-1.0.0.tgz
Source3: https://registry.npmjs.org/mkdirp/-/mkdirp-0.5.1.tgz
Source4: https://registry.npmjs.org/make-dir/-/make-dir-1.3.0.tgz
Source5: https://registry.npmjs.org/emojis-list/-/emojis-list-2.1.0.tgz
Source6: https://registry.npmjs.org/pkg-dir/-/pkg-dir-2.0.0.tgz
Source7: https://registry.npmjs.org/big.js/-/big.js-3.2.0.tgz
Source8: https://registry.npmjs.org/commondir/-/commondir-1.0.1.tgz
Source9: https://registry.npmjs.org/json5/-/json5-0.5.1.tgz
Source10: https://registry.npmjs.org/minimist/-/minimist-0.0.8.tgz
Source11: https://registry.npmjs.org/find-up/-/find-up-2.1.0.tgz
Source12: https://registry.npmjs.org/pify/-/pify-3.0.0.tgz
Source13: https://registry.npmjs.org/locate-path/-/locate-path-2.0.0.tgz
Source14: https://registry.npmjs.org/p-locate/-/p-locate-2.0.0.tgz
Source15: https://registry.npmjs.org/path-exists/-/path-exists-3.0.0.tgz
Source16: https://registry.npmjs.org/p-limit/-/p-limit-1.2.0.tgz
Source17: https://registry.npmjs.org/p-try/-/p-try-1.0.0.tgz
Source18: %{npm_name}-%{version}-registry.npmjs.org.tgz
BuildRequires: nodejs-packaging
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

Provides: npm(%{npm_name}) = %{version}
Provides: bundled(npm(babel-loader)) = 7.1.4
Provides: bundled(npm(big.js)) = 3.2.0
Provides: bundled(npm(commondir)) = 1.0.1
Provides: bundled(npm(emojis-list)) = 2.1.0
Provides: bundled(npm(find-cache-dir)) = 1.0.0
Provides: bundled(npm(find-up)) = 2.1.0
Provides: bundled(npm(json5)) = 0.5.1
Provides: bundled(npm(loader-utils)) = 1.1.0
Provides: bundled(npm(locate-path)) = 2.0.0
Provides: bundled(npm(make-dir)) = 1.3.0
Provides: bundled(npm(minimist)) = 0.0.8
Provides: bundled(npm(mkdirp)) = 0.5.1
Provides: bundled(npm(p-limit)) = 1.2.0
Provides: bundled(npm(p-locate)) = 2.0.0
Provides: bundled(npm(p-try)) = 1.0.0
Provides: bundled(npm(path-exists)) = 3.0.0
Provides: bundled(npm(pify)) = 3.0.0
Provides: bundled(npm(pkg-dir)) = 2.0.0
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
%setup -T -q -a 18 -D -n %{npm_cache_dir}

%build
npm install --cache-min Infinity --cache %{npm_cache_dir} --no-shrinkwrap --no-optional --global-style true %{npm_name}@%{version}

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/node_modules %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/lib %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr node_modules/%{npm_name}/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%clean
rm -rf %{buildroot} %{npm_cache_dir}

%files
%{nodejs_sitelib}/%{npm_name}
%license node_modules/%{npm_name}/LICENSE
%doc node_modules/%{npm_name}/CHANGELOG.md
%doc node_modules/%{npm_name}/README.md

%changelog
* Wed Jun 06 2018 Eric D. Helms <ericdhelms@gmail.com> 7.1.4-1
- Update to 7.1.4

* Tue Jul 25 2017 Michael Moll <kvedulv@kvedulv.de> 7.1.1-2
- Add missing provides to nodejs-babel-loader (eric.d.helms@gmail.com)

* Tue Jul 25 2017 Michael Moll <kvedulv@kvedulv.de> 7.1.1-1
- Bump babel-loader to 7.1.1 (eric.d.helms@gmail.com)

* Sat Sep 24 2016 Eric D Helms <ericdhelms@gmail.com> 6.2.4-2
- Fix ExclusiveArch for nodejs packages on EL6 (ericdhelms@gmail.com)

* Thu Aug 11 2016 Dominic Cleal <dominic@cleal.org> 6.2.4-1
- new package built with tito
